---
title: Textbook data for language models
videoId: yxAcTRp9EyQ
---

From: [[hu-po]] <br/> 

The paper "Textbooks Are All You Need" from Microsoft Research proposes and demonstrates that high-quality, curated, and synthetically generated data sets can significantly improve the proficiency of [[large_language_models_in_machine_learning_research | Large Language Models]] (LLMs) in code generation tasks, even with smaller model sizes and less training data <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This approach challenges the traditional scaling laws by emphasizing data quality over sheer data quantity <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

## The Phi-1 Model <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>

Phi-1 is a new [[advancements_in_language_models | language model]] for code introduced by Microsoft Research <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

*   **Size**: It is a Transformer-based model with 1.3 billion parameters, which is significantly smaller than competing models like Falcon 40B (40 billion parameters) and Llama 65B (65 billion parameters) <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. A smaller version, Phi-1 Small, has only 350 million parameters <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Training**: Phi-1 was trained for four days on eight Nvidia A100 GPUs, which represents a relatively low cost (tens of thousands of dollars compared to hundreds of thousands or millions) and minimal hardware (one server rack) <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The number eight is significant because most server racks are designed to hold exactly eight GPUs <a class="yt-timestamp" data-t="00:55:09">[00:55:09]</a>.

## The Impact of Data Quality <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>

The paper highlights that higher data quality leads to better results, a concept known in machine learning as data cleaning <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This can also lead to smaller data sets <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

*   **Redefining Scaling Laws**: Previous work like "Tiny Stories" showed that improving data quality can dramatically alter scaling laws, potentially allowing smaller models to match the performance of larger ones with less training <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Curriculum Analogy**: The process is likened to teaching a human child, where the choice of curriculum and the quality of information are crucial <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. A curriculum that gradually increases in complexity is beneficial <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
*   **Benefits**: Smaller models require less training, which can reduce the environmental cost of [[llm_large_language_models_development | LLM development]] (though the speaker questions the significance of this environmental impact compared to other human activities) <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

### Focus on Code Generation <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>

The research specifically focuses on training LLMs for code, particularly writing simple Python functions from their docstrings <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.

*   **Benchmarks**: The evaluation primarily uses HumanEval and MBP (Mostly Basic Python Programs), which are common benchmarks for [[comparison_of_language_models_in_coding_tasks | comparing LLM performance on code]] <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. Phi-1 achieves 50.6% accuracy on HumanEval and 55% on MBP <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Docstrings**: Docstrings are documentation strings within code that explain what a function does <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. The model's ability to complete functions based on these strings is key <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>. The name of the function and explicit type hints (like `X: int`) are also crucial for the model's understanding <a class="yt-timestamp" data-t="00:44:58">[00:44:58]</a>.
*   **Code for Logic**: Training on code makes LLMs better at general logic, not just code-specific logic. It acts as a "very strong prior for logic and kind of this Turing machine based reasoning" <a class="yt-timestamp" data-t="00:40:47">[00:40:47]</a>.

## Data Curation and Generation <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>

The paper critiques standard code datasets like The Stack and Stack Overflow, noting several issues <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>:
*   Not very instructive for learning coding basics <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
*   Many samples are not self-contained, depending on external modules or files <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.
*   Examples often lack meaningful computation or are buried in complex, poorly documented functions <a class="yt-timestamp" data-t="00:28:12">[00:28:12]</a>.
*   Skewed towards certain topics or use cases (e.g., coding challenge problems), resulting in an unbalanced distribution of concepts <a class="yt-timestamp" data-t="00:28:39">[00:28:39]</a>. This means models can become good at "toy problems" but not real-world production coding <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.

The researchers hypothesized that [[large_language_models_in_machine_learning_research | language models]] would benefit from a training set possessing qualities similar to a good textbook: clear, self-contained, instructive, and balanced <a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>.

### Data Sets Used <a class="yt-timestamp" data-t="00:31:27">[00:31:27]</a>

The study leveraged three key data sets, totaling less than 7 billion tokens:

1.  **Filtered Code Language Data Set**: A subset of The Stack and Stack Overflow, filtered for quality <a class="yt-timestamp" data-t="00:31:27">[00:31:27]</a>.
2.  **Synthetic Textbook Data Set**: Less than 1 billion tokens, generated by GPT-3.5. This dataset consists of natural language-heavy text interleaved with relevant code snippets, covering topics that promote reasoning and algorithmic skills <a class="yt-timestamp" data-t="00:41:30">[00:41:30]</a>.
3.  **Small Synthetic Exercises Data Set**: Less than 100 million tokens, also generated by GPT-3.5. Each exercise is a docstring of a function that needs to be completed, aiming to align the model for function completion tasks based on natural language instructions <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>.

The combination of the filtered code and synthetic textbook data was used for pre-training (to get Phi-1 Base), and the synthetic exercises data set was used for fine-tuning (to get Phi-1) <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>.

### Filtering Methodology <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>

To filter existing code datasets, the researchers used a Transformer-based classifier <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>. They manually annotated a small subset of Python files from The Stack and Stack Overflow for quality (determining "educational value" for a student learning basic coding concepts) <a class="yt-timestamp" data-t="00:33:06">[00:33:06]</a>. Interestingly, this annotation was performed by GPT-4, effectively avoiding tedious human annotation <a class="yt-timestamp" data-t="00:34:41">[00:34:41]</a>. This labeled data then trained a random forest classifier to predict the quality of other files using embeddings from a pre-trained Cogen model as features <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>.

### Challenges in Synthetic Data Generation <a class="yt-timestamp" data-t="00:37:54">[00:37:54]</a>

A key challenge with synthetic data is ensuring diversity and avoiding repetition <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a>. Simply prompting a model can lead to homogeneous and redundant datasets, as LLMs tend to follow the most probable paths <a class="yt-timestamp" data-t="00:38:55">[00:38:55]</a>. The paper highlights the need to find "the right trick" to induce more creative and diverse outputs while maintaining quality and coherence <a class="yt-timestamp" data-t="00:39:32">[00:39:32]</a>. One advantage of code is that it can be objectively tested for correctness, making synthetic generation easier <a class="yt-timestamp" data-t="00:39:43">[00:39:43]</a>.

## Model Architecture and Training Details <a class="yt-timestamp" data-t="00:46:23">[00:46:23]</a>

Phi-1 uses a decoder-only Transformer model, a common architecture for generative LLMs <a class="yt-timestamp" data-t="00:47:53">[00:47:53]</a> (the paper's title is a pun on "Attention Is All You Need," the original Transformer paper) <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>.

*   **Key Components**: It incorporates modern optimizations such as Flash Attention (to reduce memory and compute footprint) <a class="yt-timestamp" data-t="00:48:31">[00:48:31]</a>, Multi-Head Attention (MHA), Multi-Layer Perceptron (MLP) layers <a class="yt-timestamp" data-t="00:48:45">[00:48:45]</a>, and Rotary Position Embeddings (RoPE) <a class="yt-timestamp" data-t="00:50:40">[00:50:40]</a>.
*   **GPT-NeoX Architecture**: The 1.3 billion parameter model has 24 layers, a hidden dimension of 2048, and 32 attention heads <a class="yt-timestamp" data-t="00:50:03">[00:50:03]</a>.
*   **Training Parameters**:
    *   Sequence length: 2048 tokens <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>.
    *   Precision: Floating Point 16 (FP16), a common choice for [[quantization_of_language_models | quantized training]] that balances performance and memory <a class="yt-timestamp" data-t="00:54:04">[00:54:04]</a>.
    *   Optimization: Linear warm-up, linear decay learning rate schedule, and attention residual Dropout <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.
    *   Batch size: 1024 (large, requiring server-rack level hardware) <a class="yt-timestamp" data-t="00:57:28">[00:57:28]</a>.
    *   Total steps: 36,000 for pre-training (Phi-1 Base), equivalent to eight epochs over the code textbook data set, processing over 50 billion tokens <a class="yt-timestamp" data-t="00:57:48">[00:57:48]</a>.
    *   Fine-tuning (Phi-1): An additional seven hours on the same hardware, with a smaller batch size (256) and learning rate (1e-4) to avoid overwriting pre-training progress <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>.

## Emergent Capabilities and Generalization <a class="yt-timestamp" data-t="01:01:10">[01:01:10]</a>

The fine-tuning process resulted in unexpected "spikes of model capacity" or emergent behaviors <a class="yt-timestamp" data-t="01:00:25">[01:00:25]</a>.
*   Phi-1 exhibited a substantial improvement in executing tasks not explicitly featured in the fine-tuning data set, such as managing intricate algorithmic tasks and using external libraries like Pygame and Tkinter <a class="yt-timestamp" data-t="01:01:15">[01:01:15]</a>. This suggests that fine-tuning helps reorganize and consolidate knowledge from pre-training, enabling [[large_language_models_in_machine_learning_research | generalization]] to unrelated tasks <a class="yt-timestamp" data-t="01:04:08">[01:04:08]</a>.
*   The model also showed improved chat capabilities despite chat being exclusive to pre-training and not fine-tuning, demonstrating its ability to extrapolate beyond its immediate training distribution <a class="yt-timestamp" data-t="01:12:58">[01:12:58]</a>.

### Contamination and Evaluation <a class="yt-timestamp" data-t="01:14:07">[01:14:07]</a>

A common concern with strong performance on benchmarks is "contamination" (the model having seen the test data during training) <a class="yt-timestamp" data-t="01:14:07">[01:14:07]</a>. The paper addressed this by:
*   Using new, "unconventional" evaluation problems created by a dedicated team with no access to the training data or final model <a class="yt-timestamp" data-t="01:17:45">[01:17:45]</a>. This is akin to a double-blind placebo-controlled trial in medicine <a class="yt-timestamp" data-t="01:18:09">[01:18:09]</a>.
*   Employing an n-gram similarity analysis between HumanEval questions and code exercises, which found negligible overlap <a class="yt-timestamp" data-t="01:25:07">[01:25:07]</a>.
*   Using a "data pruning" approach, where portions of the training data were intentionally removed to test performance stability <a class="yt-timestamp" data-t="01:24:20">[01:24:20]</a>. Even after pruning over 40% of the code exercises data set, Phi-1 still outperformed larger models like StarCoder <a class="yt-timestamp" data-t="01:24:26">[01:24:26]</a>.
*   Evaluating solutions using GPT-4 as a "grader," which offers a more nuanced assessment than simple pass/fail unit tests <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>. However, the speaker cautions that [[large_language_models_in_machine_learning_research | AI grading of AI]] might introduce new biases based on subtle linguistic patterns that humans don't perceive <a class="yt-timestamp" data-t="01:22:34">[01:22:34]</a>.

## Limitations and Future Directions <a class="yt-timestamp" data-t="01:32:35">[01:32:35]</a>

The study acknowledges limitations:
*   Phi-1 specializes in Python coding and may lack domain-specific knowledge for particular APIs <a class="yt-timestamp" data-t="01:32:37">[01:32:37]</a>.
*   The model is less robust to stylistic variations or errors in prompts due to the structured nature of its data set <a class="yt-timestamp" data-t="01:32:55">[01:32:55]</a>. Small models, unlike larger ones, might have more fragile "local minima" of compression, leading to less consistent behavior with prompt variations <a class="yt-timestamp" data-t="01:40:46">[01:40:46]</a>.

Despite these, the authors believe their approach can be extended to tackle these limitations <a class="yt-timestamp" data-t="01:33:01">[01:33:01]</a>. They suggest that using GPT-4 to generate synthetic data (instead of GPT-3.5) could lead to even more significant gains <a class="yt-timestamp" data-t="01:33:06">[01:33:06]</a>. The work provides strong evidence that developing methodologies for creating high-quality, diverse, and non-repetitive data sets is a central direction for [[advancements_in_language_models | advancing Natural Language Processing]] <a class="yt-timestamp" data-t="01:33:25">[01:33:25]</a>. The idea of "domain randomization" for text, similar to techniques used in computer vision, could be explored to increase diversity <a class="yt-timestamp" data-t="01:34:09">[01:34:09]</a>.

The speaker emphasizes that while more data is generally better, *quality* data is paramount <a class="yt-timestamp" data-t="01:37:04">[01:37:04]</a>. This suggests a future where [[training_and_finetuning_of_language_models_for_code | synthetic data]] and meticulously crafted "textbooks" become essential for fine-tuning LLMs, allowing for models with specific behaviors or aligned to the needs of particular countries or regions <a class="yt-timestamp" data-t="01:37:31">[01:37:31]</a>. The integration of interpreters and [[training_and_finetuning_of_language_models_for_code | reinforcement learning]] during training could also be a fruitful area for future research <a class="yt-timestamp" data-t="01:08:58">[01:08:58]</a>.