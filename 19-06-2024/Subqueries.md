# SQL Subqueries Detailed Notes

## 1. Introduction to Subqueries

**Definition:**
A subquery is a query nested inside another query, such as SELECT, INSERT, UPDATE, or DELETE. Subqueries are also known as inner queries or nested queries. They can be used to perform operations that would otherwise require multiple steps in a single query.

**Syntax:**
```sql
SELECT column1, column2, ...
FROM table1
WHERE column = (SELECT column FROM table2 WHERE condition);
```

## 2. Types of Subqueries

### a. Single-Row Subquery

**Definition:**
A subquery that returns only one row.

**Example:**
Suppose we have two tables, `Employees` and `Departments`:

- Employees
  ```
  EmployeeID | Name       | DepartmentID | Salary
  ---------------------------------------------
  1          | Alice      | 1            | 60000
  2          | Bob        | 2            | 70000
  3          | Charlie    | 1            | 55000
  ```

- Departments
  ```
  DepartmentID | DepartmentName
  ----------------------------
  1            | HR
  2            | IT
  ```

**Query:**
Find the employee with the highest salary.
```sql
SELECT Name
FROM Employees
WHERE Salary = (SELECT MAX(Salary) FROM Employees);
```

**Result:**
```
Name
----
Bob
```

### b. Multiple-Row Subquery

**Definition:**
A subquery that returns more than one row.

**Example:**
**Query:**
Find employees who work in the HR department.
```sql
SELECT Name
FROM Employees
WHERE DepartmentID = (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'HR');
```

**Result:**
```
Name
----
Alice
Charlie
```

### c. Multiple-Column Subquery

**Definition:**
A subquery that returns more than one column.

**Example:**
**Query:**
Find the department ID and average salary of each department.
```sql
SELECT DepartmentID, AVG(Salary)
FROM Employees
GROUP BY DepartmentID;
```

### d. Correlated Subquery

**Definition:**
A subquery that references columns from the outer query. It is evaluated once for each row processed by the outer query.

**Example:**
**Query:**
Find employees whose salary is above the average salary of their respective departments.
```sql
SELECT Name, Salary
FROM Employees e1
WHERE Salary > (SELECT AVG(Salary) FROM Employees e2 WHERE e1.DepartmentID = e2.DepartmentID);
```

**Result:**
```
Name   | Salary
--------------
Alice  | 60000
Bob    | 70000
```

## 3. Using Subqueries in Different SQL Statements

### a. Subqueries in SELECT Statement

**Example:**
**Query:**
Find the names of employees and their department names.
```sql
SELECT Name, (SELECT DepartmentName FROM Departments WHERE DepartmentID = Employees.DepartmentID) AS DepartmentName
FROM Employees;
```

**Result:**
```
Name    | DepartmentName
------------------------
Alice   | HR
Bob     | IT
Charlie | HR
```

### b. Subqueries in INSERT Statement

**Example:**
**Query:**
Insert a new employee with the department ID of the 'Finance' department.
```sql
INSERT INTO Employees (Name, DepartmentID, Salary)
VALUES ('David', (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'Finance'), 65000);
```

### c. Subqueries in UPDATE Statement

**Example:**
**Query:**
Update the salary of employees who work in the 'HR' department.
```sql
UPDATE Employees
SET Salary = Salary * 1.1
WHERE DepartmentID = (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'HR');
```

### d. Subqueries in DELETE Statement

**Example:**
**Query:**
Delete employees who work in the 'IT' department.
```sql
DELETE FROM Employees
WHERE DepartmentID = (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'IT');
```

## 4. Subqueries in the FROM Clause

**Example:**
**Query:**
Find the average salary by department using a subquery in the FROM clause.
```sql
SELECT DepartmentID, AVG(Salary)
FROM (SELECT DepartmentID, Salary FROM Employees) AS Subquery
GROUP BY DepartmentID;
```

## 5. Subqueries with EXISTS

**Definition:**
The EXISTS keyword is used to test for the existence of any record in a subquery.

**Example:**
**Query:**
Find departments that have at least one employee.
```sql
SELECT DepartmentName
FROM Departments d
WHERE EXISTS (SELECT 1 FROM Employees e WHERE e.DepartmentID = d.DepartmentID);
```

**Result:**
```
DepartmentName
--------------
HR
IT
```

