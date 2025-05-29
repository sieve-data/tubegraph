---
title: Applications of Convolution in Probability and Image Processing
videoId: KuXjwB4LzSA
---

From: [[3blue1brown]] <br/> 

[[understanding_convolution | Convolution]] is a fundamental operation that combines two lists of numbers or functions to produce a new list or function <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Unlike simple addition or multiplication, [[understanding_convolution | convolution]] is a genuinely new operation for combining lists or functions <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. It is ubiquitous in various fields, including image processing, probability theory, and solving differential equations <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It also appears in the context of multiplying two polynomials <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Convolution in Probability

[[understanding_convolution | Convolution]] is a core construct in the theory of [[applications_of_probability_density | probability]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. A simple example is calculating the probabilities of sums when rolling a pair of dice <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Dice Rolling Example
When rolling two dice, each has six possible outcomes, leading to 36 distinct pairs of outcomes <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Sums can be visualized on a grid, where pairs with a constant sum align along diagonals <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Counting pairs on these diagonals reveals the likelihood of each sum <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

Another visualization involves picturing the possibilities for each die in a row, then flipping the second row and sliding it <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   When the rows are slid to align the "snake eyes" (1+1), only the unique pair for a sum of two aligns <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   Sliding it one unit reveals the two pairs that sum to three (1+2, 2+1) <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.
*   Different offset values of the flipped lower array reveal all distinct pairs that have a given sum <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### Non-Uniform Probabilities
If the dice are not uniform (i.e., different probabilities for each face), calculating the probability of a sum involves multiplying corresponding probabilities for each pair and then summing those products <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. For example, to find the probability of a sum of 2, you multiply the probability of the blue die being 1 by the probability of the red die being 1 <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. For a sum of 3, you find the two pairs (1,2 and 2,1), multiply their corresponding probabilities, and add those two products together <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

This process—taking two arrays of numbers, flipping the second, lining them up at various offsets, taking pairwise products, and adding them up—is a fundamental way to understand [[understanding_convolution | convolution]] <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. The resulting sequence of probabilities is the [[understanding_convolution | convolution]] of the initial probability distributions <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Alternatively, it can be viewed by creating a table of all pairwise products and then summing along the diagonals <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## Convolution in Image Processing

[[understanding_convolution | Convolution]] is ubiquitous in image processing <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It can be understood through the concept of a "moving average" <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### Moving Average and Blurring
If you have a long list of numbers (data) and a smaller list of numbers that sum to 1 (e.g., five values each equal to 1/5th), performing the sliding window [[understanding_convolution | convolution]] process with this smaller list results in a smoothed-out version of the original data <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. Each term in the [[understanding_convolution | convolution]] represents an average of the data within the window <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. Different small lists, as long as they sum to 1, can be interpreted as moving averages with different weighting, such as giving more weight to the central value <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

A two-dimensional analog of this process provides an algorithm for blurring an image <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.
*   **Average Kernel:** A small grid of values (e.g., 3x3, with each value being 1/9th) marches across the image <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. For each position, values in the grid are multiplied by corresponding pixel values, and the results are summed <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. Since colors are often represented as [[applications_of_vectors_in_data_analysis_and_computer_graphics | vectors]] of three values (RGB), this gives an average along each color channel <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. The overall effect is that each pixel bleeds into its neighbors, resulting in a blurrier image <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Gaussian Kernel:** A more elegant blurring effect can be achieved using a grid where the central value is significantly larger than values towards the edges, sampled from a bell curve (Gaussian distribution) <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>. This gives more weight to the central pixel, creating a blurring effect that simulates out-of-focus lenses <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

### Edge Detection
Different grids of values, often called "kernels," can yield different image processing effects <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>. For example, a kernel with positive numbers on one side and negative numbers on the other (e.g., left positive, right negative) can detect vertical edges <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
*   When such a kernel sits on a patch of uniform color, the sum of values is zero, resulting in zero output <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   However, when the kernel straddles a change from black (value 0) to white (value 1), it can produce highly negative or positive values, indicating variation in pixel value <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. This process detects where there is variation in pixel value, identifying edges <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.
*   Rotating the kernel allows detection of horizontal edges <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>.

### Practical Considerations
In computer science contexts, the output of a [[understanding_convolution | convolution]] may be deliberately truncated to match the size of the original input, unlike the pure mathematical operation which produces a larger array <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. The pure mathematical definition of [[understanding_convolution | convolution]] involves flipping the second array or kernel, which might seem counterintuitive in some programming contexts but is natural in pure mathematics <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

### [[fast_fourier_transform_and_its_role_in_efficient_convolution | Fast Fourier Transform]] for Efficient Convolution
The connection between [[understanding_convolution | convolution]] and [[use_of_convolution_in_polynomial_multiplication | polynomial multiplication]] opens the door to more efficient algorithms <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   Multiplying two polynomials is equivalent to taking the [[discrete_convolution_algorithm | convolution]] of their coefficients <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.
*   Directly computing [[discrete_convolution_algorithm | convolution]] for lists of size 'n' is typically an O(n²) operation <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.
*   However, multiplying polynomials by sampling their values at specific inputs (especially complex numbers on the unit circle known as roots of unity) and then performing pointwise multiplication is much faster <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   The [[fast_fourier_transform_and_its_role_in_efficient_convolution | Fast Fourier Transform]] (FFT) algorithm allows for this translation between coefficients and sampled outputs (Discrete [[applications_of_fourier_transform | Fourier Transform]]) in O(n log n) operations <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
*   Therefore, to compute a [[discrete_convolution_algorithm | convolution]] efficiently for large lists:
    1.  Compute the [[fast_fourier_transform_and_its_role_in_efficient_convolution | FFT]] of each list <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.
    2.  Multiply the results point-wise <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.
    3.  Perform an inverse [[fast_fourier_transform_and_its_role_in_efficient_convolution | Fast Fourier Transform]] to recover the [[understanding_convolution | convolution]] result <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
*   This method dramatically reduces computation time, for instance, from 4.87 seconds to 4.3 milliseconds for 100,000-element arrays <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. This efficiency is critical for large-scale applications like image processing <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>.