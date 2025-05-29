---
title: Discrete vs continuous random variables
videoId: Fvi9A_tEmXQ
---

From: [[khanacademy]] <br/> 

In probability and statistics, a [[random_variables | random variable]] is a variable whose value is the outcome of a random phenomenon <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. [[distinction_between_discrete_and_continuous_random_variables | Random variables]] are categorized into two main types: [[discrete_random_variables | discrete]] and [[continuous_random_variables | continuous]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

## Discrete Random Variables

A [[discrete_random_variables | discrete random variable]] is one that can take on a finite number of values <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This means there isn't an infinite number of possible values for a discrete random variable <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. While they tend to be integers, they are not exclusively so <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

For a [[discrete_random_variables | discrete random variable]], the sum of all possible probabilities for each outcome must be equal to 1 <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a> <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. For example, in a coin toss where X=1 for heads and X=0 for tails, if the probability of heads is 0.6, the probability of tails must be 0.4, ensuring they add up to 1 <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a> <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

## Continuous Random Variables

A [[continuous_random_variables | continuous random variable]] can take on an infinite number of values <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This means it can take on any value within a given interval <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. [[continuous_random_variables | Continuous random variables]] are typically represented by capital letters, such as Y <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a> <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Example: Amount of Rain

An example of a [[continuous_random_variables | continuous random variable]] is the exact amount of rain that falls tomorrow <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a> <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

### Probability of an Exact Value

For a [[continuous_random_variables | continuous random variable]], the probability of it taking on an *exactly* specific value is considered 0 <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a> <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. For instance, the probability of having *exactly* 2 inches of rain (not 2.000001 or 1.99999 inches) is zero <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a> <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This is because any measurement has infinite decimal points, making the chance of an exact match infinitesimally small <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

### Probability of a Range of Values (Area Under the Curve)

Instead, probabilities for [[continuous_random_variables | continuous random variables]] are determined over an interval or range of values <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>. This probability is represented by the area under its **probability density function (PDF)** curve over that interval <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a> <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

For those familiar with calculus, this area is calculated using the definite integral of the PDF over the desired range <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a> <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Total Area Under the Curve

Similar to discrete distributions, the total probability of all possible events for a [[continuous_random_variables | continuous random variable]] must equal 1 (or 100%) <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. Therefore, the entire area under the probability density function curve from its minimum to maximum possible value must be equal to 1 <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a> <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. For an amount of rain example, this would be the integral of the function from 0 to infinity <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.