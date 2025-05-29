---
title: Pis relationship to circles and geometry
videoId: d-o3eB9sfls
---

From: [[3blue1brown]] <br/> 

The mathematical constant pi (π) famously describes the ratio of a circle's circumference to its diameter. However, its appearance extends far beyond simple circular [[geometry_and_circles | geometry]], often surfacing in seemingly unrelated mathematical contexts.

## The Basel Problem

The Basel problem, initially posed and unsolved for 90 years, asks for the sum of the inverses of all positive square numbers: 1 + 1/4 + 1/9 + 1/16 + ... and so on <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Leonhard Euler discovered that this infinite sum approaches π²/6 <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The unexpected presence of pi, and particularly pi squared, in such a sum raises questions about its fundamental nature <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. The sum is named the Basel problem in honor of Euler's hometown <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Pi's Fundamental Connection to Circles

Despite pi appearing in diverse mathematical formulas, there is an argument that whenever pi emerges, a connection to circles exists within the vast interconnected web of mathematics <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. While some suggest pi is not fundamentally about circles and that insisting on geometric intuition for equations like the Basel problem is narrow-minded <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, the perspective that pi is intrinsically tied to circles implies a path leading back to [[geometry_and_circles | circles and geometry]] will always be discoverable <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Physical Intuition: The Lighthouse Analogy

To understand the Basel problem's connection to [[geometry_and_circles | geometry]], one can use a physical analogy involving lighthouses <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

### Setup
Imagine standing at the origin of a positive number line, with lighthouses placed on every positive integer (1, 2, 3, 4, ...) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.
The apparent brightness of a lighthouse is defined such that:
*   The first lighthouse (at 1) has a brightness of 1 <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   The second lighthouse (at 2) has a brightness of 1/4 as much as the first <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   The third lighthouse (at 3) has a brightness of 1/9 as much <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
This setup physically represents the Basel problem sum: the total brightness received from all lighthouses is 1 + 1/4 + 1/9 + 1/16 + ... <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The aim is to show this total brightness equals π²/6 times the brightness of the first lighthouse <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### The Inverse Square Law
The decreasing brightness with distance is due to the inverse square law <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This law states that the intensity of a quantity spreading evenly from a point source (like light, sound, or heat) decreases by the inverse square of the distance from the source <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   If light rays hit a screen one unit away from the source, doubling the distance means those rays cover an area with twice the width and twice the height, requiring four copies of the original screen to receive the same rays <a class="yt="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Thus, each screen receives 1/4 as much light <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.
*   Tripling the distance means each screen receives 1/9 as much light <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

### The Inverse Pythagorean Theorem
A key building block for manipulating lighthouse setups is the Inverse Pythagorean theorem <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>.
*   **Transformation:** Imagine an observer at the origin of an XY plane and a single lighthouse. Draw a line from the lighthouse to the observer and another line perpendicular to it at the lighthouse's position. Where this perpendicular line intersects the coordinate axes, two new lighthouses (A and B) are placed <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Theorem:** The brightness from the original lighthouse equals the combined brightness from lighthouses A and B <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. If 'a' is the distance to lighthouse A, 'b' to lighthouse B, and 'H' to the original lighthouse, the relation is 1/a² + 1/b² = 1/H² <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   **Proof Intuition:** This theorem can be demonstrated using light and screens. If a scaled-down hypotenuse of a right triangle (representing the original lighthouse's position) receives light, reshaping that "screen" to be the two legs of the miniature triangle (representing the positions of the two new lighthouses) still receives the same amount of light <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. The amount of light hitting each leg from the original lighthouse is precisely the same as the amount of light that would hit that leg from its respective new lighthouse (A or B) <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This holds true in the limiting case for a very tiny screen, leveraging similar triangles <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.

## Geometric Transformation to Derive Pi

The Inverse Pythagorean theorem allows for a series of transformations that link the lighthouse problem to pi <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

1.  **Initial Setup (Circle 1):** Imagine an observer at the edge of a circular lake, directly opposite a single lighthouse <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. If the distance along the lake's border to the lighthouse is 1, the lake has a circumference of 2. The observer's apparent brightness from this lighthouse is 1 divided by the diameter squared. Since the circumference is 2, the diameter is 2/π. Therefore, the apparent brightness is π²/4 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

2.  **First Transformation (Circle 2):** Draw a new circle twice as big (circumference 4) <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Draw a tangent line to the top of the small circle. Replace the original lighthouse with two new ones where this tangent line intersects the larger circle <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. A crucial [[geometry_and_circles | geometry]] fact is that if a triangle is formed with a circle's diameter as one side and any point on the circle as the third vertex, the angle at that third point is always 90 degrees <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. This ensures the Inverse Pythagorean theorem applies, meaning the brightness from the two new lighthouses equals the brightness from the first (π²/4) <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

3.  **Second Transformation (Circle 3):** Draw a new circle twice as big as the last (circumference 8) <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>. For each existing lighthouse, draw a line from it through the top of the *smaller* circle (which is the center of the *larger* circle). Place two new lighthouses where this line intersects the larger circle <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
    *   Since this line is a diameter of the large circle, the lines from the two new points to the observer form a right angle <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
    *   By looking at a right triangle whose hypotenuse is the diameter of the smaller circle, the line from the observer to the original lighthouse is at a right angle with the newly drawn long line <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
    *   These conditions allow the Inverse Pythagorean theorem to be applied, meaning the apparent brightness from the original lighthouse equals the combined brightness from the two newer ones <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.
    *   Repeating this for both existing lighthouses results in four new lighthouses evenly spaced around the lake <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

4.  **Continuing the Process:** This process continues by doubling the circle's size and transforming each lighthouse into two new ones along a line through the larger circle's center <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
    *   At every step, the apparent brightness to the observer remains constant at π²/4 <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
    *   At every step, the lighthouses remain evenly spaced, with a distance of 2 between each on the circumference <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.
    *   To see why the lighthouses remain evenly spaced, consider the inscribed angle theorem: if two adjacent lighthouses on the small lake make a 90-degree angle with the center, then lines drawn to a point on the circumference not between them will make an angle exactly half of that (45 degrees) <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. When this new point is at the top of the lake, these lines define the position of the new lighthouses on the larger lake, resulting in 45-degree angle pieces dividing the circle evenly at the center <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

## Limiting Case: The Sum of Inverse Odd Squares

In the limit, this infinite process transforms the circular setup into a flat horizontal line with an infinite number of lighthouses evenly spaced in both positive and negative directions <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>. Since the apparent brightness remained π²/4 throughout, it will also be π²/4 in this limiting case <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.

This limiting configuration represents the sum of the inverse squares of all odd integers (1, 3, 5, ...), and also negative odd integers (-1, -3, -5, ...), which sums to π²/4 <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.
Specifically, restricting the sum to only the positive odd numbers (1, 3, 5, ...) yields π²/8 <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.

## Deriving the Basel Problem Solution

The final step is to convert the sum of inverse odd squares to the full Basel problem sum of inverse positive integers.
The sum over all positive integers (odd and even) is desired. The sum over only the positive odd numbers is π²/8 <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.
The missing part is the sum of the reciprocals of even numbers (1/4 + 1/16 + 1/36 + ...), which can be seen as a scaled copy of the total series where each lighthouse is twice as far away <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. Doubling the distance for every lighthouse decreases the apparent brightness by a factor of four due to the inverse square law <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.
Algebraically, the sum over even integers is 1/4 times the sum over all integers. Since the sum of evens plus the sum of odds must equal the total sum, the sum over odds is 3/4 times the total sum <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
Therefore, to go from the sum over odd numbers (π²/8) to the sum over all positive integers, one must multiply by 4/3 <a class="yt-timestamp" data-t="00:16:25">[00:16:25]</a>.
(π²/8) * (4/3) = π²/6 <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>. This confirms Euler's solution to the Basel problem, providing a geometric and physical intuition for pi's unexpected appearance.