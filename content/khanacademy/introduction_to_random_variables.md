---
title: Introduction to random variables
videoId: 3v9w79NhsfI
---

From: [[khanacademy]] <br/> 

[[Random Variables | Random variables]] are a fundamental concept in [[random_variables_in_probability | probability]] and [[introduction_to_statistics | statistics]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Initially, they can be confusing because they differ significantly from [[differences_between_random_variables_and_traditional_algebraic_variables | traditional variables]] encountered in algebra <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## What is a Random Variable?

A [[Random Variables | random variable]] is a way to map outcomes of random processes to numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It essentially quantifies the outcomes of a random event <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Examples of random processes include:
*   Flipping a coin <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   Rolling dice <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>
*   Measuring the amount of rainfall <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>

## Notation

[[Random Variables | Random variables]] are typically denoted by capital letters, such as `X` or `Y` <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Examples of Defining Random Variables

### Coin Flip
Let's define a [[Random Variables | random variable]] `X` for a coin flip:
*   `X` = 1 if the coin lands on heads <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
*   `X` = 0 if the coin lands on tails <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>

This specific mapping (1 for heads, 0 for tails) is common, but a [[Random Variables | random variable]] could be defined with any numerical mapping (e.g., 100 for heads and 703 for tails) and still be legitimate <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The key is that a random process (flipping a coin) has its outcomes mapped to numbers <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

### Sum of Dice Rolls
Another example is defining a [[Random Variables | random variable]] `Y` as the sum of the upward faces after rolling 7 dice <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This quantifies the outcome of the random process of rolling multiple dice <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Why Use Random Variables?

The primary utility of [[Random Variables | random variables]] becomes apparent when delving deeper into [[basic_concepts_in_probability_and_statistics | probability]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. By quantifying outcomes, it becomes possible to perform mathematical operations and use more concise notation <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

For instance, instead of writing "the probability that the sum of the upward faces after rolling seven dice is less than or equal to 30" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, one can simply write:
`P(Y ≤ 30)` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>

Similarly, to ask for the probability that the sum is even, one can write:
`P(Y is even)` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>

This cleaner notation simplifies the expression of probabilities related to random processes <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Random Variables vs. Traditional Algebraic Variables

A crucial distinction exists between [[Random Variables | random variables]] and [[differences_between_random_variables_and_traditional_algebraic_variables | traditional algebraic variables]] (often denoted by lowercase letters like `x` or `y`) <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

*   **Traditional Variables**: In algebra (e.g., `x + 5 = 6` or `y = x + 7`), you can typically solve for or assign specific values to the variable <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. For `x + 5 = 6`, `x` is explicitly 1 <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Random Variables**: A [[Random Variables | random variable]] can take on many different values, each with a specific probability <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. It makes more sense to discuss the probability of a [[Random Variables | random variable]] equaling a certain value, being less than or greater than something, or possessing a certain property <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

Further discussions will explore the different [[discrete_vs_continuous_random_variables | types of random variables]], such as [[discrete_random_variables | discrete]] and [[continuous_random_variables | continuous random variables]] <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.