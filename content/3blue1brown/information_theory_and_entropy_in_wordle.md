---
title: Information theory and entropy in Wordle
videoId: v68zYyaEmEA
---

From: [[3blue1brown]] <br/> 

The game Wordle became widely popular, presenting an opportunity for a math lesson focused on [[probability_and_information_measurement | information theory]] and a concept called entropy <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This analysis involves developing an [[algorithms_for_optimal_wordle_play | algorithm]] to play the game as optimally as possible, with its core centered on entropy <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## [[Wordle game mechanics | Wordle Game Mechanics]]

[[Wordle game mechanics | Wordle]] challenges players to guess a mystery five-letter word within six attempts <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. After each guess, players receive feedback:
*   **Grey box**: The letter is not in the answer <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Yellow box**: The letter is in the answer but not in that specific position <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Green box**: The letter is in the answer and in the correct position <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

For instance, starting with "crane" might yield grey, yellow, green, grey, grey <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. The [[algorithms_for_optimal_wordle_play | algorithm]] might then suggest "shtik" <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. The game requires actual five-letter words for guesses <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. A good score in Wordle is considered to be four guesses ("par"), while three guesses is "birdie" <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Initial Approaches to [[Wordle solving strategies and information theory | Wordle Solving]]

An early thought for [[Wordle solving strategies and information theory | optimal Wordle play]] was to consider the [[word_frequency_data_and_wordle_strategies | relative frequencies of letters]] in the English language <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. The aim was to find an opening guess or pair of guesses that hit many frequent letters, like "other" followed by "nails" <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. Even if a guess results in all grey boxes, it provides valuable information by eliminating common letters <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. However, this approach is not systematic enough as it doesn't account for letter order <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This raises the question of whether a quantitative score can judge the quality of a potential guess <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

There are approximately 13,000 valid five-letter words that can be entered as guesses <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. However, the actual answers are drawn from a smaller, human-curated list of about 2,300 common words <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. While this answer list is visible in the source code, using it is considered cheating <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. The goal is to create a program that doesn't rely on this specific list, making it more resilient and applicable beyond the official website <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Instead, the approach uses more universal data, such as general [[word_frequency_data_and_wordle_strategies | word frequencies]], to prefer more common words <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

A guess's quality depends on how much it reduces the pool of possible answers <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. An uncommon letter like 'W' can be very informative if it matches, significantly reducing the possibilities (e.g., from 13,000 to 58 words) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. However, such informative patterns are inherently unlikely to occur <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. The most likely outcomes (e.g., getting mostly grey boxes) are also the least informative <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. To assess a guess's overall quality, a measure of the expected amount of information from its possible outcomes is needed <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

## Information as Bits and Entropy

The standard unit of information is the **bit** <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   An observation that halves the space of possibilities provides one bit of information <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   Cutting possibilities by a factor of four yields two bits <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   Cutting possibilities by a factor of eight yields three bits <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

This relationship is formalized by the formula:
$$ \text{Information (bits)} = \log_2 \left( \frac{1}{\text{Probability of occurrence}} \right) = - \log_2 (\text{Probability of occurrence}) $$
This formula measures how many times you've effectively halved your possibilities <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Logarithms are useful because information adds together, just as probabilities multiply <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>.

**Entropy** is the expected value of this information <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. It's calculated by summing the product of each pattern's probability of occurring and its corresponding information <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. For example, the word "weary" might have an expected information of 4.9 bits, while "slate" (which has a flatter distribution of outcomes) might have 5.8 bits, meaning "slate" is expected to halve the possibilities more times <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

The term "entropy" was suggested by John von Neumann to Claude Shannon, the developer of [[probability_and_information_measurement | information theory]], partly because "nobody knows what entropy really is, so in a debate you'll always have the advantage" <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. For Wordle, entropy simply means the expected information value of a particular guess <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

Entropy measures two things:
1.  **Flatness of the distribution**: A flatter distribution (where outcomes are more equally likely) results in higher entropy <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. The maximum possible entropy for Wordle (3 to the 5th total patterns) is 7.92 bits <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.
2.  **Number of possibilities**: More possible patterns lead to higher entropy <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. An entropy of 6 bits, for example, suggests as much variation as 64 equally likely outcomes <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.

## [[Algorithms for optimal Wordle play | Wordle Solver (Version 1): Maximizing Entropy]]

The first version of the [[algorithms_for_optimal_wordle_play | Wordle solver]] (the "Wurdlebot") calculates the entropy for all 13,000 possible guesses <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. It then picks the guess with the highest entropy, as this is expected to reduce the space of possibilities the most <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>. This process repeats for subsequent guesses, narrowing down the possibilities based on the feedback received <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>.

When demonstrated, the bot's top suggestion for an opening guess, based on entropy, was "Tares" <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
<a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>
> [!NOTE] Expected vs. Actual Information
> The bot shows the *expected* information (entropy) for a guess and the *actual* information gained from the specific pattern revealed <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. The left side shows the remaining possible words, and an "uncertainty" value (in bits) which, in this naive version, is a measure of the number of possibilities (e.g., 2^13.66 ≈ 13,000) <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
>
> If uncertainty decreases by 4.7 bits from 5.78 bits, it means the remaining uncertainty is 1 bit (5.78 - 4.7 = 1.08), which corresponds to 2 possibilities (2^1 = 2) <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.

Simulations of this Version 1 bot, playing against all 2,315 actual Wordle answers, resulted in an average score of about **4.124** <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>. This is considered "not bad" but falls short of consistently achieving scores of 3.

## [[Algorithms for optimal Wordle play | Wordle Solver (Version 2): Incorporating Word Frequency]]

The next improvement involved incorporating [[word_frequency_data_and_wordle_strategies | word frequency data]] to make the algorithm more sophisticated <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. This was done using Mathematica's word frequency data function, which pulls from the Google Books English Ngram public dataset <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

The challenge was to model how likely each word is to be the final answer, not just proportionally to its frequency, as many common words (like "which") are equally plausible as answers as less common ones (like "braid") <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. A sigmoid function was used to assign a probability to each word, effectively creating a binary cutoff where words are either likely (close to 1) or unlikely (close to 0) to be an answer, with a smooth transition in between <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

This refined probability distribution affects the entropy calculation:
*   Even if there are many theoretical matches for a pattern, if most of them are highly obscure words, the *actual* uncertainty (entropy) remains low <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>. For example, 16 matches with 12 obscure words might still result in only 2.11 bits of entropy, close to the 2 bits for 4 equally likely common words <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.
*   This demonstrates two applications of entropy: measuring the expected information from a guess and measuring the remaining uncertainty among possible words <a class="yt-timestamp" data-t="00:22:01">[00:22:01]</a>.

In Version 2 of the [[algorithms_for_optimal_wordle_play | Wordle algorithm]]:
1.  Entropy calculations now incorporate the refined probabilities that a word is an actual answer <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
2.  The bot models the probability of each word being the true answer and incorporates this into its decision-making <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>. The "uncertainty" value on the left is no longer just a count of matches, but a true entropy value reflecting the likelihood of each word <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>. For example, 526 actual matches might only represent 8.02 bits of uncertainty (akin to 259 equally likely outcomes) if many are obscure <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>.
3.  The bot's top picks no longer solely maximize information <a class="yt-timestamp" data-t="00:24:51">[00:24:51]</a>. For the final guesses, it prioritizes words that are highly probable answers, even if other guesses might technically yield more information <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>.

This improved approach aims to quantify the intuition that gaining more information should lead to a lower expected final score <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>. A function `f` was created by plotting data from previous games of Version 1, associating amounts of uncertainty with the number of additional guesses required <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. For instance, 1 bit of uncertainty averaged 1.5 more guesses <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>. This function helps estimate the expected score if a particular guess is made, based on the remaining uncertainty <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>.

Simulations of Version 2, playing against all 2,315 Wordle answers, achieved an average score of approximately **3.6** <a class="yt-timestamp" data-t="00:27:54">[00:27:54]</a>. This version sometimes loses (requires more than six guesses), presumably because it makes tradeoffs to go for the win rather than purely maximizing information at every step <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

## Further Optimizations and Limitations

Further improvements are possible beyond Version 2. Incorporating the *true* list of Wordle answers and using a two-step lookahead search (considering the expected information two steps forward, not just one) can achieve an average score of around **3.43** <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>. This 3.43 average likely represents the maximum achievable performance when relying on this type of model <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>.

Based on this analysis, "Crane" appears to be an optimal opening guess <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>. If using the true Wordle answer list, the initial uncertainty is over 11 bits <a class="yt-timestamp" data-t="00:29:10">[00:29:10]</a>. A brute-force search suggests the maximum expected information after the first two guesses is around 10 bits <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>. This implies that even with perfectly optimal play, one would be left with about one bit of uncertainty (down to two possible guesses) after two moves <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>. Therefore, it's highly improbable to write an [[algorithms for optimal Wordle play | algorithm]] that consistently achieves an average score as low as three, as the available words simply don't allow for enough information gain in only two steps to guarantee a third-guess solution every time <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>.