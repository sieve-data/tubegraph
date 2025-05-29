---
title: Introduction to Convolutions
videoId: KuXjwB4LzSA
---

From: [[3blue1brown]] <br/> 

A convolution is a fundamental type of mathematical combination for two lists of numbers or two functions, resulting in a new list or function [00:00:26]. Unlike simple addition or term-by-term multiplication, convolution introduces something genuinely new for combining these mathematical objects [00:00:39].

## Ubiquitous Applications

Convolutions appear in various fields and contexts:
*   [[image_processing_and_convolutions | Image processing]] [00:00:45]
*   Core construct in the [[applications_of_convolutions_in_probability | theory of probability]] [00:00:49]
*   Solving differential equations [00:00:51]
*   [[polynomial_multiplication_and_convolution | Multiplying two polynomials together]] [00:00:58]

The formulaic definition can appear intimidating without context, but understanding its purpose reveals it as a beautiful operation [00:01:04]. This article primarily focuses on the discrete case of convolutions [00:01:41].

## Understanding Discrete Convolutions

### Probability Distributions: Rolling Dice

Consider rolling a pair of dice and determining the probabilities of different sums [00:02:15]. Each die has six possible outcomes, leading to 36 distinct pairs of outcomes [00:02:24]. By arranging these pairs in a grid, sums appear along diagonals, allowing one to count how many pairs result in a given sum [00:02:36].

Alternatively, one can visualize this by picturing the possibilities for each die in a row, then flipping the second row [00:03:08]. When the second row is slid, pairs that add up to a constant sum align vertically [00:03:13]. For example, sliding the bottom row to the right aligns the pair for a sum of two (snake eyes) [00:03:19]. Sliding it further aligns pairs for a sum of three [00:03:26]. Different offset values of the flipped lower array reveal all distinct pairs that yield a given sum [00:03:32].

This becomes particularly interesting when dealing with "special" dice that are not uniform, meaning each face has a different probability of coming up [00:03:58]. To find the probability of a specific sum (e.g., a 2), one would multiply the probabilities of the outcomes that yield that sum (e.g., blue die is 1 and red die is 1) [00:04:12]. For a sum of 3, one would multiply the corresponding probabilities for the two possible pairs and then add those products together [00:04:20].

This process — taking two arrays of numbers, flipping the second, lining them up at various offsets, taking pairwise products, and adding them up — is a fundamental way to understand a convolution [00:04:46]. It mixes two lists of values (e.g., probability distributions for each die) to produce a new sequence (e.g., probabilities of sums) [00:05:12].

A convolution of two sequences, `a` and `b`, generates a new sequence where each element is a sum of pairwise products [00:05:17]. Another perspective is to create a table of all pairwise products and then sum along the diagonals [00:05:27].

### Formal Notation
The convolution of `a` and `b`, denoted `a * b`, is a new list where the nth element is defined as a sum over all pairs of indices `i` and `j` such that `i + j = n` [00:05:50]. For instance, if `n` is 6, the pairs considered would be (1,5), (2,4), (3,3), (4,2), and (5,1) [00:06:05].

### Example: Convolving Two Lists
Let's convolve the list `[1, 2, 3]` with `[4, 5, 6]` [00:06:26].
1.  Picture both lists, flipping the second one `[6, 5, 4]` [00:06:31].
2.  Start with the flipped list aligned to the left:
    *   Aligning 1 and 4: `1 * 4 = 4`. This is the first term of the output [00:06:35].
3.  Slide the bottom array one unit to the right:
    *   Aligning (1, 5) and (2, 4): `(1 * 5) + (2 * 4) = 5 + 8 = 13`. This is the next output entry [00:06:43].
4.  Slide once more:
    *   Aligning (1, 6), (2, 5), and (3, 4): `(1 * 6) + (2 * 5) + (3 * 4) = 6 + 10 + 12 = 28` [00:06:54].
5.  One more slide:
    *   Aligning (2, 6) and (3, 5): `(2 * 6) + (3 * 5) = 12 + 15 = 27` [00:07:02].
6.  Last slide:
    *   Aligning (3, 6): `3 * 6 = 18` [00:07:07].

The result of the convolution is `[4, 13, 28, 27, 18]` [00:07:18].

### Moving Averages and Image Processing

Convolutions are also used for moving averages [00:07:29]. If you have a long list of numbers (data) and a smaller list (kernel) that sums to 1 (e.g., five values all equal to 1/5), performing a sliding window convolution means multiplying values from the data by the kernel and adding them, effectively taking an average of the data within the window [00:07:34]. This process smooths out the original data [00:08:11]. By changing the kernel (e.g., giving more weight to the central value), different smoothing effects can be achieved [00:08:14].

A two-dimensional analog of this, where a small grid of values (called a "kernel") marches across an image, can be used for various [[image_processing_and_convolutions | image processing]] effects [00:08:33]. For example, a 3x3 kernel where each value is 1/9 (summing to 1) will blur an image by averaging pixel values within its window [00:09:00]. This effectively makes each pixel "bleed" into its neighbors [00:09:35].

Other kernels can produce different effects:
*   A 5x5 kernel with larger values in the center (sampled from a Gaussian distribution) creates a more authentic blurring effect, simulating an out-of-focus lens [00:10:07].
*   A kernel with positive values on one side and negative values on the other (summing to zero) detects variations in pixel value, picking up on edges [00:10:53]. For instance, a horizontal kernel can detect vertical edges [00:11:56], and a vertical kernel can detect horizontal edges [00:12:16].

In a "convolutional neural network," data is used to determine what the kernels should be to detect specific features [00:12:40].

### Important Considerations in Computing Science
*   **Output Length**: While pure mathematical convolutions produce an array larger than the inputs, computer science contexts often truncate the output to match the original size [00:13:07].
*   **Flipping the Kernel**: The definition of convolution from pure mathematics involves flipping the second array or kernel [00:09:56]. While sometimes feeling "uncalled for" in computational contexts, it's a natural and important step inherited from its mathematical origins [00:13:28].

## Fast Algorithms for Convolutions

The standard way to compute a convolution, by creating a table of pairwise products and summing diagonals, scales quadratically with the size of the lists (O(n^2)) [00:16:36]. For two lists of 100,000 elements, this can take several seconds (e.g., 4.87 seconds for `NumPy.convolve`) [00:13:59].

However, there are much faster algorithms, such as the `fftConvolve` function from the SciPy library, which can perform the same operation in milliseconds (e.g., 4.3 milliseconds for the same 100,000 elements) [00:14:16]. This improvement is three orders of magnitude [00:14:29].

### Connection to Polynomial Multiplication
[[polynomial_multiplication_and_convolution | Multiplying two polynomials together]] is equivalent to convolving their coefficients [00:15:10]. When you expand the product of two polynomials and then collect like terms, that process is exactly a convolution of their coefficient lists [00:15:24].

While convolutions are computationally more complex than simple pointwise multiplication, this connection is key to faster algorithms [00:16:09]. If you can convert the coefficients of two polynomials into their sampled output values, multiply those values pointwise, and then convert them back to coefficients, you can achieve the convolution [00:18:11].

### The Role of Fourier Transforms
The "trick" to making this approach efficient lies in choosing a specific set of inputs for sampling the polynomials: specially selected [[introduction_to_complex_numbers | complex numbers]] that sit evenly spaced on the unit circle, known as roots of unity [00:19:24]. This particular choice creates a system with significant redundancy, which can be leveraged to save computational work [00:19:46].

This set of outputs is called the **Discrete Fourier Transform** of the coefficients [00:19:56]. The **Fast Fourier Transform (FFT)** is an algorithm that computes these transformations quickly [00:20:11]. Instead of O(n^2) operations, the FFT allows for O(n log n) operations to convert coefficients to outputs and vice-versa [00:20:25].

The general algorithm for fast convolution then becomes:
1.  Compute the [[fourier_transforms_and_convolutions_in_integral_computation | Fast Fourier Transform]] (FFT) of each of the two lists you want to convolve [00:20:52]. This can be thought of as evaluating polynomials at a specially selected set of points [00:20:59].
2.  Multiply the two resulting FFTs together pointwise [00:21:06]. This step is fast [00:21:10].
3.  Perform an inverse Fast Fourier Transform on the product [00:21:10].

This "sneaky backdoor way" computes the convolution in O(n log n) operations [00:21:19]. This connection between polynomial multiplication and convolutions, facilitated by the FFT, makes a faster algorithm relevant for all applications of convolutions, including [[applications_of_convolutions_in_probability | probability distributions]] and [[image_processing_and_convolutions | image processing]] [00:21:25].

## Further Considerations

Intriguingly, ordinary multiplication of two numbers can be seen as a convolution of their digits, with additional steps for carries [00:21:51]. This implies that for very large integers, there exists an algorithm for multiplication that is faster than the elementary school method, reducing the complexity from O(n^2) to O(n log n) [00:22:16]. This is primarily useful for numbers of "monstrous" size [00:22:28].

The next step in understanding convolutions involves exploring the continuous case, with a particular focus on probability distributions [00:22:35].