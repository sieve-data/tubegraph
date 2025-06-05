---
title: Working with SQL Joins and Relationships
videoId: Cz3WcZLRaWc
---

From: [[fireship]] <br/> 

[[introduction_to_relational_databases_and_sql | Relational databases using SQL]] are a dominant technology, with a recent poll indicating that nearly two-thirds of viewers prefer SQL as their go-to database, despite it being 40-year-old technology [00:00:00]. Billions of dollars have been invested in disruptive technologies attempting to displace SQL, but it remains prevalent [00:00:10].

## What is MySQL?
MySQL is an open-source database that powers large-scale content management systems like WordPress, e-commerce platforms such as Shopify, and social media giants like Twitter [00:00:16].

### Why SQL is Popular
SQL's enduring popularity stems from its ability to model and join relational data effectively [00:00:30]. This article will explore how to interact with SQL databases, essential syntax for data manipulation (CRUD), and, crucially, how to model and join relational data using MySQL [00:00:33].

## The Genesis of Relational Databases
The concept of relational databases was pioneered by Ted Codd, author of the legendary 1970 paper, "A Relational Model of Data for Large Shared Data Banks" [00:00:50]. Before this paper, databases were primarily network-based or hierarchical [00:00:58]. Codd's paper outlined how a relational model could significantly reduce data duplication and redundancy, fundamentally altering the approach to database design [00:01:04].

A few years later, Donald Chamberlin and Raymond Boyce developed Structured Query Language (SQL) based on Codd's work [00:01:10]. SQL remains the primary language for interacting with data in a wide variety of relational databases today [00:01:19].

### Object-Relational Mapping (ORM)
While SQL is powerful, many developers using relational databases do not write raw SQL code directly [00:01:25]. Instead, they often use libraries that perform Object-Relational Mapping (ORM) [00:01:31]. ORMs allow developers to work with relational databases using their preferred object-oriented programming language, such as Sequelize for JavaScript, SQLAlchemy for Python, or Active Record in [[web_development_with_ruby_on_rails | Ruby on Rails]] [00:01:40]. ORMs can significantly boost productivity, but understanding raw SQL provides insight into the underlying operations [00:01:46].

## Understanding a Relational Database Management System (RDBMS)
An RDBMS consists of two main components [00:02:01]:
1.  **The Database Itself**: A collection of tables where data is organized into columns and rows, similar to a spreadsheet [00:02:06].
2.  **A Language**: Most often a variation of Structured Query Language (SQL), used to manipulate and read data within the database [00:02:17].

Popular RDBMS options include MySQL, PostgreSQL, SQL Server, SQLite, and tools like CockroachDB for scalable cloud applications [00:02:24].

## Database Schema and Data Modeling
A database schema acts as a blueprint, defining the rules and constraints within the database [00:02:57]. Tools like DrawSQL can help visualize and model data relationships [00:02:37].

### Tables and Columns
Each "box" in a schema diagram represents a database table [00:02:48]. Inside a table, a dictionary-like structure defines columns (keys) and their corresponding data types (values) [00:03:03].

### Data Types
Choosing the correct data type optimizes database size and performance [00:03:32]. Common MySQL data types include [00:03:19]:
*   `INT`: For whole numbers.
*   `FLOAT`: For floating-point numbers.
*   `VARCHAR`: For small strings, requiring a maximum length argument (e.g., `VARCHAR(255)`) [00:03:33].
*   `TEXT`: For longer strings of unspecified size [00:03:29].

### Constraints
Columns can have special constraints that enforce data integrity [00:03:40]:
*   `NOT NULL`: Ensures a column cannot store a null value [00:03:42].
*   `UNIQUE`: Ensures each value in a column must be unique [00:03:45].
*   `PRIMARY KEY`: A special constraint that implies `NOT NULL` and `UNIQUE`. It identifies a unique row in a table [00:03:50].
*   `AUTO_INCREMENT`: Tells the database to automatically create an ID for a column, incrementing it with each new row [00:08:21].

### Normalized Data Structure
A [[normalized_data_models_and_document_joining_in_firestore | normalized data structure]] minimizes data duplication by organizing every entity into its smallest normal form [00:04:26]. For example, in an Airbnb model, a `rooms` table doesn't store user information directly; instead, it references a `user_id` [00:04:20]. If a `bookings` table needs information about a user and a room, it uses references (IDs) to the separate `users` and `rooms` tables, rather than duplicating the entire user and room data within `bookings` [00:04:36]. This is analogous to breaking down a car into individual parts and then joining them back together when needed [00:04:52]. This concept was laid out by Ted Codd over half a century ago [00:04:32].

## Establishing Relationships with Foreign Keys
Relationships between tables are crucial for [[firestore_data_modeling_techniques | data modeling techniques]].
Lines in a schema diagram represent different relationships, such as one-to-one or one-to-many [00:02:51].

### One-to-Many Relationship
A common relationship is one-to-many, such as a user having many rooms [00:13:08]. This is established using a **foreign key** [00:13:28].
For example, a `rooms` table would have an `owner_id` column, which is a foreign key referencing the `id` of a user in the `users` table [00:13:17].

```sql
CREATE TABLE rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    owner_id INT,
    -- other room columns
    FOREIGN KEY (owner_id) REFERENCES users(id)
);
```
Setting up a foreign key constraint ensures data integrity by preventing the deletion of data that has existing relationships (e.g., you cannot delete a user who owns rooms) [00:13:45].

### Many-to-Many Relationship
More complex relationships, like a user booking many rooms, or a room having many past guests, are modeled using a **third intermediate table** [00:16:08]. This intermediate table, often called a "junction" or "join" table (e.g., `reservations` or `bookings`), holds foreign keys to both related entities [00:16:12].

For instance, a `bookings` table would contain a `guest_id` (user ID) and a `room_id`, both as foreign keys, along with other booking-specific details like `check_in_time` [00:16:20]. This allows complex queries where a user has reserved many rooms *through* the bookings table, or a room has hosted many guests *through* the bookings table [00:16:27].

## SQL Query Operations (CRUD)

### Creating Tables (`CREATE TABLE`)
Tables are created using the `CREATE TABLE` statement, specifying column names, data types, and constraints [00:07:06].

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
);
```
SQL keywords are often capitalized by convention, though they are not case-sensitive [00:07:23].

### Inserting Data (`INSERT INTO`)
Data is added to tables using the `INSERT INTO` statement, specifying columns and their corresponding values [00:09:31]. The order of values must match the order of columns [00:09:41].

```sql
INSERT INTO users (email, bio, country) VALUES
('john@example.com', 'Bio for John', 'US'),
('jane@example.com', 'Bio for Jane', 'CA');
```

### Reading Data (`SELECT`)
The `SELECT` statement retrieves data from the database [00:10:30].
*   `SELECT * FROM users;` returns all columns and rows from the `users` table [00:10:38].
*   `SELECT email, id FROM users;` filters for specific columns [00:10:48].

### Filtering and Ordering Data
*   `LIMIT`: Restricts the number of rows returned [00:11:01].
    `SELECT * FROM users LIMIT 2;`
*   `ORDER BY`: Orders results by a specified column in ascending (`ASC`) or descending (`DESC`) order [00:11:13].
    `SELECT * FROM users ORDER BY id DESC;`
*   `WHERE`: Filters rows based on conditional logic [00:11:30].
    `SELECT * FROM users WHERE country = 'US';`
*   `AND`/`OR`: Chains multiple conditions in a `WHERE` clause [00:11:42].
    `SELECT * FROM users WHERE country = 'US' AND id > 1;`
*   `LIKE`: Used for pattern matching, often with a wildcard character (`%`) [00:11:53].
    `SELECT * FROM users WHERE email LIKE 'h%';` (finds emails starting with 'h')

### Indexes
An index is a lookup table that helps retrieve data faster, especially for pattern-based queries, by avoiding full table scans [00:12:21]. However, indexes can slow down write operations and require additional memory [00:12:37].

```sql
CREATE INDEX email_index ON users (email);
```

## Working with SQL Joins

Joins are used to query data from two or more related tables [00:14:16]. When performing a join, SQL matches data based on specified conditions, typically linking a primary key in one table to a foreign key in another [00:14:38]. The type of join determines which data is returned if there isn't a corresponding relationship [00:14:47].

Consider `users` as the "left" table and `rooms` as the "right" table in the following examples [00:14:34].

### Types of Joins

#### 1. `INNER JOIN`
Returns only the rows that have matching values in both tables [00:14:55].
```sql
SELECT *
FROM users
INNER JOIN rooms ON rooms.owner_id = users.id;
```
This query would return only users who own rooms, joined with their respective room data [00:15:02].

#### 2. `LEFT JOIN` (or `LEFT OUTER JOIN`)
Returns all rows from the left table, and the matching rows from the right table. If there's no match, `NULL` values are returned for the right table's columns [00:15:17].
```sql
SELECT *
FROM users
LEFT JOIN rooms ON rooms.owner_id = users.id;
```
This would return all users, including those who don't own any rooms. For users without rooms, the room data columns would be `NULL` [00:15:21].

#### 3. `RIGHT JOIN` (or `RIGHT OUTER JOIN`)
Returns all rows from the right table, and the matching rows from the left table. If there's no match, `NULL` values are returned for the left table's columns [00:15:29].
```sql
SELECT *
FROM users
RIGHT JOIN rooms ON rooms.owner_id = users.id;
```
This would return all rooms, including those that might not have an associated owner (though foreign key constraints would typically prevent this in a well-designed database) [00:15:31].

#### 4. `FULL OUTER JOIN`
Returns all rows when there is a match in either the left or right table. If no match, `NULL` is returned for the non-matching side. MySQL does not directly support `FULL OUTER JOIN`, but it can often be emulated using `LEFT JOIN` and `RIGHT JOIN` with `UNION` [00:15:34].

### Handling Column Name Conflicts
When joining tables, if both tables have columns with the same name (e.g., `id`), MySQL will automatically rename them in the result set (e.g., `users.id`, `rooms.id`) [00:15:43]. You can explicitly rename columns in your `SELECT` statement using the `AS` keyword [00:15:51].

```sql
SELECT
    users.id AS user_id,
    users.email,
    rooms.id AS room_id,
    rooms.title
FROM users
INNER JOIN rooms ON rooms.owner_id = users.id;
```

## Deleting Data (`DROP`)
The `DROP` statement is powerful and allows for the deletion of entire tables or databases [00:17:07]. Use with extreme caution, as it can lead to permanent data loss [00:17:02].

```sql
-- To delete a table
DROP TABLE users;

-- To delete an entire database
DROP DATABASE airbnb;
```