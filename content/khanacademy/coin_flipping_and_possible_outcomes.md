---
title: Coin flipping and possible outcomes
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

A [[Random variables | random variable]] `x` can be defined as the number of heads obtained from [[Probability of flipping a coin | flipping a fair coin]] five times <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This [[Random variables | random variable]] functions by taking particular outcomes of a random process and [[Mapping outcomes of random processes | converting them into numerical values]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. For this specific scenario, the possible values for `x` are 0, 1, 2, 3, 4, or 5 heads <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

The objective is to determine the [[calculating_probabilities_for_specific_outcomes | probability]] that this [[Random variables | random variable]] `x` takes on each of these possible values <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Total Possible Outcomes

First, it's essential to identify the total number of [[Sample space and possible outcomes | possible outcomes]] when [[Probability of flipping a coin | flipping a fair coin]] five times <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Each flip has two possibilities (Heads or Tails) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Since there are five flips, the total number of equally likely outcomes is calculated as 2 multiplied by itself five times:
2 * 2 * 2 * 2 * 2 = 2^5 = 32 <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
Thus, there are [[Sample space and possible outcomes | 32 equally likely possibilities]] for five coin flips <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

Examples of such outcomes include:
*   Tails, Heads, Tails, Heads, Tails (THTHT) <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Heads, Heads, Heads, Tails, Tails (HHHTT) <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>

## Calculating Probabilities for `x`

To find the probability for each value of `x`, we need to determine how many of the 32 equally likely outcomes result in that specific number of heads <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. This involves [[Quantifying outcomes for probability | quantifying the outcomes]] <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. We can use combinatorics, specifically the "n choose k" formula (nCk), where `n` is the total number of flips (5) and `k` is the number of heads we are choosing <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

The probability for a given `x` value is (Number of ways to get `x` heads) / (Total number of outcomes = 32).

### Probability that x = 0 (No Heads)

The [[calculating_probabilities_for_specific_outcomes | probability]] that `x` equals 0 means getting no heads out of five flips <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. This can only happen in one way: all five flips are tails (TTTTT) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Combinatorics:** 5 choose 0 (⁵C₀)
    *   ⁵C₀ = 5! / (0! * (5-0)!) = 5! / (1 * 5!) = 1 <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>
*   **Probability:** 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

### Probability that x = 1 (One Head)

The [[calculating_probabilities_for_specific_outcomes | probability]] that `x` equals 1 means getting exactly one head <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. There are five different positions the single head could occur (HTTTT, THTTT, TTHTT, TTTHT, TTTTH) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   **Combinatorics:** 5 choose 1 (⁵C₁)
    *   ⁵C₁ = 5! / (1! * (5-1)!) = 5! / (1 * 4!) = 5 <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>
*   **Probability:** 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>

### Probability that x = 2 (Two Heads)

The [[calculating_probabilities_for_specific_outcomes | probability]] that `x` equals 2 means getting exactly two heads <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **Combinatorics:** 5 choose 2 (⁵C₂)
    *   ⁵C₂ = 5! / (2! * (5-2)!) = 5! / (2! * 3!) = (5 * 4 * 3 * 2 * 1) / ((2 * 1) * (3 * 2 * 1)) = 120 / (2 * 6) = 120 / 12 = 10 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>
*   **Probability:** 10/32 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

### Probability that x = 3 (Three Heads)

The [[calculating_probabilities_for_specific_outcomes | probability]] that `x` equals 3 means getting exactly three heads <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Combinatorics:** 5 choose 3 (⁵C₃)
    *   ⁵C₃ = 5! / (3! * (5-3)!) = 5! / (3! * 2!) = (5 * 4 * 3 * 2 * 1) / ((3 * 2 * 1) * (2 * 1)) = 120 / (6 * 2) = 120 / 12 = 10 <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>
*   **Probability:** 10/32 <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>

### Probability that x = 4 (Four Heads)

The [[calculating_probabilities_for_specific_outcomes | probability]] that `x` equals 4 means getting exactly four heads <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Combinatorics:** 5 choose 4 (⁵C₄)
    *   ⁵C₄ = 5! / (4! * (5-4)!) = 5! / (4! * 1!) = (5 * 4 * 3 * 2 * 1) / ((4 * 3 * 2 * 1) * 1) = 5 <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>
*   **Probability:** 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>

### Probability that x = 5 (Five Heads)

The [[calculating_probabilities_for_specific_outcomes | probability]] that `x` equals 5 means getting exactly five heads <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. This can only happen in one way: all five flips are heads (HHHHH) <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
*   **Combinatorics:** 5 choose 5 (⁵C₅)
    *   ⁵C₅ = 5! / (5! * (5-5)!) = 5! / (5! * 0!) = 1 <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>
*   **Probability:** 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

### Summary of Probabilities

| Value of `x` (Heads) | Number of Ways (Combinations) | Probability |
| :------------------- | :---------------------------- | :---------- |
| 0                    | 1                             | 1/32        |
| 1                    | 5                             | 5/32        |
| 2                    | 10                            | 10/32       |
| 3                    | 10                            | 10/32       |
| 4                    | 5                             | 5/32        |
| 5                    | 1                             | 1/32        |

Notice the symmetry in the probabilities: 1, 5, 10, 10, 5, 1 <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. For example, the probability of getting five heads (all heads) is the same as getting zero tails, which is symmetrical to the probability of getting zero heads (all tails) <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.

This exercise serves as a foundation for understanding the binomial distribution <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. The next step would be to graphically represent this probability distribution <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.