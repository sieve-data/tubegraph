---
title: Binomial Distribution
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

The binomial distribution is a fundamental concept in probability, often used to model the number of successes in a fixed number of independent trials. This article explores its core principles through the example of coin flips.

## Defining the Random Variable <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

To understand the [[Binomial Distribution | binomial distribution]], we first define a [[Random Variables in Probability | random variable]] `x` <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. In this example, `x` is defined as the number of heads obtained from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Like all [[Random Variables in Probability | random variables]], `x` converts particular outcomes into numbers <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

For five coin flips, the possible values for `x` (number of heads) are 0, 1, 2, 3, 4, or 5 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This means `x` is a [[Discrete Random Variables | discrete random variable]] as it can only take on a finite number of distinct values.

## Total Possible Outcomes <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>

Before calculating specific probabilities, it's essential to determine the total number of possible outcomes from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. For each flip, there are two possibilities (heads or tails) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

Since there are five flips, the total number of equally likely possibilities is calculated as 2 multiplied by itself five times, or 2^5 <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   First flip: 2 possibilities <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>
*   Second flip: 2 possibilities <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>
*   Third flip: 2 possibilities <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>
*   Fourth flip: 2 possibilities <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>
*   Fifth flip: 2 possibilities <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>

Total possible outcomes = 2 × 2 × 2 × 2 × 2 = 2^5 = 32 <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This concept aligns with [[equally_likely_possibilities_in_probability | equally likely possibilities in probability]].

## Calculating Probabilities for Each Outcome <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>

The probability for each value of `x` is determined by finding how many of the 32 [[equally_likely_possibilities_in_probability | equally likely possibilities]] result in that specific number of heads <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. This process is a buildup to understanding the [[Binomial Distribution | binomial distribution]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Probability of x = 0 (No Heads) <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>
This means all five flips are tails (TTTTT) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. There is only one way for this to occur <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   P(x=0) = 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

Using binomial coefficients (combinations), this is equivalent to choosing 0 heads from 5 flips:
```
5 choose 0 = 5! / (0! * (5-0)!) = 5! / (1 * 5!) = 1
```
Thus, P(x=0) = 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Probability of x = 1 (One Head) <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>
For one head, the head can appear in any of the five positions (e.g., HTTTT, THTTT, etc.) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. There are five such possibilities <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   P(x=1) = 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>

Using binomial coefficients:
```
5 choose 1 = 5! / (1! * (5-1)!) = 5! / (1 * 4!) = 5
```
Thus, P(x=1) = 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Probability of x = 2 (Two Heads) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>
This involves choosing 2 positions out of 5 for the heads:
```
5 choose 2 = 5! / (2! * (5-2)!) = 5! / (2! * 3!) = (5 * 4 * 3 * 2 * 1) / ((2 * 1) * (3 * 2 * 1)) = 120 / (2 * 6) = 120 / 12 = 10
```
There are 10 ways to get two heads <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   P(x=2) = 10/32 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

### Probability of x = 3 (Three Heads) <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>
This involves choosing 3 positions out of 5 for the heads:
```
5 choose 3 = 5! / (3! * (5-3)!) = 5! / (3! * 2!) = (5 * 4 * 3 * 2 * 1) / ((3 * 2 * 1) * (2 * 1)) = 120 / (6 * 2) = 120 / 12 = 10
```
There are 10 ways to get three heads <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   P(x=3) = 10/32 <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>

### Probability of x = 4 (Four Heads) <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>
This involves choosing 4 positions out of 5 for the heads:
```
5 choose 4 = 5! / (4! * (5-4)!) = 5! / (4! * 1!) = (5 * 4 * 3 * 2 * 1) / ((4 * 3 * 2 * 1) * 1) = 5
```
There are 5 ways to get four heads <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   P(x=4) = 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>

### Probability of x = 5 (Five Heads) <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>
This means all five flips are heads (HHHHH). There is only one way for this to occur <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
```
5 choose 5 = 5! / (5! * (5-5)!) = 5! / (5! * 0!) = 5! / (5! * 1) = 1
```
Thus, P(x=5) = 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Observing Symmetry <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>

The calculated probabilities demonstrate a clear pattern:
*   P(x=0) = 1/32
*   P(x=1) = 5/32
*   P(x=2) = 10/32
*   P(x=3) = 10/32
*   P(x=4) = 5/32
*   P(x=5) = 1/32

The sequence of numerators (1, 5, 10, 10, 5, 1) reveals a [[Symmetry in Binomial Probabilities | symmetry in binomial probabilities]] <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This makes intuitive sense: the probability of getting five heads is the same as getting zero tails, which should logically be the same as the probability of getting zero heads (all tails) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This [[Symmetry in Binomial Probabilities | symmetry]] is a characteristic of binomial probabilities when the probability of success (getting a head) is 0.5.

> [!NOTE] Buildup to Probability Distribution
> The calculations of these probabilities define the [[probability_distribution_functions | probability distribution]] for the random variable `x` <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. This detailed breakdown of probabilities for each outcome of a series of independent trials forms the basis of the [[Binomial Distribution | binomial distribution]].