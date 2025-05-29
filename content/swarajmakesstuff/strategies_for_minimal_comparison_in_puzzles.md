---
title: Strategies for minimal comparison in puzzles
videoId: IOWDHKlEEFA
---

From: [[swarajmakesstuff]] <br/> 

This article outlines [[problemsolving_techniques_for_finding_odd_ball | problem-solving techniques]] for finding a single heavier ball among several identical ones, aiming for the fewest possible comparisons using a balance scale. This type of puzzle is often posed in [[google_interview_processes | Google interview processes]] to assess a candidate's [[importance_of_critical_thinking_in_interviews | critical thinking]] skills <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>.

## The Odd Ball Puzzle

The classic puzzle involves a set of eight balls, seven of which have the same weight, and one is slightly heavier. The goal is to identify the heavier ball using the minimum number of moves on a balance scale <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Proposed Solutions

Several approaches can be taken to solve this puzzle, with varying levels of efficiency.

### Solution 1: Direct Comparison (Inefficient)

The simplest, but least efficient, method is to compare one ball to each of the other balls individually <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>. This approach would require seven moves to definitively find the heavier ball <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

### Solution 2: Binary Division

A more intuitive and common method involves separating the balls into two groups <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.
*   First, the balls are divided into two halves, and these halves are weighed to determine which side is heavier <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   The heavier group is then further divided into two smaller groups, and the process is repeated <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.
*   This method typically requires three moves to identify the heavier ball <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

### Solution 3: Optimal Three-Group Division (2 Moves)

The most efficient solution to this puzzle requires only two moves <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. This [[stepbystep_solutions_for_weight_comparison_puzzles | step-by-step solution]] involves dividing the eight balls into three distinct groups <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>:
*   Group A: 3 balls
*   Group B: 3 balls
*   Group C: 2 balls <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a> - <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>

#### Move 1

Weigh Group A (3 balls) against Group B (3 balls) <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

*   **Scenario 1: One group is heavier.** If, for example, Group A is heavier <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, this means the heavier ball is within Group A.
*   **Scenario 2: Both groups are of equal weight.** If Group A and Group B weigh the same <a class="yt-timestamp" data-t="00:01:23">[00:01:24]</a>, then the heavier ball must be in Group C (the group of 2 balls that were not weighed) <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> - <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

#### Move 2

The second move depends on the outcome of Move 1:

*   **If a group of 3 was identified as heavier (Scenario 1):** Take any two balls from that heavier group of three and weigh them against each other <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a> - <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
    *   If one is heavier, that is the odd ball <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a> - <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
    *   If they are of equal weight, the third unweighed ball from that group of three is the heavier one <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a> - <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **If the group of 2 was identified as containing the heavier ball (Scenario 2):** Take the two balls from Group C and weigh them against each other <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a> - <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. The one that tips the scale is the heavier ball <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a> - <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

In both scenarios, the heavier ball is found in just two moves <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> - <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.