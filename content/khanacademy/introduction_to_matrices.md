---
title: Introduction to matrices
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

## What is a Matrix?
A matrix is a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The term "matrices" is the plural form of "matrix" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

Here is an example of a matrix:
```
[[5, 1, 2],
 [3, 0, -5]]
```
This is a matrix <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, and it is simply a table of numbers <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## [[matrix_notation_and_conventions | Matrix Notation and Conventions]]
When using a variable to represent a matrix, a capital letter is typically used, sometimes in bold, such as a bold A <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

### [[matrix_dimensions_and_types | Matrix Dimensions]]
By [[matrix_notation_and_conventions | convention]], a matrix is described by its dimensions: `rows` by `columns` <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. For example, the matrix above is a 2-by-3 matrix <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>:
*   The first number (2) indicates the number of rows <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. (In the example, there are two rows: `[5, 1, 2]` and `[3, 0, -5]` <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>).
*   The second number (3) indicates the number of columns <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. (In the example, there are three columns <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>).

Sometimes, the dimensions (e.g., "2 by 3") are written below the bold letter representing the matrix <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

For instance, a 5-by-2 matrix would have five rows and two columns <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### Referencing Elements
Individual elements within a matrix can be referenced by their row and column position <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. For matrix A:
*   `A[row_number, column_number]` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
*   Or `a[row_number, column_number]` (lowercase a) <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>

For the example matrix `A = [[5, 1, 2], [3, 0, -5]]`:
*   The element `0` is in the second row and second column <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>, so `A[2, 2] = 0` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   The element `2` is in the first row and third column <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>, so `A[1, 3] = 2` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Purpose of Matrices
A matrix is a data representation <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>, a way of writing down data <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. They can represent various phenomena <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

In [[introduction_to_algebra | Algebra I]] or [[introduction_to_algebra | Algebra II]] classes, matrices are often used to represent linear equations <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Beyond that, in computer graphics, matrix elements can represent pixels on a screen or points in coordinate space <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

Matrices are not natural phenomena; they are a human-defined way to represent mathematical concepts or values <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Matrix Operations: Human-Defined Conventions
The operations on matrices (addition, multiplication, inversion, finding determinants) are human-defined [[matrix_notation_and_conventions | conventions]] <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### Matrix Addition
When adding two matrices, you add their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

**Example:**
Given Matrix A:
```
A = [[3, -1],
     [2,  0]]
```
And Matrix B:
```
B = [[-7, 2],
     [ 3, 5]]
```
To find A + B:
```
A + B = [[3 + (-7), -1 + 2],
         [2 + 3,    0 + 5]]  <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>
```
Result:
```
A + B = [[-4, 1],
         [ 5, 5]]             <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>
```
**Important Note:** For matrix addition, both matrices must have the same [[matrix_dimensions_and_types | dimensions]] <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. You cannot add matrices with different numbers of rows or columns <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>.

Matrix addition is commutative; A + B will yield the same result as B + A <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

### [[scalar_multiplication_of_matrices | Scalar Multiplication of Matrices]]
When multiplying a matrix by a scalar (a single number), you multiply that number by every one of the matrix's elements <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

**Example:**
If Matrix B is:
```
B = [[-7, 2],
     [ 3, 5]]
```
Then -1 times B is:
```
-1 * B = [[(-1)*(-7), (-1)*2],
          [(-1)*3,    (-1)*5]]
```
Result:
```
-1 * B = [[7,  -2],
          [-3, -5]]            <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>
```

### Matrix Subtraction
Matrix subtraction is essentially the same as addition <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. You can subtract corresponding elements directly, or you can consider A - B as A + (-1 * B) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

**Example:**
Given Matrix A:
```
A = [[3, -1],
     [2,  0]]
```
And Matrix B:
```
B = [[-7, 2],
     [ 3, 5]]
```
To find A - B:
```
A - B = [[3 - (-7), -1 - 2],
         [2 - 3,    0 - 5]]
```
Result:
```
A - B = [[10, -3],
         [-1,  -5]]            <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
```

## [[matrix_dimensions_and_types | Types of Matrices: Vectors]]
When one of a matrix's [[matrix_dimensions_and_types | dimensions]] is one, it is called a vector <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. A vector is essentially a one-dimensional matrix <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

*   **Row Vector**: A matrix with one row and multiple columns (e.g., `[-3, 2]`) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Column Vector**: A matrix with multiple rows and one column (e.g., `[[9], [7]]`) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

## Next Steps
Future lessons will cover more complex matrix operations such as:
*   How to multiply matrices <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>
*   How to invert matrices <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>
*   How to find the determinant of matrices <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>