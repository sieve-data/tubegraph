---
title: Uses of random variables in probability
videoId: 3v9w79NhsfI
---

From: [[khanacademy]] <br/> 

[[random_variables_overview | Random variables]] serve as a fundamental concept in [[introduction_to_probability | probability]], primarily as a method to quantify the [[events_and_outcomes_in_probability | outcomes]] of [[experimentation_in_probability | random processes]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. They map the [[events_and_outcomes_in_probability | outcomes]] of uncertain events, such as flipping a coin, rolling dice, or measuring rainfall, to numerical values <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. This process of "quantifying the [[events_and_outcomes_in_probability | outcomes]]" is central to their utility <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Why Quantify Outcomes with Random Variables?

The main advantage of using [[random_variables_and_probabilities | random variables]] is that by assigning numerical values to [[events_and_outcomes_in_probability | outcomes]], it becomes possible to apply mathematical operations and notation to these [[events_and_outcomes_in_probability | outcomes]] <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. This allows for a more streamlined and clearer way to express and analyze probabilities <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

### Practical Applications of Random Variables

*   **Simplifying Notation**: Instead of lengthy descriptive phrases, [[random_variables_and_probabilities | random variables]] allow for concise mathematical expressions. For example, if 'Y' represents the sum of the upward faces after rolling seven dice <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>, the probability that this sum is less than or equal to 30 can be written simply as `P(Y ≤ 30)` <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>, instead of "the probability that the sum of the upward faces after rolling seven dice is less than or equal to 30" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. Similarly, `P(Y is even)` is used instead of a long descriptive sentence <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Facilitating Mathematical Analysis**: Once [[events_and_outcomes_in_probability | outcomes]] are quantified, it becomes easier to perform further mathematical analysis and calculations related to their probabilities <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Distinction from Algebraic Variables

It is important to understand the [[differences_between_random_variables_and_algebraic_variables | differences between random variables and algebraic variables]] <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>:

*   **Algebraic Variables**: Typically denoted by lowercase letters (e.g., x, y), algebraic variables can be solved for a specific value or assigned a specific value to see how another variable changes <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. For example, in `x + 5 = 6`, `x` can be solved to `1` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   **Random Variables**: Generally denoted by capital letters (e.g., X, Y) <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, a [[concept_of_random_variables | random variable]] does not have a single, fixed value <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. Instead, it can take on many different values, each with a specific probability <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Therefore, it makes more sense to discuss the probability of a [[random_variables_and_probabilities | random variable]] taking on a certain value, being less than or greater than a value, or possessing a specific property <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

### Examples of Random Variables

[[examples_of_random_variables | Examples of random variables]] demonstrate how they map [[events_and_outcomes_in_probability | outcomes]] to numbers:

*   **Coin Flip (Capital X)**: A [[random_variables_and_probabilities | random variable]] 'X' can be defined for a fair coin flip, where X = 1 if heads, and X = 0 if tails <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. While these values are typical, any numerical assignment would still constitute a legitimate [[random_variables_and_probabilities | random variable]] (e.g., X = 100 for heads, X = 703 for tails) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Sum of Dice Rolls (Capital Y)**: Another [[random_variables_and_probabilities | random variable]] 'Y' can represent the sum of the upward faces after rolling seven dice <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This quantifies the [[events_and_outcomes_in_probability | outcome]] of the random process of rolling multiple dice <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

The discussion on [[discrete_vs_continuous_random_variables | types of random variables]] will further elaborate on their properties <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.