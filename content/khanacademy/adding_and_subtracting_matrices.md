---
title: Adding and subtracting matrices
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

Matrices are a fundamental concept in mathematics, often used to represent tables of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The word "matrices" is the plural form of "matrix" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## What is a Matrix?
A matrix is simply a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, such as:
```
5  1  2
3  0 -5
```
<a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>

Matrices serve as a data representation, a way of writing down data, and can represent various phenomena <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. In algebra classes, they are often used to represent [[solving_linear_equations_with_addition_and_subtraction | linear equations]] <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

## [[definition_and_notation_of_matrices | Matrix Notation]] and Terminology
*   **Variable Representation**: A matrix is typically represented by a capital letter, often bolded (e.g., **A** or A) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Dimensions (Rows x Columns)**: The size of a matrix is conventionally described as "rows by columns" <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
    *   For example, a matrix with two rows and three columns is a "2-by-3 matrix" <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
    *   Rows are horizontal entries <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
    *   Columns are vertical entries <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Referencing Elements**: Individual numbers within a matrix are called elements and can be referenced by their row and column position <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
    *   For a matrix **A**, the element in the second row, second column is denoted as A₂.₂ or a₂.₂ <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   For instance, in the example matrix `A = [[5, 1, 2], [3, 0, -5]]`, the element in the first row, third column (A₁₃ or a₁₃) is 2 <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## Adding Matrices
The addition of two matrices is a human-defined convention based on usefulness for various phenomena <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

To add two matrices, you add their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### Example of Matrix Addition
Given two matrices:
```
A = [ 3 -1 ]
    [ 2  0 ]
```
<a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>
```
B = [ -7  2 ]
    [  3  5 ]
```
<a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

**A + B** is calculated by adding each element at the same position:
```
A + B = [ (3 + -7)  (-1 + 2) ]
        [ (2 + 3)   (0 + 5)  ]
```
<a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>
```
A + B = [ -4  1 ]
        [  5  5 ]
```
<a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>

This definition implies that matrix addition is commutative, meaning **A + B** yields the same result as **B + A** <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

### Requirements for Matrix Addition
For two matrices to be added, they **must** have the same size (same number of rows and same number of columns) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

*   **Valid Addition Example**:
    A 3x3 matrix can be added to another 3x3 matrix <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
    ```
    [ 1  2  3 ]   [ -10  -100  -1000 ]
    [ 4  5  6 ] + [   1     0      0  ]
    [ 7  8  9 ]   [   1     0      1  ]
    ```
    The first element of the sum would be (1 + -10) = -9 <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

*   **Invalid Addition Example**:
    A 1x2 matrix cannot be added to a 2x1 matrix because they do not have corresponding elements to add up <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
    ```
    [ -3  2 ]  cannot be added to  [ 9 ]
                                   [ 7 ]
    ```
    <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>

## [[scalar_multiplication_of_matrices | Scalar Multiplication]]
When multiplying a scalar (a single number) by a matrix, you multiply that number by every single element of the matrix <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

### Example of Scalar Multiplication
Given matrix B:
```
B = [ -7  2 ]
    [  3  5 ]
```
<a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>

Then -1 times B (**-1B**) is:
```
-1 * B = [ (-1 * -7)  (-1 * 2) ]
         [ (-1 * 3)   (-1 * 5) ]
```
<a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>
```
-1 * B = [  7  -2 ]
         [ -3  -5 ]
```
<a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>

## Subtracting Matrices
Matrix subtraction is similar to addition, defined as adding the negative of the second matrix, or simply subtracting corresponding elements <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### Example of Matrix Subtraction
Using the same matrices A and B from the addition example:
```
A = [ 3 -1 ]
    [ 2  0 ]
```
```
B = [ -7  2 ]
    [  3  5 ]
```

**A - B** can be expressed as **A + (-1)B** <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
Using the result of **-1B**:
```
A - B = [  3 -1 ] + [  7  -2 ]
        [  2  0 ]   [ -3  -5 ]
```
<a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>

Adding corresponding elements:
```
A - B = [ (3 + 7)    (-1 + -2) ]
        [ (2 + -3)   (0 + -5)  ]
```
<a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
```
A - B = [  10  -3 ]
        [  -1  -5 ]
```
<a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>

Alternatively, one could directly subtract corresponding elements:
```
A - B = [ (3 - -7)  (-1 - 2) ]
        [ (2 - 3)   (0 - 5)  ]
```
```
A - B = [  10  -3 ]
        [  -1  -5 ]
```
<a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>

Like addition, matrices must be the same size to be subtracted <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

## Vectors
When a matrix has one of its dimensions equal to one (i.e., one row or one column), it is considered a vector <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Row Vector**: A matrix with one row and multiple columns (e.g., `[ -3 2 ]`) <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   **Column Vector**: A matrix with multiple rows and one column (e.g., `[ 9; 7 ]`) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.