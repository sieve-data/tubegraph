---
title: Definition and notation of matrices
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

A matrix is fundamentally a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The term "matrices" is simply the plural form of "matrix" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Basic Structure and Representation

A matrix is a simple idea, essentially a structured collection of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. For example, a matrix might contain numbers like:
```
[ 5  1  2 ]
[ 3  0 -5 ]
```
<a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>

Matrices are often represented by capital letters, sometimes bolded, such as a bold 'A' <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Matrix Dimensions and Conventions

By convention, matrices are described by their [[matrix_dimensions_and_conventions | dimensions]], which are defined by the number of rows followed by the number of columns <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

*   **Rows** are the horizontal arrangements of numbers <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Columns** are the vertical arrangements of numbers <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

For instance, the example matrix above has two rows and three columns, making it a [[matrix_dimensions_and_conventions | 2-by-3 matrix]] <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This [[matrix_dimensions_and_conventions | dimension]] (e.g., 2 by 3) is sometimes written below the bold letter used to represent the matrix <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Another example, a [[matrix_dimensions_and_conventions | 5-by-2 matrix]], would have five rows and two columns <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

## Referencing Matrix Elements

Individual elements within a matrix can be referenced by their row and column position <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This is typically done using a lowercase letter corresponding to the matrix's variable, followed by two subscripts: the row number and then the column number <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

For matrix A:
```
A = [ 5  1  2 ]
    [ 3  0 -5 ]
```
*   The element `0` is in the second row, second column <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. It can be denoted as `A₂₂ = 0` or `a₂₂ = 0` <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   The element `2` is in the first row, third column <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It can be denoted as `A₁₃ = 2` or `a₁₃ = 2` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Purpose and Applications

A matrix serves as a [[matrix_representation_in_data_and_applications | data representation]]—a structured way of writing down data <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. While it's simply a table of numbers, it can represent various phenomena <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

Common applications include:
*   Representing [[matrix_representation_in_data_and_applications | linear equations]] in algebra <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   In [[matrix_representation_in_data_and_applications | computer graphics]], elements can represent pixels on a screen or points in coordinate space <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

It's crucial to understand that a matrix is a human-defined convention for representing values, not a natural phenomenon, and its meaning must be defined in context <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Basic Matrix Operations: Addition and Scalar Multiplication

The operations performed on matrices are defined by human convention for their utility <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### Matrix Addition
To [[adding_and_subtracting_matrices | add two matrices]], you sum their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

For example, if:
```
A = [  3 -1 ]
    [  2  0 ]

B = [ -7  2 ]
    [  3  5 ]
```
Then A + B is calculated as:
```
A + B = [ 3 + (-7)  -1 + 2 ]
        [ 2 + 3    0 + 5  ]

A + B = [ -4  1 ]
        [  5  5 ]
```
<a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>

Matrix addition is commutative, meaning A + B is the same as B + A <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

A key rule for [[adding_and_subtracting_matrices | matrix addition]] (and subtraction) is that both matrices *must* have the [[matrix_dimensions_and_conventions | same dimensions]] <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. You cannot add a 1x2 matrix to a 2x1 matrix, for instance, as they lack corresponding elements <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

### Scalar Multiplication
When multiplying a [[scalar_multiplication_of_matrices | scalar]] (a single number) by a matrix, you multiply every element of the matrix by that scalar <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

For example, if `B = [ -7 2 ]`
`[ 3 5 ]`
Then, `-1 * B` would be:
```
-1 * B = [ -1 * (-7)  -1 * 2 ]
         [ -1 * 3     -1 * 5 ]

-1 * B = [  7  -2 ]
         [ -3  -5 ]
```
<a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>

### Matrix Subtraction
[[adding_and_subtracting_matrices | Matrix subtraction]] works similarly to addition, by subtracting corresponding elements <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. Alternatively, `A - B` can be viewed as `A + (-1 * B)` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

## Vectors (Special Cases)
When one of a matrix's [[matrix_dimensions_and_conventions | dimensions]] is one, it is referred to as a vector <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   A matrix with one row and multiple columns is a **row vector** (e.g., `[ -3 2 ]`) <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   A matrix with multiple rows and one column is a **column vector** (e.g., `[ 9 ]`
`[ 7 ]`) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.