---
title: Image Processing and Convolutions
videoId: KuXjwB4LzSA
---

From: [[3blue1brown]] <br/> 

Convolutions are ubiquitous in [[image_processing_and_convolutions | image processing]] <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. Although visually intriguing, the [[image_processing_and_convolutions | image processing]] application of convolutions is considered less representative of convolutions overall due to some specific intricacies <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

## Image Blurring

A two-dimensional analog of convolution can be applied to blur images <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.

### Simple Moving Average Blur

This method utilizes a small 3x3 grid, where each value within the grid is 1/9 <a class="yt-timestamp" data-t="09:05:00">[09:05:00]</a>. This grid is marched along the original image <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>. For each iteration, the values in the grid are multiplied by their corresponding pixels underneath <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>. In computer science, colors are often represented as vectors of three values (red, green, blue components) <a class="yt-timestamp" data-t="09:13:00">[09:13:00]</a>. Multiplying these values by 1/9 and summing them averages each color channel <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>. This sum then defines the corresponding pixel in the blurred output image <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>. The overall effect is that each pixel bleeds into its neighbors, resulting in a blurrier version of the original image <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>. The output image is referred to as a convolution of the original image with the small grid of values <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.

### Gaussian Blur

A more elegant blurring effect can be achieved by using a different grid of values <a class="yt-timestamp" data-t="10:05:00">[10:05:00]</a>. This involves a 5x5 grid where the central value is significantly larger than the values towards the edges <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>. These values are typically sampled from a bell curve, known as a Gaussian distribution <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>. When these values are multiplied by their corresponding pixels, more weight is given to the central pixel and less to those at the edges <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>. The resulting sum defines the output pixel <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>. This process simulates the effect of an out-of-focus lens <a class="yt-timestamp" data-t="10:41:00">[10:41:00]</a>.

## Edge Detection

Beyond blurring, convolutions can perform other [[image_processing_and_convolutions | image processing]] effects, such as sharpening and edge detection <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>, <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>.

For vertical edge detection, a grid with positive values on the left and negative values on the right is used <a class="yt-timestamp" data-t="10:53:00">[10:53:00]</a>, <a class="yt-timestamp" data-t="10:56:00">[10:56:00]</a>. When convolved with a grayscale image (where pixels are represented by one number) <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>, negative output values are possible <a class="yt-timestamp" data-t="11:21:00">[11:21:00]</a>. For example, if the left half of the grid is over black pixels (value zero) and the right half (negative values) is over white pixels (value one), the result will be very negative <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>, <a class="yt-timestamp" data-t="11:36:00">[11:36:00]</a>. If the grid is over a patch of uniform color, the output goes to zero because the sum of the values in the grid is zero <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>. This process detects variations in pixel value from left to right, highlighting vertical edges <a class="yt-timestamp" data-t="12:03:00">[12:03:00]</a>.

Similarly, rotating this grid so it varies from top to bottom allows for the detection of horizontal edges <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a>, <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.

## Key Concepts in [[image_processing_and_convolutions | Image Processing]]

### Kernel

The smaller grid used in convolution (e.g., the 3x3 or 5x5 grids discussed above) is often called a **kernel** <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>. Different [[image_processing_and_convolutions | image processing]] effects, such as blurring, edge detection, or sharpening, can be achieved simply by choosing different kernels <a class="yt-timestamp" data-t="12:32:00">[12:32:00]</a>.

### Output Size and Truncation

In pure mathematics, a convolution operation typically produces an array larger than the two input arrays (unless one has a length of one) <a class="yt-timestamp" data-t="13:07:00">[13:07:00]</a>. However, in certain computer science applications, including [[image_processing_and_convolutions | image processing]], the output is often deliberately truncated. This might be done to ensure the final output has the same size as the original image <a class="yt-timestamp" data-t="13:02:00">[13:04:00]</a>.

### Kernel Rotation

The definition of a convolution, as inherited from pure mathematics, involves flipping the second array (or kernel) before the sliding window operation <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>, <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>. While this flipping doesn't matter for symmetric kernels, it is a crucial aspect of the mathematical definition <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>. In computer science contexts, this rotation of the kernel can sometimes seem counter-intuitive or unnecessary <a class="yt-timestamp" data-t="13:24:00">[13:24:00]</a>.

## Convolutional Neural Networks

The concept of convolutions extends to [[image_processing_and_convolutions | image processing]] in machine learning. In a [[convolutional_neural_network | convolutional neural network]], data is used to determine what the kernels should be, as dictated by what the neural network needs to detect <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>.

## Computational Efficiency

For large-scale [[image_processing_and_convolutions | image processing]], the efficiency of convolution computation is critical <a class="yt-timestamp" data-t="21:34:00">[21:34:00]</a>. A conventional convolution algorithm might be O(n^2), meaning the number of operations scales with the square of the input list size <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>. However, there exists a much faster algorithm for computing convolutions:
1.  Compute the [[fast_fourier_transform_and_convolution | Fast Fourier Transform]] (FFT) of each list <a class="yt-timestamp" data-t="20:52:00">[20:52:00]</a>.
2.  Multiply these two FFT results point-wise <a class="yt-timestamp" data-t="21:06:00">[21:06:00]</a>.
3.  Perform an inverse [[fast_fourier_transform_and_convolution | Fast Fourier Transform]] <a class="yt-timestamp" data-t="21:10:00">[21:10:00]</a>.

This method reduces the computational complexity to O(n log n) operations <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>. For example, convolving two arrays of 100,000 random elements can take 4.87 seconds with a standard convolution function, but only 4.3 milliseconds with an FFT-based convolution function, a three-orders-of-magnitude improvement <a class="yt-timestamp" data-t="13:56:00">[13:56:00]</a>, <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>, <a class="yt-timestamp" data-t="14:25:00">[14:25:00]</a>. This speedup is significant for large [[image_processing_and_convolutions | image processing]] tasks <a class="yt-timestamp" data-t="21:34:00">[21:34:00]</a>.