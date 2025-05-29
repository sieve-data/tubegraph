---
title: Matrix dimensions and types
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

A [[Introduction to matrices|matrix]] (plural: matrices) is defined as a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The term "matrices" is simply the plural of "matrix" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## [[Matrix notation and terminology|Matrix Notation]]
A matrix is often represented by a capital letter, sometimes in boldface, such as bold A <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## [[Matrix notation and terminology|Dimensions]]
The [[Matrix dimensions and types|dimensions]] of a matrix are described by its number of rows and columns <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. By convention, a matrix is called an "X-by-Y" matrix, where X is the number of rows and Y is the number of columns <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. This can also be written as "X by Y" below the capital letter representing the matrix <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

For example:
*   A "2-by-3" matrix has two rows and three columns <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
*   A "5-by-2" matrix has five rows and two columns <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>, <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Referencing Elements
Individual elements within a matrix can be referenced by their row and column position. This is typically done using the matrix's variable name (either capital or lowercase), followed by the row and column numbers in parentheses or as subscripts. For instance, `A(2,2)` or `a(2,2)` refers to the element in the second row, second column <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Matrix Types
When one of a matrix's [[Matrix dimensions and types|dimensions]] is one, it is given a special name, referred to as a "vector" <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. A vector is essentially a one-dimensional matrix <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

*   **Row Vector**: A matrix with one row and multiple columns <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. For example, a 1-by-2 matrix <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Column Vector**: A matrix with multiple rows and one column <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. For example, a 2-by-1 matrix <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## [[Applications and uses of matrices|Applications]]
A matrix is a data representation, a way of writing down data <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>, <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. While often used to represent linear equations in algebra classes <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>, matrices can represent a wide range of phenomena <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. For example, in computer graphics, elements of a matrix can represent pixels on a screen or [[Understanding points and dimensions|points]] in coordinate space <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>, <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. It's important to understand that a matrix is a way to represent a mathematical concept or values, rather than a natural phenomenon itself, and its specific representation needs to be defined for context <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>, <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Matrix Operations
Operations like [[Adding and subtracting matrices|matrix addition]], subtraction, multiplication, inversion, and finding determinants are human-defined conventions useful for various phenomena <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>, <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>, <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>, <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>, <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>, <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

### Adding and Subtracting Matrices
To [[Adding and subtracting matrices|add two matrices]], one adds their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>, <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. This means the element in row 1, column 1 of the first matrix is added to the element in row 1, column 1 of the second matrix, and so on <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>, <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

For matrix addition to be possible, both matrices must have the same [[Matrix dimensions and types|dimensions]] (same number of rows and same number of columns) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>, <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>, <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   The order of addition does not matter; A + B yields the same result as B + A <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

Matrix subtraction is similar to addition; one can directly subtract corresponding elements <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>, <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. Alternatively, subtracting a matrix B from A (A - B) can be thought of as A plus negative 1 times B <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

### Scalar Multiplication
When multiplying a scalar (a single number) by a matrix, the scalar is multiplied by every element within the matrix <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>, <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>, <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>, <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.