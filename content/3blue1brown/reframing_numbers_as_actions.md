---
title: Reframing numbers as actions
videoId: F_0yfvm0UoU
---

From: [[3blue1brown]] <br/> 

The equation `e^(πi) = -1` is a highly famous and often confusing mathematical statement <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Understanding it doesn't require advanced calculus but rather an open-minded approach to [[Conceptualizing Mathematical Problems | reframing how we think about numbers]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Numbers Beyond Counting

Traditionally, numbers are introduced for counting, and operations like addition and multiplication are taught with respect to this concept <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. However, this traditional view becomes challenging when dealing with fractional amounts <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, "very tricky" with [[rational_versus_irrational_numbers_in_music | irrational amounts]] <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, and "downright nonsensical" when introducing concepts like the [[the_concept_of_imaginary_numbers | square root of -1]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

Instead, numbers should be conceptualized as simultaneously three things <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
1.  A point on an infinitely extending line <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
2.  An "adder," which is an action that slides that line along itself <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  A "multiplier," which is an action that stretches the line <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Numbers as Adders

When thinking of numbers as adders, the action involves sliding the line such that the point corresponding to zero ends up where the point corresponding to the adder itself started <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The sum of two adders is defined by the effect of successively applying both adders <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Numbers as Multipliers

Similarly, a multiplier is a way to stretch the line <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. The rule is to fix zero in place and bring the point corresponding to one to where the point corresponding with the multiplier started, while keeping everything evenly spaced <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Multiplication is then redefined as the successive application of two different multiplier actions <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The Exponential Function (e^x)

The fundamental purpose of the exponential function, written as `e^x`, is to transform adders into multipliers in the most natural way possible <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This means if you apply two adders successively (`x + y`) and then pass the sum through the function, the result is the same as first putting each adder through the function separately (`e^x`, `e^y`) and then successively applying the resulting multipliers <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. This property is succinctly stated as `e^(x+y) = e^x * e^y` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

> [!NOTE] Defining Property
> This property defines `e^x` <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. The idea that `e^x` is repeated multiplication is a consequence for counting numbers, not the definition itself <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

While multiple functions satisfy this property, the exponential function `e^x` stands out as the most natural, expressed through an infinite sum <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. The number `e` itself is simply the value of this function when `x` is one <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The convention of writing it as `e^x` is a "vestige" of its historical relationship with repeated multiplication <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Reframing [[Conceptualizing complex numbers | Complex Numbers]]

The concept of sliding and stretching can be extended to the 2D plane, which is where [[complex_numbers_and_transformations | complex numbers]] reside <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. In this plane, each complex number is simultaneously:
*   A point on the plane <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
*   An adder that slides the plane so that zero lands on the number's point <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   A multiplier that fixes zero in place and brings the point for one to the point for the number, keeping everything evenly spaced <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

This means complex number multipliers can involve not just stretching but also rotation <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Real numbers still represent side-to-side sliding and stretching, but the complex plane introduces new actions <a class="yt> [00:04:21]</a>.

For instance, the imaginary unit `i` (the [[the_concept_of_imaginary_numbers | square root of -1]]) is a specific point in the plane <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>:
*   As an adder, `i` slides the plane upwards <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   As a multiplier, `i` rotates the plane a quarter of the way around <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. Multiplying by `i` twice (applying the action twice) results in `-1`, which is why `i` is the [[the_concept_of_imaginary_numbers | square root of -1]] <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

All complex addition is a combination of sliding sideways and up/down <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>, while all complex multiplication is a combination of stretching and rotating <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Connecting e^x to Complex Numbers

Given that `e^x` transforms side-to-side slides (real adders) into stretches (real multipliers), it naturally follows that `e^x` transforms the "new dimension" of adders (up and down slides, representing imaginary numbers) directly into the "new dimension" of multipliers (rotations) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

In terms of points on the plane, `e^x` takes points on the vertical (imaginary) line and maps them onto the unit circle (multipliers that rotate the plane) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The most natural way to do this is to wrap the imaginary line around the circle without stretching or squishing it <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This means a length of two pi on the imaginary line corresponds to a full rotation around the circle, consistent with the definition of pi as the ratio of a circle's circumference to its radius <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

Therefore, going "up pi" on the imaginary line (i.e., `πi`) translates to going exactly halfway around the unit circle <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. A half-rotation on the unit circle lands on the point `-1`. Thus, the function `e^x` takes the adder `πi` to the multiplier `-1` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This reframing of numbers as actions provides an intuitive understanding of Euler's identity: `e^(πi) = -1`.