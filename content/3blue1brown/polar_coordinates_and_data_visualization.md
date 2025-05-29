---
title: Polar coordinates and data visualization
videoId: EK32jo7i5LQ
---

From: [[3blue1brown]] <br/> 

The visualization of number patterns using polar coordinates can reveal unexpected structures, even when starting with seemingly simple rules <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This approach was highlighted by a question on the Math Stack Exchange asked by Dwymark and answered by Greg Martin, connecting the distribution of prime numbers with rational approximations for pi <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Understanding Polar Coordinates

In two-dimensional space, points are typically labeled with [[vector_representation_and_coordinate_systems | xy coordinates]] <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. However, polar coordinates offer an alternative by defining a point using:
*   **r (radius):** The distance from the origin <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **theta (angle):** The angle the radial line makes with the horizontal axis, measured in radians <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. An angle of pi radians represents a half-turn, and 2 pi radians represents a full circle <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

A key characteristic of polar coordinates is their non-uniqueness; adding 2 pi to the theta coordinate does not change the physical location of the point <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## The Visualization Method

The core of this visualization involves plotting points where both the radial distance (r) and the angle (theta) are set to a given number, often a prime number <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This exercise is purely for fun and exploration in the "playground of data visualization" <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

### Visualizing All Whole Numbers

When plotting all whole numbers (n, n) in polar coordinates:
*   The point (1,1) is at distance 1 with an angle of 1 radian <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
*   The point (2,2) has twice the angle and twice the distance <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   Each subsequent point (n, n) rotates one more radian and steps one unit farther from the origin <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   This motion resembles the tip of a clock hand that rotates one radian with each tick (a little less than a sixth of a turn) and grows by one unit at each step <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.
*   The resulting pattern is an **Archimedean spiral** <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Initial Observation with Prime Numbers

When the plot is restricted to only prime numbers (p, p), the initial appearance can seem random due to primes' unpredictable behavior <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. However, zooming out reveals distinct patterns:
*   **Galactic Spirals:** Very clear, "galactic-seeming spirals" appear, with some arms noticeably missing <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Outward-Pointing Rays:** Zooming out further, these spirals give way to numerous outward-pointing rays <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. These rays often appear in clumps of four, with occasional gaps "like a comb missing its teeth" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

The presence of 20 total spirals and 280 rays at different scales raises questions about their origin and connection to prime numbers <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

### Debunking the Prime Mystery

Initially, it might seem that these patterns suggest a hidden symmetry within primes <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. However, the puzzle is somewhat misleading:
*   Similar spirals appear when plotting *all* whole numbers, not just primes <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.
*   The "all whole numbers" plot shows cleaner spirals, totaling 44 instead of 20 <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   This indicates that the origin of the spirals is separate from the properties of prime numbers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   Despite this, both questions—the origin of the spirals and what happens when filtering for primes—remain significant puzzles <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Filtering for primes leads to **Dirichlet's theorem** on the distribution of prime numbers <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

## Explanation of the Patterns

The patterns observed are a result of how the angles accumulate when plotting integers (n, n) in polar coordinates, combined with number theoretic properties, particularly concerning remainders.

### Residue Classes Modulo N

The key to understanding the spiral arms and rays lies in the concept of **residue classes modulo n**. A residue class modulo n refers to all numbers that leave the same remainder when divided by n <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

#### Modulo 6 Spirals
Zooming in reveals six small spirals <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Each arm corresponds to numbers that are a certain remainder above a multiple of 6 (e.g., multiples of 6, numbers 1 above a multiple of 6, etc.) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **Reason:** Six radians is approximately 2 pi (a full turn) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>. When counting up by 6, the angle almost completes a full turn, leading to a gentle spiral as the angle slightly decreases or increases with each cycle <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Primes Filtered:** When only primes are plotted, most of these arms disappear <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. Primes cannot be multiples of 6, or 2, 3, or 4 above a multiple of 6 (with exceptions for 2 and 3 themselves) <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Therefore, only the residue classes corresponding to numbers 1 or 5 above a multiple of 6 remain visible for primes <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

#### Modulo 44 Spirals
The larger-scale spirals, 44 in total when plotting all whole numbers, are explained similarly <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Reason:** 44 radians is very close to 7 full turns (44 / (2π) ≈ 7.0028) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This implies that 44/7 is a close rational approximation for 2 pi, or 22/7 for pi <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. As a result, counting up by multiples of 44 makes each point's angle almost identical to the last, leading to very gentle spirals <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
*   **Primes Filtered:** When filtered for primes, many residue classes modulo 44 disappear. Primes cannot be multiples of 44, or multiples of 2 or 11 (factors of 44) <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>. The remaining spirals correspond to residue classes that do not share any prime factors with 44 <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   **Relatively Prime (Coprime) and Euler's Totient Function:** Numbers that don't share any prime factors with a given number are called **relatively prime** or **coprime** <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>. For 44, there are 20 such numbers between 1 and 44 <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. This count is given by **Euler's totient function**, denoted as φ(n), where φ(44) = 20 <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. These numbers are sometimes referred to as "totitives" <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.

#### Modulo 710 Rays
The outermost pattern, appearing as "straight lines" or rays, is due to an even more precise rational approximation of 2 pi <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Reason:** 710 radians is extremely close to 113 full turns (710 / (2π) ≈ 113.000095) <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This corresponds to the very good approximation of pi as 355/113 <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a>.
*   When moving forward by steps of 710, the angle of each new point is almost exactly the same as the last, appearing as a straight line <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. In reality, with further zooming, these are still very gentle spirals <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Primes Filtered:** The factors of 710 are 71, 5, and 2 <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. Residue classes divisible by these factors (e.g., even numbers, multiples of 5, multiples of 71) contain no primes (except for the factors themselves if they are prime) and thus disappear from the prime visualization <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.
*   This filtering explains the clumps of four rays and the occasional "missing teeth" gaps, which are residue classes divisible by 5 and 71 respectively <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
*   The 280 rays observed correspond to the 280 numbers between 1 and 710 that are coprime to 710, i.e., φ(710) = 280 <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

## Dirichlet's Theorem on Arithmetic Progressions

The empirical observation that primes seem to be evenly distributed among the remaining residue classes is not accidental <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. This leads to a deep fact in number theory: **Dirichlet's theorem on arithmetic progressions** <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.

### Even Distribution of Primes
Consider residue classes modulo 10 (i.e., by their last digit) <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. Primes greater than 5 can only end in 1, 3, 7, or 9 <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. When a histogram tracks the proportion of primes falling into these four classes, they tend towards an even spread of approximately 25% each as more primes are considered <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

### Formal Statement
Dirichlet's theorem states that if you look at all prime numbers less than some large number *x*, and consider the fraction of them that have a residue of *r* modulo *n* (where *r* and *n* are coprime), that fraction will approach 1 divided by φ(*n*) as *x* approaches infinity <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.
*   This means that primes are equally dense in each of the allowable residue classes (those coprime to *n*) <a class="yt-timestamp" data-t="00:18:59">[00:18:59]</a>.
*   A simpler, but related, statement of the theorem is that each residue class that *can* contain infinitely many primes *does* contain infinitely many <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.

### Proof and Significance
The proof of Dirichlet's theorem is complex and relies heavily on **complex analysis**, which involves calculus with functions of complex numbers <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>. While primes seem unrelated to continuous calculus, this approach is standard in understanding prime distribution since the early 19th century <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. This theorem is a cornerstone of modern analytic number theory and remains relevant in contemporary research on prime gaps <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.

## Value of Playful Visualization

Though the initial visualization of (p, p) in polar coordinates might seem arbitrary and produce "artifacts" from integer radians <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>, this type of playful data visualization can lead to profound mathematical insights <a class="yt-timestamp" data-t="00:20:40">[00:20:40]</a>. It can inspire questions that lead to important theorems like Dirichlet's <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>. The interconnected nature of mathematics means that even arbitrary explorations can stumble into meaningful facts, offering a unique way to "rediscover" concepts and learn them more effectively <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>.