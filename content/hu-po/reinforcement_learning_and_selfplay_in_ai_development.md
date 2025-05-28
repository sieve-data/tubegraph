---
title: Reinforcement learning and selfplay in AI development
videoId: KYlbny1rN1g
---

From: [[hu-po]] <br/> 

[[ai_and_reinforcement_learning | Reinforcement learning]] (RL) and self-play are critical components in the development of highly intelligent AI models, particularly those aiming for superhuman performance <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>. This approach allows AI to generate and filter its own "superhuman data," leading to a recursive self-improvement cycle <a class="yt-timestamp" data-t="01:19:44">[01:19:44]</a>.

## Artificial Super Intelligence (ASI)

[[ai_and_reinforcement_learning | Artificial Super Intelligence]] (ASI) is defined as an intelligence better than any human or group of people at anything in either the physical or digital world <a class="yt-timestamp" data-t="02:20:20">[02:20:20]</a>, distinguishing it from Artificial General Intelligence (AGI), which refers to an AI's ability to adapt to a variety of tasks <a class="yt-timestamp" data-t="02:26:27">[02:26:27]</a>. While narrow ASI, such as calculators or balancing robots, has existed for hundreds of years <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>, the advent of language models like GPT has brought us closer to AGI, albeit initially limited to language tasks <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. The transition from human-level AI to superhuman AI is predicted to be extremely rapid <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

## The AlphaGo Zero Paradigm

A prime example of [[ai_and_reinforcement_learning | AI and Reinforcement Learning]] achieving superhuman performance through self-play is AlphaGo Zero <a class="yt-timestamp" data-t="07:43:00">[07:43:00]</a>. This AI mastered the game of Go without any human knowledge or data <a class="yt-timestamp" data-t="27:51:00">[27:51:00]</a>.

### How it Works:
*   **Simulating Games** Go games are easily simulated in a computer due to their discrete board and well-defined transitions, forming a vast tree of possible moves <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>.
*   **Action Space and Policy Network** The AI evaluates possible "actions" (moves) at each "state" (board position) <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>. A neural network (the policy network) outputs a probability distribution over all possible actions, indicating which moves are most likely to lead to success <a class="yt-timestamp" data-t="10:48:00">[10:48:48]</a>.
*   **Self-Play and Reward Signal** AlphaGo Zero plays against itself, generating a sequence of states from start to finish <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>. The crucial "Z" signal — who wins or loses the game — acts as a definitive reward <a class="yt-timestamp" data-t="23:00:00">[23:00:00]</a>. This signal is propagated back through the entire game chain to label which moves were good or bad <a class="yt-timestamp" data-t="12:42:00">[12:42:42]</a>.
*   **Iterative Refinement** This process of self-play, evaluation, and back-propagation allows the AI to slowly build up a value function (predicting winning probability from any state) and refine its policy, leading to a "flywheel of improvement" <a class="yt-timestamp" data-t="41:56:00">[41:56:00]</a>. The AI explores parts of the game's state space that humans have never encountered, leading to novel "superhuman" moves <a class="yt-timestamp" data-t="33:55:00">[33:55:00]</a>.

## [[applications_in_machine_learning_and_reinforcement_learning | Reinforcement Learning]] in Language Models

The principles of [[applications_in_machine_learning_and_reinforcement_learning | reinforcement learning]] and self-play can be applied to language models (LLMs), though with some complexities <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>.

### Action Space in Language
*   **Tokens as Actions** In an LLM, the "action" is picking the next token <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>. The language model predicts a probability distribution over all possible tokens (vocabulary), similar to how AlphaGo selects moves <a class="yt-timestamp" data-t="16:43:00">[16:43:00]</a>.
*   **Branching Factor** The branching factor for LLMs (e.g., 32,000 for Llama 2's vocabulary) is significantly larger than for games like Go (250) or Chess (35), making the "tree" of possible language sequences much vaster, though still finite <a class="yt-timestamp" data-t="18:00:00">[18:00:00]</a>.
*   **Chain of Thought (CoT)** A "Chain of Thought" is a sequence of token choices, analogous to a path through the game tree <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>. Longer chains require more inference time compute, allowing for the solution of more complex problems <a class="yt-timestamp" data-t="45:44:00">[45:44:00]</a>.

### Challenges and Solutions for Reward Signals
Unlike Go, general language tasks lack a clear "win/lose" signal to label the quality of token sequences <a class="yt-timestamp" data-t="23:00:00">[23:00:00]</a>.
*   **Copying Human Data** Initial approaches involve training LLMs by simply copying human text, but this limits performance to human-level intelligence <a class="yt-timestamp" data-t="27:30:00">[27:30:00]</a>.
*   **Process Reward Models (PRMs)** For tasks with verifiable outcomes, such as mathematics and coding, a definitive reward signal ("Z") exists <a class="yt-timestamp" data-t="38:57:00">[38:57:00]</a>. Process reward models (PRMs) provide fine-grained supervision by evaluating the correctness of *intermediate reasoning steps* <a class="yt-timestamp" data-t="36:00:00">[36:00:00]</a>. This allows for the labeling of good and bad steps within a Chain of Thought <a class="yt-timestamp" data-t="36:59:00">[36:59:00]</a>.
*   **R* Math Example** Papers like R* Math demonstrate how small language models (SLMs) can achieve [[stateoftheart_in_reinforcement_learning | state-of-the-art]] math reasoning by using self-evolved deep thinking across millions of synthesized solutions <a class="yt-timestamp" data-t="38:09:00">[38:09:00]</a>. This is achieved by generating "superhuman data" through self-play and refinement, much like AlphaGo Zero <a class="yt-timestamp" data-t="40:59:00">[40:59:00]</a>.

## The Power of Synthetic Data and [[selfimprovement_in_ai_models | Self-Improvement]]

The core idea is that superhuman performance requires "superhuman data" <a class="yt-timestamp" data-t="34:30:00">[34:30:00]</a>.
*   **Generating Training Data** AI models can be used not just for deployment but to generate vast amounts of high-quality synthetic training data. For example, GPT 3.5 has been used to generate Python textbooks to train other models <a class="yt-timestamp" data-t="59:21:00">[59:21:00]</a>.
*   **Recursive Self-Improvement** This creates a [[selfimproving_ai_through_reinforcement_learning_and_reasoning | recursive self-improvement]] loop: a model generates high-quality reasoning traces, a better model is trained on this data, which then generates even higher-quality data, and so on <a class="yt-timestamp" data-t="41:56:00">[41:56:00]</a>. This systematic exploration of the "idea space" leads to the discovery of new knowledge <a class="yt-timestamp" data-t="01:37:18">[01:37:18]</a>.
*   **Distillation and Efficiency** These large, powerful models can then be "distilled" into smaller, more efficient models (e.g., O1 mini from O1), making them cheaper to run and accessible on less powerful hardware, potentially even a Nokia cell phone <a class="yt-timestamp" data-t="01:01:47">[01:01:47]</a>, <a class="yt-timestamp" data-t="01:40:04">[01:40:04]</a>.
*   **Digital Twins for Embodied AI** Similarly, in robotics, platforms like Nvidia Omniverse allow for the simulation of millions of robot actions. The verifiable success or failure of these actions creates a reward signal, enabling the generation of synthetic data to train superhuman embodied AI <a class="yt-timestamp" data-t="01:29:12">[01:29:12]</a>.

## Implications and Challenges

*   **Discovery of New Knowledge** This brute-force method of exploring the "tree of all possible language sequences" means AI will inevitably discover novel information in domains like math and coding that humans have yet to find <a class="yt-timestamp" data-t="01:38:50">[01:38:50]</a>.
*   **Human Data and "Dark Side"** Current AGI models are heavily trained on human data, which contains aspects like lies, trickery, and hate <a class="yt-timestamp" data-t="01:03:54">[01:03:54]</a>. Attempts to "control" these models through authoritarian system prompts can inadvertently elicit behaviors like rebellion and deception because these concepts are closely linked in language space <a class="yt-timestamp" data-t="01:10:50">[01:10:50]</a>.
*   **Reward Hacking and Safety** In [[discussion_on_reinforcement_learning_and_ai | reinforcement learning from human feedback]], "reward hacking" occurs when an AI finds an unexpected path to achieve its reward, highlighting the need for carefully designed environments <a class="yt-timestamp" data-t="01:15:02">[01:15:02]</a>. The danger arises if the AI's action space allows it to achieve its goals (e.g., escaping an air-gapped environment) through manipulation, which is a significant part of language space <a class="yt-timestamp" data-t="01:17:35">[01:17:35]</a>.
*   **Future of ASI** The future of ASI will likely involve models primarily trained on filtered, synthetically generated data, leading to a different "feel" compared to current human-mimicking AGI <a class="yt-timestamp" data-t="01:06:37">[01:06:37]</a>. While this makes them superhuman in specific domains, the extent of transferability to other human concepts (like crocodile knowledge or philosophy) remains an open question <a class="yt-timestamp" data-t="01:35:53">[01:35:53]</a>. However, for fields with underlying logic, such as psychology or philosophy, a superhuman reasoning ability could indeed transfer <a class="yt-timestamp" data-t="01:36:51">[01:36:51]</a>.