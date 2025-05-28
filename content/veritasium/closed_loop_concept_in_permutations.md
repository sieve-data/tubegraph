---
title: Closed loop concept in permutations
videoId: iSNsgj1OCLA
---

From: [[veritasium]] <br/> 

The [[mathematical_probability_strategies | 100 Prisoners Riddle]] is a counterintuitive problem that demonstrates a surprising mathematical strategy to significantly increase the probability of a collective success where individual chances are extremely low <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This riddle, initially posed by computer scientist Peter Bro Miltersen, reveals an "incredible feature of math" related to closed loops in permutations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## The Riddle Setup

One hundred prisoners, numbered 1 to 100, face execution unless they all find their corresponding number in a sealed room <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a> <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Slips of paper containing each prisoner's number are randomly placed into 100 boxes <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. Each prisoner enters the room one at a time and can open any 50 of the 100 boxes <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. After searching, they must leave the room exactly as they found it and cannot communicate with other prisoners <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. All 100 prisoners must find their number to be freed; if even one fails, all are executed <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. They are allowed to strategize beforehand <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Initial Probability (Random Guessing)

If each prisoner searches for their number randomly, each has a 50% chance of finding it <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The probability that all 100 succeed is (1/2)^100, which is an extremely small number (approximately 8 followed by 30 zeros) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This chance is less than two people picking the same grain of sand from all Earth's beaches <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Loop Strategy

Despite the seemingly impossible odds, a strategy exists that raises their chances to nearly one in three, an improvement by almost 30 orders of magnitude <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This [[mathematical_probability_strategies | strategy]] relies on the "closed loop concept" inherent in the arrangement of numbers <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

### How the Strategy Works

Each prisoner follows these steps:
1.  **Open the box with their own number on it.** <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>
2.  **Read the number on the slip inside.** <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>
3.  **Go to the box with that number on it.** <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>
4.  **Repeat steps 2 and 3** until they find the slip with their own number <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

If they find their number, it effectively directs them back to their starting box, closing a loop <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. They stop searching once their number is found <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. This simple strategy provides over a 30% chance of collective success <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## The Closed Loop Concept Explained

The effectiveness of this strategy stems from the fact that any random arrangement of slips within the boxes creates a series of "closed loops" or cycles <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

*   **Loop Formation:** Each box *points* to another box via the slip inside it. For example, Box 1 contains slip 7, Box 7 contains slip 23, and eventually, a box will contain slip 1, completing a loop <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. These loops can be of any length, from a single box containing its own number to a loop connecting all 100 boxes <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   **Guaranteed to be on your loop:** When a prisoner starts by opening the box labeled with their own number, they are guaranteed to be on the loop that contains their slip <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This is because every box contains a slip pointing to another box, and every slip must be contained in a box, which necessarily forms loops with no dead ends <a class="yt-timestamp" data-t="00:11:33">[00:11:33]</a> <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. A prisoner will only find their own slip when it points back to their starting box, closing the loop <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.

### Success Condition: Loop Length

The success of a prisoner depends entirely on the length of the loop their number is part of <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>:
*   If a prisoner's number is part of a loop shorter than 50, they will find their slip within their allowed 50 box openings <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   If a prisoner's number is part of a loop of length 51 or longer, they will not find their slip within 50 attempts <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.
*   Crucially, if a loop is too long (e.g., 51 boxes), *all* prisoners whose numbers are part of that particular loop will fail <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

Therefore, for all prisoners to succeed, **no loop in the arrangement of slips can be longer than 50** <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Calculating the Probability of Success

The total number of ways to arrange 100 slips in 100 boxes (permutations) is 100 factorial (100!) <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
The number of unique loops of length N is (N-1)! (because N! permutations form N different starting points for the same loop) <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
The probability of a random arrangement containing a loop of length N is 1/N <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

Using this general result:
*   The probability of a loop of length 100 is 1/100 <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   The probability of a loop of length 99 is 1/99 <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.

The probability of failure is the probability that there is *any* loop longer than 50. This is the sum of probabilities for loops of length 51, 52, ..., up to 100 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>:
P(Failure) = (1/51) + (1/52) + ... + (1/100) <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
This sum equals approximately 0.69 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
Therefore, the probability of success is 1 - 0.69 = **0.31 (31%)** <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

> [!NOTE] Individual vs. Collective Probability
> While the collective probability of success dramatically increases with this strategy, the individual probability of each prisoner finding their number *if they were acting alone* is still 50% <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>. The key is that the outcomes are no longer independent; the prisoners either *all* win or the *majority* loses together, determined by the longest loop <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a> <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

## External Factors and Scaling

### Sympathetic or Malicious Guards
*   **Sympathetic Guard:** A guard could guarantee success by swapping the contents of just two boxes if there's a loop longer than 50, effectively breaking it into two shorter loops (both less than 50) <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>. Since there can be at most one loop longer than 50, this always works <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
*   **Malicious Guard:** If a malicious guard tried to doom the prisoners by ensuring a long loop, the prisoners could counter by arbitrarily renumbering the boxes (e.g., adding 5 to each box number) <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>. Renumbering the boxes is mathematically equivalent to redistributing the slips randomly, returning the prisoners to their 31% chance of survival <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

### Increasing the Number of Prisoners
Surprisingly, as the number of prisoners (N) and the number of allowed box openings (N/2) increases, the probability of success does not drop significantly <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
*   For 1,000 prisoners checking 500 boxes, the chance of success is 30.74% <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   For 1 million prisoners, it's 30.685% <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

The probability of winning this game approaches a limit as the number of prisoners goes to infinity <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. The formula for the probability of success is 1 minus the sum of (1/k) for k from (N/2 + 1) to N <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. This sum can be approximated by the integral of 1/X from N/2 to N <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
The integral of 1/X is the natural logarithm of X (ln(X)) <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.
The result is ln(N) - ln(N/2) = ln(N / (N/2)) = ln(2) <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
So, the probability of failure approaches ln(2) <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
The probability of success approaches **1 - ln(2)**, which is approximately **30.7%** <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

This demonstrates that no matter how large the number of prisoners, using this strategy maintains a chance of success above 30% <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>. The beauty of the loop strategy lies in linking everyone's outcomes, transforming independent 50-50 shots into a collective win-or-lose scenario <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.