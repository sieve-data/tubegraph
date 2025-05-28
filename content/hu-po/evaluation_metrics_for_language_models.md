---
title: evaluation metrics for language models
videoId: yxAcTRp9EyQ
---

From: [[hu-po]] <br/> 

Evaluating [[large_language_models and their applications | large language models]] (LLMs) is a complex and evolving field. While various benchmarks exist, there's an ongoing discussion about their effectiveness and the trustworthiness of reported scores <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a> <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.

## Current Benchmarks and Their Limitations

Many publicly available leaderboards, such as the Hugging Face Open LLM Leaderboard, track different [[large_language_models and their applications | language models]] and their performance on various benchmarks <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a> <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. However, these benchmarks are not always considered ideal <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

Common benchmarks mentioned include:
*   **HumanEval** <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a> <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>: This benchmark assesses a model's ability to generate code, often for simple Python functions from their docstrings <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a> <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. The "pass at one accuracy" metric, common in HumanEval, means the model must provide the correct solution on its first attempt <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>.
*   **MBP (Mostly Basic Python Programs)** <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a> <a class="yt-timestamp" data-t="01:05:01">[01:05:01]</a>: Another benchmark for Python code generation.

A significant issue is the lack of standardized benchmarks, making direct comparisons between models difficult across different leaderboards <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a> <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. The general sentiment is that many current benchmarks are flawed <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Contamination Concerns

A major challenge in evaluating LLMs, especially with publicly available benchmarks, is the risk of "contamination" or "memorization" <a class="yt-timestamp" data-t="01:14:07">[01:14:07]</a> <a class="yt-timestamp" data-t="01:14:11">[01:14:11]</a>. If a model's training data includes the benchmark's test data, its high scores may not reflect true generalized ability but rather memorization <a class="yt-timestamp" data-t="01:14:31">[01:14:31]</a> <a class="yt-timestamp" data-t="01:15:22">[01:15:22]</a>. This raises questions about the trustworthiness of reported scores, particularly when there's an incentive to achieve high rankings on leaderboards <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a> <a class="yt-timestamp" data-t="01:15:51">[01:15:51]</a>.

To counter this, evaluation problems ideally should be unconventional enough to be unlikely to appear in any training dataset <a class="yt-timestamp" data-t="01:17:48">[01:17:48]</a> <a class="yt-timestamp" data-t="01:17:50">[01:17:50]</a>. This concept is akin to a double-blind placebo-controlled trial, where neither the model being tested nor those evaluating it know which test data is being used <a class="yt-timestamp" data-t="01:18:09">[01:18:09]</a> <a class="yt-timestamp" data-t="01:18:33">[01:18:33]</a>.

## Nuanced Evaluation and AI Graders

Traditional code evaluation is often binary (pass or fail unit tests) <a class="yt-timestamp" data-t="01:19:30">[01:19:30]</a>. However, this doesn't capture the nuances of a model's performance, such as almost-correct code with minor errors or completely wrong code that incidentally passes some tests <a class="yt-timestamp" data-t="01:19:44">[01:19:44]</a>.

A more informative approach, similar to how human coders are evaluated, involves comparing a model's output to a correct solution and grading it based on how well it matches the expected logic and reasoning <a class="yt-timestamp" data-t="01:19:53">[01:19:53]</a> <a class="yt-timestamp" data-t="01:20:10">[01:20:10]</a>.

### Using LLMs as Graders
Some approaches involve using powerful [[large_language_models and their applications | LLM]]s, like GPT-4, to grade the solutions of other models <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>. This leverages the grader's knowledge and generative abilities to obtain a more fine-grained signal of the student model's coding capabilities <a class="yt-timestamp" data-t="01:21:30">[01:21:30]</a> <a class="yt-timestamp" data-t="01:21:32">[01:21:32]</a>.

However, this method also comes with potential controversies:
*   **Bias**: There's a concern that the AI grader might introduce its own biases, potentially grading solutions based on subtle patterns like word ordering, word choice, or stylistic elements that humans might not prioritize <a class="yt-timestamp" data-t="01:22:34">[01:22:34]</a> <a class="yt-timestamp" data-t="01:22:38">[01:22:38]</a>. This is because LLMs are highly adept at next token prediction, which might give them a "superhuman" sense of linguistic coherence beyond mere semantic correctness <a class="yt-timestamp" data-t="01:22:51">[01:22:51]</a> <a class="yt-timestamp" data-t="01:22:55">[01:22:55]</a>.
*   **Ethical implications**: Using LLMs to curate data for future LLMs raises ethical and social implications regarding accountability, transparency, and data/model bias <a class="yt-timestamp" data-t="01:36:01">[01:36:01]</a>.

## Detecting Contamination through Data Analysis

To address contamination, techniques like n-gram analysis are used to measure the similarity of text segments based on shared word sequences <a class="yt-timestamp" data-t="01:25:08">[01:25:08]</a>. If training and test datasets have significant n-gram overlap, it could indicate contamination <a class="yt-timestamp" data-t="01:25:47">[01:25:47]</a>.

More refined methods for detecting code similarity include:
*   **Embedding-based distances**: Such as L2 distance on the last layer (embedding) of a pre-trained model. This is effective in capturing code pairs with similar overall semantics <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a> <a class="yt-timestamp" data-t="01:28:31">[01:28:31]</a> <a class="yt-timestamp" data-t="01:28:37">[01:28:37]</a>.
*   **Syntax-based distances**: Calculating the string edit distance between the abstract syntax trees (ASTs) of code snippets. This can identify overlaps while being agnostic to non-syntax differences like variable names or comments <a class="yt-timestamp" data-t="01:28:43">[01:28:43]</a> <a class="yt-timestamp" data-t="01:29:05">[01:29:05]</a>. This is analogous to how college courses detect plagiarism in code <a class="yt-timestamp" data-t="01:29:37">[01:29:37]</a>.

Even after aggressively pruning training data, models trained on high-quality, curated datasets (like Phi-1 from Microsoft Research) can still outperform larger models trained on significantly more data but of lower quality <a class="yt-timestamp" data-t="01:24:24">[01:24:24]</a> <a class="yt-timestamp" data-t="01:32:19">[01:32:19]</a>. This highlights the importance of data quality over sheer quantity in achieving high model proficiency <a class="yt-timestamp" data-t="01:32:05">[01:32:05]</a> <a class="yt-timestamp" data-t="01:33:30">[01:33:30]</a>.

## The Future of Evaluation

The discussion suggests that the future of LLM evaluation will likely involve:
*   More sophisticated methods for creating and evaluating high-quality, diverse, and non-repetitive datasets <a class="yt-timestamp" data-t="01:33:39">[01:33:39]</a> <a class="yt-timestamp" data-t="01:34:50">[01:34:50]</a>.
*   Potentially incorporating interactive learning environments with interpreters and reinforcement learning (RL) for training and evaluation <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a> <a class="yt-timestamp" data-t="01:09:04">[01:09:04]</a>.
*   A deeper consideration of how to measure "emergent abilities" or "spikes in model capacity" that appear unexpectedly after fine-tuning <a class="yt-timestamp" data-t="01:00:25">[01:00:25]</a> <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>. This is when a model suddenly exhibits a substantial improvement in tasks not explicitly featured in its fine-tuning data, suggesting a reorganization and consolidation of knowledge acquired during pre-training <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a> <a class="yt-timestamp" data-t="01:04:10">[01:04:10]</a>.
*   Addressing the challenge of [[vulnerability of aligned language models | prompt sensitivity]] in models, especially smaller ones, which can show inconsistent behavior with minor changes in prompts <a class="yt-timestamp" data-t="01:40:30">[01:40:30]</a>. This suggests that the "local minima" (or compressed data distribution) found by smaller models might be more fragile compared to the deeper, more consistent ones found by larger models <a class="yt-timestamp" data-t="01:40:46">[01:40:46]</a>.