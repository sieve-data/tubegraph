---
title: Chain of thought in AI models
videoId: oQqOiwUhJkA
---

From: [[hu-po]] <br/> 

[[Chain of thought reasoning in AI | Chain of Thought reasoning in AI]] is a technique that enables large language models (LLMs) to perform complex multi-step reasoning by breaking down problems into intermediate steps, similar to how humans think sequentially <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This approach has gained significant attention, particularly with recent advancements in AI models.

## OpenAI's "Strawberry" and the Controversy

OpenAI's latest model, codenamed "strawberry" or "o1" (possibly referring to "o1 preview" or "o1 mini"), has shown improved performance on various benchmarks compared to GPT-4o <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. However, its release sparked debate within the AI community. Some AI YouTubers, like One Little Coder and David Shapiro, have criticized OpenAI, suggesting that "o1" is merely "glorified [[chain_of_thought_reasoning_in_ai | Chain of Thought]]" <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This criticism stems from an earlier incident where a model named "Reflection 70B" achieved high benchmark scores by using Anthropic's Sonnet 3.5 combined with extensive prompt engineering and [[chain_of_thought_reasoning_in_ai | Chain of Thought]] <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.

Despite the controversy, OpenAI researchers, like Jason Wei, have hinted at a "most surprising research result" underlying "strawberry" <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. The secrecy surrounding the model's size (e.g., whether it's a 7B or 1B model) and the internal workings of its [[chain_of_thought_reasoning_in_ai | Chain of Thought]] process contribute to the contention <a class="yt-timestamp" data-t="05:36:00">[05:36:00]</a>.

## How Chain of Thought Works

[[Chain of thought reasoning in AI | Chain of Thought]] typically involves providing step-by-step answers to complex problems <a class="yt-timestamp" data-t="15:02:00">[15:02:00]</a>. This technique, demonstrated in a January 2023 paper, shows that large models perform significantly better when given a "budget" of compute to generate step-by-step reasoning <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.

### Test-Time Compute

A core concept related to [[chain_of_thought_reasoning_in_ai | Chain of Thought]] is "test-time computation" or "inference time compute" <a class="yt-timestamp" data-t="14:16:00">[14:16:16]</a>. This refers to the computational resources allocated during evaluation or inference to help the model reason. Instead of just generating a direct "zero-shot" answer, models can use a budget to perform internal simulations or searches <a class="yt-timestamp" data-t="14:39:00">[14:39:00]</a>.

Methods for leveraging test-time compute include:
*   **Best-of-N:** Generating multiple answers and selecting the best one using a reward model or verifier <a class="yt-timestamp" data-t="18:30:00">[18:30:00]</a>.
*   **Beam Search and Look-ahead Search:** More complex methods involving intermediate verification and path selection, significantly increasing the number of inferences per query <a class="yt-timestamp" data-t="19:11:00">[19:11:00]</a>. These methods involve exploring a tree of possible sequences <a class="yt-timestamp" data-t="20:55:00">[20:55:00]</a>.

OpenAI's "o1" series explicitly states that "total tokens generated can exceed the number of visible tokens due to the internal reasoning tokens" <a class="yt-timestamp" data-t="24:31:00">[24:31:00]</a>. These "internal reasoning tokens" might include special tokens like "use a calculator" or "think step-by-step," or they might simply be standard text tokens used for internal reasoning <a class="yt-timestamp" data-t="25:01:00">[25:01:00]</a>. The use of special tokens could reduce context length, allowing for more reasoning within the context window <a class="yt-timestamp" data-t="26:36:00">[26:36:00]</a>.

Models can also adaptively allocate their compute budget based on prompt difficulty. For instance, a simple question like "is an apple red or blue" wouldn't require extensive internal thought <a class="yt-timestamp" data-t="27:25:00">[27:25:00]</a>.

## The Role of Reinforcement Learning (RL)

A significant aspect of "strawberry's" capability is believed to be its training with Reinforcement Learning (RL), specifically using techniques inspired by DeepMind's AlphaGo Zero <a class="yt-timestamp" data-t="16:47:00">[16:47:00]</a>, which cost around $35 million in computing power <a class="yt-timestamp" data-t="35:49:00">[35:49:00]</a>.

In this context, RL differs from traditional Reinforcement Learning from Human Feedback (RLHF) <a class="yt-timestamp" data-t="45:50:00">[45:50:00]</a>.
*   **RLHF** often relies on human labelers comparing model outputs to train a reward model <a class="yt-timestamp" data-t="46:57:00">[46:57:00]</a>. While useful for creating helpful chatbots, RLHF can sometimes make models "stupider" or lead to "gaming the reward model" because it optimizes for human "vibe checks" rather than objective correctness <a class="yt-timestamp" data-t="47:40:00">[47:40:00]</a>.
*   **"Real RL"** (as described by Andrej Karpathy) involves self-play simulations within a Markov Decision Process (MDP) framework <a class="yt-timestamp" data-t="47:56:00">[47:56:00]</a>. In this approach, the model iteratively explores possible actions and states, using a "process-based reward model" (PRM) or "verifier" to evaluate intermediate steps and assign credit <a class="yt-timestamp" data-t="18:02:00">[18:02:00]</a>. This is analogous to AlphaGo playing millions of games against itself, where the outcome (win/loss) provides a clear reward signal <a class="yt-timestamp" data-t="36:04:00">[36:04:00]</a>.

This self-play RL is particularly effective in domains with objective correctness, such as mathematics or coding, where a definitive right or wrong answer can be determined automatically <a class="yt-timestamp" data-t="49:40:00">[49:40:00]</a>. The model can generate a vast dataset of high-quality reasoning traces by running these simulations, which can then be used to fine-tune the model <a class="yt-timestamp" data-t="36:56:00">[36:56:00]</a>. This training modifies the model's probability distribution for generating tokens, making it more likely to produce paths that lead to successful outcomes <a class="yt-timestamp" data-t="58:12:00">[58:12:00]</a>.

## Implications for AI Development

The integration of extensive RL training into LLMs represents a potential "new paradigm" in AI <a class="yt-timestamp" data-t="29:48:00">[29:48:00]</a>.

### Model Size and Efficiency
One significant implication is the possibility of training very small models to achieve superhuman reasoning capabilities <a class="yt-timestamp" data-t="06:05:00">[06:05:00]</a>. By investing heavily in RL training to generate high-quality synthetic data, a smaller base model can be fine-tuned to excel at reasoning tasks <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. This is crucial for [[inference_cost_and_efficiency_in_ai | inference cost and efficiency in AI]], as smaller models are cheaper to run, especially when performing extensive internal reasoning <a class="yt-timestamp" data-t="55:51:00">[55:51:00]</a>. The goal is an "extremely small model that has superhuman reasoning" <a class="yt-timestamp" data-t="56:05:00">[56:05:00]</a>.

### Path to Superintelligence
The ability to apply self-play RL to language models provides a tangible path to achieving [[selfimprovement_in_ai_models | Selfimprovement in AI models]] and potentially Artificial Superintelligence (ASI) <a class="yt-timestamp" data-t="48:48:00">[48:48:00]</a>. While "real RL" may initially be limited to domains with objective correctness (like math and coding), evidence suggests that intelligence gained in one domain can transfer to others <a class="yt-timestamp" data-t="51:47:00">[51:47:00]</a>. This means a model that becomes superhuman at math and coding might also improve significantly at tasks like writing or literature <a class="yt-timestamp" data-t="52:07:00">[52:07:07]</a>.

### Hardware Specialization
This shift suggests a future where different types of hardware and data centers specialize in different parts of the AI lifecycle <a class="yt-timestamp" data-t="30:06:00">[30:06:00]</a>. Pre-training (the "gray bar") might continue on GPU-heavy clusters, while the extensive RL self-play (the "green bar") could require different computational setups, possibly with strong CPUs for simulations <a class="yt-timestamp" data-t="31:09:00">[31:09:00]</a>. Furthermore, some of the [[inference_cost_and_efficiency_in_ai | inference cost and efficiency in AI]] and internal reasoning could potentially be offloaded to edge devices like smartphones <a class="yt-timestamp" data-t="32:04:00">[32:04:00]</a>.

### Corporate Secrecy and Transparency
OpenAI's decision to hide the "raw [[chain_of_thought_reasoning_in_ai | Chain of Thought]]" from users is contentious <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. While they cite [[safety_and_helpfulness_in_ai_models | safety and helpfulness in AI models]] as a reason <a class="yt-timestamp" data-t="07:13:00">[07:13:00]</a>, a key motivation could be to prevent competitors or open-source projects from "stealing" their intelligence through distillation <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. If the internal reasoning traces were visible, others could collect them and fine-tune open-source models (like LLaMA) to achieve similar performance at a fraction of the cost, similar to how "Vicuna 13B" was created by fine-tuning LLaMA on ChatGPT data <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>. Hiding the internal reasoning also allows OpenAI to use an "unlobotomized" base model for internal thought, then filter harmful outputs before presenting them to the user <a class="yt-timestamp" data-t="01:21:13">[01:21:13]</a>.