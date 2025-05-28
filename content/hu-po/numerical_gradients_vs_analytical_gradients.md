---
title: Numerical gradients vs analytical gradients
videoId: ccGxQCpbrnM
---

From: [[hu-po]] <br/> 

In machine learning and optimization, particularly in the context of neural networks and geometric reconstruction, the choice between numerical and analytical gradients is crucial for balancing accuracy, computational efficiency, and stability. Both methods aim to determine the derivative of a function, which is fundamental for [[gradientbased_optimization_vs_language_modelbased_optimization|gradient-based optimization]] techniques like gradient descent <a class="yt-timestamp" data-t="01:09:58">[01:09:58]</a>.

## Analytical Gradients

Analytical gradients involve deriving the exact mathematical expression for the derivative of a function <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.

*   **Calculation**: This method requires "actually solving and actually basically sitting there with the equation and calculating the exact derivative of some kind of function" <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>, <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>.
*   **Accuracy**: Analytical gradients provide the precise derivative value <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Complexity**: They can be "complicated" to compute, especially if the function itself is complex <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Limitations in specific contexts**: In multi-resolution hash encodings, analytical gradients are "not continuous across space under tri-linear interpolation" <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>. This discontinuity arises because rounding operations involved in finding sampling locations in a voxel grid are non-differentiable <a class="yt-timestamp" data-t="01:18:26">[01:18:26]</a>. As a result, optimization updates only propagate to "locally sampled hash entries" <a class="yt-timestamp" data-t="01:22:41">[01:22:41]</a>, preventing "non-local smoothness" across the coarser resolution grids <a class="yt-timestamp" data-t="01:09:06">[01:09:06]</a>. This means updates are "limited to local grid cells unless all corresponding grid cells happen to be sampled and optimized simultaneously," which is "not always guaranteed" <a class="yt-timestamp" data-t="01:23:43">[01:23:43]</a>.

## Numerical Gradients

Numerical gradients approximate the derivative by evaluating the function at nearby points <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.

*   **Calculation**: Think of it as "you basically have a point you take the the kind of like slope at that point and then you sample a slightly above and then you sample slightly below and then you basically get an estimate of what the gradient is" <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This is analogous to [[comparison_between_first_and_second_order_methods|Newton's method]] <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **Speed & Ease**: They are "generally faster and easier to compute," especially for complex functions <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Accuracy**: They are "inaccurate fundamentally" as they provide an estimate rather than an exact value <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Advantages in Neuralangelo**:
    *   **Higher Order Derivatives**: Numerical gradients are used for computing "higher order derivatives" (anything beyond the first derivative, like acceleration as the second derivative of position) <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. These are crucial for losses like the [[comparison_between_first_and_second_order_methods|Iconal equation]] regularization, which requires a "double backwards operation" on the SDF <a class="yt-timestamp" data-t="01:14:40">[01:14:40]</a>.
    *   **Solving Locality Issue**: Unlike analytical gradients, numerical gradients "solve the locality issue without the need of additional Networks" <a class="yt-timestamp" data-t="01:28:58">[01:28:58]</a>. By taking samples across different grid cells (e.g., six additional SDF samples in 3D space, two for each axis, around a given point <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>), they allow hash entries of "multiple grid cells to receive optimization sub updates simultaneously" <a class="yt-timestamp" data-t="01:25:45">[01:25:45]</a>. This distributes backpropagation updates "beyond the local hash grid cell" <a class="yt-timestamp" data-t="01:26:08">[01:26:08]</a>.
    *   **Smoothing Operation**: "Intuitively, numerical gradients with carefully chosen step sizes can be interpreted as a smoothing operation on the analytical gradient expression" <a class="yt-timestamp" data-t="01:25:52">[01:25:52]</a>. This leads to "consistent and continuous surfaces" <a class="yt-timestamp" data-t="01:40:17">[01:40:17]</a>, especially at larger scales <a class="yt-timestamp" data-t="01:40:30">[01:40:30]</a>.
    *   **Course-to-Fine Optimization**: The step size of the numerical gradient can be used to control the resolution and amount of detail covered. By initializing with a larger step size (coarsest hash grid) and exponentially decreasing it, a [[thermodynamic_natural_gradient_descent|course-to-fine optimization]] is naturally enabled, matching different hash grid sizes throughout the optimization <a class="yt-timestamp" data-t="01:39:51">[01:39:51]</a>. This allows for progressive activation of finer hash grids as the step size decreases <a class="yt-timestamp" data-t="01:51:55">[01:51:55]</a>.

## Conclusion

While analytical gradients offer precision, their inherent discontinuities when applied to multi-resolution hash encodings (due to rounding and interpolation) limit their ability to propagate updates across the entire structure, leading to less smooth surfaces. Numerical gradients, despite their inherent inaccuracy, provide a practical solution in Neuralangelo by acting as a smoothing operator that distributes optimization updates beyond local cells. This property, combined with a progressive optimization schedule, enables the model to reconstruct highly detailed and smooth 3D surfaces from RGB images alone <a class="yt-timestamp" data-t="02:05:08">[02:05:08]</a>.