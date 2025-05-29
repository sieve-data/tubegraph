---
title: Differences between random variables and traditional algebraic variables
videoId: 3v9w79NhsfI
---

From: [[khanacademy]] <br/> 

When first introduced to [[Random Variables | random variables]], it can be easy to confuse them with the traditional variables encountered in [[understanding_algebraic_expressions | algebra class]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. However, they are fundamentally different concepts <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## What is a Random Variable?

A [[Random Variables | random variable]] is a way to map outcomes of random processes to numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. It quantifies the outcomes of an unpredictable event <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Examples of random processes include:
*   Flipping a coin <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   Rolling dice <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>
*   Measuring tomorrow's rainfall <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>

### Defining Random Variables

[[defining_random_variables_in_different_scenarios | Random variables]] are typically denoted by capital letters, such as X or Y <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

*   **Example 1: Coin Flip**
    A [[introduction_to_random_variables | random variable]] `X` could be defined as:
    *   `X = 1` if a fair coin rolls heads <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>
    *   `X = 0` if a fair coin rolls tails <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>

    While 1 and 0 are common assignments for a coin flip, the specific numbers can be arbitrary (e.g., X=100 for heads, X=703 for tails) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The key is that the outcomes of the random process (heads or tails) are mapped to quantifiable numbers <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

*   **Example 2: Sum of Dice Rolls**
    A [[introduction_to_random_variables | random variable]] `Y` could be defined as:
    *   `Y =` the sum of the upward faces after rolling 7 dice <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

    Here, the random process involves rolling seven dice and observing their upward faces, and `Y` quantifies the sum of these observations <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Comparison with Traditional Algebraic Variables

Traditional algebraic variables, typically denoted by lowercase letters (e.g., `x`, `y`), are used in equations like `x + 5 = 6` or `y = x + 7` <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

Key distinctions:
*   **Assignment/Solving:** With traditional variables, you can either [[understanding_equality_in_algebra | solve for them]] to find a specific value (e.g., `x = 1` in `x + 5 = 6`) or assign values to them to observe how other variables change (e.g., `y` varies as a function of `x`) <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Value Representation:** A traditional variable represents a fixed unknown value or a value that can be assigned by a user.
*   **Probabilistic Nature:** This is *not* the case for [[Random Variables | random variables]] <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. A [[Random Variables | random variable]] can take on many different values, each with its own associated probability <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

> "A random variable can take on many, many, many, many, many, many different values with different probabilities." <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>

## Why Use Random Variables?

The primary utility of [[Random Variables | random variables]] becomes clear when working with [[Random Variables in Probability | probability]] <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. By quantifying outcomes, it becomes possible to perform mathematical operations and use cleaner notation <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

Consider the example of the sum of 7 dice rolls (`Y`):
*   **Without a random variable:** To express the probability that the sum is less than or equal to 30, one would have to write: "the probability that the sum of the upward faces after rolling seven dice is less than or equal to 30" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **With a random variable:** This can be compactly written as `P(Y <= 30)` <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Similarly, "what's the probability that Y is even?" replaces "what's the probability that this sum of the upward face after rolling seven dice is even?" <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

This notational clarity and mathematical framework allow for discussing the *probability* of a [[Random Variables | random variable]] equaling a certain value, being within a range, or possessing a certain property <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.