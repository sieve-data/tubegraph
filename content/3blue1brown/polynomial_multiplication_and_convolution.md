---
title: Polynomial Multiplication and Convolution
videoId: KuXjwB4LzSA
---

From: [[3blue1brown]] <br/> 

Convolution is a fundamental method for combining two lists of numbers or two functions to produce a new list or function, distinct from simple term-by-term addition or multiplication <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Unlike these simpler operations, convolution is not merely inherited from numerical operations but is something genuinely new for lists or functions <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Its definition can appear intimidating without context, but it is an "incredibly beautiful operation" when unpacked and motivated <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Ubiquity of Convolution
Convolutions are [[fourier_transforms_and_convolutions_in_integral_computation | ubiquitous]] in various fields:
*   Image processing <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   Probability theory <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>
*   Solving differential equations <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>
*   Multiplying two polynomials together <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>

This article primarily focuses on the discrete case of convolution <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Understanding Convolution Through Examples

### Probability Distributions (Discrete Case)
One of the simplest examples of convolution arises when calculating the probability of sums when rolling a pair of dice <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
If each die has an equal chance for each face, you can count the pairs that sum to a given number by arranging them in a grid and observing how sums align along diagonals <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.

A key visualization for convolution in this context involves two rows representing the dice outcomes. If you flip the second row and slide it past the first, the values that align vertically for a given offset sum to a particular total <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. For example, to find pairs that sum to seven, align the flipped second row so these pairs line up vertically <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

If the dice are *not* uniform (i.e., they have different probabilities for each face), finding the probability of a sum involves:
1.  Identifying all pairs of outcomes that sum to the target number <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
2.  Multiplying the probabilities of the individual outcomes in each pair <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
3.  Adding these products together <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

This process of taking two arrays of numbers, flipping the second one, and then lining them up at various offsets to take pairwise products and sum them up, is a fundamental way to understand convolution <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Alternatively, you can create a table of all pairwise products and then sum along the diagonals <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

Mathematically, the convolution of `a` and `b`, denoted `a * b`, yields a new list where the `n`th element is the sum over all pairs of indices `i` and `j` such that `i + j = n` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

### Moving Averages and Image Processing
Convolution can also be used for:
*   **Moving Average:** Convolving a list of numbers with a smaller list (where elements sum to 1, e.g., all 1/5) results in a smoothed-out version of the original data, representing a moving average within a sliding window <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   **Image Blurring:** This is a two-dimensional analog of a moving average <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. A small grid of values (e.g., 3x3 with each value 1/9) is marched across an image. At each step, the grid's values are multiplied by the corresponding pixel values (represented as [[vector_addition_and_scalar_multiplication | vectors]] of RGB components) and summed to determine the new pixel value for the output image <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. This process averages neighboring pixels, creating a blur <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
    *   Using a [[generating_functions_and_polynomials | Gaussian distribution]] for the grid's values (kernel) gives more weight to the central pixel, simulating out-of-focus lenses more authentically <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Edge Detection:** By choosing a different "kernel" (the small grid of values), such as one with positive values on one side and negative on the other, convolution can detect variations in pixel values, like vertical or horizontal edges <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. If the sum of kernel values is zero, areas of uniform color will result in zero, highlighting only transitions <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

In pure mathematics, the definition of convolution implies flipping around the second array (or kernel) <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. While this might seem "uncalled for" in some computer science contexts (especially if the kernel is symmetric), it is a natural part of the mathematical definition and is crucial for understanding its connection to other operations <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
The output of a pure mathematical convolution is always larger than the input arrays (unless one has a length of one), though in computer science, it's often truncated <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>.

## Convolution and Polynomial Multiplication

One context where convolution is "especially natural" is when multiplying two [[generating_functions_and_polynomials | polynomials]] <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
If you have two polynomials, say \(A(x) = a_1 + a_2x + a_3x^2\) and \(B(x) = b_1 + b_2x + b_3x^2\), and you form a multiplication table of all pairwise products of their terms (e.g., \(a_i \cdot b_j\)), then adding these products along diagonals corresponds to collecting like terms after expanding the full polynomial product <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

This means that expanding a polynomial product and collecting like terms is *exactly the same process* as a convolution of their coefficients <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### Computational Efficiency
Directly computing a convolution or multiplying polynomials by filling out a grid of pairwise products and summing diagonals requires a number of operations proportional to \(n^2\) (O(n²)), where \(n\) is the size of the lists/number of coefficients <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>. For two lists of 100 elements, this means around 10,000 products and 10,000 additions <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

However, there's a more efficient approach leveraging the connection between polynomial multiplication and convolution:
1.  **Polynomial Multiplication via Pointwise Product:** Multiplying two functions (like polynomials) by sampling their values at a handful of inputs and then multiplying those samples point-wise requires far fewer operations <a class="yt-timestamp" data-t="00:17:06">[00:17:06]</a>. For polynomials, finitely many samples are sufficient to uniquely recover the coefficients <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. For instance, `n` distinct outputs are enough to uniquely specify a polynomial with `n` coefficients <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.

2.  **[[Fast Fourier Transform and Convolution | Fast Fourier Transform]] (FFT):** The crucial trick to make this approach efficient lies in the choice of evaluation points. Instead of arbitrary inputs (like 0, 1, 2...), evaluating polynomials at a specially selected set of [[complex_numbers_multiplication_and_rotation | complex numbers]]—specifically, points evenly spaced on the unit circle known as the roots of unity—simplifies the system of equations for recovering coefficients <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. This specific set of outputs is called the **discrete Fourier transform** of the coefficients <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.

    The [[Fast Fourier Transform and Convolution | Fast Fourier Transform]] (FFT) is an algorithm that can compute these transforms (and their inverses) much more quickly due to redundancy in calculations. It reduces the computational complexity from O(n²) to O(n log n) <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

### FFT-based Convolution Algorithm
To convolve two long lists of numbers using the FFT:
1.  Compute the [[Fast Fourier Transform and Convolution | Fast Fourier Transform]] of each list (treating them as polynomial coefficients and evaluating at special points) <a class="yt-timestamp" data-t="00:5:52">[00:05:52]</a>.
2.  Multiply the two resulting transforms point-wise <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.
3.  Perform an inverse [[Fast Fourier Transform and Convolution | Fast Fourier Transform]] on the product <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

This "sneaky backdoor way" to compute the convolution significantly reduces the number of operations to O(n log n) <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>. For example, convolving two arrays of 100,000 random elements takes approximately 4.87 seconds using a direct convolution function (NumPy) versus 4.3 milliseconds using an FFT-based function (SciPy), demonstrating a three orders of magnitude improvement <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.

## Further Implications
This connection between polynomial multiplication and convolution, facilitated by the [[Fast Fourier Transform and Convolution | Fast Fourier Transform]], is relevant wherever convolutions appear, including large image processing or adding probability distributions <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.

As a thought experiment, ordinary multiplication of two numbers can be seen as a convolution of their digits, with added steps for carries <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. This implies that for very large integers, there exists an O(n log n) algorithm for multiplication, faster than the O(n²) method taught in elementary school, though it's practically useful only for "absolutely monstrous" numbers <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.