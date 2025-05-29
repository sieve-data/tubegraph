---
title: Ordinary derivatives versus partial derivatives
videoId: ly4S0oi3Yz8
---

From: [[3blue1brown]] <br/> 

Differential equations describe how systems change over time <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. When thinking about these "rules of change," the language of derivatives is used <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. While ordinary derivatives are suitable for describing systems where a handful of numbers change over time, the mathematical tools become more intricate when an entire function changes with time <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## Ordinary Derivatives (ODEs)

In the context of [[calculating_derivatives_and_their_applications | ordinary differential equations]] (ODEs), one analyzes systems where a limited number of values, such as the angle and angular velocity of a pendulum, change over time <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. The rate of change for any of these values depends on the other values in the system <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. This is typically written as a system of equations where the derivative of each value with respect to time is expressed as a combination of the other values <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. The notation for [[computing_derivatives_of_functions | ordinary derivatives]] commonly uses the letter 'D' <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

## Partial Derivatives (PDEs)

[[understanding_derivatives_of_combined_functions | Partial derivatives]] are necessary when dealing with functions that have multiple input dimensions, such as a temperature function `T(x,t)` that depends on both space (`x`) and time (`t`) <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. In such cases, there are multiple rates of change at play <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>:

*   **Derivative with respect to `x`**: This describes how rapidly the temperature changes as you move along the object (e.g., a rod) <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. It can be visualized as the slope of the temperature surface when sliced parallel to the x-axis <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Derivative with respect to `t`**: This describes the rate at which the temperature of a single point on the object changes over time <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. This is analogous to the slope of the temperature surface when sliced parallel to the time axis <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.

Each of these derivatives tells only a part of the full story of how the temperature function changes, hence they are called partial derivatives <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

### Notation and Interpretation

The notation for partial derivatives replaces the letter 'D' with a special curly 'D', often called 'del' <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. While the notation changes, the underlying operation is essentially the same as [[understanding_what_a_derivative_is | ordinary derivatives]] <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Both ordinary and partial derivatives can be initially read as a literal ratio between a small change in the function's output and the small change in the input that caused it <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This interpretation holds true, with the understanding that the notation encodes the limit of that ratio as the input nudges become infinitesimally small <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Partial Differential Equations (PDEs)

When a rule of change is written using partial derivatives, it is called a partial differential equation (PDE) <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. PDEs, like the heat equation, describe phenomena where infinitely many values across a continuum are changing in concert <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Each value's change depends on its immediate neighbors, rather than a sum or product of all other numbers <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>. This makes PDEs generally much harder to solve than ODEs, but they tell a much richer story about complex systems <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

### Second Partial Derivatives and the Laplacian

The heat equation, for instance, relates the rate of change of temperature with respect to time to the second partial derivative of temperature with respect to space <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. The second partial derivative gives a measure of how a value compares to the average of its neighbors <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>. In a one-dimensional case (like a rod), it's denoted as `del-squared t over del x-squared` <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. This intuitively means that at points where the temperature distribution curves, it tends to change more quickly in the direction of that curvature <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

For objects spread out in more than one dimension (e.g., a plate or a 3D body), the heat equation includes second derivatives with respect to all spatial directions <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. The sum of these second spatial derivatives is called the **Laplacian**, often written as an upside-down triangle squared (∇²) <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>. The Laplacian is a multivariable version of the second derivative and retains the intuition of measuring how different a point is from the average of its neighbors, but now considering neighbors in all surrounding directions <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.