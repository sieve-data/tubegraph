---
title: Information theory in gamesolving
videoId: fRed0Xmc2Wg
---

From: [[3blue1brown]] <br/> 

This article serves as an addendum and correction to a previous video discussing the use of [[information_theory_and_entropy | information theory]] to solve the game Wordle <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. A slight bug in the code used for simulation led to inaccurate results regarding the optimal Wordle strategy <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## The Bug and its Impact

The error stemmed from how colors were assigned to letters in a guess when multiple instances of the same letter were present <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

*   **Example 1**: If "speed" was guessed and "abide" was the answer, the first 'e' would be yellow (matching a true answer 'e') and the second 'e' would be gray (indicating no second 'e') <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   **Example 2**: If the answer was "erase", both 'e's in "speed" would be yellow, signifying two 'e's in different locations <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   **Example 3**: If one 'e' was green (correct position), a second 'e' in the guess would be gray if no other 'e' existed in the answer, but yellow if a second 'e' was present elsewhere <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

The bug was introduced during an attempt to speed up computations for pattern value calculations, a shortcut that was ultimately unnecessary as pre-computing all patterns proved to be the fastest method <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

Despite the bug, the core lessons on [[information_theory_and_entropy | information]] and [[information_theory_and_entropy | entropy]] remained valid <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The primary impact was on the final conclusion regarding the theoretically optimal opening guess for Wordle <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. The previous video incorrectly stated "crane" as the best opening word due to the algorithms playing a slightly different game <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Refined Optimal Wordle Strategy

To find the absolute best performance, the analysis incorporated the official Wordle answer list, assigning uniform probability to each word and "shamelessly overfitting to the test set" <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.

### Step 1: Expected Information (One-Step Heuristic)

The initial approach involved calculating the expected [[information_theory_and_entropy | information]] gain from a given opening guess <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This is done by:
1.  Counting how many possible answers produce each specific pattern for a given guess <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
2.  Quantifying the [[information_theory_and_entropy | information]] gained from each pattern using a log expression, which represents how many times the space of possibilities is cut in half <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
3.  Taking a weighted average of these values to measure the expected learning from the first guess <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

When searching all 13,000 potential starting words, "soar" (an obsolete term for a baby hawk) yielded the highest expected [[information_theory_and_entropy | information]] <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. However, this is a one-step heuristic and not necessarily the true optimal opening guess <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Step 2: Two-Step Exhaustive Search

A more comprehensive approach involves an exhaustive search two steps into the game <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. For each first guess and the resulting pattern:
1.  An identical analysis is run to find the optimal second guess within the restricted set of remaining possible answers <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>.
2.  The flatness of the distribution for that second guess is measured using the expected [[information_theory_and_entropy | information]] formula <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
3.  By doing this for all possible patterns, a full map of best second guesses and their expected [[information_theory_and_entropy | information]] is created <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.
4.  A weighted average of these second-step values provides a measure of expected [[information_theory_and_entropy | information]] after two steps <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

Using this two-step metric, "slain" (a British term for a turf-cutting spade) rose to the top, displacing "soar" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Still, this is based on an [[information_theory_and_entropy | information]] heuristic, not the actual game score <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.

### Step 3: Full Simulation for Actual Score

To determine the true optimal opener, a simulation was run, playing all 2315 possible Wordle games using the top 250 candidates from the two-step analysis <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

The word that marginally achieved the best average score was "Salé" (an alternate spelling for a light medieval helmet) <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. For those preferring real words, "trace" and "crate" offer almost identical performance and are actual Wordle answers <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Human vs. Algorithmic Play

While finding the optimal opening guess is interesting from an algorithmic perspective, it is argued that it "ruins the game" for human players <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Why the Optimal Strategy Isn't for Humans
*   **Memory and Calculation**: Human players would need to know the optimal second guess for every possible pattern, which is impractical <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Overfitting**: The algorithm's strategy is absurdly overfit to the current official Wordle answer list. Any change to this list by the New York Times would render the optimal strategy obsolete <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>.
*   **Intuition vs. Exhaustion**: [[human_vs_algorithmic_gameplay_differences | Humans play Wordle very differently from algorithms]] <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. They rely on intuition about common letters and patterns, rather than memorizing word lists or performing exhaustive searches <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

The true value of writing algorithms for games lies not in affecting human gameplay, but in honing [[problemsolving_strategies_in_mathematical_puzzles | algorithmic problem-solving skills]] applicable in more meaningful contexts <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>. Key takeaways include understanding how to quantify [[information_theory_and_entropy | information]] and recognizing when a greedy algorithm falls short of globally optimal performance <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.