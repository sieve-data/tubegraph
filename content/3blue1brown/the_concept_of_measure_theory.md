---
title: The concept of measure theory
videoId: cyW5z-M2yzw
---

From: [[3blue1brown]] <br/> 

[[measure_theory_in_probability | Measure theory]] is a foundational result in mathematics <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. It serves as the formal underpinning for how mathematicians define [[fundamental_concepts_of_calculus | integration]] and [[probability_and_information_measurement | probability]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## A Foundational Challenge in Measure Theory

A key challenge related to [[measure_theory_in_probability | measure theory]] involves covering numbers with open sets <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. This concept can be very counterintuitive <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>, often defying [[mathematical_intuition_versus_analysis | intuition]] even after seeing a proof <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.

### The Challenge Defined

The challenge is to cover all rational numbers between 0 and 1 with open intervals, such that the sum of the lengths of these intervals is strictly less than 1 <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>, <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>, <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. Although this seems impossible, especially since rational numbers are dense in real numbers (meaning any stretch, no matter how small, contains infinitely many rational numbers) <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>, <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>, there is a way to achieve it <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

### The Solution

1.  **Enumerate Rational Numbers:** The first step is to organize the rational numbers between 0 and 1 into an infinitely long list <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. This can be done by listing them in reduced form, starting with 1/2, then 1/3 and 2/3, then 1/4 and 3/4 (skipping 2/4 as it's 1/2), and so on <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This method ensures each fraction appears exactly once <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
2.  **Assign Intervals:** Assign one specific interval to each rational number in the enumerated list <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>, <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.
3.  **Determine Interval Lengths:** To ensure the sum of lengths is less than 1, an infinite sum with positive terms that converges to 1 (e.g., 1/2 + 1/4 + 1/8 + ...) can be used <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>, <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   Choose any desired value of epsilon (ε) greater than 0, such as 0.5 <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>, <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
    *   Multiply all terms in the infinite sum by ε, creating a new sum that converges to ε <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>, <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.
    *   Scale the *n*th interval in the list to have a length equal to the *n*th term in this new sum <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
    *   Since ε can be arbitrarily small, the sum of the lengths of all intervals can be arbitrarily small, not just less than 1 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

### Intuition vs. Analysis

This result often defies [[mathematical_intuition_versus_analysis | intuition]] because the proof requires thinking analytically, treating rational numbers as a list, while [[mathematical_intuition_versus_analysis | intuition]] tends to think geometrically, seeing them as a dense set where skipping any continuous stretch would include infinitely many rationals <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>, <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>, <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.

The intervals become extremely small very quickly, especially for rational numbers that appear later in the enumerated list (i.e., those with large denominators) <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>, <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>, <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>, <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. This means that irrational numbers, or rational numbers with very large denominators, are unlikely to be covered by these small intervals even if they are close to rationals <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>, <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. The fact that the intervals shrink faster than any sequence of rational numbers converges formalizes the idea that certain irrational numbers (like the square root of 2 over 2) are "cacophonous" because the only rational numbers close to them have large denominators <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>, <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>, <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>, <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.