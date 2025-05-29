---
title: derivative and velocity relationship
videoId: v0YEaeIClKY
---

From: [[3blue1brown]] <br/> 

The concept of [[derivatives and integrals | derivatives]] can be intuitively understood through the relationship between position and velocity, especially when considering the exponential function e<sup>t</sup> <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## e<sup>t</sup>: Position and Velocity

The most crucial property of the function e<sup>t</sup> is that it is its own [[understanding_the_meaning_and_computation_of_derivatives | derivative]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This, combined with the initial condition that inputting 0 returns 1, makes it the unique function with this characteristic <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

If e<sup>t</sup> represents an object's position on a number line over time, its [[graphical_representation_of_motion_distance_and_velocity | velocity]]—which is the [[understanding_the_meaning_and_computation_of_derivatives | derivative]] of position—is always equal to its current position <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This [[velocity_and_distance_relationship | relationship]] implies that the farther an object is from 0, the faster it moves <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. This [[introduction_to_derivatives_and_calculus_concepts | intuitive picture]] illustrates that the function must grow by accelerating at an accelerating rate, giving a sense of rapid, "out of control" expansion <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Varying Growth Rates: e<sup>kt</sup>

When a constant 'k' is added to the exponent, such as e<sup>2t</sup>, the [[derivatives_of_simple_functions_and_their_intuition | derivative]] becomes 'k' times the function itself, as dictated by the chain rule <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. For e<sup>2t</sup>, the velocity is always twice the position <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, making the "runaway growth" feel even more intense <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Exponential Decay

If the constant in the exponent is negative, for example, e<sup>-0.5t</sup>, the velocity vector is always -0.5 times the position vector <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. This means the velocity vector is flipped 180 degrees and its length is scaled by half <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This results in movement in the opposite direction, leading to exponential decay towards 0 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Imaginary Exponents: e<sup>it</sup> in the Complex Plane

Introducing an imaginary constant 'i' (where i is the square root of -1) into the exponent, as in e<sup>it</sup>, changes the interpretation of velocity <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. If position is e<sup>it</sup>, its [[understanding_the_meaning_and_computation_of_derivatives | derivative]] (velocity) is always 'i' times itself <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

Multiplying by 'i' has the [[geometric_interpretation_of_derivatives | geometric effect]] of rotating numbers 90 degrees <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. This necessitates extending the analysis beyond the number line into the complex plane <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

*   For any position e<sup>it</sup>, the velocity at that time will be a 90-degree rotation of that position <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   Starting at 1 (when t=0), the trajectory of e<sup>it</sup> is a circle of radius 1, traversed at a speed of 1 unit per second <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   This leads to specific values:
    *   e<sup>iπ</sup> = -1 <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>
    *   e<sup>iτ</sup> = 1 (where τ is 2π) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
*   In general, e<sup>it</sup> corresponds to a number 't' radians around the unit circle in the complex plane <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

> [!NOTE] Notation of e<sup>t</sup>
> The notation "e<sup>t</sup>" is considered a "notational disaster" by some, as it places undue emphasis on the number 'e' and the idea of repeated multiplication <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>. Further explanation of this perspective is reserved for future discussions <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.