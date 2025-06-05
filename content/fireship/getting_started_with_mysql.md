---
title: Getting Started with MySQL
videoId: Cz3WcZLRaWc
---

From: [[fireship]] <br/> 

## Introduction to MySQL

[[introduction_to_relational_databases_and_sql | Relational databases using SQL]] are widely popular in the tech industry <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A recent poll showed that nearly two-thirds of viewers prefer SQL as their go-to database <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Despite being over 40 years old, SQL remains dominant, even with billions invested in technologies attempting to displace it <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

MySQL is an open-source database that powers major systems like WordPress <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, Shopify <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, and Twitter <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. This guide takes a hands-on approach by recreating Airbnb's database, which uses MySQL in real life <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

### Why SQL is Popular

*   **Historical Impact**: The foundation for modern relational databases was laid by Ted Codd's legendary 1970 paper, "A Relational Model of Data for Large Shared Data Banks" <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Prior to this, databases were network-based or hierarchical <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Codd's paper demonstrated how a [[introduction_to_relational_databases_and_sql | relational model]] could reduce data duplication and redundancy <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Development of SQL**: A few years later, Donald Chamberlin and Raymond Boyce developed [[introduction_to_relational_databases_and_sql | Structured Query Language (SQL)]] based on Codd's paper, which is still used today to interact with [[introduction_to_relational_databases_and_sql | relational databases]] <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

### Object-Relational Mapping (ORM)

Most developers using [[introduction_to_relational_databases_and_sql | relational databases]] don't write raw SQL code <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. Instead, they use Object-Relational Mapping (ORM) libraries, which allow interaction with relational databases using object-oriented programming languages <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Examples include Sequelize for JavaScript, SQLAlchemy for Python, and Active Record for Ruby on Rails <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. While ORMs boost productivity, understanding raw SQL is crucial for comprehending their underlying mechanics <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Other Relational Database Options

Beyond MySQL, other [[database_options_for_web_applications | popular database options]] include PostgreSQL, SQL Server, SQLite, and distributed tools like CockroachDB for scaling high-traffic applications <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Understanding Relational Databases

A [[introduction_to_relational_databases_and_sql | relational database management system]] (RDBMS) consists of two main components <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>:
1.  **Database**: A collection of tables <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. Each table organizes data into columns and rows, similar to a spreadsheet <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  **Language**: A language, typically a variation of SQL, used to manipulate and read data within the database <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Database Schema and Data Integrity

The database schema is a blueprint defining the rules and [[data_types_and_constraints_in_mysql | constraints]] within the database <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. In a table, each column has a name and a [[data_types_and_constraints_in_mysql | data type]] <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

Common [[data_types_and_constraints_in_mysql | data types]] in MySQL include:
*   `INT`: For whole numbers <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   `FLOAT`: For floating-point numbers <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   `VARCHAR`: For small strings with a specified maximum length (e.g., `VARCHAR(255)`) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   `TEXT`: For longer strings of unspecified size <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

Choosing the correct [[data_types_and_constraints_in_mysql | data type]] optimizes database size and performance <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### Constraints

A column can also have special [[data_types_and_constraints_in_mysql | constraints]] <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>:
*   **NOT NULL**: Ensures a column cannot store a null value <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **UNIQUE**: Requires each value in a column to be unique <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **[[data_types_and_constraints_in_mysql | Primary Key]]**: A combination of `NOT NULL` and `UNIQUE`, ensuring every row in the table can be uniquely identified <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   **[[data_types_and_constraints_in_mysql | Auto Increment]]**: Automatically generates an ID for new rows, starting from 1 and incrementing <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   **[[data_types_and_constraints_in_mysql | Foreign Key]]**: References a [[data_types_and_constraints_in_mysql | primary key]] in a different table, enforcing relationships and data integrity <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This prevents deletion of data that holds a relationship (e.g., a user with associated rooms cannot be deleted if a foreign key constraint is set) <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

### Normalized Data Structure

A normalized data structure minimizes data duplication between tables by organizing every entity into its smallest normal form <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. For example, instead of storing user data within a bookings table, it's better to separate users and rooms into their own entities, then [[creating_and_managing_tables_in_mysql | join]] them with bookings when needed <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## Installing MySQL

### Windows Installation

1.  Go to the MySQL website and download the installer <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
2.  Select "MySQL Server" as the only required component for this tutorial <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
3.  Stick with default settings <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
4.  Create and remember a password, as it will be needed later to connect to the database <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
5.  The installer will configure the system <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

### Mac Installation

*   An installer is available on the MySQL website, similar to the Windows process <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   Alternatively, use Homebrew <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

After installation, the `mysql` command should be accessible from the command line <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

## Interacting with MySQL

### Command Line Interface

To access the database from the command line:
```bash
mysql -u [your_username] -p
```
The `-u` flag is for username, and `-p` is for password (you'll be prompted to enter it) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

### VS Code SQL Tools Extension

For a more developer-friendly experience, install the SQL Tools extension for VS Code <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
1.  Install the extension and the MySQL driver <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.
2.  Create a new connection, using default settings, but ensure to add the database name, username, and password <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
3.  Test the connection <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

The extension allows storing connection details, visualizing the database, and viewing query history <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. SQL comments are created using a double dash (`--`) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. The VS Code extension allows running individual statements by adding `@block` after a comment <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.

## Essential SQL Statements

SQL statements are pieces of code that perform actions, ending with a semicolon (`;`) <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. SQL keywords (like `CREATE`, `TABLE`, `SELECT`) are typically written in uppercase by convention, though they are not case-sensitive <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### Creating a Database

To create a new database:
```sql
CREATE DATABASE airbnb;
```
Verify its creation:
```sql
SHOW DATABASES;
```
This will list all databases <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### [[creating_and_managing_tables_in_mysql | Creating a Table]]

To add the first table (e.g., `users`):
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
);
```
This statement defines columns with their [[data_types_and_constraints_in_mysql | data types]] and [[data_types_and_constraints_in_mysql | constraints]] <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

### [[creating_and_managing_tables_in_mysql | Inserting Data]]

To add rows into a table (e.g., `users`):
```sql
INSERT INTO users (email, bio, country) VALUES
('homer@simpsons.com', 'D’oh!', 'US'),
('marge@simpsons.com', 'Hmmmm', 'US');
```
The order of values must match the order of columns specified <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. The `id` column is omitted here because it has the [[data_types_and_constraints_in_mysql | `AUTO_INCREMENT` constraint]] <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

### [[creating_and_managing_tables_in_mysql | Reading Data (SELECT)]]

The [[creating_and_managing_tables_in_mysql | `SELECT` statement]] reads data <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

*   **Select all columns and rows**:
    ```sql
    SELECT * FROM users;
    ```
    This returns the entire table <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.

*   **Select specific columns**:
    ```sql
    SELECT email, id FROM users;
    ```
    Columns are separated by commas <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

*   **Limit number of rows**:
    ```sql
    SELECT * FROM users LIMIT 2;
    ```
    The `LIMIT` keyword restricts the number of rows returned <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

*   **Order results**:
    ```sql
    SELECT * FROM users ORDER BY id DESC; -- Or ASC for ascending
    ```
    The `ORDER BY` clause specifies a column and direction (`ASC` or `DESC`) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

*   **Filter with `WHERE` clause**:
    ```sql
    SELECT * FROM users WHERE country = 'US';
    ```
    The `WHERE` clause applies conditional logic <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. Conditions can be chained using `AND` or `OR` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

*   **Pattern matching with `LIKE`**:
    ```sql
    SELECT * FROM users WHERE email LIKE 'h%';
    ```
    The `LIKE` operator is used for pattern matching (e.g., emails starting with 'h') <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

### Indexing for Performance

For faster data retrieval, especially with `LIKE` queries on large datasets, an index is essential <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. An index is a lookup table that helps the database find keywords without scanning the entire dataset <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. It comes at the cost of slower write operations and increased memory usage <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

```sql
CREATE INDEX email_index ON users (email);
```

### [[creating_and_managing_tables_in_mysql | Joins]] for Relational Data

When dealing with relationships, such as a user having many rooms (a one-to-many relationship), [[creating_and_managing_tables_in_mysql | joins]] are used <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

First, create the `rooms` table with a [[data_types_and_constraints_in_mysql | foreign key]] referencing the `users` table:
```sql
CREATE TABLE rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    owner_id INT,
    address VARCHAR(255),
    price INT,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);
```
Then, insert some data:
```sql
INSERT INTO rooms (owner_id, address, price) VALUES
(1, '123 Main St', 100),
(1, '456 Oak Ave', 150),
(1, '789 Pine Ln', 200),
(1, '101 Elm Dr', 120);
```

There are four main types of [[creating_and_managing_tables_in_mysql | joins]]:

1.  **INNER JOIN**: Returns only rows where there's a match in both tables <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
    ```sql
    SELECT * FROM users INNER JOIN rooms ON rooms.owner_id = users.id;
    ```
    This returns users who own rooms, with their respective room data <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

2.  **LEFT JOIN**: Returns all rows from the "left" table (first table in `FROM` clause) and matching rows from the "right" table. If no match, NULLs are returned for right table columns <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.
    ```sql
    SELECT * FROM users LEFT JOIN rooms ON rooms.owner_id = users.id;
    ```
    This would return all users, including those without associated rooms (room data would be NULL) <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.

3.  **RIGHT JOIN**: The opposite of LEFT JOIN; returns all rows from the "right" table and matching rows from the "left" table <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

4.  **FULL OUTER JOIN**: Returns all rows when there is a match in either left or right table. (Note: MySQL does not natively support `FULL OUTER JOIN`, but it can be simulated with `UNION` of `LEFT JOIN` and `RIGHT JOIN`) <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

To rename conflicting column names in a join's result set, use the `AS` operator:
```sql
SELECT users.id AS user_id, rooms.id AS room_id, users.email, rooms.address
FROM users
INNER JOIN rooms ON rooms.owner_id = users.id;
```

### Complex Relationships with Intermediate Tables

To model complex relationships, like a user booking a room from another user, an intermediate table is used (e.g., `bookings` or `reservations`) <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. This table would have its own ID, a check-in time, and two [[data_types_and_constraints_in_mysql | foreign keys]]: `guest_id` (referencing users) and `room_id` (referencing rooms) <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

```sql
CREATE TABLE bookings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    check_in_time DATETIME,
    guest_id INT,
    room_id INT,
    FOREIGN KEY (guest_id) REFERENCES users(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);
```

This allows querying, for example:
*   All rooms a user has booked by joining `rooms` to `bookings` and filtering by `guest_id` <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
*   A history of guests who stayed in a room by joining `users` to `bookings` and filtering by `room_id` <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.

### Deleting Data (DROP)

The `DROP` statement deletes data, such as an individual table or an entire database <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. Use with extreme caution as it can lead to permanent data loss <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

```sql
DROP TABLE users; -- Deletes the users table
DROP DATABASE airbnb; -- Deletes the entire airbnb database
```