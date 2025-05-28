---
title: Prisoner number riddle strategy
videoId: iSNsgj1OCLA
---

From: [[veritasium]] <br/> 
The Prisoner Number Riddle is a [[Counterintuitive logic puzzles | counterintuitive]] riddle that challenges conventional understanding of probability and [[Strategies for complex problem solving | strategies]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Even when the solution is known, it can still seem incorrect <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The problem was published by computer scientist Peter Bro Miltersen <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## The Riddle Setup
One hundred prisoners, numbered 1 to 100, face a challenge <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Their corresponding numbers are randomly placed on slips of paper inside 100 sealed boxes <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Each prisoner enters a room one at a time and is allowed to open any 50 of the 100 boxes to find their own number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. After searching, they must leave the room exactly as they found it, and no communication is allowed between prisoners <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

The condition for release is that *all* 100 prisoners must find their own number <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. If even one prisoner fails, all will be executed <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The prisoners are allowed to coordinate a [[Strategies for complex problem solving | strategy]] before any of them enter the room <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## The Random Search Strategy
If each prisoner searches randomly for their number, each has a 50% chance of success <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The probability of all 100 prisoners succeeding independently is (1/2)^100 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This equates to an incredibly small probability of approximately 0.00...008 (with 30 zeros before the 8) <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. To put it in perspective, this chance is less than two people picking the same grain of sand from all the beaches and deserts on Earth <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Loop Strategy
Despite the dire odds, a [[Strategies for complex problem solving | strategy]] exists that raises their chances of success to nearly one in three <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, an improvement of roughly 30 orders of magnitude <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This [[Strategies for complex problem solving | strategy]] is not a trick question, but relies on a fundamental feature of math <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### How it Works
The [[Strategies for complex problem solving | strategy]] is as follows:
1.  When a prisoner enters the room, they open the box labeled with their own number <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  The number on the slip inside this box will likely not be their own <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  They then go to the box corresponding to the number they just found <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
4.  They continue this process – opening the box indicated by the slip they just found – until they find their own number <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
5.  Finding their own number directs them back to the box they started with, closing a loop of numbers <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
6.  If they find their number, they stop and leave the room <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

This simple [[Strategies for complex problem solving | strategy]] dramatically increases the chance of all prisoners succeeding to over 30% <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### Why the Loop Strategy Works
The core of this [[Strategies for complex problem solving | strategy]] lies in the concept of "loops" or cycles <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>. When the slips are randomly placed in the boxes, they form permutations that can always be broken down into one or more disjoint cycles (loops) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

*   **Loop Formation**: A box containing its own number is a loop of length one <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. A box pointing to another, which points back to the first, forms a loop of two <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. Loops can be any length up to 100 <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Guaranteed to be on the loop**: When a prisoner starts by opening the box with their own number, they are guaranteed to be on the loop that contains their slip <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This is because every box contains a slip, and every slip points to another box, preventing "dead ends" and forcing the formation of closed loops <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Eventually, following the chain of numbers must lead back to the starting box, which contains the prisoner's own number <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
*   **Success Condition**: A prisoner will find their number if and only if the loop their number belongs to is 50 boxes or shorter <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. If the loop is 51 boxes or longer, they will exhaust their 50 allowed searches before finding their number <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Crucially, if a loop is longer than 50, *all* prisoners whose numbers are part of that loop will fail <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **Calculating the Probability**: The probability of success for all prisoners is the probability that no loop longer than 50 exists in the random arrangement of numbers <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.
    *   The total number of ways to arrange 100 slips in 100 boxes (permutations) is 100 factorial (100!) <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   The number of unique loops of a specific length `N` is (N-1)! (because any starting point on a loop of `N` elements is the same loop, so 100! / 100 = 99! for a loop of 100) <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
    *   The [[Probability theory in problem solving | probability]] of a random arrangement containing a loop of length `L` is 1/L <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. So, the probability of a loop of length 100 is 1/100, length 99 is 1/99, and so on <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
    *   The probability of failure (a loop longer than 50) is the sum of probabilities of loops of length 51, 52, ..., up to 100: `1/51 + 1/52 + ... + 1/100` <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This sum approximates 0.69 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   Therefore, the probability of success is `1 - 0.69 = 0.31` or 31% <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

## Interdependence of Outcomes
While each prisoner still has a 50% chance of finding their number individually (since they open half the boxes) <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>, these probabilities are no longer independent when the loop [[Strategies for complex problem solving | strategy]] is employed <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. With the loop [[Strategies for complex problem solving | strategy]], either all prisoners succeed (31% of the time) or the majority fail (69% of the time), meaning the group either wins entirely or loses hard <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Success or failure is determined by the maximum loop length in the permutation, making their fates linked <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.

## Variations and Generalizations
*   **Sympathetic Guard**: If a sympathetic guard can swap the contents of just two boxes before the prisoners enter, they can guarantee success. This is done by breaking any single loop longer than 50 into two shorter loops <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
*   **Malicious Guard**: If a malicious guard tries to ensure failure by arranging the numbers to form a long loop, the prisoners can counter this by arbitrarily renumbering the boxes (e.g., adding five to each box number) <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. Renumbering the boxes is mathematically equivalent to a random redistribution of the slips, restoring their 31% chance of survival <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.
*   **Increasing Number of Prisoners**: The probability of success approaches a limit as the number of prisoners (N) increases, assuming each is allowed to open N/2 boxes <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
    *   For 1,000 prisoners checking 500 boxes, the chance of success is 30.74% <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
    *   For 1 million prisoners, it's 30.685% <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
    *   The probability of success approaches `1 - ln(2)` (natural logarithm of two), which is approximately 30.7% <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This is derived from the integral of `1/x` from `N/2` to `N` (or `n` to `2n`), which represents the sum of probabilities for loops longer than N/2 <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

Ultimately, no matter how many prisoners there are, the loop [[Strategies for complex problem solving | strategy]] ensures at least a 30% chance of escape, a result that continues to feel counterintuitive given the initial odds <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.