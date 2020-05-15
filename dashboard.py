import cx_Oracle
import re
import chart_studio
from plotly import graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dash

chart_studio.tools.set_credentials_file(username='VladSavustianenko', api_key='Zo5X31Vyy4kxvLnWN6Xa')

def fileId_from_url(url):
    raw_fileId = re.findall("~[A-z.0-9]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

username = '"VladDB"'
password = 'Vlad03042001'
database = 'localhost:1521/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

cursor.execute("""
SELECT
    TEAM, sum(GOALS)
        FROM (SELECT MATCH.TEAM_HOME_NAME as TEAM, sum(MATCH.MATCH_HOME_GOALS) as GOALS from MATCH 
        GROUP BY MATCH.TEAM_HOME_NAME
        UNION
        SELECT MATCH.TEAM_AWAY_NAME as TEAM, sum(MATCH.MATCH_AWAY_GOALS) as GOALS from MATCH 
        GROUP BY MATCH.TEAM_AWAY_NAME)
GROUP BY TEAM
ORDER BY sum(GOALS) DESC
""")

team = []
goals = []


for row in cursor:
    print("Team:", row[0],"Goals :",row[1])
    team += [row[1]]
    goals += [row[0]]

data = [go.Bar(
             x=goals,
             y=team
      )]

layout = go.Layout(
    title = 'All goals of teams',
    xaxis=dict(
        title='Teams ',
        titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7d7d7d'
        )
    ),
    yaxis=dict(
        title='Count of goals',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7d7d7d'
        )
    )
)

fig = go.Figure(data=data, layout=layout)

track_duration_artist = py.plot(fig, filename='duration -artist')

cursor.execute( """
SELECT MATCH.MATCH_RESULTS, count(*) FROM MATCH
GROUP BY MATCH.MATCH_RESULTS
""")
artist = []
percent = []

for row in cursor:
    artist.append(row[0])
    percent.append(row[1])

pie_data = go.Pie(
        labels=artist,
        values=percent,
        title="Away, home and draw for all teams in all seasons"
    )
artist_percent = py.plot([pie_data], filename='artist-percent')


cursor.execute( """
SELECT MATCH.SEASON_PERIOD, count(*) FROM MATCH
WHERE MATCH.MATCH_RESULTS = 'D'
GROUP BY MATCH.SEASON_PERIOD
ORDER BY MATCH.SEASON_PERIOD
""")

draw = []
count = []

for row in cursor:
    print("chart_place", row[0], " popular: ", row[1])
    draw += [row[0]]
    count += [row[1]]

chart_place_popular = go.Scatter(
    x=draw,
    y=count,
    mode='lines+markers'
)
data = [chart_place_popular]
chart_place_popular_url = py.plot(data, filename='popular_chart_place')


my_dboard = dash.Dashboard()
track_duration_artist_id = fileId_from_url(track_duration_artist)
artist_percent_id = fileId_from_url(artist_percent)
chart_place_popular_id = fileId_from_url(chart_place_popular_url)

box_1= {
    'type': 'box',
    'boxType': 'plot',
    'fileId': track_duration_artist_id,
    'title': 'Запит 1: Кількість голів, які забили команди за всі сезони.'
}
box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': artist_percent_id,
    'title': 'Запит 2: Кількість нічиїх, перемог та поразок.'

}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': chart_place_popular_id,
    'title': 'Запит 3: Загальна кількість нічиїх усіх команд за кожен сезон.'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'right', 2)

py.dashboard_ops.upload(my_dboard, 'Billboard1')


cursor.close()
connection.close()
