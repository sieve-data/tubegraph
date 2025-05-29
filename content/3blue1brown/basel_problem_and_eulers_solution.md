---
title: Basel problem and Eulers solution
videoId: d-o3eB9sfls
---

From: [[3blue1brown]] <br/> 

The **Basel problem** is a mathematical challenge that asks for the sum of the inverses of the square numbers: 1 plus 1/4 plus 1/9 plus 1/16, and so on, as more and more terms are added <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This infinite sum can be written as:

$$ \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \dots $$

This problem remained [[problemsolving_strategies_in_mathematical_puzzles | unsolved]] for 90 years after it was initially posed <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Finally, [[eulers_formula_and_its_significance | Euler]] discovered the answer <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

The surprising solution found by [[eulers_formula_and_its_significance | Euler]] is $\frac{\pi^2}{6}$ <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The problem is often referred to as the Basel problem in honor of [[eulers_formula_and_its_significance | Euler]]'s hometown, Basel <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Pi and Circles

The appearance of pi in the solution often implies a connection to circles <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. While there is debate on whether pi is fundamentally about circles <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, it is deeply tied to them, suggesting that a path back to circles and geometry exists within the interconnected web of mathematics <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The proof demonstrated in the video differs from [[eulers_formula_and_its_significance | Euler]]'s original method <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, and it starts with a physical analogy involving light <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## The Lighthouse Analogy

To understand the sum physically, imagine standing at the origin of a positive number line with lighthouses placed on every positive integer (1, 2, 3, 4, and so on) <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

The apparent brightness of the first lighthouse is set to 1 <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Due to the inverse square law, the apparent brightness of the second lighthouse is 1/4 as much as the first, the third is 1/9, and the fourth is 1/16, and so on <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

The total brightness received from this infinite line of lighthouses is the sum of the Basel problem: $1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \dots$ <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The goal is to show that this total brightness equals $\frac{\pi^2}{6}$ times the brightness of the first lighthouse <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

### Apparent Brightness and the Inverse Square Law

Apparent brightness refers to the proportion of light rays from a source that hit a screen <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This is related to the solid angle covered by the screen as viewed from the light source <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

The **inverse square law** states that if you double the distance from a light source, the light will cover an area with twice the width and twice the height, meaning it covers four times the area <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Consequently, each individual screen at twice the distance receives 1/4 as much light <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Similarly, at three times the distance, it receives 1/9 as much light <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. This pattern continues because the area hit by light increases by the square of the distance, so the brightness decreases by the inverse square of the distance <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. This law applies to any quantity that spreads evenly from a point source, such as sound, heat, or radio signals <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. It's why the infinite array of lighthouses physically represents the Basel problem <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

## The Inverse Pythagorean Theorem

A key building block for manipulating light setups without changing total brightness is the **Inverse Pythagorean theorem** <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

Imagine an observer at the origin of the XY plane and a single lighthouse (H) on that plane <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. Draw a line from the lighthouse to the observer, and then another line perpendicular to that one, passing through the lighthouse <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. Place two new lighthouses (A and B) where this new perpendicular line intersects the coordinate axes <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

The brightness experienced by the observer from the first lighthouse (H) is equal to the combined brightness from lighthouses A and B <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. If 'a' is the distance to lighthouse A, 'b' to lighthouse B, and 'H' to the first lighthouse, the relationship is:

$$ \frac{1}{a^2} + \frac{1}{b^2} = \frac{1}{H^2} $$ <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>

This theorem can be proven by expressing the triangle's area in two ways or by using intuitions of light and screens <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>. If a miniature hypotenuse acts as a screen receiving light from the first lighthouse, reshaping it into the two legs of the triangle still receives the same amount of light <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. The light hitting each leg from the first lighthouse is exactly the same as the light hitting that leg from its respective new lighthouse (A or B), due to similar triangles in the limiting case of a very tiny screen <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

## Geometric Proof of the Basel Problem

The Inverse Pythagorean theorem allows transforming a single lighthouse into two others without changing the observer's brightness <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. This is used to build the infinite array of lighthouses needed for the Basel problem <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

### Step-by-Step Transformation

1.  **Initial Setup:** Imagine standing at the edge of a circular lake, directly opposite a lighthouse <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. If the distance between you and the lighthouse along the lake's border is 1, the lake's circumference is 2 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. The apparent brightness is $1 / \text{diameter}^2$. Since circumference = $\pi \times \text{diameter}$, diameter = circumference/$\pi$. So, diameter = $2/\pi$ <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. The apparent brightness is $1 / (2/\pi)^2 = \pi^2 / 4$ <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

2.  **First Transformation (2 lighthouses):** Draw a new circle twice as big (circumference 4) <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Draw a tangent line to the top of the small circle. Replace the original lighthouse with two new ones where this tangent line intersects the larger circle <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>. An important geometric fact is that if you form a triangle with a circle's diameter and any point on the circle, the angle at that point is always 90 degrees <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. This allows the Inverse Pythagorean theorem to apply, so the brightness from the two new lighthouses equals the brightness from the first: $\frac{\pi^2}{4}$ <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

3.  **Second Transformation (4 lighthouses):** Draw another circle twice as big (circumference 8) <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. For each existing lighthouse, draw a line through the top of the smaller circle (which is the center of the larger circle). Create two new lighthouses where this line intersects the larger circle <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>. Since this line is a diameter of the large circle, the lines from the two new points to the observer form a right angle <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. The line from the observer to the original lighthouse is perpendicular to the long line drawn, allowing the Inverse Pythagorean theorem to be applied <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This means the apparent brightness remains $\frac{\pi^2}{4}$ <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. These four lighthouses become evenly spaced around the lake <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

4.  **Third Transformation (8 lighthouses):** Repeat the process with a circle twice as big (circumference 16) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. For each lighthouse, draw a line through the center of the bigger circle and create two new lighthouses at the intersections <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>. The same perpendicularity conditions apply, justifying the Inverse Pythagorean theorem <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. When this is done for all lighthouses, the eight new lighthouses are evenly spaced around the larger lake <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. This is due to the inscribed angle theorem, where the angle formed by lines from two adjacent lighthouses to a point on the circumference is half the angle they make with the center (e.g., 45 degrees if the center angle is 90 degrees) <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. This divides the circle into 45-degree angle pieces, resulting in evenly spaced lighthouses <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

### The Limiting Case

As this process continues, doubling the circle size and transforming each lighthouse into two new ones, the apparent brightness to the observer remains constant at $\frac{\pi^2}{4}$ <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. The lighthouses remain evenly spaced on the circumference <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. In the limit, this setup becomes a flat horizontal line with an infinite number of lighthouses evenly spaced in both directions <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>.

The total brightness in this limiting case is still $\frac{\pi^2}{4}$ <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. This gives an infinite series:

$$ \sum_{n \text{ odd, } n \neq 0} \frac{1}{n^2} = \dots + \frac{1}{(-5)^2} + \frac{1}{(-3)^2} + \frac{1}{(-1)^2} + \frac{1}{1^2} + \frac{1}{3^2} + \frac{1}{5^2} + \dots = \frac{\pi^2}{4} $$ <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>

This sum includes all odd integers, both positive and negative <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

## Deriving the Final Solution

1.  **Sum of Positive Odd Integers:** Restricting the sum to only positive odd numbers (since $n^2 = (-n)^2$) gives half the total sum:
    $$ \sum_{n \text{ odd, } n > 0} \frac{1}{n^2} = \frac{1}{1^2} + \frac{1}{3^2} + \frac{1}{5^2} + \dots = \frac{\pi^2}{8} $$ <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>

2.  **Missing Even Integers:** The original Basel problem requires summing over all positive integers (odd and even). The missing sum is for even numbers: $\frac{1}{2^2} + \frac{1}{4^2} + \frac{1}{6^2} + \dots$ <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.
    This can be rewritten as:
    $$ \frac{1}{2^2}(1) + \frac{1}{2^2}(1/2^2) + \frac{1}{2^2}(1/3^2) + \dots = \frac{1}{4} \left( \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \dots \right) $$
    This means the sum of the reciprocals of even numbers is $\frac{1}{4}$ of the total series we are looking for <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

3.  **Combining Odd and Even Series:** Let $S = \sum_{n=1}^{\infty} \frac{1}{n^2}$.
    The sum of odd terms ($S_{odd}$) is $\frac{\pi^2}{8}$ <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
    The sum of even terms ($S_{even}$) is $\frac{1}{4} S$ <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
    Since $S = S_{odd} + S_{even}$, we have:
    $$ S = S_{odd} + \frac{1}{4} S $$ <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>
    Subtracting $\frac{1}{4} S$ from both sides gives:
    $$ \frac{3}{4} S = S_{odd} $$
    $$ S = \frac{4}{3} S_{odd} $$ <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>

    Substituting the value for $S_{odd}$:
    $$ S = \frac{4}{3} \left( \frac{\pi^2}{8} \right) = \frac{4 \pi^2}{24} = \frac{\pi^2}{6} $$ <a class="yt-timestamp" data-t="00:16:30">[00:16:30]</a>

This confirms [[eulers_formula_and_its_significance | Euler]]'s solution to the Basel problem <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. This explanation and animation were primarily created by Ben Hambricht <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.