import csv
import cx_Oracle
username = '"VladDB"'
password = 'Vlad03042001'
database = 'localhost:1521/xe'
connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()


csv_file="results.csv"


with open(csv_file, newline='') as file:
    reader = csv.DictReader(file)
    i=1

    try:
        for row in reader:
            home_team = row['home_team']
            away_team = row['away_team']
            home_goals = int(float(row['home_goals']))
            away_goals = int(float(row['away_goals']))
            result = row['result']
            season = row['season']
            

            insert = """INSERT INTO Match ( TEAM_HOME_NAME, TEAM_AWAY_NAME, MATCH_HOME_GOALS, MATCH_AWAY_GOALS, MATCH_RESULTS, SEASON_PERIOD)values (:home_team, :away_team, :home_goals, :away_goals, :result, :season)"""
            cursor.execute(insert, home_team=home_team, away_team=away_team, home_goals=home_goals, away_goals=away_goals, result=result, season=season)
            


            i += 1

    except:
        print(f"Error in line: {i}")
        raise

connection.commit()
cursor.close()
