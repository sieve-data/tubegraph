---
title: Optimal strategy for Wordle
videoId: v68zYyaEmEA
---

From: [[3blue1brown]] <br/> 

The game [[Wordle game rules | Wordle]] has gained significant popularity, presenting a compelling opportunity for a math lesson, particularly concerning information theory and entropy <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The objective of developing an optimal strategy is to create an [[algorithm_design_for_wordle | algorithm]] capable of playing the game as effectively as possible <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Introduction to Wordle and Optimization

[[Wordle game rules | Wordle]] requires players to guess a mystery five-letter word within six attempts <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. After each guess, feedback is provided:
*   **Grey box:** The letter is not in the answer <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Yellow box:** The letter is in the answer, but in the wrong position <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Green box:** The letter is in the answer and in the correct position <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

An example game starting with "crane" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, followed by "shtik" <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, successfully narrowed the possibilities to "shard" or "sharp" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>, ultimately revealing "shard" as the answer in three guesses <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Achieving a score of three is considered a "birdie," while four is "par" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The core of this strategy involves understanding "information" and "entropy" <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Initial Approaches: Letter Frequencies

An early idea for an [[wordle_strategies_and_optimal_openers | opening guess]] involved examining the relative frequencies of letters in the English language <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The thought was to choose a word, or a pair of words, that would hit many common letters, such as "other" followed by "nails" <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. While getting green or yellow feedback is good, even receiving all grey boxes provides significant information by ruling out common letters <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. However, this approach is not systematic as it doesn't account for letter order <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This highlights the need for a quantitative measure of guess quality <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

## Quantifying Guess Quality: Information and Entropy

To rank potential guesses, it's important to understand the structure of the game's word lists. There are approximately 13,000 words considered valid guesses <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>, and a curated list of around 2,300 common words that are possible answers <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. For a robust algorithm that works against any set of five-letter words, it's preferable not to rely on the specific official answer list, especially since that list is visible in the source code <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Instead, the strategy uses universal data like relative word frequencies <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

The quality of a guess is measured by the amount of information it's expected to provide <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. Informative patterns are, by nature, less likely to occur <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. For example, a rare pattern might reduce 13,000 possibilities to just 58 <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. Conversely, the most likely outcomes (like all grey boxes) are the least informative <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### The Bit as a Unit of Information

The standard unit of information is the **bit** <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   An observation that halves the space of possibilities provides **one bit** of information <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   Cutting possibilities by a factor of four yields **two bits** <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   Cutting by a factor of eight yields **three bits** <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

The formula for information (in bits) is: `Information = log₂(1 / Probability)` or `Information = -log₂(Probability)` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. This logarithmic unit is useful because information adds together, just as probabilities multiply <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

### Defining Entropy

**Entropy** is the expected amount of information gained from a distribution of possible outcomes <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. To calculate it, each pattern's probability is multiplied by its information value, and these products are summed <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. For instance, the word "weary" yields an average of 4.9 bits of information <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>, while "slate" (which has a flatter distribution of outcomes) yields about 5.8 bits <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.

Entropy measures two things:
1.  **Flatness of distribution:** A more uniform distribution across patterns results in higher entropy <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
2.  **Number of possibilities:** More potential patterns or outcomes lead to higher entropy <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. For example, if there are 64 equally likely patterns, the entropy is 6 bits <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

The name "entropy" was suggested by John von Neumann to Claude Shannon because the function was already used in statistical mechanics, and its mysterious nature would give an advantage in debates <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. For Wordle, entropy simply refers to the expected information value of a guess <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

## [[Algorithm design for Wordle | Wordle Bot Version 1]]: Maximizing Entropy with Uniform Probabilities

The first version of the [[algorithm_design_for_wordle | Wordle bot]] operates by:
1.  Iterating through all 13,000 possible guesses <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
2.  Computing the entropy of the distribution of all possible patterns for each guess <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
3.  Selecting the guess with the highest entropy, as this is expected to reduce the space of possibilities the most <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
4.  This process is repeated for subsequent guesses, playing the same game on a restricted set of matching words <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

In this initial version, the bot assumes all 13,000 words are equally likely to be the answer <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>. The highest entropy opener was "Tares" <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>. When running simulations against all 2,315 actual [[Wordle game rules | Wordle]] answers, this naive method achieved an average score of about 4.124 <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

## Refining the Model: Incorporating Word Frequencies

The obvious next step for [[wordle_strategies_and_optimal_openers | improving the strategy]] is to incorporate the commonality of words <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.

### Leveraging Frequency Data

Word frequency data, such as from the Google Books English Ngram public dataset, can be used to assign probabilities to words being the final answer <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>. For example, "which" is very common, while "braid" is about 1000 times less likely <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>.

### Sigmoid Function for Probability Assignment

Instead of making probabilities directly proportional to frequencies, a **sigmoid function** is applied to the sorted list of words <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>. This function provides a nearly binary output (0 or 1) with a smooth transition, effectively creating a cutoff for plausibility <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>. The sigmoid's parameters determine how gradually the probability drops from 1 to 0 <a class="yt-timestamp" data-t="00:19:52">[00:19:52]</a>. This allows the model to assign a low probability to obscure words while giving more common words a higher chance, even if their raw frequencies differ greatly.

With an unequal weighting to words, the entropy calculation for expected information of a guess is affected <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>. For instance, a pattern that matches 32 very unlikely words might have similar entropy to one matching 8 plausible words, because the model's uncertainty is primarily driven by the plausible words <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>. This demonstrates the [[role_of_probability_in_word_guessing | role of probability]] in refining the entropy measurement.

## [[Algorithm design for Wordle | Wordle Bot Version 2]]: Optimizing for Expected Score

Version 2 of the [[algorithm_design_for_wordle | Wordle bot]] incorporates these refinements:
1.  **Refined Entropy Calculation:** It uses the non-uniform distribution of word probabilities when computing the expected information (entropy) for each guess <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
2.  **Expected Score Optimization:** Instead of just maximizing information, the bot now aims to minimize the *expected future score* <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>. This means considering the probability that a guess is the actual answer, and if not, how many more guesses are likely needed based on the remaining uncertainty <a class="yt-timestamp" data-t="00:25:32">[00:25:32]</a>.
3.  An empirical function `f(uncertainty)` is used, based on historical simulation data, to associate the remaining bits of uncertainty with an expected number of future guesses <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>. For example, if there's 1 bit of uncertainty (two possibilities), an average of 1.5 more guesses might be needed <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>.

## Simulation Results and Limitations

Running simulations with [[algorithm_design_for_wordle | Wordle bot]] Version 2 against all 2,315 possible answers shows an improved average score of about 3.6 <a class="yt-timestamp" data-t="00:28:00">[00:28:00]</a>. This version sometimes loses (requires more than six guesses) because it prioritizes guessing the answer over maximizing information in certain scenarios <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

Further sophistication, such as incorporating the true list of Wordle answers and performing a two-step forward search for expected information, can achieve an average score of around 3.43 <a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a>. In a two-step search, "Crane" appears to be the best opener <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

Even with optimal play, it's believed impossible for an [[algorithm_design_for_wordle | algorithm]] to consistently achieve an average score of three. This is because there simply isn't enough room to gain sufficient information after only two guesses to guarantee the answer on the third attempt every time <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. After two perfectly optimal guesses, the best-case scenario leaves about one bit of uncertainty, meaning two possibilities remain <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>. This highlights the inherent [[combinatorial_puzzles_and_strategy_development | combinatorial complexity]] of the puzzle.