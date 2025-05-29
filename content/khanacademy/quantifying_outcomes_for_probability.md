---
title: Quantifying outcomes for probability
videoId: 3v9w79NhsfI
---

From: [[khanacademy]] <br/> 

The concept of a random variable is fundamental to [[understanding_probability_concepts|understanding probability concepts]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. While they might initially seem similar to traditional variables encountered in algebra, random variables serve a distinct purpose <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## What is a Random Variable?

A random variable is a way to [[mapping_outcomes_of_random_processes|map outcomes]] of random processes to numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Essentially, it involves [[sample_space_and_possible_outcomes|quantifying the outcomes]] of an unpredictable event <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

For example, a random process could be:
*   Flipping a coin <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>
*   Rolling dice <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>
*   Measuring tomorrow's rainfall <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>

Random variables are typically denoted by capital letters, such as `X` or `Y` <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Examples

Here are some specific examples of how random variables quantify outcomes:

*   **Coin Flip**
    A random variable `X` could be defined for a fair coin flip <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>:
    *   `X = 1` if the coin rolls heads <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
    *   `X = 0` if the coin rolls tails <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
    This is a typical definition, but the numbers can be arbitrary (e.g., 100 for heads and 703 for tails would still constitute a legitimate random variable) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The key is that a random process (flipping a coin) has its outcomes mapped to numbers <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

*   **Sum of Dice Rolls**
    Another random variable `Y` could be defined as the sum of the upward faces after rolling 7 dice <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This quantifies the outcome of rolling multiple dice <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Usefulness of Random Variables

Defining random variables is crucial because it allows for mathematical operations and cleaner notation when working with [[calculating_probability|probability]] <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>:

*   **Simplifying Notation**: Instead of writing out a lengthy description of an event, a random variable allows for concise expressions. For example, to discuss the probability that the sum of 7 dice rolls is less than or equal to 30, one can simply write `P(Y <= 30)` <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Similarly, the probability that the sum is even can be written as `P(Y is even)` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

*   **Enabling Mathematical Analysis**: By quantifying outcomes, random variables make it possible to apply mathematical tools and concepts to probabilistic scenarios. This is particularly important in [[probability_in_inferential_statistics|inferential statistics]].

## Random Variables vs. Traditional Variables

It's important to distinguish random variables from the traditional variables (often lowercase letters like `x` or `y`) used in algebra <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

*   **Traditional Variables**: In algebra, you can often solve for a variable (e.g., `x` in `x + 5 = 6` equals 1) or assign values to them (e.g., `y = x + 7`, where `y` varies with `x`) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

*   **Random Variables**: A random variable, in contrast, can take on many different values, each with its own [[calculating_probabilities_for_specific_outcomes|probability]] <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. You typically discuss the [[calculating_probability|probability]] that a random variable equals a certain value, is less than or greater than something, or possesses a specific property <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.