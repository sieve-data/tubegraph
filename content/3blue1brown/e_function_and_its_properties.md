---
title: e function and its properties
videoId: v0YEaeIClKY
---

From: [[3blue1brown]] <br/> 

The [[exponential_functions_and_their_properties | function]] $e^t$ can be understood by examining its fundamental properties <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Defining Property

The most crucial, and arguably defining, property of the [[exponential_functions_and_their_properties | function]] $e^t$ is that it is its own [[derivatives_of_simple_functions_and_their_intuition | derivative]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Coupled with the condition that an input of 0 yields an output of 1 ($e^0=1$), this makes $e^t$ the unique [[mathematical_functions_and_graphs | function]] possessing this characteristic <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

### Physical Intuition

This property can be illustrated using a physical model <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>:
*   If $e^t$ represents your position on a number line over time, you start at position 1 <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.
*   The equation implies that your velocity (the [[derivatives_of_simple_functions_and_their_intuition | derivative]] of position) is always equal to your current position <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.
*   This means the farther away from 0 you are, the faster you move <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   This relationship provides a strong intuitive understanding of how the [[mathematical_functions_and_graphs | function]] grows, indicating accelerating growth that feels "out of hand quickly" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

## Variations of the Exponent

### Constant Multiplier ($e^{kt}$)

If a constant $k$ is added to the exponent, such as $e^{2t}$, the [[understanding_complex_functions_and_their_transformations | chain rule]] dictates that the [[derivatives_of_simple_functions_and_their_intuition | derivative]] becomes $k$ times itself <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

*   **Positive Constant ($k>0$):** For $e^{2t}$, the velocity is always twice the position. This leads to an even more rapid and "out of control" runaway growth <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. At each point, instead of just attaching a [[functions_as_vectors | vector]] corresponding to the position, you first double its magnitude <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

*   **Negative Constant ($k<0$):** If the constant is negative, like -0.5, the velocity [[functions_as_vectors | vector]] is always negative 0.5 times the position [[functions_as_vectors | vector]] <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. This means the [[functions_as_vectors | vector]] is flipped 180 degrees and its length is scaled by half <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This behavior results in movement in the opposite direction, slowing down in an [[exponential_functions_and_their_properties | exponential decay]] towards 0 <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

### Imaginary Constant ($e^{it}$)

When the constant is the imaginary unit $i$ (the square root of -1), as in $e^{it}$, the behavior shifts from the number line to the [[understanding_function_behavior_beyond_graphs | complex plane]] <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

*   The [[derivatives_of_simple_functions_and_their_intuition | derivative]] of position will always be $i$ times itself <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Multiplying a [[understanding_function_behavior_beyond_graphs | complex number]] by $i$ has the effect of rotating it 90 degrees <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   Therefore, the velocity at any point in time will be a 90-degree rotation of that position <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   Visualizing this for all possible positions creates a [[functions_as_vectors | vector field]] <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   Starting at the initial condition $e^{i0} = 1$ (at time $t=0$), the only trajectory where velocity consistently matches a 90-degree rotation of position is movement around a circle of radius 1 at a speed of 1 unit per second <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   This implies:
    *   After $\pi$ seconds, $e^{i\pi}$ is -1 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   After $\tau$ (tau, or $2\pi$) seconds, $e^{i\tau}$ equals 1 (a full circle) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   More generally, $e^{it}$ represents a number that is $t$ radians around the unit circle in the [[understanding_function_behavior_beyond_graphs | complex plane]] <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## Notational Considerations

The notation $e^t$ can be seen as a "notational disaster" because it places undue emphasis on the number $e$ and the concept of repeated multiplication, potentially obscuring the fundamental defining properties of the [[mathematical_functions_and_graphs | function]] itself <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.