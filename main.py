import cx_Oracle

username = 'VladDB'
password = 'Vlad03042001'
database = 'localhost:1521/xe'

connection = cx_Oracle.connect(username, password, database)

cursor = connection.cursor()

print("Кількість забитих голів кожною командою.\n")
query1 ="""
SELECT
    TEAM, sum(GOALS)
        FROM (SELECT "EPL".HOME_TEAM as TEAM, sum("EPL".HOME_GOALS) as GOALS from EPL 
        GROUP BY "EPL".HOME_TEAM
        UNION
        SELECT "EPL".AWAY_TEAM as TEAM, sum("EPL".AWAY_GOALS) as GOALS from EPL 
        GROUP BY "EPL".AWAY_TEAM)
GROUP BY TEAM
ORDER BY sum(GOALS) DESC;
"""
cursor.execute(query1)

for row in cursor:
    print(row)



print("Кількість нічиїх, перемог та поразок.\n")
query2 = """
SELECT count(*) FROM "EPL"
GROUP BY "EPL".RESULTS;
"""
cursor.execute(query2)

for row in cursor:
    print(row)



print("Кількість нічиїх в кожному сезоні.\n")
query3 = """
SELECT "EPL".SEASON, count(*) FROM "EPL"
WHERE "EPL".RESULTS = 'H'
GROUP BY "EPL".SEASON
ORDER BY "EPL".SEASON;
"""
cursor.execute(query3)



for row in cursor:
    print(row)


cursor.close()
connection.close()