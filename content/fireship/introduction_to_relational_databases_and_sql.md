---
title: Introduction to Relational Databases and SQL
videoId: Cz3WcZLRaWc
---

From: [[fireship]] <br/> 

Relational databases using [[introduction_to_relational_databases_and_sql | SQL]] are widely popular, with a recent poll indicating nearly two-thirds of viewers prefer SQL as their go-to database technology, despite it being 40-year-old tech <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article will cover essential information about [[getting_started_with_mysql | MySQL]], a prominent open-source relational database <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Why SQL is Popular

SQL powers major platforms such as:
*   Content Management Systems like WordPress <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>
*   E-commerce platforms like Shopify <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>
*   Social media giants like Twitter <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>

This guide will take a hands-on approach by recreating Airbnb's database, which uses [[getting_started_with_mysql | MySQL]] in real life <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. In the process, you'll learn:
*   Why SQL is so popular <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>
*   How to install and interact with the database using modern tooling like VS Code <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>
*   Essential syntax for Create, Read, Update, and Delete (CRUD) operations <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>
*   How to model and [[working_with_sql_joins_and_relationships | join relational data]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>

## History of Relational Databases and SQL

The concept of relational databases began about 50 years ago with Ted Codd, who authored "A Relational Model of Data for Large Shared Data Banks" <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Prior to this paper, databases were network-based or hierarchical <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Codd's paper outlined how a relational model could reduce duplication and redundancy, fundamentally changing the approach to [[comparison_of_sql_and_nosql_databases | databases]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

A few years later, Donald Chamberlin and Raymond Boyce developed Structured Query Language (SQL) based on Codd's paper <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. SQL is still the language used today to interact with data in a wide variety of relational databases <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### SQL and Object-Relational Mapping (ORMs)

Most developers using relational databases do not write raw SQL code <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Instead, they often use libraries that perform Object-Relational Mapping (ORMs) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. ORMs allow interaction with relational databases using an object-oriented programming language of choice, such as:
*   JavaScript with Sequelize <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>
*   Python with SQLAlchemy <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>
*   Ruby on Rails with Active Record <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>

While ORMs boost productivity by abstracting raw SQL, understanding how raw SQL works is crucial for comprehending the underlying mechanisms <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## Relational Database Management System (RDBMS)

A relational database management system (RDBMS) consists of two main components:
1.  **The Database Itself:** A collection of tables, where data is organized into columns and rows, similar to an Excel spreadsheet <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
2.  **A Language:** Used to manipulate and read data in the database, most often a variation of Structured Query Language (SQL) <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

Besides [[getting_started_with_mysql | MySQL]], other popular database options include PostgreSQL, SQL Server, SQLite, and distributed tools like CockroachDB <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Data Modeling: The Airbnb Example

Data modeling involves visualizing and defining data relationships. Using a tool like DrawSQL, one can see that each box represents a database table, and lines between them represent relationships like one-to-one or one-to-many <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

### Database Schema

The database schema is a blueprint that defines rules and constraints within the database <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Tables:** Act as dictionaries where keys represent columns and values represent data types <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Data Types:** Vary between SQL databases but generally represent numbers and strings. Examples in [[getting_started_with_mysql | MySQL]] include:
    *   `INT` for integers <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>
    *   `FLOAT` for floating-point numbers <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>
    *   `VARCHAR` for small strings (with a specified maximum length) <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>
    *   `TEXT` for longer strings of unspecified size <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>
    Choosing the correct data type helps optimize database size and performance <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Constraints:** Special rules applied to columns, ensuring data integrity. Common constraints include:
    *   `NOT NULL`: Prevents a column from storing a null value <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   `UNIQUE`: Ensures each value in a column is unique <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
    *   `PRIMARY KEY`: A combination of `NOT NULL` and `UNIQUE`, ensuring every row can be uniquely identified. This is essential for building relationships <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
    *   `AUTO_INCREMENT`: Automatically generates unique IDs, starting from 1 and incrementing <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

### Normalized Data Structure

Relational databases aim for a normalized data structure, where there is minimal data duplication between tables <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Each table represents a unique entity, storing only a reference (like an ID) to related information in other tables <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. This concept, laid out by Ted Codd, ensures entities are organized into their smallest "normal form" <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. For example, instead of storing user data and room data in a `bookings` table, separate `users` and `rooms` tables are created, and they are then [[working_with_sql_joins_and_relationships | joined]] back together with `bookings` when needed <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Getting Hands-On with [[getting_started_with_mysql | MySQL]]

### Installation
To install [[getting_started_with_mysql | MySQL]]:
*   **Windows:** Download and run the installer from the [[getting_started_with_mysql | MySQL]] website. Select "[[getting_started_with_mysql | MySQL]] Server" and follow default settings, creating a password to remember <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Mac:** Use the installer or Homebrew <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
After installation, the `mysql` command should be accessible from the command line <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

### Connecting to [[getting_started_with_mysql | MySQL]]
*   **Command Line:** Run `mysql -u [username] -p` (if you set a password) <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **VS Code SQL Tools Extension:** Install the extension and driver for [[getting_started_with_mysql | MySQL]]. Create a new connection, adding the database name, username, and password <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This extension allows storing connection details, visualizing the database, and viewing query history <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## Basic SQL Operations (CRUD)

SQL statements perform actions and typically end with a semicolon <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. SQL keywords are often written in uppercase by convention, though they are not case-sensitive <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

### 1. Create Database
To create a new database:
```sql
CREATE DATABASE airbnb; <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>
```
Verify creation:
```sql
SHOW DATABASES; <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>
```

### 2. Create Table
To add a table to the database, for example, a `users` table:
```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
); <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>
```
*   `id`: `INT` (whole numbers), `PRIMARY KEY` (unique, not null), `AUTO_INCREMENT` (generated automatically) <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   `email`: `VARCHAR(255)` (string up to 255 chars), `NOT NULL`, `UNIQUE` <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   `bio`: `TEXT` (unspecified size string) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   `country`: `VARCHAR(2)` (2-character string) <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### 3. Insert Data (Rows)
To add data into a table:
```sql
INSERT INTO users (email, bio, country) VALUES
('homer@gmail.com', 'Bio 1', 'US'),
('marge@gmail.com', 'Bio 2', 'CA'),
('bart@gmail.com', 'Bio 3', 'MX'); <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>
```
The `id` field is omitted because `AUTO_INCREMENT` will generate it <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. Multiple rows can be inserted by separating them with commas <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

### 4. Read Data (Query)
The `SELECT` statement reads data <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.
*   **Select all columns and rows:**
    ```sql
    SELECT * FROM users; <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>
    ```
*   **Select specific columns:**
    ```sql
    SELECT email, id FROM users; <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>
    ```
*   **Limit rows:**
    ```sql
    SELECT * FROM users LIMIT 2; <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>
    ```
*   **Order rows:**
    ```sql
    SELECT * FROM users ORDER BY id DESC; <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>
    ```
*   **Filter rows with `WHERE` clause:**
    ```sql
    SELECT * FROM users WHERE country = 'US'; <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>
    SELECT * FROM users WHERE country = 'US' AND id > 1; <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>
    ```
*   **Pattern matching with `LIKE`:**
    ```sql
    SELECT * FROM users WHERE email LIKE 'h%'; <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>
    ```
    (Finds emails starting with 'h').

### Database Index
To speed up data retrieval, especially for large datasets, an index can be created <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. An index acts like a lookup table, helping the database find keywords without scanning the entire dataset <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. It comes at the cost of slower write operations and additional memory <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
```sql
CREATE INDEX email_index ON users (email); <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>
```

## [[working_with_sql_joins_and_relationships | Working with SQL Joins and Relationships]]

### One-to-Many Relationship
An example is a user having many rooms. This is modeled by creating a `rooms` table with an `owner_id` column that references the `id` of the `users` table <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

```sql
CREATE TABLE rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    street VARCHAR(255),
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES users(id)
); <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>
```
*   `FOREIGN KEY (owner_id) REFERENCES users(id)`: This constraint links `owner_id` in `rooms` to `id` in `users`. It ensures data integrity, preventing deletion of users who own rooms <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

### Types of Joins
When [[working_with_sql_joins_and_relationships | joining]] tables (e.g., `users` as the left table and `rooms` as the right), you match IDs between them <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. The join type determines which data is returned based on corresponding relationships <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.

*   **INNER JOIN:** Returns only rows where there is a match in *both* tables <a class="yt-timestamp" data-t="00:14:55">[00:14:55]</a>.
    ```sql
    SELECT *
    FROM users
    INNER JOIN rooms
    ON rooms.owner_id = users.id; <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>
    ```
*   **LEFT JOIN:** Returns all rows from the *left* table, and the matching rows from the *right* table. If no match, the right side's columns will be `NULL` <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
    ```sql
    SELECT *
    FROM users
    LEFT JOIN rooms
    ON rooms.owner_id = users.id; <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>
    ```
*   **RIGHT JOIN:** The opposite of a left join; returns all rows from the *right* table and matching rows from the *left* table <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.
*   **FULL OUTER JOIN:** (Not supported in [[getting_started_with_mysql | MySQL]]) Returns all rows from both tables, with `NULL`s where there's no match <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

You can rename conflicting column names in the result set using the `AS` operator <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.
```sql
SELECT
    users.id AS user_id,
    rooms.id AS room_id,
    users.email,
    rooms.street
FROM users
INNER JOIN rooms
ON rooms.owner_id = users.id; <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>
```

### Many-to-Many Relationship
For a many-to-many relationship (e.g., a user can book many rooms, and a room can be booked by many users), an intermediate or "bookings" table is created <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. This table contains foreign keys referencing both related tables.
```sql
CREATE TABLE bookings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    check_in_time DATETIME,
    guest_id INT,
    room_id INT,
    FOREIGN KEY (guest_id) REFERENCES users(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
); <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>
```
This allows for complex relationships, enabling queries like getting all rooms a user has booked by [[working_with_sql_joins_and_relationships | joining]] `rooms` to `bookings` and filtering by `guest_id`, or getting a history of guests in a room by [[working_with_sql_joins_and_relationships | joining]] `users` to `bookings` and filtering by `room_id` <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.

## ![[danger_zone_callout.png|30]] Danger Zone: `DROP` Statement

The `DROP` statement allows you to delete data, including individual tables or an entire database <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. Use with extreme caution as it can lead to permanent data loss <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.
```sql
-- To delete a table
DROP TABLE table_name;

-- To delete an entire database
DROP DATABASE database_name;
```