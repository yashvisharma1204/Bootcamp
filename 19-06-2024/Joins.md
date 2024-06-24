# SQL JOINS Detailed Notes

## 1. INNER JOIN

**Definition:**
The INNER JOIN keyword selects records that have matching values in both tables.

**Syntax:**
```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

**Example:**
Suppose we have two tables, `Employees` and `Departments`:

- Employees
  ```
  EmployeeID | Name       | DepartmentID
  -------------------------------------
  1          | Alice      | 1
  2          | Bob        | 2
  3          | Charlie    | 1
  ```

- Departments
  ```
  DepartmentID | DepartmentName
  ----------------------------
  1            | HR
  2            | IT
  ```

**Query:**
```sql
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
INNER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;
```

**Result:**
```
Name    | DepartmentName
------------------------
Alice   | HR
Bob     | IT
Charlie | HR
```

## 2. LEFT JOIN (or LEFT OUTER JOIN)

**Definition:**
The LEFT JOIN keyword returns all records from the left table (table1), and the matched records from the right table (table2). The result is NULL from the right side if there is no match.

**Syntax:**
```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

**Example:**
Using the same `Employees` and `Departments` tables:

**Query:**
```sql
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
LEFT JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;
```

**Result:**
```
Name    | DepartmentName
------------------------
Alice   | HR
Bob     | IT
Charlie | HR
```

## 3. RIGHT JOIN (or RIGHT OUTER JOIN)

**Definition:**
The RIGHT JOIN keyword returns all records from the right table (table2), and the matched records from the left table (table1). The result is NULL from the left side when there is no match.

**Syntax:**
```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

**Example:**
Using the same `Employees` and `Departments` tables but adding a new department:

- Departments (Updated)
  ```
  DepartmentID | DepartmentName
  ----------------------------
  1            | HR
  2            | IT
  3            | Finance
  ```

**Query:**
```sql
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
RIGHT JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;
```

**Result:**
```
Name    | DepartmentName
------------------------
Alice   | HR
Bob     | IT
NULL    | Finance
Charlie | HR
```

## 4. FULL JOIN (or FULL OUTER JOIN)

**Definition:**
The FULL JOIN keyword returns all records when there is a match in either left (table1) or right (table2) table records. The result is NULL from the side where there is no match.

**Syntax:**
```sql
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;
```

**Example:**
Using the updated `Employees` and `Departments` tables:

**Query:**
```sql
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
FULL OUTER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;
```

**Result:**
```
Name    | DepartmentName
------------------------
Alice   | HR
Bob     | IT
Charlie | HR
NULL    | Finance
```

## 5. CROSS JOIN

**Definition:**
The CROSS JOIN keyword returns the Cartesian product of the two tables. This means it returns all possible combinations of rows from the two tables.

**Syntax:**
```sql
SELECT columns
FROM table1
CROSS JOIN table2;
```

**Example:**
Using the same `Employees` and `Departments` tables:

**Query:**
```sql
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
CROSS JOIN Departments;
```

**Result:**
```
Name    | DepartmentName
------------------------
Alice   | HR
Alice   | IT
Alice   | Finance
Bob     | HR
Bob     | IT
Bob     | Finance
Charlie | HR
Charlie | IT
Charlie | Finance
```

## 6. SELF JOIN

**Definition:**
A self join is a regular join but the table is joined with itself.

**Syntax:**
```sql
SELECT a.column, b.column
FROM table a, table b
WHERE condition;
```

**Example:**
Suppose we have a `Employees` table with a `ManagerID` that references the `EmployeeID` of the manager:

- Employees (with ManagerID)
  ```
  EmployeeID | Name       | ManagerID
  -----------------------------------
  1          | Alice      | NULL
  2          | Bob        | 1
  3          | Charlie    | 1
  ```

**Query:**
```sql
SELECT e1.Name AS Employee, e2.Name AS Manager
FROM Employees e1
LEFT JOIN Employees e2
ON e1.ManagerID = e2.EmployeeID;
```

**Result:**
```
Employee | Manager
-------------------
Alice    | NULL
Bob      | Alice
Charlie  | Alice
```
