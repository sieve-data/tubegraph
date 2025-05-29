---
title: Matrix notation and conventions
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

A **matrix** is fundamentally a table of numbers <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. The plural form of matrix is **matrices** <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. While the term might be more familiar from Hollywood, in mathematics, it serves as a straightforward data representation tool <a class="yt-timestamp" data-t="00:45:04">[00:45:04]</a>.

A matrix is not a natural phenomenon, but rather a way to represent mathematical concepts or values; its specific meaning must be defined by the user <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>. Matrices can be used to represent various phenomena, such as linear equations in algebra <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>, or pixels and points in coordinate space in computer graphics <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>.

## [[Matrix notation and conventions | Matrix Notation]]

When representing a matrix as a variable, a capital letter is typically used, often bolded (e.g., **A**) <a class="yt-timestamp" data-t="00:48:46">[00:48:46]</a>.

### [[Matrix dimensions and types | Matrix Dimensions]]

The [[Matrix dimensions and types | dimensions]] of a matrix are described by its number of rows and columns, in the format "rows-by-columns" <a class="yt-timestamp" data-t="01:06:06">[01:06:06]</a>. For example, a "2-by-3 matrix" has two rows and three columns <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>. This can sometimes be written directly below the variable representing the matrix <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

*   **Rows** are horizontal <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
*   **Columns** are vertical <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

An example of a 2-by-3 matrix:
```
[ 5  1  2 ]
[ 3  0 -5 ]
```
<a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>

### Referencing Elements

Individual elements within a matrix can be referenced by their row and column position. This is typically done using the matrix's variable name followed by subscripts for the row and column (e.g., A₂,₂ or a₂,₂) <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>. The first subscript indicates the row number, and the second indicates the column number <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.

For matrix **A** above:
*   A₂,₂ = 0 (element in the second row, second column) <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>
*   A₁₃ = 2 (element in the first row, third column) <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>

## Matrix Operations

Matrix operations, such as [[Matrix addition and subtraction | addition]], [[Scalar multiplication of matrices | multiplication]], or inversion, are human-defined conventions <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>. These definitions are established because they are useful for representing and solving various mathematical problems <a class="yt-timestamp" data-t="05:29:00">[05:29:00]</a>.

### [[Matrix addition and subtraction | Matrix Addition]]

To add two matrices, you add their corresponding elements <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>. This means the element in row 1, column 1 of the first matrix is added to the element in row 1, column 1 of the second matrix, and so on <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>.

For example, given:
**A** =
```
[  3  -1 ]
[  2   0 ]
```
and **B** =
```
[ -7   2 ]
[  3   5 ]
```
**A** + **B** =
```
[ (3 + (-7))   (-1 + 2) ]
[  (2 + 3)     (0 + 5)  ]
```
=
```
[ -4   1 ]
[  5   5 ]
```
<a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>

#### Rules for [[Matrix addition and subtraction | Addition]]
*   **Same [[Matrix dimensions and types | Dimensions]] Required**: For matrices to be added, they must have the exact same number of rows and columns <a class="yt-timestamp" data-t="09:49:00">[09:49:00]</a>. You cannot add a 1-by-2 matrix to a 2-by-1 matrix, as they lack corresponding elements <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>.
*   **Commutative Property**: By definition, matrix addition is commutative, meaning the order of addition does not matter (A + B = B + A) <a class="yt-timestamp" data-t="07:41:00">[07:41:00]</a>.

### [[Scalar multiplication of matrices | Scalar Multiplication]]

[[Scalar multiplication of matrices | Scalar multiplication]] involves multiplying a matrix by a single number (a scalar). To perform this operation, you multiply every element within the matrix by that scalar <a class="yt-timestamp" data-t="08:46:00">[08:46:00]</a>.

For example, to calculate **A** - **B**, it can be thought of as **A** + (-1) * **B** <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>.
If **B** =
```
[ -7   2 ]
[  3   5 ]
```
Then (-1) * **B** =
```
[ (-1 * -7)   (-1 * 2) ]
[ (-1 * 3)    (-1 * 5) ]
```
=
```
[  7  -2 ]
[ -3  -5 ]
```
<a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>

So, **A** - **B** =
```
[  3  -1 ]   +   [  7  -2 ]   =   [ (3 + 7)   (-1 + (-2)) ]   =   [ 10  -3 ]
[  2   0 ]       [ -3  -5 ]       [ (2 + (-3)) (0 + (-5)) ]       [ -1  -5 ]
```
<a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>

### [[Matrix dimensions and types | Vectors]]

A **vector** is a one-dimensional matrix where one of its [[Matrix dimensions and types | dimensions]] is one <a class="yt-timestamp" data-t="11:29:00">[11:29:00]</a>.
*   A **row vector** has one row and multiple columns (e.g., a 1-by-2 matrix) <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>.
*   A **column vector** has multiple rows and one column (e.g., a 2-by-1 matrix) <a class="yt-timestamp" data-t="11:33:00">[11:33:00]</a>.