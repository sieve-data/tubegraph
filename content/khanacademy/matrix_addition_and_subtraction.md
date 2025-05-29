---
title: Matrix addition and subtraction
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

A matrix is a fundamental concept in mathematics, simply defined as a table of numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. The term "matrices" is the plural of "matrix" <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Matrix Notation and Structure
Matrices are typically represented by a capital letter, often bolded (e.g., **A**) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

A matrix's dimensions are described by its number of rows and columns <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. For example, a matrix with two rows and three columns is called a 2-by-3 matrix <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. This can sometimes be written as "2 by 3" below the capital letter representing the matrix <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Referencing Elements
Individual elements within a matrix can be referenced by their row and column position <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. For a matrix A, the element in the second row and second column can be denoted as A(2,2) or a(2,2) <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Purpose of Matrices
A matrix is a data representation, a way of writing down data <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. They are very powerful and can represent various phenomena such as linear equations, pixels in computer graphics, or points in coordinate space <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. A matrix is not a natural phenomenon itself, but rather a way to represent mathematical concepts or values, requiring definition of what it represents <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

## Matrix Operations: Addition
Adding matrices is a human-defined convention that proves useful for various phenomena <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

### How to Add Matrices
When adding two matrices, you add their corresponding elements <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
For example, to find A + B for matrices:
**A** =
```
[ 3  -1 ]
[ 2   0 ]
```
**B** =
```
[ -7  2 ]
[  3  5 ]
```

The sum **A** + **B** is calculated by adding each element at the same position:
```
[ (3 + -7)   (-1 + 2) ]  =  [ -4   1 ]
[ (2 + 3)    (0 + 5)  ]     [  5   5 ]
```
The operations involved include [[adding_negative_numbers | adding negative numbers]] (e.g., 3 + -7 <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>).

### Conditions for Addition
For two matrices to be added, they must be the same size <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. This means they must have the same number of rows and columns <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. If matrices have different dimensions (e.g., a 1x2 matrix and a 2x1 matrix), they cannot be added or subtracted <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

### Commutative Property of Matrix Addition
By this definition, matrix addition follows [[understanding_the_commutative_property_of_addition | the commutative property of addition]]; that is, **A** + **B** will yield the same result as **B** + **A** <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>. This is analogous to how normal numbers add (e.g., 1 + 2 = 2 + 1) <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Matrix Operations: Subtraction
Matrix subtraction is very similar to addition.

### Scalar Multiplication of Matrices
Before performing subtraction, it's useful to understand [[scalar_multiplication_of_matrices | scalar multiplication of matrices]]. When a scalar (a single number) is multiplied by a matrix, that number is multiplied by *every* element within the matrix <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
For example, if **B** =
```
[ -7  2 ]
[  3  5 ]
```
Then -1 * **B** =
```
[ (-1 * -7)  (-1 * 2) ]  =  [  7  -2 ]
[ (-1 * 3)   (-1 * 5) ]     [ -3  -5 ]
```
<a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>

### How to Subtract Matrices
To subtract matrix **B** from matrix **A** (A - B), you can either:
1.  Subtract the corresponding elements directly <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.
2.  Add matrix **A** to the scalar product of -1 and matrix **B** (A + (-1)B) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

Using the previous example where **A** =
```
[ 3  -1 ]
[ 2   0 ]
```
And -1 * **B** =
```
[  7  -2 ]
[ -3  -5 ]
```
**A** + (-1)**B** =
```
[ (3 + 7)     (-1 + -2) ]  =  [ 10  -3 ]
[ (2 + -3)    (0 + -5)  ]     [ -1  -5 ]
```
<a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>

### Conditions for Subtraction
Similar to addition, matrices must have the same dimensions to be subtracted <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

## Terminology: Vectors
When one of a matrix's dimensions is one, it is often referred to as a vector <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
*   A matrix with one row and multiple columns (e.g., [ -3 2 ]) is called a **row vector** <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
*   A matrix with multiple rows and one column (e.g., [ 9; 7 ]) is called a **column vector** <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.
These terms are common in linear algebra and calculus <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.