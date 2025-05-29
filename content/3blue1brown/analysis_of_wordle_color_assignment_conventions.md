---
title: Analysis of Wordle color assignment conventions
videoId: fRed0Xmc2Wg
---

From: [[3blue1brown]] <br/> 

This article addresses a correction regarding a slight bug in code used to analyze [[Wordle game mechanics | Wordle]] performance, specifically concerning [[bug_identification_and_its_impact_on_wordle_algorithm | bug identification and its impact on Wordle algorithm]] related to how the game assigns colors to guesses <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This bug affected the accuracy of [[algorithms_for_optimal_wordle_play | algorithms for optimal Wordle play]] and their performance testing <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## The Bug in Color Assignment

The identified bug related to how a color is assigned to a guess containing multiple instances of the same letter <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. It was a subtle error, affecting only a small percentage of cases, making it easy to miss and leading to only a slight overall effect <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The mistake originated from an attempt to speed up computations, which involved a "trick" for calculating the pattern value between word pairs that introduced a slight, unthought-through change <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

### Wordle Color Conventions Explained

Wordle's conventions for coloring letters, particularly duplicate letters in a guess, follow specific rules:

*   **Guess: "speed", True Answer: "abide"**
    In this scenario, the first 'e' in "speed" would be colored yellow, indicating it's in the word but in a different position. The second 'e' would be colored gray, signaling that there is no second 'e' in the true answer "abide" <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
    > "the first e would be colored yellow, and the second one would be colored gray." <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>

*   **Guess: "speed", True Answer: "erase"**
    If the true answer contains multiple instances of a guessed letter, both instances in the guess are colored yellow (if they are in different locations). For example, if the answer is "erase", both 'e's in "speed" would be yellow, indicating two 'e's exist in the word at different positions <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
    > "both of those e's would be colored yellow, telling you that there is a first e in a different location, and there's a second e also in a different location." <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>

*   **Green Hit Scenarios**
    If one of the guessed letters hits the correct position and is colored green, the treatment of subsequent duplicate letters depends on the true answer:
    *   If the true answer has no second instance of that letter, the second guessed letter would be gray <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.
    *   If the true answer does have a second instance of that letter, but in a different location, the second guessed letter would be yellow <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

### Impact on Analysis

While the core lessons about [[information_theory_and_entropy_in_Wordle | information theory and entropy in Wordle]] remained unaffected <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, the bug could slightly alter displayed distributions for words, as certain pattern "buckets" might have incorrectly counted true answers <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

Crucially, the bug influenced the conclusion regarding [[optimal_wordle_opening_guesses_and_their_analysis | optimal Wordle opening guesses]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The previous video's claim that "crane" was the best opening guess was based on [[algorithms_for_optimal_wordle_play | algorithms]] playing a slightly different game due to this bug <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. After correction and rerunning the [[algorithms_for_optimal_wordle_play | algorithms]], a different theoretically optimal first guess emerged <a class="yt-timestamp" data-t="00:02:53">[00:02:56]</a>.