---
title: Matrix dimensions and conventions
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

## What is a Matrix?
A matrix is essentially a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The term "matrices" is simply the plural form of "matrix" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This concept is a fundamental part of mathematics, though often more familiar from popular culture than from academic settings <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

### Example
A matrix can be visualized as an arrangement of numbers, such as:
```
  5   1   2
  3   0  -5
```
This is an example of a matrix <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

## [[definition_and_notation_of_matrices | Notation and Representation]]
When using a variable to represent a matrix, a capital letter is typically used, often bolded in textbooks (e.g., **A**) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.

## Matrix Dimensions
The size of a matrix is defined by its dimensions, always expressed as `rows-by-columns` <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   The first number indicates the number of rows <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   The second number indicates the number of columns <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

For example, the matrix shown above (with 5, 1, 2 in the first row and 3, 0, -5 in the second) is a "2-by-3 matrix" because it has two rows and three columns <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. This dimension notation is sometimes written below the bold letter used to represent the matrix <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Example of Dimensions
A matrix **B** defined as a 5-by-2 matrix would have five rows and two columns <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>, <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>, <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
```
  0  -10
 -5    3
 10    7
  0    2
  1   pi
```

## Referencing Matrix Elements
Individual elements within a matrix can be referenced by their position using the row and column index. The general notation for an element in matrix A is A(row, column) or lowercase a with subscripts (e.g., a₂₂).
*   **A₂₂** (or **a₂₂**) refers to the element in the second row, second column <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   In the example matrix A above, the element in the second row, second column is 0 <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>, <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>, <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **A₁₃** (or **a₁₃**) refers to the element in the first row, third column <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. In the example matrix A, this value is 2 <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>, <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Matrices as Data Representation
A matrix is fundamentally a [[matrix_representation_in_data_and_applications | data representation]]—a way of organizing and writing down data <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>, <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. They are very powerful and can represent various phenomena:
*   In algebra, they are often used to represent linear equations <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   In computer graphics, elements can represent pixels on a screen or points in coordinate space <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Matrices themselves are not a natural phenomenon but a defined way to represent mathematical concepts or values <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

## Operations on Matrices
Many matrix operations, such as [[adding_and_subtracting_matrices | addition]], [[scalar_multiplication_of_matrices | multiplication]], inversion, and finding determinants, are human-defined conventions <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.

### [[adding_and_subtracting_matrices | Adding and Subtracting Matrices]]
To add two matrices, you add their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   **Condition**: Both matrices must have the same [[dimensions_in_geometry | dimensions]] (same number of rows and same number of columns) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>, <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. If they don't have corresponding elements, they cannot be added or subtracted <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>, <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>, <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>.
*   **Commutativity**: Matrix addition is commutative (A + B = B + A) <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

#### Example of Addition
Given matrix **A** and matrix **B**:
**A** = `[[3, -1], [2, 0]]` <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>, <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>
**B** = `[[-7, 2], [3, 5]]` <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>, <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>

**A + B** = `[[3 + (-7), -1 + 2], [2 + 3, 0 + 5]]` <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>, <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>, <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>, <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>
**A + B** = `[[-4, 1], [5, 5]]` <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>, <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>, <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>

### [[scalar_multiplication_of_matrices | Scalar Multiplication]]
When a scalar (a single number) is multiplied by a matrix, that number is multiplied by every single element within the matrix <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>, <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>, <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

#### Example of Scalar Multiplication in Subtraction
**A - B** can be expressed as **A + (-1 * B)** <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>, <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
**-1 * B** = `-1 * [[-7, 2], [3, 5]]` = `[[7, -2], [-3, -5]]` <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>, <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>

Then, **A + (-1 * B)** = `[[3 + 7, -1 + (-2)], [2 + (-3), 0 + (-5)]]`
**A - B** = `[[10, -3], [-1, -5]]` <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>, <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>, <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>, <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

## Vectors
A vector is a special type of matrix where one of its [[dimensions_in_geometry | dimensions]] is one <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>, <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   **Row vector**: A matrix with one row and multiple columns (e.g., `[-3, 2]`) <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>, <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>, <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   **Column vector**: A matrix with multiple rows and one column (e.g., `[[9], [7]]`) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.