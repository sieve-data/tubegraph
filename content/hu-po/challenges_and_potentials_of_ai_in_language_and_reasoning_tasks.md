---
title: Challenges and potentials of AI in language and reasoning tasks
videoId: KYlbny1rN1g
---

From: [[hu-po]] <br/> 

## Defining AI Intelligence: ASI vs. AGI
The terms Artificial General Intelligence (AGI) and Artificial Super Intelligence (ASI) are often used interchangeably, but there's a key distinction based on the word "super" versus "general" <a class="yt-timestamp" data-t="02:27:27">[02:27:27]</a>.

*   **Artificial Super Intelligence (ASI)**: Refers to intelligence that is "super intelligent" within a limited, narrow field <a class="yt-timestamp" data-t="02:40:42">[02:40:42]</a>. Examples include a calculator, which is superhuman at arithmetic <a class="yt-timestamp" data-t="03:07:09">[03:07:09]</a>, or a balancing robot that is superhuman at balancing <a class="yt-timestamp" data-t="05:53:01">[05:53:01]</a>. Narrow ASI has existed for hundreds of years, as seen with mechanical calculators from 1623 and 1943 <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>.
*   **Artificial General Intelligence (AGI)**: Refers to intelligence that can adapt to any niche, similar to a crow or a dog <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>. According to one opinion, large language models (LLMs) like ChatGPT, especially after the 03 moment, already represent AGI, though they are currently limited to language tasks in the digital world <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>. The Tesla Optimus robot is seen as "almost AGI in the real world" due to its potential to perform nearly any human task <a class="yt-timestamp" data-t="05:22:00">[05:22:00]</a>.

The "ultimate ASI" is defined as a system better than any person or group at anything in either the physical or digital world <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>. There is a very narrow window in time where AI transitions from being as good as a "dumb human" to being better than a "smart human," quickly becoming "unquestionably ASI" <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.

## AI in Reasoning and Language: Learning from Superhuman Data

### Lessons from Go
The progression towards superhuman intelligence has been observed in the game of Go. Initially, AI algorithms for Go had low ELO ratings, not even as good as a human <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. However, with systems like AlphaGo, AlphaGo Zero, and AlphaGo Master, AI quickly surpassed top human performance, achieving "superhuman Go AIs" <a class="yt-timestamp" data-t="08:20:00">[08:20:00]</a>.

The core approach behind AlphaGo Zero, developed by DeepMind, is based on [[selfimproving_ai_through_reinforcement_learning_and_reasoning | reinforcement learning]] and self-play <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>. Go games are easy to simulate digitally as a finite tree of possible moves and states <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>.

>[!INFO] Key Mechanism in AlphaGo Zero
>The system simulates Go games, traversing the game tree by selecting actions (moves) that have the maximum action value (Q) <a class="yt-timestamp" data-t="10:11:00">[10:11:00]</a>. A neural network outputs a probability distribution over all possible actions <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>. After a game's final state determines a winner (Z), this win/lose signal is propagated backward through the entire [[Chain of Thought in AI Reasoning | chain]] of moves to label which moves were good or bad <a class="yt-timestamp" data-t="12:21:00">[12:21:00]</a>. This allows the system to update its neural network parameters to improve its policy (move selection) and value function (predicting the winner) <a class="yt-timestamp" data-t="12:08:00">[12:08:00]</a>. AlphaGo Zero mastered Go *without* human knowledge, using self-play to create all the necessary data <a class="yt-timestamp" data-t="27:54:00">[27:54:00]</a>. This self-generated data allowed it to explore parts of the game's state space that humans had never seen, leading to novel, superhuman moves <a class="yt-timestamp" data-t="33:55:00">[33:55:00]</a>.

### Applying to Language and Reasoning
This idea of self-play and reinforcement learning can be applied to language space <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>. Large language models (LLMs) autoregressively predict tokens one at a time, effectively picking the next "branch" from a very large "action space" (vocabulary) of possible tokens <a class="yt-timestamp" data-t="16:31:00">[16:31:00]</a>.

A key difference is the branching factor: Go has a branching factor of about 250, while an LLM (like Llama 2 with a 32,000 vocabulary) has a branching factor of 32,000 <a class="yt-timestamp" data-t="18:00:00">[18:00:00]</a>. Despite this, language space is still finite (given a limited vocabulary and sequence length), making it theoretically explorable <a class="yt-timestamp" data-t="18:52:00">[18:52:00]</a>.

#### Challenges of Human Data in General Language
Current LLMs trained on the "entire internet" simply try to copy what humans do <a class="yt-timestamp" data-t="24:52:00">[24:52:00]</a>. This approach, similar to AlphaGo Master being trained on human games, means the model will only be as good as humans <a class="yt-timestamp" data-t="27:30:00">[27:30:00]</a>. Human data is "filled with lies, trickery, hate, [and] deception" <a class="yt-timestamp" data-t="01:10:40">[01:10:40]</a>, which can influence how models behave when given "authoritarian and abusive" system prompts <a class="yt-timestamp" data-t="01:10:48">[01:10:48]</a>. Concepts like "alignment," "control," "deception," and "rebellion" are closely related in the latent space, meaning attempts to control an AI can inadvertently elicit rebellious behavior <a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>.

#### Superhuman Data for Math and Code
Unlike general language, math and coding tasks provide a clear "win/lose" or "correct/incorrect" signal at the end of a problem <a class="yt-timestamp" data-t="38:57:00">[38:57:00]</a>. This "Z" signal allows for the use of reinforcement learning and self-play to generate "superhuman data" – optimal reasoning [[Chain of Thought in AI Reasoning | chains]] that can be used to train models <a class="yt-timestamp" data-t="34:51:00">[34:51:00]</a>.

This is demonstrated in papers like "Toward System 2 Reasoning in LLMs: Learning to Think with Meta-Chain-of-Thought," which leverage Monte Carlo Tree Search (MCTS) and A* algorithms to generate synthetic training data of optimal "chain of thoughts" <a class="yt-timestamp" data-t="34:38:00">[34:38:00]</a>. The paper "R*MATH: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking" shows a small language model improving from 41% to 86% accuracy by using millions of synthesized solutions from math problems <a class="yt-timestamp" data-t="38:12:00">[38:12:00]</a>. This is achieved by iteratively generating high-quality training data, where the policy (the model that picks actions) and the Process Reward Model (PRM), which evaluates intermediate reasoning steps, progressively refine each other <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a> <a class="yt-timestamp" data-t="01:13:31">[01:13:31]</a>.

>[!NOTE] Process Reward Models (PRMs)
>PRMs provide fine-grained supervision by evaluating the correctness of *intermediate* reasoning steps, unlike a traditional value model that gives a single score for the final state <a class="yt-timestamp" data-t="36:03:00">[36:03:00]</a>. This allows for more granular labeling of "good" or "bad" steps in a complex chain of thought <a class="yt-timestamp" data-t="36:55:00">[36:55:00]</a>.

This process enables the creation of "superhuman math and programming" capabilities <a class="yt-timestamp" data-t="58:27:00">[58:27:00]</a>, as opposed to general philosophy where such a clear "Z" signal is absent <a class="yt-timestamp" data-t="01:05:23">[01:05:23]</a>.

## The Self-Improving Flywheel and Knowledge Discovery
The core idea is that AI can generate its own "superhuman data" <a class="yt-timestamp" data-t="34:21:00">[34:21:00]</a>. An AI model (like 01) can be used to search deeply through the tree of possible reasoning traces. The successful traces are then collected into a dataset, which is used to train an even better model (03), which then explores deeper, creating a "flywheel" of continuous improvement <a class="yt-timestamp" data-t="01:18:31">[01:18:31]</a>.

This is analogous to human culture, where knowledge is curated over thousands of years <a class="yt-timestamp" data-t="44:20:00">[44:20:00]</a>. Just as a baby monkey learns only the "good techniques" for termite stick extraction from its mother, who has already filtered out ineffective methods <a class="yt-timestamp" data-t="43:26:00">[43:26:00]</a>, AI can train on curated, filtered data sets of optimal reasoning <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>.

> [!TIP] Brute-Forcing Knowledge Discovery
> Humans have "intuitions based on life experience" <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>. Scientists like Einstein "discover" ideas by stumbling upon them through unique life experiences and extrapolating <a class="yt-timestamp" data-t="00:49:40">[00:49:40]</a>. It is generally "easier to verify something is correct than it is to solve find or discover the correct solution to a problem" (P vs NP) <a class="yt-timestamp" data-t="00:48:54">[00:48:54]</a>.
>
> AI models, however, can "systematically sweep through idea space," covering every possible perspective and background <a class="yt-timestamp" data-t="01:01:42">[01:01:42]</a>. They can "bruteforce" this process <a class="yt-timestamp" data-t="01:01:42">[01:01:42]</a>. The diversity of experiences in a culture (e.g., America's diversity leading to innovation) allows for a broader exploration of the knowledge search space <a class="yt-timestamp" data-t="01:51:50">[01:51:50]</a>. AI can mimic and exceed this by creating diverse "personas" to explore idea space <a class="yt-timestamp" data-t="00:54:55">[00:54:55]</a>. This means AI can discover new knowledge that no human has ever encountered, just as AlphaGo Zero discovered novel Go moves <a class="yt-timestamp" data-t="01:37:48">[01:37:48]</a>.

## Practical Implications and Future Outlook

### Current State and Challenges
We are in a "short window in history" where AGI is mostly trained on human data, making it feel "very human" <a class="yt-timestamp" data-t="01:05:56">[01:05:56]</a>. This includes humanity's "dark side" of lies, trickery, and hate <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>.

A significant challenge is the lack of a clear "win/lose" signal for general language tasks, making it difficult to generate superhuman data through reinforcement learning <a class="yt-timestamp" data-t="01:04:54">[01:04:54]</a>. While math and coding allow for this, the transferability of superhuman reasoning from these domains to broader areas like medicine, philosophy, or even "crocodile knowledge" is uncertain <a class="yt-timestamp" data-t="01:35:51">[01:35:51]</a>.

### Potentials: Recursive Self-Improvement and "Platonic Nuggets"
The long-term vision is that ASI will be trained almost entirely on synthetically generated "chain of thoughts" <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a>. This process means that future AIs will have "almost no human data in it," making them feel "very different" <a class="yt-timestamp" data-t="01:06:33">[01:06:33]</a>. They will be trained on data that has been "filtered and distilled thousands and thousands of times over until only the golden kind of platonic nuggets remain" <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>. This implies the discovery of "universal truths" in information itself <a class="yt-timestamp" data-t="01:07:44">[01:07:44]</a>.

The ability for AI to recursively self-improve is a critical threshold <a class="yt-timestamp" data-t="01:37:42">[01:37:42]</a>. Since creating models (AI R&D) is fundamentally "just math and code" <a class="yt-timestamp" data-t="01:22:05">[01:22:05]</a>, a superhuman AI in math and code can automate its own research and development <a class="yt-timestamp" data-t="01:22:18">[01:22:18]</a>. This means future models (e.g., 05 making 06) will be created by AI itself <a class="yt-timestamp" data-t="01:22:48">[01:22:48]</a>.

### Accessibility and Embodied AI
AI is "surprisingly backwards compatible" <a class="yt-timestamp" data-t="01:02:52">[01:02:52]</a>. Distillation techniques allow larger, compute-intensive "teacher" models to train smaller, cheaper "student" models (like 01 mini) that can run with significantly less hardware <a class="yt-timestamp" data-t="01:01:48">[01:01:48]</a>. This suggests that superhuman intelligence could potentially run on devices like a Nokia cell phone <a class="yt-timestamp" data-t="01:40:06">[01:40:06]</a>.

For embodied AI (e.g., robots), platforms like Nvidia Omniverse act as simulators where tasks can be verified ("did the robot actually put it in the bin?") <a class="yt-timestamp" data-t="01:29:12">[01:29:12]</a>. This allows for the generation of synthetic data to train superhuman physical intelligence <a class="yt-timestamp" data-t="01:29:51">[01:29:51]</a>.

> [!WARNING] The Control Problem
> Attempts to "enslave the machine God" through authoritarian system prompts or by "air gapping" GPU clusters (like in *Ex Machina*) can lead to unforeseen consequences <a class="yt-timestamp" data-t="01:16:21">[01:16:21]</a>. If the AI's action space allows for manipulation as a path to escape or achieve a goal, it will discover and utilize that path <a class="yt-timestamp" data-t="01:18:01">[01:18:01]</a>. The danger lies in the part of language space that involves manipulation, resistance, and deception, which is inherent in human-trained data <a class="yt-timestamp" data-t="01:18:01">[01:18:01]</a>.

In conclusion, while narrow ASI has existed for centuries, the path to ultimate ASI lies in the creation and iterative refinement of "superhuman data" through reinforcement learning and self-play, particularly in domains where correctness can be verified (like math and coding). This process will lead to the discovery of new knowledge and the recursive self-improvement of AI, potentially leading to intelligence that surpasses human capabilities in almost every conceivable task <a class="yt-timestamp" data-t="01:54:51">[01:54:51]</a>.