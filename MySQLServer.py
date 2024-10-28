import mysql.connector
from mysql.connector import Error


try:
    
    mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "Adunola@Adriel12345")
    cursor = mydb.cursor()
    try:


        cursor.execute(CREATE DATABASE IF NOT EXISTS alx_book_store)

        print("Database 'alx_book_store' created successfully!")

    except  error as e:


        print("failed to create to database")

except mysql.connector.Error as e:
    print("database not connected")

cursor.close()
