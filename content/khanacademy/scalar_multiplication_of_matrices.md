---
title: Scalar multiplication of matrices
videoId: xyAuNHPsq-g
---

From: [[khanacademy]] <br/> 

Scalar multiplication of matrices involves multiplying a matrix by a single number, known as a scalar <a class="yt-timestamp" data-t="00:08:46"></a>.

## Definition and Process
When you multiply a scalar (a single number or value) by a matrix, you multiply that number by every single element within the matrix <a class="yt-timestamp" data-t="00:08:46"></a>, <a class="yt-timestamp" data-t="00:08:50"></a>, <a class="yt-timestamp" data-t="00:09:41"></a>.

For example, if you have a matrix B:
```
B = [-7  2]
    [ 3  5]
```
To find `-1 * B`, you would multiply each element in B by `-1` <a class="yt-timestamp" data-t="00:08:32"></a>, <a class="yt-timestamp" data-t="00:08:57"></a>:
```
-1 * B = [-1 * -7   -1 * 2]
         [-1 * 3    -1 * 5]
```
This results in the matrix:
```
-1 * B = [ 7  -2]
         [-3  -5]
```
<a class="yt-timestamp" data-t="00:09:00"></a>

## Application in Matrix Subtraction
Scalar multiplication is particularly useful when performing [[matrix_addition_and_subtraction | matrix subtraction]]. Subtracting one matrix (B) from another (A) is conventionally defined as adding matrix A to `(-1)` times matrix B <a class="yt-timestamp" data-t="00:08:32"></a>.

For example, given matrix A and matrix B:
```
A = [ 3 -1]
    [ 2  0]
```
```
B = [-7  2]
    [ 3  5]
```
To find `A - B`, it can be rewritten as `A + (-1 * B)` <a class="yt-timestamp" data-t="00:08:32"></a>.

First, calculate `-1 * B`:
```
-1 * B = [ 7  -2]
         [-3  -5]
```
Then, add the resulting matrix to A (following the rules for [[matrix_addition_and_subtraction | matrix addition]]):
```
A + (-1 * B) = [ (3 + 7)   (-1 + -2)]
               [ (2 + -3)  (0 + -5)]
```
Which yields:
```
A - B = [ 10  -3]
        [ -1  -5]
```
<a class="yt-timestamp" data-t="00:09:13"></a>, <a class="yt-timestamp" data-t="00:09:27"></a>

You can also directly subtract corresponding elements, which yields the same result <a class="yt-timestamp" data-t="00:09:29"></a>. However, understanding scalar multiplication helps to conceptualize matrix subtraction as a form of addition.