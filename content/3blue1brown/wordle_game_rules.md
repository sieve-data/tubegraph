---
title: Wordle game rules
videoId: v68zYyaEmEA
---

From: [[3blue1brown]] <br/> 

Wordle, a game that went viral in late 2021/early 2022 <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, serves as an excellent example for understanding [[information_theory_in_gamesolving | information theory]] and entropy <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The objective of the game is to guess a mystery five-letter word <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a> within six attempts <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Gameplay and Feedback

After each guess, players receive feedback on how close their word was to the hidden answer:
*   **Grey Box**: Indicates that a letter is not present in the actual answer <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   **Yellow Box**: Means the letter is in the answer, but it is not in the correct position <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.
*   **Green Box**: Shows that the letter is in the secret word and is in the correct position <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

An example progression might involve starting with "crane", receiving feedback (grey C, yellow R, green A, grey N, grey E), then trying "shtik", and finally guessing "shard" to solve the puzzle in three attempts <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>, <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>, <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>, <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Valid Guesses and Answers

To make a guess, the word entered must be an actual five-letter word <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. The game is "pretty liberal" with its acceptance of valid guesses <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Allowed Guesses**: There is a list of approximately 13,000 words considered valid guesses <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This list includes many uncommon words like "aahed," "aalii," and "aargh" <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.
*   **Possible Answers**: The actual answer is always a "decently common word" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. These answers are drawn from a smaller, human-curated list of about 2,300 words <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This list, along with the daily sequence of answers, is visible in the game's source code <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>, though using this information to "look up tomorrow's answer" is considered cheating <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

## Scoring and Strategy

A common analogy for Wordle scores is that getting the answer in four guesses is "par," while three guesses is a "birdie" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Achieving a score of three "feels great" <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

Developing an [[algorithm_design_for_wordle | algorithm]] to play Wordle optimally often involves concepts from [[information_theory_in_gamesolving | information theory]], particularly entropy, to select guesses that maximize the expected information gained <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. Early [[wordle_strategies_and_optimal_openers | Wordle strategies and optimal openers]] might consider the [[role_of_probability_in_word_guessing | relative frequencies of letters in the English language]] <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. A simple approach to [[optimal_strategy_for_wordle | optimal strategy for Wordle]] involves iterating through all valid guesses, computing the entropy (expected information value) for each, and choosing the one with the highest entropy <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. More advanced strategies incorporate the probability that a given word is actually the answer <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.