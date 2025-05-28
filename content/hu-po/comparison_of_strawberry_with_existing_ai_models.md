---
title: Comparison of Strawberry with existing AI models
videoId: oQqOiwUhJkA
---

From: [[hu-po]] <br/> 

The introduction of OpenAI's latest model, dubbed "Strawberry" (officially `o1` preview/mini), has sparked debate regarding its novelty and performance compared to existing AI models like GPT-4o <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>. While some consider it a significant breakthrough, others view it as a [[comparison_with_other_selfsupervised_and_supervised_models | glorified Chain of Thought]] implementation <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.

## Initial Reception and Benchmarks
Strawberry (o1) is reported to perform better than GPT-4o on various benchmarks <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. This has led to excitement, with some researchers at OpenAI hinting at surprising research results that cannot be revealed <a class="yt-timestamp" data-t="05:14:00">[05:14:00]</a>. However, the exact size of the `o1` model is not publicly known, leading to speculation that its impressive performance might be due to its potentially small size combined with advanced techniques <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.

## The "Glorified Chain of Thought" Debate
Critics, including AI YouTubers like "one little coder" and David Shapiro, argue that `o1` is merely a glorified Chain of Thought <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This criticism stems from a recent incident involving "Reflection 70B," an "open source" model that achieved high benchmark scores by using Anthropic's Sonnet 3.5 with extensive prompt engineering and Chain of Thought <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>. The argument is that OpenAI is being held to a different standard when applying similar techniques <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.

Chain of Thought prompting, a technique for eliciting complex, multi-step reasoning through step-by-step answers, has been recognized since at least January 2023 <a class="yt-timestamp" data-t="15:42:00">[15:42:00]</a>. It has been shown that larger models perform significantly better when given a "budget" to create a Chain of Thought and think step-by-step, as opposed to zero-shot inference <a class="yt-timestamp" data-t="16:01:00">[16:01:00]</a>. This suggests that the concept itself is not new <a class="yt-timestamp" data-t="16:22:00">[16:22:00]</a>.

## Test-Time Computation and Internal Reasoning
OpenAI's `o1` series explicitly utilizes "internal reasoning tokens," where the total tokens generated can exceed the number visible to the user <a class="yt-timestamp" data-t="24:31:00">[24:31:00]</a>. This is a form of "test-time computation," which involves using additional compute during the evaluation or inference phase to improve outputs <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>.

There are theories that these "internal reasoning tokens" could be:
*   **Special Tokens**: Abstract action tokens (e.g., "use a calculator token," "think step-by-step token") that condense complex internal processes, reducing context length and allowing for more reasoning within the context window <a class="yt-timestamp" data-t="24:52:00">[24:52:00]</a>.
*   **Reused Text Tokens**: More likely, the model reuses its existing vocabulary to perform internal reasoning, which is then hidden from the user <a class="yt-timestamp" data-t="25:52:00">[25:52:00]</a>.

The amount of test-time compute allocated to a query can be adaptive, based on the difficulty of the prompt <a class="yt-timestamp" data-t="27:41:00">[27:41:00]</a>. Ideally, users should have control over this "reasoning tokens" budget <a class="yt-timestamp" data-t="28:28:00">[28:28:00]</a>, possibly even expressed in monetary terms (e.g., "spend $10 worth of compute on this query") <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>. This "inference time scaling" could create a new category of specialized hardware and startups <a class="yt-timestamp" data-t="29:52:00">[29:52:00]</a>.

## The Role of Reinforcement Learning (RL)
A significant difference between `o1` and previous models lies in its potential use of true Reinforcement Learning (RL) for training, beyond just Chain of Thought at inference time <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>. This is what some believe to be the "secret sauce" <a class="yt-timestamp" data-t="38:01:00">[38:01:00]</a>.

### Distinguishing from RLF (Reinforcement Learning from Human Feedback)
Traditional RLHF (Reinforcement Learning from Human Feedback) involves human labelers comparing model outputs and training a reward model to imitate human preferences ("vibe check") <a class="yt-timestamp" data-t="46:55:00">[46:55:00]</a>. This method can sometimes lead to models that "game the reward model" or even become "stupider" <a class="yt-timestamp" data-t="47:56:00">[47:56:00]</a>.

### AlphaGo Zero Analogy and Self-Play
The suspected approach for `o1` draws parallels to Google DeepMind's AlphaGo Zero, which cost approximately $35 million in computing power to train <a class="yt-timestamp" data-t="35:42:00">[35:42:00]</a>. AlphaGo Zero learned by playing millions of games against itself, using Monte Carlo Tree Search (MCTS) to explore possible moves and assign credit to successful paths <a class="yt-timestamp" data-t="36:00:00">[36:00:00]</a>. This process of [[selfimprovement_in_ai_models | self-play]] allows for the generation of high-quality synthetic training data <a class="yt-timestamp" data-t="38:10:00">[38:10:00]</a>.

The hypothesis is that OpenAI is taking a pre-trained LLM, creating a massive synthetic dataset of MCTS trees and paths, and then using this data to fine-tune the model (or push significant gradients into it) in a way similar to AlphaGo Zero's self-play <a class="yt-timestamp" data-t="36:56:00">[36:56:00]</a>. This would represent a new, substantial "green bar" of RL post-training compute, akin to the scale of pre-training <a class="yt-timestamp" data-t="38:31:00">[38:31:00]</a>.

### Path to Superhuman Intelligence
The ability to apply true RL (like in AlphaGo) to language models, particularly in domains with clear right/wrong answers such as math and coding, opens a path to "superhuman reasoning" <a class="yt-timestamp" data-t="48:37:00">[48:37:00]</a>. While currently limited to verifiable tasks, there's evidence of knowledge transfer, meaning superhuman performance in coding and math could lead to improved reasoning in other subjective areas like writing <a class="yt-timestamp" data-t="51:47:00">[51:47:00]</a>.

This marks the first "production-grade actual RL on an LLM that has been convincingly achieved and demonstrated," according to researchers like Andrej Karpathy <a class="yt-timestamp" data-t="01:23:41:00">[01:23:41:00]</a>.

## Secrecy and [[open_source_vs_proprietary_ai_models | Anti-Competitive Practices]]
OpenAI's decision to hide the "raw chain of thoughts" from users, while sharing it with agencies like the FBI, has been criticized as "creepy and Orwellian" <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. A primary reason for this secrecy is believed to be anti-competitive:
*   **Preventing Fine-tuning/Distillation**: If the full Chain of Thought were visible, competitors could easily fine-tune open-source models (like LLaMA) on this data, effectively "stealing" the results of OpenAI's expensive RL training <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>. This is reminiscent of how `vuna 13B` was fine-tuned on ChatGPT data for a low cost <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>.
*   **Monopolistic Practices**: By subsidizing the product (e.g., limits of 30 responses per day, losing money on inferences), OpenAI might aim to undercut competitors and gain market dominance before raising prices <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>.
*   **Safety/Alignment**: Hiding internal reasoning could also allow OpenAI to use a less-aligned (non-RLHF) base model for reasoning, then filter out undesirable outputs before presentation to the user, providing a "cleaner way of preventing bad stuff from being shown" <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

## AGI Claims and Financial Interests
Sam Altman's denial of `o1` being AGI is speculated to be tied to OpenAI's unique agreement with Microsoft. Their partnership dictates that once OpenAI achieves AGI, the financial revenue-sharing arrangement with Microsoft significantly changes, making OpenAI more of a non-profit entity <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>. Thus, Altman's statements might reflect financial interests rather than a genuine assessment of AGI <a class="yt-timestamp" data-t="09:32:00">[09:32:00]</a>.

## Future Outlook
The integration of massive pre-training with large-scale RL-based self-play is seen as a redefinition of the AI development landscape <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. This approach allows for potentially infinite [[selfimprovement_in_ai_models | self-play]] and pouring hundreds of millions of dollars into compute for obtaining more intelligence <a class="yt-timestamp" data-t="01:51:54:00">[01:51:54:00]</a>.

This paradigm shift could lead to:
*   **Specialized Hardware**: Data centers will likely specialize in either pre-training (requiring GPUs for gradients) or RL-based self-play (potentially requiring strong CPUs for simulations) <a class="yt-timestamp" data-t="01:13:52:00">[01:13:52:00]</a>.
*   **On-Device Inference**: The raw foundation model could remain on cloud servers, while the costly inference-time compute (like MCTS searches) might eventually shift to on-device processing (e.g., iPhones) to preserve user privacy <a class="yt-timestamp" data-t="01:31:51:00">[01:31:51:00]</a>.
*   **Path to ASI**: This combination of massive pre-training and self-play RL is seen as a path not just to Artificial General Intelligence (AGI) but to Artificial Super Intelligence (ASI) <a class="yt-timestamp" data-t="01:09:01:00">[01:09:01:00]</a>.
*   **Bitter Lesson in Hindsight**: While current complex engineered solutions (like `o1`) offer immediate performance gains, the "bitter lesson" of AI development suggests that simpler, massively scaled models trained on vast data sets might eventually outperform them in the long run <a class="yt-timestamp" data-t="01:17:22:00">[01:17:22:00]</a>. However, this is a trend observed in hindsight over decades, not a day-to-day decision-making principle <a class="yt-timestamp" data-t="01:25:36:00">[01:25:36:00]</a>.

The primary [[challenges_and_improvements_in_animated_ai_models | limitation]] of this RL-driven approach is the need for a verifiable "final reward" signal <a class="yt-timestamp" data-t="01:07:40:00">[01:07:40:00]</a>. This is readily available in games (win/loss) or coding/math problems (correct answer), allowing for automated data generation and backpropagation of rewards through the entire reasoning trace <a class="yt-timestamp" data-t="01:02:46:00">[01:02:46:00]</a>. However, for subjective fields like writing or philosophy, a clear "correct answer" and automated reward signal are absent, limiting the direct application of this particular RL approach <a class="yt-timestamp" data-t="01:50:51:00">[01:50:51:00]</a>.