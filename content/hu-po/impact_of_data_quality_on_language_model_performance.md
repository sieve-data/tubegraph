---
title: Impact of data quality on language model performance
videoId: yxAcTRp9EyQ
---

From: [[hu-po]] <br/> 

The paper "Textbooks Are All You Need," published by Microsoft Research in June 2023, introduces Phi-1, a new [[advancements_in_language_models | language model]] for code that demonstrates the significant impact of high-quality, curated data on model performance, even with a substantially smaller model size and reduced compute requirements <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

## Introducing Phi-1: A Smaller, Capable Code Model

Phi-1 is a Transformer-based [[model_architecture_and_data_quality_in_ai | model architecture]] with 1.3 billion parameters, which is considered "pretty small" compared to other [[comparison_of_language_models_in_coding_tasks | competing models]] like Falcon 40B (40 billion parameters) and LLaMA (65 billion parameters) <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

The model was trained for just four days on eight A100 GPUs, which is considered "relatively cheap" compared to the millions of dollars typically required for training larger models <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The use of eight A100s is significant because it represents the capacity of a single server rack <a class="yt-timestamp" data-t="00:55:05">[00:55:05]</a>.

## The Power of Textbook Quality Data

The core hypothesis of the paper is that the quality of training data can dramatically change scaling laws, potentially allowing smaller models with leaner training to match the performance of large-scale models <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. This approach focuses on using [[textbook_data_for_language_models | textbook quality data]] selected from the web and synthetically generated <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

> "It has long been known the higher quality data leads to better results" <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>
> "improving data quality can dramatically change the shape of those scaling laws potentially allowing to match the performance of large-scale models with much leaner training and models" <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>

The paper draws an analogy between training a neural network and teaching a human child, suggesting that the "curriculum" or choice of information and its timing for training a neural network matters <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. This contrasts with common [[training_and_finetuning_of_language_models_for_code | pre-training]] methods for large [[advancements_in_language_models | language models]] which do not typically involve a slowly building curriculum of complexity <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

### Performance Benchmarks

Despite its small scale, Phi-1 achieved a "pass@1 accuracy" of 50.6% on HumanEval and 55% on MBP (Mostly Basic Python Programs) <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. The smaller Phi-1 small model, with only 350 million parameters, still achieved 45% accuracy on these benchmarks <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. This performance is particularly impressive given that it uses significantly less data and compute than larger, competing models <a class="yt-timestamp" data-t="01:32:19">[01:32:19]</a>. For instance, it outperforms StarCoder, which is 10 times larger and trained on over 10 times more tokens <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

## Data Curation and Synthetic Generation

The authors emphasize that standard code datasets, while large and diverse, are often not ideal for teaching models the basics of coding. Many snippets are not self-contained, are poorly documented, or are skewed towards specific, less instructive topics like coding challenges <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. This is akin to the frustration a human learner would experience trying to acquire coding skills from such disorganized data <a class="yt-timestamp" data-t="00:30:16">[00:30:16]</a>.

The "textbook quality" data used for Phi-1 is characterized by being:
*   Clear <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>
*   Self-contained <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>
*   Instructive <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>
*   Balanced <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>

The data used in this paper consists of two main categories:

1.  **Filtered Code Language Dataset:** A subset of deduplicated Python files from "the stack" (a 6 terabyte dataset of open-source code) and Stack Overflow, annotated for quality using a Transformer-based classifier <a class="yt-timestamp" data-t="00:32:28">[00:32:28]</a>. The annotation process was conducted by GPT-4 to determine a sample's "educational value" <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>.
    *   Examples of high educational value code snippets are clear, self-contained functions with doc strings, contrasting with low educational value snippets that depend on external, undefined modules <a class="yt-timestamp" data-t="00:35:45">[00:35:45]</a>.

2.  **Synthetic Data Sets:**
    *   **Synthetic Textbook Data Set:** Less than 1 billion tokens, generated by GPT-3.5. This data consists of natural language explanations interleaved with relevant code snippets, similar to a textbook, and targeted topics promoting reasoning and basic algorithms <a class="yt-timestamp" data-t="00:41:29">[00:41:29]</a>. Diversity in this dataset was achieved by providing constraints on topics and target audiences to GPT-3.5 <a class="yt-timestamp" data-t="00:42:12">[00:42:12]</a>.
    *   **Small Synthetic Exercises Data Set:** Less than 100 million tokens, also generated by GPT-3.5. This dataset comprises Python exercises where the model completes a function based on its docstring, used for [[finetuning_large_language_models | fine-tuning]] <a class="yt-timestamp" data-t="00:43:45">[00:43:45]</a>. Diversity here was achieved by constraining function names <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>.

The total dataset size for both [[training_and_finetuning_of_language_models_for_code | pre-training]] and [[finetuning_large_language_models | fine-tuning]] combined was less than 7 billion tokens <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### Training Methodology
The model uses a decoder-only Transformer architecture, employing techniques like Flash Attention for [[compute_efficiency_in_language_models | compute efficiency]] and Rotary Position Embeddings (RoPE) <a class="yt-timestamp" data-t="00:47:55">[00:47:55]</a>. [[quantization_of_language_models | Floating Point 16 (FP16)]] precision was used for training <a class="yt-timestamp" data-t="00:54:06">[00:54:06]</a>.

For [[training_and_finetuning_of_language_models_for_code | pre-training]], Phi-1 base was trained on the filtered code language and synthetic textbook data for 36,000 steps with a batch size of 1024, equivalent to eight epochs <a class="yt-timestamp" data-t="00:57:26">[00:57:26]</a>. [[finetuning_large_language_models | Fine-tuning]] for Phi-1 on the synthetic exercises dataset used a smaller batch size (256) and learning rate (1e-4) for 6,000 steps <a class="yt-timestamp" data-t="00:59:45">[00:59:45]</a>.

## Emergent Abilities and Generalization

A remarkable finding was that [[finetuning_large_language_models | fine-tuning]] on short Python coding exercises unexpectedly improved the model's ability to execute tasks not featured in the [[finetuning_large_language_models | fine-tuning]] dataset <a class="yt-timestamp" data-t="01:01:17">[01:01:17]</a>. This included managing intricate algorithmic tasks and using external libraries like Pygame and Tkinter, even though these libraries were not present in the [[finetuning_large_language_models | fine-tuning]] data <a class="yt-timestamp" data-t="01:03:56">[01:03:56]</a>. This suggests that [[finetuning_large_language_models | fine-tuning]] helped the model reorganize and consolidate knowledge acquired during [[training_and_finetuning_of_language_models_for_code | pre-training]] <a class="yt-timestamp" data-t="01:01:37">[01:01:37]</a>.

Additionally, Phi-1 showed better chat capabilities than its base model, despite chat functionality being exclusive to the [[training_and_finetuning_of_language_models_for_code | pre-training]] phase and not the [[finetuning_large_language_models | fine-tuning]] <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. This highlights the model's capacity for generalizing beyond its explicit [[training_and_finetuning_of_language_models_for_code | training]] distribution.

## Addressing Contamination and Evaluation Bias

The paper addresses concerns about data contamination, especially given that benchmarks are often publicly available and could lead to models being trained on the test sets <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>. To minimize bias, new evaluation problems were created by a dedicated team that did not have access to the [[finetuning_large_language_models | fine-tuning]] data or the final model <a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>.

To further ensure fair evaluation, the authors used a "pruning" method (similar to trimming a tree) to aggressively remove up to 40% of the [[training_and_finetuning_of_language_models_for_code | training]] data, based on embedding and syntax-based distances, and still observed strong performance <a class="yt-timestamp" data-t="01:23:43">[01:23:43]</a>. This process was deemed more insightful than standard contamination studies based on simple overlap measures <a class="yt-timestamp" data-t="01:24:45">[01:24:45]</a>.

The paper also explores using GPT-4 as a grader for evaluation, acknowledging that while it leverages GPT-4's vast knowledge, it might introduce biases due to GPT-4's "superhuman ability" to detect subtle patterns in code structure or word choice that humans might not <a class="yt-timestamp" data-t="01:20:24">[01:20:24]</a>.

## Limitations

Despite its successes, Phi-1 has limitations:
*   It is specialized in Python coding <a class="yt-timestamp" data-t="01:32:37">[01:32:37]</a>.
*   It lacks deep domain-specific knowledge for particular APIs due to the structured nature of its dataset <a class="yt-timestamp" data-t="01:32:48">[01:32:48]</a>.
*   It is less robust to stylistic variations or errors in prompts compared to larger models like GPT-4 or StarCoder <a class="yt-timestamp" data-t="01:32:55">[01:32:55]</a>. This "sensitivity to prompt variations" might be a property of smaller models where their learned data compression is more "fragile" <a class="yt-timestamp" data-t="01:40:48">[01:40:48]</a>.

## Conclusion

The paper concludes that developing methodologies for creating high-quality, thoughtfully curated data sets is a central direction for [[advancements_in_language_models | advancing natural language processing]] <a class="yt-timestamp" data-t="01:33:30">[01:33:30]</a>. This includes ensuring data covers relevant concepts, is diverse, and non-repetitive <a class="yt-timestamp" data-t="01:33:44">[01:33:44]</a>. The findings suggest that synthetic data generation, perhaps even from more advanced models like GPT-4, holds significant promise for [[training_and_finetuning_of_language_models_for_code | training]] specialized and efficient [[advancements_in_language_models | language models]] <a class="yt-timestamp" data-t="01:33:06">[01:33:06]</a>. This could lead to models tailored for specific applications or cultural contexts, demonstrating the potential for data quality to lead to more efficient and capable AI <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>.