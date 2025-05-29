---
title: Human vs algorithmic approaches to playing Wordle
videoId: fRed0Xmc2Wg
---

From: [[3blue1brown]] <br/> 

The video discusses the nuanced differences between how humans approach the game of Wordle and how [[algorithms_for_optimal_Wordle_play | algorithms]] are designed to solve it, particularly after a [[bug_identification_and_its_impact_on_Wordle_algorithm | bug fix]] in the initial algorithmic approach <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. While the initial goal was to find a theoretically optimal solution, the broader lesson lies in the application of concepts like [[information_theory_and_entropy_in_Wordle | information theory]] and the [[approaches_to_mathematical_problem_solving | approaches to mathematical problem solving]] <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## Algorithmic Approaches to Wordle

The algorithmic approach aims to find the absolute best performance for [[Wordle game mechanics | Wordle]] <a class="yt-timestamp" data-t="03:13">[00:04:13]</a>. This involves:

*   **Overfitting to the Official List**: The algorithm shamelessly incorporates the official Wordle answer list, assigning a uniform probability to each word, which is akin to "overfitting to a test set" <a class="yt-timestamp" data-t="04:13">[00:04:13]</a>.
*   **Quantifying Information**:
    *   The first step is to determine how likely each of the possible patterns is for a given opening guess, counting how many of the possible answers result in each pattern <a class="yt-timestamp" data-t="04:26">[00:04:26]</a>.
    *   This uses a formula involving a log expression to quantify the amount of [[information_theory_and_entropy_in_Wordle | information]] gained from a guess, representing how many times the space of possibilities is cut in half <a class="yt-timestamp" data-t="04:45">[00:04:45]</a>. This expected information is a measure of how much is learned from a first guess <a class="yt-timestamp" data-t="05:10">[00:05:10]</a>.
*   **Exhaustive Search**:
    *   Initially, searching through all 13,000 possible starting words for the highest expected [[information_theory_and_entropy_in_Wordle | information]] identified "soar" as the best opening guess <a class="yt-timestamp" data-t="05:13">[00:05:13]</a>.
    *   However, these are heuristics for estimating the true score <a class="yt-timestamp" data-t="05:37">[00:05:37]</a>. An exhaustive two-step search can be performed by running identical analysis for a given pattern, finding the optimal second guess, and measuring the expected [[information_theory_and_entropy_in_Wordle | information]] gained <a class="yt-timestamp" data-t="05:47">[00:05:47]</a>.
    *   Using this two-step metric, "slain" rose to the top, though many top contenders were very close <a class="yt-timestamp" data-t="06:57">[00:06:57]</a>.
*   **Simulation for Optimal Score**: To find the actual best score, a simulation was run playing all 2315 possible Wordle games with all answers for the top 250 words from the two-step [[information_theory_and_entropy_in_Wordle | entropy]] list <a class="yt-timestamp" data-t="07:34">[00:07:34]</a>. This identified "Salé" as the best opening guess, with "trace" and "crate" performing almost identically <a class="yt-timestamp" data-t="07:50">[00:07:50]</a>.

## Human Approaches to Wordle

Human play contrasts sharply with algorithmic play:

*   **No Memorization or Exhaustive Search**: Humans do not have the Wordle list memorized or perform exhaustive searches <a class="yt-timestamp" data-t="09:38">[00:09:38]</a>.
*   **Intuition-Based**: Humans rely on intuition, such as identifying vowels and their placement <a class="yt-timestamp" data-t="09:41">[00:09:41]</a>.
*   **Resilience**: A human strategy is more resilient to changes in the underlying Wordle answer list, unlike algorithms that "overfit" to a specific list <a class="yt-timestamp" data-t="09:20">[00:09:20]</a>.
*   **Optimal Guess for Humans**: The technically optimal opening guesses derived from algorithms (like "Salé") are not necessarily the best for a human player <a class="yt-timestamp" data-t="09:10">[00:09:10]</a>. This is because a human would also need to know the optimal second guess for every possible pattern seen <a class="yt-timestamp" data-t="09:14">[00:09:14]</a>.

## Comparison and Key Takeaways

There's a perceived tension where over-analysis might "ruin the game" <a class="yt-timestamp" data-t="08:55">[00:08:55]</a>. However, the video emphasizes that the point of writing [[algorithms_for_optimal_Wordle_play | algorithms]] for games is not to dictate human play, but to refine skills in algorithm writing for more meaningful contexts <a class="yt-timestamp" data-t="10:11">[00:10:11]</a>.

Instead of focusing on the "best opener," the primary lessons intended are:
*   How to quantify [[information_theory_and_entropy_in_Wordle | information]] <a class="yt-timestamp" data-t="09:52">[09:52]</a>.
*   Understanding when greedy [[algorithms_for_optimal_Wordle_play | algorithms]] fall short of a globally optimal performance that requires deeper searches <a class="yt-timestamp" data-t="09:55">[09:55]</a>.

Ultimately, the joy of writing [[algorithms_for_optimal_Wordle_play | algorithms]] is separate from the enjoyment of playing games as a human <a class="yt-timestamp" data-t="10:03">[10:03]</a>.