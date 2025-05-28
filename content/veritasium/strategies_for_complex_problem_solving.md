---
title: Strategies for complex problem solving
videoId: iSNsgj1OCLA
---

From: [[veritasium]] <br/> 

The **100 Prisoners Riddle** is a well-known [[Counterintuitive logic puzzles | counterintuitive logic puzzle]] that demonstrates how a sophisticated strategy can dramatically improve the odds of success in a seemingly impossible situation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## The Riddle Setup

One hundred prisoners, numbered 1 to 100, face a challenge <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. In a sealed room, 100 boxes contain slips of paper, each bearing one of the prisoners' numbers (1 to 100) randomly placed <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Each prisoner enters the room one at a time and is allowed to open any 50 of the 100 boxes <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. After searching, they must leave the room exactly as they found it <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. No communication is permitted between prisoners <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

The condition for release is strict: all 100 prisoners must find their own number during their turn <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. If even one fails, all are executed <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The prisoners are allowed to strategize beforehand <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Initial Probability (Random Guessing)

If each prisoner searches randomly, they each have a 50% chance of finding their number <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The probability of all 100 prisoners succeeding is (1/2) multiplied by itself 100 times, or 1/2^100 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This probability is approximately 0.000... (30 zeros) ...8 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. To put it in perspective, it's a lower chance than two people picking the same grain of sand from all beaches and deserts on Earth <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Loop Strategy

Despite the seemingly impossible odds, a strategy exists that increases their chance of success to nearly one in three <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This represents an improvement by nearly 30 orders of magnitude <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This riddle was conceived by computer scientist Peter Bro Miltersen, who himself didn't initially think of the solution <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### Strategy Steps

Each prisoner follows these steps:
1.  Open the box labeled with your own prisoner number <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
2.  The slip inside will likely contain a different number <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  Go to the box labeled with the number found on the slip <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
4.  Repeat this process: open the box corresponding to the number on the slip you just found <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
5.  Continue until you find the slip with your own number <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. If found, you are done and leave the room <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

This simple strategy results in over a 30% chance for all prisoners to find their numbers <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## How the Strategy Works: Permutation Cycles

The core of the strategy lies in the concept of permutation cycles. When slips are randomly placed in boxes, they form closed loops or cycles <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   A "loop of one" occurs if a box contains its own number (e.g., box 1 contains slip 1) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   "Loops of two" involve two boxes pointing to each other (e.g., box 1 points to box 7, and box 7 points to box 1) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Cycles can be of any length up to 100 <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   Any random arrangement of slips will result in a mixture of shorter and longer loops <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

When a prisoner starts by opening the box labeled with their number, they are guaranteed to be on the loop that contains their slip <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This is because every box contains a slip, and every slip points to another box, creating an unbroken chain that must eventually loop back <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.

### The Role of Loop Length

A prisoner will find their number if and only if their number is part of a loop shorter than or equal to 50 <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. If their number is part of a loop 51 or longer, they will not find it within their allowed 50 box openings <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Crucially, if a loop is longer than 50 (e.g., 51 numbers), all prisoners whose numbers are part of that loop will fail <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This means the prisoners either all win together or the majority loses together, linking their fates <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

## Calculating the Probability of Success

The probability of all prisoners succeeding is the probability that a random arrangement of 100 numbers contains no loops longer than 50 <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

To understand this probability, consider the number of ways to arrange 100 slips in 100 boxes: this is 100 factorial (100!) <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>. The number of unique loops of length 100 is 100! / 100 <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Therefore, the probability that a random arrangement results in a loop of length 100 is (100! / 100) / 100! = 1/100 <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.

This is a general result: the probability of getting a loop of length 'k' is 1/k <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

The probability that there *is* a loop longer than 50 is the sum of probabilities for loops of length 51, 52, up to 100:
1/51 + 1/52 + 1/53 + ... + 1/100 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
This sum approximates 0.69 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
So, there is approximately a 69% chance of failure for the prisoners, meaning a 31% chance of success (1 - 0.69) <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

### Scalability and Limit

The effectiveness of this strategy holds true even for a large number of prisoners <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   For 1,000 prisoners (each checking 500 boxes), the chance of success is 30.74% <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   For 1 million prisoners, the probability of success is 30.685% <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

The probability of winning this game approaches a limit as the number of prisoners (N) and the number of allowed box openings (N/2) increases <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. The sum 1/51 + ... + 1/100 is an approximation of the integral of 1/X from N/2 to N <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. This integral evaluates to the natural logarithm of two (ln(2)) <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

Therefore, the probability of success approaches 1 - ln(2), which is approximately 30.7% <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This means no matter how many prisoners there are, they will always have at least a 30% chance of escaping using this strategy <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

## Mitigating External Interference

### Sympathetic Guard
If a sympathetic guard swaps the contents of just two boxes, they can guarantee success for the prisoners <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. This is because there can be at most one loop longer than 50 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. Swapping two slips breaks this long loop into two shorter loops, each now shorter than 50 <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Malicious Guard
If a malicious guard arranges the slips to ensure a loop longer than 50 (thereby dooming the prisoners), the prisoners can counter this <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. They can arbitrarily renumber the boxes (e.g., adding five to each box number) <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Renumbering the boxes effectively redistributes the slips from the prisoners' perspective, returning the problem to a random arrangement of loops and restoring their 31% chance of survival <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

## Conclusion

The loop strategy illustrates a powerful concept in [[Probability theory in problem solving | probability theory in problem solving]] and [[Strategies and Challenges in Solving Collatz Conjecture | strategies for complex problem solving]]: by linking individual outcomes, a collective probability of success can be dramatically improved, even if individual probabilities remain unchanged <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. Instead of 100 independent 50-50 shots, the strategy ensures that all prisoners within a cycle succeed or fail together <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>. This means the outcome is either complete success or widespread failure, eliminating scenarios where only a few prisoners miss their numbers <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.