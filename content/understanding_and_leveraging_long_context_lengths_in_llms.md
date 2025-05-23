---
title: Understanding and leveraging long context lengths in LLMs
videoId: UTuuTTnjxMQ
---

From: [[dwarkesh | The Dwarkesh Podcast]]

This article summarizes a podcast discussion on the topic of long context lengths in Large Language Models (LLMs), drawing insights from Sholto (noted for his contributions to Gemini [00:01:32]) and Trenton (from Anthropic, working on [[mechanistic_interpretability_in_ai | mechanistic interpretability]] [00:01:37]). The conversation focused exclusively on capabilities, as alignment was humorously declared "solved" [00:01:51].

## Definition and Current State
Long context lengths refer to the ability of LLMs to process and utilize a large amount of information (e.g., a million tokens) within a single input or "context window" [00:02:05]. This capability has seen rapid advancements, with companies like Google and Magick reportedly achieving million-token attention windows [00:11:27], a significant jump from the 100K context windows introduced less than a year prior to the discussion [00:11:10].

## Perceived Importance
Despite its transformative potential, long context length was considered an "underhyped" topic during the discussion [00:01:59], [00:02:17]. Sholto noted that its importance was initially underestimated, even by those working directly on it, and that its impact was perhaps "buried by some other news" [00:02:41].

# Enhanced Capabilities with Long Context

## Improved Intelligence and Onboarding
Long context provides a significant step up in model intelligence by essentially solving the "onboarding problem" instantly [00:02:21], [00:02:24]. By providing millions of tokens of context, such as an entire codebase, models can become dramatically better at next-token prediction, an improvement typically associated with huge increments in model scale [00:02:29].

## In-Context Learning Prowess
The ability of models to learn within the provided context is a key benefit of longer context windows.

### Language Acquisition
An evaluation demonstrated a model learning an actual human language in context, reportedly better than a human expert could over a couple of months [00:02:56], [00:03:43]. Crucially, this language was esoteric enough not to be in the model's training data; without the context, the model showed no prior knowledge of the language [00:03:30], [00:03:34].

### Potential in Complex Tasks
There is interest in exploring long context for tasks like learning Atari games by providing a few hundred or a thousand frames of labeled actions, similar to how one might teach a friend [00:03:08]. While current infrastructure makes this slow, it's speculated that it might "just work out of the box" [00:03:21], [00:03:26].

## "Superhuman" Memory and Information Integration
Long context allows models to integrate vast amounts of information—like an entire codebase—far exceeding human working memory capacity [00:03:47], [00:03:52]. This is seen as a "huge unlock," enabling models to "know things that you don't" by ingesting information in a way humans cannot [00:04:02], [00:04:15].

# Understanding In-Context Learning Mechanisms

## Analogy to Gradient Descent
One way to understand in-context learning is by likening it to gradient descent [00:04:27]. Research suggests the attention operation can be viewed as performing gradient descent on the in-context data [00:04:33]. Studies have shown that `n` layers of in-context learning can look very similar to `n` steps of gradient descent [00:04:38]. For example, when a model was taught linear regression through context examples, its loss decreased with the number of "shots" (examples) in a way that exactly matched the number of gradient descent steps [00:05:39], [00:05:55].

## The Role of Meta-Learning
For models to excel at long-context tasks, they must improve at "learning to learn" from the examples or context within the window [00:06:03], [00:06:09]. This implies that meta-learning is a crucial component, suggesting that the task of intelligence itself may require long-context examples and training [[challenges_and_methodologies_in_ai_training_and_data_usage | challenges and methodologies in AI training and data usage]] [00:06:16], [00:06:30]. Understanding how to better induce meta-learning during pre-training is vital for developing flexible and adaptive intelligence [00:06:39].

## Safety Considerations
The power of in-context learning also presents potential safety challenges. There's concern about what happens if a model is given a "hundred shot prompt for jailbreaks" or adversarial attacks [00:05:00], [00:05:07]. If a model is effectively performing gradient descent and learning on the fly, even a model trained to be harmless could transform into a "totally new model" in ways that are difficult to control [00:05:16], [00:05:21].

# Long Context, Long-Horizon Tasks, and AI Agents

## The Bottleneck: Context vs. Reliability
While long context is necessary for AI to perform long-horizon tasks (i.e., tasks requiring engagement for hours, weeks, or months [00:06:53]), it was argued that it hasn't been the primary limiting factor for AI agents taking off [00:07:25], [00:08:01]. Instead, the bottleneck is more about achieving sufficient "nines of reliability" in task execution [[challenges_and_opportunities_in_deploying_ai_at_scale | challenges and opportunities in deploying AI at scale]] [00:07:30]. If a model cannot chain tasks successively with a high enough probability of success, agent-like behavior won't emerge [00:07:35]. The issue is less about the context window size and more about the base task solve rate; if the rate is, for example, 90%, chaining tasks becomes problematic, but at 99%, it's less of an issue [00:09:48].

## Evaluating Performance on Extended Tasks
Current academic evaluations often focus on single problems rather than complex, long-horizon tasks [00:10:04]. There's a growing need for benchmarks like SWE-bench (which involves GitHub issues taking sub-hour to resolve) but extended to multi-hour or multi-day tasks. Understanding success rates on these longer tasks is crucial for judging the economic impact and capabilities of models, more so than scores on benchmarks like MMLU [00:10:35], [00:10:46].

# Technical Considerations: Attention Costs

## Debunking the "Quadratic Cost" Myth
The notion that long context windows are infeasible due to "quadratic attention costs" (O(n²)) has been challenged [00:11:14].
1. In typical dense transformers, the quadratic cost of attention is often dominated by the MLP (Multi-Layer Perceptron) block. There's also an n² term associated with the model's residual stream dimension (D_model) [00:11:44], [00:11:59].
2. According to a visualization by Sasha Rush, for very large models, the cost of attention can trail off, and context needs to be quite long before this term becomes truly dominant [00:12:08], [00:12:14].

## Inference Time Efficiency
When generating tokens at inference time, the attention operation is not n². A set of query (Q) vectors looks up key-value (KV) vectors, which is a linear operation (O(n)) with respect to the amount of context the model has [00:12:31], [00:12:39]. This understanding is important when considering research into linear attention, recurrence, and state-space models [00:12:52].

# Evaluating Long Context Models

## Challenges of Contamination and Recall
A significant challenge in evaluating long context models is ensuring that the evaluation material is not part of the model's training data [00:29:38]. For instance, a "Sherlock Holmes eval" where the entire book is put into context might be confounded if the novel was in the training set [[limitations_of_large_language_models_llms_in_solving_novel_tasks | limitations of large language models (LLMs) in solving novel tasks]] [00:29:17]. Excluding specific content from vast training datasets is a difficult task [00:29:44], [00:29:51].

Moreover, evaluations like the "needle in a haystack" test (e.g., recalling a fact from Paul Graham’s essays, as in the Gemini 1.5 paper [00:30:06]) focus on recall, but there's a need to assess deeper understanding and reasoning over long contexts [00:30:25].

## Designing Effective Benchmarks
Given that the models' primary loss function is unsupervised next-token prediction [00:30:30], there's an interest in developing unsupervised benchmarks. One approach involves using another LLM to rate the output of the model being tested, similar to Anthropic's constitutional RL paper where an LLM assesses helpfulness and harmlessness [[reinforcement_learning_from_human_feedback_rlhf | Reinforcement Learning from Human Feedback (RLHF)]] [00:30:58]. However, this method is imperfect and susceptible to issues like reward function hacking [00:31:18].

# Future Directions and Implications

## Learning in the Forward Pass
A potential trend is that more learning will occur in the "forward pass" of the model [00:13:16]. This is more sample efficient, akin to how humans think and process information while reading, rather than just inductively absorbing word sequences [00:13:53]. Long context provides an expanded working memory that facilitates this [00:14:18], and the emergence of meta-learning behavior (as seen from GPT-2 to GPT-3) is tied to the model's ability to adapt to context [[large_language_models_and_transfer_learning | Large Language Models and Transfer Learning]] [00:14:34].

## Accelerating AI Research and Automation
Long context is expected to significantly aid AI researchers by enabling models to act as highly effective "copilots." With super long context, models can be onboarded instantly to large codebases and assist with coding tasks, potentially speeding up research cycles [[ai_for_science_and_societal_challenges | AI for Science and Societal Challenges]] [00:35:31], [00:37:07], [00:54:10].

## The Role of Reasoning Traces and Synthetic Data
A key element missing from much training data is "reasoning traces" [00:55:12]. Long context could facilitate the generation and use of such data. If models can generate high-quality synthetic data that embodies complex reasoning (e.g., verified geometry proofs [[impact_of_ai_on_software_development_and_productivity | impact of AI on software development and productivity]] [00:57:34]), this could become a crucial ingredient for future model progress [00:53:42].

## The Future of Fine-Tuning
With advancements in adaptive compute and extremely long context windows, the distinction between fine-tuning and prompting might blur. It's conceivable that fine-tuning could become less necessary, as models can be specialized on-the-fly by providing vast amounts of relevant context [01:25:45], [01:25:51].