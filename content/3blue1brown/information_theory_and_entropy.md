---
title: Information theory and entropy
videoId: v68zYyaEmEA
---

From: [[3blue1brown]] <br/> 

The game Wordle has become a popular subject for exploring [[concepts_in_information_theory_and_coding_theory | information theory]], particularly the concept of [[information_theory_in_gamesolving | entropy]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. An algorithm designed to play Wordle optimally can be built around this idea <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## Wordle Basics

The objective of Wordle is to guess a mystery five-letter word within six attempts <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. After each guess, players receive feedback:
*   **Grey box:** The letter is not in the answer <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Yellow box:** The letter is in the answer but in the wrong position <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Green box:** The letter is correct and in the right position <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

For example, starting with "crane" might yield grey-yellow-green-grey-grey, indicating no 'C', an 'R' in the wrong spot, an 'A' in the third position, and no 'N' or 'E' <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. The game's difficulty is often compared to golf, where four guesses is "par" and three is a "birdie" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Initial Strategies and Limitations

Early attempts to solve Wordle often involved analyzing the relative frequencies of letters in the English language <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. An opening strategy might involve guessing words like "other" followed by "nails" to hit many frequent letters <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>. Even if a guess results in all grey boxes, it provides significant information by eliminating common letters <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. However, this approach is not systematic as it doesn't account for letter order or positional information <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

## Wordle's Lexicon

Wordle uses two main word lists:
*   **Valid Guesses:** Approximately 13,000 words that can be entered as guesses <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This list includes many uncommon words like "aahed" or "aalii" <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **Possible Answers:** A human-curated list of about 2,300 words that are the actual daily answers <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

For developing an optimal solver, it is preferable not to incorporate prior knowledge of the human-curated answer list <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. This ensures the program is more resilient and not reliant on data visible in the game's source code, which could be considered "cheating" <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Instead, the approach should leverage more universal data, such as general word frequencies, to capture intuitions about common words <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Quantifying Guess Quality with Information Theory

The quality of a potential guess can be assessed quantitatively <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. A pattern that reveals a lot of information, such as one matching only 58 words out of 13,000, is by its nature unlikely to occur <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Conversely, the most likely outcomes (e.g., a pattern with no matches) are the least informative <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Bits: The Unit of Information

The standard unit of information is the **bit** <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   An observation that halves the space of possibilities provides one bit of information <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   Cutting possibilities by a factor of four yields two bits <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   Cutting possibilities by a factor of eight yields three bits <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.

The formula for information (in bits) in terms of the probability (P) of an occurrence is:
$$ \text{Information (bits)} = \log_2 \left( \frac{1}{\text{P}} \right) = - \log_2 (\text{P}) $$ <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>

This logarithmic scale is advantageous because it makes it easier to describe unlikely events (e.g., 20 bits of information is simpler than a probability of 0.0000095) <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>. More substantively, information adds together: if one observation provides two bits and a second provides three bits, together they give five bits <a class="yt-timestamp" data-t="00:10:02">[00:10:02]</a>. This additive property is very useful when dealing with expected values, where multiple outcomes are summed <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.

### Entropy: Expected Information Value

In the context of Wordle, the quality of a guess is measured by the **expected amount of information** it yields from the distribution of possible patterns <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This expected information value is known as [[concepts_in_information_theory_and_coding_theory | entropy]] <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

The term "entropy" was suggested by John von Neumann to Claude Shannon, who developed information theory. Von Neumann reportedly advised Shannon to call it entropy because the mathematical function had been used in statistical mechanics under that name, and also because "nobody knows what entropy really is, so in a debate you'll always have the advantage" <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. For Wordle, entropy represents the expected information value of a particular guess <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.

Entropy simultaneously measures two things:
1.  **Flatness of Distribution:** The closer a distribution is to uniform, the higher its entropy <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. For Wordle's 3^5 possible patterns, the theoretical maximum entropy is `log2(3^5)` or 7.92 bits <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.
2.  **Number of Possibilities:** Entropy also reflects how many possibilities exist <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>. For instance, if there are 16 equally likely patterns, the entropy is 4 bits; if there are 64 equally likely patterns, it's 6 bits <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.

### Wordlebot Version 1: Maximizing Entropy

The first version of a Wordle solver (the "Wurtelebot") works by:
1.  Iterating through all ~13,000 valid guesses <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.
2.  Computing the entropy for each guess, assuming all possible answers are equally likely <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
3.  Picking the guess with the highest entropy, as this is expected to reduce the space of possibilities as much as possible <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

This strategy applies to subsequent guesses as well: after a pattern is revealed, the bot plays the same game with the reduced set of possible words <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
When simulated against all 2,315 actual Wordle answers, this naive method achieves an average score of approximately 4.124 guesses <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

## Refining the Model with Word Frequencies

To improve the solver, word frequencies are incorporated <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>. Data from sources like the Google Books English Ngram public dataset can provide relative frequencies for English words <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.

To model how likely each word is to be the final answer, a sigmoid function is applied to the sorted list of words by frequency <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>. This assigns a probability between 0 and 1, effectively creating a "binary cutoff" where common words have high probabilities and obscure ones have low probabilities <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.

When word probabilities are unequal, entropy remains a useful measurement <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. For example, if there are 16 matching words but 12 are very obscure, the actual uncertainty (entropy) is much closer to what it would be if only the 4 common words were considered <a class="yt-timestamp" data-t="00:21:02">[00:21:02]</a>. The expected information from a guess is then calculated using this non-uniform distribution <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>.

### Wordlebot Version 2: Incorporating Probabilities

Version 2 of the Wordlebot differs in two key ways:
1.  **Refined Entropy Calculation:** The expected information (entropy) for guesses now incorporates the probability that a given word would actually be the answer <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.
2.  **Probability Model for Answers:** The bot maintains a model of the probability that each remaining word is the actual answer <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>.

A new "uncertainty measurement" tracks the entropy of the current distribution of possible words <a class="yt-timestamp" data-t="00:24:04">[00:24:04]</a>. This number indicates the effective number of equally likely outcomes, even if the total count of matching words is higher due to obscure possibilities <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>.

For endgame strategy, the bot shifts from purely maximizing information to minimizing the *expected score* <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>. It estimates the expected score by considering the probability of guessing correctly immediately and the likely remaining uncertainty for other outcomes <a class="yt-timestamp" data-t="00:25:28">[00:25:28]</a>. This estimation uses a regression function (f) that maps uncertainty (in bits) to the expected number of remaining guesses, based on data from previous simulations <a class="yt-timestamp" data-t="00:26:14">[00:26:14]</a>.

Simulating version 2 against all 2,315 Wordle answers shows an improved average score of approximately 3.6 guesses <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>. However, it occasionally requires more than six guesses, as it sometimes prioritizes winning over strictly maximizing information <a class="yt-timestamp" data-t="00:28:06">[00:28:06]</a>.

## Further Optimization and Limits

Incorporating the *true* list of Wordle answers into the model can further improve performance, achieving an average score of around 3.43 <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>. This involves more sophisticated techniques, such as looking two steps ahead in terms of expected information gain <a class="yt-timestamp" data-t="00:28:52">[00:28:52]</a>. With the true Wordle list, the initial uncertainty is a little over 11 bits <a class="yt-timestamp" data-t="00:29:14">[00:29:14]</a>. Even with optimal play, the maximum expected information after two guesses is around 10 bits, suggesting that about one bit of uncertainty will remain <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>. This means it's usually down to two possible answers <a class="yt-timestamp" data-t="00:29:34">[00:29:34]</a>. It's unlikely that an algorithm could consistently achieve an average score as low as three, as there isn't enough room to gain sufficient information in just two steps to guarantee the answer every time <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>.