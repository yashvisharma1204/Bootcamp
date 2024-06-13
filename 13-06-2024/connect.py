import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # replace with your MySQL username
            password='',  # replace with your MySQL password
            database='mynewdatabase'  # replace with your database name
        )
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


connect_to_mysql()
