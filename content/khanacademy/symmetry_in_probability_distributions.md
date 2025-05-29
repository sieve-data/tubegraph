---
title: Symmetry in probability distributions
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

When analyzing certain [[Probability Distribution Functions | probability distribution functions]], particularly those related to events with two possible outcomes (like coin flips), a notable symmetry can be observed in the probabilities of the [[Random variables and probabilities | random variable]] taking on different values. This concept is foundational to understanding the [[Binomial distribution | binomial distribution]].

## Defining a Random Variable

Consider an [[Experimentation in Probability | experiment]] where a fair coin is flipped five times <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. We can define a [[Random variables and probabilities | random variable]] `x` as the number of heads obtained from these five flips <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

This [[Random variables and probabilities | random variable]] `x` can take on integer values from zero (no heads) to five (all heads) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>:
*   x = 0
*   x = 1
*   x = 2
*   x = 3
*   x = 4
*   x = 5

## Total Possible Outcomes

To determine the probability for each value of `x`, we first need to calculate the total number of possible outcomes from flipping a fair coin five times. For each flip, there are two possibilities (heads or tails) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

Since there are five flips, the total number of equally likely outcomes in the [[Sample space in probability | sample space]] is 2 multiplied by itself five times (2 to the power of 5) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>:
$2^5 = 32$ total possible outcomes <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

## Calculating Probabilities for Number of Heads

The probability for each value of `x` (number of heads) is found by dividing the number of ways to achieve that specific number of heads by the total number of outcomes (32). The number of ways to achieve `k` heads in `n` flips can be calculated using binomial coefficients, often expressed as "n choose k" or $ \binom{n}{k} $ <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.

In this case, $n=5$ (total flips).

*   **Probability that x = 0 (No heads)**
    *   There is only one way to get zero heads: TTTTT <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   This is equivalent to $\binom{5}{0} = \frac{5!}{0!(5-0)!} = 1$ <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    *   $P(x=0) = \frac{1}{32}$ <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

*   **Probability that x = 1 (One head)**
    *   There are five possible ways to get one head (e.g., HTTTT, THTTT, etc.) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   This is equivalent to $\binom{5}{1} = \frac{5!}{1!(5-1)!} = 5$ <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>, <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
    *   $P(x=1) = \frac{5}{32}$ <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>

*   **Probability that x = 2 (Two heads)**
    *   Number of ways to get two heads: $\binom{5}{2} = \frac{5!}{2!(5-2)!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{(2 \times 1)(3 \times 2 \times 1)} = 10$ <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>, <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
    *   $P(x=2) = \frac{10}{32}$ <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

*   **Probability that x = 3 (Three heads)**
    *   Number of ways to get three heads: $\binom{5}{3} = \frac{5!}{3!(5-3)!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{(3 \times 2 \times 1)(2 \times 1)} = 10$ <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>, <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
    *   $P(x=3) = \frac{10}{32}$ <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>

*   **Probability that x = 4 (Four heads)**
    *   Number of ways to get four heads: $\binom{5}{4} = \frac{5!}{4!(5-4)!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{(4 \times 3 \times 2 \times 1)(1)} = 5$ <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
    *   $P(x=4) = \frac{5}{32}$ <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>

*   **Probability that x = 5 (Five heads)**
    *   There is only one way to get five heads: HHHHH <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
    *   This is equivalent to $\binom{5}{5} = \frac{5!}{5!(5-5)!} = 1$ <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>, <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
    *   $P(x=5) = \frac{1}{32}$ <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

## Observing the Symmetry

When we list the probabilities calculated above, a clear pattern of symmetry emerges <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>:

| Number of Heads (x) | Probability (P(x)) |
| :------------------ | :------------------ |
| 0                   | 1/32                |
| 1                   | 5/32                |
| 2                   | 10/32               |
| 3                   | 10/32               |
| 4                   | 5/32                |
| 5                   | 1/32                |

The probabilities are symmetrical around the central values (x=2 and x=3) <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.
*   P(x=0) = P(x=5) = 1/32
*   P(x=1) = P(x=4) = 5/32
*   P(x=2) = P(x=3) = 10/32

This symmetry is a characteristic [[Properties of probability distribution functions | property]] of [[Binomial distribution | binomial distributions]] when the probability of success (getting a head in this case) is 0.5 (for a fair coin). This also relates to [[Patterns and symmetry in binomial expansions | patterns and symmetry in binomial expansions]]. For a large number of trials, the binomial distribution approximates the [[Normal Distribution | normal distribution]], which is also symmetrical.

The sum of all these probabilities is $ \frac{1+5+10+10+5+1}{32} = \frac{32}{32} = 1 $, which is a fundamental [[Probability distribution and density functions | property of probability distribution functions]].