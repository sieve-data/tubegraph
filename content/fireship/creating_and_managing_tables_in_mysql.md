---
title: Creating and Managing Tables in MySQL
videoId: Cz3WcZLRaWc
---

From: [[fireship]] <br/> 

[[introduction_to_relational_databases_and_sql | Relational databases]] using [[introduction_to_relational_databases_and_sql | SQL]] are a dominant technology in database management <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite being 40 years old, [[introduction_to_relational_databases_and_sql | SQL]] remains a go-to choice for nearly two-thirds of developers, even with billions invested in disruptive technologies <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This article focuses on [[getting_started_with_mysql | MySQL]], an open-source database that powers large content management systems like WordPress, e-commerce platforms like Shopify, and social media giants like Twitter <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

Most developers use Object Relational Mapping (ORM) libraries, such as SQLize for JavaScript, SQLAlchemy for Python, or Active Record for Ruby on Rails, which allow interaction with databases using an [[object_creation_and_manipulation | object-oriented programming]] language <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>. However, understanding raw [[introduction_to_relational_databases_and_sql | SQL]] is crucial for comprehending how ORMs function <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

## Database Structure

A relational database management system consists of two main components:
1.  The database itself, which is a collection of tables <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
2.  A language, typically a variation of [[introduction_to_relational_databases_and_sql | Structured Query Language]], used to manipulate and read data within the database <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

Data within each table is organized into columns and rows, similar to a spreadsheet <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Database Schema and Data Modeling

A database schema is a blueprint that defines the rules and constraints within the database <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Tools like DrawSQL can help visualize and model data relationships <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Each box in a schema diagram represents a database table, and lines between them represent relationships like one-to-one or one-to-many <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

### Data Normalization

Relational databases aim for a normalized data structure, meaning every entity is organized into its smallest normal form, a concept laid out by Ted Codd <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This approach minimizes data duplication across tables <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. For instance, in an Airbnb-like application, user and room data are separated into their own tables, and then joined back together through a "bookings" table when needed <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. This is analogous to breaking down a car into individual parts and joining them back to build a car <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Creating Tables

Tables are created using the `CREATE TABLE` statement <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. [[introduction_to_relational_databases_and_sql | SQL]] statements end with a semicolon <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. [[introduction_to_relational_databases_and_sql | SQL]] keywords (like `CREATE`, `TABLE`) are typically written in uppercase by convention, though they are not case-sensitive <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. The table name is an identifier <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

Inside parentheses, a list of columns to be included in the table is defined, each with a [[data_types_and_constraints_in_mysql | data type]] and optional constraints <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    bio TEXT,
    country VARCHAR(2)
);
```
<a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>

## Data Types and Constraints

Columns require a [[data_types_and_constraints_in_mysql | data type]] to specify the kind of data they can store <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>. Attempting to save incorrect data types will result in an error due to [[introduction_to_relational_databases_and_sql | SQL]]'s strict data integrity <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

Common [[data_types_and_constraints_in_mysql | MySQL data types]]:
*   `INT`: For whole numbers (integers) <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
*   `FLOAT`: For floating-point numbers <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   `VARCHAR(size)`: For strings with a specified maximum length (e.g., `VARCHAR(255)` often used due to 8-bit character limits) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   `TEXT`: For longer strings of unspecified size <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

Constraints are additional rules beyond [[data_types_and_constraints_in_mysql | data types]] that columns must adhere to <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.

Key constraints:
*   `PRIMARY KEY`: Ensures that the column's values are unique and not null, identifying each row uniquely <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   `AUTO_INCREMENT`: Automatically generates unique, incrementing integer values for a column, typically used for primary keys <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   `NOT NULL`: Requires that a column must contain a value; it cannot be empty <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   `UNIQUE`: Ensures all values in a column are distinct <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

### Establishing Relationships with Foreign Keys

[[working_with_sql_joins_and_relationships | Relationships]] between tables are established using foreign keys. For example, in an Airbnb-like application, a user can have many rooms (a one-to-many relationship) <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

```sql
CREATE TABLE rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    street VARCHAR(255) NOT NULL,
    owner_id INT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);
```
<a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>

In the `rooms` table, `owner_id` is a foreign key that references the `id` column in the `users` table <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This constraint prevents deletion of users who have associated rooms, ensuring data integrity <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

Complex relationships, such as a user booking a room from another user, can be modeled using a third, intermediate table, like `bookings` or `reservations` <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. This table would contain foreign keys for both the guest (user) and the room, allowing for a many-to-many relationship <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.

## Inserting Data

Data is added to tables using the `INSERT INTO` statement <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. You specify the table name, the columns to update, and then the values to be inserted <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. The order of values must match the order of columns <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Columns with `AUTO_INCREMENT` do not need to be specified <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.

```sql
INSERT INTO users (email, bio, country) VALUES
('hello@gmail.com', 'i am a software engineer', 'US'),
('bill@microsoft.com', 'i sell software', 'US'),
('elon@tesla.com', 'i build rockets', 'US'),
('sundar@google.com', 'i run google', 'IN');
```
<a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>

Multiple rows can be inserted in a single `INSERT INTO` statement by separating value sets with commas <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

## Reading Data

The `SELECT` statement is used to retrieve or query data <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>.

*   `SELECT * FROM users;`: Returns all columns and rows from the `users` table <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   `SELECT email, id FROM users;`: Filters out specific columns <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   `LIMIT`: Limits the number of rows returned (e.g., `SELECT * FROM users LIMIT 2;`) <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.
*   `ORDER BY`: Orders the result set by a specified column in ascending (`ASC`) or descending (`DESC`) order (e.g., `SELECT * FROM users ORDER BY id DESC;`) <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   `WHERE`: Filters rows based on a specified condition (e.g., `SELECT * FROM users WHERE country = 'US';`) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. Conditions can be chained with `AND` or `OR` <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   `LIKE`: Used for pattern matching (e.g., `SELECT * FROM users WHERE email LIKE 'h%';`) <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.

### Database Indexing

For faster data retrieval, especially with large datasets or pattern matching, an index can be created on a column <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. An index acts like a lookup table, helping the database find data without scanning the entire dataset <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. While improving read performance, indexes can slow down write operations and require additional memory <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.

```sql
CREATE INDEX email_index ON users (email);
```
<a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>

## Deleting Data and Tables

The `DROP` statement is used to delete data, such as individual tables or entire databases <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. This command should be used with extreme caution, as it can lead to permanent data loss <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>.

```sql
DROP TABLE users; -- Deletes the 'users' table
DROP DATABASE airbnb; -- Deletes the 'airbnb' database
```