---
title: Comparison of language models in coding tasks
videoId: yxAcTRp9EyQ
---

From: [[hu-po]] <br/> 

## Phi-1: A Small Model, Big Impact
Microsoft Research introduced Phi-1, a new [[training_and_finetuning_of_language_models_for_code | language model]] specifically designed for code, released on June 20, 2023 <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This model stands out due to its significantly smaller size compared to competing models <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Phi-1 is built on a Transformer-based, decoder-only architecture <a class="yt-timestamp" data-t="00:46:27">[00:46:27]</a>, which is a popular choice for [[advancements_in_language_models | large language models]] <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

### Model Parameters and Training Cost
The base Phi-1 model has 1.3 billion parameters <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>, which is notably smaller than models like Falcon (40 billion parameters) or Llama (65 billion parameters) <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. A smaller version, Phi-1 small, has only 350 million parameters <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

Phi-1 was trained for just four days on eight A100 GPUs <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>, which is considered a relatively low cost, estimated in the tens of thousands of dollars rather than hundreds of thousands or millions <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This low compute cost for training highlights a focus on [[compute_efficiency_in_language_models | compute efficiency]] <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>.

### Data Quality Over Quantity
A key aspect of Phi-1's success is its reliance on high-quality training data, rather than simply massive datasets <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. The model was trained on a selection of [[textbook_data_for_language_models | textbook-quality data]] from the web (6 billion tokens) and [[textbook_data_for_language_models | synthetically generated textbooks]] (1 billion tokens) using GPT-3.5 <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. The fine-tuning phase used an even smaller dataset of less than 200 million synthetically generated coding exercises <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

The researchers hypothesize that improving data quality can dramatically change [[large_language_models_and_optimization | scaling laws]], allowing for the matching of large-scale model performance with much leaner training and models <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. They explicitly state that traditional web-based data sources like "the Stack" are not optimal for teaching models to plan and reason, due to issues like code snippets not being self-contained or having low educational value <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. High-quality data, akin to a human textbook, should be clear, self-contained, instructive, and balanced <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>.

The synthetic data generation process involved constraining topics and target audiences to ensure diversity, avoiding homogeneous and redundant datasets that often result from simply prompting a [[large_language_models_in_machine_learning_research | language model]] <a class="yt-timestamp" data-t="00:39:06">[00:39:06]</a>.

### Performance on Coding Benchmarks
Despite its small scale, Phi-1 achieved a pass@1 accuracy of 50% on HumanEval and 55% on MBPP (Mostly Basic Python Programs) benchmarks <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>, <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. Pass@1 accuracy means the model must get the correct answer on the first attempt <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

A direct [[comparison_of_different_vision_language_models | comparison]] with StarCoder, a model more than 10 times larger and trained on over 10 times more tokens, showed that Phi-1 achieved a better score on HumanEval <a class="yt-timestamp" data-t="01:21:01">[01:21:01]</a>.

## Emergent Capabilities
Fine-tuning Phi-1 on coding exercises unexpectedly improved the model's ability to use external libraries like Pygame and Tkinter, even though these libraries were not present in the fine-tuning dataset <a class="yt-timestamp" data-t="01:03:54">[01:03:54]</a>. This highlights a phenomenon sometimes referred to as "emergent behavior" or "emergent abilities," where models gain capabilities not explicitly trained for <a class="yt-timestamp" data-t="01:00:25">[01:00:25]</a>. This suggests that fine-tuning helps the model reorganize and consolidate knowledge acquired during pre-training <a class="yt-timestamp" data-t="01:01:37">[01:01:37]</a>.

For example, when asked to generate Pygame code, the Phi-1 base model used `pygame.display.flip()`, while the fine-tuned Phi-1 model used `pygame.display.update()`, which is an optimized version of `flip()` <a class="yt-timestamp" data-t="01:08:40">[01:08:40]</a>.

## Benchmarking and Contamination Concerns
The abundance and sometimes inconsistent nature of benchmarks for [[large_language_models_in_machine_learning_research | large language models]] pose challenges for direct comparison <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. The researchers specifically addressed concerns about data contamination, where models might perform well on benchmarks because the benchmark data was accidentally included in their training sets <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>.

To combat this, they used:
*   **GPT-4 for annotation**: GPT-4 was used to annotate a small subset of code quality, which then trained a random forest classifier to filter the larger dataset <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>. This process was seen as a way to avoid tedious human annotation <a class="yt-timestamp" data-t="00:34:49">[00:34:49]</a>.
*   **Unconventional evaluation problems**: A dedicated team created new evaluation problems designed to be unlikely to appear in any training dataset, minimizing bias and leakage <a class="yt-timestamp" data-t="01:17:47">[01:17:47]</a>.
*   **GPT-4 as a grader**: GPT-4 was used to grade solutions to capture nuances beyond simple pass/fail unit tests <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>.
*   **Data pruning**: Even after aggressively pruning over 40% of the fine-tuning data, Phi-1 still outperformed StarCoder, suggesting the benefit comes from quality, not just memorization <a class="yt-timestamp" data-t="01:24:34">[01:24:34]</a>.
*   **Embedding and syntax-based distances**: Instead of just n-gram analysis, a combination of embedding distance (L2 distance of last layer embeddings) and abstract syntax tree (AST) string edit distance was used to identify similar code snippets for pruning <a class="yt-timestamp" data-t="01:27:57">[01:27:57]</a>.

## Limitations
Despite its strong performance, Phi-1 has limitations:
*   **Specialized in Python**: The model is specialized in Python coding tasks <a class="yt-timestamp" data-t="01:32:37">[01:32:37]</a>.
*   **Lack of domain-specific knowledge**: It lacks deep domain-specific knowledge for complex APIs <a class="yt-timestamp" data-t="01:32:48">[01:32:48]</a>.
*   **Sensitivity to prompt variations**: Phi-1 is less robust to stylistic variations or errors in prompts compared to larger models <a class="yt-timestamp" data-t="01:32:55">[01:32:55]</a>, <a class="yt-timestamp" data-t="01:40:46">[01:40:46]</a>. This suggests that the model's "compression" of the data distribution might be more fragile <a class="yt-timestamp" data-t="01:40:48">[01:40:48]</a>. For instance, changing the number of layers in a prompt from "three" to "four" could cause it to fail <a class="yt-timestamp" data-t="01:41:47">[01:41:47]</a>.

The authors believe these limitations are not fundamental and can be addressed with further work <a class="yt-timestamp" data-t="01:33:01">[01:33:01]</a>. They also suggest that using GPT-4 for synthetic data generation instead of GPT-3.5 could lead to significant gains <a class="yt-timestamp" data-t="01:33:07">[01:33:07]</a>.

## Future Implications
This research suggests that developing effective methodologies for creating high-quality datasets is crucial for advancing [[advancements_in_language_models | natural language processing]] <a class="yt-timestamp" data-t="01:33:30">[01:33:30]</a>. The use of synthetic data generation, akin to "domain randomization" in computer vision, could be applied to text to increase diversity and prevent overfitting <a class="yt-timestamp" data-t="01:33:59">[01:33:59]</a>, <a class="yt-timestamp" data-t="01:34:09">[01:34:09]</a>.

The paper opens the door for further research into fine-tuning with synthetically generated "textbook" datasets, especially for aligning [[large_language_models_in_machine_learning_research | LLMs]] to specific behaviors or domains <a class="yt-timestamp" data-t="01:37:31">[01:37:31]</a>. The continuous change in APIs for programming languages like Python also presents a challenge for [[quantization_of_language_models | LLM training]] and usage <a class="yt-timestamp" data-t="01:12:21">[01:12:21]</a>. The concept of recursive training, where LLMs curate data for future LLMs, raises ethical and social implications regarding accountability, transparency, and bias <a class="yt-timestamp" data-t="01:36:01">[01:36:01]</a>.