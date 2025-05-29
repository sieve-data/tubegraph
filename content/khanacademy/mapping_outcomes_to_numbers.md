---
title: Mapping outcomes to numbers
videoId: 3v9w79NhsfI
---

From: [[khanacademy]] <br/> 

Random variables provide a method to map [[events_and_outcomes_in_probability | outcomes]] of random processes to numerical values <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This process involves quantifying the [[events_and_outcomes_in_probability | outcomes]] of unpredictable events, such as flipping a coin, rolling dice, or measuring rainfall <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Distinction from Traditional Variables

Unlike traditional algebraic variables (e.g., `x` in `x + 5 = 6`), which can be solved for or assigned specific values <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>, random variables do not have a single, fixed value <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. Instead, a random variable can take on many different numerical [[events_and_outcomes_in_probability | values]], each with a specific probability <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. It makes more sense to discuss the probability of a random variable equaling, being less than, or being greater than a certain value <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.

## Purpose and Usefulness

The primary utility of random variables is to enable mathematical operations and notation on probabilistic [[events_and_outcomes_in_probability | outcomes]] <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. By quantifying [[events_and_outcomes_in_probability | outcomes]], it becomes possible to apply mathematical concepts and express probabilities more concisely <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.

For instance, instead of writing "the probability that the sum of the upward faces after rolling seven dice is less than or equal to 30" <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, one can define a random variable, say `Y`, for that sum and simply write `P(Y <= 30)` <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This provides a cleaner and more efficient notation <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Notation

Random variables are typically denoted by capital letters <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Examples

### Coin Flip

A common example is defining a random variable `X` for the [[events_and_outcomes_in_probability | outcome]] of a coin flip <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>:
- `X = 1` if the coin lands heads <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
- `X = 0` if the coin lands tails <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>

While `1` and `0` are typical assignments for convenience, any numerical values could be used (e.g., `X = 100` for heads and `X = 703` for tails would still constitute a legitimate random variable) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. The crucial aspect is that a numerical value is assigned to each possible [[events_and_outcomes_in_probability | outcome]] <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

### Sum of Dice Rolls

Another example involves defining a random variable `Y` as the sum of the upward faces after rolling seven dice <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Here, the random process is rolling the dice and observing the faces, and the random variable quantifies the aggregate result of that process <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.