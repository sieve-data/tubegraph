---
title: Fast Fourier Transform and its Role in Efficient Convolution
videoId: KuXjwB4LzSA
---

From: [[3blue1brown]] <br/> 

[[understanding_convolution | Convolution]] is a fundamental operation for combining two lists of numbers or functions, distinct from simple addition or term-by-term multiplication <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. It represents something genuinely new for combining sequences <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

The definition of [[understanding_convolution | convolution]] can appear intimidating without context, but it is an incredibly beautiful operation when understood <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This article focuses on the discrete case and an unexpected, clever algorithm for computing convolutions <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

## Applications of Convolution

[[applications_of_convolution_in_probability_and_image_processing | Convolutions]] are ubiquitous and appear in various fields:
*   **Image Processing**: A core component <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Probability Theory**: A fundamental construct <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   **Solving Differential Equations**: Widely used <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   **Polynomial Multiplication**: Used when multiplying two polynomials together <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Understanding Discrete Convolution

### Probability Distributions (Dice Example)

A simple example of [[understanding_convolution | convolution]] arises when calculating the sum probabilities of rolling a pair of dice <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. While one can simply count pairs in a grid <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>, another visualization involves two sets of outcomes, where the second is flipped and slid along the first <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Different offset values reveal distinct pairs that sum to a given total <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

This concept becomes especially useful with non-uniform dice, where each face has a specific probability <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. To find the probability of a sum (e.g., 3), one multiplies the probabilities of corresponding pairs (e.g., blue die 1 and red die 2, or blue die 2 and red die 1) and adds these products <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

This process of taking two arrays, flipping the second, sliding it, taking pairwise products, and summing them up is a fundamental way to think about what a [[understanding_convolution | convolution]] is <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

Mathematically, the [[understanding_convolution | convolution]] of two sequences `a` and `b`, denoted `a * b`, yields a new sequence where the `n`-th element is a sum of pairwise products `a_i * b_j` such that `i + j = n` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. For example, for `n=6`, pairs `(i,j)` include `(1,5), (2,4), (3,3), (4,2), (5,1)` <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

> ##### Example
> The [[understanding_convolution | convolution]] of `[1, 2, 3]` with `[4, 5, 6]` is calculated by:
> *   Sliding the flipped `[6, 5, 4]` (from `[4, 5, 6]`) across `[1, 2, 3]`.
> *   `1 * 4 = 4` (first term) <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>
> *   `1 * 5 + 2 * 4 = 13` (second term) <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>
> *   `1 * 6 + 2 * 5 + 3 * 4 = 28` (third term) <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>
> *   `2 * 6 + 3 * 5 = 27` (fourth term) <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>
> *   `3 * 6 = 18` (fifth term) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>
> The result is `[4, 13, 28, 27, 18]` <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

### Moving Averages and Image Processing

[[applications_of_convolution_in_probability_and_image_processing | Convolution]] is also used for calculating moving averages, where a smaller list of numbers (a "kernel") summing to 1 is convolved with a longer data list <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. This process smooths out the original data <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.

A two-dimensional analog of this process is used in image processing for effects like blurring <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. A small grid of values (e.g., 3x3 where each is 1/9) marches across an image, multiplying its values by corresponding pixel values and summing them to define a new pixel <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. This causes pixels to "bleed into" neighbors, resulting in a blur <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. Using a kernel sampled from a Gaussian distribution (bell curve) gives more weight to the central pixel, simulating lens blur more authentically <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

Different "kernels" can achieve various image processing effects:
*   **Edge Detection**: Kernels with positive values on one side and negative on the other can detect variations in pixel values, highlighting vertical or horizontal edges <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   **Sharpening**: Other kernels can sharpen images <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

In Convolutional Neural Networks, data is used to learn what the appropriate kernels should be for specific detection tasks <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

It's worth noting that in computer science contexts, the output of a [[understanding_convolution | convolution]] may be deliberately truncated, and the kernel flipping step (inherited from pure math) might seem unusual but is natural in other contexts like probabilities <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

## The Fast Fourier Transform and Efficient Convolution

Naively calculating [[discrete_convolution_algorithm | discrete convolution]] for two lists of size `n` involves `O(n^2)` operations <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. However, a significantly faster algorithm exists.

### Connection to Polynomial Multiplication

One insightful way to view [[understanding_convolution | convolution]] is through polynomial multiplication <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. If the elements of two lists are treated as coefficients of two polynomials, then expanding the product of these polynomials and collecting like terms is precisely the same process as [[understanding_convolution | convolution]] <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.

This implies a relationship: multiplying two functions (e.g., polynomials) is equivalent to taking the [[understanding_convolution | convolution]] of their coefficients <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. While multiplication of functions can be a simple pointwise operation, [[understanding_convolution | convolution]] appears more computationally complex <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

The challenge lies in translating between the coefficient representation (where convolution is complex) and the function output representation (where multiplication is simple) <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.

### The Fast Fourier Transform (FFT) Algorithm

The trick to speeding up [[discrete_convolution_algorithm | convolution]] involves evaluating polynomials at a special set of complex numbers known as the "roots of unity," which are evenly spaced on the unit circle <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. This choice of evaluation points creates a system with significant redundancy <a class="yt-timestamp" data-t="00:19:46">[00:19:46]</a>.

The set of outputs generated by evaluating coefficients at these specific points is called the [[fourier_transforms_and_their_role_in_frequency_analysis | discrete Fourier transform]] (DFT) <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. Crucially, the [[fourier_transforms_and_their_role_in_frequency_analysis | Fast Fourier Transform]] (FFT) is an algorithm that computes this transformation from coefficients to outputs (and vice-versa) in `O(n log n)` operations, a vast improvement over the `O(n^2)` of naive calculation <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.

> ##### The FFT Convolution Algorithm
> To efficiently compute the [[understanding_convolution | convolution]] of two long lists of numbers:
> 1.  Compute the [[fourier_transforms_and_their_role_in_frequency_analysis | Fast Fourier Transform]] (FFT) of each list <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.
> 2.  Multiply the two resulting FFTs point-wise (which is fast) <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.
> 3.  Perform an inverse [[fourier_transforms_and_their_role_in_frequency_analysis | Fast Fourier Transform]] on the product <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
> This process yields the convolution result in `O(n log n)` operations <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.

In practice, this `fftConvolve` method (e.g., in SciPy) can be thousands of times faster than direct `convolve` methods (e.g., in NumPy) for large arrays <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

## Broader Implications

This connection between [[understanding_convolution | convolution]] and polynomial multiplication, facilitated by the [[fourier_transforms_and_their_role_in_frequency_analysis | Fast Fourier Transform]], is powerful. It allows for an algorithm relevant across all applications of [[understanding_convolution | convolution]], from adding probability distributions to large-scale image processing <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.

Even ordinary multiplication of large integers can be seen as a [[understanding_convolution | convolution]] of their digits (with carries), meaning that the `O(n log n)` FFT-based algorithm can be used for faster multiplication of "monstrous" numbers than traditional elementary school methods <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

Further discussion will explore the continuous case of [[understanding_convolution | convolution]], especially concerning probability distributions <a class="yt-timestamp" data-t="00:22:35">[00:22:35]</a>.