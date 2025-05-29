---
title: Use of Convolution in Polynomial Multiplication
videoId: KuXjwB4LzSA
---

From: [[3blue1brown]] <br/> 

[[Understanding Convolution | Convolution]] is a mathematical operation that combines two lists or functions to produce a new list or function <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. While not as commonly discussed as addition or term-by-term multiplication, it is a fundamental combination method <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. It is widely used in various fields, including [[applications_of_convolution_in_probability_and_image_processing | image processing]], probability theory, and solving differential equations <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. One context where [[understanding_convolution | convolution]] appears, though perhaps not by name, is in the multiplication of two polynomials <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## Convolution as Polynomial Expansion

When multiplying two polynomials, the process of expanding their product and collecting like terms is analogous to a [[understanding_convolution | convolution]] <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

Consider two polynomials whose coefficients are represented by lists of numbers. For example, if the coefficients are (1, 2, 3) and (4, 5, 6), representing `(1 + 2x + 3x^2)` and `(4 + 5x + 6x^2)` respectively <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>:
*   Creating a multiplication table of all pairwise products of these coefficients effectively expands the full product of the two polynomials <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   Adding the products along the diagonals of this table corresponds to collecting all like terms (e.g., terms with `x^1`, `x^2`, etc.) <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
*   This diagonal summation process is one of the fundamental ways to conceptualize a [[understanding_convolution | convolution]] <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

Therefore, multiplying two functions (like polynomials) through a simple pointwise operation (e.g., `P1(x) * P2(x)`) is equivalent to extracting their coefficients and then taking a [[understanding_convolution | convolution]] of those coefficient lists <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

## Computational Efficiency

While [[understanding_convolution | convolution]] might seem more complex than simple multiplication conceptually, it also has implications for computational efficiency <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

Directly multiplying two polynomials, each with `n` coefficients, by expanding the product table (an `n x n` grid) requires `n^2` products and approximately `n^2` additions to collect like terms <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>. This means the algorithm scales as O(n^2) <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

However, if polynomials are considered in terms of their outputs (sampling their values at various inputs), multiplying them only requires as many operations as the number of samples, as it's a pointwise operation <a class="yt-timestamp" data-t="00:17:01">[00:17:01]</a>. For a polynomial with `n` coefficients, `n` distinct samples are enough to uniquely specify it <a class="yt-timestamp" data-t="00:17:29">[00:17:29]</a>.

An initial algorithm outline for computing [[discrete_convolution_algorithm | discrete convolution]] using this principle would be <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>:
1.  Treat the lists of numbers as coefficients of two polynomials <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>.
2.  Sample those polynomials at enough outputs <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>.
3.  Multiply those samples pointwise <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.
4.  Solve a system of equations to recover the coefficients, which is the [[understanding_convolution | convolution]] result <a class="yt-timestamp" data-t="00:18:24">[00:18:24]</a>.

Initially, this approach seems no more efficient, as calculating samples and solving the system can also be O(n^2) operations <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.

### The Role of [[Fast Fourier Transform and its Role in Efficient Convolution | Fast Fourier Transform]] (FFT)

The breakthrough comes with the choice of specific sampling points <a class="yt-timestamp" data-t="00:19:01">[00:19:01]</a>. If polynomials are evaluated at a specially selected set of complex numbers known as the roots of unity (evenly spaced on the unit circle), the system becomes "friendlier" <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.

This specific set of outputs is called the [[Fast Fourier Transform and its Role in Efficient Convolution | discrete Fourier transform]] (DFT) of the coefficients <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. Due to inherent redundancies when evaluating at these specific points, there exists an algorithm, the [[Fast Fourier Transform and its Role in Efficient Convolution | Fast Fourier Transform]] (FFT), that can compute these transforms (from coefficients to outputs and vice versa) in O(n log n) operations <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>. This is a significant improvement over O(n^2) for large lists <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.

### The FFT-based Convolution Algorithm

This leads to a much faster algorithm for computing [[understanding_convolution | convolution]] <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>:
1.  **Compute FFT**: Take two lists of numbers to be convolved and compute the [[Fast Fourier Transform and its Role in Efficient Convolution | FFT]] of each <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>. (Mentally, this corresponds to evaluating the polynomials' coefficients at special complex points).
2.  **Pointwise Multiplication**: Multiply the two resulting FFTs together pointwise <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. This step is very fast.
3.  **Inverse FFT**: Compute the inverse [[Fast Fourier Transform and its Role in Efficient Convolution | FFT]] of the product from step 2 <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

This three-step process computes the [[understanding_convolution | convolution]] in O(n log n) time <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>. This connection between polynomial multiplication and [[understanding_convolution | convolution]] through [[Fast Fourier Transform and its Role in Efficient Convolution | FFT]] provides a universally applicable and efficient algorithm for convolutions in various fields, such as adding probability distributions or performing large-scale [[applications_of_convolution_in_probability_and_image_processing | image processing]] <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.

This principle even extends to elementary school multiplication of large integers, where the multiplication of digits can be seen as a [[understanding_convolution | convolution]], allowing for faster multiplication algorithms for extremely large numbers than the traditional O(n^2) method <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.