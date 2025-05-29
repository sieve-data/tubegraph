---
title: Relationship between e to the x and complex numbers
videoId: F_0yfvm0UoU
---

From: [[3blue1brown]] <br/> 

The equation [[understanding_e_to_the_pi_i_equals_negative_1 | e to the pi i equals negative 1]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, often referred to as Euler's Identity, is one of the most famous and simultaneously confusing equations in mathematics <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Understanding it doesn't require calculus or advanced math, but rather a reframing of how numbers are perceived <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Re-framing Numbers as Actions

The expression "e to the x" (e^x) should not be understood as repeated multiplication, as that only makes sense for countable x values <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Instead, numbers should be conceptualized as actions <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>:

*   **A point** on an infinitely extending line <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   An **"adder"**: an action that slides the line along itself <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
    *   Addition is redefined as the successive application of two adders <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. An adder slides the line until the point corresponding to zero lands where the adder itself started <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   A **"multiplier"**: an action that stretches the line <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   Multiplication is redefined as the successive application of two multipliers <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. A multiplier fixes zero in place and moves the point corresponding to one to where the multiplier itself started, keeping everything evenly spaced <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### The Role of e to the x

The fundamental purpose of `e^x` is to transform adders into multipliers as naturally as possible <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This means if you apply two adders successively, then pump the resulting sum through the function, it's the same as putting each adder through the function separately and then successively applying the two multipliers you get <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

This property is expressed as:
`e^(x + y) = e^x * e^y` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>

This property defines `e^x`; the fact that it relates to repeated multiplication for counting numbers is a consequence, not the definition itself <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. The number `e` itself is simply the value of this function at one <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Complex Numbers and the 2D Plane

The concept of numbers as actions can be extended to the 2D plane, which is where [[complex_numbers_introduction | complex numbers]] come into play <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. Each [[geometric_representation_of_complex_numbers | complex number]] simultaneously represents <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>:

*   A point on the plane <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   An **adder**: slides the plane so that the point for zero lands on the point for the number <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   A **multiplier**: fixes zero in place and moves the point for one to the point for the number, keeping everything evenly spaced <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This can include rotating along with stretching or shrinking <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

Real numbers perform actions like sliding side-to-side and stretching <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. However, [[complex_numbers_introduction | complex numbers]] introduce new actions, such as sliding up or down, and rotation <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

### The Imaginary Unit 'i'

Consider the point "i" on the complex plane <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>:

*   As an adder, it slides the plane up <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   As a multiplier, it rotates the plane a quarter of the way around (90 degrees) <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

Multiplying 'i' by itself results in -1 <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>, meaning applying the action of 'i' twice is equivalent to the action of -1 as a multiplier <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. This is why 'i' is the square root of -1 <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

*   All adding on the [[complex_plane_and_exponential_functions | complex plane]] is a combination of sliding sideways and sliding up or down <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   All multiplication on the [[complex_plane_and_exponential_functions | complex plane]] is a combination of stretching and rotating <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## e to the x and Complex Numbers

Since `e^x` transforms side-to-side slides (real adders) into stretches (real multipliers), it naturally extends to transform vertical slides (imaginary adders) into rotations (complex multipliers) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

In terms of points on the plane, this means `e^x` (where x is an imaginary number, e.g., `x = y*i`) takes points on the vertical (imaginary) axis, which correspond to adders that slide the plane up and down, and maps them onto the circle with radius one <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This circle corresponds to multipliers that only rotate the plane <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

The most natural way for this transformation to occur is by wrapping the vertical line around the circle without stretching or squishing it <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This implies that a length of `2π` on the vertical line corresponds to a full rotation around the circle <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>, consistent with `2π` being the ratio of a circle's circumference to its radius <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

Therefore, going "up pi" on the imaginary axis (i.e., taking the adder `πi`) translates to going exactly halfway around the circle <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. On the unit circle, halfway around from 1 is -1.

Thus, `e^(πi) = -1` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This function `e^x` takes the adder `πi` and transforms it into the multiplier -1.