---
title: Concept of random variables
videoId: 3v9w79NhsfI
---

From: [[khanacademy]] <br/> 

A [[random_variables_overview | random variable]] is a fundamental concept in [[introduction_to_probability | probability]] used to map outcomes of random processes to numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This allows for the quantification of outcomes <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## [[differences_between_random_variables_and_algebraic_variables | Distinction from Traditional Variables]]

Initially, [[random_variables_overview | random variables]] can be confusing because they differ from the algebraic variables commonly encountered in mathematics <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

Traditional algebraic variables (often denoted by lowercase letters like `x` or `y`) can be solved for a specific value or assigned specific values <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. For example, in `x + 5 = 6`, `x` can be solved as `1` <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

In contrast, a [[random_variables_overview | random variable]] (typically denoted by capital letters like `X` or `Y`) can take on many different values, each with its own probability <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. The focus with a [[random_variables_overview | random variable]] is on the [[random_variables_and_probabilities | probability]] of it equaling a certain value, being less than/greater than something, or possessing a certain property <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## Mapping Random Processes to Numbers

A [[random_variables_overview | random variable]] essentially quantifies the results of an [[experimentation_in_probability | experiment]] or random process <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

### [[examples_of_random_variables | Examples of Random Variables]]

*   **Coin Flip** <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>:
    *   Define a [[random_variables_overview | random variable]] `X` <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
    *   If a fair coin rolls heads, `X` = 1 <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
    *   If a fair coin rolls tails, `X` = 0 <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
    *   While 1 and 0 are typical values, `X` could be defined with other numbers, such as 100 for heads and 703 for tails, and still be a legitimate [[random_variables_overview | random variable]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This process maps the outcomes ("heads" or "tails") from the [[sample_space_in_probability | random process]] of flipping a coin to numerical values <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

*   **Sum of Dice Rolls** <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>:
    *   Define a [[random_variables_overview | random variable]] `Y` as the sum of the upward faces after rolling seven dice <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
    *   This quantifies the outcome of the random process of rolling the dice and summing their results <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## [[uses_of_random_variables_in_probability | Usefulness of Random Variables]]

Defining [[random_variables_overview | random variables]] allows for more mathematical operations and notation on the outcomes of random processes <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

### Simplified Notation
Using [[random_variables_overview | random variables]] cleans up probability statements <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

*   Instead of writing "the probability that the sum of the upward faces after rolling seven dice is less than or equal to 30" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, one can simply write `P(Y ≤ 30)` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   Similarly, "the probability that Y is even" replaces a longer description <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

The discussion on [[discrete_vs_continuous_random_variables | types of random variables]] will continue in subsequent videos <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.