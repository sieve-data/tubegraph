---
title: Synthetic data generation in AI training
videoId: _TghtP0ZyoM
---

From: [[hu-po]] <br/> 

The development of advanced AI models like Llama 3 relies heavily on sophisticated data management techniques, particularly [[Data Generation for AI Models | synthetic data generation]] <a class="yt-timestamp" data-t="01:22:11">[01:22:11]</a>. This approach allows for the creation of vast and high-quality training datasets, often at a lower cost and higher scale than purely human-annotated data <a class="yt-timestamp" data-t="01:31:46">[01:31:46]</a>.

## Key Aspects of Synthetic Data Generation

### Iterative Self-Improvement
Meta has been a pioneer in using [[Data Generation for AI Models | synthetic data]], notably with their Segment Anything model <a class="yt-timestamp" data-t="01:22:45">[01:22:45]</a>. The process involves an iterative approach where the latest checkpoint of a model is used to generate more data. For instance, in language models, this means using the model to create [[synthetic data sets for training AI | synthetic preference data]] or to label more images in vision tasks <a class="yt-timestamp" data-t="01:23:09">[01:23:09]</a>. This creates a "self-improvement flywheel" where the model generates higher quality [[synthetic data sets for training AI | synthetic data]] for subsequent training rounds, paving the way for superhuman performance in specific domains <a class="yt-timestamp" data-t="01:33:41">[01:33:41]</a>.

### Data Filtering and Quality Control
A significant portion of training data for Llama 3 is model-generated <a class="yt-timestamp" data-t="01:24:40">[01:24:40]</a>. To ensure quality, rigorous data cleaning and quality control are essential <a class="yt-timestamp" data-t="01:24:40">[01:24:40]</a>.
Techniques used include:
*   **Filtering based on Reward Model Scores** Data that falls into the top quartile of reward model scores is selected <a class="yt-timestamp" data-t="01:26:02">[01:26:02]</a>.
*   **Self-Filtering** The Llama 3 checkpoint can be prompted to filter its own data <a class="yt-timestamp" data-t="01:26:11">[01:26:11]</a>.
*   **Deduplication** Clustering complete dialogues and keeping only those with a maximum cosine similarity less than a certain threshold to avoid redundant examples <a class="yt-timestamp" data-t="01:26:20">[01:26:20]</a>.
*   **Content-Specific Filtering** Filtering out data containing overused phrases, such as "I'm sorry" or "I apologize," to prevent undesirable model behaviors <a class="yt-timestamp" data-t="01:25:21">[01:25:21]</a>.

### Verification and Domain Specificity
[[Data Generation for AI Models | Synthetic data]] is particularly effective in domains where the output can be objectively verified <a class="yt-timestamp" data-t="01:30:12">[01:30:12]</a>. For example, AlphaGo achieved superhuman performance in Go by generating [[synthetic data sets for training AI | synthetic data sets]] of master-level gameplay, as the outcome (win/loss) is clearly verifiable <a class="yt-timestamp" data-t="01:30:23">[01:30:23]</a>.

*   **Code Generation**: [[synthetic data in feature detection | Synthetic data]] for code generation is highly effective because code output can be verified through execution. The Llama 3 code expert model generates large quantities of [[synthetic data sets for training AI | synthetic supervised fine-tuning dialogues]], essentially creating fake "LeetCode" problems and their solutions <a class="yt-timestamp" data-t="01:31:53">[01:31:53]</a>.
    *   **Execution Feedback**: This acts as a "code of truth," allowing the model to learn from its mistakes <a class="yt-timestamp" data-t="01:32:53">[01:32:53]</a>.
    *   **Quality Improvement**: Adding general rules of good programming to the prompt improves the quality of generated solutions <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>.
    *   **Automated Testing**: Generated code is run through a parser and linter, unit tests are generated and executed in a containerized environment (e.g., Docker), and if a solution fails, the model is prompted to revise it <a class="yt-timestamp" data-t="01:33:25">[01:33:25]</a>.
    *   **Language Translation**: To supplement data for less common programming languages, Python examples are translated into languages like PHP, further expanding the dataset <a class="yt-timestamp" data-t="01:34:15">[01:34:15]</a>. Over 1.2 million synthetic code examples were generated using these methods <a class="yt-timestamp" data-t="01:34:21">[01:34:21]</a>. The model also acts as its own judge, assessing code correctness and style <a class="yt-timestamp" data-t="01:34:31">[01:34:31]</a>.

*   **Math Reasoning**: Similar to code, math problems allow for heuristic verification of solutions, making [[Data Generation for AI Models | synthetic data]] highly valuable. This is a primary reason why superhuman performance in math and code is emerging first among AI models <a class="yt-timestamp" data-t="01:31:37">[01:31:37]</a>. While human annotation for complex "Chain of Thought" reasoning is impractical, [[Data Generation for AI Models | synthetic data]] fills this gap <a class="yt-timestamp" data-t="01:43:32">[01:43:32]</a>.

### Role in Post-Training
[[Data Generation for AI Models | Synthetic data]] plays a crucial role in the post-training phase, which includes instruction tuning and Reinforcement Learning from Human Feedback (RLHF).
*   **Preference Data Generation**: [[Data Generation for AI Models | Synthetic data]] is used to generate more preference data for training reward models <a class="yt-timestamp" data-t="01:22:35">[01:22:35]</a>.
*   **Data Augmentation**: Existing academic datasets are converted into question-answer pairs using templates or through LLM rewriting. This process augments the data, similar to how images are flipped or corrupted in image space <a class="yt-timestamp" data-t="02:14:14">[02:14:14]</a>.
*   **Multimodal Data**: Text-only LLMs can generate question-answer pairs in the text domain, which are then combined with corresponding images to produce [[synthetic data sets for training AI | synthetic multimodal data]] <a class="yt-timestamp" data-t="02:14:53">[02:14:53]</a>.
*   **Quality Tuning (QT)**: A small, highly selective dataset of human-rewritten and verified samples is used to train DPO (Direct Preference Optimization) models. This "quality tuning" significantly improves human evaluations without affecting generalization <a class="yt-timestamp" data-t="02:17:11">[02:17:11]</a>. The entire training pipeline, including pre-training mix adjustments and multiple rounds of sft and DPO with varying quality levels, is increasingly complicated, but financially feasible for well-resourced organizations like Meta <a class="yt-timestamp" data-t="02:17:34">[02:17:34]</a>.