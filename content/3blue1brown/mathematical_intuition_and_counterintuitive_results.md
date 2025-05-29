---
title: Mathematical intuition and counterintuitive results
videoId: cyW5z-M2yzw
---

From: [[3blue1brown]] <br/> 

This article explores two seemingly unrelated challenges that highlight the interplay between [[spatial_intuition_in_math | mathematical intuition]] and counterintuitive results: one concerning musical harmony and another foundational concept in measure theory, which underpins integration and probability <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Both demonstrate how analytical reasoning can defy initial [[spatial_intuition_in_math | geometric intuition]] <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

## The Musical Harmony Challenge

The first challenge involves determining whether two musical notes, played with a frequency ratio `R` (between 1 and 2), will sound harmonious or cacophonous <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The task is to analyze the number `R` without listening to the notes <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Pythagorean Hypothesis

An initial approach, attributed to Pythagoras, suggests that notes sound harmonious when their frequency ratio is a rational number and cacophonous when it's irrational <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. For example, a ratio of 3/2 produces a musical fifth, and 4/3 yields a musical fourth <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This idea stems from the belief that when the ratio of frequencies is rational, a detectable pattern emerges in the beats, which the brain perceives as a rhythm or harmony <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

However, this hypothesis quickly proves insufficient, as many rational numbers (e.g., 211/198 or 1093/826) still result in unpleasant sounds <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. The issue is that these rational numbers are "more complicated," preventing the ear from easily picking up the pattern <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Measuring Complexity: Denominator Size

A simpler measure of a rational number's complexity is the size of its denominator when written in reduced form <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Thus, a revised answer might suggest that only fractions with small denominators (e.g., less than 10) produce harmonious sounds <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### Proximity to Simple Rational Numbers

Even this refinement is incomplete. Many notes sound good together even if their frequency ratio is irrational, as long as it is very close to a harmonious rational number <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This is particularly relevant for instruments like pianos, which are not tuned to exact rational intervals <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Instead, each half-step increase in frequency corresponds to multiplying the original frequency by the 12th root of 2, an irrational number <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.

For instance, a musical fifth on a piano, which is expected to be a 3/2 ratio, is actually 2^(7/12), an irrational number very close to 3/2 <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Similarly, a musical fourth is 2^(5/12), close to 4/3 <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. The chromatic scale works well because powers of the 12th root of 2 tend to be within a 1% margin of error of simple rational numbers <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

This leads to a refined rule: a ratio `R` produces a harmonious sound if it is sufficiently close to a rational number with a sufficiently small denominator <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### The Musical Savant Thought Experiment

Consider a hypothetical musical savant who finds pleasure in *all* pairs of notes with rational ratios, no matter how complicated <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. The question then becomes: would this savant find *all* ratios `R` (even irrational ones) harmonious? <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a> Since any given real number can be approximated arbitrarily closely by a rational number, it seems plausible <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. This thought experiment leads to the second challenge.

## The Covering Rational Numbers Challenge

This challenge is a foundational result in measure theory <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. It asks: can all rational numbers between 0 and 1 be covered by a collection of open intervals such that the sum of the lengths of these intervals is strictly less than 1? <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>

### The Initial Intuition

Initially, this task seems impossible <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. The rational numbers are "dense" in the real numbers, meaning any continuous stretch, no matter how small, contains infinitely many rational numbers <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. It feels like covering all rationals would necessarily cover the entire interval from 0 to 1, thus requiring a total length of at least 1 <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>. However, it is possible to achieve this <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

### The Counterintuitive Solution

The solution involves a shift from [[spatial_intuition_in_math | geometric intuition]] to analytical thinking <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>:
1.  **Enumerate the Rational Numbers**: The rational numbers between 0 and 1 can be organized into an infinitely long list <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. This means we can talk about the first, second, or *n*th rational number <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
2.  **Assign Shrinking Intervals**: To cover each rational, one specific open interval is assigned to each rational number in the list <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
3.  **Sum of Lengths**: The key insight is that each interval can be made arbitrarily small while still covering its designated rational number <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. By assigning lengths based on a convergent infinite sum (e.g., 1/2 + 1/4 + 1/8 + ...), the total sum of the interval lengths can be any positive number, including arbitrarily small values (e.g., 0.5 or 0.01) <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. This means the sum can be strictly less than 1 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### Visualizing the Counter-Intuition

The result "defies intuition" because our brain typically thinks of rationals as a dense set, making it seem impossible to "skip" any continuous stretch <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

When we zoom in on a number not covered by these intervals (e.g., √2/2), we observe that while rationals are always present within our field of view, the intervals covering them become incredibly small, very quickly <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>. This is because intervals are smaller if they correspond to rational numbers that appear later in the enumerated list, which typically means they have larger denominators <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.

This phenomenon provides a way to [[challenges_of_formalizing_mathematical_insights | formalize]] the vague idea that "the only rational numbers close to [an irrational number] have a large denominator" <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. The uncovered numbers are, in essence, "cacophonous" in the musical sense <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

### Connecting Music and Measure Theory

If we shift this setup to the interval from 1 to 2 and choose a very small total length for the intervals (e.g., 0.01), only a small percentage (1%) of the numbers will be covered <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Almost all of these covered numbers would be harmonious, such as the irrational 2^(7/12) (close to 3/2) or 2^(5/12) (close to 4/3), which fall within the "fat" intervals of their simple rational approximations <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.

Conversely, the "cacophonous" numbers (irrationals very close to high-denominator rationals, or high-denominator rationals themselves) would fall outside this 1% covered region <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

The musical savant, who finds harmony in all rational numbers, could be understood as experiencing harmony only within this "covered" 1% of numbers, provided her tolerance for error decreases exponentially for more complicated rationals <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>. The paradoxical fact that a collection of intervals can densely populate a range while covering only a tiny fraction of its values directly corresponds to the idea that harmonious numbers are rare, even for a savant <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. This connection, while surprising, highlights the profound and often [[challenges_of_formalizing_mathematical_insights | counterintuitive aspects of mathematical thinking]] <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.