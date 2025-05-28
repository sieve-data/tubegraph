---
title: Mathematical reasoning and coin rotation paradox
videoId: FUHkTs-Ipfg
---

From: [[veritasium]] <br/> 

In 1982, a specific question on the SAT mathematics exam stumped every single student who took it <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The question involved two circles, A and B, where the radius of circle A was 1/3 the radius of circle B <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. Circle A rolled around circle B, and students were asked how many revolutions circle A would make to return its center to its starting point <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

The intuitive answer for many, including the test writers themselves, was three <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This was based on the logic that since the circumference of circle B is three times that of circle A (due to its three times larger radius), circle A should logically rotate three times <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. However, this answer was incorrect, and surprisingly, none of the listed options were correct either <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The test writers admitted their mistake, having also believed the answer was three <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## The Problem with the SAT Question

The error in question 17 of the 1982 SAT was significant, especially given the exam's reputation for determining college admissions and future opportunities <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Out of 300,000 test takers, only three students—Shivan Kartha, Bruce Taub, and Doug Jungreis—identified the error and wrote to the College Board, the SAT's administrator <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. They confidently stated that the College Board was wrong and provided proof <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## The Coin Rotation Paradox

The core of the SAT question's error lies in a phenomenon known as the [[counterintuitive_logic_puzzles | coin rotation paradox]] <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

Consider two identical coins. Intuitively, if one coin rolls around the other, it should rotate exactly once because their circumferences are the same <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. However, upon demonstration, it becomes clear that the rolling coin rotates twice by the time it completes its path around the stationary coin <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

This paradox applies directly to the SAT question. When circle A (with 1/3 the radius of circle B) rolls around circle B, it rotates not three times, but four times in total <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This is one more rotation than initially expected <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### The General Solution

The additional rotation occurs because the smaller circle is not merely rolling a straight distance equal to the larger circle's circumference; it is also going *around* a circular path <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This circular path itself contributes an additional rotation <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

The general solution for a circle rolling around another circle is to calculate the ratio between the circumferences of the larger circle (B) and the smaller circle (A), and then add one rotation to account for the circular path <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

#### Mathematical Proof

A formal [[mathematicians_perspectives_on_collatz_conjecture | mathematical proof]] explains this phenomenon:
The amount a small circle rotates is always equal to the distance its center travels, assuming it rolls without slipping <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

*   **Rolling on a flat line**: The distance traveled by the center of the circle is equal to the length of the line. Dividing this by the circle's circumference gives `N` rotations <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Rolling continuously around the *outside* of a shape**: The distance traveled by the circle's center increases by exactly one circumference of the rolling circle. Therefore, the total number of rotations is `N + 1` <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **Rolling continuously within the *inside* of a shape**: The distance traveled by the circle's center decreases by one circumference of the rolling circle. Thus, the total number of rotations is `N - 1` <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

In the SAT problem, the radius of circle B is three times that of circle A. The center of circle A travels a path with a radius equal to the sum of the radii of circle A and circle B (R_B + R_A = 3R_A + R_A = 4R_A). The circumference of this path is 2π(4R_A) = 8πR_A <a class="yt-timestamp" data-t="00:09:45">[00:09:45]</a>. Since the circumference of circle A is 2πR_A, dividing 8πR_A by 2πR_A gives 4 rotations <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.

### Alternative Interpretations

The ambiguity of the question's wording allowed for other justifiable answers:
*   **Perspective of Circle B**: If one considers the rotation from the perspective of circle B looking out at circle A, circle A rotates three times <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. This is analogous to "straightening out" the circular path <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.
*   **Astronomical Definition of Revolution**: In astronomy, a "revolution" is a complete orbit around another body, distinct from rotating about one's own axis <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. By this definition, circle A only revolves around circle B once <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

The SAT question's extreme ambiguity, allowing for at least three different defensible solutions, highlighted a significant flaw <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.

## Astronomical Implications: Sidereal vs. Solar Time

The principle behind the [[counterintuitive_logic_puzzles | coin rotation paradox]] is not just a [[mathematical_permutations_and_loops | mathematical]] curiosity; it is essential for accurate timekeeping in astronomy <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.

*   **Solar Day/Year**: When we count 365.24 days in a year on Earth, we are measuring the time it takes for the sun to appear directly overhead again (a solar day) <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. From our perspective on Earth, this implies 365.24 rotations <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   **Sidereal Day/Year**: To an external observer (e.g., relative to distant stars), the Earth performs one extra rotation due to its circular path around the Sun <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. Thus, an external observer counts 366.24 rotations in a year, known as a Sidereal year <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. A Sidereal day is 23 hours, 56 minutes, and four seconds long – the time it takes for a distant star to appear directly overhead again <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

This difference is crucial:
*   **Solar time** is practical for daily life on Earth, ensuring day and night align with solar positions <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **Sidereal time** is used by astronomers to track objects in space, ensuring telescopes are always pointed at the same region of the sky each night, and by geostationary satellites to maintain their orbits <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

## Aftermath of the SAT Error

Following the students' letters, the College Board publicly admitted its mistake and nullified question 17 for all test takers <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. This decision, while rectifying the error, caused scores to be re-scaled, potentially shifting them by up to 10 points out of 800 <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. This seemingly small shift could have an impact on college admissions or scholarship eligibility <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. The rescoring process itself cost the testing service over $100,000 <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

The incident highlights the importance of thorough mathematical reasoning and the surprising complexities that can arise even in seemingly simple geometric problems.