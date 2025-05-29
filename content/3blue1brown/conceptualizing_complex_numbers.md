---
title: Conceptualizing complex numbers
videoId: F_0yfvm0UoU
---

From: [[3blue1brown]] <br/> 

The equation `e^πi = -1` <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a> is widely recognized but often confusing <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Understanding it requires a reframing of how numbers are perceived, moving beyond traditional counting <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.

## Numbers as Actions

Instead of solely viewing numbers as quantities for counting <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>, a more expansive perspective is needed, especially when dealing with fractional, irrational, or [[the_concept_of_imaginary_numbers | imaginary numbers]] <a class="yt-timestamp" data-t="01:21:21">[01:21:21]</a>. Each number can be conceptualized simultaneously as three things <a class="yt-timestamp" data-t="01:31:31">[01:31:31]</a>:

1.  **A point** on an infinitely extending line <a class="yt-timestamp" data-t="01:35:35">[01:35:35]</a>.
2.  **An "adder"**: an action that slides the line along itself <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>.
    *   When thinking of adders, one imagines sliding the line such that the point corresponding to zero lands where the point corresponding to the adder itself started <a class="yt-timestamp" data-t="01:57:57">[01:57:57]</a>.
    *   The sum of two adders is defined by their successive application <a class="yt-timestamp" data-t="02:06:06">[02:06:06]</a>.
3.  **A "multiplier"**: an action that stretches the line <a class="yt-timestamp" data-t="01:40:40">[01:40:40]</a>.
    *   For multipliers, zero is fixed, and the point corresponding to one is brought to where the multiplier itself started, keeping everything evenly spaced <a class="yt-timestamp" data-t="02:19:19">[02:19:19]</a>.
    *   Multiplication is redefined as the successive application of two multipliers <a class="yt-timestamp" data-t="02:31:31">[02:31:31]</a>.

## The Exponential Function `e^x`

The function `e^x` is not about repeated multiplication <a class="yt-timestamp" data-t="00:54:54">[00:54:54]</a>. Its fundamental purpose is to naturally transform adders into multipliers <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>. This means:

*   Applying two adders successively and then processing the result through `e^x` yields the same outcome as processing each adder separately through `e^x` and then successively applying the resulting multipliers <a class="yt-timestamp" data-t="02:43:43">[02:43:43]</a>.
*   This property is expressed as `e^(x + y) = e^x * e^y` <a class="yt-timestamp" data-t="02:55:55">[02:55:55]</a>, which defines the function rather than being a consequence of repeated multiplication <a class="yt-timestamp" data-t="03:03:03">[03:03:03]</a>.
*   The number `e` itself is simply the value of this function when the input is one <a class="yt-timestamp" data-t="03:26:26">[03:26:26]</a>. The convention of writing `e^x` is a remnant of its connection to repeated multiplication <a class="yt-timestamp" data-t="03:33:33">[03:33:33]</a>.

## [[introduction_to_complex_numbers | Complex Numbers]] and Actions in 2D

The concept of numbers as adders and multipliers can be extended to a two-dimensional plane, which is what [[complex_numbers_in_mathematics | complex numbers]] represent <a class="yt-timestamp" data-t="03:56:56">[03:56:56]</a>.

*   Each [[introduction_to_complex_numbers | complex number]] is simultaneously a point on the plane <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
*   As an adder, it slides the entire plane so that the point for zero lands on the point for that number <a class="yt-timestamp" data-t="04:05:05">[04:05:05]</a>.
*   As a multiplier, it fixes zero in place and transforms the plane by bringing the point for one to the point for the number, maintaining even spacing. This action can include both stretching and rotating <a class="yt-timestamp" data-t="04:08:08">[04:08:08]</a>, <a class="yt-timestamp" data-t="04:17:17">[04:17:17]</a>.

### The [[the_concept_of_imaginary_numbers | Imaginary Unit]] `i`

The point `i` <a class="yt-timestamp" data-t="04:30:30">[04:30:30]</a> has a specific [[geometric_interpretation_of_complex_numbers | geometric interpretation]]:

*   As an adder, it slides the plane upwards <a class="yt-timestamp" data-t="04:34:34">[04:34:34]</a>.
*   As a multiplier, it rotates the plane a quarter turn <a class="yt-timestamp" data-t="04:34:34">[04:34:34]</a>.
*   Multiplying `i` by itself results in `-1` <a class="yt-timestamp" data-t="04:39:39">[04:39:39]</a>, meaning applying the action of `i` twice is equivalent to the action of `-1` as a multiplier. Thus, `i` is the square root of `-1` <a class="yt-timestamp" data-t="04:46:46">[04:46:46]</a>.

In the [[complex_numbers_in_mathematics | complex plane]], adding involves a combination of sliding sideways and sliding up or down <a class="yt-timestamp" data-t="04:51:51">[04:51:51]</a>, while multiplying involves a combination of stretching and rotating <a class="yt-timestamp" data-t="04:54:54">[04:54:54]</a>.

## [[complex_numbers_and_imaginary_exponents | Euler's Identity]]: `e^πi = -1`

Just as `e^x` transforms horizontal slides (real number adders) into stretches (real number multipliers) <a class="yt-timestamp" data-t="05:01:01">[05:01:01]</a>, it also naturally transforms vertical slides (imaginary number adders) into rotations (imaginary number multipliers) <a class="yt-timestamp" data-t="05:04:04">[05:04:04]</a>.

*   `e^x` maps points on the vertical line (representing adders that slide the plane up and down) to points on the unit circle <a class="yt-timestamp" data-t="05:12:12">[05:12:12]</a> (representing multipliers that rotate the plane) <a class="yt-timestamp" data-t="05:21:21">[05:21:21]</a>.
*   This mapping occurs by wrapping the vertical line around the unit circle without stretching or squishing <a class="yt-timestamp" data-t="05:27:27">[05:27:27]</a>.
*   A length of `2π` on the vertical line corresponds to a full revolution around the circle <a class="yt-timestamp" data-t="05:32:32">[05:32:32]</a>.
*   Therefore, going up by `π` on the vertical line translates to going exactly halfway around the circle <a class="yt-timestamp" data-t="05:40:40">[05:40:40]</a>. This halfway point on the unit circle corresponds to the multiplier `-1` <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.

The equation `e^πi = -1` means that the function `e^x` transforms the adder `πi` into the multiplier `-1` <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.