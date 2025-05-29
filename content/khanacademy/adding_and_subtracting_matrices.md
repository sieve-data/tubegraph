---
title: Adding and subtracting matrices
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

A matrix (plural: matrices) is fundamentally a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It serves as a way of writing down and representing data <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>, such as linear equations, pixels in computer graphics, or points in coordinate space <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Unlike some mathematical concepts, a matrix is a defined convention rather than a natural phenomenon <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## [[Matrix notation and terminology | Matrix Notation and Terminology]]

Matrices are typically represented by a capital letter, which is sometimes bolded <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

A matrix's "size" or "dimensions" are described by its number of rows and columns <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. For example, a matrix with two rows and three columns is called a "2-by-3 matrix" <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This dimension is sometimes written below the matrix's capital letter notation <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Elements within a matrix can be referenced by their row and column position. For matrix `A`, the element in the second row, second column, for example, could be written as `A(2,2)` or `a(2,2)` <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Examples of Matrices and Their Dimensions:
*   **Matrix A (2-by-3):**
    ```
    ┌ 5  1  2 ┐
    └ 3  0 -5 ┘
    ```
    In this matrix, `A(2,2)` (second row, second column) is `0` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    `A(1,3)` (first row, third column) is `2` <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

*   **Matrix B (5-by-2):**
    ```
    ┌   0 -10 ┐
    │  -5   3 │
    │  10   7 │
    │   0   2 │
    └   0  pi ┘
    ```
    This matrix has five rows and two columns <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Vectors
When a matrix has only one row or one column, it's referred to as a vector <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **Row Vector:** A matrix with one row and multiple columns (e.g., `[-3 2]`) <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   **Column Vector:** A matrix with multiple rows and one column (e.g., `[9; 7]`) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

## [[Adding negative numbers | Adding]] Matrices

To add two matrices, you add their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. This means the element in the first row, first column of the first matrix is added to the element in the first row, first column of the second matrix, and so on <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

### Requirement for Addition
For matrix addition to be possible, both matrices **must have the same dimensions** (same number of rows and same number of columns) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. You cannot add a 1-by-2 matrix to a 2-by-1 matrix because they don't have corresponding elements <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

### Example of Matrix Addition
Let's consider two matrices:
*   Matrix A:
    ```
    ┌  3 -1 ┐
    └  2  0 ┘
    ```
    <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>

*   Matrix B:
    ```
    ┌ -7  2 ┐
    └  3  5 ┘
    ```
    <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

To find A + B:
```
A + B = ┌  3 + (-7)   -1 + 2 ┐
        └  2 + 3       0 + 5 ┘
```
<a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>, <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>

Performing the [[adding_and_subtracting_negative_numbers | arithmetic]]:
```
A + B = ┌ -4  1 ┐
        └  5  5 ┘
```
<a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>, <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>

It's important to note that, by this definition, matrix addition is commutative; A + B will yield the same result as B + A <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## [[Subtracting negative numbers | Subtracting]] Matrices

Matrix subtraction is similar to addition; you subtract the corresponding elements <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>, <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

### Scalar Multiplication
Before proceeding with subtraction, it's useful to understand **scalar multiplication**. When you multiply a matrix by a scalar (a single number), you multiply every element within the matrix by that scalar <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>, <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

For instance, if `B` is:
```
B = ┌ -7  2 ┐
    └  3  5 ┘
```
Then `-1 * B` would be:
```
-1 * B = ┌ -1 * (-7)   -1 * 2 ┐
         └ -1 * 3       -1 * 5 ┘
         = ┌  7  -2 ┐
           └ -3  -5 ┘
```
<a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>

### Example of Matrix Subtraction
Using Matrix A and Matrix B from the addition example, to find A - B, you can think of it as A + (-1 * B) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>:

```
A - B = A + (-1 * B)
      = ┌  3 -1 ┐ + ┌  7 -2 ┐
        └  2  0 ┘   └ -3 -5 ┘
```
<a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>

Performing the [[adding_and_subtracting_negative_numbers | element-wise addition]]:
```
A - B = ┌  3 + 7      -1 + (-2) ┐
        └  2 + (-3)    0 + (-5) ┘
      = ┌ 10  -3 ┐
        └ -1  -5 ┘
```
<a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>, <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>, <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>, <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>

Alternatively, you could directly subtract the corresponding elements:
```
A - B = ┌  3 - (-7)   -1 - 2 ┐
        └  2 - 3       0 - 5 ┘
      = ┌ 10  -3 ┐
        └ -1  -5 ┘
```
This yields the same result <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

As with addition, matrices must have the same dimensions to be subtracted <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.