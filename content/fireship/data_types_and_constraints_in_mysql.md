---
title: Data Types and Constraints in MySQL
videoId: Cz3WcZLRaWc
---

From: [[fireship]] <br/> 

When working with [[introduction_to_relational_databases_and_sql | relational databases]], such as [[getting_started_with_mysql | MySQL]], understanding data types and constraints is crucial for defining the structure and rules within your database <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. This blueprint, known as the database schema, ensures data integrity and optimal performance <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

## Data Types

Each column in a database table requires a specific data type, which dictates the kind of data that can be stored there <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. If you try to save the wrong data to a column, the database will throw an error because SQL is very strict about data integrity <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>. While data types can vary between different SQL databases, they generally represent various types of numbers and strings <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

Choosing the correct data type is essential for optimizing the size and performance of your database, especially when building serious applications <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

Common data types in [[getting_started_with_mysql | MySQL]] include:
*   **`INT`**: Used for integers, which are whole numbers <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.
*   **`FLOAT`**: Used for floating-point numbers, which include decimals <a class="yt-timestamp" data-t="03:23:00">[03:23:00]</a>.
*   **`VARCHAR(n)`**: Designed for small strings, where `n` specifies the maximum length of the string <a class="yt-timestamp" data-t="03:25:00">[03:25:00]</a>. A common maximum length is 255 characters, as it efficiently uses an 8-bit number <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.
*   **`TEXT`**: Used for longer strings with an unspecified size <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>.

## Constraints

In addition to a data type, a column can also have one or more special constraints <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. Constraints act as an extra layer of data validation beyond just the data type <a class="yt-timestamp" data-t="08:13:00">[08:13:00]</a>.

Key constraints:
*   **`NOT NULL`**: Ensures that a column cannot store a null value <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. This means a value *must* be added to that field on every row <a class="yt-timestamp" data-t="08:51:00">[08:51:00]</a>.
*   **`UNIQUE`**: Requires each value in that column to be unique <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.
*   **`PRIMARY KEY`**: Identifies a unique row in the table <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. A primary key automatically implies `NOT NULL` and `UNIQUE` constraints <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>. Every table in a schema typically has an `id` with a `PRIMARY KEY` constraint, ensuring every row can be uniquely identified <a class="yt-timestamp" data-t="03:47:00">[03:47:00]</a>.
*   **`AUTO_INCREMENT`**: Instructs the database to automatically create the ID for you, starting at 1 and incrementing with each new row <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.
*   **`FOREIGN KEY`**: References an ID in a different table <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>. This is essential for [[working_with_sql_joins_and_relationships | building relationships]] between tables <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. For example, in an Airbnb-like database, an `owner_id` in a `rooms` table would be a foreign key referencing the `id` in the `users` table <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>. A `FOREIGN KEY` constraint tells the database not to delete anything that holds data about that relationship, guaranteeing data integrity <a class="yt-timestamp" data-t="13:45:00">[13:45:00]</a>.

> [!example] Creating a table with data types and constraints
> ```sql
> CREATE TABLE users (
>     id INT PRIMARY KEY AUTO_INCREMENT,
>     email VARCHAR(255) NOT NULL UNIQUE,
>     bio TEXT,
>     country VARCHAR(2)
> );
> ```
> This SQL statement, used when [[creating_and_managing_tables_in_mysql | creating a table]], defines columns with their respective data types and constraints <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.
> *   `id` is an integer, a primary key, and auto-increments <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>.
> *   `email` is a string up to 255 characters, cannot be null, and must be unique <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.
> *   `bio` is a text field for longer strings <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.
> *   `country` is a string exactly two characters long <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>.