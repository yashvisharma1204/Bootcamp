### Day 1: Setup and Basic Connectivity

#### Objective:
- Set up your development environment
- Establish basic connectivity between Python and MySQL

### 1. Install MySQL Server and MySQL Workbench

#### MySQL Server:
- **Download MySQL Server** from the official MySQL website
#### MySQL Workbench:
- **Download MySQL Workbench** from the official website

### 2. Set Up MySQL Database

#### Create a Database:
- Open **MySQL Workbench** and connect to your MySQL server using the root account.
- Create a new database by executing:
  ```sql
  CREATE DATABASE mynewdatabase;
  ```

#### Create a Table:
- Switch to the newly created database:
  ```sql
  USE mynewdatabase;
  ```
- Create a simple table:
  ```sql
    CREATE TABLE student_info(
	st_id int(3) primary key,
	st_name varchar(30) not null,
    st_address varchar(300) not null,
    st_phone_no bigint not null,
    st_major varchar(50)
    );

  ```
- Insert some sample data:
  ```sql
    INSERT INTO student_info (st_id, st_name, st_address, st_phone_no, st_major) VALUES
    (1, 'Aarav Sharma', '123 MG Road, Delhi', 9876543210, 'Computer Science'),
    (2, 'Vivaan Gupta', '456 Lal Bagh, Mumbai', 9876543211, 'Mechanical Engineering'),
    (3, 'Aditya Patel', '789 Sector 21, Noida', 9876543212, 'Electrical Engineering'),
    (4, 'Arjun Singh', '101 Indira Nagar, Lucknow', 9876543213, 'Civil Engineering'),
    (5, 'Ananya Mehta', '202 Banjara Hills, Hyderabad', 9876543214, 'Information Technology'),
    (6, 'Diya Kapoor', '303 Whitefield, Bangalore', 9876543215, 'Chemical Engineering'),
    (7, 'Ishaan Desai', '404 Marine Drive, Mumbai', 9876543216, 'Biotechnology'),
    (8, 'Kavya Nair', '505 Salt Lake, Kolkata', 9876543217, 'Aerospace Engineering'),
    (9, 'Laksh Jain', '606 Anna Nagar, Chennai', 9876543218, 'Environmental Science'),
    (10, 'Meera Roy', '707 Gariahat, Kolkata', 9876543219, 'Physics');
  ```

### 3. Install Required Python Packages

#### Install `mysql-connector-python`:
- Open your terminal or command prompt.
- Run the following command to install the MySQL connector for Python:
  ```sh
  pip install mysql-connector-python
  ```

### 4. Basic Python Script to Connect to MySQL

#### Writing the Script:
- Create a new Python file, e.g., `mysql_connect.py`.

#### Connect to MySQL:
- Write a Python script to connect to the MySQL database and fetch data from the `student_info` table.

```python
import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # replace with your MySQL username
            password='your_password',  # replace with your MySQL password
            database='mydatabase'  # replace with your database name
        )
        
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


connect_to_mysql()
```

#### Explanation:
- **Import mysql.connector and Error**: These imports are necessary to use the MySQL connector and handle potential errors.
- **connect_to_mysql function**:
  - Establishes a connection to the MySQL database using `mysql.connector.connect()`. The `host`, `user`, `password`, and `database` parameters need to be replaced with your own MySQL credentials.
  - Checks if the connection is established.
  - Handles any potential errors using a `try-except` block.
  - Ensures the connection is closed properly in the `finally` block.

