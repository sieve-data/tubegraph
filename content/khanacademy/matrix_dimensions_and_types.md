---
title: Matrix dimensions and types
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

## Introduction to Matrices

The term "matrices" is the plural form of "matrix" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. In mathematics, a matrix is simply a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Matrix Notation and Dimensions

When working with matrices, a [[understanding_variables | variable]] representing a matrix is typically a boldface capital letter, such as a bold 'A' <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

The [[matrix_notation_and_conventions | notation]] for describing a matrix's size is "rows-by-columns" <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. This describes the matrix's [[concept_of_dimensions_in_geometry | dimensions]].

*   **Rows** are horizontal lines of numbers <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Columns** are vertical lines of numbers <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

For example:
*   A matrix with 2 rows and 3 columns is called a "2-by-3 matrix" <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
    ```
    [[5, 1, 2],
     [3, 0, -5]]
    ```
*   A "5-by-2 matrix" would have five rows and two columns <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>, <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

The [[matrix_notation_and_conventions | notation]] for the matrix's dimensions can sometimes be written below the bold letter representing the matrix, e.g., A₂ₓ₃ <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

### Referencing Elements

Individual elements within a matrix can be referenced by their row and column position <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This is often done using a lowercase letter corresponding to the matrix's name, followed by two subscripts: `row_number, column_number` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

*   `A₂,₂` refers to the element in the second row and second column <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>, <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   `A₁,₃` refers to the element in the first row and third column <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Purpose and Applications

A matrix serves as a data representation, providing a structured way of writing down data <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>, <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. While it's a useful mathematical construct, a matrix itself is not a natural phenomenon; its meaning must be defined by what it represents <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>, <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

Matrices are powerful tools capable of representing various phenomena, including:
*   Linear equations in algebra classes <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   Pixels in computer graphics <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Points in coordinate space <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

## Special Matrix Types: Vectors

When one of a matrix's [[concept_of_dimensions_in_geometry | dimensions]] is one, it is called a [[differences_between_vectors_and_scalars | vector]] <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

*   A **row [[differences_between_vectors_and_scalars | vector]]** has one row and multiple columns (e.g., a 1-by-2 matrix) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>, <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
    ```
    [[-3, 2]]
    ```
*   A **column [[differences_between_vectors_and_scalars | vector]]** has multiple rows and one column (e.g., a 2-by-1 matrix) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
    ```
    [[9],
     [7]]
    ```

## Matrix Operations (Dimensional Requirement)

The way humans have defined matrix operations, such as [[matrix_addition_and_subtraction | matrix addition]] and [[matrix_addition_and_subtraction | subtraction]], means there are specific dimensional requirements <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>, <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

For [[matrix_addition_and_subtraction | matrix addition]], both matrices *must* be the same size (have the same number of rows and columns) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. If matrices do not have the same [[concept_of_dimensions_in_geometry | dimensions]], they cannot be added or subtracted <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>, <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

When performing [[scalar_multiplication_of_matrices | scalar multiplication]] (multiplying a matrix by a single number), that number is multiplied by every element within the matrix <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>, <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.