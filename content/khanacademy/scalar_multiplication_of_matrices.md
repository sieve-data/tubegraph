---
title: Scalar multiplication of matrices
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

A [[definition_and_notation_of_matrices | matrix]] is a table of numbers, serving as a way to represent data <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. When working with [[definition_and_notation_of_matrices | matrices]], mathematical operations like addition, subtraction, and multiplication are defined by convention <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

## Definition of a Matrix
The plural of [[definition_and_notation_of_matrices | matrix]] is [[definition_and_notation_of_matrices | matrices]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. A [[definition_and_notation_of_matrices | matrix]] is simply a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>, <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Notation and Dimensions
[[definition_and_notation_of_matrices | Matrices]] are often represented by capital letters, sometimes bolded, such as a bold 'A' <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

The [[matrix_dimensions_and_conventions | dimensions]] of a [[definition_and_notation_of_matrices | matrix]] are described by its number of rows and columns <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. By convention, a [[matrix_dimensions_and_conventions | matrix]] is called "rows-by-columns" <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. For example, a [[matrix_dimensions_and_conventions | 2-by-3 matrix]] has two rows and three columns <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. A [[matrix_dimensions_and_conventions | 5-by-2 matrix]] would have five rows and two columns <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

Individual elements within a [[definition_and_notation_of_matrices | matrix]] can be referenced by their row and column position. For a [[definition_and_notation_of_matrices | matrix]] 'A', the element in the second row, second column, would be denoted as A(2,2) or a(2,2) <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Vectors
When one of a [[definition_and_notation_of_matrices | matrix]]'s [[matrix_dimensions_and_conventions | dimensions]] is one, it's referred to as a vector <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   A [[definition_and_notation_of_matrices | matrix]] with one row and multiple columns is a **row vector** <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   A [[definition_and_notation_of_matrices | matrix]] with multiple rows and one column is a **column vector** <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

## Scalar Multiplication
When you multiply a scalar (a single number) by a [[definition_and_notation_of_matrices | matrix]], you multiply that number by every single element within the [[definition_and_notation_of_matrices | matrix]] <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>, <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

### Example: Scalar Multiplication and Matrix Subtraction
[[adding_and_subtracting_matrices | Matrix subtraction]] can be conceptualized as a form of [[adding_and_subtracting_matrices | matrix addition]] combined with scalar multiplication.

Consider two [[definition_and_notation_of_matrices | matrices]], A and B:
$A = \begin{pmatrix} 3 & -1 \\ 2 & 0 \end{pmatrix}$ <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>
$B = \begin{pmatrix} -7 & 2 \\ 3 & 5 \end{pmatrix}$ <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

To calculate A - B, it's equivalent to A + (-1)B <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
First, perform the scalar multiplication of B by -1:
$(-1)B = (-1) \times \begin{pmatrix} -7 & 2 \\ 3 & 5 \end{pmatrix} = \begin{pmatrix} (-1) \times -7 & (-1) \times 2 \\ (-1) \times 3 & (-1) \times 5 \end{pmatrix} = \begin{pmatrix} 7 & -2 \\ -3 & -5 \end{pmatrix}$ <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>

Then, [[adding_and_subtracting_matrices | add matrices]] A and (-1)B by adding their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>:
$A + (-1)B = \begin{pmatrix} 3 & -1 \\ 2 & 0 \end{pmatrix} + \begin{pmatrix} 7 & -2 \\ -3 & -5 \end{pmatrix}$ <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>
$= \begin{pmatrix} 3+7 & -1+(-2) \\ 2+(-3) & 0+(-5) \end{pmatrix}$ <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
$= \begin{pmatrix} 10 & -3 \\ -1 & -5 \end{pmatrix}$ <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>

Alternatively, one could directly [[adding_and_subtracting_matrices | subtract]] the corresponding elements of B from A to arrive at the same result <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

<div class="callout" data-callout="info">
### Requirement for Addition/Subtraction
For [[adding_and_subtracting_matrices | matrix addition]] or [[adding_and_subtracting_matrices | subtraction]] to be possible, both [[definition_and_notation_of_matrices | matrices]] must have the same [[matrix_dimensions_and_conventions | dimensions]] (i.e., the same number of rows and columns) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
</div>