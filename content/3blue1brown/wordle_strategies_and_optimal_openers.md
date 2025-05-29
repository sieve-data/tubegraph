---
title: Wordle strategies and optimal openers
videoId: fRed0Xmc2Wg
---

From: [[3blue1brown]] <br/> 

This article serves as an addendum and correction to a previous video on solving Wordle using [[Wordle strategies and optimal openers | information theory]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. A slight bug in the code used to simulate [[Wordle strategies and optimal openers | Wordle]] games affected the determination of the theoretically optimal opening guess <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## The Bug Explained

The bug was subtle, affecting a small percentage of cases and having only a slight overall impact <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. It concerned how colors were assigned to guesses containing multiple instances of the same letter <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

According to [[wordle_game_rules | Wordle conventions]]:
*   If you guess "speed" and the answer is "abide", the first 'e' is yellow (different location, present) and the second 'e' is gray (not present) <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   If the answer is "erase", both 'e's in "speed" would be yellow, indicating two 'e's in different locations <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   If one 'e' is green (correct position), and the true answer has no second 'e', the second guessed 'e' would be gray <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   If a second 'e' exists elsewhere, it would be yellow <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

The bug arose from a shortcut taken to speed up computations, which inadvertently introduced a slight deviation from these conventions <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Ironically, the fastest way to compute patterns is to pre-compute them as lookups, making the trick unnecessary <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Impact on Optimal Openers

While core concepts like [[Wordle strategies and optimal openers | information theory]] and entropy remain unchanged <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, the bug did affect the final conclusion regarding the [[optimal_strategy_for_wordle | optimal possible score for the Wordle answer list]] <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. The previously identified best opener, "crane," was only optimal under the slightly different game rules simulated by the buggy code <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. After correction, a different word emerged as the theoretically [[optimal_strategy_for_wordle | optimal first guess]] <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Methodology for Finding Optimal Openers

To find the absolute best performance, the analysis incorporates the official Wordle answer list, essentially "overfitting" to the test set <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This means every word in the list is assigned a uniform probability <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

### Step 1: One-Step Information Gain

The first step is to calculate how likely each of the possible patterns is for a given opening guess <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This involves counting how many of the possible answers yield each specific pattern <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. The amount of information gained from a guess is quantified using an entropy formula involving a log expression, which measures how many times the space of possibilities is cut in half <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. A weighted average of these information gains provides an expected learning measure for the first guess <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

By searching through 13,000 potential starting words for the highest expected information, "soar" was identified as the best <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. This, however, is merely a heuristic and doesn't guarantee the best overall score <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Step 2: Two-Step Information Gain

A deeper search can be performed by considering two steps ahead <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. For a given first guess (e.g., "soar") and an observed pattern (e.g., all grays), the same analysis is run for the second guess <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This involves:
1.  Restricting the word list to only those compatible with the first guess's pattern <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
2.  Measuring the flatness of the distribution for a proposed second guess using the expected information formula <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
3.  Repeating this for all 13,000 possible second guesses to find the optimal one for that specific scenario <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

By performing this for all possible first-step patterns and taking a weighted average of the second-step values, a two-step metric for information gain is established <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Using this metric, "slain" rises to the top, with "soar" falling to 14th place <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Step 3: Full Simulation for Actual Score

While information gain is a useful heuristic, it doesn't directly translate to the actual score if the game is played out <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. To find the true [[optimal_strategy_for_wordle | optimal strategy for Wordle]], a simulation was run for all 2,315 possible Wordle games using the top 250 words identified from the two-step analysis <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

This full simulation revealed that "Salé" (an alternate spelling for a medieval helmet) marginally achieves the best possible average score <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. For those preferring common words, "trace" and "crate" offer almost identical performance and are actual Wordle answers <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This shift from sorting by two-step entropies to lowest average score also reorders the list, but less dramatically <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. Further minor improvements can be achieved through brute-forcing <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.

## Human vs. Algorithmic Play

The [[optimal_strategy_for_wordle | optimal strategy for Wordle]] derived from these [[algorithm_design_for_wordle | algorithms]] is not necessarily ideal for human players <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>. Human players would need to know the optimal second guess for every possible pattern <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. More importantly, this analysis is heavily "overfit" to the official Wordle answer list <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Any change to this list (e.g., by the New York Times) would invalidate the results <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

Humans play differently, relying on intuition about vowels and letter placement rather than memorized word lists or exhaustive searches <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. The true value of this analysis lies not in finding a "cheat code" for the game, but in understanding how to quantify information and recognizing when a greedy [[algorithm_design_for_wordle | algorithm]] falls short compared to a deeper search <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. The goal of designing [[algorithm_design_for_wordle | algorithms]] for games is to hone [[problem_solving_strategies_in_mathematics | problem-solving strategies]] for more meaningful contexts <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.