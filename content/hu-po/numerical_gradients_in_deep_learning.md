---
title: Numerical gradients in deep learning
videoId: ccGxQCpbrnM
---

From: [[hu-po]] <br/> 

Numerical gradients are a method for estimating the gradient of a function, contrasting with analytical gradients which involve calculating the exact derivative of a function <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. While analytical gradients are precise, numerical gradients approximate the slope of a line by sampling points slightly above and below a given point <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

## Advantages and Disadvantages

Numerical gradients are generally faster and easier to compute, especially when dealing with complex functions for which deriving an exact partial derivative might be difficult <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. However, their fundamental limitation is their inaccuracy <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. Despite this, numerical methods are sometimes employed in deep learning where they might seem counterintuitive but work effectively in practice <a class="yt-timestamp" data-t="01:13:59">[01:13:59]</a>.

## Application in Neural Angelo

In the context of the "Neural Angelo" paper, numerical gradients are a key ingredient, particularly for computing higher-order derivatives as a smoothing operator <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

### Overcoming Locality Issues

The paper proposes using numerical gradients to address a "locality problem" associated with analytical gradients of hash encodings <a class="yt-timestamp" data-t="01:09:25">[01:09:25]</a>. When analytical gradients are used with multi-resolution hash grids under tri-linear interpolation, they are not continuous across space <a class="yt-timestamp" data-t="01:15:49">[01:15:49]</a>. This discontinuity arises because rounding operations (involved in determining grid cell boundaries) are non-differentiable <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>. As a point moves across cell borders, the corresponding hash entries change, leading to discontinuities in the derivative <a class="yt-timestamp" data-t="01:22:06">[01:22:06]</a>.

This discontinuity limits the backpropagation of the iconal loss (a regularization term) to only locally sampled hash entries <a class="yt-timestamp" data-t="01:22:34">[01:22:34]</a>. Joint optimization of grid cells, desirable for consistent surface representation, is not guaranteed by analytical gradients unless all corresponding cells are sampled and optimized simultaneously <a class="yt-timestamp" data-t="01:23:22">[01:23:22]</a>.

Numerical gradients solve this locality issue <a class="yt-timestamp" data-t="01:28:56">[01:28:56]</a>:
*   They allow hash entries of multiple grid cells to participate in surface normal computation and receive optimization updates simultaneously <a class="yt-timestamp" data-t="01:25:34">[01:25:34]</a>.
*   By taking a step size (Epsilon) that extends beyond a single grid cell, backpropagation updates are distributed beyond the local hash grid cell, affecting more surrounding feature vectors <a class="yt-timestamp" data-t="01:27:29">[01:27:29]</a>, <a class="yt-timestamp" data-t="01:32:28">[01:32:28]</a>.

### Numerical Gradient as a Smoothing Operator

Intuitively, numerical gradients with carefully chosen step sizes can be interpreted as a smoothing operation on the analytical gradient expression <a class="yt-timestamp" data-t="01:25:51">[01:25:51]</a>. This smoothing effect occurs because updating a wider area around a point through numerical methods contributes to a smoother surface <a class="yt-timestamp" data-t="01:33:10">[01:33:10]</a>.

### Integration with Coarse-to-Fine Optimization

Numerical gradients enable a [[initialization_and_gradient_stability | coarse-to-fine optimization]] scheme in Neural Angelo from two perspectives:
1.  **Step Size (Epsilon)**: The step size controls the resolution and the amount of detail covered. A larger Epsilon for the iconal loss ensures surface normal consistency at a larger scale, leading to consistent and continuous surfaces <a class="yt-timestamp" data-t="01:39:40">[01:39:40]</a>, <a class="yt-timestamp" data-t="01:40:14">[01:40:14]</a>. The step size is initialized to the coarsest hash grid and exponentially decreased, matching different hash grid sizes throughout optimization <a class="yt-timestamp" data-t="01:40:44">[01:40:44]</a>.
2.  **Hash Grid Resolution**: The optimization process starts by enabling only an initial set of coarse hash grids <a class="yt-timestamp" data-t="01:41:51">[01:41:51]</a>. Finer hash grids are progressively activated as the optimization continues and the step size decreases to the spatial size of the finer grids <a class="yt-timestamp" data-t="01:42:05">[01:42:05]</a>. This allows for a quick "quick and dirty" reconstruction early on, which is then refined with more detail as optimization time increases <a class="yt-timestamp" data-t="01:42:20">[01:42:20]</a>.

### Computation Method

In "Neural Angelo," to compute surface normals using numerical gradients, six additional SDF samples are required for each sampled point (x_i) <a class="yt-timestamp" data-t="01:35:06">[01:35:06]</a>. These samples are taken along each axis of the canonical coordinate system (X, Y, Z) around x_i, within a vicinity defined by the step size Epsilon <a class="yt-timestamp" data-t="01:33:42">[01:33:42]</a>. For example, the X component of the surface normal is estimated using the SDF values at (x_i + Epsilon, y_i, z_i) and (x_i - Epsilon, y_i, z_i) <a class="yt-timestamp" data-t="01:34:22">[01:34:22]</a>.

This approach ensures that the gradient is not computed exactly at the vertices, avoiding the discontinuity problem common with analytical methods for functions like ReLU <a class="yt-timestamp" data-t="01:34:32">[01:34:32]</a>.