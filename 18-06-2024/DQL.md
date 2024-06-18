# Notes on DQL and Built-in Functions of SQL

## 1. Data Query Language (DQL)

### Definition and Purpose
- **Data Query Language (DQL)** is a subset of SQL used primarily for querying data from the database. The primary function of DQL is to retrieve data based on specific criteria. The most common and fundamental DQL command is `SELECT`.
- DQL allows users to perform complex queries with various clauses such as `WHERE`, `ORDER BY`, `GROUP BY`, and `HAVING`. This enables filtering, sorting, grouping, and aggregating data to extract meaningful insights.

### Key Features
- **SELECT Statement**: The core of DQL, used to specify the columns to retrieve and the tables to query from.
  ```sql
  SELECT column1, column2 FROM table_name;
  ```
- **Filtering with WHERE**: Allows conditional retrieval of data.
  ```sql
  SELECT column1, column2 FROM table_name WHERE condition;
  ```
- **Sorting with ORDER BY**: Enables sorting of the result set in ascending or descending order.
  ```sql
  SELECT column1, column2 FROM table_name ORDER BY column1 ASC;
  ```
- **Grouping with GROUP BY**: Aggregates data based on one or more columns.
  ```sql
  SELECT column1, COUNT(*) FROM table_name GROUP BY column1;
  ```
- **Aggregating with HAVING**: Filters groups based on aggregate conditions.
  ```sql
  SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > 1;
  ```

