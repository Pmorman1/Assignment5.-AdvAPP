# Student Name: Precious Morman
# Assignment Number: Lab#5
# Due Date: 04/15/2025
# Purpose: This program creates a SQLite database, stores temperature readings from a file, and calculates the average temperature for Sunday and Thursday. 
#It demonstrates reading from a file, inserting data into a database, and running basic SQL queries in Python.
# List Specific resources used to complete the assignment:
#SQLite3 Python documentation: https://docs.python.org/3/library/sqlite3.html
#Received help from a friend and tutor in understanding the database setup and query structure,
#but all code, variable names, and comments were written by me.

import sqlite3

# Establish a connection to the SQLite database and create it if it doesn't exist
conn = sqlite3.connect('temperature_readings.db')
cursor = conn.cursor()

# Define and create the table structure
cursor.execute('''
CREATE TABLE IF NOT EXISTS temperature_data (
    ID INTEGER PRIMARY KEY,
    Day_Of_Week TEXT,
    Temperature_Value REAL
)
''')

# Open the input file (Assignment5input.txt) and insert each data entry into the database
# Assuming the file 'Assignment5input.txt' has two columns: day_of_week and temperature_value separated by space
with open('Assignment5input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:  # Check if the line is not empty
            try:
                day_of_week, temperature_value = line.split()
                temperature_value = float(temperature_value)
                
                cursor.execute('''
                INSERT INTO temperature_data (Day_Of_Week, Temperature_Value)
                VALUES (?, ?)
                ''', (day_of_week, temperature_value))
            except ValueError:
                # Skip lines that don't have the expected format
                print(f"Skipping invalid line: {line}")

# Commit the changes to the database
conn.commit()

# Query the database to calculate the average temperature for Sunday and Thursday
cursor.execute('''
SELECT AVG(Temperature_Value) FROM temperature_data WHERE Day_Of_Week = 'Sunday'
''')
sunday_avg = cursor.fetchone()[0]

cursor.execute('''
SELECT AVG(Temperature_Value) FROM temperature_data WHERE Day_Of_Week = 'Thursday'
''')
thursday_avg = cursor.fetchone()[0]

# Output the average temperatures for Sunday and Thursday
print(f"Average temperature for Sunday: {sunday_avg}")
print(f"Average temperature for Thursday: {thursday_avg}")

# Close the connection to the database
conn.close()


