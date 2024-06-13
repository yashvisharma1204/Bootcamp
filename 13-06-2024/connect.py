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
        
        if connection.is_connected():
            print("Connected to MySQL database")
            
            # Create a cursor object
            cursor = connection.cursor()
            # Execute a query
            cursor.execute("SELECT * FROM student_info")
            # Fetch and print all rows from the last executed statement
            rows = cursor.fetchall()
            
            print("Total number of rows in users table: ", cursor.rowcount)
            for row in rows:
                print(row)
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


connect_to_mysql()
