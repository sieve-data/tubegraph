---
title: Eulers Solution to Basel Problem
videoId: d-o3eB9sfls
---

From: [[3blue1brown]] <br/> 

The [[the_basel_problem | Basel Problem]] asks what sum is approached when adding the inverses of successive square numbers (1 + 1/4 + 1/9 + 1/16, and so on) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This challenge remained unsolved for 90 years after it was first posed <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a> until [[leonhard_eulers_contribution_to_mathematics | Euler]] found the answer to be pi squared divided by 6 <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. The sum is often referred to as the [[the_basel_problem | Basel Problem]] in honor of [[leonhard_eulers_contribution_to_mathematics | Euler]], whose hometown was Basel <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

## The Role of Pi

The appearance of pi, especially pi squared, in the solution to the [[the_basel_problem | Basel Problem]] is surprising <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. While some argue that pi is not fundamentally about circles, there is a perspective that suggests whenever pi appears in mathematics, there will be some connection to circles and [[mathematical_insights_and_elegant_solutions | geometry]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. In the case of the [[the_basel_problem | Basel Problem]], this connection to circles is much shorter and less convoluted than one might initially think <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## The Lighthouse Analogy

The problem can be physically represented using lighthouses <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Imagine an observer standing at the origin of a positive number line, with lighthouses placed on all positive integers (1, 2, 3, 4, etc.) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. If the first lighthouse has an apparent brightness of one, the second lighthouse appears 1/4 as bright, the third 1/9 as bright, and so on <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

This setup is useful because the total brightness received from the infinite line of lighthouses is 1 + 1/4 + 1/9 + 1/16 + ... <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. The goal is to show that this total brightness equals pi squared divided by 6 times the brightness of the first lighthouse <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. The challenge then becomes finding ways to rearrange these lighthouses without changing the total brightness for the observer <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

### The Inverse Square Law

The decreasing brightness of the lighthouses follows the inverse square law <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This law states that the brightness of a light source decreases by the inverse square of the distance from the source <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. For example, at twice the distance, the light covers an area four times larger, so each individual screen receives 1/4 as much light <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. At three times the distance, it receives 1/9 as much light <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This principle applies whenever a quantity spreads out evenly from a point source, such as sound or heat <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The inverse square law is why an infinite array of evenly spaced lighthouses physically implements the [[the_basel_problem | Basel Problem]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## The Inverse Pythagorean Theorem

A key building block for manipulating light setups is the ability to transform a single lighthouse into two <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. Consider an observer at the origin of an XY plane and a single lighthouse <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. Draw a line from the lighthouse to the observer, then a line perpendicular to that one at the lighthouse <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. Placing two new lighthouses where this perpendicular line intersects the coordinate axes results in a remarkable relationship: the brightness from the original lighthouse is equal to the combined brightness from the two new lighthouses <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

If `a` is the distance from the observer to lighthouse A, `b` to lighthouse B, and `H` to the first lighthouse, the relation is:
1/a² + 1/b² = 1/H² <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
This is known as the Inverse Pythagorean theorem <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### Proof Using Light and Screens

A visually intuitive proof involves scaling down a right triangle <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. Imagine the miniature hypotenuse as a screen receiving light from the first lighthouse <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. If this screen is reshaped to be the combination of the two legs of the miniature triangle, it still receives the same amount of light <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. The amount of light from the first lighthouse hitting the left leg is exactly the same as the amount of light from lighthouse A hitting that side <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>. Similarly, the light hitting the bottom leg from the first lighthouse is the same as the light from lighthouse B hitting that portion <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. This is due to similar triangles, which apply in the limiting case for a very tiny screen <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Building the Infinite Array

The Inverse Pythagorean theorem allows transforming a single lighthouse into two without changing the total brightness <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This transformation can be used to build the infinite array needed for the [[the_basel_problem | Basel Problem]] <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

1.  **Starting Point**: Picture an observer at the edge of a circular lake directly opposite a lighthouse <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. If the distance along the lake's border between the observer and the lighthouse is one, the lake has a circumference of 2 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. The apparent brightness from this single lighthouse is pi squared divided by 4 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

2.  **First Transformation**: Draw a new circle twice as big (circumference 4) <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Draw a tangent line to the top of the small circle and replace the original lighthouse with two new ones where this tangent line intersects the larger circle <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. Due to a geometric property that states a triangle formed with a circle's diameter and any point on the circle has a 90-degree angle at that point, the Inverse Pythagorean theorem applies <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. Thus, the brightness from the two new lighthouses equals the brightness from the first one, which is pi squared divided by 4 <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

3.  **Second Transformation**: Draw another circle twice as big (circumference 8) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. For each existing lighthouse, draw a line through the top of the smaller circle (which is the center of the larger circle) <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. Where this line intersects the larger circle, place two new lighthouses <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. Again, because the connecting line is a diameter of the large circle, the lines from the two new points to the observer form a right angle, allowing the Inverse Pythagorean theorem to be applied <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. This means the apparent brightness remains pi squared over 4 <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. After this step, there will be four evenly spaced lighthouses around the lake <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

4.  **Continuing the Process**: This process continues iteratively <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. At every step, the size of the circle doubles, and each lighthouse is transformed into two new ones <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. The apparent brightness to the observer remains constant at pi squared over 4 <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>, and the lighthouses remain evenly spaced <a class="yt-timestamp" data-t="00:13:47">[00:13:47]</a>.

### The Limiting Case

In the limit, this iterative process results in a flat horizontal line with an infinite number of lighthouses evenly spaced in both directions <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. Since the apparent brightness was pi squared over 4 throughout the process, it remains true in this limiting case <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

This yields an infinite series: the sum of the inverse squares 1/n², where `n` covers all odd integers (1, 3, 5, ...) and negative odd integers (-1, -3, -5, ...) <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. Summing these up gives pi squared over 4 <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. This demonstrates the connection between the sum of simple fractions and [[mathematical_insights_and_elegant_solutions | geometry]], as the number line can be seen as a limit of ever-growing circles <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

## Deriving the Full Solution

The sum derived from the lighthouse analogy is for all odd integers, which is pi squared over 4 <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. Restricting this sum to only the positive odd numbers gives pi squared divided by 8 <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.

The full [[the_basel_problem | Basel Problem]] requires the sum over all positive integers (odd and even) <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. The missing part is the sum of the reciprocals of even numbers <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. This missing series can be viewed as a scaled copy of the total series where each lighthouse is twice as far from the origin (1 becomes 2, 2 becomes 4, etc.) <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>. Doubling the distance for every lighthouse decreases the apparent brightness by a factor of four <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. Therefore, the sum over all even integers is 1/4 of the sum over all integers <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

Since the sum over all integers is the sum over odd integers plus the sum over even integers, we have:
Sum (all) = Sum (odd) + Sum (even)
Sum (all) = Sum (odd) + (1/4) * Sum (all)
(3/4) * Sum (all) = Sum (odd) <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

To find the sum over all positive integers from the sum over positive odd numbers (pi squared over 8), multiply by 4/3 <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
Sum (all) = (4/3) * (pi squared / 8)
Sum (all) = pi squared / 6 <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>.

This method, though different from [[leonhard_eulers_contribution_to_mathematics | Euler]]'s original proof, provides an elegant and intuitive [[mathematical_insights_and_elegant_solutions | geometric]] explanation for the solution to the [[the_basel_problem | Basel Problem]] <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.