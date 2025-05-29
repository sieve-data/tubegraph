---
title: Combinatorics and Factorials
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

This article explores the application of combinatorics and factorials in determining probabilities, specifically using the example of flipping a fair coin five times and defining a random variable 'x' as the number of heads obtained <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This serves as a foundational buildup to understanding the binomial distribution <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Total Possible Outcomes

When flipping a fair coin five times, there are two possibilities for each flip (heads or tails) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The total number of equally likely outcomes is calculated by multiplying the possibilities for each flip: 2 x 2 x 2 x 2 x 2, which is 2 to the power of 5 <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

```
Total Possible Outcomes = 2^5 = 32
```
There are 32 equally likely outcomes from flipping a coin five times <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

## Calculating Probabilities Using Combinations

To find the probability of the random variable 'x' (number of heads) taking on a specific value, we determine how many of these 32 equally likely outcomes result in that value <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. This involves using combinations, specifically "n choose k," where 'n' is the total number of flips and 'k' is the number of heads we are looking for <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

The formula for "n choose k" (often written as C(n, k) or (n k)) is:
$$ \binom{n}{k} = \frac{n!}{k!(n-k)!} $$

Where 'n!' (n factorial) means the product of all positive integers less than or equal to n (e.g., 5! = 5 × 4 × 3 × 2 × 1) <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. By definition, 0! (zero factorial) is equal to 1 <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.

### Probability of x = 0 Heads

The probability of getting zero heads (all tails) in five flips is:

*   **Combinations**: 5 choose 0, representing choosing 0 heads out of 5 flips <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
    *   $$ \binom{5}{0} = \frac{5!}{0!(5-0)!} = \frac{5!}{0!5!} = \frac{5!}{1 \cdot 5!} = 1 $$ <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>
*   **Probability**: 1 out of 32 equally likely outcomes <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   $$ P(x=0) = \frac{1}{32} $$

### Probability of x = 1 Head

The probability of getting one head in five flips is:

*   **Combinations**: 5 choose 1, representing choosing 1 head out of 5 flips <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
    *   $$ \binom{5}{1} = \frac{5!}{1!(5-1)!} = \frac{5!}{1!4!} = \frac{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{1 \cdot (4 \cdot 3 \cdot 2 \cdot 1)} = 5 $$ <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>
*   **Probability**: 5 out of 32 equally likely outcomes <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
    *   $$ P(x=1) = \frac{5}{32} $$

### Probability of x = 2 Heads

The probability of getting two heads in five flips is:

*   **Combinations**: 5 choose 2, representing choosing 2 heads out of 5 flips <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    *   $$ \binom{5}{2} = \frac{5!}{2!(5-2)!} = \frac{5!}{2!3!} = \frac{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}{(2 \cdot 1)(3 \cdot 2 \cdot 1)} = \frac{120}{2 \cdot 6} = \frac{120}{12} = 10 $$ <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>
*   **Probability**: 10 out of 32 equally likely outcomes <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   $$ P(x=2) = \frac{10}{32} $$

### Probability of x = 3 Heads

The probability of getting three heads in five flips is:

*   **Combinations**: 5 choose 3, representing choosing 3 heads out of 5 flips <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   $$ \binom{5}{3} = \frac{5!}{3!(5-3)!} = \frac{5!}{3!2!} $$ <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>
    *   As observed, this is the same calculation as 5 choose 2, simply swapping the denominators' factorial terms <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
    *   $$ \binom{5}{3} = 10 $$ <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>
*   **Probability**: 10 out of 32 equally likely outcomes <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
    *   $$ P(x=3) = \frac{10}{32} $$

### Probability of x = 4 Heads

The probability of getting four heads in five flips is:

*   **Combinations**: 5 choose 4, representing choosing 4 heads out of 5 flips <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
    *   $$ \binom{5}{4} = \frac{5!}{4!(5-4)!} = \frac{5!}{4!1!} $$ <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>
    *   This is the same calculation as 5 choose 1, as 1! does not change the value <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
    *   $$ \binom{5}{4} = 5 $$ <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>
*   **Probability**: 5 out of 32 equally likely outcomes <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
    *   $$ P(x=4) = \frac{5}{32} $$

### Probability of x = 5 Heads

The probability of getting five heads (all heads) in five flips is:

*   **Combinations**: 5 choose 5, representing choosing 5 heads out of 5 flips <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    *   $$ \binom{5}{5} = \frac{5!}{5!(5-5)!} = \frac{5!}{5!0!} $$ <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>
    *   Since 0! = 1, this simplifies to 1 <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
    *   $$ \binom{5}{5} = 1 $$ <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>
*   **Probability**: 1 out of 32 equally likely outcomes <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.
    *   $$ P(x=5) = \frac{1}{32} $$

## Summary of Probabilities and Symmetry

The probabilities for the number of heads in five coin flips are:
*   P(x=0) = 1/32
*   P(x=1) = 5/32
*   P(x=2) = 10/32
*   P(x=3) = 10/32
*   P(x=4) = 5/32
*   P(x=5) = 1/32

This sequence (1, 5, 10, 10, 5, 1) demonstrates a clear [[Symmetry in Binomial Probabilities]] <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>, which is a characteristic pattern in binomial expansions related to [[patterns_in_binomial_expansions|binomial expansions]] <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. For example, the probability of getting five heads is the same as the probability of getting zero tails, and vice-versa <a class="yt-timestamp" data-t="00:11:31">[00:11:31]</a>. This approach highlights [[understanding_n_choose_k_and_factorials_in_the_context_of_binomials|understanding n choose k and factorials in the context of binomials]] <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a> and provides a method for [[calculating_powers_of_binomials|calculating powers of binomials]] related to probability distributions.