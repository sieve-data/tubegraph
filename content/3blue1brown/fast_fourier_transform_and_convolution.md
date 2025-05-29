---
title: Fast Fourier Transform and Convolution
videoId: KuXjwB4LzSA
---

From: [[3blue1brown]] <br/> 

Convolution is a fundamental mathematical operation for combining two lists of numbers or two functions, distinct from simple addition or term-by-term multiplication <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. It introduces a genuinely new method of combination specific to lists and functions <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

Convolutions are ubiquitous, appearing in:
*   Image processing <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   Probability theory <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   Solving differential equations <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   Multiplying polynomials <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>

While its formulaic definition can seem intimidating, convolution is a beautiful operation when its underlying principles and motivations are understood <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This article primarily focuses on the discrete case of convolution <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Visualizing Discrete Convolution

One of the simplest ways to understand convolution is through the example of rolling a pair of dice and figuring out the chances of various sums <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### The "Sliding Array" Method
Consider two lists of possibilities, such as the outcomes of two dice.
1.  Picture the two lists in rows <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  Flip the second row around <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
3.  Slide the flipped second row across the first row, aligning it at different offset values <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
4.  At each offset, multiply the corresponding aligned pairs of numbers and sum these products <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
This process reveals all distinct pairs that have a given sum <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This "sliding window" approach, where the second array is flipped, is a fundamental way to think about convolution <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>, <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

### The "Multiplication Table" Method
Another perspective is to:
1.  Create a table of all pairwise products of the numbers from the two lists <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>.
2.  Add up the products along the diagonals of this table <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
Each diagonal sum corresponds to one of the final outputs of the convolution <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

### Formal Notation
The convolution of two sequences `a` and `b`, denoted `a * b`, produces a new list where the nth element is a sum over all pairs of indices `i` and `j` such that their sum equals `n` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Applications of Convolution

### Probability Distributions
Convolution naturally arises when combining probability distributions, especially for events with non-uniform probabilities, such as "special" dice <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. To find the probability of a specific sum, one multiplies the probabilities of corresponding outcomes for each die and adds these products together <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>, <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This process generates a new sequence of probabilities, which is the convolution of the individual probability distributions <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Moving Averages and Smoothing
A moving average can be interpreted as a convolution <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. If you have a long list of numbers (data) and a smaller list (kernel) whose values sum to 1 (e.g., all values are 1/5), applying the sliding window convolution process effectively calculates an average of the data within the window <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>, <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This results in a smoothed-out version of the original data <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. Different kernels can apply different weights to the central values, leading to varied smoothing effects <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>, <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

### Image Processing
In image processing, a two-dimensional analog of convolution is used <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. A small grid of values, called a **kernel** <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>, marches across the image. At each step, kernel values are multiplied by corresponding pixel values (e.g., RGB components) and summed to determine the new pixel value in the output image <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Blurring:** Using a kernel where all values sum to 1 (e.g., 1/9th for a 3x3 grid) calculates an average along each color channel, causing pixels to bleed into their neighbors, resulting in a blurred image <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>, <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>, <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. A Gaussian distribution for kernel values, giving more weight to the central pixel, creates a more natural blurring effect <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>, <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **Edge Detection:** A kernel with both positive and negative values that sum to zero (e.g., positive on one side, negative on the other) can detect variations in pixel values <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>, <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. This highlights edges, such as vertical or horizontal lines in an image <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>, <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.
Different kernels allow for various image processing effects, including sharpening <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>, <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>. In convolutional neural networks, the kernels themselves are learned from data <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

## Convolution and Polynomial Multiplication

One context where the "multiplication table" view of convolution is especially natural is when multiplying two polynomials <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. If the coefficients of two polynomials are treated as lists of numbers, their product (expanded out fully) involves all pairwise products, and collecting like terms (which correspond to diagonals in the multiplication table) is exactly equivalent to performing a convolution of their coefficient lists <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>, <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>, <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>, <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

This connection reveals a powerful insight: multiplying two functions (like polynomials) by simple pointwise operation is equivalent to taking the convolution of their coefficients <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

## Computational Complexity and the [[fourier_transforms_and_convolutions_in_integral_computation|Fast Fourier Transform]]

Directly computing a convolution for two lists of size 'n' (e.g., using the multiplication table method) requires approximately n² operations <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>, making it an O(n²) algorithm <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. For large lists, this can be computationally expensive. For example, convolving two arrays of 100,000 random elements can take several seconds <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

### The [[introduction_to_fourier_transform|Fast Fourier Transform]] (FFT) Algorithm
While simple polynomial multiplication by sampling outputs is faster (pointwise multiplication is O(n)) <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>, the process of converting coefficients to sampled outputs and back (solving systems of equations) is typically just as difficult as the convolution itself <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.

The trick lies in evaluating the polynomials at a very specially selected set of [[complex_numbers_and_fourier_transform|complex numbers]]: the ones that sit evenly spaced on the unit circle, known as the roots of unity <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>, <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>. This choice creates a system with significant redundancy in calculations, which can be leveraged for efficiency <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.

This set of outputs is called the [[introduction_to_fourier_transform|discrete Fourier transform]] (DFT) of the coefficients <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>, <a class="yt-timestamp" data-t="00:19:58">[00:19:58]</a>. The [[fourier_transforms_and_convolutions_in_integral_computation|Fast Fourier Transform]] (FFT) is an algorithm that computes these [[introduction_to_fourier_transform|discrete Fourier transforms]] much more quickly than O(n²) <a class="yt-timestamp" data-t="00:20:11">[00:20:11]</a>. The FFT reduces the computational complexity from O(n²) to O(n log n) for both transforming coefficients to outputs and outputs back to coefficients <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>, <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>, <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.

### The Convolution Theorem
The connection between convolution and the [[fourier_transforms_and_convolutions_in_integral_computation|Fast Fourier Transform]] leads to a powerful algorithm for computing convolutions rapidly:
1.  Compute the [[fourier_transforms_and_convolutions_in_integral_computation|Fast Fourier Transform]] of each of the two lists you want to convolve <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>, <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
2.  Multiply the two resulting [[introduction_to_fourier_transform|Fourier transforms]] together pointwise <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. This step is very fast <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
3.  Perform an inverse [[fourier_transforms_and_convolutions_in_integral_computation|Fast Fourier Transform]] on the product from step 2 <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

This three-step process is a "sneaky backdoor way" to compute the convolution with an O(n log n) complexity <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>, <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>. This significantly improves performance, e.g., reducing runtime from 4.87 seconds to 4.3 milliseconds for large arrays <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>, <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.

This demonstrates the profound implications when a mathematical operation like convolution connects to seemingly unrelated areas (like polynomial multiplication and [[fourier_transforms_and_convolutions_in_integral_computation|Fourier transforms]]), opening doors for faster algorithms applicable across many fields <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>, <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

## Further Implications
The existence of an O(n log n) algorithm for convolution implies that even ordinary multiplication of very large integers can be performed faster than the elementary school method, as integer multiplication can be viewed as a convolution of their digits with added "carry" steps <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>, <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>, <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.