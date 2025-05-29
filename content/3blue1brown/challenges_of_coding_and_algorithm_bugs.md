---
title: Challenges of coding and algorithm bugs
videoId: fRed0Xmc2Wg
---

From: [[3blue1brown]] <br/> 

## The Discovery of a Bug

In a previous video attempting to solve Wordle using information theory, a "very slight bug" was discovered in the code used to recreate the game and test algorithms <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This bug was easy to miss because it affected only a small percentage of cases and had only a slight effect on overall performance <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

### Nature of the Bug: Wordle Color Assignment

The bug primarily concerned how colors are assigned to a guess containing multiple instances of the same letter <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

*   **Example 1: Guess "speed", True Answer "abide"**
    *   According to Wordle conventions, the first 'e' would be yellow (matching a letter in a different position), and the second 'e' would be gray (indicating no second 'e' exists in the answer) <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **Example 2: Guess "speed", True Answer "erase"**
    *   Both 'e's would be colored yellow, indicating two 'e's in different locations <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Example 3: One 'e' is green (correct position)**
    *   If the first 'e' hits as green, the second 'e' would be gray if no second 'e' exists in the true answer <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   However, if a second 'e' *does* exist in a different location, the second 'e' in the guess would be yellow <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

The bug caused the code to deviate slightly from these standard Wordle conventions <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

### Cause of the Bug

The mistake stemmed from an attempt to optimize computations. To speed up the calculation of pattern values between word pairs, a "trick" was implemented without sufficient consideration, leading to the slight change in behavior <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Ironically, the most efficient method ultimately involved pre-computing all patterns, rendering the speed of individual computations irrelevant and making the complex, buggy code unnecessary <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This highlights a common pitfall in [[practical_implementation_of_error_correction_algorithms | practical implementation of algorithms]]: premature optimization can introduce errors.

## Impact and Lessons Learned

Despite the bug, the main lessons of the original video, such as the concepts of information and entropy, remained unaffected <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The visual distributions shown in the video might have been slightly inaccurate in some cases due to incorrect bucket assignments for patterns <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>, but this was rare due to the specific edge case involved <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

The most significant impact of the bug was on the conclusion regarding the theoretically optimal opening guess for Wordle <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. Initially, "crane" was identified as the best opener, but this was based on the algorithms playing a slightly different game due to the bug <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. After fixing the bug, a different optimal answer emerged <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

The experience served as a reminder that "you live and you learn" <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. This situation also underscores the importance of understanding the limitations of algorithms. Even when using a greedy approach, like maximizing expected information, it may not lead to the globally optimal solution without deeper searches or simulations <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This reflects broader [[problemsolving_strategies_in_mathematical_puzzles | problem-solving strategies]] and the nuances of algorithmic design, distinguishing between [[human_vs_algorithmic_gameplay_differences | human intuition]] and machine-driven exhaustive searches.