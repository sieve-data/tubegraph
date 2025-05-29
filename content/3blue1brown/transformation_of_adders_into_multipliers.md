---
title: Transformation of adders into multipliers
videoId: F_0yfvm0UoU
---

From: [[3blue1brown]] <br/> 

Euler's identity, `e^(pi * i) = -1`, is recognized as one of the most famous equations in mathematics, yet it is also one of the most confusing <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Understanding it doesn't require calculus or advanced math, but rather an open-minded approach to reframing how numbers are conceived <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Numbers as Actions

Traditionally, numbers are taught as tools for counting things, and operations like addition and multiplication are defined with respect to counting <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. However, this perspective becomes challenging when dealing with fractional or irrational numbers, and nonsensical with concepts like the square root of -1 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Instead, each number can be thought of as simultaneously three things <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
1.  **A point** on an infinitely extending line <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
2.  **An "adder"**: an action that slides the line along itself <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. When applying an adder, the point corresponding to zero ends up where the adder itself started <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. Successive application of two adders defines their sum <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  **A "multiplier"**: an action that stretches the line <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. When applying a multiplier, zero is fixed in place, and the point corresponding to one moves to where the multiplier itself started, keeping everything evenly spaced <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Successive application of two multipliers defines their product <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The Exponential Function (`e^x`)

The function written as `e^x` is not about repeated multiplication <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Instead, its fundamental purpose is to **transform adders into multipliers** in the most natural way possible <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

This transformation satisfies a key property: `e^(x+y) = e^x * e^y` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This means if you take two adders, apply them successively (sum them), and then pass the result through the `e^x` function, it's the same as first passing each adder through the function separately and then successively applying the resulting multipliers <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

> [!NOTE] Defining Property
> This property (`e^(x+y) = e^x * e^y`) is fundamental and *defines* `e^x`. The fact that it relates to repeated multiplication for counting numbers is a consequence, not the definition <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. While multiple functions satisfy this property, `e^x` (defined by an infinite sum) is considered the most natural <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. The number `e` itself is simply the value of this function at one <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

## Complex Numbers and 2D Transformations

The concept of numbers as actions (sliding and stretching) can be extended to a 2D plane <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. This is the realm of complex numbers <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. In this context:
*   A complex number is a point on the plane <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   As an **adder**, it slides the plane so that the point for zero lands on the number's point <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This means sliding sideways (real part) and up/down (imaginary part) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   As a **multiplier**, it fixes zero and moves the point for one to the number's point, keeping everything evenly spaced <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This now includes **rotating** in addition to stretching and shrinking <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### The Imaginary Unit `i`
Consider the point `i` <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>:
*   As an adder, `i` slides the plane directly upwards <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   As a multiplier, `i` rotates the plane a quarter of the way around <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   Multiplying `i` by itself (`i * i`) results in -1, meaning applying the action of `i` twice is the same as the action of -1 as a multiplier <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Therefore, `i` is the square root of -1 <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## `e^(pi*i)`: Transforming Imaginary Adders into Rotational Multipliers

Since `e^x` transforms adders into multipliers:
*   It transforms adders that slide side-to-side (real numbers) into multipliers that stretch or shrink <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   Naturally, it transforms adders that slide up and down (imaginary numbers like `y*i`) into multipliers that rotate <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

Specifically, `e^x` maps points on the vertical (imaginary) line, which represent adders that slide the plane up and down, to points on the circle with radius one in the complex plane <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This circle corresponds to multipliers that only rotate the plane <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

The most natural way for this transformation to occur is to wrap the imaginary line around the unit circle without stretching or squishing it <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This means a length of `2*pi` on the imaginary line corresponds to a full rotation around the circle <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>, consistent with the definition of `pi` as the ratio of a circle's circumference to its radius <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

Therefore, going up `pi` on the imaginary line (`pi*i`) translates to going exactly halfway around the unit circle <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. On the unit circle, halfway around from positive 1 is -1.

Thus, the function `e^x` takes the adder `pi*i` and transforms it into the multiplier -1 <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.