---
title: Random Variables in Probability
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 

A [[random_variables | random variable]] is a function that converts particular outcomes from an experiment into numbers <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This transformation allows for quantitative analysis of the outcomes.

## Example: Coin Flips

Let's define a [[random_variables | random variable]] `x` as the number of heads obtained from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

Possible values that the [[random_variables | random variable]] `x` can take are 0, 1, 2, 3, 4, or 5 heads <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. The objective is to determine the [[basic_probability_concepts | probability]] that this [[random_variables | random variable]] takes on each of these values <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. This process lays the groundwork for understanding the [[random_variables | probability distribution]] of a [[random_variables | random variable]], particularly the [[random_variables | binomial distribution]] <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

### Total Possible Outcomes

First, consider the total number of possible outcomes when flipping a fair coin five times. For each flip, there are two possibilities (Heads or Tails) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

The total number of [[equally_likely_possibilities_in_probability | equally likely possibilities]] for five flips is:
2 (first flip) × 2 (second flip) × 2 (third flip) × 2 (fourth flip) × 2 (fifth flip) = 2^5 = 32 outcomes <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
Each of these 32 outcomes, like "tails, heads, tails, heads, tails" or "heads, heads, heads, tails, tails," is an [[equally_likely_possibilities_in_probability | equally likely outcome]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Calculating Probabilities for `x`

To find the [[basic_probability_concepts | probability]] of `x` taking a specific value, we determine how many of these 32 [[equally_likely_possibilities_in_probability | equally likely possibilities]] result in that value, and then divide by 32 <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Combinatorics (specifically "n choose k" or binomial coefficients) can be used to count these possibilities.

*   **P(x=0): Probability of zero heads**
    This means all five flips are tails. There is only one such outcome (TTTTT) <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    Using combinatorics: "5 choose 0" (C(5, 0)) = 1 <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
    $$P(x=0) = \frac{\text{C(5, 0)}}{32} = \frac{1}{32}$$ <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>

*   **P(x=1): Probability of one head**
    There are five ways to get one head (HTTTT, THTTT, TTHTT, TTTHT, TTTTH) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    Using combinatorics: "5 choose 1" (C(5, 1)) = 5 <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
    $$P(x=1) = \frac{\text{C(5, 1)}}{32} = \frac{5}{32}$$ <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>

*   **P(x=2): Probability of two heads**
    Using combinatorics: "5 choose 2" (C(5, 2)) = $\frac{5!}{2!(5-2)!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{(2 \times 1)(3 \times 2 \times 1)} = \frac{120}{2 \times 6} = \frac{120}{12} = 10$ <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    $$P(x=2) = \frac{\text{C(5, 2)}}{32} = \frac{10}{32}$$ <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

*   **P(x=3): Probability of three heads**
    Using combinatorics: "5 choose 3" (C(5, 3)) = $\frac{5!}{3!(5-3)!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{(3 \times 2 \times 1)(2 \times 1)} = \frac{120}{6 \times 2} = \frac{120}{12} = 10$ <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
    $$P(x=3) = \frac{\text{C(5, 3)}}{32} = \frac{10}{32}$$ <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>

*   **P(x=4): Probability of four heads**
    Using combinatorics: "5 choose 4" (C(5, 4)) = $\frac{5!}{4!(5-4)!} = \frac{5 \times 4 \times 3 \times 2 \times 1}{(4 \times 3 \times 2 \times 1)(1)} = \frac{120}{24} = 5$ <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
    $$P(x=4) = \frac{\text{C(5, 4)}}{32} = \frac{5}{32}$$ <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>

*   **P(x=5): Probability of five heads**
    This means all five flips are heads. There is only one such outcome (HHHHH) <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
    Using combinatorics: "5 choose 5" (C(5, 5)) = 1 <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    $$P(x=5) = \frac{\text{C(5, 5)}}{32} = \frac{1}{32}$$ <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

### Probability Distribution Summary

The probabilities for the [[random_variables | random variable]] `x` (number of heads in 5 coin flips) are:
*   P(x=0) = 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>
*   P(x=1) = 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>
*   P(x=2) = 10/32 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>
*   P(x=3) = 10/32 <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>
*   P(x=4) = 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>
*   P(x=5) = 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

Notice the symmetry in the probabilities (1, 5, 10, 10, 5, 1) <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This makes sense because the [[basic_probability_concepts | probability]] of getting a certain number of heads is symmetrical to getting the same number of tails (e.g., 5 heads is 0 tails, 0 heads is 5 tails) <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. The sum of these probabilities is 1 (1+5+10+10+5+1 = 32/32 = 1).

Further analysis of this [[random_variables | probability distribution]] can involve graphical representations and is foundational to understanding concepts like the [[random_variables | binomial distribution]] <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.