---
title: Calculating Probability with Dice
videoId: uzkc-qNVoOk
---

From: [[khanacademy]] <br/> 

[[introduction_to_probability | Probability]] provides a way to quantify the likelihood of an event that is fundamentally random <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. While the exact outcome of a single event cannot be predicted, probability helps describe the chances of different outcomes <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Core Concept of Probability

The most common way to introduce probability is by comparing the number of favorable outcomes to the total number of equally likely outcomes <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>:

$$P(\text{Event}) = \frac{\text{Number of equally likely possibilities that meet conditions}}{\text{Total number of equally likely possibilities}}$$

### Conceptualizing Probability Through Experimentation

Another way to think about probability is by imagining an [[experimentation_in_probability | experiment]] being run many, many times <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. For example, if an experiment is repeated a million or even an infinite number of times, the probability of an event represents the percentage of those trials that would result in the desired outcome <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. The more trials conducted, the closer the observed percentage of the event will be to its theoretical probability <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

## Probability with a Fair Coin

To illustrate basic probability, consider flipping a [[understanding_fair_coins_and_probability | fair coin]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. A fair coin has an equal chance of landing on one side or the other, meaning its weight is distributed evenly <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

The possible outcomes for a single coin flip are heads or tails <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. If we assume the coin cannot land on its edge <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>, there are two equally likely possibilities.

To find the probability of getting heads <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>:
*   **Total equally likely possibilities**: 2 (Heads, Tails) <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>
*   **Possibilities meeting conditions (Heads)**: 1 <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>

$$P(\text{Heads}) = \frac{1}{2} = 50\%$$ <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>

## Calculating Probability with Dice

A common example when learning [[probability_calculation | probability calculation]] involves rolling a die <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Assuming a fair die, there are six equally likely possibilities when rolled: 1, 2, 3, 4, 5, or 6 <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

### Probability of Rolling a Specific Number

What is the probability of getting a 1 when rolling a fair die <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>?
*   **Total equally likely possibilities**: 6 <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>
*   **Possibilities meeting conditions (1)**: 1 <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>

$$P(\text{Rolling a 1}) = \frac{1}{6}$$ <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>

### Probability of Rolling Multiple Specific Numbers (OR)

What is the probability of rolling a 1 or a 6 <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>?
*   **Total equally likely possibilities**: 6 <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>
*   **Possibilities meeting conditions (1 or 6)**: 2 (the outcome can be a 1 or a 6) <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>

$$P(\text{Rolling a 1 or a 6}) = \frac{2}{6} = \frac{1}{3}$$ <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>

### Probability of Mutually Exclusive Events (AND)

Consider the probability of rolling a 2 and a 3 on a single roll <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. On one roll of a die, it is impossible to get both a 2 and a 3 simultaneously <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. These are "mutually exclusive events" <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **Total equally likely possibilities**: 6 <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>
*   **Possibilities meeting conditions (2 AND 3)**: 0 <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>

$$P(\text{Rolling a 2 and a 3}) = \frac{0}{6} = 0$$ <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>

### Probability of Rolling an Even Number

What is the probability of getting an even number when rolling a die <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>?
*   **Total equally likely possibilities**: 6 <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>
*   **Possibilities meeting conditions (even numbers)**: 3 (2, 4, 6) <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>

$$P(\text{Rolling an even number}) = \frac{3}{6} = \frac{1}{2}$$ <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>