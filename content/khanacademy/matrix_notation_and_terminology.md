---
title: Matrix notation and terminology
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

A [[introduction_to_matrices | matrix]] is defined as a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The term "[[introduction_to_matrices | matrices]]" is simply the plural form of [[introduction_to_matrices | matrix]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Representing Matrices

Matrices are typically represented using a capital letter, often bolded, such as **A** <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

For example, a [[introduction_to_matrices | matrix]] **A** could look like this:
```
[ 5  1  2 ]
[ 3  0 -5 ]
```
<a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>

## Matrix Dimensions

The [[matrix_dimensions_and_types | dimensions]] of a [[introduction_to_matrices | matrix]] describe its size by specifying the number of rows and columns <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This is expressed as "rows by columns" <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

For the example [[introduction_to_matrices | matrix]] **A** above:
*   It has two rows <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   It has three columns <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
Therefore, **A** is a 2-by-3 [[introduction_to_matrices | matrix]] <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This is sometimes written as "2 by 3" below the bold letter representing the [[introduction_to_matrices | matrix]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Another example: If **B** is a 5-by-2 [[introduction_to_matrices | matrix]] <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>, it means **B** would have five rows and two columns <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
```
[  0  -10 ]
[ -5    3 ]
[ 10    7 ]
[  .    2 ]
[  .   pi ]
```
<a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>

### Referencing Individual Elements
Individual elements within a [[introduction_to_matrices | matrix]] can be referenced by their row and column position <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. This [[understanding_basic_algebraic_notation | notation]] typically uses the [[introduction_to_matrices | matrix]]'s letter (lowercase or capital) followed by its row and column indices <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

For [[introduction_to_matrices | matrix]] **A**:
*   The element `0` is in the second row and second column <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. It can be written as A(2,2) = 0 or a(2,2) = 0 <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   The element `2` is in the first row and third column <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. It can be written as A(1,3) = 2 or a(1,3) = 2 <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Purpose of Matrices

A [[introduction_to_matrices | matrix]] is fundamentally a data representation tool, a way of writing down data in a structured table of numbers <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. They can be used to represent a wide range of phenomena <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.

Common applications include:
*   Representing linear equations <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   Computer graphics, where elements might represent pixels or points in coordinate space <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

It's important to understand that a [[introduction_to_matrices | matrix]] itself is not a natural phenomenon, but rather a method to represent mathematical concepts or values, and its specific representation needs to be defined within a given context <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Matrix Operations

### Adding Matrices
To [[adding_and_subtracting_matrices | add two matrices]], you add their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. This is a human-defined convention that proves useful <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

For example, if:
**A** = `[ 3  -1 ]`
    `[ 2   0 ]`
<a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>
and
**B** = `[ -7  2 ]`
    `[  3  5 ]`
<a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

Then **A** + **B** is calculated by adding the elements in the same positions:
**A** + **B** = `[ (3 + (-7))  (-1 + 2) ]`
            `[ (2 + 3)    (0 + 5)   ]`
            `[ -4   1 ]`
            `[  5   5 ]`
<a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>

For [[adding_and_subtracting_matrices | matrix addition]], the order does not matter (A + B = B + A) <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### Scalar Multiplication
When multiplying a scalar (a single number) by a [[introduction_to_matrices | matrix]], you multiply that number by every one of the [[introduction_to_matrices | matrix]]'s elements <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

For example, if **B** = `[ -7  2 ]`
                    `[  3  5 ]`
Then, -1 * **B** = `[ (-1 * -7)  (-1 * 2) ]`
                 `[ (-1 * 3)   (-1 * 5)  ]`
                 `[  7  -2 ]`
                 `[ -3  -5 ]`
<a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>

### Subtracting Matrices
[[adding_and_subtracting_matrices | Matrix subtraction]] is similar to [[adding_and_subtracting_matrices | matrix addition]], performed element-wise <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. Alternatively, subtracting a [[introduction_to_matrices | matrix]] B from A (A - B) is equivalent to A + (-1 * B) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

Using the examples above, **A** - **B**:
**A** - **B** = `[ (3 - (-7))  (-1 - 2) ]`
            `[ (2 - 3)    (0 - 5)   ]`
            `[ 10  -3 ]`
            `[ -1  -5 ]`
<a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>

### Dimensional Requirements for Addition/Subtraction
For [[adding_and_subtracting_matrices | matrix addition]] or [[adding_and_subtracting_matrices | subtraction]] to be possible, both matrices must have the exact same [[matrix_dimensions_and_types | dimensions]] (same number of rows and same number of columns) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. If [[introduction_to_matrices | matrices]] have different [[matrix_dimensions_and_types | dimensions]], they cannot be added or subtracted <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

## Vector Terminology
When a [[introduction_to_matrices | matrix]] has one of its [[matrix_dimensions_and_types | dimensions]] equal to one, it is referred to as a vector <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   A [[introduction_to_matrices | matrix]] with one row and multiple columns (e.g., 1x2) is called a **row vector** <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
    *   Example: `[ -3  2 ]` <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>
*   A [[introduction_to_matrices | matrix]] with multiple rows and one column (e.g., 2x1) is called a **column vector** <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
    *   Example: `[ 9 ]`
                `[ 7 ]`
<a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>