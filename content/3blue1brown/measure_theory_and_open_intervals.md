---
title: Measure theory and open intervals
videoId: cyW5z-M2yzw
---

From: [[3blue1brown]] <br/> 

[[measure_theory_in_probability | Measure theory]] is a foundational result in mathematics that serves as the formal underpinning for how mathematicians define [[integrals_and_probability_distributions | integration and probability]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. A key concept within measure theory involves riddles about [[covering_rational_numbers_with_open_intervals | covering various sets with open intervals]] <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

## Definition of an Open Interval
An open interval is defined as a continuous stretch of real numbers that are strictly greater than some number 'a' and strictly less than some other number 'b', where 'b' is greater than 'a' <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.

## The Challenge of Covering Rational Numbers
A significant challenge in measure theory involves covering all rational numbers within a given range, for instance, between 0 and 1, using open intervals <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. The condition for this challenge is that the sum of the lengths of all the chosen intervals must be strictly less than 1 <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>. This task can be accomplished by using infinitely many intervals <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.

### Counterintuitive Nature
This challenge might seem impossible because rational numbers are dense in the real numbers, meaning that any continuous stretch, no matter how small, contains infinitely many rational numbers <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. This density makes it appear that covering all rationals would necessitate covering the entire interval, thereby making the total length of the open intervals at least 1 <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

### Solution: Enumerating Rationals and Assigning Intervals
The solution involves a two-step process:
1.  **Enumerate Rational Numbers**: Organize all the rational numbers between 0 and 1 into an infinitely long list <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. A natural way to do this is to list them by increasing denominator size (in reduced form), starting with 1/2, then 1/3, 2/3, followed by 1/4, 3/4 (excluding 2/4 as it's already listed as 1/2), and so on <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. Each fraction appears exactly once in its reduced form in this list <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
2.  **Assign Specific Intervals**: Assign one specific interval to each rational number in the enumerated list <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. The sum of the lengths of these intervals can indeed be less than 1, as each individual interval can be made arbitrarily small while still covering its designated rational number <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

### Constructing the Sum of Lengths
The sum of the interval lengths can be any positive number <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This is achieved by choosing an infinite sum with positive terms that converges to 1 (e.g., 1/2 + 1/4 + 1/8 + ...) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Then, for any desired value of epsilon (a positive number like 0.5), all terms in the sum are multiplied by epsilon, resulting in an infinite sum that converges to epsilon <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. The nth interval is then scaled to have a length equal to the nth term in this new sum <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>. This means intervals get progressively smaller very quickly, especially those later in the list, which are responsible for covering rationals with large denominators <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

The surprising result is that the sum of lengths can be arbitrarily small, not just less than 1 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Intuition vs. Analytical Proof
This result often defies [[spatial_intuition_in_math | intuition]] <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a> because the proof relies on analytical thinking (treating rationals as a list), while intuition often relies on geometrical thinking (viewing rationals as a dense set on an interval that cannot be "skipped over") <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

Despite the density of rational numbers, the intervals placed on them can shrink faster than sequences of rational numbers converge to an irrational number <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. This means that a significant portion of the real numbers within an interval (e.g., 70% if epsilon is 0.3) can remain outside these infinitely many intervals <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. This concept highlights that rational numbers close to an irrational number often have very large denominators <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.