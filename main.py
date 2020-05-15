import cx_Oracle

username = '"VladDB"'
password = 'Vlad03042001'
database = 'localhost:1521/xe'

connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

print("Кількість голів, які забили команди за всі сезони.\n")
query1 ="""
SELECT
    TEAM, sum(GOALS)
        FROM (SELECT MATCH.TEAM_HOME_NAME as TEAM, sum(MATCH.MATCH_HOME_GOALS) as GOALS from MATCH 
        GROUP BY MATCH.TEAM_HOME_NAME
        UNION
        SELECT MATCH.TEAM_AWAY_NAME as TEAM, sum(MATCH.MATCH_AWAY_GOALS) as GOALS from MATCH 
        GROUP BY MATCH.TEAM_AWAY_NAME)
GROUP BY TEAM
ORDER BY sum(GOALS) DESC
"""
cursor.execute(query1)

for row in cursor:
    print(row)



print("Кількість нічиїх, перемог та поразок.\n")
query2 = """
SELECT MATCH.MATCH_RESULTS, count(*) FROM MATCH
GROUP BY MATCH.MATCH_RESULTS
"""
cursor.execute(query2)

for row in cursor:
    print(row)



print("Загальна кількість нічиїх усіх команд за кожен сезон.\n")
query3 = """
SELECT MATCH.SEASON_PERIOD, count(*) FROM MATCH
WHERE MATCH.MATCH_RESULTS = 'D'
GROUP BY MATCH.SEASON_PERIOD
ORDER BY MATCH.SEASON_PERIOD
"""
cursor.execute(query3)



for row in cursor:
    print(row)


cursor.close()
connection.close()
