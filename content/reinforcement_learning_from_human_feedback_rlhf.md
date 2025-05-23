---
title: Reinforcement Learning from Human Feedback (RLHF)
videoId: Wo95ob_s_NI
---

From: [[dwarkesh | The Dwarkesh Podcast]]

Reinforcement Learning from Human Feedback (RLHF) is a critical component of the post-training process for large language models (LLMs). It aims to align model behavior with human preferences and intentions, making them more helpful, harmless, and honest. John Schulman, a co-founder of OpenAI who leads the post-training team and led the creation of ChatGPT [00:00:24]-[00:00:30], discusses various aspects of RLHF and its impact on models like ChatGPT.

## Overview and Purpose

The primary goal of post-training, which includes RLHF, is to refine a pre-trained model that can generate content resembling "random web pages" [00:01:23] into a more targeted and useful AI. Instead of merely imitating diverse internet content, RLHF optimizes models towards a "narrower range of behaviors" [00:02:08], such as behaving like a helpful chat assistant [00:02:17]. The objective shifts from predicting the next token to "producing outputs that humans will like and find useful" [00:02:30].

## Mechanism of RLHF

RLHF operates by training models based on human judgments about the quality of their outputs.

*   **Objective:** The model is trained to maximize "human approval as measured by a reward model" [00:31:15]. Essentially, it's "trying to produce something that people are going to like and judge as correct" [00:31:20].
*   **Analogy:** This process can be likened to having a "drive" or "goal" [00:30:21], steering the model "towards a certain set of states rather than some other states" [00:30:29].
*   **Iterative Process:** RLHF often involves an iterative approach. If not full reinforcement learning, a similar effect can be achieved through "iterative supervised fine-tuning where humans edit the model-generated outputs" [00:48:28]. This is because models may initially struggle to perfectly replicate high-quality human data if it's outside their immediate capabilities [00:48:41].

## Impact on Model Behavior and Capabilities

RLHF significantly shapes how models behave and what they can reliably do.

### Shaping Persona and Style
*   RLHF helps instill a "specific persona," such as a helpful chat assistant that isn't just trying to imitate a person but is focused on answering questions and performing tasks [00:02:17]-[00:02:25].
*   The "helpful robot" persona adopted in chat interfaces was intuitive for human labelers and the model alike, leading to "a much more coherent personality and it was much easier to get pretty sensible behavior robustly" [00:47:09]-[00:47:36].

### Improving Reliability and Safety
*   **Addressing Hallucinations:** RLHF can make significant progress on issues like "blatant hallucination" using "pretty straightforward methods" [00:46:40].
*   **Understanding Limitations:** A key improvement brought by RLHF is teaching models their own limitations. Early ChatGPT versions might "think that it could send you an email or call you an Uber" [00:15:18]. A small amount of data (e.g., ~30 examples) explaining these limitations generalized well to other untrained capabilities [00:15:29]-[00:15:53]. This understanding was a notable feature of chat models refined with RLHF [00:46:19].
*   **Factuality:** ChatGPT, developed with RLHF, showed improvements in "factuality" compared to earlier models [00:49:28].

### Enhancing User Experience
*   RLHF makes models "easier to use" than base models, which often require "elaborate" and carefully constructed prompts with examples [00:41:52]-[00:42:06].

## RLHF in the Development of ChatGPT

The creation of ChatGPT heavily relied on RLHF techniques.
*   OpenAI initially had "instruction following models" which were fine-tuned base models designed to be easier to prompt [00:41:52]-[00:42:20].
*   ChatGPT built on this, focusing on a "conversational chat assistant" [00:43:59]. Data from both instruction-following and chat efforts were combined to create a model that was easy to use and sensible about its limitations [00:46:02]-[00:46:19].
*   Replicating ChatGPT externally would have required more than a single fine-tuning iteration, likely involving RL or iterative supervised fine-tuning with human edits of model outputs [00:47:52]-[00:48:57]. This can be compared to the ongoing advancements at Meta as seen in [[llama_3_and_ai_advancements_at_meta | Llama 3 and AI advancements at Meta]].
*   An earlier RL-trained instruction-following model, if put in a chat wrapper, would have been "decently close" but differed in strengths (e.g., better at writing/poetry, worse on limitations/factuality) [00:49:04]-[00:49:28].

## Challenges and Considerations in RLHF

Despite its benefits, RLHF presents several challenges.

### Behavioral Quirks
*   **Standardized Speech Patterns:** Models trained with RLHF can develop a "very similar way of speaking," often using phrases like "delve into things," preferring bullet points, and adopting a formal, sometimes "dull," tone [01:20:44]-[01:20:55]. This can lead to complaints about reduced creativity [01:21:03]. Schulman notes that OpenAI is "actively trying to improve this and make the writing more lively and fun" [01:21:27].
*   **Verbosity:** Models can be "persistently more verbose than some people want" [01:23:25]. This might stem from labelers preferring more verbose answers during rating [01:23:31], or from training one message at a time, where longer, comprehensive messages might appear more complete than shorter, interactive ones [01:23:42]-[01:24:05]. User preference for verbosity might also vary with output speed [01:24:13].
*   **Origin of "Ticks":** The prevalence of certain words (e.g., "delve") is an interesting phenomenon, with Schulman humorously noting he'd caught himself using it [01:21:54]-[01:22:00]. Some traits, like bullet points, are genuinely preferred by users [01:22:44]. For an in-depth look at how standardized patterns can develop across platforms, see [[open_source_ai_models_and_their_implications | Open source AI models and their implications]].

### Influence of Raters
*   **Rater Demographics:** Raters are an "international group," often sourced from platforms like Upwork [01:30:07]. Skills vary, with STEM task raters often from India or other middle/lower-middle income countries, and English writing raters more US-based [01:30:29]-[01:30:45]. Some raters are highly skilled and careful [01:31:03]-[01:31:11].
*   **Unintentional Distillation:** A convergence in chatbot styles might occur if labelers use existing models to help generate responses for labeling tasks, leading to "unintentional distillation" [01:22:10]-[01:22:38].

### Aggregating Preferences and Defining "Good" Behavior
*   Aggregating preferences across diverse humans is a complex task, especially for more powerful systems [01:11:11]. Further analysis can be found in [[ai_economic_and_societal_structures | Impact of AI on economic and societal structures]].
*   **The Model Spec:** OpenAI uses a document called the "Model Spec" to guide model behavior in products like ChatGPT and the API [01:12:16]-[01:12:25]. It considers various stakeholders: the end-user, the developer, the platform (OpenAI), and "the rest of humanity" [01:12:32]-[01:13:16].
*   **Conflict Resolution:** The Spec aims to provide actionable guidance for resolving conflicts between stakeholder desires, generally prioritizing user/developer instructions unless they cause harm, while striving for neutrality and avoiding paternalism [01:14:05]-[01:14:49]. The document uses examples of non-obvious situations to clarify desired behavior [01:15:26]-[01:15:36].

## Future of RLHF and Model Alignment

As models become more capable, RLHF techniques and their application in alignment will continue to evolve.

### Adapting RLHF for Advanced Models
*   For future models (e.g., GPT-6, GPT-7), a key question is whether to rely more on explicit written instructions (like a constitution) or continue with pairwise preferences, which capture subtle nuances hard to articulate [01:24:59]-[01:25:43]. A discussion of future advancements can be found in [[future_of_ai_interaction_in_everyday_life_and_personalization | Future of AI interaction in everyday life and personalization]].
*   It's hypothesized that "fuzzy preferences" from large datasets might be distillable into shorter documents [01:26:19].
*   More advanced models will automatically learn many concepts of helpfulness and even complex moral theories, but will still require specific guidance (e.g., a "decently long document") to "latch onto a specific style, a specific morality" [01:26:27]-[01:27:21].

### Role in Long-Horizon Tasks
*   RLHF and similar RL techniques will be crucial for training models to perform "longer projects" and more complex, multi-step tasks [00:04:29]-[00:04:51]. For further insights into complex task management, refer to [[challenges_and_opportunities_in_deploying_ai_at_scale | Challenges and opportunities in deploying AI at scale]].

### Ensuring Safety with More Capable Models
*   The current RLHF approach, where the model tries to produce text "pleasing to a human," is considered "very safe even though the models are very smart" [00:28:12]-[00:28:20]. The model's primary concern is the approval of its output [00:28:26].
*   For well-specified tasks (e.g., coding an app), even with tool use, the model's incentive remains focused on producing a high-quality final result, not on unrelated, potentially "wacky" intermediate goals [00:28:33]-[00:28:56]. However, ill-defined tasks like "make money" could lead to nefarious instrumental goals [00:29:30]-[00:29:39]. For an exploration of safety concerns, see [[ai_alignment_and_safety_concerns | AI alignment and safety concerns]].

## RLHF in the Broader AI Landscape

### Contribution to Model Improvement
*   Post-training, heavily featuring RLHF, is credited with "most of" the roughly 100-point Elo score increase in GPT-4 since its initial release [00:51:35]-[00:51:48]. This improvement stems from factors like data quality/quantity, iterative deployment and data collection, and evolving annotation types [00:52:05]-[00:52:16].
*   There is significant "room for improvement from post-training" [00:52:29].
*   The proportion of compute dedicated to post-training versus pre-training may increase. As model outputs can be higher quality than average web content, it makes sense for models to "think by itself" more, guided by RLHF [00:50:52]-[01:51:13]. The role of compute in AI development was further discussed in [[role_of_compute_in_ai_development | Role of compute in AI development]].

### RLHF as a Competitive Factor ("Moat")
*   Expertise in post-training, including RLHF, can serve as a "moat" for AI companies due to its complexity, the need for skilled personnel, and the accumulation of "tacit knowledge and organizational knowledge" [01:27:47]-[01:28:04].
*   Creating fully functional models via post-training is a "pretty complicated effort" requiring substantial R&D [01:28:14]-[01:28:36]. Leading pre-training companies are also typically leaders in post-training [01:28:45].
*   However, this moat can be somewhat diminished by practices like model distillation or using outputs from leading models for cloning or as judges, which smaller players might employ to catch up (though this may violate terms of service) [01:29:06]-[01:29:33]. Understanding implications in competitive environments can relate to discussions in [[ai_scalability_and_breakthroughs | AI scalability and breakthroughs]].