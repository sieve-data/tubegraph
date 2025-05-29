---
title: Outcomes in coin flipping
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

This article explores the concept of [[random_variables_and_probabilities | random variables]] by analyzing the [[events_and_outcomes_in_probability | outcomes]] of flipping a [[understanding_fair_coins_and_probability | fair coin]] five times. A [[examples_of_random_variables | random variable]], denoted as `x`, is defined as the number of heads obtained from these five flips <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Like all [[random_variables_and_probabilities | random variables]], this `x` serves to convert specific [[events_and_outcomes_in_probability | outcomes]] into numbers <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Possible Values for the Random Variable

For five coin flips, the [[random_variables_and_probabilities | random variable]] `x` (number of heads) can take on the following integer values <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>:
*   `x = 0` (zero heads)
*   `x = 1` (one head)
*   `x = 2` (two heads)
*   `x = 3` (three heads)
*   `x = 4` (four heads)
*   `x = 5` (five heads) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

The objective is to determine the [[calculating_probability_with_dice | probability]] of each of these values <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Total Possible Outcomes from Five Flips

To calculate these probabilities, it's first necessary to determine the total number of unique [[events_and_outcomes_in_probability | outcomes]] when flipping a [[understanding_fair_coins_and_probability | fair coin]] five times <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. For each flip, there are two possibilities: heads or tails <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
Since there are five flips, the total number of possible [[events_and_outcomes_in_probability | outcomes]] is:
`2 × 2 × 2 × 2 × 2 = 2^5 = 32` <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>

These 32 [[events_and_outcomes_in_probability | outcomes]] are all equally likely <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.

## Calculating Probabilities for Each Value of X

The [[calculating_probability_with_dice | probability]] for each value of `x` is found by determining how many of the 32 equally likely [[events_and_outcomes_in_probability | outcomes]] result in that specific number of heads, and then dividing by 32 <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This process is a precursor to understanding the [[binomial_distribution | binomial distribution]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### P(X = 0) - Zero Heads

To get zero heads, all five flips must result in tails. There is only one such [[events_and_outcomes_in_probability | outcome]] (TTTTT) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Combinatorial representation:** Five flips, choosing zero to be heads: `⁵C₀` <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>
    *   `⁵C₀ = 5! / (0! * (5-0)!) = 5! / (1 * 5!) = 1` <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>
*   **Probability:** `P(X=0) = 1/32` <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>, <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

### P(X = 1) - One Head

To get one head, the head can appear in any of the five positions (e.g., HTTTT, THTTT, etc.). There are five such [[events_and_outcomes_in_probability | outcomes]] <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>, <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Combinatorial representation:** Five flips, choosing one to be a head: `⁵C₁` <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>
    *   `⁵C₁ = 5! / (1! * (5-1)!) = 5! / (1 * 4!) = 5` <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>
*   **Probability:** `P(X=1) = 5/32` <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>, <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>

### P(X = 2) - Two Heads

To get two heads, we need to find how many ways two heads can be chosen from five positions.
*   **Combinatorial representation:** Five flips, choosing two to be heads: `⁵C₂` <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>
    *   `⁵C₂ = 5! / (2! * (5-2)!) = 5! / (2! * 3!) = (5 × 4 × 3!) / (2 × 1 × 3!) = (5 × 4) / 2 = 10` <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>, <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>
*   **Probability:** `P(X=2) = 10/32` <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>, <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>

### P(X = 3) - Three Heads

To get three heads, we find how many ways three heads can be chosen from five positions.
*   **Combinatorial representation:** Five flips, choosing three to be heads: `⁵C₃` <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>
    *   `⁵C₃ = 5! / (3! * (5-3)!) = 5! / (3! * 2!)` <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>
    *   This is the same calculation as `⁵C₂`, which also equals 10 <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>, <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **Probability:** `P(X=3) = 10/32` <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>, <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>

### P(X = 4) - Four Heads

To get four heads, we find how many ways four heads can be chosen from five positions.
*   **Combinatorial representation:** Five flips, choosing four to be heads: `⁵C₄` <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>
    *   `⁵C₄ = 5! / (4! * (5-4)!) = 5! / (4! * 1!) = 5` <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>
*   **Probability:** `P(X=4) = 5/32` <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>, <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
    *   This is consistent with reasoning that getting four heads is equivalent to getting one tail, and there are five positions for that single tail <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

### P(X = 5) - Five Heads

To get five heads, all five flips must result in heads. There is only one such [[events_and_outcomes_in_probability | outcome]] (HHHHH) <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>, <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Combinatorial representation:** Five flips, choosing five to be heads: `⁵C₅` <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>
    *   `⁵C₅ = 5! / (5! * (5-5)!) = 5! / (5! * 0!) = 1` <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>, <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>
*   **Probability:** `P(X=5) = 1/32` <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>, <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>
    *   This is consistent with reasoning that getting five heads is equivalent to getting zero tails <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>, <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

## Summary of Probabilities and Symmetry

The probabilities for each possible value of the [[random_variables_and_probabilities | random variable]] `x` are:
*   `P(X=0) = 1/32`
*   `P(X=1) = 5/32`
*   `P(X=2) = 10/32`
*   `P(X=3) = 10/32`
*   `P(X=4) = 5/32`
*   `P(X=5) = 1/32` <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>

Notice the symmetry in these probabilities: 1, 5, 10, 10, 5, 1 <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>, <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This symmetry makes sense because, for a [[understanding_fair_coins_and_probability | fair coin]], the [[calculating_probability_with_dice | probability]] of getting a certain number of heads is the same as getting that many tails <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. For example, `P(X=5)` (five heads) is the same as `P(0 tails)`, which is symmetrical to `P(X=0)` (zero heads or five tails) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>, <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>.

The next step in understanding this [[random_variables_and_probabilities | random variable]] is to graphically represent this [[calculating_probability_with_dice | probability]] distribution <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>, <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.