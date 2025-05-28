---
title: Challenges and future directions in vision language modeling
videoId: 446QYqELoIs
---

From: [[hu-po]] <br/> 

[[Vision language models and their advancements | Vision language models]] (VLMs) are a rapidly evolving field, integrating visual and textual information to enable advanced AI capabilities. However, several challenges and open questions remain regarding their development, training, and application.

## Terminology Confusion
A notable challenge in the field is the lack of standardized terminology. Different research groups and companies use various acronyms to describe similar models, including:
*   Multimodal Large Language Models (MLLMs) <a class="yt-timestamp" data-t="00:3:18">[00:03:18]</a>, <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>
*   Large Multimodal Models (LMMs) <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>
*   [[Vision language models and their advancements | Vision Language Models]] (VLMs) <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>
*   Large Scale [[Vision language models and their advancements | Vision Language Models]] (LVLMs) <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>, <a class="yt-timestamp" data-t="01:45:05">[01:45:05]</a>

This inconsistency can lead to confusion and hinder clear communication within the research community <a class="yt-timestamp" data-t="01:55:07">[01:55:07]</a>.

## Data Challenges
### Data Quality and Cleaning
The increasing scale of datasets, often scraped from the internet or synthetically generated, presents significant data quality challenges. Unlike smaller datasets that could be manually cleaned, these massive datasets are often noisy and imperfect, making it difficult to ensure accuracy and consistency <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>, <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>. The amount of noise in datasets is expected to worsen as reliance on synthetic data grows <a class="yt-timestamp" data-t="00:24:16">[00:24:16]</a>.

### Lack of Specialized Datasets
There is a shortage of high-quality, specialized datasets for specific VLM applications, such as:
*   Multi-round, multi-image interleaved dialogues <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>.
*   [[Advancements in language models | Instruction tuning]] for visual assistants <a class="yt-timestamp" data-t="01:33:02">[01:33:02]</a>.

Researchers often resort to creating synthetic datasets or employing data blending techniques to overcome these limitations <a class="yt-timestamp" data-t="00:44:45">[00:44:45]</a>, but this can introduce further noise and lead to "deteriorated performances characterized by incomplete sentences and incorrect references" <a class="yt-timestamp" data-t="01:36:21">[01:36:21]</a>.

## Model Architecture and Training
### Optimizing Vision Encoder Choice
Research indicates that [[Vision language models and encoders | vision encoders]] pre-trained with a contrastive objective (e.g., SigLIP or CLIP) generally perform better in visual question answering (VQA) tasks than those pre-trained with a classification objective (e.g., ImageNet classifiers) <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>, even if they underperform on standard image classification benchmarks <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.

### Balancing Model Scale
There's an ongoing debate about the optimal balance between the size of the [[Vision language models and encoders | vision encoder]] and the [[Advancements in language models | language model]] within a VLM. Some models pair a large [[Advancements in language models | language model]] (e.g., 70B parameters) with a relatively small [[Vision language models and encoders | vision encoder]] (e.g., 2B parameters), which might be an "overkill" and lead to suboptimal results <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>, <a class="yt-timestamp" data-t="00:51:50">[00:51:50]</a>. It is speculated that increasing the size and quality of the [[Vision language models and encoders | visual encoder]] could lead to significant performance gains, similar to how larger text encoders improved stable diffusion models <a class="yt-timestamp" data-t="00:46:04">[00:46:04]</a>.

### Effectiveness of Complex Architectures
*   **Multiple Vision Encoders**: While combining multiple [[Vision language models and encoders | vision encoders]] (e.g., CLIP and DINOv2) and utilizing intermediate features from different layers can lead to slight improvements <a class="yt-timestamp" data-t="01:51:11">[01:51:11]</a>, the gain might not justify the increased complexity and inference cost <a class="yt-timestamp" data-t="01:26:59">[01:26:59]</a>.
*   **Complex Connectors**: Using a sophisticated connector like a cross-attention module between the [[Vision language models and encoders | vision encoder]] and the [[Advancements in language models | language model]], instead of a simpler Multi-Layer Perceptron (MLP), does not always yield significant benefits <a class="yt-timestamp" data-t="00:53:10">[00:53:10]</a>, <a class="yt-timestamp" data-t="01:31:54">[01:31:54]</a>.
*   **Training Recipes**: More complicated multi-stage training recipes involving freezing and unfreezing different model parts (similar to [[challenges_and_improvements_in_vision_language_models | locked image tuning]]) may not always lead to substantial gains compared to simpler approaches <a class="yt-timestamp" data-t="01:54:16">[01:54:16]</a>.

### Overfitting and Checkpoints
Historically, stopping training to avoid overfitting was crucial <a class="yt-timestamp" data-t="01:01:57">[01:01:57]</a>. However, with larger datasets and better data augmentations, overfitting is becoming less of a concern. In some cases, the "final checkpoint, even if it appears overfitted, often delivers better testing results" <a class="yt-timestamp" data-t="01:00:17">[01:00:17]</a>. Instead of stopping at an optimal overfitting point, training often ceases when the computational budget runs out <a class="yt-timestamp" data-t="01:02:27">[01:02:27]</a>.

## Evaluation and Benchmarking
The concept of "state-of-the-art" (SOTA) is often diluted as research groups claim SOTA on obscure or niche benchmarks, making it difficult to truly compare model performance <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>, <a class="yt-timestamp" data-t="00:37:39">[00:37:39]</a>. This highlights a need for more robust and widely accepted evaluation standards. For example, ImageNet classification performance is not a reliable indicator of a [[Vision language models and encoders | vision encoder]]'s quality for VQA tasks <a class="yt-timestamp" data-t="01:39:17">[01:39:17]</a>.

Furthermore, there is a lack of good benchmarks for evaluating VLMs as part of practical systems or autonomous agents, which are often required to interact with external APIs or perform complex, multi-step tasks <a class="yt-timestamp" data-t="01:46:51">[01:46:51]</a>.

## Future Directions
Future research needs to address:
*   **Beyond Text Output**: Current VLMs primarily output text. The next step involves models that can directly output images and text, moving beyond relying on external tools or APIs like Diffusion Models <a class="yt-timestamp" data-t="01:19:16">[01:19:16]</a>. This would likely require training [[Advancements in language models | language models]] to output "vision tokens" directly <a class="yt-timestamp" data-t="01:21:16">[01:21:16]</a>.
*   **Optimizing Glue Layers**: A full experiment is needed to determine the best "glue" layer or adapter type to connect [[Vision language models and encoders | vision encoders]] and [[Advancements in language models | language models]] <a class="yt-timestamp" data-t="01:32:22">[01:32:22]</a>.
*   **Standardized Terminology**: The community needs to converge on a single, clear acronym for [[Multimodal large language models vs vision language models | Vision Language Models]] to improve communication and understanding <a class="yt-timestamp" data-t="01:56:22">[01:56:22]</a>.
*   **Scaling and Emergent Behavior**: Continued exploration of scaling both the [[Vision language models and encoders | vision encoder]] and the [[Advancements in language models | language model]] simultaneously, as current observations suggest scaling laws lead to "emergent behavior" and improved performance <a class="yt-timestamp" data-t="01:30:59">[01:30:59]</a>.