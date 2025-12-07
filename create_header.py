import csv

rows = [['ID', 'Date', 'Description', 'amount']]

with open('database.csv', 'w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(rows)