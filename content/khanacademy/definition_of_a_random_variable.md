---
title: Definition of a random variable
videoId: WWv0RUxDfbs
---

From: [[khanacademy]] <br/> 
A [[random_variables | random variable]] is a mathematical concept used to convert particular outcomes of a random process into numbers <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

## Example: Coin Flips <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

Let's define a [[random_variables | random variable]] `x` as the number of heads obtained from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

This specific [[random_variables | random variable]] can take on the following integer values: 0, 1, 2, 3, 4, or 5 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Total Possible Outcomes <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>

To determine the probability of `x` taking on any of its possible values, we first need to calculate the total number of equally likely outcomes from flipping a fair coin five times <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>, <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

*   For each flip, there are two possibilities (heads or tails) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   Since there are five flips, the total number of equally likely outcomes is 2 multiplied by itself five times (2^5) <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   2^5 = 32 <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

So, there are 32 equally likely possible outcomes when flipping a fair coin five times <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. Examples of such outcomes include "tails, heads, tails, heads, tails" or "heads, heads, heads, tails, tails" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Calculating Probabilities for `x` <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>

To find the probability that the [[random_variables | random variable]] `x` takes on a certain value, we need to determine how many of the 32 equally likely outcomes result in that specific number of heads <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

*   **P(x = 0): Probability of getting zero heads**
    *   This means all five flips are tails <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   There is only one way to get no heads (TTTTT) <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
    *   This can also be expressed using combinations: "5 choose 0" (C(5,0)) ways to choose 0 heads out of 5 flips <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.
    *   C(5,0) = 5! / (0! * (5-0)!) = 5! / (1 * 5!) = 1 <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
    *   P(x = 0) = 1/32 <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

*   **P(x = 1): Probability of getting one head**
    *   There are five different places the single head can occur (e.g., HTTTT, THTTT, TTHTT, TTTHT, TTTTH) <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
    *   This is "5 choose 1" (C(5,1)) ways to choose 1 head out of 5 flips <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
    *   C(5,1) = 5! / (1! * (5-1)!) = 5! / (1 * 4!) = 5 <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
    *   P(x = 1) = 5/32 <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

*   **P(x = 2): Probability of getting two heads**
    *   This is "5 choose 2" (C(5,2)) ways to choose 2 heads out of 5 flips <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    *   C(5,2) = 5! / (2! * (5-2)!) = 5! / (2! * 3!) = (5 * 4 * 3 * 2 * 1) / ((2 * 1) * (3 * 2 * 1)) = 10 <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   P(x = 2) = 10/32 <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

*   **P(x = 3): Probability of getting three heads**
    *   This is "5 choose 3" (C(5,3)) ways to choose 3 heads out of 5 flips <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
    *   C(5,3) = 5! / (3! * (5-3)!) = 5! / (3! * 2!) = 10 <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
    *   P(x = 3) = 10/32 <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

*   **P(x = 4): Probability of getting four heads**
    *   This is "5 choose 4" (C(5,4)) ways to choose 4 heads out of 5 flips <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.
    *   C(5,4) = 5! / (4! * (5-4)!) = 5! / (4! * 1!) = 5 <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
    *   Alternatively, getting four heads means getting one tail, and there are five places for that one tail <a class="yt-timestamp" data-t="00:10:16">[00:10:16]</a>.
    *   P(x = 4) = 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.

*   **P(x = 5): Probability of getting five heads**
    *   This means all five flips are heads <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
    *   There is only one way to get all heads (HHHHH) <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
    *   This is "5 choose 5" (C(5,5)) ways to choose 5 heads out of 5 flips <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    *   C(5,5) = 5! / (5! * (5-5)!) = 5! / (5! * 0!) = 1 <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
    *   P(x = 5) = 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

### Summary of Probabilities <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>

The probabilities for `x` are:
*   P(x = 0) = 1/32 <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>
*   P(x = 1) = 5/32 <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>
*   P(x = 2) = 10/32 <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>
*   P(x = 3) = 10/32 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>
*   P(x = 4) = 5/32 <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>
*   P(x = 5) = 1/32 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>

Notice the symmetry in the probabilities: 1, 5, 10, 10, 5, 1 <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>, <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>. This makes sense because the probability of getting `k` heads is the same as the probability of getting `k` tails (which corresponds to 5-k heads) <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. For instance, the probability of 5 heads (0 tails) is the same as 0 heads (5 tails) <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.