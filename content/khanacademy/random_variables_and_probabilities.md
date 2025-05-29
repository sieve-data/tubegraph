---
title: Random variables and probabilities
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

This article explores the concept of [[concept_of_random_variables | random variables]] and how to calculate probabilities associated with their possible values, using the example of flipping a fair coin five times. <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

## Defining the Random Variable

A [[concept_of_random_variables | random variable]] X is defined as the number of heads obtained from flipping a fair coin five times. <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>, <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a> Like all [[random_variables_overview | random variables]], X takes specific [[events_and_outcomes_in_probability | outcomes]] from an [[experimentation_in_probability | experiment]] and converts them into numbers. <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>, <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

In this scenario, the [[concept_of_random_variables | random variable]] X can take on the following values: 0, 1, 2, 3, 4, or 5. <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>, <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> The objective is to determine the [[probability_distribution_and_density_functions | probability]] that X equals each of these possible values. <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>

## Total Possible Outcomes

To calculate these [[probability_distribution_and_density_functions | probabilities]], first determine the total number of possible [[events_and_outcomes_in_probability | outcomes]] when flipping a fair coin five times. <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>, <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>

For each flip, there are two possibilities (Heads or Tails). Since there are five flips, the total number of equally likely [[events_and_outcomes_in_probability | outcomes]] is calculated as: <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>, <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>, <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>, <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>

$$2 \times 2 \times 2 \times 2 \times 2 = 2^5 = 32$$ <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>

There are 32 equally likely possible [[events_and_outcomes_in_probability | outcomes]] from five coin flips. <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>

## Calculating Probabilities for X

For each value the [[concept_of_random_variables | random variable]] X can take, the [[probability_distribution_and_density_functions | probability]] is determined by finding how many of the 32 equally likely [[events_and_outcomes_in_probability | outcomes]] result in that specific value. <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>, <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>

### Probability X = 0 (Zero Heads)

The [[probability]] that X equals zero (no heads) means getting five tails. There is only one such [[events_and_outcomes_in_probability | outcome]]: TTTTT. <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>, <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>, <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>

This can be expressed using combinatorics as "5 choose 0" (number of ways to choose 0 heads from 5 flips): <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>, <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>, <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>

$$ P(X=0) = \frac{\binom{5}{0}}{32} $$ <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

Calculation of $\binom{5}{0}$: <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>

$$ \binom{5}{0} = \frac{5!}{0!(5-0)!} = \frac{5!}{1 \cdot 5!} = 1 $$ <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>, <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>, <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>, <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>, <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>

Therefore:
$$ P(X=0) = \frac{1}{32} $$ <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

### Probability X = 1 (One Head)

To get one head, there are five possible positions for that single head (e.g., HTTTT, THTTT, etc.). <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>, <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>

Using combinatorics, this is "5 choose 1": <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>

$$ P(X=1) = \frac{\binom{5}{1}}{32} $$ <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>

Calculation of $\binom{5}{1}$: <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>

$$ \binom{5}{1} = \frac{5!}{1!(5-1)!} = \frac{5!}{1 \cdot 4!} = 5 $$ <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>, <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>, <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>, <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>

Therefore:
$$ P(X=1) = \frac{5}{32} $$ <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>

### Probability X = 2 (Two Heads)

For two heads, we determine the number of ways to choose 2 positions for heads out of 5 flips, "5 choose 2": <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>, <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>, <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>

$$ P(X=2) = \frac{\binom{5}{2}}{32} $$ <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>, <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>

Calculation of $\binom{5}{2}$: <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>

$$ \binom{5}{2} = \frac{5!}{2!(5-2)!} = \frac{5!}{2!3!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{(2 \times 1)(3 \times 2 \times 1)} = \frac{120}{2 \times 6} = \frac{120}{12} = 10 $$ <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>, <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>, <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>, <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>, <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>, <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>, <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>, <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>, <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>, <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>

Therefore:
$$ P(X=2) = \frac{10}{32} $$ <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

### Probability X = 3 (Three Heads)

For three heads, we use "5 choose 3": <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>, <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>, <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>

$$ P(X=3) = \frac{\binom{5}{3}}{32} $$ <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>

Calculation of $\binom{5}{3}$: <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>

$$ \binom{5}{3} = \frac{5!}{3!(5-3)!} = \frac{5!}{3!2!} $$ <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>, <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>, <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>, <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>, <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>

This is the same calculation as $\binom{5}{2}$, resulting in 10. <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>, <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>, <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>

Therefore:
$$ P(X=3) = \frac{10}{32} $$ <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>

### Probability X = 4 (Four Heads)

For four heads, we use "5 choose 4": <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>, <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>

$$ P(X=4) = \frac{\binom{5}{4}}{32} $$ <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>

Calculation of $\binom{5}{4}$: <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>

$$ \binom{5}{4} = \frac{5!}{4!(5-4)!} = \frac{5!}{4!1!} = 5 $$ <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>, <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>, <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>, <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>, <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>

Therefore:
$$ P(X=4) = \frac{5}{32} $$ <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>

### Probability X = 5 (Five Heads)

For five heads, this means all flips are heads. There is only one such [[events_and_outcomes_in_probability | outcome]]: HHHHH. <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>, <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>, <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>, <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>

Using combinatorics, this is "5 choose 5": <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>, <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>

$$ P(X=5) = \frac{\binom{5}{5}}{32} $$ <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>

Calculation of $\binom{5}{5}$: <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>, <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>

$$ \binom{5}{5} = \frac{5!}{5!(5-5)!} = \frac{5!}{5!0!} = \frac{5!}{5! \cdot 1} = 1 $$ <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>, <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>, <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>, <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>, <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>, <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

Therefore:
$$ P(X=5) = \frac{1}{32} $$ <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

## Summary of Probabilities and Symmetry

The calculated [[probability_distribution_and_density_functions | probabilities]] for the [[concept_of_random_variables | random variable]] X are:

*   **P(X=0)** = 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
*   **P(X=1)** = 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>
*   **P(X=2)** = 10/32 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>
*   **P(X=3)** = 10/32 <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>
*   **P(X=4)** = 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>
*   **P(X=5)** = 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

Notice the symmetry in the probabilities: 1, 5, 10, 10, 5, 1. <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>, <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>, <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>, <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a> This makes sense because, for example, the [[probability]] of getting zero heads (all tails) is the same as getting zero tails (all heads), and similarly for one head/one tail, and so on. <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>, <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>, <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>, <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>

> [!NOTE] Further Exploration
> This process lays the groundwork for understanding the binomial distribution, which describes the [[probability]] of obtaining a certain number of successes (like heads) in a fixed number of trials (coin flips). <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>, <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a> The graphical representation of these probabilities forms the [[probability_distribution_and_density_functions | probability distribution]] for this [[concept_of_random_variables | random variable]]. <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>, <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>