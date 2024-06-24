# Cursor
## 3. Cursors

**Definition:**
A cursor is a database object used to retrieve, manipulate, and navigate through a result set row by row.

### Declaring a Cursor

**Syntax:**
```sql
DECLARE cursor_name CURSOR FOR
SELECT_statement;
```

### Opening a Cursor

**Syntax:**
```sql
OPEN cursor_name;
```

### Fetching Data from a Cursor

**Syntax:**
```sql
FETCH NEXT FROM cursor_name INTO variables;
```

### Closing and Deallocating a Cursor

**Syntax:**
```sql
CLOSE cursor_name;
DEALLOCATE cursor_name;
```

### Example

**Example:**
Suppose we want to use a cursor to iterate through all employees and increase their salary by 10%.

**Query:**
```sql
DECLARE @EmployeeID INT, @Salary DECIMAL(10, 2);

DECLARE employee_cursor CURSOR FOR
SELECT EmployeeID, Salary
FROM Employees;

OPEN employee_cursor;

FETCH NEXT FROM employee_cursor INTO @EmployeeID, @Salary;

WHILE @@FETCH_STATUS = 0
BEGIN
    UPDATE Employees
    SET Salary = @Salary * 1.1
    WHERE EmployeeID = @EmployeeID;

    FETCH NEXT FROM employee_cursor INTO @EmployeeID, @Salary;
END;

CLOSE employee_cursor;
DEALLOCATE employee_cursor;
```
