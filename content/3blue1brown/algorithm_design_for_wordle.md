---
title: Algorithm design for Wordle
videoId: v68zYyaEmEA
---

From: [[3blue1brown]] <br/> 

The game [[wordle_game_rules | Wordle]] gained significant viral popularity, presenting an excellent opportunity for a math lesson on information theory, specifically entropy <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. This led to efforts to write an algorithm to play the game as optimally as possible <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Wordle Game Rules

The objective of [[wordle_game_rules | Wordle]] is to guess a mystery five-letter word within six attempts <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. After each guess, feedback is provided:
*   **Grey box**: The letter is not in the actual answer <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Yellow box**: The letter is in the word but not in that position <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Green box**: The letter is in the word and in the correct position <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

Guesses must be actual five-letter words <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. A common measure of success in [[wordle_game_rules | Wordle]] is aiming for four guesses as 'par' and three as a 'birdie' <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Initial Approaches & Challenges

An early [[wordle_strategies_and_optimal_openers | strategy]] considered the relative frequencies of letters in the English language <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. The idea was to choose an opening guess (or pair of guesses like "other" and "nails") that hits many frequent letters, as getting grays for common letters also provides significant information <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. However, this approach lacked systematic consideration of letter order <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

To develop a quantitative score for judging guess quality, it's crucial to understand the game's word lists <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>:
*   **Valid guesses**: Approximately 13,000 words are allowed as guesses, including many uncommon words <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Possible answers**: A curated list of about 2,300 common words are the actual potential answers <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

The goal was to design a program that doesn't rely on prior knowledge of the curated answer list, but instead uses universal data like relative word frequencies to prefer common words <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Quantifying Guess Quality: Information Theory and Entropy

A pattern that significantly reduces the space of possibilities (e.g., from 13,000 to 58 matches) is highly informative but unlikely to occur <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. Conversely, a common pattern is less informative <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Bits of Information

The standard unit of information is the **bit** <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   An observation that halves the space of possibilities provides one bit of information <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
*   Cutting possibilities by a factor of four yields two bits <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   Cutting by a factor of eight yields three bits <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

The formula for information (number of bits) in terms of the [[role_of_probability_in_word_guessing | probability]] (P) of an occurrence is `log₂(1/P)` or `-log₂(P)` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. This logarithmic nature is useful because information adds together (e.g., two bits plus three bits equals five bits), aligning with how expected values are calculated <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.

### Entropy

To judge the overall quality of a guess, we need to measure the **expected amount of information** it will provide across all possible patterns <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This is done by multiplying each pattern's [[role_of_probability_in_word_guessing | probability]] of occurring by its information content and summing these values <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This "expected value of information quantity" was named **entropy** by John von Neumann <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

For the purposes of [[wordle_game_rules | Wordle]] [[wordle_strategies_and_optimal_openers | strategy]], entropy can be thought of as:
1.  **How flat the distribution is**: A flatter distribution (where outcomes are more equally likely) has higher entropy <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.
2.  **How many possibilities there are**: More potential patterns lead to higher entropy <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.

For example, the guess "Weary" might have an expected information value (entropy) of 4.9 bits, meaning it's as good as chopping the possibilities in half about five times on average <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. In contrast, "Slate" might have an entropy of 5.8 bits, indicating a more effective reduction in possibilities <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Version 1: Maximizing Entropy

The first version of the [[wordle_strategies_and_optimal_openers | Wordle]] bot was designed to:
*   Go through all 13,000 possible valid guesses <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   Compute the entropy for the distribution of patterns each guess might produce <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>.
*   Pick the guess with the highest entropy, as this is most likely to reduce the space of possibilities <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
*   This process is repeated for subsequent guesses, narrowing down the possibilities based on previous feedback <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

This naive method, which assumes all words are equally likely to be the answer, resulted in an average score of about 4.124 over 2,315 simulated games <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>.

## Refining the Algorithm: Incorporating Word Frequency

A significant limitation of Version 1 was its failure to account for word commonality <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. To address this, word frequency data (e.g., from Google Books English Ngram public dataset) was incorporated <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.

Instead of directly using frequency as [[role_of_probability_in_word_guessing | probability]], a sigmoid function was applied to the sorted list of words <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>. This creates a more binary-like [[role_of_probability_in_word_guessing | probability]] assignment, where common words have a high likelihood of being an answer (closer to 1), and obscure words have a very low likelihood (closer to 0) <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.

This refined [[role_of_probability_in_word_guessing | probability]] distribution across words allowed entropy to become an even more useful measurement:
*   It still measures the expected information gained from a guess <a class="yt-timestamp" data-t="00:22:05">[00:22:05]</a>.
*   It also measures the remaining uncertainty among possible words, where obscure words contribute less to the overall uncertainty even if they formally match a pattern <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>.

## Version 2: Entropy with Refined Probabilities

Version 2 of the [[wordle_strategies_and_optimal_openers | Wordle]] bot introduced two main improvements:
1.  **Refined Entropy Calculation**: The computation of expected information values (entropies) for guesses now incorporates the assigned [[role_of_probability_in_word_guessing | probability]] that a given word would actually be the answer <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.
2.  **Expected Score Optimization**: The bot maintains a model of each word's [[role_of_probability_in_word_guessing | probability]] of being the actual answer. When choosing a guess, it focuses on the **expected score** of the game, rather than just maximizing immediate information gain <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>.

This expected score is calculated by:
*   Considering the [[role_of_probability_in_word_guessing | probability]] that the current guess is the answer (which would end the game).
*   Estimating the remaining score based on the projected uncertainty after the guess, using an empirical function `f` that maps bits of uncertainty to expected guesses needed <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>. This function was derived from plotting data from previous simulations of Version 1 <a class="yt-timestamp" data-t="00:26:18">[00:26:18]</a>.

Simulations of Version 2, playing against all 2,315 possible [[wordle_game_rules | Wordle]] answers, yielded an average score of approximately 3.6 <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>. While better than Version 1, this version occasionally loses (requires more than six guesses) due to its tradeoff between information gain and direct goal achievement <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>.

## Further Optimizations and Limitations

Further sophistication, such as incorporating the true list of [[wordle_game_rules | Wordle]] answers and performing a two-step lookahead search (evaluating the expected information of two guesses forward), can achieve an average score of around 3.43 <a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a>. With such advanced [[wordle_strategies_and_optimal_openers | strategies]], "Crane" has been identified as a top opener <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

The theoretical maximum expected information after the first two guesses, if using the true [[wordle_game_rules | Wordle]] list, is around 10 bits <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>. Given that the initial uncertainty is about 11 bits, this suggests that even with perfectly [[optimal_strategy_for_wordle | optimal play]], one would typically be left with about one bit of uncertainty (two possible answers) after two guesses <a class="yt-timestamp" data-t="00:29:34">[00:29:34]</a>. Therefore, consistently achieving an average score as low as three is likely impossible due to the inherent information limitations within the game <a class="yt-timestamp" data-t="00:29:44">[00:29:44]</a>.