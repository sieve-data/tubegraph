---
title: AlphaZero and Efficient Search Techniques
videoId: qTogNUV3CAI
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Demis Hassabis, CEO of DeepMind, has discussed the principles behind AlphaZero, a system developed by DeepMind capable of mastering games like Go, chess, and shogi at a superhuman level. A key aspect of AlphaZero's success lies in its highly efficient search techniques, which differ significantly from brute-force methods and offer insights into building more capable AI systems.

## AlphaZero's Search Efficiency

AlphaZero is designed to play any game and has demonstrated performance stronger than human world champions <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. Critically, it achieves this with "a lot less search than a brute force method like Deep Blue to play chess" <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. While traditional systems like Deep Blue or Stockfish might explore millions of possible moves for each decision, AlphaZero and its predecessor AlphaGo examine significantly fewer positions—around "tens of thousands" <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. This is still more than human grandmasters, who might consider only a few hundred moves <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

## The Role of the World Model

The efficiency of AlphaZero's search is intrinsically linked to the quality of its internal "world model" of the game. Hassabis explains, "The better your world model is, the more efficient your search can be" <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Brute-force systems often lack a deep model, relying more on heuristics <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. AlphaGo, and by extension AlphaZero, possess "quite a decent model" <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

This leads to a trade-off: "If you improve the models, then I think your search can be more efficient and therefore you can get further with your search" <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. A sophisticated world model allows the system to "pick which leaf nodes you should expand with search much more accurately," leading to "a lot less search" overall <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. The model can guide the search to a promising "node in a tree," requiring only "a little bit of search around that leaf node" <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

## Comparison with Human Intuition and Search

Human experts, like chess grandmasters or scientists like Einstein, also achieve remarkable results with limited explicit search. Hassabis notes that human brains "are not built for doing Monte Carlo tree search" <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Instead, humans leverage highly accurate mental models, intuition, knowledge, and experience <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. Top human players possess a "much richer, much more accurate model" of their domain, enabling "world-class decisions on a very small amount of search" <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>. No human could perform a brute-force search over any significant space <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

## Learning and Broader Applications

### Self-Play and Active Learning
AlphaZero's powerful model was developed through self-play, where the system "play[s] against each other and actually learn[s] from each other’s mistakes and build[s] up a knowledge base that way" <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Such Reinforcement Learning (RL) agents are "active learners," meaning their decisions influence the subsequent data or experiences they encounter, creating a feedback loop for learning <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.

### Implications for Future AI and AGI
The principles underlying AlphaZero's search are considered crucial for advancing AI capabilities, particularly in conjunction with Large Language Models (LLMs). DeepMind is working on "AlphaZero-like planning mechanisms on top [of LLMs]" <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>. These mechanisms would utilize the LLM as a world model to "make concrete plans to achieve certain goals" and employ search to "explore massive spaces of possibility" <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>, <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This search and planning capability is seen as "kind of missing from our current large models" <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a> and is anticipated to be a necessary component of Artificial General Intelligence (AGI) systems [[the_geopolitical_stakes_of_agi_development]] <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.

While theoretically, an AGI could be developed "full AlphaZero-like," building all knowledge from scratch without priors <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>, Hassabis believes the "quickest way to get to AGI" involves using existing world knowledge (e.g., from the web, ingested by LLMs) as a foundational model or prior, and then augmenting it with planning and search capabilities <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>. Search, alongside reinforcement learning and deep learning, was one of the core algorithmic types DeepMind focused on from its inception due to its potential for scalability and generality [[ai_scalability_and_breakthroughs]] <a class="yt-timestamp" data-t="00:33:39">[00:33:39]</a>.