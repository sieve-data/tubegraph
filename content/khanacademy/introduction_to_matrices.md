---
title: Introduction to matrices
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

Matrices are a fundamental concept in mathematics, often encountered in topics like [[introduction_to_algebra | algebra]] and computer science <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A matrix is simply a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The term "matrices" is the plural form of "matrix" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## [[Matrix notation and terminology | Matrix Notation]]

A matrix is typically represented by a capital letter, often bolded, such as **A** <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

An example of a matrix is:
```
A = [ 5  1  2 ]
    [ 3  0 -5 ]
```
<a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>

### [[Matrix dimensions and types | Matrix Dimensions]]
The size, or dimensions, of a matrix are described by its number of rows and columns <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The format is usually "rows by columns."
*   **Rows**: Horizontal lines of numbers <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Columns**: Vertical lines of numbers <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

The example matrix **A** above has 2 rows and 3 columns, making it a 2-by-3 matrix <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This can sometimes be written as 2x3 below the matrix's capital letter representation <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Another example:
```
B = [  0  -10 ]
    [ -5    3 ]
    [ 10    7 ]
    [  7    2 ]
    [  π    1 ]
```
<a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>
Matrix **B** has five rows and two columns, making it a 5-by-2 matrix <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

### Referencing Elements
Individual numbers within a matrix are called elements. Elements are referenced by their row and column position, typically written as A_row,column or a_row,column <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

Using matrix **A**:
```
A = [ 5  1  2 ]
    [ 3  0 -5 ]
```
*   The element in the second row, second column is 0. This is written as A_2,2 = 0 or a_2,2 = 0 <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   The element in the first row, third column is 2. This is written as A_1,3 = 2 or a_1,3 = 2 <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

### Vectors
When a matrix has one of its dimensions as one, it is often called a vector <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   **Row Vector**: A matrix with one row and multiple columns (e.g., `[ -3  2 ]` is a 1-by-2 matrix) <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   **Column Vector**: A matrix with multiple rows and one column (e.g., `[ 9 ]` <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>
    `[ 7 ]`
    is a 2-by-1 matrix) <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>.

## [[Applications and uses of matrices | Applications of Matrices]]

A matrix serves as a data representation, providing a structured way to organize numerical information <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. They are versatile and can represent a wide array of phenomena <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   In [[introduction_to_algebra | algebra]] classes, matrices are often used to represent [[introduction_to_linear_equations | linear equations]] <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
*   In computer graphics, elements of a matrix can represent pixels on a screen or points in coordinate space <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   It's important to note that a matrix is a human-defined concept for representing mathematical concepts or values, rather than a natural phenomenon itself <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## [[Adding and subtracting matrices | Matrix Operations]]

The operations defined for matrices are human conventions, designed to be useful for various applications <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### [[Adding and subtracting matrices | Adding Matrices]]
To add two matrices, you add their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

Let:
```
A = [ 3 -1 ]
    [ 2  0 ]
```
<a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>
And:
```
B = [ -7  2 ]
    [  3  5 ]
```
<a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>

Then **A** + **B** is calculated by adding each element in **A** to its corresponding element in **B**:
```
A + B = [ (3 + (-7))  (-1 + 2) ]
        [ (2 + 3)    (0 + 5)   ]
```
<a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>
```
A + B = [ -4  1 ]
        [  5  5 ]
```
<a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>

*   **Requirement for Addition**: Both matrices must have the exact same dimensions (same number of rows and same number of columns) <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. For example, a 1x2 matrix cannot be added to a 2x1 matrix <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   Matrix addition is commutative, meaning **A** + **B** = **B** + **A** <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

### Scalar Multiplication
When a matrix is multiplied by a single number (a scalar), every element within the matrix is multiplied by that scalar <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.

For example, given matrix **B**:
```
B = [ -7  2 ]
    [  3  5 ]
```
<a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>
Then -1 * **B** would be:
```
-1 * B = [ (-1 * -7)  (-1 * 2) ]
         [ (-1 * 3)   (-1 * 5) ]
```
<a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>
```
-1 * B = [  7 -2 ]
         [ -3 -5 ]
```
<a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>

### [[Adding and subtracting matrices | Subtracting Matrices]]
Matrix subtraction is defined as adding the first matrix to the second matrix multiplied by a scalar of -1 <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
So, **A** - **B** is equivalent to **A** + (-1 * **B**) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

Using the matrices **A** and **B** from above:
```
A - B = A + (-1 * B)
```
```
A - B = [  3 -1 ]  +  [  7 -2 ]
        [  2  0 ]     [ -3 -5 ]
```
<a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
```
A - B = [ (3 + 7)  (-1 + (-2)) ]
        [ (2 + (-3)) (0 + (-5)) ]
```
<a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
```
A - B = [ 10 -3 ]
        [ -1 -5 ]
```
<a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
Alternatively, you can directly subtract corresponding elements <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
*   **Requirement for Subtraction**: Like addition, both matrices must have the exact same dimensions <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.