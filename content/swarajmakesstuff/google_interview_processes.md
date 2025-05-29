---
title: Google interview processes
videoId: IOWDHKlEEFA
---

From: [[swarajmakesstuff]] <br/> 

Google interview processes often include challenging questions designed to test a candidate's [[importance_of_critical_thinking_in_interviews | critical thinking]] skills <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. One such simple interview question has reportedly caused many candidates to fail <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## Common Interview Question: Finding the Odd Ball

The specific question involves:
> "You are given eight balls, seven of same weight and one is of different weight. You need to find the odd one out or the heavier ball with the least amount of moves." <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>

Candidates are encouraged to pause and attempt to solve it before proceeding <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Solution Strategies

Multiple solutions exist for this problem, with varying efficiency in terms of "moves" (weighing operations).

### Naive Approach (7 Moves)

The simplest solution involves comparing one ball to each and every other ball <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This method takes seven moves to identify the heavier ball <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

### Binary Division (3 Moves)

A more efficient method involves repeatedly separating the balls into two groups <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
1.  Separate the eight balls into two groups (e.g., four and four). Weigh them to find the heavier group <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
2.  Take the heavier group and separate those into two smaller groups (e.g., two and two). Weigh them to find the heavier pair <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
3.  Take the heavier pair and separate them into two individual balls. Weigh them to find the heavier ball <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

This approach takes three moves <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Optimal Ternary Division (2 Moves)

The most efficient solution allows finding the heavier ball in just two moves <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
1.  **First Move:** Divide the eight balls into three groups: one group of two balls and two groups of three balls each <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
    *   Weigh the two groups of three balls against each other <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
    *   **Scenario A: One group of three is heavier.** If one group of three is heavier, proceed with that group <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
    *   **Scenario B: Both groups of three are of the same weight.** If they are equal, the heavier ball must be in the group of two balls that were set aside <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
        *   Take these two balls and weigh them against each other to immediately identify the heavier one <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This concludes the process in two moves <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
2.  **Second Move (Scenario A Continuation):** If one group of three was heavier from the first weigh, take any two balls from this heavier group of three <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
    *   Weigh these two balls against each other <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   **If they are of equal weight:** The third ball from that group (the one not weighed) is the heavier ball <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
    *   **If one is heavier:** That ball is the heavier ball <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

In all cases, this optimal method allows for identifying the heavier ball in just two moves <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.