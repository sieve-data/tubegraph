---
title: Discrete vs continuous random variables
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

Previously, the concept of a [[random_variables_overview | random variable]] was introduced, followed by an overview of its two main types: discrete and continuous <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Discrete Random Variables
[[Discrete random variables | Discrete random variables]] can take on a finite number of values <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. While they often tend to be integers, they are not always required to be <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The key characteristic is that a [[Discrete random variables | discrete random variable]] cannot have an infinite number of values <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Continuous Random Variables
[[Continuous random variables | Continuous random variables]], in contrast, can take on an infinite number of values <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. [[Examples of random variables | Random variables]] are typically represented by capital letters, such as `Y` <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Example: Amount of Rain
Consider a [[Continuous random variables | continuous random variable]], `Y`, representing the exact amount of rain tomorrow <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. The amount of rain can be any value within a range, not just whole numbers.

### Probability for Continuous Random Variables
When dealing with [[Continuous random variables | continuous random variables]], a key distinction arises in calculating probabilities.

#### Probability of an Exact Value
The probability that a [[Continuous random variables | continuous random variable]] `Y` is exactly equal to a specific value (e.g., exactly 2 inches of rain) is essentially zero <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

Consider the precision required for "exactly 2 inches": it means not 2.01, not 1.99, not even 2.000001 or 1.99999 inches <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. The odds of any measurement being precisely exact to an infinite decimal point is 0 <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

This concept can be understood by analogy: asking for the area under a curve at just one specific line or, more simply, asking for the area of a line <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>. A line, as defined, has no width, and therefore no area <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>. Similarly, when a [[random_variables_overview | random variable]] can take on an infinite number of values, the probability of hitting one exact value is 0 <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>.

#### Probability Over an Interval
For [[Continuous random variables | continuous random variables]], probabilities are defined over intervals <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. For example, to find the probability that `Y` is almost 2 (e.g., between 1.9 and 2.1 inches), an interval is used <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

To find the probability of a [[Continuous random variables | continuous random variable]] falling within a specific range, the **area under its probability density function (PDF)** for that interval is calculated <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. Those familiar with calculus would recognize this as the definite integral of the PDF over the given interval <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. For a function `f(x)`, the probability from 1.9 to 2.1 would be ∫(from 1.9 to 2.1) f(x) dx <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

#### Total Probability
For any probability distribution, the sum of all possible probabilities must equal 1 (or 100%) <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

*   **For [[Continuous random variables | continuous random variables]]**: The entire area under the probability density function curve must be equal to 1 <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. If the function is `f(x)` and the domain is from 0 to infinity, then ∫(from 0 to ∞) f(x) dx = 1 <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **For [[Discrete random variables | discrete random variables]]**: The sum of all individual probabilities for each possible outcome must equal 1 <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. For example, with a coin flip where heads (1) and tails (0) each have a 0.5 probability, 0.5 + 0.5 = 1 <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>. It's not possible to have a 60% chance for heads and a 60% chance for tails, as that would sum to 120%, which is illogical <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

The next discussion will introduce the concept of an expected value <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.