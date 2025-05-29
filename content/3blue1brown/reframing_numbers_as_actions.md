---
title: Reframing numbers as actions
videoId: F_0yfvm0UoU
---

From: [[3blue1brown]] <br/> 

Euler's identity, e to the pi i equals negative 1 <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, is one of the most famous and confusing equations in mathematics <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. For many, even those who know what each term means, the statement can seem nonsensical <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a> or feel like "black magic" even after encountering it in calculus <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Understanding this equation intuitively requires an open mind to reframing how we think about numbers <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Beyond Repeated Multiplication

Initially, we are taught to think of numbers as counting things, with addition and multiplication derived from this concept <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. However, this traditional view becomes tricky when dealing with fractional amounts <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, "very tricky" with irrational amounts <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, and "downright nonsensical" when introducing concepts like the square root of -1 <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

The expression "e to the x" is not based on repeated multiplication <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>; that interpretation only makes sense for countable numbers like 1, 2, 3, and so on <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Instead, to understand what the exponential function actually does, we need to learn to think about numbers as actions <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Numbers as Actions

Instead of solely viewing numbers as quantities, each number can be simultaneously considered as three things <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>:
1.  **A point** on an infinitely extending line <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
2.  **An "adder"**: an action that slides that line along itself <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
3.  **A "multiplier"**: an action that stretches the line <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

When thinking of numbers as adders, you slide the line until the point corresponding to zero lands where the point corresponding to the adder itself started <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. The successive application of two adders defines their sum <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

Similarly, a multiplier purely stretches the line <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. The rule for multipliers is to fix zero in place and move the point corresponding to one to where the point corresponding to the multiplier itself started, while keeping everything evenly spaced <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>. Multiplication is then redefined as the successive application of two different multiplying actions <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This concept aligns with [[group_actions_in_mathematical_objects | group actions in mathematical objects]].

## The Exponential Function: Transforming Actions

The fundamental "life's ambition" of the function e to the x (e^x) is to transform adders into multipliers as naturally as possible <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
This transformation follows a key property:
`e^(x + y) = e^x * e^y` <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>

If you take two adders, apply them successively, and then "pump the resulting sum through the function," it yields the same result as putting each adder through the function separately and then successively applying the two multipliers obtained <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. This property *defines* e^x, rather than being a consequence of repeated multiplication <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

The number e itself is simply defined as the value of this function at one <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The convention of writing the function as e^x is a "vestige" of its historical relationship with repeated multiplication <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This provides a new way of [[visualizing mathematical concepts | visualizing mathematical concepts]].

## Complex Numbers: Actions in 2D

This concept of numbers as actions extends to the 2D plane, which is where [[imaginary_numbers_and_their_reality | complex numbers]] reside <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. In this plane, each complex number is simultaneously:
*   A point on the plane <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   An adder that slides the plane so that zero lands on the number's point <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   A multiplier that fixes zero and moves one to the number's point, maintaining even spacing <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

This means multiplication in the complex plane can include both stretching/shrinking and rotation <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. All the actions of real numbers (sliding side-to-side and stretching) still apply, but new actions emerge <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

For example, the imaginary unit "i" <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>:
*   As an adder, "i" slides the plane directly upwards <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>.
*   As a multiplier, "i" rotates the plane a quarter of the way around <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

Since multiplying "i" by itself results in -1, applying the "i" action twice is the same as applying the multiplier action of -1 <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This is why "i" is the square root of -1 <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

In the complex plane, all adding is a combination of sideways and up/down sliding <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. All multiplication is a combination of stretching and rotating <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. This provides a powerful [[connection_between_numerical_and_geometric_understandings | connection between numerical and geometric understandings]].

## Euler's Identity Explained

Since e^x naturally transforms real adders (side-to-side slides) into real multipliers (stretches) <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>, the most natural expectation is for it to transform the new dimension of adders (up-and-down slides) directly into the new dimension of multipliers (rotations) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

This means e^x takes points on the vertical line (adders that slide the plane up and down) and maps them onto the circle with radius one (multipliers that rotate the plane) <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. The most natural way to do this is to wrap the vertical line around the unit circle without stretching or squishing it <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

This wrapping means it takes a length of two pi (2π) to go completely around the circle, as 2π is defined as the ratio of a circle's circumference to its radius <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. Therefore, going "up pi" on the vertical line (representing the adder pi i) translates to going exactly halfway around the circle <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Halfway around the unit circle brings you to the point -1.

In essence, the function e^x takes the adder "pi i" and transforms it into the multiplier "-1" <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, thus providing an intuitive understanding of Euler's identity: e^(pi i) = -1.