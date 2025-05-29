---
title: Probability and information measurement
videoId: v68zYyaEmEA
---

From: [[3blue1brown]] <br/> 

The game Wordle serves as a central example for understanding information theory and, in particular, a topic known as entropy <a class="yt-timestamp" data-t="00:00:08">00:00:08</a>. An algorithm can be written to play Wordle optimally by centering on the idea of entropy <a class="yt-timestamp" data-t="00:00:28">00:00:28</a>.

## Wordle: A Case Study in Information Theory

The objective of Wordle is to guess a mystery five-letter word within six chances <a class="yt-timestamp" data-t="00:00:58">00:00:58</a>. After each guess, information is provided about how close the guess is to the true answer <a class="yt-timestamp" data-t="00:01:07">00:01:07</a>:
*   **Grey box**: The letter is not in the actual answer <a class="yt-timestamp" data-t="00:01:10">00:01:10</a>.
*   **Yellow box**: The letter is in the word but not in that position <a class="yt-timestamp" data-t="00:01:14">00:01:14</a>.
*   **Green box**: The letter is in the secret word and in the correct position <a class="yt-timestamp" data-t="00:01:18">00:01:18</a>.

The game has a list of about 13,000 words considered valid guesses <a class="yt-timestamp" data-t="00:03:54">00:03:54</a>. However, only about 2,300 words are possible answers, a human-curated list <a class="yt-timestamp" data-t="00:04:14">00:04:14</a>. To make the problem more interesting and resilient, a solving program should avoid incorporating this specific answer list and instead use more universal data like relative word frequencies to prefer common words <a class="yt-timestamp" data-t="00:05:06">00:05:06</a>.

## Quantifying Information: The Bit

Information theory seeks to explain what information is and what entropy is <a class="yt-timestamp" data-t="00:02:40">00:02:40</a>. The standard unit of information is the "bit" <a class="yt-timestamp" data-t="00:08:10">00:08:10</a>. An observation that halves the space of possibilities provides one bit of information <a class="yt-timestamp" data-t="00:08:21">00:08:21</a>.
*   Cutting possibilities by a factor of two: 1 bit <a class="yt-timestamp" data-t="00:08:21">00:08:21</a>.
*   Cutting possibilities by a factor of four: 2 bits <a class="yt-timestamp" data-t="00:08:39">00:08:39</a>.
*   Cutting possibilities by a factor of eight: 3 bits <a class="yt-timestamp" data-t="00:08:47">00:08:47</a>.

The formula for information (in bits) in terms of the [[probability_density_and_distribution | probability]] of an occurrence is:
*   `Information = log₂ (1 / Probability)` <a class="yt-timestamp" data-t="00:09:17">00:09:17</a>
*   Equivalently, `Information = -log₂ (Probability)` <a class="yt-timestamp" data-t="00:09:24">00:09:24</a>

This logarithmic unit is preferred because it simplifies discussing very unlikely events <a class="yt-timestamp" data-t="00:09:43">00:09:43</a>, and more substantially, information adds together <a class="yt-timestamp" data-t="00:10:02">00:10:02</a>. For example, two observations providing two and three bits respectively, combine to give five bits of information <a class="yt-timestamp" data-t="00:10:14">00:10:14</a>.

## Entropy: Expected Information Value

In the context of Wordle, a pattern with a lot of information is inherently unlikely to occur <a class="yt-timestamp" data-t="00:06:04">00:06:04</a>. What it means to be informative is that it is unlikely <a class="yt-timestamp" data-t="00:06:07">00:06:07</a>. The most likely outcomes provide the least information <a class="yt-timestamp" data-t="00:06:30">00:06:30</a>.

To judge the overall quality of a guess, a "measure of the expected amount of information" is needed from the [[probability_density_and_distribution | distribution]] of possible patterns <a class="yt-timestamp" data-t="00:07:31">00:07:31</a>. This measure is calculated by multiplying each pattern's [[probability_density_and_distribution | probability]] of occurring by how informative it is <a class="yt-timestamp" data-t="00:07:39">00:07:39</a>.

This expected value of information is called **entropy** <a class="yt-timestamp" data-t="00:12:10">00:12:10</a>. Claude Shannon, the developer of information theory, adopted the name "entropy" on the suggestion of John von Neumann, partly because the "uncertainty function" was already known by that name in statistical mechanics, and partly because "nobody knows what entropy really is, so in a debate you'll always have the advantage" <a class="yt-timestamp" data-t="00:12:22">00:12:22</a>. For the purpose of Wordle, entropy simply means the expected information value of a particular guess <a class="yt-timestamp" data-t="00:12:45">00:12:45</a>.

Entropy measures two things simultaneously <a class="yt-timestamp" data-t="00:12:54">00:12:54</a>:
1.  **Flatness of the distribution**: The closer a [[probability_density_and_distribution | distribution]] is to uniform, the higher its entropy <a class="yt-timestamp" data-t="00:12:57">00:12:57</a>. For example, with 3^5 (243) total patterns, the absolute maximum entropy for a uniform distribution would be log₂(3^5) = 7.92 bits <a class="yt-timestamp" data-t="00:13:11">00:13:11</a>.
2.  **Number of possibilities**: Entropy also indicates how many possibilities exist in the first place <a class="yt-timestamp" data-t="00:13:20">00:13:20</a>. An entropy of 6 bits suggests as much variation and uncertainty as if there were 64 equally likely outcomes <a class="yt-timestamp" data-t="00:13:49">00:13:49</a>.

## Wordle Bot: Applying Entropy

### Version 1: Maximizing Information Gain

The first version of a Wordle solving bot calculates the entropy for each of the 13,000 possible guesses and selects the one with the highest entropy <a class="yt-timestamp" data-t="00:14:05">00:14:05</a>. This maximizes the expected reduction in the space of possibilities <a class="yt-timestamp" data-t="00:14:13">00:14:13</a>. This process is repeated for subsequent guesses based on the reduced set of possible words <a class="yt-timestamp" data-t="00:14:27">00:14:27</a>. In this naive approach, it is assumed each word is equally likely to be the answer <a class="yt-timestamp" data-t="00:15:38">00:15:38</a>.

When simulating this version against all 2,315 actual Wordle answers, the average score was approximately 4.124 guesses <a class="yt-timestamp" data-t="00:17:54">00:17:54</a>.

### Version 2: Incorporating Word Frequencies

To improve performance, common word frequencies can be incorporated into the model <a class="yt-timestamp" data-t="00:18:11">00:18:11</a>. This involves assigning a [[probability_density_and_distribution | probability]] to each word for being the final answer, not just based on its frequency, but using a sigmoid function to create a "binary cutoff" that smooths the likelihood between common and obscure words <a class="yt-timestamp" data-t="00:19:33">00:19:33</a>.

With a non-uniform [[probability_density_and_distribution | distribution]] across words, entropy becomes a useful measurement in two ways <a class="yt-timestamp" data-t="00:22:01">00:22:01</a>:
1.  **Expected Information from a Guess**: The entropy calculation for a guess's expected information now incorporates the [[probability_density_and_distribution | probability]] that a given word would actually be the answer <a class="yt-timestamp" data-t="00:23:33">00:23:33</a>.
2.  **Remaining Uncertainty**: It measures the remaining uncertainty among the possible words, reflecting that obscure words contribute less to the "true" uncertainty <a class="yt-timestamp" data-t="00:21:33">00:21:33</a>.

Version 2 of the Wordle bot not only uses these refined entropy calculations but also incorporates a model of the [[probability_density_and_distribution | probability]] that each word is the actual answer into its decision-making <a class="yt-timestamp" data-t="00:23:52">00:23:52</a>. It aims to minimize the expected final score rather than just maximizing information at each step <a class="yt-timestamp" data-t="00:25:28">00:25:28</a>. This is done by estimating the expected number of remaining guesses based on the current uncertainty, often derived from previous game data <a class="yt-timestamp" data-t="00:27:18">00:27:18</a>.

Simulations of Version 2 showed an improved average score of approximately 3.6 guesses <a class="yt-timestamp" data-t="00:28:04">00:28:04</a>, though it occasionally failed to solve within six guesses <a class="yt-timestamp" data-t="00:28:09">00:28:09</a>.

## Limits and Further Refinements

The best performance achieved by incorporating the true Wordle answer list and more sophisticated search strategies (like a two-step lookahead) was around 3.43 guesses <a class="yt-timestamp" data-t="00:28:35">00:28:35</a>.

Even with optimal play, it is suggested that an algorithm could never consistently achieve an average score as low as three <a class="yt-timestamp" data-t="00:29:44">00:29:44</a>. This is because there isn't enough room to gain sufficient information after only two steps to guarantee the answer in the third slot every time <a class="yt-timestamp" data-t="00:29:51">00:29:51</a>. The maximum expected information after the first two guesses is around 10 bits, which would still leave approximately one bit of uncertainty, equivalent to two possible guesses <a class="yt-timestamp" data-t="00:29:34">00:29:34</a>.