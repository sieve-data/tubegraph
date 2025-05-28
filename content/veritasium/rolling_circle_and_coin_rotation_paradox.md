---
title: Rolling circle and coin rotation paradox
videoId: FUHkTs-Ipfg
---

From: [[veritasium]] <br/> 

In 1982, a specific SAT math question stumped every student who took the exam, including the test writers themselves, highlighting a common mathematical misconception known as the [[coin_rotation_paradox | Coin Rotation Paradox]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## The 1982 SAT Question

The problematic question (Question 17) was as follows:
"In the figure above, the radius of circle A is 1/3 the radius of circle B. Starting from the position shown in the figure, circle A rolls around circle B. At the end of how many revolutions of circle A will the center of the circle first reach its starting point?" <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>

The multiple-choice options were A) 3/2, B) three, C) six, D) 9/2, or E) nine <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

### Initial Intuition vs. Reality

Many, including the test writers, initially thought the answer was three <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a> <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This intuition stems from the fact that Circle B's circumference is three times that of Circle A (since its radius is three times larger) <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Logically, it seems Circle A should rotate three times to roll around Circle B <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

However, this answer, along with all other options, was incorrect <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The actual correct answer was not listed <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Students Who Identified the Error

Despite the SAT's reputation for determining futures and the difficulty of challenging it <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, three students—Shivan Kartha, Bruce Taub, and Doug Jungreis—wrote to the College Board to point out the mistake <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. They flatly stated the test writers were wrong and provided proof <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## The Coin Rotation Paradox

The core issue lies in the [[coin_rotation_paradox | Coin Rotation Paradox]] <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. If two identical coins are used, one rolling around the other, intuition suggests it should rotate once <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. However, a demonstration shows it rotates twice <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

Applying this to the SAT question with Circle A (radius 1) and Circle B (radius 3), Circle A rotates four times as it rolls around Circle B <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. The smaller circle performs one more rotation than expected <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Explaining the "Extra" Rotation

The extra rotation occurs because Circle A is not just rolling its circumference length; it's also moving along a circular path <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. The circular path itself contributes an additional rotation for Circle A to return to its starting point <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

The general solution for a circle rolling around another circle is to find the ratio between the circumferences of the outer circle (B) and the inner circle (A), and then add one rotation to account for the circular path <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### Different Perspectives, Different Answers

The problem's wording creates ambiguity, leading to other possible interpretations:

1.  **From the perspective of Circle B:** If one observes Circle A from the perspective of Circle B, Circle A would appear to rotate only three times <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. This is analogous to unwrapping Circle B's circumference into a straight line <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
2.  **Astronomical definition of "revolution":** In astronomy, "revolution" precisely means a complete orbit around another body (e.g., Earth revolving around the Sun), distinct from rotation about its own axis <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. By this definition, Circle A would only "revolve" around Circle B once <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.

The ambiguity in the question's wording allows for at least three different justifiable solutions (1, 3, or 4 rotations) <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

## Formal Proof and General Solution

A formal proof demonstrates that the total amount a small circle rotates is always equal to the total distance its center travels, assuming it rolls without slipping <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a> <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

*   In the SAT problem, the center of Circle A travels around a circle with a radius equal to the sum of the radii of Circle A and Circle B (1+3=4). The circumference of this path is `2 * pi * 4 = 8pi` <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>.
*   Circle A's circumference is `2 * pi * 1 = 2pi` <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   Dividing the distance traveled by the center (`8pi`) by Circle A's circumference (`2pi`) yields `8pi / 2pi = 4` rotations <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a> <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

This general principle holds true for a circle rolling on any surface (polygon, blob, inside, or outside) <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

*   **Rolling outside a shape:** If a circle rolls continuously around the outside of a shape, its center travels an increased distance, specifically the perimeter of the shape plus the circle's own circumference. This results in `N + 1` rotations, where `N` is the ratio of the shape's perimeter to the circle's circumference <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
*   **Rolling inside a shape:** If a circle rolls continuously within a shape, its center travels a decreased distance, resulting in `N - 1` rotations <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Rolling along a flat line:** The distance traveled by the circle's center equals the length of the line, resulting in `N` rotations <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.

## Real-World Application: Sidereal vs. Solar Time

This principle extends to astronomy, explaining the difference between a Solar year/day and a Sidereal year/day <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

*   **Solar Day/Year:** Measured from Earth's perspective, tracking the Sun's position. A solar day is the time for the Sun to be directly overhead again (approximately 24 hours) <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. A solar year has 365.24 solar days <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   **Sidereal Day/Year:** Measured from an external observer's perspective (e.g., relative to distant stars). An external observer sees Earth complete one extra rotation around its axis per orbit around the Sun <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
    *   A sidereal day is the time for a distant star to be directly overhead again, which requires Earth to rotate exactly 360 degrees (23 hours, 56 minutes, 4 seconds) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a> <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
    *   A sidereal year has 366.24 sidereal days <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

While solar time is practical for daily life on Earth, sidereal time is crucial for astronomers to track objects in space consistently and for geostationary satellites to maintain their orbits <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a> <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>. The [[coin_rotation_paradox | Coin Rotation Paradox]] thus illuminates the difference between how we perceive time on Earth and how time is tracked in the universe <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

## Aftermath of the SAT Mistake

After reviewing the students' letters, the College Board publicly admitted its mistake and nullified Question 17 for all test takers <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. This decision led to scores being scaled without the question, potentially shifting final results by 10 points <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>. Though seemingly small, 10 points could impact educational opportunities by affecting eligibility for certain universities or scholarships <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. The re-scoring process also cost the testing service over $100,000 <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>.