import csv

with open('jnumca2k17.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Email address'] == 'msinha034@gmail.com':
            print(row['Email address'] ,row ['Nickname'])
