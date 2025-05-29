---
title: Stepbystep solutions for weight comparison puzzles
videoId: IOWDHKlEEFA
---

From: [[swarajmakesstuff]] <br/> 

This article explores a classic weight comparison puzzle often posed during [[google_interview_processes | Google interviews]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The challenge is to identify an odd-weight ball (specifically, a heavier one) among a set of identical balls using the fewest possible moves or weighings.

## The Problem Statement

You are presented with eight balls <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Seven of these balls share the same weight, while one is of a different, specifically heavier, weight <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Your task is to find the odd, heavier ball using the minimum number of comparisons <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This puzzle falls under the category of [[strategies_for_minimal_comparison_in_puzzles | strategies for minimal comparison in puzzles]] and [[problemsolving_techniques_for_finding_odd_ball | problemsolving techniques for finding odd ball]].

## Solution Approaches

Here are three methods to solve this puzzle, ranging from the most straightforward to the most efficient.

### Method 1: Direct Comparison (7 Moves)

The simplest approach involves directly comparing one ball against each of the others <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

*   **Process:** Pick one ball and weigh it against another. If they are equal, the heavier ball is not among them, so you continue comparing your initial ball with a new, unweighed ball. If one is heavier, you've found it.
*   **Moves:** This method will require a maximum of seven moves to find the heavier ball <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Method 2: Binary Division (3 Moves)

A more common solution involves dividing the balls into two groups and successively narrowing down the possibilities <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

*   **Process:**
    1.  Divide the eight balls into two groups of four <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
    2.  Weigh one group of four against the other <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The heavier side contains the odd ball. (1st move) <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>
    3.  Take the heavier group (four balls) and divide it into two groups of two <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Weigh these two groups against each other. The heavier side contains the odd ball. (2nd move) <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>
    4.  Take the remaining heavier group (two balls) and weigh them against each other <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. The heavier ball is identified. (3rd move) <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>
*   **Moves:** This method identifies the heavier ball in three moves <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Method 3: Optimal Ternary Division (2 Moves)

The most efficient solution, often the one sought in interviews, involves dividing the balls into three groups <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

*   **Process:**
    1.  Divide the eight balls into three groups:
        *   Group A: 3 balls <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
        *   Group B: 3 balls <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>
        *   Group C: 2 balls <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
    2.  **First Weighing:** Weigh Group A against Group B <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. (1st move)
        *   **Scenario 1: Group A is heavier.** The heavier ball is in Group A (3 balls) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
        *   **Scenario 2: Group B is heavier.** The heavier ball is in Group B (3 balls).
        *   **Scenario 3: Groups A and B are of equal weight.** The heavier ball must be in Group C (2 balls) <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
    3.  **Second Weighing:**
        *   **If the heavier group was 3 balls (Scenario 1 or 2):** Take two balls from this group and weigh them against each other <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. (2nd move)
            *   If one is heavier, it is the odd ball <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
            *   If they are equal, the third ball (the one not weighed) is the heavier ball <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.
        *   **If the heavier group was 2 balls (Scenario 3):** Weigh the two balls from Group C against each other <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. (2nd move)
            *   The heavier of the two is the odd ball <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **Moves:** This method guarantees finding the heavier ball in just two moves <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

```ad-tip
This optimal solution relies on the principle of reducing the potential pool of balls by a factor of three in each weighing, rather than two (as in binary division).
```