# Waist-Measurement
Steps to run the application in your local machine:

#Database
For the database I have used mysql make sure mysql is installed in your system.
Then open mysql in your command line and create the database " measurements_db"
You could then import and create the tables by using the create_tables.sql file.

#Frontend
For the frontend make sure nodejs is installed on your system.
Then, run the command npm install to install all the required packages.
To start the client side or the frontend run the command npm start.

#Backend
For the backend make sure python is installed in your system.
To populate the database with the csv file data run the file csv_to_db.py using the command python csv_to_db.py
Then you could start the back end by using flask run.

The database configuration credentials must be filled in the config.py file.
