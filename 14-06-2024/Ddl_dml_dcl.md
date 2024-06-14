## Introduction
In SQL (Structured Query Language), commands are categorized into three main types: Data Definition Language (DDL), Data Manipulation Language (DML), and Data Control Language (DCL). Each type of command serves a specific purpose in managing and manipulating databases. Here is a detailed explanation of each:

### Data Definition Language (DDL)

DDL commands are used to define and manage the structure of database objects such as tables, indexes, and schemas. These commands affect the schema or structure of the database.

#### Common DDL Commands:

1. **CREATE**: Used to create database objects like tables, indexes, and databases.
   - **Example**: 
     ```sql
     CREATE TABLE students (
         student_id INT PRIMARY KEY,
         name VARCHAR(50),
         age INT
     );
     ```

2. **ALTER**: Used to modify the structure of an existing database object. It can add, delete, or modify columns in a table.
   - **Example**:
     ```sql
     ALTER TABLE students ADD COLUMN email VARCHAR(100);
     ```

3. **DROP**: Used to delete objects from the database, such as tables, indexes, or entire databases.
   - **Example**:
     ```sql
     DROP TABLE students;
     ```

4. **TRUNCATE**: Used to delete all rows from a table without removing the table structure.
   - **Example**:
     ```sql
     TRUNCATE TABLE students;
     ```

5. **RENAME**: Used to rename database objects.
   - **Example**:
     ```sql
     ALTER TABLE students RENAME TO alumni;
     ```

### Data Manipulation Language (DML)

DML commands are used to retrieve, insert, update, and delete data in database tables. These commands deal with the manipulation of data within the existing schema of the database.

#### Common DML Commands:

1. **SELECT**: Used to query and retrieve data from a database.
   - **Example**:
     ```sql
     SELECT * FROM students;
     ```

2. **INSERT**: Used to add new rows of data to a table.
   - **Example**:
     ```sql
     INSERT INTO students (student_id, name, age) VALUES (1, 'John Doe', 22);
     ```

3. **UPDATE**: Used to modify existing data within a table.
   - **Example**:
     ```sql
     UPDATE students SET age = 23 WHERE student_id = 1;
     ```

4. **DELETE**: Used to remove existing rows from a table.
   - **Example**:
     ```sql
     DELETE FROM students WHERE student_id = 1;
     ```

### Data Control Language (DCL)

DCL commands are used to control access to data within the database. These commands manage the permissions and access levels of users and roles.

#### Common DCL Commands:

1. **GRANT**: Used to give users access privileges to the database.
   - **Example**:
     ```sql
     GRANT SELECT, INSERT ON students TO 'username';
     ```

2. **REVOKE**: Used to remove access privileges from users.
   - **Example**:
     ```sql
     REVOKE SELECT, INSERT ON students FROM 'username';
     ```
