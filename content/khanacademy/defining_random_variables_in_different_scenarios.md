---
title: Defining random variables in different scenarios
videoId: 3v9w79NhsfI
---

From: [[khanacademy]] <br/> 

The idea of a [[random_variables | random variable]] can initially be confusing because it differs from the [[understanding_variables | traditional algebraic variables]] commonly encountered in algebra classes <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Unlike algebraic variables, [[random_variables | random variables]] are not values that can be solved for or explicitly assigned specific values <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.

## What is a Random Variable?

A [[random_variables | random variable]] is essentially a way to [[mapping_outcomes_to_random_variables | map outcomes]] of random processes to numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It quantifies the outcomes of an uncertain event <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Examples of Random Processes:
*   Flipping a coin <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   Rolling dice <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>
*   Measuring rainfall <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>

[[random_variables | Random variables]] are typically denoted by capital letters <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Defining Random Variables in Practice

### Example 1: Coin Flip
Consider a random variable `X` defined for a coin flip:
*   `X = 1` if the coin lands on heads <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
*   `X = 0` if the coin lands on tails <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>

While `1` for heads and `0` for tails is a common definition, a [[random_variables | random variable]] could be defined with any numerical mapping (e.g., `100` for heads, `703` for tails) and still be legitimate <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The core idea is [[mapping_outcomes_to_random_variables | mapping]] the random process's outcomes to numbers <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Example 2: Sum of Dice Rolls
Another example is a random variable `Y` defined as the sum of the upward faces after rolling seven dice <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This process quantifies the outcome of rolling multiple dice <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Why Define Random Variables?

Defining [[random_variables | random variables]] is useful because it allows for mathematical operations and cleaner notation when working with probabilities <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

Once outcomes are quantified, it becomes possible to perform mathematical analysis on them <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. For instance, instead of writing "the probability that the sum of the upward faces after rolling seven dice is less than or equal to 30" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, one can simply write:

> P(Y ≤ 30) <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>

Similarly, to ask "what's the probability that Y is even?" is much cleaner than describing the entire event <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## [[differences_between_random_variables_and_traditional_algebraic_variables | Differences between Random Variables and Traditional Algebraic Variables]]

It's crucial to understand the [[differences_between_random_variables_and_traditional_algebraic_variables | differences between random variables]] and [[understanding_variables | traditional algebraic variables]] (e.g., `x + 5 = 6` or `y = x + 7`), which are typically denoted by lowercase letters <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

*   **Traditional Variables:** Values can be assigned to them, or they can be solved for (e.g., `x = 1` in `x + 5 = 6`) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **[[random_variables | Random Variables]]:** A [[random_variables | random variable]] can take on many different values, each with different probabilities <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. It makes more sense to discuss the probability of a [[random_variables | random variable]] equaling a certain value, being less than or greater than something, or possessing a certain property <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

Further discussion will delve into the types of [[random_variables | random variables]] <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.