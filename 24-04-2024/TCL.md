# TCL (Transaction Control Language) Commands 

## 1. Introduction to TCL

**Definition:**
Transaction Control Language (TCL) commands are used to manage transactions in a database. A transaction is a sequence of one or more SQL operations treated as a single unit of work. TCL commands help ensure the integrity of data by controlling how transactions are executed and saved.

## 2. Types of TCL Commands

### a. COMMIT

**Definition:**
The COMMIT command is used to save all changes made in the current transaction to the database.

**Syntax:**
```sql
COMMIT;
```

**Example:**
Suppose we perform an update operation and then commit the transaction.
```sql
UPDATE Employees
SET Salary = Salary * 1.1
WHERE DepartmentID = 1;

COMMIT;
```

### b. ROLLBACK

**Definition:**
The ROLLBACK command is used to undo changes made in the current transaction. This command reverts the database to the state it was in before the transaction began.

**Syntax:**
```sql
ROLLBACK;
```

**Example:**
Suppose we perform an update operation but decide to roll back the changes.
```sql
UPDATE Employees
SET Salary = Salary * 1.1
WHERE DepartmentID = 1;

ROLLBACK;
```

### c. SAVEPOINT

**Definition:**
The SAVEPOINT command sets a point within a transaction to which you can later roll back. This allows partial rollbacks within a transaction.

**Syntax:**
```sql
SAVEPOINT savepoint_name;
```

**Example:**
Suppose we perform multiple operations and set a savepoint to roll back to if needed.
```sql
UPDATE Employees
SET Salary = Salary * 1.1
WHERE DepartmentID = 1;

SAVEPOINT Savepoint1;

UPDATE Employees
SET Salary = Salary * 1.2
WHERE DepartmentID = 2;

-- Rollback to Savepoint1 if needed
ROLLBACK TO Savepoint1;

-- Changes to DepartmentID 1 will be committed
COMMIT;
```

### d. RELEASE SAVEPOINT

**Definition:**
The RELEASE SAVEPOINT command removes a savepoint that you have created. After a savepoint is released, you can no longer roll back to that savepoint.

**Syntax:**
```sql
RELEASE SAVEPOINT savepoint_name;
```

**Example:**
```sql
SAVEPOINT Savepoint1;

UPDATE Employees
SET Salary = Salary * 1.1
WHERE DepartmentID = 1;

RELEASE SAVEPOINT Savepoint1;

-- The savepoint Savepoint1 is now released and cannot be used for a rollback
COMMIT;
```

## 3. Using TCL Commands in a Transaction

### Example Transaction

**Scenario:**
Suppose we have a transaction involving multiple operations on the `Employees` table. We will use TCL commands to manage the transaction.

```sql
BEGIN TRANSACTION;

-- Update salaries for HR department
UPDATE Employees
SET Salary = Salary * 1.1
WHERE DepartmentID = 1;

-- Set a savepoint after the first update
SAVEPOINT HR_Update;

-- Update salaries for IT department
UPDATE Employees
SET Salary = Salary * 1.2
WHERE DepartmentID = 2;

-- Decide to roll back to the HR_Update savepoint
ROLLBACK TO HR_Update;

-- Commit the transaction (only changes to HR department will be committed)
COMMIT;
```

**Explanation:**
- The transaction begins with `BEGIN TRANSACTION`.
- Salaries for the HR department are updated.
- A savepoint named `HR_Update` is set.
- Salaries for the IT department are updated.
- The changes made to the IT department are rolled back to the savepoint `HR_Update`.
- The transaction is committed, saving only the changes made to the HR department.

