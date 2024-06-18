## Built-in Functions

### Definition and Purpose
- **Built-in Functions** in SQL are predefined functions provided by SQL databases to perform various operations on data. These functions can manipulate data, perform calculations, format data, and more. They are essential for simplifying complex queries and enhancing data processing capabilities.

### Categories and Examples

- **Aggregate Functions**: Used to perform calculations on a set of values and return a single value.
  - `COUNT()`: Counts the number of rows.
    ```sql
    SELECT COUNT(*) FROM table_name;
    ```
  - `SUM()`: Calculates the sum of a numeric column.
    ```sql
    SELECT SUM(column_name) FROM table_name;
    ```
  - `AVG()`: Computes the average of a numeric column.
    ```sql
    SELECT AVG(column_name) FROM table_name;
    ```
  - `MAX()` and `MIN()`: Returns the maximum and minimum values in a column.
    ```sql
    SELECT MAX(column_name) FROM table_name;
    ```

- **String Functions**: Manipulate string data.
  - `CONCAT()`: Concatenates two or more strings.
    ```sql
    SELECT CONCAT(first_name, ' ', last_name) FROM table_name;
    ```
  - `SUBSTRING()`: Extracts a substring from a string.
    ```sql
    SELECT SUBSTRING(column_name, start, length) FROM table_name;
    ```
  - `UPPER()` and `LOWER()`: Converts a string to upper or lower case.
    ```sql
    SELECT UPPER(column_name) FROM table_name;
    ```

- **Date and Time Functions**: Handle date and time data.
  - `NOW()`: Returns the current date and time.
    ```sql
    SELECT NOW();
    ```
  - `DATEADD()`: Adds a specified time interval to a date.
    ```sql
    SELECT DATEADD(day, 7, column_name) FROM table_name;
    ```
  - `DATEDIFF()`: Calculates the difference between two dates.
    ```sql
    SELECT DATEDIFF(day, start_date, end_date) FROM table_name;
    ```

- **Numeric Functions**: Perform operations on numeric data.
  - `ROUND()`: Rounds a number to a specified number of decimal places.
    ```sql
    SELECT ROUND(column_name, 2) FROM table_name;
    ```
  - `ABS()`: Returns the absolute value of a number.
    ```sql
    SELECT ABS(column_name) FROM table_name;
    ```