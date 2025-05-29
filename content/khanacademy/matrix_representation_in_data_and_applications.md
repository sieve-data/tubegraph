---
title: Matrix representation in data and applications
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

Matrices are the plural form of "matrix," a term often more familiar from Hollywood than mathematics <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. At its core, a matrix is a straightforward concept: simply a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## [[Definition and notation of matrices | Definition and Notation]]

A matrix organizes numbers within a structured table <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Here is an example of a matrix:
```
[ 5  1  2 ]
[ 3  0 -5 ]
```
<a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>

### Representing Matrices
When using a variable to represent a matrix, a capital letter is typically used, sometimes in boldface <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. For example, a bold 'A' might denote a matrix <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### [[Matrix dimensions and conventions | Dimensions]]
The [[matrix_dimensions_and_conventions | dimensions]] of a matrix are defined by its number of rows and columns <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. By [[definition_and_notation_of_matrices | convention]], a matrix is described as "rows-by-columns" <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

*   A 2-by-3 matrix has two rows and three columns <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.
    *   Example: Matrix A above is a 2-by-3 matrix <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   A 5-by-2 matrix has five rows and two columns <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>, <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Referencing Elements
Individual elements within a matrix can be referenced by their row and column position <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. For matrix A, an element is denoted as A<sub>(row, column)</sub> or a<sub>(row, column)</sub> <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   A<sub>(2,2)</sub> (or a<sub>(2,2)</sub>) refers to the element in the second row, second column <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>, which is 0 in the example matrix A <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   A<sub>(1,3)</sub> refers to the element in the first row, third column <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, which is 2 in the example matrix A <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Applications of Matrices

A matrix serves as a data representation, providing a structured way to write down data <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>, <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. It can represent a wide range of phenomena <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

Common applications include:
*   Representing linear equations <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   In [[Graphical representation and visual understanding of functions | computer graphics]], elements can represent pixels on a screen or points in coordinate space <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>, <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.

It's crucial to understand that a matrix is not a natural phenomenon, but rather a tool to represent mathematical concepts or values <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Its meaning depends on what it is defined to represent <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>, <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Matrix Operations: Human-Defined Conventions

The rules for operating with matrices (such as addition, multiplication, inversion, and determinants) are human-defined [[definition_and_notation_of_matrices | conventions]] established because of their usefulness in various applications <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>, <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>, <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. Learning these conventions first is essential, with the intuition behind them coming later <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>, <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Matrix Addition
To add two matrices, you add their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
Given:
Matrix A:
```
[  3  -1 ]
[  2   0 ]
```
<a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>

Matrix B:
```
[ -7   2 ]
[  3   5 ]
```
<a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

A + B is calculated by adding each element in A to its corresponding element in B:
```
[ (3 + -7)  (-1 + 2) ]
[ (2 + 3)    (0 + 5)  ]
```
<a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>, <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>

Resulting in:
```
[ -4  1 ]
[  5  5 ]
```
<a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>, <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>

#### Properties of Matrix Addition
*   **Commutativity**: A + B is the same as B + A <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Dimension Requirement**: For addition, both matrices must have the same [[matrix_dimensions_and_conventions | dimensions]] <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, meaning the same number of rows and columns <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. For instance, a 1x2 matrix cannot be added to a 2x1 matrix because they lack corresponding elements <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>, <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### [[Scalar multiplication of matrices | Scalar Multiplication]]
When a scalar (a single number) is multiplied by a matrix, that number is multiplied by every element within the matrix <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>, <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

For example, if B is the matrix shown above, then -1 * B is:
```
[ (-1 * -7)  (-1 * 2) ]
[ (-1 * 3)   (-1 * 5) ]
```
<a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>

Resulting in:
```
[  7  -2 ]
[ -3  -5 ]
```
<a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>

### Matrix Subtraction
Matrix subtraction can be understood as adding a scalar-multiplied matrix. A - B is equivalent to A + (-1 * B) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. Alternatively, you can directly subtract the corresponding elements <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

Using A and B from above:
A - B = A + (-1 * B)
```
[  3  -1 ]   +   [  7  -2 ]   =   [ (3 + 7)   (-1 + -2) ]   =   [ 10  -3 ]
[  2   0 ]       [ -3  -5 ]       [ (2 + -3)  (0 + -5)  ]       [ -1  -5 ]
```
<a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>, <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>, <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>, <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>, <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>

### Vectors
As a side note, when one of a matrix's [[matrix_dimensions_and_conventions | dimensions]] is one, it is called a vector <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>, <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   A **row vector** has one row and multiple columns (e.g., [ -3 2 ]) <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>, <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   A **column vector** has multiple rows and one column (e.g., [ 9 7 ] vertically) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.