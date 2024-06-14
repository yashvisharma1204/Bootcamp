### Comparison Operators

1. **Equal (=)**: Tests for equality between two expressions.
   - Example: `SELECT * FROM table WHERE column1 = 10;`

2. **Not Equal (<> or !=)**: Tests for inequality between two expressions.
   - Example: `SELECT * FROM table WHERE column1 <> 10;`

3. **Greater Than (>)**: Tests if one expression is greater than another.
   - Example: `SELECT * FROM table WHERE column1 > 10;`

4. **Less Than (<)**: Tests if one expression is less than another.
   - Example: `SELECT * FROM table WHERE column1 < 10;`

5. **Greater Than or Equal To (>=)**: Tests if one expression is greater than or equal to another.
   - Example: `SELECT * FROM table WHERE column1 >= 10;`

6. **Less Than or Equal To (<=)**: Tests if one expression is less than or equal to another.
   - Example: `SELECT * FROM table WHERE column1 <= 10;`

### Logical Operators

1. **AND**: Combines two or more Boolean expressions and returns true if all expressions are true.
   - Example: `SELECT * FROM table WHERE column1 > 5 AND column2 < 10;`

2. **OR**: Combines two or more Boolean expressions and returns true if at least one expression is true.
   - Example: `SELECT * FROM table WHERE column1 = 10 OR column2 = 20;`

3. **NOT**: Reverses the logical state of its operand (negation).
   - Example: `SELECT * FROM table WHERE NOT column1 = 10;`

### Arithmetic Operators

1. **+ (Addition)**: Adds two numeric values.
   - Example: `SELECT column1 + column2 AS sum_result FROM table;`

2. **- (Subtraction)**: Subtracts one numeric value from another.
   - Example: `SELECT column1 - column2 AS difference FROM table;`

3. **\* (Multiplication)**: Multiplies two numeric values.
   - Example: `SELECT column1 * column2 AS product FROM table;`

4. **/ (Division)**: Divides one numeric value by another.
   - Example: `SELECT column1 / column2 AS division_result FROM table;`

5. **% (Modulo)**: Returns the remainder of a division operation.
   - Example: `SELECT 10 % 3 AS modulo_result;`

### String Operators

1. **|| (Concatenation)**: Concatenates two or more strings.
   - Example: `SELECT 'Hello ' || 'World' AS greeting;`

2. **LIKE**: Performs pattern matching using wildcards.
   - Example: `SELECT * FROM table WHERE column1 LIKE 'A%';`

3. **IN**: Specifies multiple values for a column.
   - Example: `SELECT * FROM table WHERE column1 IN ('value1', 'value2', 'value3');`

4. **BETWEEN**: Specifies a range to test against.
   - Example: `SELECT * FROM table WHERE column1 BETWEEN 10 AND 20;`
