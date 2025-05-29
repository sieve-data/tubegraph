---
title: Covering sets with open intervals
videoId: cyW5z-M2yzw
---

From: [[3blue1brown]] <br/> 

## Introduction
The concept of [[Covering sets with open intervals | covering numbers with open sets]] is a foundational result in measure theory, which provides the formal basis for how mathematicians define [[evaluating_integrals_and_the_role_of_the_convergence_point | integration]] and probability <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This concept, often found to be highly counterintuitive, involves using infinitely many intervals to cover a set of numbers <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Defining Open Intervals and Covering
An "open interval" refers to a continuous stretch of real numbers that are strictly greater than a number 'a' and strictly less than a number 'b', where 'b' is greater than 'a' <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. When discussing "covering" a set, it means that each specific number within that set must lie inside at least one of the chosen intervals <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

## The Challenge: Covering Rational Numbers
A common challenge in measure theory is to cover all rational numbers between 0 and 1 with open intervals, such that the sum of the lengths of these intervals is strictly less than 1 <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. While the most obvious approach might be to use the entire interval from 0 to 1, this challenge specifies that the total length must be less than 1 <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

This task seems impossible because rational numbers are "dense" in the real numbers <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>, meaning any continuous stretch, no matter how small, contains infinitely many rational numbers <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. Therefore, covering them without also covering the entire interval from 0 to 1 appears contradictory <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. However, it is possible <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

## The Solution
The solution involves two key steps:

### 1. Enumerating Rational Numbers
First, the rational numbers between 0 and 1 are enumerated, meaning they are organized into an infinitely long list <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. A natural way to do this is by listing them in order of their denominators, starting with 1/2, then 1/3 and 2/3, followed by 1/4 and 3/4 (excluding 2/4 as it's already listed as 1/2), and so on, continuing with all reduced fractions for each denominator <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. This process ensures each rational number appears exactly once in its reduced form, allowing for reference to the "first," "second," or "42nd" rational number <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### 2. Assigning Intervals with Converging Lengths
Next, one specific open interval is assigned to each rational number in the enumerated list <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. To ensure the total length remains less than 1, an infinite sum with positive terms that [[concept_of_infinite_sums_and_convergence | converges]] to a desired value (e.g., 1/2 + 1/4 + 1/8 ...) is chosen <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. This sum can then be multiplied by any desired epsilon (a positive number, e.g., 0.5) so that the new sum converges to epsilon <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. The length of the nth interval is then scaled to be equal to the nth term in this converging sum <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.

This means intervals get very small very quickly <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. Since each interval is only responsible for covering one rational number <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>, their sum can be arbitrarily small <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Intuition vs. Analytical Proof
This result often [[converting_analytic_reasoning_to_geometric_intuition | defies intuition]] <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The discord arises because the proof relies on analytical thinking, viewing rational numbers as an enumerable list <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>. Our intuition, however, tends to think geometrically, imagining rational numbers as a dense set on the interval where "skipping" any continuous stretch seems impossible due to the infinite rationals it would contain <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

### Visualizing Small Intervals
When illustrating this concept, especially with very small intervals, a visual representation might show the "parentheses" or markers of intervals crossing over, indicating an extremely tiny stretch between their centers <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

For example, if epsilon is chosen as 0.3, it implies that if a number between 0 and 1 is chosen at random, there's a 70% chance it falls outside these infinitely many intervals <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>. An irrational number, like the square root of 2 over 2, would be among those 70% <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. Even when zooming in on such an irrational number, while rational numbers will always appear in the field of view, the intervals placed on top of them become very small, very quickly <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This illustrates that for any sequence of rational numbers approaching an irrational number, the intervals containing them shrink faster than the sequence converges <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.

Intervals are smaller if they appear later in the enumerated list, which corresponds to rational numbers having larger denominators <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Thus, an irrational number not being covered by the intervals formalizes the idea that the only rational numbers close to it have large denominators <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

## Connection to Musical Harmony
This mathematical result has a surprising connection to musical harmony. Just as some musical ratios (like the square root of 2) sound "cacophonous" because they are far from simple rational numbers <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, an irrational number like the square root of 2 over 2 is not covered by the intervals because the rational numbers near it have large denominators <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

If the setup of covering intervals is shifted to the interval from 1 to 2 (representing musical ratios) and epsilon is set to a very small number, say 0.01 <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>, then only a tiny percentage (1%) of numbers would be covered <a class="yt-timestamp" data-t="00:11:45">[00:11:45]</a>. Almost all of these covered numbers would be harmonious, such as 2 to the 7/12ths (which is close to 3/2) covered by a "fat" interval <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>. The numbers that are cacophonous are those rational numbers with high denominators, and irrationals very close to them <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

This mathematical fact implies that even for a "musical savant" who finds pleasure in *all* rational ratios (even complicated ones) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>, harmonious numbers would still be rare (e.g., only 1% of ratios) <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. This happens if her tolerance for error decreases exponentially for more complicated rational numbers <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. The fact that a collection of intervals can densely populate a range while covering only a small percentage of its values directly corresponds to the rarity of harmonious numbers, even for a savant <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.