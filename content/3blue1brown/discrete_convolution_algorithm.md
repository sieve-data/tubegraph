---
title: Discrete Convolution Algorithm
videoId: KuXjwB4LzSA
---

From: [[3blue1brown]] <br/> 

[[understanding_convolution | Convolution]] is a fundamental mathematical operation that combines two lists of numbers or two functions to produce a new list or function <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Unlike simple term-by-term addition or multiplication, convolution is a genuinely new type of combination for lists and functions <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>. It is ubiquitous across various fields, including [[applications_of_convolution_in_probability_and_image_processing | image processing]], [[applications_of_convolution_in_probability_and_image_processing | probability theory]], solving differential equations, and [[use_of_convolution_in_polynomial_multiplication | multiplying polynomials]] <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>. While its formulaic definition can appear intimidating, the underlying concept is highly intuitive when visualized and motivated <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.

This article primarily focuses on the discrete case of convolution <a class="yt-timestamp" data-t="01:41:00">[01:41:00]</a>.

## Understanding Discrete Convolution

### Probability Example: Rolling Dice
A simple way to understand discrete convolution is through the example of rolling two dice and calculating the probabilities of different sums <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

Initially, with fair dice, one can list all 36 possible pairs of outcomes and count how many pairs yield a specific sum <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. Arranging these pairs in a grid reveals that all pairs with a constant sum lie along specific diagonals <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.

A more intuitive way to visualize this for convolution involves taking the two lists of possible outcomes (e.g., [1, 2, 3, 4, 5, 6]), flipping one of them around, and then sliding it past the other <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. When the flipped list aligns with the first list, the pairs that sum to a specific value line up vertically <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. For example, to get a sum of 2, only (1,1) aligns; for a sum of 3, (1,2) and (2,1) align, and so on, as the second list is offset <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.

If the dice are *not* uniform, meaning each face has a different probability of coming up (e.g., list `a` for the blue die, list `b` for the red die) <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>:
*   To find the probability of a sum of 2, one multiplies the probability of blue die being 1 (`a1`) by the probability of red die being 1 (`b1`) <a class="yt-timestamp" data-t="04:12:00">[04:12:00]</a>.
*   To find the probability of a sum of 3, one considers the pairs (1,2) and (2,1). The total probability is `(a1 * b2) + (a2 * b1)` <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.
*   This process, of taking two arrays, flipping the second, lining them up at various offsets, taking pairwise products, and summing them up, is a fundamental way to understand discrete convolution <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

### Formal Definition
Given two sequences (lists) `a` and `b`, their convolution, denoted `a * b`, produces a new sequence where the `n`-th element is a sum over all pairs of indices `i` and `j` such that `i + j = n` <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.
Specifically, `(a * b)n = Σ (ai * bj)` for all `i, j` such that `i + j = n` <a class="yt-timestamp" data-t="05:54:00">[05:54:00]</a>.

An alternative visualization for this operation is to create a multiplication table of all pairwise products and then sum along the diagonals <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. This yields the same result as the sliding window method <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.

**Example:**
Convolving `[1, 2, 3]` with `[4, 5, 6]` <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>:
1.  Flip `[4, 5, 6]` to `[6, 5, 4]` (for the mental model).
2.  Slide 1: `(1 * 4) = 4` (Output: [4]) <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>
3.  Slide 2: `(1 * 5) + (2 * 4) = 5 + 8 = 13` (Output: [4, 13]) <a class="yt-timestamp" data-t="06:43:00">[06:43:00]</a>
4.  Slide 3: `(1 * 6) + (2 * 5) + (3 * 4) = 6 + 10 + 12 = 28` (Output: [4, 13, 28]) <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>
5.  Slide 4: `(2 * 6) + (3 * 5) = 12 + 15 = 27` (Output: [4, 13, 28, 27]) <a class="yt-timestamp" data-t="07:02:00">[07:02:00]</a>
6.  Slide 5: `(3 * 6) = 18` (Output: [4, 13, 28, 27, 18]) <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>

## [[applications_of_convolution_in_probability_and_image_processing | Applications of Convolution]]

### Moving Average
Convolution can be used to compute a moving average. If you have a long list of numbers (data) and a smaller list (kernel) whose elements sum to 1 (e.g., `[1/5, 1/5, 1/5, 1/5, 1/5]`), convolving them effectively averages the data within a sliding window. This results in a smoothed version of the original data <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>. By changing the values in the kernel, one can create weighted moving averages, giving more importance to central values <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.

### Image Processing
In [[visual_representation_of_signal_processing | image processing]], a two-dimensional analog of convolution is used. A small grid of values, called a "kernel," slides across an image <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>. For each position, the kernel's values are multiplied by the corresponding pixel values (e.g., R, G, B components) and summed to determine the new pixel value in the output image <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

*   **Blurring:** A kernel with all equal values (e.g., 1/9 for a 3x3 grid) averages neighboring pixels, causing each pixel to "bleed" into its neighbors, resulting in a blurred image <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>. A more elegant blurring effect, like simulating an out-of-focus lens, can be achieved with a kernel sampled from a [[discovery_and_definition_of_convergent_sums | Gaussian distribution]] (bell curve), which gives more weight to the central pixel <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>.
*   **Edge Detection:** A kernel with both positive and negative values (and summing to zero) can detect variations in pixel values. For instance, a kernel with negative values on one side and positive on the other will pick up vertical edges in an image, coloring them based on the sign of the result <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>. Rotating this kernel detects horizontal edges <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>.

The versatility of convolution in image processing comes from simply choosing different kernels <a class="yt-timestamp" data-t="12:32:00">[12:32:00]</a>. In [[backpropagation_algorithm | convolutional neural networks]], algorithms are used to determine optimal kernels for specific detection tasks <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>.

### Considerations in Computer Science
*   **Output Length:** While pure mathematical convolution always produces an output array larger than the inputs (unless one input has length 1), in computer science contexts, the output is often deliberately truncated to match the original size, especially in image processing <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>.
*   **Kernel Flipping:** The pure mathematical definition of convolution involves flipping the second array (or kernel) before the sliding sum-of-products <a class="yt-timestamp" data-t="09:48:00">[09:48:00]</a>. Although this "flipping" might seem unnecessary in some programming contexts (especially if the kernel is symmetric), it is a crucial aspect inherited from the mathematical definition, which is natural in applications like probability <a class="yt-timestamp" data-t="13:28:00">[13:28:00]</a>.

## Efficient Convolution: The [[convolution_theorem_and_its_mathematical_significance | Convolution Theorem]]

Directly computing convolution by iterating through all pairwise products (as in the sliding window or multiplication table methods) is computationally intensive. For two lists of size `n`, this method requires `O(n^2)` operations <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>. For large arrays, this can be very slow; for example, convolving two 100,000-element arrays takes seconds using a direct implementation (e.g., NumPy's `convolve`) <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.

A much faster algorithm exists, which relies on the connection between convolution and [[use_of_convolution_in_polynomial_multiplication | polynomial multiplication]] <a class="yt-timestamp" data-t="13:43:00">[13:43:00]</a>.

### Connection to Polynomial Multiplication
When two polynomials are multiplied, the process of expanding the product and then collecting like terms is mathematically equivalent to convolving their coefficients <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.
For example, `(1 + 2x + 3x^2) * (4 + 5x + 6x^2)`:
*   The pairwise products fill a grid similar to the multiplication table for convolution <a class="yt-timestamp" data-t="15:13:00">[15:13:00]</a>.
*   Collecting like terms (e.g., all `x` terms) corresponds to summing along the diagonals of this product table, exactly like convolution <a class="yt-timestamp" data-t="15:37:00">[15:37:00]</a>.

This connection reveals a crucial property: multiplying two functions (like polynomials) in the "pointwise" domain is equivalent to convolving their coefficients in the "coefficient" domain <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>.

### The [[fast_fourier_transform_and_its_role_in_efficient_convolution | Fast Fourier Transform]] (FFT) Algorithm
While pointwise multiplication of polynomials is faster than convolving their coefficients (requiring only `n` operations if `n` samples are taken) <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>, transforming between coefficients and samples efficiently is the challenge <a class="yt-timestamp" data-t="18:52:00">[18:52:00]</a>.

The trick lies in evaluating the polynomials not at arbitrary inputs (like 0, 1, 2, ...), but at a very specific set of [[complex_numbers_in_discrete_math | complex numbers]]: the *roots of unity*, which are evenly spaced on the unit circle <a class="yt-timestamp" data-t="19:17:00">[19:17:00]</a>.
*   This evaluation process is known as the **Discrete Fourier Transform (DFT)** <a class="yt-timestamp" data-t="19:56:00">[19:56:00]</a>.
*   The DFT exploits redundancies in calculations when using these special inputs, allowing for a much faster computation <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>.
*   The **Fast Fourier Transform (FFT)** is an algorithm that computes the DFT (and its inverse) in `O(n log n)` operations, significantly faster than `O(n^2)` for large `n` <a class="yt-timestamp" data-t="20:25:00">[20:25:00]</a>.

### Algorithm Outline
To compute the convolution of two lists `a` and `b` efficiently using the FFT <a class="yt-timestamp" data-t="20:49:00">[20:49:00]</a>:
1.  Compute the [[fast_fourier_transform_and_its_role_in_efficient_convolution | Fast Fourier Transform]] of list `a` and list `b` <a class="yt-timestamp" data-t="20:52:00">[20:52:00]</a>. (Mentally, this means treating them as polynomial coefficients and evaluating them at the roots of unity.)
2.  Multiply the two resulting FFTs *point-wise* <a class="yt-timestamp" data-t="21:06:00">[21:06:00]</a>. This step is very fast.
3.  Compute the *inverse* [[fast_fourier_transform_and_its_role_in_efficient_convolution | Fast Fourier Transform]] of the product obtained in step 2 <a class="yt-timestamp" data-t="21:10:00">[21:10:00]</a>. This gives the convolution result.

This method achieves `O(n log n)` complexity for convolution <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>. For instance, SciPy's `fftConvolve` function, which uses this approach, computes the convolution of two 100,000-element arrays in milliseconds, a dramatic improvement over the direct `O(n^2)` method <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.

This powerful algorithm demonstrates the significance of [[convolution_theorem_and_its_mathematical_significance | convolution theorem and its mathematical significance | mathematical connections]] between seemingly unrelated areas, allowing for practical, efficient computations across diverse applications like probability distribution addition or large-scale image processing <a class="yt-timestamp" data-t="21:25:00">[21:25:00]</a>.

As a final thought, even elementary school multiplication of two numbers can be seen as a convolution of their digits, with added steps for carries. The existence of the `O(n log n)` convolution algorithm implies that two very large integers can be multiplied faster than the traditional method, though this is only practically useful for "monstrously" large numbers <a class="yt-timestamp" data-t="21:51:00">[21:51:00]</a>.