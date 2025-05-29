---
title: Problemsolving techniques for finding odd ball
videoId: IOWDHKlEEFA
---

From: [[swarajmakesstuff]] <br/> 

This article explores a classic puzzle often used in [[google_interview_processes | Google interview processes]] to assess a candidate's [[importance_of_critical_thinking_in_interviews | critical thinking]] and problem-solving skills <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The challenge is to identify an "odd" ball (specifically, a heavier one) from a set of otherwise identical balls using the fewest possible moves with a balance scale <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>, <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## The Puzzle

You are given eight balls <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Seven of these balls have the same weight, while one ball is heavier <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>, <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. The objective is to find the heavier ball with the least amount of moves (weighings) <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>, <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Solution Approaches

There are several ways to approach this puzzle, ranging from straightforward but inefficient to optimized solutions.

### 1. One-to-One Comparison

The simplest, though least efficient, solution involves comparing one ball against every other ball individually <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>, <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>, <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.
*   **Moves:** This method would take seven moves <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>, <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### 2. Binary Division (Divide and Conquer)

A more common and somewhat intuitive approach involves dividing the balls into two groups <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>, <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.
*   **Steps:**
    1.  Separate the eight balls into two groups (e.g., four balls per group) <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
    2.  Weigh the two groups to find which is heavier <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
    3.  Take the heavier group and separate its balls into two new groups (e.g., two balls per group) <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>, <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
    4.  Weigh these new groups to identify the heavier pair <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
    5.  From the heavier pair, separate them into two individual balls and weigh them to find the odd one out <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>, <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>, <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   **Moves:** This approach takes three moves <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### 3. Optimal Solution (Three-Group Division)

The most efficient solution involves dividing the balls into three groups <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.
*   **Groups:**
    *   Group 1: Two balls <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>
    *   Group 2: Three balls <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>
    *   Group 3: Three balls <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>, <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Weighing Steps:**

    *   **Move 1:** Weigh Group 2 (three balls) against Group 3 (three balls) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
        *   **Scenario A: One side is heavier.** If, for instance, Group 2 is heavier <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, the heavier ball is among those three <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
            *   **Move 2 (for Scenario A):** Take any two balls from this heavier group of three <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>, <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>, and weigh them against each other <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
                *   If one is heavier, that's your ball <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>, <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
                *   If they are of equal weight <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, the third ball (the one not weighed) is the heavier one <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>, <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>, <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
        *   **Scenario B: Both sides are of same weight.** If Group 2 and Group 3 are of the same weight <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>, <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, it means the heavier ball must be in Group 1 (the two balls that were not weighed) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>, <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>, <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
            *   **Move 2 (for Scenario B):** Take the two balls from Group 1 and weigh them against each other <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>, <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. The heavier ball will immediately be identified <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>, <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

*   **Moves:** Regardless of the outcome, this method consistently finds the heavier ball in just two moves <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>, <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>, <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>, <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>, <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>, <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

---
**See Also:**
*   [[strategies_for_minimal_comparison_in_puzzles | Strategies for minimal comparison in puzzles]]
*   [[stepbystep_solutions_for_weight_comparison_puzzles | Stepbystep solutions for weight comparison puzzles]]