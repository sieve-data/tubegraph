---
title: Human vs algorithmic gameplay differences
videoId: fRed0Xmc2Wg
---

From: [[3blue1brown]] <br/> 

When analyzing games like Wordle, a distinction can be made between how algorithms approach problem-solving and how humans typically play. Algorithms are designed for optimal performance within a defined ruleset and data environment, while human play often relies on intuition, general knowledge, and adaptability.

## Algorithmic Approach to Wordle

Initially, an attempt was made to solve the game Wordle using [[information_theory_in_gamesolving | information theory]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This involved developing an algorithm to identify the best opening guesses and subsequent plays based on maximizing information gain.

### Overfitting and Test Sets
The first iteration of the algorithm aimed to build something "resilient" by *not* using the official list of all possible answers, as this felt like "overfitting to a test set" <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Instead, it considered relative word frequencies in the English language <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

However, for determining an "absolute best performance," the official Wordle answer list was incorporated, which is described as "shamelessly overfitting to the test set" <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This allows the algorithm to assign uniform probabilities to each word, knowing with certainty whether it is included <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Algorithmic Optimization and Bugs
Algorithms quantify information by calculating the likelihood of patterns for a given guess and using a formula involving a logarithmic expression to measure how much the possibility space is cut down <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

A slight bug in the code used to recreate Wordle and test algorithms affected a small percentage of cases, leading to a minor deviation from the correct Wordle conventions <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. This bug related to how colors were assigned to guesses with multiple identical letters <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Despite the minor nature of the bug, it significantly altered the conclusion about the theoretically optimal opening guess <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This highlights [[challenges_of_coding_and_algorithm_bugs | challenges of coding and algorithm bugs]].

After fixing the bug, the algorithmic analysis of the optimal first guess for the specific Wordle answer list changed:
*   **One-step expected information:** The word "soar" was initially found to have the highest expected information <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
*   **Two-step expected information:** By conducting an exhaustive search two steps in, 'slain' rose to the top as the best opener based on expected information after two steps <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Lowest average score (simulation):** By simulating all possible Wordle games with the top 250 openers, the word 'Salé' (an alternate spelling for a light medieval helmet) was found to yield the lowest average score <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>, <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. 'Trace' and 'crate' also provided almost identical performance and were actual Wordle answers <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Human vs. Algorithmic Play

The "optimal opener" identified by algorithms is *not* the best opener for a human player <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### Key Differences:
*   **Memorization and Search:** Humans do not have the entire word list memorized and cannot perform exhaustive searches through thousands of possibilities for each turn <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>, <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Optimal Subsequent Guesses:** For a human to benefit from an algorithmically optimal first guess, they would also need to know the optimal second guess for every possible pattern they might see <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Overfitting to Data:** Algorithms are "absurdly overfit" to the official Wordle answer list <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. If this list changes, the algorithm's strategy would become invalid <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. Humans, by contrast, rely on general language intuition <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Intuition vs. Calculation:** Humans gain intuition from factors like vowel placement, rather than brute-force calculations <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
*   **Purpose:** For humans, the game remains a fun word game <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. The point of writing algorithms for games is not to dictate human play, but to refine skills for writing algorithms in more meaningful contexts <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>, <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

The process of finding an optimal solution through algorithms demonstrates how a "greedy algorithm" (like one-step information maximization) can fall short of the "globally best performance" achieved through a deeper search <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. This represents [[different_problemsolving_styles | different problemsolving styles]].