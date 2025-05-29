---
title: Applications of Convolutions in Probability
videoId: KuXjwB4LzSA
---

From: [[3blue1brown]] <br/> 

[[introduction_to_convolutions | Convolutions]] are a fundamental concept in the theory of probability, appearing as a core construct <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. They provide a natural way to combine lists of numbers or functions to produce a new result <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Combining Probability Distributions

One common application of convolutions is in adding up probability distributions <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. This is particularly evident in scenarios involving the sum of independent random variables.

### Discrete Case: Rolling Dice

A simple and relatable example is calculating the chances of seeing various sums when rolling a pair of dice <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

#### Fair Dice
When rolling two fair dice, each die has six possible outcomes <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. This leads to a total of 36 distinct possible pairs of outcomes <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. To find the probability of a given sum, one can count how many pairs result in that sum <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

Visually, if all pairs are arranged in a grid, pairs with a constant sum align along diagonals <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. By counting the number of outcomes on each diagonal, the likelihood of a particular sum can be determined <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

Another visualization involves picturing the possibilities for each die in a row and then flipping the second row <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This alignment method reveals all distinct pairs that add up to a specific sum <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>:
*   Sliding the flipped row fully to the right aligns the unique pair for a sum of 2 (snake eyes) <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   Sliding it one unit further aligns the two different pairs that add up to 3 <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

#### Non-Uniform (Loaded) Dice
The concept becomes more complex and directly relates to convolutions when dealing with dice that do not have an equal chance for each face to come up <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. For example, if a blue die and a red die each have their own unique probability distributions for their faces <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>:
*   To find the probability of seeing a sum of 2, one multiplies the probability of the blue die being 1 by the probability of the red die being 1 <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   For a sum of 3, one looks at the two distinct pairs (1+2, 2+1), multiplies their corresponding probabilities, and then adds those products together <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   For a sum of 4, this involves multiplying together three different pairs of possibilities and summing them <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

This process of taking two different arrays of numbers (e.g., probability distributions `a` and `b`), flipping the second one around, lining them up at various offsets, performing pairwise products, and summing them up, is a fundamental way to understand what a convolution is <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This operation produces a new sequence of probabilities for all possible sums (e.g., 2 to 12 for two dice) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

Alternatively, a convolution can be visualized by creating a table of all pairwise products and then adding up along the diagonals <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This yields the same result as the sliding window method <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.

The mathematical notation for the convolution of two sequences `a` and `b` (denoted `a * b`) results in a new list where the nth element is the sum of products `a_i * b_j` for all pairs of indices `i` and `j` such that `i + j = n` <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. For instance, if `n` is 6, the pairs considered would be (1,5), (2,4), (3,3), (4,2), and (5,1) <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>. The visual understanding of the process is often more important than the formulaic notation <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

## Connection to Normal Distributions

While the continuous case of convolutions is discussed in detail elsewhere, it is worth noting that they provide insight into why normal distributions play such a significant role in probability <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>. Convolutions help explain why the bell curve is such a natural shape for a function in this context <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.