---
title: Bug identification and its impact on Wordle algorithm
videoId: fRed0Xmc2Wg
---

From: [[3blue1brown]] <br/> 

A significant bug was discovered in the code used to recreate and test [[Algorithms for optimal Wordle play | Wordle-solving algorithms]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This bug, though slight and affecting only a small percentage of cases, had a notable impact on the reported optimal [[Optimal Wordle opening guesses and their analysis | Wordle opening guesses]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Nature of the Bug

The bug concerned the assignment of colors to guesses containing multiple instances of the same letter <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Specifically, it deviated from the official [[Wordle game mechanics | Wordle conventions]] for color assignment <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

### Examples of Correct Color Assignment:

*   **Guess: "speed", Answer: "abide"**
    *   The first 'e' would be yellow (indicating presence in a different location).
    *   The second 'e' would be gray (indicating no second 'e' in the true answer) <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Guess: "speed", Answer: "erase"**
    *   Both 'e's would be colored yellow (indicating two 'e's in different locations) <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Guess with a green hit:**
    *   If one 'e' is green (correct letter, correct position), a second 'e' would be gray if the true answer has no second 'e' <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   It would be yellow if there is a second 'e' in a different location <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

The bug was inadvertently introduced while attempting to speed up computations related to patterns between word pairs <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Ironically, the fastest method for computation involves pre-computing all patterns for simple lookups, rendering the "trick" unnecessary <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

## Impact of the Bug

While most of the fundamental lessons on [[Information theory and entropy in Wordle | information theory]] and entropy remained unchanged <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a> <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>, the bug did have specific effects:

### Minor Effects

*   **Distributions:** Some displayed distributions associated with given words might have been slightly inaccurate, as the buckets for various patterns could contain more or fewer true answers <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. However, this rarely manifested on screen due to the infrequency of words hitting this specific edge case <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Major Effects

*   **Optimal Opening Guess:** The most significant impact was on the determination of the theoretically [[Optimal Wordle opening guesses and their analysis | optimal first guess]] for the Wordle answer list <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   Prior to the fix, the best performance was attributed to "crane" <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
    *   After fixing the bug and re-running the algorithms, a different optimal answer emerged <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.

## Corrected Findings on Optimal Opening Guesses

To find the absolute best performance, the analysis incorporated the official Wordle answer list, treating it as a fixed "test set" with uniform probability for each word <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### Step 1: Expected Information (One-Step Lookahead)

*   This involves counting how many possible answers yield each pattern for a given opening guess <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   The amount of information gained from a guess is quantified using a formula involving a log expression, which measures how many times the space of possibilities is cut in half <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   Based on this metric, searching through all 13,000 potential starting words, the word with the highest expected information was found to be **"soare"** (an obsolete term for a baby hawk) <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   However, this only looks one step ahead and is a heuristic <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Step 2: Two-Step Exhaustive Search

*   To achieve a more accurate ranking, an exhaustive search was performed two steps in <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
*   For each possible first guess and subsequent pattern seen (e.g., all grays from "soare"), the optimal second guess within the restricted word list was identified, and its expected information calculated <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   A weighted average of these second-step values provides a measure of expected information after two steps <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   Using this two-step metric, **"slain"** (a British term for a turf-cutting spade) rose to the top, with "soare" falling to 14th place <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

### Step 3: Simulation of Actual Game Play (Lowest Average Score)

*   Expected information is still a heuristic and doesn't directly represent the actual average score in a game <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   To find the true optimal opening guess, simulations were run for all 2315 possible Wordle games with the top 250 words from the two-step information metric <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   The word that yielded the *best possible score* (lowest average guesses) was **"salet"** (an alternate spelling for "sallet", a light medieval helmet) <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>.
*   **"Trace"** and **"crate"** provide almost identical performance and are considered more "real" words, having the benefit of being actual Wordle answers <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   This shift from information-based ranking to average score-based ranking also reordered the list, with "salet" moving from third to first, and "crate" and "trace" from fourth and fifth respectively <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

## Broader Implications

Despite finding the "theoretically" optimal openers, this level of [[Algorithms for optimal Wordle play | algorithmic analysis]] is not necessarily ideal for [[Human vs algorithmic approaches to playing Wordle | human players]] <a class="yt-timestamp" data-t="00:09:10">[00:09:10]</a>.

*   Humans would need to memorize optimal second guesses for various patterns <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   The findings are highly [[Optimal Wordle opening guesses and their analysis | overfit to the official Wordle answer list]] <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Any change to the underlying list by the New York Times would invalidate these results <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.
*   [[Human vs algorithmic approaches to playing Wordle | Human play]] relies on intuition (e.g., vowel placement) rather than exhaustive searches or memorized lists <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

The primary takeaway from this detailed [[Wordle solving strategies and information theory | Wordle analysis]] is not to find a "technically optimal answer" for a game, but rather to illustrate concepts like [[Information theory and entropy in Wordle | quantifying information]] and understanding when a greedy algorithm might fall short of a globally optimal solution found through deeper search <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. The goal of writing algorithms for games is to hone skills for more meaningful contexts, not to alter how humans enjoy playing them <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.