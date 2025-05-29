---
title: Applications of Bayes theorem in various fields
videoId: HZGCoVF3YvM
---

From: [[3blue1brown]] <br/> 

[[Understanding Bayes theorem | Bayes' theorem]] is considered one of the most important formulas in probability <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. It is central to scientific discovery <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, a core tool in machine learning and artificial intelligence (AI) <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>, and can even be used for practical applications like treasure hunting <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Key Applications

### Treasure Hunting
In the 1980s, a team led by Tommy Thompson utilized [[Bayesian probability concepts and Bayes rule | Bayesian search tactics]] to locate a ship that had sunk a century and a half prior <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This ship was carrying an estimated $700 million worth of gold in today's terms <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

### Science and Artificial Intelligence
[[Understanding Bayes theorem | Bayes' theorem]] is used by scientists to analyze new data and determine the extent to which it validates or invalidates their models <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Programmers apply it in building AI, specifically when explicitly and numerically modeling a machine's belief <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. The formula allows for the quantification and systematization of changing beliefs <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

## Core Principle: Updating Beliefs with Evidence

A fundamental principle underlying [[Understanding Bayes theorem | Bayes' theorem]] is that new evidence should not completely determine beliefs in a vacuum, but rather [[Bayesian approach to updating beliefs with new evidence | update prior beliefs]] <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. This concept reframes how one thinks about thought itself and the process of changing one's mind <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### The Steve Example
This principle is illustrated through a classic example from a study by psychologists Daniel Kahneman and Amos Tversky <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Their work, which won a Nobel Prize, focused on human judgments and when they irrationally contradict the laws of probability <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

The "Steve" scenario asks whether Steve, described as "very shy and withdrawn, invariably helpful but with very little interest in people or the world of reality. A meek and tidy soul, he has a need for order and structure, and a passion for detail," is more likely to be a librarian or a farmer <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>, <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

Kahneman and Tversky observed that most people conclude Steve is more likely a librarian, based on stereotypical traits <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>, <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. However, this often neglects crucial base-rate information: the ratio of farmers to librarians in the general population <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>, <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. In the US, this ratio was about 20 farmers to 1 librarian according to their paper <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

Applying Bayesian reasoning, one might consider a sample of 200 farmers and 10 librarians <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. If 40% of librarians (4 individuals) and 10% of farmers (20 individuals) fit Steve's description, then among those who fit the description, 4 out of 24 (or 16.7%) would be librarians <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>, <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. Even if a librarian is four times as likely as a farmer to fit the description, the much larger number of farmers means it's still more probable that Steve is a farmer <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### Components of Bayes' Theorem
The general situation where [[Understanding Bayes theorem | Bayes' theorem]] is relevant involves a hypothesis (H) and new evidence (E) <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. The goal is to determine the probability of the hypothesis given the evidence (P(H|E)) <a class="yt-timestamp" data-t="00:05:04">[00:05:04]</a>.

The formula is expressed as:
P(H|E) = P(H) * P(E|H) / P(E)

Where:
*   **P(H)**: The **prior** probability that the hypothesis holds *before* considering the new evidence <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>, <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. (e.g., the general proportion of librarians to farmers).
*   **P(E|H)**: The **likelihood**—the probability of seeing the evidence *given that* the hypothesis is true <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>, <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. (e.g., the proportion of librarians who fit Steve's description).
*   **P(E)**: The total probability of seeing the evidence <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. This is often broken down into two cases:
    *   P(E|H) * P(H) (probability of evidence AND hypothesis)
    *   P(E|not H) * P(not H) (probability of evidence AND not hypothesis)
    Thus, P(E) = P(E|H) * P(H) + P(E|not H) * P(not H) <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>, <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **P(H|E)**: The **posterior** probability—the updated belief about the hypothesis *after* seeing the evidence <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>, <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

## Intuitive Understanding

The "Steve" example demonstrates that the core reasoning behind [[Understanding Bayes theorem | Bayes' theorem]] can be understood by picturing a representative sample and restricting the possibilities based on evidence <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>, <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. The final probability is the proportion of the restricted space where the hypothesis holds true <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

### Visualizing Probability as Area
An effective way to understand [[Understanding Bayes theorem | Bayes' theorem]] and probability more broadly is to think of the space of all possibilities as a 1x1 square, where any event occupies a subset of this space, and its probability is represented by the area of that subset <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. When evidence restricts the possibilities, the new probability for the hypothesis is the proportion it occupies within this new, restricted area <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>, <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

### The Linda Problem
Kahneman and Tversky also conducted an experiment with a fictitious woman named Linda, described with traits suggestive of feminist activism <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>, <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Participants were asked whether it's more likely that Linda is "a bank teller" or "a bank teller and is active in the feminist movement" <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. A significant majority (85%) incorrectly chose the latter <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>, despite the fact that the set of bank tellers who are also feminist activists is a subset of all bank tellers and therefore must be smaller <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.

The error rate dropped to 0% when the question was rephrased using counts (e.g., "Out of 100 people who fit this description, how many are bank tellers and how many are bank tellers who are active in the feminist movement?") <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>, <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>, <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. This highlights that framing probability in terms of specific numbers or proportions (like "40 out of 100") can activate intuitions more effectively than percentages or abstract likelihoods <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.

Ultimately, the core message of [[Understanding Bayes theorem | Bayes' theorem]] is that evidence should update, not solely determine, existing beliefs <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.