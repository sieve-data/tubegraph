---
title: Probability calculations and mathematical strategies
videoId: iSNsgj1OCLA
---

From: [[veritasium]] <br/> 

The 100 Prisoners Riddle is a perplexing problem known for its highly counterintuitive solution, which often seems wrong even after the answer is revealed <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Despite its complex nature, the solution involves an incredible feature of mathematics <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. While many online explanations exist, they are often incomplete or incorrect <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This article delves into the riddle, its [[mathematical_probability_strategies | mathematical probability strategies]], and the surprising [[Probability calculations and mathematical strategies | probability calculations]] behind its resolution.

## The Riddle Setup

Imagine 100 prisoners, numbered 1 to 100 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Slips of paper, each containing one of their numbers, are randomly placed inside 100 sealed boxes in a room <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Each prisoner, one at a time, enters the room and is allowed to open any 50 of the 100 boxes in search of their own number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. After searching, they must leave the room exactly as they found it, and no communication with other prisoners is permitted <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

The stakes are high: if all 100 prisoners successfully find their own number, they are all freed <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. However, if even one prisoner fails, all are executed <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The prisoners are allowed to strategize together beforehand <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. The core question is: what is their best strategy to maximize their chances of survival <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>?

### The Random Guessing Scenario

If each prisoner were to search for their number randomly, each would have a 50% chance of finding it <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The probability of all 100 prisoners finding their numbers would be (1/2) multiplied by itself 100 times, or (1/2)^100 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This results in an incredibly small probability of approximately 0.0000000000000000000000000000008 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. To put this in perspective, two people have a better chance of picking the same grain of sand from all the beaches and deserts on Earth than the prisoners do of escaping this way <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Loop Strategy: A Game-Changer

Surprisingly, with the right strategy, their chances of success can be raised to nearly one in three <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>, an improvement of nearly 30 orders of magnitude <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This [[mathematical_probability_strategies | mathematical strategy]], devised by computer scientist Peter Bro Miltersen, is not immediately obvious <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### How the Strategy Works

The strategy is as follows:
1.  When a prisoner enters the room, they open the box labeled with their own number <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  The slip inside will likely contain a different number <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  The prisoner then goes to the box with *that* number on it <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
4.  They continue this process – opening the box indicated by the slip found inside the current box – until they find their own number <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
5.  If they find their number, they are done and can leave the room <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

This seemingly simple strategy gives over a 30% chance that all prisoners will find their number <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### The Underlying Principle: Loops

The key to understanding this strategy lies in recognizing that the arrangement of slips in boxes forms closed loops <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. For example:
*   A loop of one: Box 1 contains slip 1 <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   A loop of two: Box 1 points to Box 7, and Box 7 points back to Box 1 <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Loops can be of any length up to 100 <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
Any random arrangement of slips will result in a mixture of shorter and longer loops <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

When a prisoner starts by opening the box labeled with their own number, they are guaranteed to be on the loop that includes their slip <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This is because every box contains a slip, which points to another box, ensuring that there are no "dead ends" and only loops are formed <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. Starting with Box X means the prisoner *must* eventually find Slip X to close that specific loop <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

The success of a prisoner depends on the length of the loop their number belongs to <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. If their number is part of a loop shorter than 50, they will definitely find their slip within their allotted 50 box openings <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. However, if their number is part of a loop that is 51 boxes or longer, they will not find it before exhausting their 50 attempts <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Crucially, if there's a loop longer than 50, *all* prisoners whose numbers are part of that long loop will fail together <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### Calculating the Probability of Success

The probability that all prisoners succeed using this strategy is the probability that a random arrangement of 100 numbers contains no loops longer than 50 <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

To calculate this, consider the total number of ways to arrange the slips (permutations). For 100 boxes, there are 100 factorial (100!) ways to arrange the slips <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. However, since these are loops, a sequence like 1->2->...->100->1 is the same loop as 2->...->100->1->2 <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. There are 100 such starting points for a loop of length 100, so the number of unique loops of length 100 is 100! / 100 <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

The probability of a random arrangement containing a loop of length `N` in a set of `N` items is `1/N` <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. Therefore:
*   The probability of a loop of length 100 is 1/100 <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   The probability of a loop of length 99 is 1/99 <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   And so on.

The prisoners fail if there is *any* loop longer than 50. So, the probability of failure is the sum of probabilities for loops of length 51, 52, ..., up to 100:
P(Failure) = (1/51) + (1/52) + ... + (1/100) <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
This sum equals approximately 0.69, or 69% <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
Therefore, the probability of success is 1 - P(Failure) = 1 - 0.69 = 0.31, or 31% <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Collective vs. Individual Outcomes

While the collective probability of success for all prisoners is 31%, each individual prisoner's chance of finding their number is still 50% <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. However, unlike random guessing, these probabilities are no longer independent <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. The loop strategy links everyone's outcomes: they all win together (31% of the time) or the majority loses together (69% of the time) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. This means there's no scenario where only a few people miss their numbers; it's either a complete success or a widespread failure <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

## External Influences and Scaling

### Sympathetic or Malicious Guards

*   **Sympathetic Guard**: If a sympathetic prison guard could sneak into the room beforehand, they could guarantee success <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. This is achieved by identifying the single loop longer than 50 (if one exists) and breaking it in half by swapping the contents of just two boxes, creating two loops each shorter than 50 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **Malicious Guard**: If a malicious guard knew the strategy and arranged the slips to form a loop longer than 50, the prisoners are not doomed <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. They can counter by arbitrarily renumbering the boxes (e.g., adding five to each box number) <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Renumbering the boxes is mathematically equivalent to redistributing the slips, effectively returning the problem to a random arrangement of loops and restoring their 31% chance of survival <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

### Increasing the Number of Prisoners

A remarkable aspect of this riddle is how the probability changes (or doesn't change much) as the number of prisoners increases <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. For example:
*   With 1,000 prisoners, each allowed to check 500 boxes, the chance of success is 30.74% <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   For 1 million prisoners, the probability of success is 30.685% <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

The probability of winning this game approaches a limit <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. This limit is derived from the [[mathematical_series_expansion | mathematical series expansion]] representing the probability of failure: 1/N + 1/(N+1) + ... + 1/(2N-1). This sum can be approximated by the integral of 1/X from N to 2N <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. The integral of 1/X is the natural logarithm of X (ln X) <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. Thus, the probability of failure approaches ln(2N) - ln(N) = ln(2N/N) = ln(2) <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

Therefore, the probability of success approaches **1 - ln(2)**, which is approximately 30.7% <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This means that no matter how many prisoners are involved, using this strategy maintains an escape chance of over 30% <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

## Conclusion

The 100 Prisoners Riddle showcases how a clever [[mathematical_probability_strategies | mathematical strategy]] can drastically improve odds that initially seem impossible <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. By linking the outcomes of all individuals through the "loop strategy," their collective chance of success transforms from infinitesimally small to a consistent one-in-three, regardless of the number of participants <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

***

*This article was brought to you in part by Brilliant.org, offering interactive lessons in math and science, including courses on perplexing probability and problem-solving. Find out more at brilliant.org/veritasium.* <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>