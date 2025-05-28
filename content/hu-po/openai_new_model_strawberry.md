---
title: OpenAI new model strawberry
videoId: oQqOiwUhJkA
---

From: [[hu-po]] <br/> 

OpenAI has recently introduced a new model, colloquially referred to as "Strawberry," which is causing a significant stir in the AI community. While its official names, such as "O1 preview" or "O1 mini," are considered "kind of terrible" by some, its performance is undeniable as it is "breaking a bunch of these benchmarks" and outperforming models like GPT-4o <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

## The Contention: Glorified Chain of Thought?

Despite its impressive benchmark scores, "Strawberry" has become a "contentious issue" <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Prominent AI YouTubers and researchers like "one little coder" and David Shapiro have publicly questioned its novelty, asking, "Why is no one saying open ai1 his glorified Chain of Thought" <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This sentiment echoes a recent incident where an "AI kind of grifter kind of Twitter personality" claimed to have the "top open source model" (Reflection 70B), only for it to be revealed that they were using Sonnet 3.5 with extensive prompt engineering and Chain of Thought <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. Critics highlight a "two different standards that people are holding" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> when Chain of Thought is used.

## The "Secret Sauce": Test Time Computation & RL

While acknowledging some truth to the "glorified Chain of Thought" critique, the presenter suggests there's "more to it" <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. The core of this perceived innovation lies in "test time computation" <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

### Understanding Test Time Computation

Test time computation refers to "compute that you're using during your test" <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a> or "inference time or evaluation time" <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>. Traditionally, model evaluation focuses on the immediate output (zero-shot). However, this new approach involves an "allocated amount of compute that you can spend for every single question at test time" <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>, which significantly improves performance <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. This is not a new concept; a January 2023 paper demonstrated that "Large Language Models are Zero-Shot Reasoners," utilizing Chain of Thought prompting for multi-step reasoning <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

OpenAI's developer documentation confirms this, stating that with the O1 series, "the total tokens generated can exceed the number of visible tokens due to the internal reasoning tokens" <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>. This implies the model is performing internal computations and reasoning steps that are not directly shown to the user. These internal reasoning tokens could be special "action tokens" (e.g., "use a calculator," "think step-by-step") <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>, which would allow for more efficient internal processing, especially for smaller models.

### The Role of Reinforcement Learning (RL)

The true differentiator for "Strawberry" appears to be the integration of [[Selfimprovement in AI models | Reinforcement Learning (RL)]] into its training process <a class="yt-timestamp" data-t="01:05:22">[01:05:22]</a>. Unlike traditional RLHF (Reinforcement Learning from Human Feedback), which relies on human preferences, O1 seems to use "real RL" that trains the model to "think" <a class="yt-timestamp" data-t="01:05:22">[01:05:22]</a>.

This "real RL" uses a "process-based reward model" (PRM), which evaluates the entire "Chain of Thought" or process to arrive at an answer, not just the final output <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>. This helps solve the "credit assignment problem" in reinforcement learning, where it's difficult to know which specific steps in a long sequence contributed to a positive outcome <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

The mechanism at play is likely similar to Monte Carlo Tree Search (MCTS), famously used in AlphaGo Zero <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>. The model runs "millions and millions of games of Chess" <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a> (or, in this case, internal reasoning simulations), exploring different paths and evaluating them based on a reward signal. This extensive self-play generates high-quality [[synthetic training data for AI | synthetic training data]] <a class="yt-timestamp" data-t="00:38:12">[00:38:12]</a>, which is then used to fine-tune the model <a class="yt-timestamp" data-t="00:38:16">[00:38:16]</a>.

*   **Best of N**: The simplest form, where the LLM produces N answers, and a reward model picks the best <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>.
*   **Beam Search / Look-Ahead Search**: More complex methods involve running the verifier on intermediate parts of the process, picking a path, and generating further steps <a class="yt-timestamp" data-t="00:19:13">[00:19:13]</a>. This requires significantly more compute at inference time <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.

Studies from [[DINOv2 and Meta AIs Vision Models | Google DeepMind]] have shown that "test time compute can be used to outperform a 14x larger model" <a class="yt-timestamp" data-t="00:23:59">[00:23:59]</a>. This suggests that a smaller model, coupled with sophisticated reasoning techniques and substantial test-time computation, can surpass a much larger model. This is potentially why the O1 model's actual size is kept secret, as a "really tiny model" achieving such results would be "really impressive" <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.

## OpenAI's Secrecy and Financial Incentives

OpenAI's approach with "Strawberry" is marked by a high degree of secrecy.

### Hiding the Chain of Thought

OpenAI has "decided not to show the raw chain of thoughts to user," describing it as "very creepy and Orwellian" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. While they claim to monitor the Chain of Thought for safety reasons (e.g., "signs of manipulating the user") <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>, a significant reason for this secrecy is likely anti-competitive <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. Releasing the raw Chain of Thought would enable competitors to "fine-tune on that" <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>. For example, the Vuna 13B model was created by fine-tuning LLaMA on ChatGPT data, achieving performance "pretty much as good as GPT" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. By withholding this data, OpenAI prevents others from distilling their expensive RL-trained reasoning capabilities into open-source models <a class="yt-timestamp" data-t="01:15:15">[01:15:15]</a>. It also allows them to use "not lobotomized" <a class="yt-timestamp" data-t="01:21:49">[01:21:49]</a> (i.e., not safety-aligned) models for internal reasoning, applying a filter only to the final user-facing output <a class="yt-timestamp" data-t="01:21:25">[01:21:25]</a>.

### AGI Claims and Financial Status

Sam Altman's denial of "Strawberry" being AGI (Artificial General Intelligence) <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a> is not necessarily an honest assessment of the model's capabilities, but rather a strategic financial decision. OpenAI's agreement with Microsoft dictates that the highly profitable revenue-sharing model ceases once OpenAI achieves AGI <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Therefore, for financial reasons, Altman "continues to say that this is not AGI" <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

The 30-response daily limit on "Strawberry" is also attributed to cost. OpenAI is likely "losing money on these inferences" <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>, subsidizing the product to encourage adoption and establish a monopoly, a "pretty standard monopolistic practice" <a class="yt-timestamp" data-t="01:03:32">[01:03:32]</a>.

## The "New Paradigm": RL Training and Superhuman Reasoning

The presenter argues that "Strawberry" marks a "new paradigm" in AI <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a> by effectively merging the "LLM world" (large-scale next-token prediction) with "reinforcement learning kind of DeepMind self-play" <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>.

Historically, the computational cost of pre-training (the "gray bar") has dwarfed that of fine-tuning or RLHF (the "green bar") <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>. However, with the integration of "real RL," this "green bar" of RL training is expected to "explode" <a class="yt-timestamp" data-t="00:35:29">[00:35:29]</a>. AlphaGo Zero, for example, cost around $35 million in computing power for its self-play simulations <a class="yt-timestamp" data-t="00:35:42">[00:35:42]</a>.

This "real RL" allows models to become "superhuman at reasoning" <a class="yt-timestamp" data-t="00:48:51">[00:48:51]</a>. Unlike RLHF, which is limited by human preference data and can lead to models "gaming the reward model" <a class="yt-timestamp" data-t="01:04:23">[01:04:23]</a>, true RL involves self-play where the model learns by exploring paths and receiving concrete rewards for success (e.g., solving a math problem, winning a game) <a class="yt-timestamp" data-t="00:48:08">[00:48:08]</a>. This is most effective in domains with objective correctness, like "code or math" <a class="yt-timestamp" data-t="00:50:19">[00:50:19]</a>.

Karpathy, a leading AI researcher, has noted that "no production grade actual RL on an llm has so far been convincingly achieved and demonstrated in an open domain at scale" <a class="yt-timestamp" data-t="01:24:44">[01:24:44]</a> before the emergence of O1. The "Strawberry" model is therefore significant because it represents this combination at a production scale <a class="yt-timestamp" data-t="01:33:17">[01:33:17]</a>.

## Future Implications and Challenges

The emergence of models like "Strawberry" will likely lead to [[enhancements in AI model serving processes | new hardware and data center specializations]]. Training for large pre-trained models (the "gray bar") differs from the compute workload for RL (the "green bar") <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. The latter requires massive simulation capabilities, often CPU-intensive, distinct from GPU-heavy gradient pushing <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>. This could create a "new category of hey we don't train Foundation models we don't do anything with Foundation models we're just very good at creating uh data centers that have different types of computers that specialize in these different things" <a class="yt-timestamp" data-t="00:30:12">[00:30:12]</a>.

There's also speculation about [[alternative uses for AI models | on-device inference]] for the reasoning component, with the raw Foundation model remaining in the cloud <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>. This could be appealing for privacy-focused companies like Apple <a class="yt-timestamp" data-t="00:32:59">[00:32:59]</a>.

The ability to integrate self-play RL means there is "no limit" to improving reasoning capabilities, as "you can now pour more money and get more intelligence" through continuous self-play simulations <a class="yt-timestamp" data-t="01:51:57">[01:51:57]</a>. This points towards a path not just to AGI, but to ASI (Artificial Super Intelligence) <a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a>. Despite the current "over engineered" solutions, the "bitter lesson" of AI research suggests that eventually, simpler, massively scaled approaches will prevail <a class="yt-timestamp" data-t="01:17:25">[01:17:25]</a>.

Ultimately, while the model is currently limited to text output, the next "paradigm shift" will involve models with broader "action spaces," capable of controlling a computer's mouse, opening tabs, or accessing terminals <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a>. This would truly unlock its potential and lead to a more profound experience of AGI.