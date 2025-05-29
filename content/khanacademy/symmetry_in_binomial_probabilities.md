---
title: Symmetry in Binomial Probabilities
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 
The probability distribution for a random variable that represents the number of heads in a series of coin flips exhibits a noticeable symmetry. This concept is a build-up for understanding the [[binomial_distribution | Binomial Distribution]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Defining the Random Variable

Consider a random variable `x` defined as the number of heads obtained from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This random variable can take on integer values from zero (no heads) to five (all heads) <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Total Possible Outcomes

When flipping a coin five times, there are two possibilities for each flip (heads or tails) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Therefore, the total number of [[equally_likely_possibilities_in_probability | equally likely outcomes]] from five flips is 2 * 2 * 2 * 2 * 2, or 2^5, which equals 32 <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a><a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Calculating Probabilities for Each Outcome

To find the probability for each value of `x`, we determine how many of the 32 [[equally_likely_possibilities_in_probability | equally likely outcomes]] result in that specific number of heads. This can be calculated using [[combinatorics_and_factorials | combinatorics]], specifically the "n choose k" formula (C(n, k)), which is the number of ways to choose 'k' successes from 'n' trials. In this case, 'n' is the number of flips (5) and 'k' is the number of heads.

*   **P(x = 0 heads)**:
    *   There is only one way to get zero heads (all tails) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   Using [[combinatorics_and_factorials | combinatorics]]: 5 choose 0 (C(5,0)) = 1 <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a><a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    *   Probability: 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

*   **P(x = 1 head)**:
    *   There are five possible ways to get exactly one head (e.g., H T T T T, T H T T T, etc.) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   Using [[combinatorics_and_factorials | combinatorics]]: 5 choose 1 (C(5,1)) = 5 <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a><a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
    *   Probability: 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

*   **P(x = 2 heads)**:
    *   Using [[combinatorics_and_factorials | combinatorics]]: 5 choose 2 (C(5,2)) = 10 <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a><a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
    *   Probability: 10/32 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

*   **P(x = 3 heads)**:
    *   Using [[combinatorics_and_factorials | combinatorics]]: 5 choose 3 (C(5,3)) = 10 <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a><a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. (Note: C(n, k) = C(n, n-k), so C(5,3) = C(5,2) = 10)
    *   Probability: 10/32 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

*   **P(x = 4 heads)**:
    *   Using [[combinatorics_and_factorials | combinatorics]]: 5 choose 4 (C(5,4)) = 5 <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a><a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. (Note: C(5,4) = C(5,1) = 5)
    *   Probability: 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

*   **P(x = 5 heads)**:
    *   There is only one way to get five heads (all heads) <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
    *   Using [[combinatorics_and_factorials | combinatorics]]: 5 choose 5 (C(5,5)) = 1 <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a><a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. (Note: C(5,5) = C(5,0) = 1)
    *   Probability: 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### Observing the Symmetry

When listing the probabilities, a clear symmetry emerges:
*   P(x=0) = 1/32
*   P(x=1) = 5/32
*   P(x=2) = 10/32
*   P(x=3) = 10/32
*   P(x=4) = 5/32
*   P(x=5) = 1/32

This symmetry is evident in the coefficients: 1, 5, 10, 10, 5, 1 <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a><a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

#### Explanation of Symmetry
The symmetry arises because the probability of getting a certain number of heads is the same as the probability of getting that same number of tails. For example:
*   Getting 5 heads means getting 0 tails <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>. The probability of 5 heads (all heads) is the same as the probability of 0 tails (all heads) <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>.
*   Getting 4 heads means getting 1 tail <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>. The number of ways to get 4 heads (C(5,4)) is the same as the number of ways to get 1 tail (C(5,1)), which is 5 <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>.

This relationship, where C(n, k) = C(n, n-k), is fundamental to [[patterns_in_binomial_expansions | patterns in binomial expansions]] and is directly observed in these probabilities.