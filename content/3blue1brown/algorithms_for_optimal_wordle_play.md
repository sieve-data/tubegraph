---
title: Algorithms for optimal Wordle play
videoId: v68zYyaEmEA
---

From: [[3blue1brown]] <br/> 

The game Wordle has gained significant popularity, serving as an excellent example for lessons in [[information_theory_and_entropy_in_wordle | information theory]] and specifically [[information_theory_and_entropy_in_wordle | entropy]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Programmers, including the speaker, have attempted to [[human_vs_algorithmic_approaches_to_playing_wordle | write algorithms]] to play the game as optimally as possible, with the entire algorithm centering on the concept of [[information_theory_and_entropy_in_wordle | entropy]] <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## [[wordle_game_mechanics | Wordle Game Mechanics]]

The goal of Wordle is to guess a mystery five-letter word within six chances <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. After each guess, players receive feedback:
*   **Grey box**: The letter is not in the actual answer <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Yellow box**: The letter is in the word but not in that specific position <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Green box**: The letter is in the word and in the correct position <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

An example game using the bot started with "crane" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, receiving grey, yellow, green, grey, grey <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. The bot's next suggestion was "shtik" <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, followed by "shard" <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>, solving the puzzle in three guesses <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Four guesses is considered "par" and three is a "birdie" <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

## Initial Approaches and Challenges

Early [[wordle_solving_strategies_and_information_theory | Wordle solving strategies]] involved looking at the relative frequencies of letters in English to find an opening guess that hits many common letters <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. An initial favorite combination was "other" followed by "nails" <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. While hitting green or yellow feels good, even all grey boxes provide information by eliminating possibilities <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. However, this approach lacked systematic consideration for letter order <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. The need for a quantitative score to judge guess quality became apparent <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### The Wordle Lexicon
There are approximately 13,000 words considered valid guesses in Wordle <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. However, the actual answers are drawn from a smaller, human-curated list of about 2,300 common words <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. To create a more robust algorithm that plays against anyone, not just the official website, the goal was to avoid incorporating prior knowledge of this specific answer list <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Using the official list, which is visible in the source code, would be considered cheating <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Instead, the approach favored using more universal data, such as general [[word_frequency_data_and_wordle_strategies | relative word frequencies]], to capture the intuition for preferring common words <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Information Theory and Entropy: The Core Concept

The value of a guess lies in its ability to reduce the space of possible answers. A pattern that yields a lot of information is, by its very nature, unlikely to occur <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. For example, if a guess of "weary" resulted in a specific pattern (grey, yellow, green, green, grey), it would narrow down 13,000 words to only 58, a huge reduction <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. Conversely, a very common pattern, like all grays for "weary," is less informative, still leaving 1,400 possible matches <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. The most likely outcomes are the least informative <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Bits as a Unit of Information
The standard unit of information is the **bit** <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>:
*   An observation that cuts the space of possibilities in half provides **one bit** of information <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   Cutting by a factor of four yields **two bits** <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   Cutting by a factor of eight yields **three bits** <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

The formula for information (in bits) based on the probability (P) of an occurrence is:
`Information = log₂(1/P)` or `Information = -log₂(P)` <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>. This logarithmic expression is useful because information adds together <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. For example, two bits followed by three bits yields five bits of information <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

### Entropy
The quality of a guess is measured by the **expected value of information**, known as [[information_theory_and_entropy_in_wordle | entropy]] <a class="yt-timestamp" data-t="00:10:45">[00:10:45]</a>. This is calculated by summing the product of each pattern's probability of occurring and the information it provides <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

For example, the guess "weary" yields an average of 4.9 bits of information <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>. By contrast, "slate" results in a flatter distribution of outcomes, with even the most probable "all grays" pattern having only a ~6% chance <a class="yt-timestamp" data-t="00:11:15">[00:11:15]</a>, yielding an average of 5.8 bits <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. The higher the probability of a pattern, the lower the information it provides <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

Entropy was named by John von Neumann, suggesting it was already used in statistical mechanics and that its mysterious nature would give an advantage in debates <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. For Wordle, [[information_theory_and_entropy_in_wordle | entropy]] simply means the expected information value of a guess <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

Entropy measures:
1.  **How flat the distribution is**: A uniform distribution has higher entropy <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. For 3^5 possible patterns (243), the maximum entropy is 7.92 bits <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
2.  **The number of possibilities**: More patterns generally mean higher entropy <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## Wordle Solver Version 1: Maximizing Entropy

The first version of the Wordle bot implements this strategy:
1.  It iterates through all ~13,000 possible guesses <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
2.  It calculates the [[information_theory_and_entropy_in_wordle | entropy]] for each guess, specifically the entropy of the distribution of all possible color patterns <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
3.  It selects the guess with the highest [[information_theory_and_entropy_in_wordle | entropy]], as this is expected to reduce the space of possibilities the most <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.
4.  This process is repeated for subsequent guesses, playing the same game on the reduced set of possible words <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

An example bot shows "Tares" as the top opening suggestion <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. The bot also displays the expected information vs. actual information gained, and the current uncertainty (entropy) of the remaining possible words <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

*   Simulations of Version 1 against all 2,315 actual Wordle answers yielded an average score of about **4.124** <a class="yt-timestamp" data-t="00:17:54">[00:17:54]</a>. This was considered "not bad" but aimed for improvement <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>.

## Wordle Solver Version 2: Incorporating Word Frequency

The "low-hanging fruit" for improvement was to incorporate how common a word is <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.

### Word Frequency Data
The algorithm utilizes [[word_frequency_data_and_wordle_strategies | word frequency data]], such as the Google Books English Ngram public dataset, to assign probabilities to words <a class="yt-timestamp" data-t="00:18:26">[00:18:26]</a>. Instead of a direct proportionality, a sigmoid function is applied to the sorted list of words to create a more binary probability (0 or 1) with a smooth transition, reflecting that most common words are plausible answers <a class="yt-timestamp" data-t="00:19:21">[00:19:21]</a>.

This non-uniform distribution of word probabilities affects the [[information_theory_and_entropy_in_wordle | entropy]] calculation for both the expected information from a guess and the remaining uncertainty among possible words <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. For instance, if 16 words match a pattern, but 12 are very obscure (low probability), the actual uncertainty (2.11 bits) is much closer to what it would be for only the 4 common words (2 bits), rather than 4 bits (log₂16) <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>.

### Refinements in Version 2
Version 2 incorporates two main differences <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>:
1.  **Refined Entropy Calculation**: The [[information_theory_and_entropy_in_wordle | entropy]] (expected information) for guesses now incorporates the probability that a given word would actually be an answer <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.
2.  **Expected Game Score Decision**: The algorithm models the probability of each word being the actual answer and incorporates this into its decision-making <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>. Instead of purely maximizing information, it aims to minimize the *expected score* of the game <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>. This is done by predicting the probability that a guess is the correct answer and estimating the remaining guesses needed based on the expected uncertainty after the current guess. This estimation uses a function `f` derived from past simulation data, mapping uncertainty (in bits) to the expected number of future guesses <a class="yt-timestamp" data-t="00:26:08">[00:26:08]</a>.

*   Simulations of Version 2 showed an average score of around **3.6** <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>. This version sometimes loses (requires more than six guesses), presumably because it makes tradeoffs to prioritize solving the puzzle over merely maximizing information <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

## Further Optimizations and Limitations

Further improvements are possible, including:
*   **Incorporating the true Wordle answer list**: This can achieve a performance of around **3.43** on average <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>.
*   **Two-step forward search**: The algorithm can search for the expected information two steps ahead instead of just one <a class="yt-timestamp" data-t="00:28:52">[00:28:52]</a>. Initial simulations suggest "Crane" as a strong opener for this approach <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

Even with optimal play, it is likely impossible to consistently achieve an average score as low as three, as there may not be enough room to gain sufficient information after only two steps to guarantee the answer in the third guess every single time <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>. The maximum expected information after the first two guesses is around 10 bits, which means at best, one bit of uncertainty would remain, equivalent to being down to two possible guesses <a class="yt-timestamp" data-t="00:29:26">[00:29:26]</a>.