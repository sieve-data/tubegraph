---
title: Understanding random variables
videoId: 3v9w79NhsfI
---

From: [[khanacademy]] <br/> 

[[random_variables_overview | Random variables]] can initially be confusing because they might be mistaken for traditional variables encountered in algebra classes <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. However, [[random_variables | random variables]] are fundamentally different <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Definition
A [[definition_of_a_random_variable | random variable]] is a way to map outcomes of random processes to numbers <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This means quantifying the outcomes of an unpredictable process <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. [[random_variables | Random variables]] are typically denoted by capital letters <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

Examples of random processes include:
*   Flipping a coin <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>
*   Rolling dice <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>
*   Measuring tomorrow's rainfall <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>

## [[examples_of_random_variables | Examples of Random Variables]]

### Coin Flip
Consider a fair coin flip as the random process. A [[random_variables | random variable]], `capital X`, could be defined as:
*   `X = 1` if the coin lands on heads <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
*   `X = 0` if the coin lands on tails <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>

While this is a typical definition, `X` could be defined with any numerical values (e.g., 100 for heads, 703 for tails) and still be a legitimate [[random_variables | random variable]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The key is mapping and quantifying the random outcomes <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Sum of Dice Rolls
Another example is defining a [[random_variables | random variable]], `capital Y`, as the sum of the upward faces after rolling seven dice <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This quantifies the outcome of the random process of rolling multiple dice <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Why Use Random Variables?
The primary utility of defining [[random_variables | random variables]] is to quantify outcomes, which allows for more mathematical analysis and cleaner notation in probability <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.

For instance, instead of writing "the probability that the sum of the upward faces after rolling seven dice is less than or equal to 30" <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>, one can simply write `P(Y ≤ 30)` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. Similarly, "the probability that Y is even" is a concise way to refer to the probability that the sum of the dice rolls is an even number <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

## [[differences_between_random_and_traditional_variables | Differences from Traditional Variables]]
[[random_variables | Random variables]] differ significantly from traditional variables found in algebra (e.g., `x` in `x + 5 = 6` or `y` in `y = x + 7`), which are usually denoted by lowercase letters <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

With traditional variables:
*   You can assign specific values to them <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   You can solve for them (e.g., `x = 1` in `x + 5 = 6`) <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.

In contrast, a [[random_variables | random variable]]:
*   Can take on many different values <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   Each possible value has a specific probability associated with it <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   It makes more sense to discuss the probability of a [[random_variables | random variable]] equaling, being less than, or having a certain property, rather than assigning it a fixed value <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

The next discussion will delve into [[discrete_vs_continuous_random_variables | different types of random variables]] <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.