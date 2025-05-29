---
title: Wordle game mechanics
videoId: v68zYyaEmEA
---

From: [[3blue1brown]] <br/> 

The game of [[Wordle]] gained significant popularity in recent months <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It serves as a good example for a lesson on [[Information theory and entropy in Wordle | information theory]], particularly the concept of [[Information theory and entropy in Wordle | entropy]] <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Many programmers, in addition to playing the puzzle, have attempted to write an [[Algorithms for optimal Wordle play | algorithm]] to play the game as optimally as possible <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## How to Play Wordle

The objective of [[Wordle]] is to guess a mystery five-letter word <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Players are given six different chances to guess <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Each guess must be an actual five-letter word <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### Receiving Information from Guesses

Each time a guess is made, the player receives information about how close their guess is to the true answer <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This information is conveyed through colored boxes:

*   **Grey box**: Indicates that the letter is not in the actual answer <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Yellow box**: Indicates that the letter is in the word, but not in that specific position <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Green box**: Indicates that the letter is in the secret word and is in the correct position <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

For example, if the guess is "crane" and the result is grey, yellow, green, grey, grey <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>:
*   'C' is not in the answer.
*   'R' is in the answer, but not in the second position.
*   'A' is in the answer and is in the third position.
*   'N' and 'E' are not in the answer.

### Word Lists in Wordle

There are two primary lists of words relevant to [[Wordle]] gameplay:

1.  **Valid Guess List**: This list comprises about 13,000 words that are accepted as valid guesses <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This list includes many uncommon words <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
2.  **Possible Answer List**: This is a smaller, human-curated list of about 2,300 words that are the possible answers <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. These answers are typically more common words <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

While the official answer list is visible in the game's source code, revealing the daily answers <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>, a more interesting challenge for developing an [[Algorithms for optimal Wordle play | algorithm]] is to not incorporate this specific list <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. Instead, using [[Word frequency data and Wordle strategies | universal word frequency data]] captures the intuition of preferring more common words without "cheating" <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Wordle Scoring

A player's score in [[Wordle]] is determined by the number of guesses it takes to find the mystery word. An apt analogy suggests that getting it in four guesses is "par," while getting it in three guesses is a "birdie" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Achieving a score of three feels particularly good <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. An [[Algorithms for optimal Wordle play | algorithm]] that aims to maximize [[Information theory and entropy in Wordle | information]] at each step, without considering word commonality, can achieve an average score of about 4.124 <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>. Incorporating [[Word frequency data and Wordle strategies | word frequency data]] to guide guesses can improve the average score to around 3.6 <a class="yt-timestamp" data-t="00:28:04">[00:28:04]</a>. Further sophistication, such as a two-step lookahead search, can lead to an average performance around 3.43 <a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a>. It's suggested that achieving an average score as low as three may not be possible due to the inherent information limits after only two steps <a class="yt-timestamp" data-t="00:29:41">[00:29:41]</a>.