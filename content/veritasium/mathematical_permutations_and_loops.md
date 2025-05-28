---
title: Mathematical permutations and loops
videoId: iSNsgj1OCLA
---

From: [[veritasium]] <br/> 

The 100 Prisoners Riddle is a [[mathematical_reasoning_and_coin_rotation_paradox | counterintuitive riddle]] that often seems incorrect even when the solution is known, confusing many people <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It's a problem that demonstrates an incredible feature of math <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. The riddle was devised by computer scientist Peter Bro Miltersen, who initially didn't conceive of the optimal strategy himself <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

## The Riddle Setup

The riddle involves 100 prisoners, numbered 1 to 100 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Slips of paper, each containing one of their numbers, are randomly placed into 100 boxes in a sealed room <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

Each prisoner is allowed to enter the room one at a time <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. They can open any 50 of the 100 boxes to search for their number <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. After searching, they must leave the room exactly as they found it, and they cannot communicate with other prisoners <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

The condition for release is strict: if all 100 prisoners find their own number during their turn, they will all be freed <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. However, if even one prisoner fails to find their number, all will be executed <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The prisoners are permitted to strategize *before* anyone enters the room <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

## Probability with a Random Strategy

If each prisoner searches randomly for their number, each has a 50% chance of finding it <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The [[Probability theory in problem solving | probability]] that all 100 prisoners succeed is calculated as 1/2 multiplied by itself 100 times, or (1/2)^100 <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This results in an extremely low probability of approximately 0.000... (30 zeros) ...8 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. To put this in perspective, two people have a better chance of picking the same grain of sand from all the beaches and deserts on Earth than escaping this way <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

However, with the right strategy, their chances can be raised to nearly one in three, improving their odds by almost 30 orders of magnitude <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## The Loop Strategy

The optimal strategy involves a specific sequence of opening boxes:
1.  When a prisoner enters the room, they first open the box with their own number on it <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
2.  The slip inside this box will likely not be their number, but it will have another prisoner's number <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
3.  They then go to the box with *that* number on it <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
4.  They continue this process – opening the box indicated by the number on the slip they just found – until they find the slip with their own number <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
5.  If they find their number, it effectively directs them back to their starting box, closing a loop, and they are done <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

This strategy gives the prisoners over a 30% chance of success collectively <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.

## How the Strategy Works: Permutation Cycles

The key to understanding this strategy lies in how the random placement of slips in boxes forms "loops" or permutation cycles <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
*   A "loop of one" occurs if a box contains its own number (e.g., box 1 contains slip 1) <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
*   Longer loops can form, such as box 1 pointing to box 7, and box 7 pointing back to box 1 (a loop of two) <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   Any random arrangement of slips results in a mixture of shorter and longer loops <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

When a prisoner starts by opening the box labeled with their own number, they are guaranteed to be on the loop that includes their slip <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. The success of a prisoner depends entirely on the length of this loop <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>:
*   If the prisoner's number is part of a loop shorter than 50, they will definitely find their slip within their allotted 50 box openings <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   If the prisoner's number is part of a loop that is 51 or longer, they will not find it before exhausting their 50 searches <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Crucially, if a loop is 51 or longer, *all* prisoners whose numbers are part of that specific loop will fail <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. Therefore, the prisoners succeed if and only if no loops longer than 50 are formed by the arrangement of slips <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

### Why a Prisoner is Guaranteed to Find Their Slip on Their Loop

A common question is how a prisoner is guaranteed to be on the correct loop <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. This is because every slip is contained within a box, and every box contains a slip, preventing dead ends <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>. The slips and boxes with matching numbers (e.g., slip 73 and box 73) form a unit, and by starting at their own numbered box, a prisoner is implicitly initiating a traversal of the unique cycle that their number belongs to <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. The process continues until the slip for the starting box's number is found, which closes the loop <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

## Calculating the Probability of Success

The [[Probability theory in problem solving | probability]] of success is the probability that a random arrangement of 100 numbers contains no loops longer than 50 <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

### Number of Permutations and Unique Loops
The total number of ways to arrange 100 slips in 100 boxes (permutations) is 100 factorial (100!) <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
However, since these are loops, a sequence like "1, 2, 3... 100" is the same loop as "2, 3... 100, 1" <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. There are 100 different ways to write the same loop of length 100 <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
So, the number of unique loops of length 100 is 100! / 100 <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

### Probability of a Specific Loop Length
The [[Probability theory in problem solving | probability]] that a random arrangement of 100 slips forms a loop of length 100 is (100! / 100) / 100!, which simplifies to 1/100 <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. This is a general result: the probability of getting a loop of length `N` in a set of `N` items is 1/N <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Total Probability of Failure/Success
The probability that there is a loop *longer* than 50 is the sum of the probabilities of having loops of length 51, 52, up to 100 <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>:
1/51 + 1/52 + 1/53 + ... + 1/100 <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
This sum equals approximately 0.69, meaning there is a 69% chance of failure for the prisoners <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
Consequently, the chance of success is 1 - 0.69 = 0.31, or 31% <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

While each individual prisoner still has a 50% chance of finding their number because they can only open half the boxes <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, these probabilities are no longer independent <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. With the loop strategy, either all prisoners succeed (31% of the time) or the majority fail (69% of the time) <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

## External Influences

### Sympathetic Guard
If a sympathetic prison guard were to sneak into the room before the prisoners, they could guarantee success <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. This is possible because there can be at most one loop longer than 50 <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. By simply swapping the contents of just two boxes within that long loop, the guard can break it into two separate loops, each shorter than 50 <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

### Malicious Guard
If a malicious guard knew the prisoners' loop strategy, they could arrange the slips to ensure a loop longer than 50 forms, dooming the prisoners <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. However, the prisoners can counter this by arbitrarily renumbering the boxes beforehand <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. Renumbering the boxes is mathematically equivalent to redistributing the slips, effectively restoring the problem to a random arrangement of loops and giving the prisoners back their 31% chance of survival <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

## Scaling the Problem to [[Infinity in mathematics | Infinite Prisoners]]

Surprisingly, if the number of prisoners increases, the probability of success using this strategy does not drop dramatically <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
*   For 1,000 prisoners, each checking 500 boxes, the chance of success is 30.74% <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   For 1 million prisoners, it's 30.685% <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

The probability of winning approaches a limit as the number of prisoners (`N`) tends to [[Infinity in mathematics | infinity]] <a class="yt-timestamp" data-t="00:14:31">[00:14:31]</a>. The formula for the probability of failure (the sum of 1/X for X from N/2+1 to N) can be approximated by the integral of 1/X from N/2 to N <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. This integral evaluates to the natural logarithm of two (ln(2)) <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

Therefore, the probability of success approaches `1 - ln(2)`, which is approximately 30.7% <a class="yt-timestamp" data-t="00:15:25">[00:15:25]</a>. This means no matter how large the number of prisoners, the chance of escaping using this strategy will always be above 30% <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

## Conclusion

The loop strategy is powerful because it links everyone's outcomes together <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>. Instead of each prisoner having an independent 50-50 chance, their success becomes entirely dependent on the overall configuration of the loops formed by the slips <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. This strategy results in an all-or-nothing outcome: either all prisoners find their numbers (100% success for the group) or a significant portion fail (0% success for the group) <a class="yt-timestamp" data-t="00:16:17">[00:16:17]</a>.

> [!NOTE] Learn More!
> If you enjoy solving puzzles like the 100 Prisoners Riddle, consider exploring resources like Brilliant.org. They offer interactive courses on topics like perplexing probability and the joy of problem-solving, which delve into similar mathematically inclined puzzles and concepts <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>. You can check them out at brilliant.org/veritasium for a discount <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.