---
title: Introduction to Strawberry AI model
videoId: oQqOiwUhJkA
---

From: [[hu-po]] <br/> 

**Strawberry** is the latest AI model released by OpenAI <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. While not strictly a single model, it represents a collection of different elements that are "breaking a bunch of these benchmarks" <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. It has sparked debate within the AI community, with some calling it a "glorified Chain of Thought" <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>, and others considering it a new "scaling paradigm" <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

## Key Characteristics and Performance

Strawberry, specifically the "01" or "01 preview" series, shows improved performance compared to the existing GPT-4o model in benchmarks <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. Despite the improved results, its exact composition and size remain undisclosed by OpenAI <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>. Some speculate that a significant part of its impressiveness lies in its potential small size combined with advanced reasoning capabilities <a class="yt-timestamp" data-t="05:55:00">[05:55:00]</a>.

## Underlying Mechanisms

The enhanced capabilities of Strawberry are believed to stem from a combination of advanced techniques, primarily involving [[AI and Reinforcement Learning | Reinforcement Learning]] (RL) and test-time computation.

### Test-Time Computation and Chain of Thought

Strawberry utilizes "test-time computation," which involves spending an allocated amount of compute for every question at inference or evaluation time <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. This concept, while not new <a class="yt-timestamp" data-t="15:26:00">[15:26:00]</a>, allows the model to "think step by step" by creating a "Chain of Thought" <a class="yt-timestamp" data-t="16:18:00">[16:18:00]</a>. This process involves the model generating "internal reasoning tokens" that are hidden from the user, which then influence the final output <a class="yt-timestamp" data-t="24:31:00">[24:31:00]</a>.

Different search methods employ this:
*   **Best of N**: The model produces multiple answers, and a reward model (or verifier) selects the best one <a class="yt-timestamp" data-t="18:30:00">[18:30:00]</a>.
*   **Beam Search and Look Ahead Search**: These methods involve the verifier evaluating intermediate parts of the process to pick an optimal path <a class="yt-timestamp" data-t="19:13:00">[19:13:00]</a>.

This increased test-time compute can lead to a smaller model outperforming a much larger one by enabling it to perform more internal inferences to find a better answer <a class="yt-timestamp" data-t="23:59:00">[23:59:00]</a>.

### Integration of [[AI and Reinforcement Learning | Reinforcement Learning]]

A key aspect of Strawberry is its use of [[AI and Reinforcement Learning | RL]] training to improve its reasoning capabilities <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>, differentiating it from earlier methods like RHF (Reinforcement Learning from Human Feedback).

#### Beyond RHF: Self-Play and Process-Based Reward Models
Traditionally, LLMs undergo pre-training and then post-training, often using RHF <a class="yt-timestamp" data-t="34:40:00">[34:40:00]</a>. RHF involves human labelers comparing outputs and training a reward model based on human preference <a class="yt-timestamp" data-t="47:02:00">[47:02:00]</a>. However, this approach can make models "stupider" at reasoning <a class="yt-timestamp" data-t="47:52:00">[47:52:00]</a>.

Strawberry, on the other hand, is believed to integrate "real RL" or "classic DeepMind [[AI and Reinforcement Learning | RL]]" into its training <a class="yt-timestamp" data-t="47:56:00">[47:56:00]</a>. This involves:
*   **Monte Carlo Tree Search (MCTS)**: Similar to how AlphaGo Zero learned to play Go <a class="yt-timestamp" data-t="35:56:00">[35:56:00]</a>, Strawberry likely uses MCTS to explore various "Chain of Thought" paths in the language space <a class="yt-timestamp" data-t="21:32:00">[21:32:00]</a>.
*   **Process-Based Reward Model (PRM)**: This model evaluates not just the final answer but the entire "Chain of Thought" or process to reach it <a class="yt-timestamp" data-t="18:02:00">[18:02:00]</a>.
*   **Self-Play Simulations**: The model can generate high-quality training data through self-play, pushing gradients into the model itself <a class="yt-timestamp" data-t="36:16:00">[36:16:00]</a>. This is akin to AlphaGo spending millions of dollars playing simulated games against itself to learn and improve <a class="yt-timestamp" data-t="36:00:00">[36:00:00]</a>.

This "real RL" phase creates a massive synthetic data set of MCTS trees and paths, on which the model is fine-tuned <a class="yt-timestamp" data-t="36:59:00">[36:59:00]</a>. This is seen as a new, significant "green bar" of compute investment, potentially as large as the initial pre-training ("gray bar") <a class="yt-timestamp" data-t="38:31:00">[38:31:00]</a>.

## Controversies and Secrecy

OpenAI's approach with Strawberry has drawn criticism due to its lack of transparency:
*   **Hidden Chain of Thought**: OpenAI explicitly states they "have decided not to show the raw chain of thoughts to user" <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. This is viewed by some as "creepy and Orwellian" <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>.
*   **Unknown Model Size**: The actual size of the 01 models remains unknown <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.
*   **Motivation for Secrecy**:
    *   **Anti-Competitive Practices**: Hiding the Chain of Thought may prevent others from "fine-tuning" on it <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. If the reasoning traces were public, open-source models could potentially achieve similar performance by distilling this costly data <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>. This mirrors concerns in [[Open source AI models and accessibility | data generation for AI models]], such as Stable Diffusion pinging Midjourney's API for training data <a class="yt-timestamp" data-t="01:16:37">[01:16:37]</a>.
    *   **Safety/Alignment**: Hiding internal reasoning allows OpenAI to filter out potentially "bad" or unaligned outputs before they reach the user, potentially using a less "lobotomized" [[Foundation models in AI | foundation model]] internally <a class="yt-timestamp" data-t="01:21:13">[01:21:13]</a>.

## Implications for AI Development

### Path to Superhuman Intelligence
The combination of large-scale pre-training with sophisticated [[AI and Reinforcement Learning | RL]] (like MCTS and self-play) is seen as a direct path to [[Foundation models in AI | superhuman reasoning]] <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>. This is particularly effective in domains like math and coding, where a clear "correct answer" or reward signal is available to guide the [[AI and Reinforcement Learning | RL]] process <a class="yt-timestamp" data-t="00:49:49">[00:49:49]</a>. While subjective tasks like writing lack this clear signal, there's evidence that reasoning improvements in one domain can transfer to others <a class="yt-timestamp" data-t="00:51:47">[00:51:47]</a>.

This advancement suggests a move from Artificial General Intelligence (AGI), which is as good as a human, towards Artificial Super Intelligence (ASI), which surpasses human capabilities <a class="yt-timestamp" data-t="01:09:03">[01:09:03]</a>.

### New Hardware and Business Models
This shift towards extensive [[AI and Reinforcement Learning | RL]] training at scale will likely lead to new types of data centers and specialized hardware <a class="yt-timestamp" data-t="01:13:52">[01:13:52]</a>. While pre-training might rely on GPU-heavy clusters, the experience collection and simulation parts of RL might benefit from strong CPUs <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>. This creates a new market for companies specializing in these specific compute workloads <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>.

There's also a potential future where the "Foundation Model" is hosted on large data centers, but the inference-time computation, including the iterative search and Chain of Thought, could be performed on-device (e.g., on an iPhone), due to privacy concerns and the increasingly efficient distillation of large models into smaller, performant ones <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>.

### [[Challenges and improvements in animated AI models | The Bitter Lesson]]
The speaker notes that while current innovations add complexity (like [[AI and Reinforcement Learning | RL]] on top of LLMs), the "bitter lesson" of AI suggests that over time, simpler, larger-scale approaches (just bigger models trained on more data) tend to win out <a class="yt-timestamp" data-t="01:17:22">[01:17:22]</a>. However, for now, these "over-engineered" methods are driving progress.

## Conclusion
Strawberry marks a significant step in AI development by combining massive pre-training with production-grade [[AI and Reinforcement Learning | reinforcement learning]] for reasoning <a class="yt-timestamp" data-t="01:48:51">[01:48:51]</a>. While OpenAI's secrecy surrounding its implementation is a contentious point, this model signals a shift towards models capable of [[Foundation models in AI | superhuman reasoning]] through continuous self-play and advanced computational strategies.