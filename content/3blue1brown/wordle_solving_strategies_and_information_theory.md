---
title: Wordle solving strategies and information theory
videoId: fRed0Xmc2Wg
---

From: [[3blue1brown]] <br/> 

This article serves as an addendum to a previous video on solving Wordle using [[information_theory_and_entropy_in_wordle | information theory]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It addresses a slight [[bug_identification_and_its_impact_on_wordle_algorithm | bug]] in the original code and provides a corrected analysis of [[optimal_wordle_opening_guesses_and_their_analysis | optimal Wordle opening guesses]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## The Bug in Wordle Simulation

A minor [[bug_identification_and_its_impact_on_wordle_algorithm | bug]] was identified in the code used to recreate Wordle and test [[algorithms for optimal Wordle play | algorithms]] <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This [[bug_identification_and_its_impact_on_wordle_algorithm | bug]] affected a small percentage of cases and had a slight impact on performance results <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

The issue specifically concerned how colors are assigned to guesses with multiple instances of the same letter <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. According to [[analysis_of_wordle_color_assignment_conventions | Wordle's conventions]] for [[wordle_game_mechanics | color assignment]]:
*   If you guess "speed" and the answer is "abide", the first 'e' is yellow, and the second 'e' is gray <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The gray indicates no second 'e' <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
*   If the answer is "erase", both 'e's in "speed" would be yellow, indicating two 'e's in different locations <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   If one 'e' is green (correct position), a second 'e' would be gray if the answer has no second 'e', or yellow if there is a second 'e' in a different location <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

The [[bug_identification_and_its_impact_on_wordle_algorithm | bug]] arose from an attempt to speed up computations, which inadvertently introduced a slight deviation from these conventions <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Ironically, pre-computing all patterns would have been the fastest method, rendering the optimization attempt unnecessary <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Impact on Optimal Wordle Strategies

While the fundamental lessons about [[information_theory_and_entropy_in_wordle | information]] and [[information_theory_and_entropy_in_wordle | entropy]] remain unchanged <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, the [[bug_identification_and_its_impact_on_wordle_algorithm | bug]] did affect the final conclusion regarding the [[optimal_wordle_opening_guesses_and_their_analysis | optimal Wordle opening guess]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. The previously stated best opener, "crane", was accurate only for the slightly different game played by the buggy [[algorithms for optimal Wordle play | algorithms]] <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

### Corrected Analysis for Optimal Opening Guesses

To find the absolute best performance, the analysis incorporates the official Wordle answer list, essentially "overfitting to the test set" by assigning a uniform probability to each word <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>. This differs from a previous approach that used [[word_frequency_data_and_wordle_strategies | relative word frequencies]] to build a more resilient strategy <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

#### One-Step Optimization (Expected Information)

The first step in finding an optimal guess involves calculating the expected [[information_theory_and_entropy_in_wordle | information]] gained from a particular opening guess <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This is done by counting how many possible answers produce each pattern and then quantifying the [[information_theory_and_entropy_in_wordle | information]] gained, often using a logarithmic expression to represent how many times the space of possibilities is cut in half <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

*   By this metric, searching through 13,000 potential starting words, the word with the highest expected [[information_theory_and_entropy_in_wordle | information]] is **soar** <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

#### Two-Step Optimization

Since expected [[information_theory_and_entropy_in_wordle | information]] is a heuristic, a deeper search provides a more accurate estimate of true score <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. An exhaustive search two steps in is feasible due to the limited number of patterns <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. This involves:
1.  Simulating an opening guess (e.g., "soar") and observing a pattern (e.g., all grays) <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
2.  Analyzing the distribution of patterns for a proposed second guess within the restricted set of remaining words <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
3.  Measuring the flatness of this distribution using the expected [[information_theory_and_entropy_in_wordle | information]] formula for all possible second guesses <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
4.  Taking a weighted average of these second-step values to measure the total expected [[information_theory_and_entropy_in_wordle | information]] gained after two steps <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

*   Using this two-step metric, **slain** rises to the top, with "soar" falling to 14th place <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

#### Full Simulation (Actual Game Score)

To find the true [[optimal_wordle_opening_guesses_and_their_analysis | optimal opening guess]], a simulation was run, playing all 2315 possible Wordle games using the official answer list with the top 250 words from the two-step information list <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

*   The word that marginally yields the best possible score is **Salé** <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   For those preferring more common words, **trace** and **crate** offer almost identical performance and are actual Wordle answers <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

The shift from sorting by two-step [[information_theory_and_entropy_in_wordle | entropies]] to lowest average score does shake up the list, but not as drastically <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

## Human vs. Algorithmic Approaches to Playing Wordle

While these [[algorithms for optimal Wordle play | algorithms]] identify a theoretically optimal opening guess, this may not be ideal for a [[human_vs_algorithmic_approaches_to_playing_wordle | human playing the game]] <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.
*   Humans would need to memorize optimal second guesses for various patterns <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   This analysis is heavily "overfit" to the current official Wordle answer list; any changes to the list by The New York Times would invalidate these findings <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   [[human_vs_algorithmic_approaches_to_playing_wordle | Human play]] differs significantly from [[algorithms for optimal Wordle play | algorithmic approaches]]; humans rely on intuition regarding vowels and placements rather than memorizing word lists or performing exhaustive searches <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

The primary purpose of developing [[algorithms for optimal Wordle play | algorithms]] for games like Wordle is not to dictate how humans play, but to refine skills in [[algorithms for optimal Wordle play | algorithm]] writing for more significant contexts <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. The key takeaways from such analyses include understanding how to quantify [[information_theory_and_entropy_in_wordle | information]] and recognizing when a greedy [[algorithms for optimal Wordle play | algorithm]] might fall short of a globally optimal solution found through deeper searches <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.