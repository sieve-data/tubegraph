---
title: Role of probability in word guessing
videoId: v68zYyaEmEA
---

From: [[3blue1brown]] <br/> 

The popular game Wordle offers a compelling platform for exploring concepts in [[information_theory | information theory]] and the [[entropy | entropy]]. Solving Wordle optimally, particularly through an algorithmic approach, heavily relies on understanding and applying probability <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Wordle Game Overview

Wordle challenges players to guess a mystery five-letter word within six attempts <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. After each guess, players receive feedback indicating how close their guess is to the true answer:
*   **Grey box**: The letter is not in the word <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Yellow box**: The letter is in the word but not in that specific position <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
*   **Green box**: The letter is in the word and in the correct position <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

The game allows approximately 13,000 valid guess words <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>, but the actual answers are drawn from a smaller, human-curated list of about 2,300 common words <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>. An optimal Wordle solver seeks to maximize the information gained with each guess to narrow down possibilities quickly <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

## Early Approaches and Their Limitations

Initial thoughts on designing a Wordle solver might involve:
*   **Letter Frequencies**: Considering the relative frequencies of letters in the English language to choose an opening guess that includes many common letters, like "other" or "nails" <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.
*   **Intuition about "Informative" Letters**: Some players might favor words with uncommon letters (e.g., "weary" with W and Y) for their potential to drastically reduce possibilities if a match occurs <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

However, these approaches lack systematic rigor. Simply knowing a letter is present (green/yellow) or absent (grey) provides [[information | information]] <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>, but a more quantitative measure is needed to judge the overall quality of a potential guess <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>. A key insight is that patterns which provide a lot of information (e.g., heavily reducing the word space) are inherently unlikely to occur <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>. Conversely, the most likely outcomes (like getting all grey boxes) are often the least informative <a class="yt-timestamp" data-t="06:30:00">[06:30:00]</a>.

## Quantifying Information: The Bit

To objectively score potential guesses, the concept of a "bit" of information is introduced, a standard unit developed by Claude Shannon <a class="yt-timestamp" data-t="08:10:00">[08:10:00]</a>:
*   An observation that cuts the space of possibilities in half provides **one bit** of information <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>.
*   Cutting possibilities by a factor of four provides **two bits** <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.
*   Cutting possibilities by a factor of eight provides **three bits** <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>.

The formula for information (I) in bits, given the probability (P) of an occurrence, is:
I = log₂(1/P) or I = -log₂(P) <a class="yt-timestamp" data-t="09:03:00">[09:03:00]</a>.
This logarithmic expression is useful because:
1.  It simplifies discussions of very unlikely events (e.g., "20 bits of information" is easier than a very small probability) <a class="yt-timestamp" data-t="09:39:00">[09:39:00]</a>.
2.  Information is additive: If one observation gives two bits and a second gives three bits, the total is five bits <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>. This is analogous to how probabilities multiply.

## Entropy: The Expected Information Value

To evaluate a guess globally, the **[[entropy | entropy]]** of its potential outcome patterns is calculated. This is the "expected value of information" <a class="yt-timestamp" data-t="10:43:00">[10:43:00]</a>, determined by summing the product of each pattern's probability and its corresponding information value <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>. For example, the word "weary" might yield an average of 4.9 bits, while "slate" might yield 5.8 bits, meaning "slate" is expected to reduce the space of possibilities more significantly <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>.

The term "entropy" was suggested to Claude Shannon by John von Neumann, partly because "nobody knows what entropy really is, so in a debate you'll always have the advantage" <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>. In this context, [[entropy | entropy]] measures two things simultaneously <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>:
1.  **Flatness of the distribution**: A more uniform distribution of possible outcomes results in higher [[entropy | entropy]] <a class="yt-timestamp" data-t="12:54:00">[12:54:00]</a>.
2.  **Number of possibilities**: More potential outcomes inherently lead to higher [[entropy | entropy]] <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>. An [[entropy | entropy]] of 6 bits, for instance, implies a level of uncertainty equivalent to 64 equally likely outcomes <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.

## Wordle Bot Version 1: Maximizing Entropy

The first version of a Wordle solver focused on maximizing [[entropy | entropy]] <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>. It iterates through all ~13,000 valid guess words, calculates the [[entropy | entropy]] of the pattern distribution for each (initially assuming all words are equally likely to be the answer), and selects the word with the highest [[entropy | entropy]] <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>. This process is repeated for subsequent guesses, playing the same game with the reduced set of remaining possibilities <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>.

This naive approach, when tested against the 2,315 actual Wordle answers, achieved an average score of about 4.124 guesses <a class="yt-timestamp" data-t="17:50:00">[17:50:00]</a>. While respectable, players often aim for an average closer to 3 or 4 <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

## Refining Probability Models: Incorporating Word Frequency

To improve performance, the algorithm must move beyond the assumption that all words are equally likely to be the answer <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. This involves incorporating real-world word frequency data, such as that from the Google Books English Ngram dataset <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a>.

Instead of directly using raw frequencies, a **sigmoid function** can be applied to create a more binary-like probability for each word, reflecting whether it's common enough to be a plausible answer <a class="yt-timestamp" data-t="19:19:00">[19:19:00]</a>. This assigns a probability to each word being the *final answer*, not just being a valid guess.

This refined probability distribution affects the [[entropy | entropy]] calculation for a given guess. For example, if a pattern matches 16 words, but 12 of them are extremely obscure, the "actual uncertainty" (entropy) is much lower than if all 16 were common, as the obscure words carry little weight in the probability distribution <a class="yt-timestamp" data-t="20:54:00">[20:54:00]</a>.

This leads to two distinct but related applications of [[entropy | entropy]] in Wordle:
1.  **Expected information from a guess**: How much the chosen word is expected to reduce possibilities.
2.  **Remaining uncertainty among possible words**: A measure of how many "effective" possibilities are left, given their assigned probabilities <a class="yt-timestamp" data-t="22:01:00">[22:01:00]</a>.

## Wordle Bot Version 2: Prioritizing Common Words

Version 2 of the Wordle bot incorporates these refined probability distributions <a class="yt-timestamp" data-t="23:22:00">[23:22:00]</a>. It still calculates [[entropy | entropy]] for guesses, but now factoring in the probability of each word being the actual answer. Furthermore, in later stages of the game, it prioritizes guesses that are themselves likely answers, even if they don't strictly maximize information, to target a swift win <a class="yt-timestamp" data-t="24:48:00">[24:48:00]</a>. This involves estimating the expected final score based on the current uncertainty and the information a potential guess might yield <a class="yt-timestamp" data-t="25:28:00">[25:28:00]</a>.

By running simulations with Version 2, the average score improved to approximately 3.6 guesses <a class="yt-timestamp" data-t="27:54:00">[27:54:00]</a>. This version occasionally loses (exceeds six guesses) because it sometimes trades off pure information gain for the goal of guessing the most probable answer <a class="yt-timestamp" data-t="28:06:00">[28:06:00]</a>.

Further optimizations, such as incorporating the official Wordle answer list or performing a two-step lookahead for expected information, can further refine the strategy <a class="yt-timestamp" data-t="28:23:00">[28:23:00]</a>. The initial uncertainty for the true Wordle list is about 11 bits <a class="yt-timestamp" data-t="29:10:00">[29:10:00]</a>, and optimal play suggests that after two guesses, it's possible to reduce this to approximately one bit of uncertainty, leaving two possible answers <a class="yt-timestamp" data-t="29:20:00">[29:20:00]</a>. However, achieving an average score of three or less is likely impossible due to limitations in the available words and the information gain after only two steps <a class="yt-timestamp" data-t="29:37:00">[29:37:00]</a>.