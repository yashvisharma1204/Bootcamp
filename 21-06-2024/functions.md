# Functions
## 2. Functions

**Definition:**
A function is a subprogram that performs actions and returns a result. SQL functions can return a single value or a table.

### Scalar Functions

**Definition:**
A scalar function returns a single value.

**Syntax:**
```sql
CREATE FUNCTION function_name (@parameter datatype)
RETURNS return_datatype
AS
BEGIN
    DECLARE @result return_datatype;
    -- SQL statements
    RETURN @result;
END;
```

**Example:**
Suppose we want to create a function to calculate the annual salary of an employee.

**Query:**
```sql
CREATE FUNCTION CalculateAnnualSalary (@Salary DECIMAL(10, 2))
RETURNS DECIMAL(10, 2)
AS
BEGIN
    RETURN @Salary * 12;
END;
```

### Table-Valued Functions

**Definition:**
A table-valued function returns a table.

**Syntax:**
```sql
CREATE FUNCTION function_name (@parameter datatype)
RETURNS TABLE
AS
RETURN
    (SELECT ... FROM ... WHERE ...);
```

**Example:**
Suppose we want to create a function to get employees by department.

**Query:**
```sql
CREATE FUNCTION GetEmployees (@DepartmentID INT)
RETURNS TABLE
AS
RETURN
    (SELECT EmployeeID, Name, Salary
     FROM Employees
     WHERE DepartmentID = @DepartmentID);
```

### Using Functions

**Example:**
Using the `CalculateAnnualSalary` function.
```sql
SELECT Name, dbo.CalculateAnnualSalary(Salary) AS AnnualSalary
FROM Employees;
```

**Example:**
Using the `GetEmployees` function.
```sql
SELECT * FROM dbo.GetEmployees(1);
```

