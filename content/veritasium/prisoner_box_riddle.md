---
title: Prisoner box riddle
videoId: iSNsgj1OCLA
---

From: [[veritasium]] <br/> 

The [[counterintuitive_riddles|Prisoner Box Riddle]] is a [[counterintuitive_riddles|riddle]] that seems incorrect even after learning the solution due to its highly [[counterintuitive_riddles|counterintuitive]] nature <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It is designed to confuse people <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. Many explanations found online are either incorrect or incomplete <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Riddle Setup

The setup involves 100 prisoners, numbered 1 to 100 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Slips of paper, each containing one of their numbers, are randomly placed into 100 sealed boxes in a room <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

Each prisoner enters the room one at a time and is allowed to open any 50 of the 100 boxes to search for their number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. After searching, they must leave the room exactly as they found it and cannot communicate with other prisoners <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. If all 100 prisoners find their own number, they will all be freed; if even one fails, they will all be executed <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Prisoners are allowed to strategize before any of them enter the room <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Random Search Probability

If prisoners each search for their number randomly, each has a 50% chance of finding it <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The probability that all 100 prisoners find their numbers is (1/2)^100, which is approximately 0.000... (30 zeros)8 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. To illustrate, two people have a better chance of picking the same grain of sand from all Earth's beaches and deserts than escaping this way <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

Despite these incredibly low odds, a strategy exists that raises their chances to nearly one in three <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, improving their odds by nearly 30 orders of magnitude <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This solution involves an incredible feature of mathematics <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

The riddle was conceived by computer scientist Peter Bro Miltersen, who didn't initially think of this strategy until a colleague pointed it out <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

## The Loop Strategy

The optimal strategy is as follows:
1.  When a prisoner enters the room, they open the box labeled with their own number <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  If the slip inside is not their number, they go to the box with the number found on the slip <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
3.  They continue this process of opening the box indicated by the slip found inside the current box <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
4.  They stop when they find their own number <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

This strategy yields over a 30% chance for all prisoners to find their number <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### How it Works: Permutation Cycles

The arrangement of slips in boxes forms closed loops (also called permutation cycles) <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   A simple loop might be a box containing its own number <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   A loop of two would be Box 1 pointing to Box 7, and Box 7 pointing back to Box 1 <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Loops can be of any length up to 100 <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   Any random arrangement of slips results in a mixture of shorter and longer loops <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

When a prisoner starts by opening the box labeled with their own number, they are guaranteed to be on the loop that includes their slip <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. The slip and box with the same number essentially form a "unit," and since every slip is hidden inside another box, there are no dead ends, only loops <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>. Starting with Box `X` means eventually finding Slip `X`, which directs back to Box `X`, closing the loop <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

A prisoner will find their slip if their number is part of a loop shorter than 50 <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. If their number is part of a loop that is 51 or longer, they will not find it before exhausting their 50 allowed searches <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. If a loop is 51 or longer, *all* prisoners on that loop will fail <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.

### Calculating Success Probability

The probability that all prisoners succeed is the probability that a random arrangement of 100 numbers contains no loops longer than 50 <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

The total number of ways to arrange 100 slips in 100 boxes (permutations) is 100 factorial (100!) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. However, since these are loops, a sequence of 100 numbers can be written 100 different ways while representing the same loop <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. Thus, the total number of unique loops of length 100 is 100! / 100 <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

The probability of a random arrangement containing a loop of length `N` in an `N`-box system is 1/`N` <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Therefore, the probability of a loop of length 100 is 1/100, length 99 is 1/99, and so on <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

The probability that there *is* a loop longer than 50 is the sum of probabilities for loops of length 51 to 100: 1/51 + 1/52 + ... + 1/100 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This sum equals approximately 0.69 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
*   This means there is a 69% chance of failure for the prisoners <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   Conversely, there is a 31% chance of success (1 - 0.69 = 0.31), where the longest loop is 50 or shorter <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Interdependence of Outcomes

While each prisoner's individual chance of finding their number is still 50% (as they can only open half the boxes), these probabilities are no longer independent <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   With a random guessing strategy, on most runs, around 50 prisoners would find their number <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   With the loop strategy, either *all* 100 prisoners find their numbers (31% of the time) or the *majority* fail (69% of the time) <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. The prisoners all win together or the majority loses together <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. This strategy links everyone's outcomes together, ensuring everyone in a loop has the same chance of finding their number <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. The chance for a given arrangement is either 100% or 0% <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

## Variations

### Sympathetic Guard

If a sympathetic prison guard sneaks into the room before the prisoners, they can guarantee success by swapping the contents of just two boxes <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. There can be at most one loop longer than 50 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. Swapping two box contents breaks this long loop into two separate loops, each shorter than 50 <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Malicious Guard Counter-Strategy

If a malicious guard knows the loop strategy and arranges the numbers to ensure a loop longer than 50, the prisoners are not doomed <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. They can counter by arbitrarily renumbering the boxes (e.g., adding five to each box number) <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Renumbering the boxes is functionally equivalent to redistributing the slips, effectively returning the problem to a random arrangement of loops, and thus restoring the 31% chance of survival <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

### Increasing the Number of Prisoners

The probability of success approaches a limit as the number of prisoners increases <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   For 1,000 prisoners, each checking 500 boxes, the chance of success is 30.74% <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   For 1 million prisoners, the probability is 30.685% <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   For 1 billion prisoners, the probability is only slightly lower <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

The probability of winning this game approaches a limit, which is calculated using the integral of 1/X from `n` to `2n` (where `n` is the number of boxes a prisoner can open, and `2n` is the total number of prisoners/boxes) <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. This integral is equal to the natural logarithm of two (ln(2)) <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>. Thus, the probability of success approaches **1 - ln(2)**, which is approximately 30.7% <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This means no matter how many prisoners there are, they will always have above a 30% chance of escaping using this strategy <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

At first, success seemed impossible, but with the loop strategy, a large number of prisoners can still achieve at least a 30% chance of all finding their numbers <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.