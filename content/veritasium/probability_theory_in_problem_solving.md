---
title: Probability theory in problem solving
videoId: iSNsgj1OCLA
---

From: [[veritasium]] <br/> 

The 100 Prisoners Riddle is a [[counterintuitive_logic_puzzles|counterintuitive riddle]] that often seems wrong even when the solution is known <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It serves as a prime example of how [[strategies_for_complex_problem_solving|strategies for complex problem solving]] can drastically improve odds, revealing an "incredible feature of math" <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. Computer scientist Peter Bro Miltersen, who originated the riddle, did not initially conceive of its optimal strategy until a colleague pointed it out <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

## The Riddle Setup

There are 100 prisoners, numbered 1 to 100 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Slips of paper, each containing one of their numbers, are randomly placed into 100 sealed boxes in a room <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

Each prisoner is allowed to enter the room one at a time <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>:
*   They can open any 50 of the 100 boxes to search for their number <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   After their turn, they must leave the room exactly as they found it <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   They cannot communicate with other prisoners in any way <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

If all 100 prisoners find their own number, they will all be freed <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. If even one fails, they will all be executed <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The prisoners are allowed to strategize beforehand <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Initial Random Strategy

If each prisoner searches randomly for their number, they each have a 50% chance of finding it <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The probability that all 100 succeed is calculated as (1/2) multiplied by itself 100 times, or (1/2)^100 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This results in an incredibly low probability of 0.000... (30 zeros) ...8 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This chance is less than two people picking out the same grain of sand from all the beaches and deserts on Earth <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Loop Strategy

With the right strategy, the prisoners can improve their chances to nearly one in three <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, an improvement of nearly 30 orders of magnitude <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

The strategy is as follows:
1.  When a prisoner enters the room, they open the box with their own number on it <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  The slip inside will likely contain a different number <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  They then go to the box with *that* number on it and look at the slip inside <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
4.  They continue this process of opening the box indicated by the slip found in the previous box <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
5.  They continue until they find the slip with their own number <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. If they find it, they stop and leave the room <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

This strategy gives the prisoners over a 30% chance of all finding their numbers <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### How the Loop Strategy Works

The key insight is that the arrangement of slips in boxes forms **closed loops** <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   A "loop of one" occurs if a box contains its own number <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   A "loop of two" occurs if box A points to box B, and box B points back to box A <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Loops can be of any length up to 100 <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>. A random arrangement will result in a mixture of shorter and longer loops <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

When a prisoner starts with the box labeled with their own number, they are guaranteed to be on the loop that includes their slip <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This is because every box contains a slip, and every slip points to another box, meaning there are no "dead ends" and all numbers necessarily form loops <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>, <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. Following this chain of numbers will always lead back to the starting box's number, closing the loop <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

Success depends on the length of the loop containing the prisoner's number <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>:
*   If a prisoner's number is part of a loop shorter than 50 boxes, they will definitely find their slip within their 50 allowed searches <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   If a prisoner's number is part of a loop that is 51 or longer, they will not find it before exhausting their 50 searches <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

If even one prisoner is on a loop longer than 50, all prisoners on that loop (and thus all prisoners on any loop longer than 50) will fail <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. Therefore, the probability that all prisoners succeed is the probability that a random arrangement of 100 numbers contains **no loops longer than 50** <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### Calculating the Probability of Success

The total number of unique arrangements (permutations) of 100 slips in 100 boxes is 100 factorial (100!) <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>, <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>.

For any given permutation, the probability of it forming a loop of a specific length 'L' is 1/L <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. For example:
*   The probability of a random arrangement resulting in a loop of length 100 is 1/100 <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   The probability of a loop of length 99 is 1/99 <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   The probability of a loop of length 98 is 1/98 <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.

The probability that there is a loop longer than 50 is the sum of the probabilities of loops of length 51, 52, up to 100 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>:
1/51 + 1/52 + 1/53 + ... + 1/100

This sum equals approximately 0.69 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. This means there is a 69% chance of failure for the prisoners <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>. Consequently, there is a **31% chance of success**, meaning the longest loop is 50 or shorter <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Interdependent Probabilities

While each prisoner's individual chance of finding their number is still 50% (as they can only open half the boxes) <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>, these probabilities are no longer independent <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   With random guessing, around 50 prisoners would find their numbers on most runs <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   With the loop strategy, all prisoners find their numbers 31% of the time <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   69% of the time, fewer than 50 find their numbers (as all on the long loop fail together) <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

The strategy means the prisoners either all win together or the majority loses together <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

## Variations and Extensions

### Sympathetic Prison Guard

If a sympathetic guard could sneak into the room beforehand, they could guarantee success by swapping the contents of just two boxes <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. There can be at most one loop longer than 50 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>, and swapping two slips within that loop breaks it into two shorter loops, each under 50 <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Malicious Prison Guard

If a malicious guard knew the loop strategy and intentionally arranged the numbers to form a loop longer than 50, the prisoners are not doomed <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. They can counter by arbitrarily renumbering the boxes (e.g., adding five to each box number) <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Renumbering the boxes is equivalent to redistributing the slips, effectively returning the problem to a random arrangement and restoring their 31% chance of survival <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

### Increasing the Number of Prisoners

Contrary to what might be intuitively assumed <a class="yt-timestamp" data-t="00:14:45">[00:14:45]</a>, the probability of success does not drop dramatically as the number of prisoners increases, provided each prisoner can still check half the boxes <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   For 1,000 prisoners (each checking 500 boxes), the chance of success is 30.74% <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
*   For 1 million prisoners, it's 30.685% <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

The probability of winning this game approaches a limit <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. This limit is calculated using the natural logarithm of two (ln(2)) <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. The probability of failure is approximated by the integral of 1/X from n to 2n (where 'n' is the number of boxes a prisoner can open, and '2n' is the total number of boxes), which is equal to ln(2) <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. Thus, the probability of success approaches 1 - ln(2), which is approximately **30.7%** <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.

No matter how many prisoners there are, using this strategy, they maintain at least a 30% chance of escape <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. The beauty of the loop strategy lies in linking everyone's outcomes together, rather than each prisoner having an independent 50-50 chance <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. With this strategy, the outcome is often all-or-nothing: either complete success or catastrophic failure for the majority <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.