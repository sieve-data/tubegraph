---
title: Understanding e to the pi i equals negative 1
videoId: F_0yfvm0UoU
---

From: [[3blue1brown]] <br/> 

The equation `e` to the `pi` `i` equals `-1` is recognized as one of the most famous equations in mathematics, yet it is also one of the most confusing <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Those encountering this concept often fall into one of three groups:
1.  Individuals who understand the meaning of each term but find the overall statement nonsensical <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
2.  Those who have encountered explanations in a calculus class involving long formulae, which, while explaining *why* it works, still leave the concept feeling like "black magic" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
3.  People who are not entirely clear on what the terms themselves represent <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

Ironically, those in the third category may be best positioned to grasp the explanation, as it doesn't require calculus or advanced math <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Instead, it requires an open mind to reframe how numbers are perceived <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This reframing clarifies the equation's meaning, its truth, and its intuitive sense <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Reframing Numbers: From Counting to Actions

Initially, numbers are taught as tools for counting things, with addition and multiplication understood in relation to counting <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This perspective becomes challenging when dealing with fractional amounts, very tricky with irrational amounts, and "downright nonsensical" when introducing concepts like the square root of -1 (i.e., `i`) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

To truly understand the function `e` to the `x`, it's necessary to conceptualize numbers as actions <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Each number can be simultaneously considered three things <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
1.  A point on an infinitely extending line <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
2.  An "adder," which slides the line along itself <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  A "multiplier," which stretches the line <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Adders

When thinking of numbers as adders, one can imagine adding them to all numbers as points on the line simultaneously <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. An adder's action is defined by sliding the line until the point corresponding to zero lands where the point corresponding to the adder itself started <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The sum of two adders is defined by the effect of successively applying them <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Multipliers

Forgetting previous knowledge of multiplication, a multiplier is purely a way to stretch the line <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. The rule for a multiplier is to fix zero in place and bring the point corresponding with one to where the point corresponding with the multiplier itself started, while keeping everything evenly spaced <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Multiplication is redefined as the successive application of two different multiplier actions <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## The Function `e` to the `x`

The "life's ambition" of `e` to the `x` is to transform adders into multipliers as naturally as possible <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This means if two adders are successively applied and their resulting sum is then fed through the function, it yields the same result as putting each adder through the function separately and then successively applying the two multipliers obtained <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. More succinctly, this property is `e^(x+y) = e^x * e^y` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

While this property is a consequence if `e` to the `x` were simply repeated multiplication, the inverse is true: this property *defines* `e` to the `x` <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. The fact that it relates to repeated multiplication for counting numbers is a consequence of this fundamental property <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

Although multiple functions satisfy this property, one stands out as the most natural, expressed by an infinite sum <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. [[importance_of_eulers_number_e_in_calculus|The number e]] itself is defined as the value of this function at one <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The number `e` is not as special as the function as a whole; the convention to write this function as `e` to the `x` is a "vestige of its relationship with repeated multiplication" <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. Other less natural functions satisfying this property are exponentials with different bases <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## [[relationship_between_e_to_the_x_and_complex_numbers|Complex Numbers]] and the 2D Plane

To understand "e to the pi i," one only needs to think about converting adders into multipliers <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This concept of sliding and stretching can be extended to the 2D plane, which is precisely what [[relationship_between_e_to_the_x_and_complex_numbers|complex numbers]] represent <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

In the 2D plane, each number is simultaneously:
*   A point on the plane <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   An adder, which slides the plane so that the point for zero lands on the point for the number <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   A multiplier, which fixes zero in place and brings the point for one to the point for the number while keeping everything evenly spaced <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

This expansion means that multiplication can now include rotation, along with stretching and shrinking <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. All actions of real numbers (sliding side-to-side and stretching) still apply, but a host of new actions are introduced <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

Consider the point "i" (the imaginary unit) <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>:
*   As an adder, it slides the plane up <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   As a multiplier, it turns the plane a quarter of the way around <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.

Since multiplying `i` by itself gives `-1`, applying this action twice is the same as the multiplier action of `-1` <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. Therefore, `i` is the square root of `-1` <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

All adding in the complex plane is a combination of sliding sideways and sliding up or down <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>, and all multiplication is a combination of stretching and rotating <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

Since `e` to the `x` transforms horizontal slides (real adders) into stretches (real multipliers) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>, the most natural expectation is for it to transform the new dimension of adders (vertical slides, or imaginary numbers) directly into the new dimension of multipliers (rotations) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

In terms of points on the plane, `e` to the `x` takes points on the vertical line (which correspond to adders that slide the plane up and down) and puts them on the [[eulers_formula_and_unit_circle|unit circle]] with radius one (which corresponds to multipliers that rotate the plane) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The most natural way to do this is to wrap the line around the circle without stretching or squishing it <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This means it takes a length of `2pi` to go completely around the circle, as [[relationship_between_counting_and_pi|pi]] is, by definition, the ratio of a circle's circumference to its radius <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

Therefore, going up `pi` on the imaginary axis (i.e., `pi i`) translates to going exactly halfway around the circle <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. When there's a natural way to do something, `e` to the `x` will do it <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Thus, the function `e` to the `x` takes the adder `pi i` to the multiplier `-1` <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.