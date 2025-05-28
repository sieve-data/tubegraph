---
title: Mathematical probability strategies
videoId: iSNsgj1OCLA
---

From: [[veritasium]] <br/> 

Some riddles are so counter-intuitive that their solutions still seem wrong even after knowing the answer <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This phenomenon can apply to [[probability_calculations_and_mathematical_strategies | mathematical probability strategies]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## The 100 Prisoners Riddle: Setup

The setup for this famous riddle involves 100 prisoners, numbered 1 to 100 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Slips of paper, each containing one of their numbers, are [[random_number_selection | randomly placed]] into 100 boxes in a sealed room <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   One at a time, each prisoner enters the room <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   They are allowed to open any 50 of the 100 boxes to search for their number <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
*   After searching, they must leave the room exactly as they found it <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   No communication between prisoners is allowed <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.
*   **The Goal:** If all 100 prisoners find their own number during their turn, they are all freed <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. If even one prisoner fails, all are executed <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **The Advantage:** Prisoners are allowed to strategize together before anyone enters the room <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Initial Probability (Random Guessing)

If prisoners were to search for their numbers randomly, each prisoner would have a 50% chance of finding their number <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The [[probability_calculations_and_mathematical_strategies | probability]] that all 100 prisoners find their numbers would be (1/2) multiplied by itself 100 times, or (1/2)^100 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This calculates to an extremely small number: 0.00... (30 zeros) ...8 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This chance is less than two people picking the same grain of sand from all beaches and deserts on Earth <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Loop Strategy

Despite the seemingly impossible odds, a specific [[probability_calculations_and_mathematical_strategies | mathematical strategy]] can increase the prisoners' chance of success to nearly one in three, improving their odds by almost 30 orders of magnitude <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This riddle was devised by computer scientist Peter Bro Miltersen, who initially did not conceive of this solution himself <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### How it Works

The solution involves an incredible feature of math <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.
1.  When a prisoner enters the room, they first open the box labeled with their own number <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  They then look at the number on the slip inside that box <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  They proceed to the box labeled with that number <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
4.  They continue this process – opening the box indicated by the number on the slip they just found – until they find the slip with their own number <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
5.  If they find their number, it effectively directs them back to the box where they started, closing a loop of numbers <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
6.  Once they find their number, they stop searching and leave the room <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

This seemingly simple strategy results in over a 30% chance for all prisoners to find their numbers <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### Mathematical Explanation: The Loops

The effectiveness of the strategy relies on the concept of "loops" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   Any random arrangement of slips within the boxes will form one or more closed loops <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   A "loop of one" occurs if a box contains its own number <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   Longer loops can connect two, three, or up to all 100 numbers <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   When a prisoner starts by opening the box labeled with their number, they are guaranteed to be on the loop that contains their slip <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   A prisoner will find their slip if and only if their number is part of a loop that is shorter than or equal to 50 boxes <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   If a prisoner's number is part of a loop that is 51 boxes or longer, they will not find their number within the allowed 50 box openings <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. In this scenario, all prisoners on that particular long loop will fail <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

#### Calculating the Probability of Success

The probability that all prisoners succeed is equivalent to the probability that a random arrangement of 100 numbers contains no loops longer than 50 <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

To calculate this:
1.  **Total Permutations:** The total number of ways to arrange 100 slips in 100 boxes is 100 factorial (100!) <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
2.  **Unique Loops of Length N:** The number of unique loops of length N is (N-1)! (because there are N ways to write a loop of N numbers, so N! permutations divided by N) <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
3.  **Probability of a Single Long Loop:** The probability that a random arrangement of 100 boxes will contain a loop of a specific length (e.g., 100) is the number of unique loops of that length divided by the total number of permutations <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. For a loop of length 100, this is (100! / 100) / 100! = 1/100 <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. This is a general result: the probability of getting a loop of length N is 1/N <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
4.  **Probability of Failure:** The probability that there is a loop longer than 50 is the sum of probabilities for loops of length 51, 52, up to 100 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>:
    *   1/51 + 1/52 + 1/53 + ... + 1/100 <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
    *   This sum equals approximately 0.69 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   Therefore, there is a 69% chance of failure for the prisoners <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
5.  **Probability of Success:** The chance of success is 1 minus the chance of failure <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>:
    *   1 - 0.69 = 0.31, or 31% <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Why the Loop Strategy Works

A common question is: "How do you know that if you start with a box with your number on it, you are guaranteed to be on the loop that contains your slip?" <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   Every slip is hidden inside another box <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.
*   This arrangement ensures that there are no "dead ends" where a box does not point to another <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.
*   Every box contains a slip that points to another box, which necessarily forms loops <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.
*   When a prisoner starts with the box labeled with their number, they must eventually find their slip, as finding that slip is the only way to be directed back to their starting box, thus closing the loop they are on <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

## Manipulating the Problem

### Sympathetic Guard
If a sympathetic prison guard could sneak into the room before the prisoners, they could guarantee success by swapping the contents of just two boxes <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. This is because there can be at most one loop longer than 50 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. Swapping two boxes can break this long loop into two shorter loops, each less than 50 <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Malicious Guard
If a malicious guard knew the prisoners' loop strategy, they could arrange the slips to ensure a loop longer than 50 <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. However, the prisoners can counter this by arbitrarily renumbering the boxes (e.g., adding five to each box number) <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Renumbering the boxes is mathematically equivalent to redistributing the slips, effectively restoring the problem to a random arrangement of loops <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This returns the prisoners to their 31% chance of survival <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.

## Scaling the Problem: Approaching a Limit

The probability of success for the prisoners does not drop dramatically as the number of prisoners increases <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   For 1,000 prisoners (each checking 500 boxes), the chance of success is 30.74% <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   For 1 million prisoners, it's 30.685% <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
*   The probability of winning this game approaches a limit <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>.

The formula for the probability of failure (sum of 1/N for loops longer than N/2) can be represented as a [[mathematical_series_expansion | series]] of rectangles, whose area is approximated by the integral of 1/x <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. As the number of prisoners approaches infinity, this approximation becomes more accurate <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.
*   The integral of 1/x from n to 2n (where n is the number of boxes checked, and 2n is the total number of boxes) is equal to the natural logarithm of two (ln 2) <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
*   Thus, the probability of success approaches 1 - ln 2 <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>.
*   1 - ln 2 ≈ 1 - 0.693 = 0.307 or 30.7% <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

This demonstrates that no matter how many prisoners are involved, the [[probability_calculations_and_mathematical_strategies | probability]] of escaping using this strategy will always remain above 30% <a class="yt-timestamp" data-t="00:15:33">[00:15:33]</a>.

## Conclusion

The beauty of the loop strategy lies in its ability to link everyone's outcomes together <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. Instead of each prisoner having an independent 50% chance, the strategy ensures that all prisoners within a loop have the same chance of finding their number <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. Once the boxes and slips are arranged, their chance is either 100% or 0% <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. This strategy means that success is complete for all, or failure affects the majority <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

## Further Learning

For those interested in similar perplexing [[probability_calculations_and_mathematical_strategies | probability]] puzzles and delightful math problems, resources like Brilliant offer courses such as "Perplexing Probability" and "Joy of Problem Solving" <a class="yt-timestamp" data-t="00:16:55">[00:16:55]</a>.