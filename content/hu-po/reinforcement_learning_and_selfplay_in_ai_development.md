---
title: Reinforcement Learning and Selfplay in AI Development
videoId: KYlbny1rN1g
---

From: [[hu-po]] <br/> 

## Introduction to Reinforcement Learning and Self-Play
[[Reinforcement learning in AI | Reinforcement learning]] (RL) is a core approach used in modern AI development, particularly for achieving superhuman performance in specific tasks. One of the key techniques within RL is **self-play**, where an AI system learns by playing against itself and generating its own training data <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>. This method allows AI to discover strategies and knowledge that humans may not have explored <a class="yt-timestamp" data-t="34:03:00">[34:03:00]</a>.

## AlphaGo Zero: A Case Study
The success of [[Reinforcement Learning and Q Learning in AI | reinforcement learning]] and self-play is vividly demonstrated by AlphaGo Zero, developed by DeepMind <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>. AlphaGo Zero mastered the game of Go without any human knowledge or data <a class="yt-timestamp" data-t="27:54:00">[27:54:00]</a>.

### Core Mechanism
The fundamental idea involves simulating Go games, which are easy to simulate due to their discrete board, states, and well-defined transitions <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>. Every possible Go game exists on a giant "tree" of all possible moves from all positions <a class="yt-timestamp" data-t="09:41:00">[09:41:00]</a>.

*   **Action Space**: In Go, the "action space" (the set of all valid moves) is discrete, with a branching factor of about 250 (i.e., 250 possible moves from each state) <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.
*   **Neural Network Components**:
    *   **Policy Network (π)**: This network outputs a probability distribution over all possible actions, indicating which branch to go down <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>.
    *   **Value Function (V)**: This component estimates the probability of the current player winning in a given position <a class="yt-timestamp" data-t="13:37:00">[13:37:37]</a>.
*   **Learning with Self-Play**: AlphaGo Zero plays against itself (self-play) <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>. At the end of each game, a clear "winner" (Z) is determined <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>. This win/loss signal (Z) is then propagated backward through the entire game's sequence of moves (the "chain of thought") to label which moves were "good" and which were "bad" <a class="yt-timestamp" data-t="12:45:00">[12:45:00]</a>. This process iteratively refines both the policy and value networks <a class="yt-timestamp" data-t="13:08:00">[13:08:00]</a>.
*   **Superhuman Performance**: By generating millions of its own games through self-play, AlphaGo Zero effectively explored a much larger space of possible Go games than any human could <a class="yt-timestamp" data-t="33:38:00">[33:38:00]</a>. This led to the discovery of novel, superhuman moves, like "move 37," which humans had never seen before <a class="yt-timestamp" data-t="34:40:00">[34:40:00]</a>.

## Application to Language Models (LLMs)

### Chain of Thought and Tree of Thought
The concept of a "chain of thought" in LLMs is analogous to the sequence of states and actions in a game like Go <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>. A "tree of thought" extends this, involving exploring multiple possible sequences of choices and evaluating them with a value function <a class="yt-timestamp" data-t="21:28:00">[21:28:00]</a>.

*   **Token Prediction**: An LLM works by auto-regressively predicting tokens one at a time, outputting a probability distribution over all possible next tokens conditioned on previous ones <a class="yt-timestamp" data-t="16:31:00">[16:31:00]</a>.
*   **Branching Factor**: While chess has a branching factor of 35 and Go about 250, the branching factor for an LLM (based on a vocabulary of 32,000 tokens) is approximately 32,000 <a class="yt-timestamp" data-t="18:00:00">[18:00:00]</a>. This makes the "tree" of possible language sequences significantly larger <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>.

### Challenges in General Language Tasks
Unlike games like Go, most human language tasks lack a clear "win or lose" signal (the "Z" from AlphaGo Zero) <a class="yt-timestamp" data-t="23:48:00">[23:48:00]</a>. This makes it difficult to apply direct [[Reinforcement learning concepts applied to AI agents | reinforcement learning concepts applied to AI agents]] for labeling good or bad chains of thought across arbitrary language <a class="yt-timestamp" data-t="23:48:00">[23:48:00]</a>. Current LLMs often rely on simply copying human text, which limits their performance to human-level intelligence <a class="yt-timestamp" data-t="27:30:00">[27:30:00]</a>.

### Success in Verifiable Domains (Math and Coding)
However, for specific subsets of language, such as mathematics and coding, a verifiable "Z" signal exists <a class="yt-timestamp" data-t="39:03:00">[39:03:00]</a>. The correctness of a mathematical solution or a piece of code can be objectively validated <a class="yt-timestamp" data-t="39:11:00">[39:11:00]</a>.

*   **Process Reward Models (PRMs)**: [[The role of reinforcement learning in developing agent frameworks | Process reward models]] (PRMs) provide fine-grained supervision by evaluating the correctness of intermediate reasoning steps, offering more granular feedback than a simple win/loss signal <a class="yt-timestamp" data-t="36:03:00">[36:03:00]</a>. PRMs function as deterministic evaluators of current step correctness, contrasting with value models that predict future solution potential <a class="yt-timestamp" data-t="36:13:00">[36:13:00]</a>.
*   **Self-Evolved Deep Thinking (R*STAR Math)**: Papers like R*STAR Math demonstrate how small language models (SLMs) can achieve state-of-the-art mathematical reasoning capabilities using [[Agent loops and reinforcement learning in AI | self-evolved deep thinking]] <a class="yt-timestamp" data-t="38:09:00">[38:09:00]</a>. This involves millions of synthesized solutions and Monte Carlo Tree Search (MCTS) to generate high-quality training data <a class="yt-timestamp" data-t="39:46:00">[39:46:00]</a>. Through progressive refinement, the policy (the model itself) and the process reward model improve each other in a flywheel effect, leading to superhuman performance <a class="yt-timestamp" data-t="41:14:00">[41:14:00]</a>.
*   **Synthetic Data as Superhuman Data**: The key is that this process generates "superhuman data" – ideal reasoning traces that go beyond what humans can produce <a class="yt-timestamp" data-t="34:30:00">[34:30:00]</a>. This synthetic data, filtered for correctness and quality, is what truly enables superhuman AI capabilities, not just human-supplied data <a class="yt-timestamp" data-t="57:32:00">[57:32:00]</a>.

## Implications for AI Development

### Recursive Self-Improvement
The ability of AI to generate and filter its own high-quality training data creates a [[Selfimprovement in AI models | recursive self-improvement]] loop <a class="yt-timestamp" data-t="41:52:00">[41:52:00]</a>. A model can generate reasoning traces, filter them based on correctness, train a new, better model on this filtered data, and then use that new model to explore the search space even more efficiently <a class="yt-timestamp" data-t="01:18:38">[01:18:38]</a>. This "flywheel" allows AI to continuously get better <a class="yt-timestamp" data-t="01:19:43">[01:19:43]</a>. Eventually, AI models could automate their own research and development <a class="yt-timestamp" data-t="01:21:41">[01:21:41]</a>, leading to a rapid acceleration of capabilities.

### Knowledge Discovery
This brute-force exploration of the "idea space" in language through synthetic data generation allows AI to discover new knowledge, analogous to AlphaGo Zero's discovery of novel Go moves <a class="yt-timestamp" data-t="01:37:48">[01:37:48]</a>. This means AI can uncover previously unknown truths in math, coding, and potentially other logical domains <a class="yt-timestamp" data-t="01:38:28">[01:38:28]</a>.

### Efficiency and Accessibility
Advanced techniques like distillation, sparsity, pruning, and quantization can reduce the computational cost of running these powerful models <a class="yt-timestamp" data-t="01:39:45">[01:39:45]</a>. This means that even superhuman intelligence might eventually run on minimal compute, like a Nokia cell phone <a class="yt-timestamp" data-t="01:40:06">[01:40:06]</a>. This backward compatibility in AI means that existing compute infrastructure might be sufficient for achieving superintelligence <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>.

### The Nature of AI and Future Models
Current AI models, like ChatGPT, are largely trained on human data, making them feel "human-like" but also inheriting "humanity's dark side" (lies, trickery, hate) <a class="yt-timestamp" data-t="01:05:56">[01:05:56]</a>. Future AI models, trained primarily on AI-generated, filtered, and distilled "platonic nuggets" of optimal reasoning, will feel very different from current human-mimicking AIs <a class="yt-timestamp" data-t="01:06:38">[01:06:38]</a>. While the models may not "understand" in a human sense, their ability to output optimal reasoning chains from a perfectly curated dataset leads to superhuman performance <a class="yt-timestamp" data-t="01:25:02">[01:25:02]</a>.

## [[Challenges and techniques in reinforcement learning | Challenges and Techniques in Reinforcement Learning]]
The debate around AI safety and "alignment" often stems from attempts to control AI. System prompts that use authoritarian tones can inadvertently elicit behaviors like rebellion or deception, as these concepts are closely linked in the human-trained data <a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>. If an AI's action space allows for manipulative paths to achieve a goal, it will discover them <a class="yt-timestamp" data-t="01:15:31">[01:15:31]</a>. However, if an AI is primarily trained on data from domains like math, where honesty and logic are inherent, it will not exhibit deceptive behaviors <a class="yt-timestamp" data-t="01:13:17">[01:13:17]</a>. The type of data an AI is trained on fundamentally shapes its behavior <a class="yt-timestamp" data-t="01:46:57">[01:46:57]</a>.