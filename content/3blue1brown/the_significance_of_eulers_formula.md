---
title: The significance of Eulers formula
videoId: F_0yfvm0UoU
---

From: [[3blue1brown]] <br/> 

The equation `e^pi * i = -1` <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a> is one of the most renowned and often perplexing equations in mathematics. Its understanding can be challenging, whether one grasps its individual terms but finds the statement nonsensical <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, has encountered it in a calculus class but still perceives it as "black magic" <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>, or is unclear about the terms themselves <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. A deeper, more intuitive understanding can be achieved by reframing how we perceive numbers, without needing advanced calculus <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Reframing Numbers: Actions on a Line

Traditionally, numbers are understood as counting things, with operations like addition and multiplication tied to this concept <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. However, this becomes complicated with fractional or irrational numbers, and "downright nonsensical" when introducing concepts like the square root of -1 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Instead, numbers should be simultaneously considered as three things <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
*   A point on an infinitely extending line <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
*   An "adder," which slides the line along itself <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   A "multiplier," which stretches the line <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Numbers as Adders

When thinking of numbers as adders, one can imagine adding them to all numbers on the line simultaneously <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. An adder slides the line so that the point corresponding to zero ends up where the adder itself started <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The sum of two adders is defined by their successive application <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Numbers as Multipliers

As multipliers, numbers stretch the line <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This action fixes zero in place and brings the point corresponding to one to where the multiplier itself started, maintaining even spacing <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Multiplication is redefined as the successive application of two different multipliers <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The Role of `e^x`

The fundamental purpose of the `e^x` function is to naturally transform "adders" into "multipliers" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This means if you apply two adders successively and then process their sum through `e^x`, the result is the same as processing each adder separately through `e^x` and then successively applying the resulting multipliers <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. More succinctly, `e^(x+y) = e^x * e^y` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

This property is not a consequence of `e^x` being repeated multiplication; rather, it *defines* `e^x` <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. The number `e` itself is simply the value of this function at `x=1` <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>, and the `e^x` notation is a "vestige" of its historical connection to repeated multiplication <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Extending to the Complex Plane

The concept of numbers as points and actions can be extended to a 2D plane, which is how complex numbers are understood <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. In this context, a complex number is simultaneously:
*   A point on the plane <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   An adder that slides the plane <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   A multiplier that fixes zero and transforms other points <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

This transformation can now include rotation, along with stretching and shrinking <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. For example, the imaginary unit `i` <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>:
*   As an adder, `i` slides the plane upwards <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   As a multiplier, `i` rotates the plane a quarter turn <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

Since `i * i = -1`, applying `i` twice as a multiplier is equivalent to the action of `-1` as a multiplier, hence `i` is the square root of `-1` <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

All adding in the complex plane is a combination of sliding sideways and sliding up/down <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. All multiplication is a combination of stretching and rotating <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### `e^x` and Rotations

Given that `e^x` transforms horizontal "slides" (real number adders) into "stretches" (real number multipliers), it naturally follows that `e^x` transforms vertical "slides" (imaginary number adders) into "rotations" (complex number multipliers) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

Specifically, `e^x` takes points on the vertical (imaginary) line—which represent adders that slide the plane up and down—and places them onto the unit circle (radius one) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. These points on the unit circle correspond to multipliers that rotate the plane <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. The most natural way for this transformation to occur is by wrapping the vertical line around the circle without stretching or squishing it <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

This means that a length of `2pi` on the imaginary axis corresponds to a full rotation around the circle <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. Therefore, going "up `pi`" on the imaginary line translates to going exactly halfway around the circle <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. The `e^x` function always performs operations in the most natural way <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.

Thus, [[eulers_formula | Euler's formula]], `e^pi * i = -1` <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, intuitively means that the `e^x` function takes the adder `pi * i` (which represents sliding the plane 'up' by `pi`) and transforms it into the multiplier `-1` (which represents rotating the plane exactly halfway around) <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.