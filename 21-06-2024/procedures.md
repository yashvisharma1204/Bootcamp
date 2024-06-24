# SQL Procedures
## 1. Stored Procedures

**Definition:**
A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again. Stored procedures can accept parameters and return results.

### Creating a Stored Procedure

**Syntax:**
```sql
CREATE PROCEDURE procedure_name AS
BEGIN
    sql_statement;
END;
```

**Example:**
Suppose we want to create a stored procedure to get the details of employees from a specific department.

**Query:**
```sql
CREATE PROCEDURE GetEmployeesByDepartment @DepartmentID INT
AS
BEGIN
    SELECT EmployeeID, Name, Salary
    FROM Employees
    WHERE DepartmentID = @DepartmentID;
END;
```

### Executing a Stored Procedure

**Syntax:**
```sql
EXEC procedure_name parameters;
```

**Example:**
```sql
EXEC GetEmployeesByDepartment @DepartmentID = 1;
```
