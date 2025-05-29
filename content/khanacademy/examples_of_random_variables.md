---
title: Examples of random variables
videoId: 3v9w79NhsfI
---

From: [[khanacademy]] <br/> 
[[concept_of_random_variables | Random variables]] are a fundamental concept in probability that help quantify outcomes of random processes <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. They serve as a method to map the results of uncertain events to numerical values <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>, essentially "quantifying the outcomes" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

### Understanding Random Variables
Unlike traditional [[differences_between_random_variables_and_algebraic_variables | algebraic variables]] (e.g., 'x' in `x + 5 = 6`) that can be solved for or assigned a specific value <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>, a [[concept_of_random_variables | random variable]] can take on many different values, each with its own probability <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. It makes more sense to discuss the probability of a [[concept_of_random_variables | random variable]] equalling a certain value, or being less than/greater than something <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. They are typically denoted by capital letters <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Examples of Random Variables
Random processes include activities like flipping a coin, rolling dice, or measuring rainfall <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. [[concept_of_random_variables | Random variables]] provide a numerical representation for the [[events_and_outcomes_in_probability | outcomes]] of these processes <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

#### Coin Flip Example
A common example is defining a [[concept_of_random_variables | random variable]] for a coin flip <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>:
*   Let capital `X` be a [[concept_of_random_variables | random variable]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   `X` = 1 if the coin lands on heads <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   `X` = 0 if the coin lands on tails <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

While this is a typical way to define it, any numerical values could be used (e.g., `X` = 100 for heads, `X` = 703 for tails) and it would still be a legitimate [[concept_of_random_variables | random variable]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The key is mapping the [[events_and_outcomes_in_probability | outcomes]] of the random process to numbers <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

#### Sum of Dice Rolls Example
Another example involves rolling multiple dice <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>:
*   Let capital `Y` be a [[concept_of_random_variables | random variable]] <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   `Y` = the sum of the upward faces after rolling 7 dice <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

This [[concept_of_random_variables | random variable]] `Y` quantifies the outcome of the random process of rolling 7 dice <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Usefulness of Random Variables
Defining [[random_variables_and_probabilities | random variables]] is useful because once outcomes are quantified, more mathematical operations can be performed on them <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. It also allows for cleaner and more concise mathematical notation <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

For instance, instead of writing "the probability that the sum of the upward faces after rolling seven dice is less than or equal to 30" <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>, one can simply write:
*   `P(Y ≤ 30)` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>

Similarly, to ask for the probability that the sum is even, it can be written as:
*   `P(Y is even)` <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>

This streamlined notation makes working with probabilities much more efficient <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.