---
title: Complex numbers and 2D plane transformations
videoId: F_0yfvm0UoU
---

From: [[3blue1brown]] <br/> 

Complex numbers can be understood by reframing how we think about numbers themselves <a class="yt-timestamp" data-t="00:37:00">[00:37:00]</a>. Instead of just counting, numbers can be considered as "actions" on a line or plane <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. This perspective helps in understanding expressions like `e^(pi*i) = -1`, which is one of the most famous and often confusing equations in mathematics <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

## Numbers as Actions

Traditionally, numbers are taught for counting, with addition and multiplication derived from this idea <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. However, this becomes challenging with fractional or irrational numbers, and "downright nonsensical" with concepts like the square root of -1 <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

Instead, each number can be viewed as simultaneously three things <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>:
*   A point on an infinitely extending line <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.
*   An "adder," which slides the line along itself <a class="yt-timestamp" data-t="01:37:00">[01:37:00]</a>.
    *   When a number acts as an adder, it slides the line until the point corresponding to zero lands where the adder itself started <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. The sum of two adders is defined by their successive application <a class="yt-timestamp" data-t="02:06:00">[02:06:00]</a>.
*   A "multiplier," which stretches the line <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
    *   When a number acts as a multiplier, it fixes zero in place and brings the point corresponding to one to where the multiplier itself started, keeping everything evenly spaced <a class="yt-timestamp" data-t="02:16:00">[02:16:00]</a>. Multiplication is redefined as the successive application of two different multiplier actions <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.

## The Exponential Function `e^x`

The function `e^x` is not repeated multiplication in the traditional sense <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. Its core ambition is to naturally transform "adders" into "multipliers" <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. This is defined by the property that applying `e^x` to the sum of two adders (`x + y`) yields the same result as applying `e^x` to each adder separately and then successively applying the resulting multipliers: `e^(x+y) = e^x * e^y` <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>. This property *defines* `e^x`, with repeated multiplication being a consequence for counting numbers <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

While multiple functions satisfy this property, `e^x` is considered the most natural, expressed by an infinite sum <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>. The number `e` itself is defined as the value of this function at one, and the `e^x` notation is a "vestige of its relationship with repeated multiplication" <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>.

## Complex Numbers as 2D Plane Transformations

The concept of numbers as actions can be extended to the two-dimensional (2D) plane, which is what [[complex_numbers_introduction | complex numbers]] represent <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

In this context, each complex number simultaneously acts as <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>:
*   A point on the plane <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
*   An "adder" that slides the entire plane so that the point for zero lands on the point for the number itself <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.
*   A "multiplier" that fixes zero in place and brings the point for one to the point for the number, while keeping everything evenly spaced <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.

Unlike real numbers, multiplication in the 2D plane can involve both stretching/shrinking and rotation <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. The actions of real numbers (sliding side-to-side and stretching) still apply, but complex numbers introduce a "whole host of new actions" <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.

### The Imaginary Unit 'i'

Consider the point 'i' on the 2D plane <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>:
*   As an adder, 'i' slides the plane straight up <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.
*   As a multiplier, 'i' rotates the plane a quarter of the way around (90 degrees) <a class="yt-timestamp" data-t="04:34:00">[04:34:00]</a>.

Since multiplying 'i' by itself results in -1, applying the 'i' action twice is equivalent to applying the action of -1 as a multiplier <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>. This means 'i' is the square root of -1 <a class="yt-timestamp" data-t="04:46:00">[04:46:00]</a>.

Generally, all complex number addition is a combination of sliding sideways and sliding up or down <a class="yt-timestamp" data-t="04:49:00">[04:49:00]</a>, and all complex number multiplication is a combination of stretching and rotating <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.

### `e^x` and Rotations in the Complex Plane

Given that `e^x` transforms adders (side-to-side slides) into multipliers (stretches) for real numbers <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>, it naturally extends to transform the new dimension of adders (up and down slides) in the complex plane directly into the new dimension of multipliers (rotations) <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.

In terms of points on the plane <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>:
*   `e^x` takes points on the vertical line (which represent adders that slide the plane up and down) <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.
*   It maps them onto the circle with radius one (which represents multipliers that rotate the plane) <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

The most natural way for this transformation to occur is to wrap the vertical line around the circle without stretching or squishing <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. This implies that a length of `2*pi` on the vertical line corresponds to a complete rotation around the circle, as `2*pi` is the ratio of a circle's circumference to its radius <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>.

Therefore, going "up pi" on the vertical line translates to going exactly halfway around the circle <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>. This intuitive behavior is precisely what `e^x` does <a class="yt-timestamp" data-t="05:45:00">[05:45:00]</a>.

Ultimately, the function `e^x` takes the adder `pi*i` and transforms it into the multiplier `-1` <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.