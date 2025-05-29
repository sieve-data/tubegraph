---
title: Discrete vs continuous random variables
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

In probability, [[random_variables | random variables]] are used to describe the outcomes of random phenomena <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. There are two primary types of [[random_variables | random variables]]: [[discrete_random_variables | discrete]] and [[continuous_random_variables | continuous]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## [[discrete_random_variables | Discrete Random Variables]]

A [[discrete_random_variables | discrete random variable]] is one that can only take on a finite number of specific values <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. These values are often integers, but not exclusively <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. The key characteristic is that you cannot have an infinite number of possible values for a [[discrete_random_variables | discrete random variable]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

For a [[discrete_random_variables | discrete probability distribution]], the sum of all individual probabilities for each possible outcome must equal 1 (or 100%) <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>, <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.

> For example, if a [[random_variables | random variable]] `X` represents the outcome of a coin flip, `X` could be `1` for heads and `0` for tails <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. If the probability of heads is 0.5, the probability of tails must also be 0.5, so they add up to 1 <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. It's impossible to have a 60% chance of heads and a 60% chance of tails, as that would total 120%, which makes no sense <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.

## [[continuous_random_variables | Continuous Random Variables]]

In contrast, a [[continuous_random_variables | continuous random variable]] can take on an infinite number of values within a given range or interval <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. [[Random_variables | Random variables]] are typically denoted by capital letters, such as `Y` <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

An [[examples_of_continuous_variables | example of a continuous random variable]] is the exact amount of rain that falls tomorrow <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This value can be 2 inches, 2.01 inches, 1.99999 inches, or any value in between <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

### Probability of an Exact Value

For a [[continuous_random_variables | continuous random variable]], the probability of it taking on an *exact* value is essentially zero <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>, <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This is because there are an infinite number of possible values, making the chance of landing on one specific, infinitely precise point negligible <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

> For instance, the probability of exactly 2 inches of rain (not 2.000001 or 1.999999 inches) is 0 <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Our measurement tools aren't precise enough to even determine an exact value <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. This can be understood by analogy: a line, despite having height, has no width, and therefore no area <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Similarly, a single point on a continuous distribution has no "area," hence no probability <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>, <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### Probability Density Function (PDF)

The probability of a [[continuous_random_variables | continuous random variable]] falling within a range is represented by its probability density function (PDF) <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Instead of discrete bars, a PDF is a continuous curve <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

To find the probability that a [[continuous_random_variables | continuous random variable]] falls within a certain interval (e.g., between 1.9 and 2.1 inches of rain), you calculate the area under the curve of the PDF for that interval <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>, <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. This calculation is performed using a definite integral in calculus <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>, <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

For any valid probability density function, the total area under the entire curve must equal 1 <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>, <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. This signifies that the probability of all possible outcomes combined is 100% <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
