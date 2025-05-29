---
title: Challenges in realtime strategy game AI
videoId: Kedt2or9xlo
---

From: [[lexfridman]] <br/> 

Real-time strategy (RTS) games present a unique set of challenges in the realm of artificial intelligence (AI) development. Unlike other genres, RTS games require a blend of tactical and strategic decision-making, resource management, and real-time action, often with incomplete information and high computational demands. This article explores the specific challenges involved from both a player's and developer's perspective, largely using insights from the StarCraft series, a seminal RTS game.

## Core Challenges

### Exploration and Action Space

One of the most significant challenges in developing AI for RTS games is handling the vast action space and the exploration problem. In games like StarCraft, the sheer number and variety of actions make it difficult for AI to explore effectively without prior human knowledge:

- **Action Space:** The action space in StarCraft is extremely large, with a myriad of units, buildings, and strategies at any given time. Deciding which units to build, where to place buildings, and which vectors to attack from can be overwhelming for AI to manage without a robust heuristic or learning mechanism <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.
- **Exploration Problem:** Without initial guidance, AI that relies solely on reinforcement learning can struggle to make progress because most actions are initially unproductive. For example, almost any random action early can disrupt the automated gathering of resources, leading to suboptimal outcomes <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.

### Partial Observability and Uncertainty

RTS games inject uncertainty through **partial observability**, meaning the AI does not have complete information about the opponent's actions or strategies:

- **Fog of War:** In StarCraft, the map is partially covered by the fog of war. Information about the enemy is limited until the player actively scouts. This requires the AI to make decisions based on incomplete data, necessitating robust prediction and strategy adaptation mechanics to effectively counter unknown threats <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>.
- **Opponent Modeling:** The AI needs to build models of opponent behavior to make educated guesses about enemy strategies and develop effective counter-strategies, something it can struggle with, particularly against non-standard (or "cheesy") strategies <a class="yt-timestamp" data-t="01:45:25">[01:45:25]</a>.

### Real-Time Decision Making

Unlike turn-based games where each decision can be carefully calculated, RTS games require **rapid decision making:**

- **Speed and Accuracy:** The AI must balance speed with accuracy, executing a series of actions in real time while accurately assessing changing game states. Professional human players can execute between 300 to 800 actions per minute, which is a benchmark for AI performance <a class="yt-timestamp" data-t="00:41:47">[00:41:47]</a>.
- **Micro and Macro Management:** Effective RTS gameplay involves both micromanagement of individual units and macromanagement of larger strategic goals like resource allocation and army composition <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>.

### Long-Term Strategy

RTS games are complex due to their need for multi-scale planning:

- **Resource Management and Timing:** The AI must optimize the balance between gathering resources, expanding territory, and building military units—key elements that significantly influence mid- to late-game outcomes <a class="yt-timestamp" data-t="00:25:19">[00:25:19]</a>.
- **Strategic Variety:** AI needs to exhibit a variety of strategic approaches, from standard economic builds to opportunistic strikes. For example, leveraging strategies like "cheese" (early game all-ins) requires precise timing and adaptation to an opponent’s defense <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>.

## Overcoming the Challenges

### Imitation and Reinforcement Learning

The combination of supervised learning from human game replays and self-play has been key in developing strong AI agents:

- **Imitation Learning:** Using large datasets of human game replays to teach AI foundational strategies and decision patterns, helping to bootstrap further learning <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.

- **Reinforcement Learning through Self-Play:** A league of AI agents competes against one another, allowing different strategies to evolve, akin to how human players improve over time through competition <a class="yt-timestamp" data-t="00:55:44">[00:55:44]</a>.

### Specialized Neural Networks

State-of-the-art AI for RTS games incorporates neural networks capable of processing spatial data (maps and unit positions) alongside temporal sequences (ongoing game states):

- **Transformers and LSTMs:** Utilizing advanced architectures like transformers and LSTMs for capturing long-term dependencies, crucial in planning and executing complex strategies over extended periods <a class="yt-timestamp" data-t="01:19:19">[01:19:19]</a>.

## Conclusion

Developing robust AI for real-time strategy games like StarCraft involves conquering challenges of vast action spaces, partial observability, rapid decision-making, and complex strategy formulation. Successful AI systems in this domain not only enrich our understanding of AI capabilities but also push the boundaries of what is possible in computational strategy and learning algorithms. As AI continues to evolve, the lessons learned from RTS games will undoubtedly inform broader applications across diverse real-world industries and problems.