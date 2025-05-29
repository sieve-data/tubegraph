---
title: Binomial coefficients and combinatorics
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

This article explores how [[combinatorics_and_n_choose_k | combinatorics]] and binomial coefficients are used to calculate probabilities in scenarios involving repeated independent trials, such as coin flips. This serves as a buildup for understanding the [[binomial_distribution | binomial distribution]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Defining the Random Variable

A random variable *x* is defined as the number of heads obtained from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Random variables convert particular outcomes into numbers <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.
For five coin flips, the possible values for *x* are 0, 1, 2, 3, 4, or 5 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The goal is to determine the probability that *x* takes on each of these values <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Total Possible Outcomes

To calculate probabilities, it's essential to first determine the total number of equally likely outcomes from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
For each flip, there are two possibilities: heads (H) or tails (T) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
Since there are five flips, the total number of possible outcomes is calculated as:
$2 \times 2 \times 2 \times 2 \times 2 = 2^5 = 32$ <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>, <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

Each of these 32 outcomes is equally likely <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Calculating Probabilities for Different Numbers of Heads

The probability for each value of *x* is found by determining how many of the 32 equally likely outcomes result in that specific number of heads <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This involves using binomial coefficients, often denoted as "n choose k" or $C(n, k)$, which represents the number of ways to choose *k* items from a set of *n* items without regard to order.

### Probability that x = 0 (Zero Heads)

The probability of getting zero heads (i.e., five tails) in five flips <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>:
*   There is only one way to get no heads: TTTTT <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   Using [[combinatorics_and_n_choose_k | combinatorics]], this is "5 choose 0" (5C0), meaning choosing 0 heads from 5 flips <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
    $C(5, 0) = \frac{5!}{0!(5-0)!} = \frac{5!}{1 \times 5!} = 1$ <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>, <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   $P(x=0) = \frac{1}{32}$ <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>, <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Probability that x = 1 (One Head)

The probability of getting exactly one head in five flips <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>:
*   The single head could occur in any of the five positions (e.g., HTTTT, THTTT, TTHTT, TTTHT, TTTTH) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   This is "5 choose 1" (5C1), meaning choosing 1 head from 5 flips <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
    $C(5, 1) = \frac{5!}{1!(5-1)!} = \frac{5!}{1!4!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{(1)(4 \times 3 \times 2 \times 1)} = 5$ <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>, <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>, <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>, <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   $P(x=1) = \frac{5}{32}$ <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Probability that x = 2 (Two Heads)

The probability of getting exactly two heads in five flips <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>:
*   This is "5 choose 2" (5C2), representing the number of ways to have two heads among five flips <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    $C(5, 2) = \frac{5!}{2!(5-2)!} = \frac{5!}{2!3!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{(2 \times 1)(3 \times 2 \times 1)} = \frac{120}{12} = 10$ <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>, <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   $P(x=2) = \frac{10}{32}$ <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>, <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### Probability that x = 3 (Three Heads)

The probability of getting exactly three heads in five flips <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>:
*   This is "5 choose 3" (5C3) <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    $C(5, 3) = \frac{5!}{3!(5-3)!} = \frac{5!}{3!2!}$ <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>, <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>, <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   Notice that $C(5, 3)$ is the same calculation as $C(5, 2)$, just with the factorial terms in the denominator swapped <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   Therefore, $C(5, 3) = 10$ <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   $P(x=3) = \frac{10}{32}$ <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>, <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

### Probability that x = 4 (Four Heads)

The probability of getting exactly four heads in five flips <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>:
*   This is "5 choose 4" (5C4) <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
    $C(5, 4) = \frac{5!}{4!(5-4)!} = \frac{5!}{4!1!}$ <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>, <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   This is the same calculation as $C(5, 1)$ <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   Therefore, $C(5, 4) = 5$ <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   $P(x=4) = \frac{5}{32}$ <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>, <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   This also makes intuitive sense because getting four heads is equivalent to getting one tail, and there are five places for that one tail <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

### Probability that x = 5 (Five Heads)

The probability of getting exactly five heads in five flips <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>:
*   There is only one way to get five heads: HHHHH <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   This is "5 choose 5" (5C5) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    $C(5, 5) = \frac{5!}{5!(5-5)!} = \frac{5!}{5!0!}$ <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>, <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   Since $0! = 1$, $C(5, 5) = 1$ <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>, <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   $P(x=5) = \frac{1}{32}$ <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>, <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Symmetry in Probabilities

The probabilities calculated demonstrate a clear [[patterns_and_symmetry_in_binomial_expansions | symmetry]] <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>:
*   $P(x=0) = \frac{1}{32}$ and $P(x=5) = \frac{1}{32}$ <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   $P(x=1) = \frac{5}{32}$ and $P(x=4) = \frac{5}{32}$ <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
*   $P(x=2) = \frac{10}{32}$ and $P(x=3) = \frac{10}{32}$ <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

This [[patterns_and_symmetry_in_binomial_expansions | symmetry]] makes sense because, for example, the probability of getting five heads (zero tails) should be the same as getting zero heads (five tails) <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
These probabilities form a distribution which is a fundamental concept in the [[binomial_distribution | binomial distribution]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, which will be further explored graphically in subsequent discussions <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.