import cx_Oracle
import csv

username = '"VladDB"'
password = 'Vlad03042001'
database = 'localhost/xe'

connection = cx_Oracle.connect(username, password, database)
cur = connection.cursor()

tables = [ 'team_home_name', 'team_away_name', 'match_home_goals', 'match_away_goals', 'match_results', 'season_period' ]

for table in tables:
    with open(table + '.csv', 'w', newline='') as csv_file:
        query = 'SELECT * FROM ' + table
        cursor.execute(query)
        row = cursor.fetchone()

        title = tuple(map(lambda x: x[0], cursor.description))
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(title)


        while row:
            csv_writer.writerow(row)
            row = cursor.fetchone()

cursor.close()
connection.close()
