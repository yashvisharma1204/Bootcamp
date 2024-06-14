### SQL Data Types with Examples

SQL data types define the kind of data that can be stored in a table column. Below are some common data types with brief descriptions and examples:

#### Numeric Data Types

1. **INT**
   - **Description**: Stores whole numbers.
   - **Example**:
     ```sql
     CREATE TABLE employees (
         id INT(11),
         name VARCHAR(50)
     );
     ```

2. **SMALLINT**
   - **Description**: Stores small-range whole numbers.
   - **Example**:
     ```sql
     CREATE TABLE sensors (
         sensor_id SMALLINT,
         sensor_value INT
     );
     ```

3. **BIGINT**
   - **Description**: Stores large-range whole numbers.
   - **Example**:
     ```sql
     CREATE TABLE transactions (
         trans_id BIGINT,
         amount DECIMAL(10, 2)
     );
     ```

4. **FLOAT**
   - **Description**: Stores floating-point numbers with precision.
   - **Example**:
     ```sql
     CREATE TABLE measurements (
         measure_id INT,
         value FLOAT(7, 2)
     );
     ```

5. **DOUBLE**
   - **Description**: Stores double precision floating-point numbers.
   - **Example**:
     ```sql
     CREATE TABLE calculations (
         calc_id INT,
         result DOUBLE(15, 5)
     );
     ```

6. **DECIMAL**
   - **Description**: Stores exact numeric values with precision.
   - **Example**:
     ```sql
     CREATE TABLE products (
         product_id INT,
         price DECIMAL(10, 2)
     );
     ```

#### Date and Time Data Types

1. **DATE**
   - **Description**: Stores date values in `YYYY-MM-DD` format.
   - **Example**:
     ```sql
     CREATE TABLE events (
         event_id INT,
         event_date DATE
     );
     ```

2. **DATETIME**
   - **Description**: Stores date and time values in `YYYY-MM-DD hh:mm:ss` format.
   - **Example**:
     ```sql
     CREATE TABLE appointments (
         appt_id INT,
         appt_time DATETIME
     );
     ```

3. **TIMESTAMP**
   - **Description**: Stores timestamp values, used for automatic updates.
   - **Example**:
     ```sql
     CREATE TABLE logs (
         log_id INT,
         log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );
     ```

4. **TIME**
   - **Description**: Stores time values in `hh:mm:ss` format.
   - **Example**:
     ```sql
     CREATE TABLE schedules (
         schedule_id INT,
         start_time TIME,
         end_time TIME
     );
     ```

5. **YEAR**
   - **Description**: Stores year values in `YYYY` format.
   - **Example**:
     ```sql
     CREATE TABLE history (
         record_id INT,
         year YEAR
     );
     ```

#### String Data Types

1. **CHAR**
   - **Description**: Fixed-length string.
   - **Example**:
     ```sql
     CREATE TABLE codes (
         code_id INT,
         code CHAR(10)
     );
     ```

2. **VARCHAR**
   - **Description**: Variable-length string.
   - **Example**:
     ```sql
     CREATE TABLE users (
         user_id INT,
         username VARCHAR(255)
     );
     ```

3. **TEXT**
   - **Description**: Large variable-length string.
   - **Example**:
     ```sql
     CREATE TABLE articles (
         article_id INT,
         content TEXT
     );
     ```

