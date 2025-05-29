---
title: Coin Flip Probabilities
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

When flipping a [[concept_of_a_fair_coin_and_calculating_probability | fair coin]] multiple times, a [[Random Variables in Probability | random variable]] `x` can be defined as the number of heads obtained <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This [[Random Variables in Probability | random variable]] converts specific outcomes (like H T T H T) into numerical values (e.g., 2 heads) <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. For five coin flips, the [[Random Variables in Probability | random variable]] `x` can take on any integer value from 0 to 5 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Total Possible Outcomes from Five Flips

To determine the [[calculating_probability_of_an_event | probability]] of a specific number of heads, it's first necessary to know the total number of possible outcomes from five coin flips <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Each individual flip has two possibilities: heads (H) or tails (T) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Examples of outcomes include "tails, heads, tails, heads, tails" or "heads, heads, heads, tails, tails" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. These individual outcomes are [[equally_likely_possibilities_in_probability | equally likely]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

The total number of [[equally_likely_possibilities_in_probability | equally likely possibilities]] for five flips is calculated by multiplying the possibilities for each flip:
2 (first flip) × 2 (second flip) × 2 (third flip) × 2 (fourth flip) × 2 (fifth flip) <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
This results in 2^5, or 32 total [[equally_likely_possibilities_in_probability | equally likely possibilities]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Calculating Probabilities for X

To find the [[calculating_probability_of_an_event | probability]] that the [[Random Variables in Probability | random variable]] `x` takes on a specific value, one must determine how many of these 32 [[equally_likely_possibilities_in_probability | equally likely possibilities]] result in that value <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This analysis forms a foundation for understanding the Binomial Distribution <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Probability X = 0 (Zero Heads)

The [[calculating_probability_of_an_event | probability]] of getting zero heads means all five flips must be tails <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. There is only one such outcome (TTTTT) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   P(x = 0) = 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
This can be expressed using combinatorics as 5 choose 0 (⁵C₀), which equals 1 <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Probability X = 1 (One Head)

To get exactly one head, the single head could occur on any of the five flips (e.g., HTTTT, THTTT, TTHTT, TTTHT, TTTTH) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. There are five such possibilities <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   P(x = 1) = 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>
Using combinatorics, this is 5 choose 1 (⁵C₁), which equals 5 <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Probability X = 2 (Two Heads)

To get exactly two heads, we determine how many ways two heads can be chosen from five flips <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.
*   P(x = 2) = (5 choose 2) / 32 <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>
The calculation for 5 choose 2 (⁵C₂) is:
(5!)/(2! * (5-2)!) = (5 × 4 × 3 × 2 × 1) / ((2 × 1) × (3 × 2 × 1)) = 120 / (2 × 6) = 120 / 12 = 10 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   P(x = 2) = 10/32 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

### Probability X = 3 (Three Heads)

The [[calculating_probability_of_an_event | probability]] of getting exactly three heads is found by calculating 5 choose 3 (⁵C₃) <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
*   P(x = 3) = (5 choose 3) / 32 <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>
The calculation for 5 choose 3 (⁵C₃) is:
(5!)/(3! * (5-3)!) = (5 × 4 × 3 × 2 × 1) / ((3 × 2 × 1) × (2 × 1)) = 120 / (6 × 2) = 120 / 12 = 10 <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   P(x = 3) = 10/32 <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>

### Probability X = 4 (Four Heads)

To find the [[calculating_probability_of_an_event | probability]] of exactly four heads, we calculate 5 choose 4 (⁵C₄) <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
*   P(x = 4) = (5 choose 4) / 32 <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>
The calculation for 5 choose 4 (⁵C₄) is:
(5!)/(4! * (5-4)!) = (5 × 4 × 3 × 2 × 1) / ((4 × 3 × 2 × 1) × (1)) = 120 / (24 × 1) = 5 <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
*   P(x = 4) = 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>

### Probability X = 5 (Five Heads)

The [[calculating_probability_of_an_event | probability]] of getting exactly five heads means all five flips must be heads (HHHHH) <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. There is only one such outcome <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   P(x = 5) = (5 choose 5) / 32 <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>
The calculation for 5 choose 5 (⁵C₅) is:
(5!)/(5! * (5-5)!) = (5!)/(5! * 0!) = 1 (since 0! = 1 by definition) <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   P(x = 5) = 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

## Summary of Probabilities and Symmetry

The probabilities for the [[Random Variables in Probability | random variable]] `x` (number of heads in five flips) are:
*   P(x = 0): 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
*   P(x = 1): 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>
*   P(x = 2): 10/32 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>
*   P(x = 3): 10/32 <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>
*   P(x = 4): 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>
*   P(x = 5): 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

This set of probabilities demonstrates [[Symmetry in Binomial Probabilities | symmetry]] <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. For instance, the [[calculating_probability_of_an_event | probability]] of getting five heads (P=1/32) is the same as getting zero tails, which should inherently be the same as getting zero heads (P=1/32) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This symmetrical pattern (1, 5, 10, 10, 5, 1) is characteristic of binomial distributions <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.