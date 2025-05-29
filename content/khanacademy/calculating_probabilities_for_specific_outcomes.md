---
title: Calculating probabilities for specific outcomes
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

This article details how to [[calculating_probability | calculate probabilities]] for specific outcomes when a fair coin is flipped multiple times. This process involves defining a random variable, determining the total [[sample_space_and_possible_outcomes | possible outcomes]], and then calculating the number of ways each specific outcome can occur.

## Defining the Random Variable

A random variable, often denoted as *x*, is defined to convert particular outcomes into numbers <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. In this example, the random variable *x* is defined as the number of heads from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

For five coin flips, the random variable *x* can take on the following values: 0, 1, 2, 3, 4, or 5 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## [[sample_space_and_possible_outcomes | Determining the Sample Space]]

To [[calculating_probability | calculate probability]], it's first necessary to determine the total number of [[sample_space_and_possible_outcomes | possible outcomes]] from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

*   For each flip, there are two possibilities (heads or tails) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   With five flips, the total number of equally likely outcomes is 2 raised to the power of 5 <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
    *   $2^5 = 32$ <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

There are 32 unique, equally likely outcomes when a fair coin is flipped five times <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Examples include "tails, heads, tails, heads, tails" or "heads, heads, heads, tails, tails" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## [[calculating_probability | Calculating Probabilities]] for Each Outcome

To find the probability of a specific value for *x*, we determine how many of the 32 equally likely outcomes result in that value <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This often involves using combinatorics, specifically "n choose k" (denoted as $C(n, k)$ or $\binom{n}{k}$), where *n* is the total number of flips and *k* is the number of heads we are choosing <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### Probability that x = 0 Heads ($P(x=0)$)

*   This means getting no heads out of five flips, which is equivalent to getting five tails <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   There is only one way to get zero heads (TTTTT) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   Using combinatorics: $\binom{5}{0} = \frac{5!}{0!(5-0)!} = \frac{5!}{1 \cdot 5!} = 1$ <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>.
*   $P(x=0) = \frac{1}{32}$ <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

### Probability that x = 1 Head ($P(x=1)$)

*   This means getting exactly one head out of five flips.
*   There are five possible positions for that single head (e.g., HTTTT, THTTT, TTHTT, TTTHT, TTTTH) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   Using combinatorics: $\binom{5}{1} = \frac{5!}{1!(5-1)!} = \frac{5!}{1 \cdot 4!} = 5$ <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   $P(x=1) = \frac{5}{32}$ <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### Probability that x = 2 Heads ($P(x=2)$)

*   This means getting exactly two heads out of five flips.
*   Using combinatorics: $\binom{5}{2} = \frac{5!}{2!(5-2)!} = \frac{5!}{2!3!} = \frac{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{(2 \cdot 1)(3 \cdot 2 \cdot 1)} = \frac{120}{2 \cdot 6} = \frac{120}{12} = 10$ <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   $P(x=2) = \frac{10}{32}$ <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

### Probability that x = 3 Heads ($P(x=3)$)

*   This means getting exactly three heads out of five flips.
*   Using combinatorics: $\binom{5}{3} = \frac{5!}{3!(5-3)!} = \frac{5!}{3!2!} = \frac{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{(3 \cdot 2 \cdot 1)(2 \cdot 1)} = \frac{120}{6 \cdot 2} = \frac{120}{12} = 10$ <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
    *   This calculation is symmetrical to $\binom{5}{2}$ <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   $P(x=3) = \frac{10}{32}$ <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

### Probability that x = 4 Heads ($P(x=4)$)

*   This means getting exactly four heads out of five flips.
*   Using combinatorics: $\binom{5}{4} = \frac{5!}{4!(5-4)!} = \frac{5!}{4!1!} = \frac{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{(4 \cdot 3 \cdot 2 \cdot 1)(1)} = 5$ <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
    *   This is symmetrical to $\binom{5}{1}$, as getting four heads is the same as getting one tail <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   $P(x=4) = \frac{5}{32}$ <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

### Probability that x = 5 Heads ($P(x=5)$)

*   This means getting exactly five heads out of five flips.
*   There is only one way to get five heads (HHHHH) <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   Using combinatorics: $\binom{5}{5} = \frac{5!}{5!(5-5)!} = \frac{5!}{5!0!} = \frac{5!}{5! \cdot 1} = 1$ <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    *   This is symmetrical to $\binom{5}{0}$, as getting five heads is the same as getting zero tails <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   $P(x=5) = \frac{1}{32}$ <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

## Observing Symmetry

The probabilities for the number of heads in five coin flips demonstrate a clear symmetry <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>:

*   $P(x=0) = \frac{1}{32}$
*   $P(x=1) = \frac{5}{32}$
*   $P(x=2) = \frac{10}{32}$
*   $P(x=3) = \frac{10}{32}$
*   $P(x=4) = \frac{5}{32}$
*   $P(x=5) = \frac{1}{32}$

This symmetry makes sense because the probability of getting *k* heads is the same as the probability of getting *n-k* tails (or *n-k* heads, due to the nature of a fair coin) <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. For example, getting five heads (zero tails) has the same probability as getting zero heads (five tails) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.