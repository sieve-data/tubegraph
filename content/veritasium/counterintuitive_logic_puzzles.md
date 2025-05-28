---
title: Counterintuitive logic puzzles
videoId: iSNsgj1OCLA
---

From: [[veritasium]] <br/> 
The [[prisoner_number_riddle_strategy | 100 Prisoners Riddle]] is a logic puzzle considered so [[counterintuitive_engineering_concepts | counterintuitive]] that it "still seems wrong even if you know the answer" <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It is a problem that tests one's [[mathematical_reasoning_and_coin_rotation_paradox | mathematical reasoning]] and understanding of [[probability_theory_in_problem_solving | probability theory]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. The solution involves an "incredible feature of math" <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## The Riddle Setup

One hundred prisoners, numbered 1 to 100, face a challenge <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.
*   Slips of paper, each containing one of their numbers, are randomly placed in 100 sealed boxes within a room <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   Each prisoner, one at a time, enters the room and can open any 50 of the 100 boxes, searching for their number <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.
*   After searching, they must leave the room exactly as they found it, and they cannot communicate with other prisoners <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Success Condition**: If all 100 prisoners find their own number during their turn, they are all freed <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   **Failure Condition**: If even one prisoner fails to find their number, they are all executed <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **Pre-Strategy**: The prisoners are allowed to strategize before any of them enters the room <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Initial Probability: Random Guessing

If each prisoner searches for their number randomly, each has a 50% chance of finding it <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The probability that all 100 prisoners succeed is (1/2) multiplied by itself 100 times, or (1/2)^100 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This results in an incredibly small probability: 0.000... (30 zeros) ...8 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This chance is less than two people picking the same grain of sand from all Earth's beaches and deserts <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

## The Counterintuitive Strategy

Despite the seemingly impossible odds, a specific strategy can raise their chances of success to nearly one in three <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. This improves their odds by almost 30 orders of magnitude <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. This riddle was devised by computer scientist Peter Bro Miltersen, who himself didn't think of the strategy until a colleague pointed it out <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

### The Loop Strategy

The optimal strategy for the prisoners is as follows:
1.  When a prisoner enters the room, they open the box labeled with their own number <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  If the slip inside is not their number, they go to the box labeled with the number they just found <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
3.  They continue this process – opening the box matching the number on the slip they just found – until they find their own number <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
4.  If they find their number, they stop and leave the room <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

This strategy leads to "over a 30% chance that all the prisoners will find their number" <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

### How the Loop Strategy Works

The key insight is that any random arrangement of slips in boxes forms one or more "loops" <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   A "loop of one" occurs if a box contains its own number (e.g., box 1 contains slip 1) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   Longer loops occur when boxes point to other boxes in a sequence that eventually returns to the starting box (e.g., box 1 points to 7, box 7 points to 1) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Any random arrangement of slips will result in a mixture of shorter and longer loops <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

When a prisoner starts by opening the box labeled with their own number, they are guaranteed to be on the loop that includes their slip <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This is because every box contains a slip that points to another box, creating a chain that must eventually close into a loop <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

The success of a prisoner depends on the length of the loop their number is part of <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   If a prisoner's number is part of a loop shorter than 50 (the maximum number of boxes they can open), they will find their slip <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   If a prisoner's number is part of a loop that is 51 or longer, they will not find their number within the allowed 50 box openings <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Crucially, if a loop is longer than 50, *all* prisoners whose numbers are part of that long loop will fail <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

### Calculating the Probability of Success

The probability that all prisoners succeed is the probability that a random arrangement of 100 numbers contains no loops longer than 50 <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

1.  **Total Permutations**: There are 100! (100 factorial) different ways to arrange the 100 slips in the 100 boxes <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
2.  **Unique Loops of Length N**: The total number of unique loops of length N (e.g., 100) is N! / N, because each loop can be written N different ways while remaining the same loop <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
3.  **Probability of a Specific Loop Length**: The probability that a random arrangement contains a loop of a specific length 'L' (e.g., 100) is (L! / L) / 100! = 1/L <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>.
    *   Probability of a loop of length 100 is 1/100 <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
    *   Probability of a loop of length 99 is 1/99 <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
    *   And so on.
4.  **Probability of Failure**: The prisoners fail if there is *any* loop longer than 50. This is the sum of the probabilities of loops of length 51, 52, ..., up to 100 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>:
    1/51 + 1/52 + ... + 1/100
    This sum approximately equals 0.69 <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
5.  **Probability of Success**: The probability of success is 1 minus the probability of failure: 1 - 0.69 = 0.31 or 31% <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

## Key Insights

*   **Individual vs. Collective Probability**: While each prisoner still individually has a 50% chance of finding their number (since they can only open half the boxes), these probabilities are no longer independent <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Linked Outcomes**: The loop strategy links everyone's outcomes <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. The prisoners either "all win together or the majority loses together" <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. Once the boxes are arranged, each prisoner's chance of finding their number is either 100% or 0% <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

> "I still find it difficult to believe." <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>
> "This feels a bit like magic." <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>

## Variations and Extensions

### Sympathetic Prison Guard

If a sympathetic guard were to sneak into the room before the prisoners, they could guarantee success by swapping the contents of just two boxes <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. This is because there can be at most one loop longer than 50, and swapping two box contents breaks that long loop into two shorter loops, both less than 50 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

### Malicious Prison Guard

If a malicious guard knows the prisoners will use the loop strategy and arranges the numbers to ensure a loop longer than 50, the prisoners are still not doomed <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. They can counter by arbitrarily renumbering the boxes (e.g., adding five to each box number) <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Renumbering boxes is equivalent to redistributing the slips, effectively restoring the problem to a random arrangement of loops, bringing their chance of survival back to 31% <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

### Scaling to More Prisoners

The probability of success changes very little even with a much larger number of prisoners:
*   For 1,000 prisoners (each checking 500 boxes), the chance of success is 30.74% <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   For 1 million prisoners, it's 30.685% <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

The probability of winning this game approaches a limit as the number of prisoners increases <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. The formula for the probability of failure (the sum of 1/N for N from 51 to 100) approximates the integral of 1/X from n to 2n <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. This integral evaluates to the natural logarithm of two (ln(2)) <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

Therefore, the probability of success approaches 1 - ln(2), which is approximately 30.7% <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This means that no matter how many prisoners there are, using this [[prisoner_number_riddle_strategy | strategy]], they will always have at least a 30% chance of escaping <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

The problem, described as a [[strategies_for_complex_problem_solving | complex problem solving]] exercise, offers a "delightful math puzzle" <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. Resources like Brilliant offer courses on [[probability_theory_in_problem_solving | perplexing probability]] and the joy of problem solving for those interested in similar [[counterintuitive_engineering_concepts | counterintuitive]] riddles <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.