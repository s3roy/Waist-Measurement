import csv
from models import Measurement
from flask_mysqldb import MySQL


def import_csv_to_db(mysql: MySQL):
    with open('data\measurements.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # skip header row
        for row in csv_reader:
            measurement = Measurement(
                height=float(row[0]),
                weight=float(row[1]),
                age=round(float(row[2])),
                waist=float(row[3])
            )
            mysql.connection.session.add(measurement)
        mysql.connection.session.commit()
