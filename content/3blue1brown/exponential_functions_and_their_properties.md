---
title: Exponential functions and their properties
videoId: F_0yfvm0UoU
---

From: [[3blue1brown]] <br/> 

The equation e<sup>πi</sup> = -1 <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a> is one of the most famous and confusing equations in mathematics <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Understanding this equation and [[e_function_and_its_properties | exponential functions]] doesn't necessarily require calculus or advanced math, but rather an open-minded approach to reframing how we think about numbers <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Reframing Numbers as Actions

Traditionally, numbers are taught as counting things, with addition and multiplication understood in relation to counting <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. However, this view becomes complicated with fractional or irrational numbers, and nonsensical with concepts like the square root of -1 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Instead, each number can be simultaneously thought of as three things <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
1.  A point on an infinitely extending line <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
2.  An "adder": an action that slides the line along itself <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
    *   An adder slides the line until the point corresponding to zero lands where the adder itself started <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   Applying two adders successively results in the same effect as applying some other single adder, which defines their sum <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  A "multiplier": an action that stretches the line <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   A multiplier fixes zero in place and brings the point corresponding to one to where the multiplier itself started, keeping everything evenly spaced <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.
    *   Multiplication is redefined as the successive application of two different multiplier actions <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The Role of `e^x`

What we write as e<sup>x</sup> is not simply [[exponential_growth_and_decay | repeated multiplication]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Repeated multiplication only makes sense when x is a countable number (like 1, 2, 3) <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

The fundamental purpose of `e^x` (the [[e_function_and_its_properties | e function]]) is to transform adders into multipliers, and to do so as naturally as possible <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

### Key Property
The defining property of `e^x` is that `e^(x+y) = e^x * e^y` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
This means:
*   If you take two adders, apply them successively, and then "pump" the resulting sum through the function, it's the same as first putting each adder through the function separately, and then successively applying the two multipliers you get <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   This property defines `e^x`, and the fact that for counting numbers it relates to repeated multiplication is a *consequence* of this property, not the definition itself <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

Many functions satisfy this property, but `e^x` is considered the most natural, defined by an infinite sum <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. The number `e` itself is simply the value of this function at one <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The convention of writing the function as `e^x` is a remnant of its connection to repeated multiplication <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Other less natural functions satisfying this property are [[exponential_growth_and_decay | exponentials]] with different bases <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Extension to Complex Numbers and Euler's Formula

The concept of numbers as actions (sliding and stretching) can be extended to the 2D plane, which is how [[normal_distribution_and_its_properties | complex numbers]] are understood <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
In the complex plane:
*   Each complex number is a point on the plane <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   An adder slides the plane so that the point for zero lands on the number's point <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   A multiplier fixes zero and brings the point for one to the number's point, keeping spacing even <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This can include rotation along with stretching and shrinking <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

The imaginary unit `i` (the square root of -1) is a specific example <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>:
*   As an adder, `i` slides the plane upwards <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   As a multiplier, `i` rotates the plane a quarter of the way around <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   Multiplying `i` by itself gives -1, meaning applying the `i` multiplier action twice is the same as the multiplier action of -1 <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

Since `e^x` transforms side-to-side slides (real adders) into stretches (real multipliers), it naturally turns the new dimension of adders (up and down slides) directly into the new dimension of multipliers (rotations) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

In terms of points on the plane, `e^x` takes points on the vertical line (corresponding to adders that slide the plane up and down) and maps them onto the circle with radius one (corresponding to multipliers that rotate the plane) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The most natural way to do this is by wrapping the line around the circle without stretching or squishing it <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This means it takes a length of 2π to go completely around the circle, as 2π is the ratio of a circle's circumference to its radius <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

Going "up π" on the imaginary axis translates to going exactly halfway around the circle <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
Therefore, the function `e^x` takes the adder `πi` (representing an upward slide of length π) to the multiplier `-1` (representing a rotation of half a circle to the point -1 on the real axis) <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This explains Euler's formula: e<sup>πi</sup> = -1 <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.