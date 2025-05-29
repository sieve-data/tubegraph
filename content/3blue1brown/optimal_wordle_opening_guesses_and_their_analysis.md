---
title: Optimal Wordle opening guesses and their analysis
videoId: fRed0Xmc2Wg
---

From: [[3blue1brown]] <br/> 

This article provides an addendum and correction to previous analysis on solving [[Wordle game mechanics | Wordle]] using [[Information theory and entropy in Wordle | information theory]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. A slight [[Bug identification and its impact on Wordle algorithm | bug]] in the code used for simulation led to a re-evaluation of optimal opening guesses <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Identifying and Correcting the Bug

The bug affected how colors were assigned to guesses, specifically when a guess contained multiple instances of the same letter <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. The [[Analysis of Wordle color assignment conventions | Wordle conventions]] for color assignment are specific:
*   If you guess "speed" and the answer is "abide", the first 'e' is yellow (matching an 'e' in "abide"), and the second 'e' is gray (no second 'e' in "abide") <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   If the answer is "erase", both 'e's in "speed" would be yellow, indicating two 'e's in different locations <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.
*   If one 'e' is green (correct position), and there's no second 'e' in the answer, the second 'e' in the guess would be gray <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. If there is a second 'e' elsewhere, it would be yellow <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

The bug arose from a shortcut taken during computation optimization that subtly altered these [[Analysis of Wordle color assignment conventions | conventions]] <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Ironically, pre-computing all patterns would have eliminated the need for such shortcuts <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Impact on Optimal Guesses

While core concepts of [[Information theory and entropy in Wordle | information theory]] and [[Information theory and entropy in Wordle | entropy]] remain unchanged <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>, the bug did affect the final conclusion regarding the [[Algorithms for optimal Wordle play | optimal opening guess]] for the official Wordle answer list <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. The previously identified best opener, "crane," was only accurate because the [[Algorithms for optimal Wordle play | algorithms]] were playing a slightly different version of the game <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.

## Methodology for Finding Absolute Best Performance

To find the absolute best performance for the official Wordle answer list, the analysis shamelessly "overfits" to the specific answer list <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This means assigning uniform probability to each word in the official list, unlike previous methods that used [[Word frequency data and Wordle strategies | word frequency data]] for resilience <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Step 1: Expected Information (One-Step)

The first step involves calculating the expected information gained from a particular opening guess <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. This is done by:
1.  Counting how many possible answers yield each unique pattern for a given guess <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
2.  Quantifying the amount of information gained using an [[Information theory and entropy in Wordle | information theory]] formula involving a log expression, which indicates how many times the possibility space is halved <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
3.  Taking a weighted average of these values to measure expected learning <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

Based on expected information alone, the best opening guess among 13,000 possible words is "soar," an obsolete term for a baby hawk <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. However, this is only a one-step heuristic <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Step 2: Two-Step Exhaustive Search

A more comprehensive approach involves an exhaustive search two steps in <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. For each possible first guess and every potential pattern it could yield, the [[Algorithms for optimal Wordle play | algorithm]] then finds the optimal second guess among the remaining valid words and calculates its expected information <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

By taking a weighted average of the expected information from all possible second steps, a new ranking emerges <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. With this two-step metric, "soar" drops to 14th place, and "slain" (a British term for a turf-cutting spade) rises to the top <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

### Step 3: Full Game Simulation for Optimal Score

Expected information is merely a heuristic; it doesn't directly measure the actual average score if the game is played out <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. To find the true optimal opener, simulations were run for all 2,315 possible Wordle games using the top 250 words from the two-step analysis <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

The word that marginally achieves the best possible average score is "Salé," an alternate spelling for a light medieval helmet <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. If "Salé" feels too obscure, "trace" and "crate" offer almost identical performance and are common words that are also actual Wordle answers <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Human vs. Algorithmic Approaches to Playing Wordle

While these [[Algorithms for optimal Wordle play | algorithms]] provide a theoretically optimal solution, this detailed analysis is not necessarily ideal for human play <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

### Why the Optimal Algorithm Is Not for Humans:
*   **Memorization**: Humans don't memorize the optimal second guess for every possible pattern <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Overfitting**: The analysis is heavily "overfit" to the current official Wordle answer list <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. Any change to this list by the New York Times would invalidate the findings <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   **Intuition vs. Search**: Humans rely on intuition about common letter placements and vowels, not exhaustive searches <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

The primary purpose of this deep dive into [[Wordle solving strategies and information theory | Wordle solving strategies]] using [[Algorithms for optimal Wordle play | algorithms]] is not to dictate how humans should play a fun word game <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. Instead, it serves as a lesson in understanding how to quantify [[Information theory and entropy in Wordle | information]], the pitfalls of greedy [[Algorithms for optimal Wordle play | algorithms]], and honing skills for applying [[Algorithms for optimal Wordle play | algorithms]] in more significant contexts <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. The joy of writing [[Algorithms for optimal Wordle play | algorithms]] is distinct from the enjoyment of playing the game itself <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.