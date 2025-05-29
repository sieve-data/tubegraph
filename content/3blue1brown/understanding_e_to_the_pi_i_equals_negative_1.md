---
title: Understanding e to the pi i equals negative 1
videoId: F_0yfvm0UoU
---

From: [[3blue1brown]] <br/> 

The equation e<sup>πi</sup> = -1 <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a> is one of mathematics' most famous and confusing equations <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Many find it nonsensical even if they know what each term means, or it feels like "black magic" even after seeing it in a calculus class <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. This explanation does not require calculus or advanced math, but an open mind to reframing how we think about numbers <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Reframing Numbers as Actions

Traditionally, numbers are taught for counting, and operations like addition and multiplication are defined by counting <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This thinking becomes difficult with fractional or irrational amounts, and nonsensical with concepts like the square root of -1 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

Instead, numbers should be thought of as simultaneously three things <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
1.  A point on an infinitely extending line <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
2.  An "adder": an action that slides the line along itself <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  A "multiplier": an action that stretches the line <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Numbers as Adders
When thinking of numbers as adders, imagine sliding the line <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The rule for an adder is: slide the line until the point corresponding to zero ends up where the adder itself started <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. The sum of two adders is defined by the effect of successively applying them <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Numbers as Multipliers
A multiplier is a way to stretch the line <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. The rule is to fix zero in place and bring the point corresponding to one to where the multiplier itself started, keeping everything evenly spaced <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Multiplication is redefined as the successive application of two different multiplier actions <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The Function e<sup>x</sup>

The function e<sup>x</sup> (the exponentiation of the number e) transforms adders into multipliers, doing so as naturally as possible <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. Its defining property is that applying the function to the sum of two adders (e.g., x + y) is the same as applying the function to each adder separately and then successively applying the resulting multipliers <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. More succinctly: e<sup>x+y</sup> = e<sup>x</sup> * e<sup>y</sup> <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

This property *defines* e<sup>x</sup> <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. The fact that it relates to repeated multiplication for counting numbers is a *consequence* of this property <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Many functions satisfy this property, but the one expressed by an infinite sum is considered the most natural <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. The number [[Properties of Eulers Number e | e]] itself is defined as the value of this function at one <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>; the function as a whole is more special than the number <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>.

## Complex Numbers and Actions in 2D

The concept of sliding and stretching can be extended to the 2D plane, which is what complex numbers represent <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. In this context, each complex number is simultaneously <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>:
1.  A point on the plane <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
2.  An adder: slides the plane so zero lands on the number's point <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
3.  A multiplier: fixes zero and brings one to the number's point, keeping spacing even <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

This 2D multiplication can include rotation along with stretching and shrinking <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Real numbers still correspond to side-to-side sliding and stretching, but complex numbers introduce new actions <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### The Number 'i'
Consider the point 'i' on the complex plane <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   As an adder, 'i' slides the plane upwards <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   As a multiplier, 'i' turns the plane a quarter of the way around <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

Since multiplying 'i' by itself results in -1, applying the 'i' action twice as a multiplier is the same as the action of -1 (a 180-degree rotation) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Thus, 'i' is the square root of -1 <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## Connecting e<sup>x</sup> to Complex Numbers

All adding is a combination of sliding sideways and up/down <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. All multiplication is a combination of stretching and rotating <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Since e<sup>x</sup> already turns side-to-side slides (real adders) into stretches (real multipliers) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>, it naturally turns the new dimension of adders (up-and-down slides) into the new dimension of multipliers (rotations) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

This means e<sup>x</sup> takes points on the vertical line (adders that slide up and down) and maps them onto the circle with radius one (multipliers that rotate the plane) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The most natural way to do this is to wrap the line around the circle without stretching or squishing <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This implies it takes a length of two [[Geometric Intuition of Pi | pi]] to go completely around the circle, as [[Geometric Intuition of Pi | pi]] is defined as the ratio of a circle's circumference to its radius <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

Therefore, going "up [[Geometric Intuition of Pi | pi]]" (i.e., applying an adder of πi) translates to going exactly halfway around the unit circle <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. The function e<sup>x</sup> always behaves in the most natural way <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

In conclusion, the function e<sup>x</sup> takes the adder πi (which represents sliding up by a distance of π) and transforms it into the multiplier -1 (which represents rotating 180 degrees) <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.