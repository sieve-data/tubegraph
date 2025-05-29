---
title: Galton board as a demonstration tool
videoId: zeJD6dqJ5lo
---

From: [[3blue1brown]] <br/> 

A [[visualizing_mathematical_concepts | Galton board]] is a popular device used to demonstrate how, even when individual events are chaotic and random, precise statements can still be made about a large number of events <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. It illustrates how the relative proportions for many different outcomes are distributed <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Demonstrating the Normal Distribution
Specifically, the Galton board showcases one of the most prominent distributions in probability: the normal distribution, also known as a bell curve or Gaussian distribution <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This distribution is exceptionally common, appearing in various seemingly unrelated contexts, such as the heights of people within a similar demographic or the number of distinct prime factors in large natural numbers <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The phenomenon observed on the Galton board is a key illustration of the Central Limit Theorem <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## Simplified Model for Explanation
To illustrate the Central Limit Theorem, a simplified model of the Galton board is often used <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. In this model:
*   Each ball falls onto a central peg <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   It has a 50-50 probability of bouncing to the left or to the right <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.
*   Each bounce is thought of as adding one or subtracting one from the ball's position <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
*   The ball is assumed to land precisely in the middle of the adjacent peg below, where it again faces the same 50-50 choice <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   For a board with five rows of pegs, the ball makes five random choices (+1 or -1), and its final position is the sum of these numbers <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The buckets are labeled with the sums they represent <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

While this model simplifies physics, its purpose is to provide a clear example for understanding the Central Limit Theorem <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. If many balls are allowed to fall (assuming they don't influence each other), the number of balls in each bucket indicates the likelihood of each outcome <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. The calculation of probabilities in this simplified model is reminiscent of Pascal's triangle <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

The core idea demonstrated is that as the number of "random choices" (rows of pegs) increases, the distribution of the final positions (sums) increasingly resembles a bell curve <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.

## Limitations and Assumptions
Despite its effectiveness as a demonstration, the real Galton board actually violates some of the fundamental assumptions of the Central Limit Theorem <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>. The theorem assumes that the variables being added are:
1.  **Independent from each other (I):** The outcome of one process does not influence the outcome of another <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>. In a real Galton board, how a ball bounces off one peg directly influences its trajectory and interaction with the next peg <a class="yt-timestamp" data-t="00:28:56">[00:28:56]</a>.
2.  **Identically distributed (ID):** All variables are drawn from the same probability distribution <a class="yt-timestamp" data-t="00:28:27">[00:28:27]</a>. For a real Galton board, the distribution of possible outcomes off each peg might not be the same, as a ball might hit one peg glancing to the left and the next glancing to the right <a class="yt-timestamp" data-t="00:29:08">[00:29:08]</a>.

These two assumptions are often collectively referred to as "IID" (independent and identically distributed) <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>. The initial simplifying assumptions made for the Galton board model were necessary to align it with the Central Limit Theorem's requirements <a class="yt-timestamp" data-t="00:29:29">[00:29:29]</a>.

Despite these violations in a real Galton board, a normal distribution still appears to emerge <a class="yt-timestamp" data-t="00:29:38">[00:29:38]</a>. This might be partly due to generalizations of the theorem that relax these assumptions <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a>. However, it's important to exercise caution, as variables are sometimes assumed to be normally distributed without proper justification <a class="yt-timestamp" data-t="00:29:54">[00:29:54]</a>.