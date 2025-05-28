---
title: Application of Monte Carlo Tree Search MCTS in Language Models
videoId: vOA9JSDPJs0
---

From: [[hu-po]] <br/> 

The concept of Q* (Q-star) is rumored to be a specific method or algorithm utilized by OpenAI to achieve a significant step-function improvement in the current state of artificial intelligence <a class="yt-timestamp" data-t="02:51:39">[02:51:39]</a>. While shrouded in mystery, leading experts like Yann LeCun suggest that Q* is likely an attempt at integrating [[Large Language Models and Optimization | planning]] and reinforcement learning (RL) <a class="yt-timestamp" data-t="04:01:54">[04:01:54]</a>. This approach, though hyped, builds upon decades of existing reinforcement learning research <a class="yt-timestamp" data-t="04:14:15">[04:14:15]</a>.

## Modern Approaches to [[Advancements in language models | Language Models]]

Currently, the performance of [[LLM Large Language Models development | large language models]] (LLMs) is enhanced primarily through [[Training and Finetuning of Language Models for Code | advanced prompting techniques]] and [[Training and Finetuning of Language Models for Code | fine-tuning]] with high-quality data <a class="yt-timestamp" data-t="09:16:16">[09:16:16]</a>. This fine-tuning, involving supervised learning on instruction-tuned datasets, complements the self-supervised pre-training of LLMs <a class="yt-timestamp" data-t="09:30:16">[09:30:16]</a>. However, these methods are constrained by the availability and quality of data <a class="yt-timestamp" data-t="09:56:49">[09:56:49]</a>.

## Monte Carlo Tree Search (MCTS) for Self-Improvement

A proposed strategy allows LLMs to refine their outputs and learn from self-assessed rewards, leading to self-improvement <a class="yt-timestamp" data-t="10:01:13">[10:01:13]</a>. This method draws inspiration from AlphaGo, a pivotal success story in reinforcement learning, leading to the concept of "AlphaLLM" <a class="yt-timestamp" data-t="10:21:05">[10:21:05]</a>.

### AlphaGo and Self-Play
Search algorithms like MCTS have enabled models to learn from self-play, achieving and even surpassing human performance in complex tasks such as the game of Go <a class="yt-timestamp" data-t="12:46:58">[12:46:58]</a>. AlphaGo initially used imitation learning on expert human data but achieved superhuman performance through reinforcement learning on self-play <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>. This self-play fosters the emergence of novel tactics by exploring potential moves through statistical sampling of a large search space <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.

### Challenges in Applying MCTS to LLMs
While effective in games like Go, applying MCTS to LLMs presents unique challenges:
*   **Vast Search Space**: The action space in natural language is enormous. Each token prediction can involve choosing from 30,000 possible tokens <a class="yt-timestamp" data-t="15:38:00">[15:38:00]</a>. This leads to an exponentially expanding search space <a class="yt-timestamp" data-t="33:28:00">[33:28:00]</a>.
*   **Subjective Feedback**: Unlike games with clear win/loss signals, evaluating the quality of natural language responses is fuzzy and lacks unambiguous environmental feedback <a class="yt-timestamp" data-t="16:07:00">[16:07:00]</a>. This makes deriving a clear reward signal difficult <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>.
*   **Data Scarcity**: There isn't an abundance of "expert games" or annotated data for language tasks compared to Go <a class="yt-timestamp" data-t="18:54:00">[18:54:00]</a>.

## AlphaLLM: An MCTS Framework for LLMs
AlphaLLM, as proposed in the paper "Toward Self-Improvement of LLMs via Imagination, Searching and Criticizing" <a class="yt-timestamp" data-t="06:35:46">[06:35:46]</a>, addresses these challenges with an "imagination, searching, and criticizing" framework that does not require additional human annotations <a class="yt-timestamp" data-t="19:08:00">[19:08:00]</a>.

### Core Components
AlphaLLM involves:
1.  **MCTS Decoding**: Instead of greedily picking the next token, MCTS decoding looks ahead, evaluating potential sequences of tokens to find the best path <a class="yt-timestamp" data-t="21:06:00">[21:06:00]</a>.
2.  **Imagination Component**: The LLM synthesizes its own data to push gradients back into itself <a class="yt-timestamp" data-t="31:03:00">[31:03:00]</a>.
3.  **Efficient Search (N-MCTS)**: Guides the search for high-quality trajectories based on the value of each trajectory <a class="yt-timestamp" data-t="30:16:00">[30:16:00]</a>.

### Adapting MCTS for Language
To navigate the vast search space of language, AlphaLLM introduces:
*   **Option-Level MCTS**: Instead of evaluating at the token level, which is computationally expensive, actions are considered at the sentence or "option" level <a class="yt-timestamp" data-t="33:36:00">[33:36:00]</a>. A "termination function" is introduced to determine the variable length of these options <a class="yt-timestamp" data-t="34:24:00">[34:24:00]</a>.
*   **Heuristic Filtering**: To prevent exploring similar or redundant subtrees, the model uses a heuristic function (e.g., cosine similarity of embeddings) to measure the similarity between existing options and filter out overly similar paths <a class="yt-timestamp" data-t="40:26:00">[40:26:00]</a>.
*   **Fast Rollout Policy**: A smaller, specialized language model is used for rapid simulation during tree expansion, making the search more efficient <a class="yt-timestamp" data-t="42:01:00">[42:01:00]</a>.

### Critics (Value Functions)
Critics, or value functions, provide a reliable guidance signal towards achieving the end goal <a class="yt-timestamp" data-t="48:04:00">[48:04:00]</a>. AlphaLLM uses three types:
*   **Value Function (V)**: A language model with a small multi-layer perceptron (MLP) head that outputs a single number, estimating the sum of discounted future rewards for a given state <a class="yt-timestamp" data-t="52:50:00">[52:50:00]</a>.
*   **Process Reward Model (PRM)**: Provides feedback for each step in a "Chain of Thought" <a class="yt-timestamp" data-t="48:57:00">[48:57:00]</a>. It's formulated as a text generation task, initialized from the policy model, and uses a detailed rubric to evaluate each step <a class="yt-timestamp" data-t="53:48:00">[53:48:40]</a>.
*   **Outcome Reward Model (OMM)**: Provides feedback for the complete trajectory or final result <a class="yt-timestamp" data-t="48:53:00">[48:53:00]</a>, similar to a game's win/loss signal <a class="yt-timestamp" data-t="49:28:00">[49:28:00]</a>.

These critics allow the system to learn which trajectories are good, back-propagating gradients to improve the policy (the LLM) over time <a class="yt-timestamp" data-t="37:27:00">[37:27:00]</a>.

### Results and Limitations
AlphaLLM, starting from Llama 2 70B, demonstrated significant performance improvements on mathematical reasoning problems like GSM8K (from 57% to 92%) and Math (from 20% to 51%) <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>. This performance is comparable to GPT-4 on these specific tasks <a class="yt-timestamp" data-t="18:27:00">[18:27:00]</a>.

However, the improvement is largely dependent on using MCTS during inference; the language model itself isn't *inherently* much smarter when used with greedy decoding <a class="yt-timestamp" data-t="1:02:27">[1:02:27]</a>. Furthermore, the paper only demonstrated results over two iterations of self-improvement <a class="yt-timestamp" data-t="1:04:47">[1:04:47]</a>, suggesting potential limitations to continuous improvement, possibly due to static critic models or challenges in balancing training dynamics akin to generative adversarial networks <a class="yt-timestamp" data-t="1:07:09">[1:07:09]</a>.

## Theoretical Justification: LLMs as Q-Functions
The paper "From R to Q*: Your Language Model is Secretly a Q Function" <a class="yt-timestamp" data-t="1:09:53">[1:09:53]</a> provides theoretical support for viewing LLMs within an RL framework. It argues that Direct Preference Optimization (DPO), a method for [[Training and Finetuning of Language Models for Code | training language models]] using preferences, can be effectively seen as a Q-learning algorithm that satisfies the Bellman equation <a class="yt-timestamp" data-t="1:20:12">[1:20:12]</a>.

This paper highlights that while language models often use terminology like "input sequence X" and "output sequence Y," these can be reframed as "states" and "actions" in an RL context <a class="yt-timestamp" data-t="1:22:20">[1:22:20]</a>. Crucially, it posits that an LLM is *always* the optimal soft Q-function for some reward function in a token-level Markov Decision Process (MDP) <a class="yt-timestamp" data-t="1:28:28">[1:28:28]</a>. This is significant because natural language, being composed of a limited set of discrete tokens, fits the discrete action space requirements for many RL algorithms <a class="yt-timestamp" data-t="1:30:43">[1:30:43]</a>.

The paper also addresses the "credit assignment problem" in natural language: how to determine which specific tokens in a long sequence contributed most to a correct or desired outcome <a class="yt-timestamp" data-t="1:33:04">[1:33:04]</a>. The ability to perform credit assignment, especially with offline data, is seen as a promising sign for future [[Large language models in machine learning research | generalization]] and [[Large language models and optimization | optimal exploration behavior]] in LLM agents and [[Large language models in machine learning research | robotics]] <a class="yt-timestamp" data-t="1:34:25">[1:34:25]</a>.

## Conclusion
The application of MCTS and reinforcement learning principles to LLMs, as demonstrated by AlphaLLM and theoretically justified by the concept of LLMs as Q-functions, marks a significant step towards self-improving AI. While current breakthroughs are primarily in domains with unambiguous feedback like math and coding, the potential to extend these self-play loops to general natural language reasoning or [[Large language models in machine learning research | robotics]] remains a subject of intense research and speculation <a class="yt-timestamp" data-t="1:15:00">[1:15:00]</a>. The continuous improvement and ability to generate superhuman-level data through self-play is the core promise of this approach, potentially leading to truly advanced [[Advancements in language models | AI capabilities]] <a class="yt-timestamp" data-t="0:55:00">[0:55:00]</a>.