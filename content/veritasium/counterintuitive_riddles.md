---
title: Counterintuitive riddles
videoId: iSNsgj1OCLA
---

From: [[veritasium]] <br/> 

Some riddles are so counterintuitive that their solutions still seem wrong even after understanding them <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These riddles often involve "incredible features of math" <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. One such example is the [[prisoner_box_riddle | 100 Prisoners Riddle]], originally proposed by computer scientist Peter Bro Miltersen <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## The [[prisoner_box_riddle | 100 Prisoners Riddle]] Setup

The riddle presents the following scenario <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>:
*   **Participants**: 100 prisoners, numbered 1 to 100 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   **The Room**: 100 boxes are in a sealed room <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Slips of paper, each containing one of the prisoner's numbers, are randomly placed inside these boxes <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **The Task**: One at a time, each prisoner enters the room and can open any 50 of the 100 boxes to find the slip with their own number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   **Conditions**:
    *   The room must be left exactly as it was found <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
    *   Prisoners cannot communicate with each other in any way once the process begins <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **Outcome**: If *all* 100 prisoners find their number, they are all freed. If even one fails, all are executed <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   **Strategy**: Prisoners are allowed to strategize together *before* anyone enters the room <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Initial Probability (Random Guessing)

If each prisoner randomly opens 50 boxes, their individual chance of finding their number is 50% <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. For all 100 prisoners to succeed, the probability would be (1/2)^100 <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

This probability is extremely low, approximately 0.000... (30 zeros) ...8 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. To put this in perspective, two people have a better chance of picking the same grain of sand from all Earth's beaches and deserts than escaping this way <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### The "Loop Strategy"

Despite the dire odds, a specific strategy can raise their chances of success to nearly one in three <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, improving their odds by almost 30 orders of magnitude <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This strategy was not even conceived by the riddle's creator, Peter Bro Miltersen, until a colleague pointed it out <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

The strategy is as follows:
1.  When a prisoner enters the room, they first open the box that has their own number on it <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
2.  If the slip inside is not their number, they note the number on that slip <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  They then go to the box corresponding to the number they just read <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
4.  They continue this process – opening the box whose number matches the slip they just found – until they find their own number <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
5.  If they find their number within 50 attempts, they succeed for their turn and leave the room <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Using this "loop strategy," the probability that all prisoners succeed jumps to over 30% <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### How the Loop Strategy Works

The key insight is that any random arrangement of the slips in the boxes will form one or more closed loops <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   For example, if box 1 contains slip 7, box 7 contains slip 23, and box 23 contains slip 1, this forms a loop of length three <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   A box containing its own number forms a loop of length one <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   Every box contains a slip, and every slip points to another box, meaning there are no "dead ends" and only loops can form <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

When a prisoner starts by opening the box labeled with their own number, they are guaranteed to be on the loop that contains their slip <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. They must eventually find their own slip because that is the slip that directs them back to the box they started with, closing the loop <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

The success of a prisoner depends entirely on the length of the loop their number is part of <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   If their number is part of a loop shorter than 50 (the maximum allowed searches), they will definitely find their slip <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   If their number is part of a loop that is 51 or longer, they will not find it within their 50 attempts <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. If a loop is 51 long, all 51 prisoners on that loop will fail <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Calculating the Probability of Success

The probability that all prisoners succeed is the probability that a random arrangement of 100 slips contains no loops longer than 50 <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

1.  **Total Arrangements**: There are 100 factorial (100!) ways to arrange 100 slips in 100 boxes <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
2.  **Unique Loops**: The number of unique loops of a given length `N` is `N! / N` <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
3.  **Probability of a Specific Loop Length**: The probability that a random arrangement contains a loop of length `N` (e.g., 100) is `(N! / N) / N!` = `1/N` <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. So, the chance of a loop of length 100 is 1/100, length 99 is 1/99, and so on <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
4.  **Probability of Failure**: The prisoners fail if there is *any* loop longer than 50. This is the sum of probabilities for loops of length 51, 52, ..., up to 100 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>:
    `P(failure) = 1/51 + 1/52 + 1/53 + ... + 1/100`
    This sum approximately equals 0.69 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
5.  **Probability of Success**: Therefore, the probability of success (where the longest loop is 50 or shorter) is `1 - P(failure)` = `1 - 0.69` = `0.31` or 31% <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### The Linked Outcome

While each prisoner still individually has a 50% chance of finding their number if they were isolated <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, the probabilities are no longer independent of each other with the loop strategy <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. With this strategy, the prisoners either all win together (31% of the time) or the majority lose together (69% of the time) <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. There's no middle ground where only a few people miss their numbers; success is complete or failure is widespread <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

### Variations and Counters

*   **Sympathetic Guard**: If a sympathetic prison guard could sneak into the room before the prisoners, they could guarantee success by swapping the contents of just two boxes <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. This is because there can be at most one loop longer than 50, and swapping two boxes breaks it into two shorter loops <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **Malicious Guard**: If a malicious guard knew the prisoners' strategy and deliberately arranged the slips to form a loop longer than 50, the prisoners might seem doomed <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. However, the prisoners can counter this by arbitrarily renumbering the boxes (e.g., adding five to each box number) <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Renumbering the boxes is mathematically equivalent to redistributing the slips, effectively resetting the problem to a random arrangement of loops and restoring their 31% chance of survival <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

### Scaling the Riddle to Infinity

The probability of success remains surprisingly high as the number of prisoners increases.
*   For 1,000 prisoners (each checking 500 boxes), the chance of success is about 30.74% <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   For 1 million prisoners, it's 30.685% <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   As the number of prisoners (N) goes to infinity, the probability of success approaches a limit: `1 - natural logarithm of 2` (1 - ln(2)) <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This is approximately 30.7% <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>.

The probability of winning this game indeed approaches a limit, meaning that no matter how many prisoners there are, they will always have above a 30% chance of escaping using this strategy <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>. This constant probability for an arbitrarily large number of prisoners is a testament to the riddle's counterintuitive nature <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.