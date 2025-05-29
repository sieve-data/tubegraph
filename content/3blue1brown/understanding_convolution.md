---
title: Understanding Convolution
videoId: KuXjwB4LzSA
---

From: [[3blue1brown]] <br/> 

Convolution is a fundamental operation for combining two lists of numbers or two functions to produce a new list or function <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Unlike simpler operations like term-by-term addition or multiplication, convolution is a genuinely new type of combination specific to lists or functions <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. While its formulaic definition can appear intimidating without context <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, understanding its underlying motivation reveals it to be a beautiful operation <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

## Ubiquitous Applications

Convolutions are widely used across various fields:
*   [[applications_of_convolution_in_probability_and_image_processing | Image processing]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   The theory of probability <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   Solving differential equations <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   [[use_of_convolution_in_polynomial_multiplication | Multiplying two polynomials together]] <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>

The discussion in this article primarily focuses on the [[discrete_convolution_algorithm | discrete case]] <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>, building towards a clever algorithm for its computation <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. The continuous case is often addressed separately <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Probability Example: Rolling Dice

A simple example of convolution in probability involves rolling a pair of dice and determining the chances of seeing various sums <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.
Conventionally, one might list all 36 distinct pairs of outcomes and count how many pairs result in a given sum <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. Pairs with a constant sum align along diagonals in a grid representation <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.

An alternative visualization involves picturing the possibilities for each die in a row, then flipping the second row <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. When the rows are slid past each other, all pairs that add up to a specific sum line up vertically <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. For example, sliding the bottom row all the way to the right aligns only the pair that adds up to two <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>. Subsequent slides reveal pairs that add up to other sums, such as three (two pairs) <a class="yt-timestamp" data-t="03:28:00">[03:28:00]</a>. Different offset values of the flipped lower array reveal all distinct pairs with a given sum <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

This concept becomes particularly relevant with non-uniform dice, where each face has a specific probability <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>. To find the probability of a specific sum (e.g., 3), you multiply the probabilities of the corresponding pairs (e.g., blue die 1 & red die 2; blue die 2 & red die 1) and add those products together <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>. This process—taking two arrays, flipping the second, lining them up at various offsets, taking pairwise products, and summing them—is a fundamental way to understand convolution <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

The result is a new sequence (e.g., 11 values for two dice), where each value is a sum of pairwise products <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>. Alternatively, one could create a table of all pairwise products and then sum along the diagonals <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.

### Notation and Simple Example
The convolution of two lists `a` and `b`, denoted with an asterisk `a * b`, produces a new list <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. The `n`th element of this new list is a sum over all pairs of indices `i` and `j` such that `i + j = n` <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.

```
Example: Convolve [1, 2, 3] with [4, 5, 6]
1.  Flip the second list: [6, 5, 4]
2.  Align and multiply:
    *   Offset 0: 1 * 4 = 4 (First term) <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>
    *   Offset 1: (1 * 5) + (2 * 4) = 5 + 8 = 13 (Second term) <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>
    *   Offset 2: (1 * 6) + (2 * 5) + (3 * 4) = 6 + 10 + 12 = 28 (Third term) <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>
    *   Offset 3: (2 * 6) + (3 * 5) = 12 + 15 = 27 (Fourth term) <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>
    *   Offset 4: (3 * 6) = 18 (Fifth term) <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>
Result: [4, 13, 28, 27, 18] <a class="yt-timestamp" data-t="07:18:00">[07:18:00]</a>
```

### Moving Averages and Smoothing Data
Convolution can also be used for computing a moving average <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>. If you have a long list of numbers and convolve it with a smaller list whose values sum to 1 (e.g., `[1/5, 1/5, 1/5, 1/5, 1/5]`), the result is a smoothed version of the original data <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>. At each iteration, the operation averages the data within a small "window" <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>. By modifying the smaller list (often called a "kernel"), you can achieve different weighted moving averages, giving more weight to central values, for instance <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.

### Image Processing
A two-dimensional analog of this process provides algorithms for [[applications_of_convolution_in_probability_and_image_processing | blurring images]] <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>. A small grid of values (e.g., a 3x3 grid where each value is 1/9) marches across the image <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>. Each value in the grid is multiplied by the corresponding pixel value, and these products are summed to define a pixel in the output image <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>. For color images, this averaging happens across red, green, and blue channels <a class="yt-timestamp" data-t="09:17:00">[09:17:00]</a>. This causes each pixel to bleed into its neighbors, resulting in a blur <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>.

More sophisticated blurring can be achieved with a kernel sampled from a [[graphical_intuition_versus_transformational_understanding_in_calculus | bell curve]] (Gaussian distribution), where the central values are larger than those at the edges <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>. This gives more weight to the central pixel, simulating an out-of-focus lens <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.

Beyond blurring, different kernels can achieve other image processing effects:
*   **Edge Detection**: A kernel with positive numbers on one side and negative numbers on the other (e.g., left positive, right negative) can detect variations in pixel value, highlighting vertical edges <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>. If the kernel sums to zero, uniform patches of color will result in zero, emphasizing changes <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>. Rotating such a kernel detects horizontal edges <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>.
*   **Sharpening**: Other kernels can sharpen images <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>.

In convolutional neural networks, the kernels themselves are learned from data to detect specific features <a class="yt-timestamp" data-t="12:44:00">[12:44:00]</a>.

[!NOTE]
In the pure mathematical context, the definition of convolution always involves flipping the second array or kernel before the sliding window operation <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>. While this doesn't matter for symmetric kernels (like the blurring examples), it's crucial for understanding the operation fully <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>. Computer science contexts sometimes omit this flip, but the pure math definition is where it naturally arises, as seen in probability examples <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>.

The output length of a convolution is generally larger than the input arrays (unless one input has a length of one) <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>. However, in certain computer science applications (e.g., image processing), the output is often deliberately truncated to match the size of the original input <a class="yt-timestamp" data-t="13:16:00">[13:16:00]</a>.

## Efficient Computation of Convolution

Directly computing a convolution involves many pairwise products and sums. For two lists of size `n`, this process is typically O(n²) <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>, meaning the number of operations scales with the square of `n` <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>. For large lists, this can be very slow <a class="yt-timestamp" data-t="13:56:00">[13:56:00]</a>.

### Connection to Polynomial Multiplication
A powerful insight into convolution comes from its connection to [[use_of_convolution_in_polynomial_multiplication | multiplying two polynomials]] <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. If you consider the coefficients of two polynomials as lists, expanding their product involves creating a multiplication table of all pairwise products <a class="yt-timestamp" data-t="15:13:00">[15:13:00]</a>. Collecting like terms in the polynomial product corresponds exactly to summing along the diagonals of this table, which is the same process as a convolution <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>.

This implies that multiplying two functions (like polynomials) point-wise is equivalent to convolving their coefficients <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>. While convolution seems more complicated, this relationship is key to a faster algorithm <a class="yt-timestamp" data-t="16:09:00">[16:09:00]</a>.

For polynomials, if you sample their values at enough inputs, you can recover their coefficients <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>. For example, `n` distinct outputs are enough to uniquely specify a polynomial with `n` coefficients <a class="yt-timestamp" data-t="17:29:00">[17:29:00]</a>. This leads to a theoretical algorithm:
1.  Treat the lists to be convolved as polynomial coefficients <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a>.
2.  Sample those polynomials at enough outputs <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>.
3.  Multiply these samples point-wise <a class="yt-timestamp" data-t="18:20:00">[18:20:00]</a>.
4.  Solve the resulting system of equations to recover the convolution (coefficients) <a class="yt-timestamp" data-t="18:24:00">[18:24:00]</a>.

Initially, this approach seems inefficient because sampling and solving the system are also O(n²) operations <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>.

### The Power of the [[fast_fourier_transform_and_its_role_in_efficient_convolution | Fast Fourier Transform]]
The trick to making this process efficient lies in the choice of sampling points <a class="yt-timestamp" data-t="19:01:00">[19:01:00]</a>. Instead of arbitrary inputs, evaluating the polynomials at a specially selected set of [[complex_numbers_introduction | complex numbers]]—specifically, the roots of unity evenly spaced on the unit circle—creates a "friendlier system" <a class="yt-timestamp" data-t="19:24:00">[19:24:00]</a>. This choice introduces redundancy that can be leveraged to save computational work <a class="yt-timestamp" data-t="19:46:00">[19:46:00]</a>.

This specific set of outputs is called the discrete Fourier transform (DFT) of the coefficients <a class="yt-timestamp" data-t="19:56:00">[19:56:00]</a>. The [[fast_fourier_transform_and_its_role_in_efficient_convolution | Fast Fourier Transform (FFT)]] is an algorithm that computes these transforms much faster, reducing the number of operations from O(n²) to O(n log n) <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>. Crucially, the FFT algorithm works in both directions, allowing conversion from coefficients to outputs and back again <a class="yt-timestamp" data-t="20:39:00">[20:39:00]</a>.

This leads to a much faster algorithm for convolution, often referred to as the [[convolution_theorem_and_its_mathematical_significance | Convolution Theorem]]:
1.  Compute the [[fast_fourier_transform_and_its_role_in_efficient_convolution | Fast Fourier Transform]] of each of the two lists <a class="yt-timestamp" data-t="20:52:00">[20:52:00]</a>.
2.  Multiply the two resulting FFTs together point-wise <a class="yt-timestamp" data-t="21:06:00">[21:06:00]</a>.
3.  Perform an inverse [[fast_fourier_transform_and_its_role_in_efficient_convolution | Fast Fourier Transform]] on the product <a class="yt-timestamp" data-t="21:10:00">[21:10:00]</a>.
This process yields the convolution result in O(n log n) operations <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>, a significant improvement over the direct O(n²) method <a class="yt-timestamp" data-t="14:25:00">[14:25:00]</a>. This powerful connection from [[use_of_convolution_in_polynomial_multiplication | polynomial multiplication]] makes the FFT-based algorithm relevant for any application of convolution, from probability to image processing <a class="yt-timestamp" data-t="21:25:00">[21:25:00]</a>.

[!NOTE]
Standard long multiplication of numbers, as learned in elementary school, can be thought of as a convolution between the digits of those numbers, with additional steps for carries <a class="yt-timestamp" data-t="21:51:00">[21:51:00]</a>. The existence of the FFT-based convolution algorithm implies that there is a way to multiply very large integers faster than the O(n²) method learned in school, achieving O(n log n) efficiency <a class="yt-timestamp" data-t="22:07:00">[22:07:00]</a>. This is practically useful for "monstrously" large numbers <a class="yt-timestamp" data-t="22:25:00">[22:25:00]</a>.

The discussion will next focus on the continuous case of convolution, particularly in the context of probability distributions <a class="yt-timestamp" data-t="22:35:00">[22:35:00]</a>.