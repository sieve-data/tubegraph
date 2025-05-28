---
title: The role of data quality and training scale in AI models
videoId: _TghtP0ZyoM
---

From: [[hu-po]] <br/> 

The development of Llama 3.1 represents a significant [[implications_of_ai_model_scaling_and_convergence | paradigm shift]] in AI, primarily driven by advancements in data quality and training scale rather than substantial architectural changes <a class="yt-timestamp" data-t="04:06">[04:06]</a> <a class="yt-timestamp" data-t="06:30">[06:30]</a>.

## Core Philosophy: Data & Scale
Llama 3.1’s performance, which is on par with, and in some benchmarks, even surpasses GPT-4 <a class="yt-timestamp" data-t="02:19">[02:19]</a> <a class="yt-timestamp" data-t="02:25">[02:25]</a>, is largely attributed to meticulously curated and diverse datasets, along with extensive training <a class="yt-timestamp" data-t="00:31">[00:31]</a>. The model utilizes a standard dense Transformer model architecture, almost identical to Llama 2, with performance gains primarily stemming from improvements in data quality and diversity <a class="yt-timestamp" data-t="00:57">[00:57]</a> <a class="yt-timestamp" data-t="03:32">[03:32]</a>.

## Data Curation and Pre-processing
A critical aspect of Llama 3.1’s [[challenges_and_methodologies_in_ai_training | training processes]] involves careful pre-processing and data curation pipelines <a class="yt-timestamp" data-t="01:46">[01:46]</a>. This includes:
*   **Filtering**: Data is filtered based on various criteria, such as adult content (using "dirty word counting") <a class="yt-timestamp" data-t="02:53">[02:53]</a> <a class="yt-timestamp" data-t="03:17">[03:17]</a>.
*   **Outlier Token Filtering**: [[Technical aspects of AI model training and finetuning | KL Divergence]] is used to filter out documents containing an excessive number of outlier tokens, such as text heavily featuring emojis <a class="yt-timestamp" data-t="03:01">[03:01]</a>.
*   **Model-Based Quality Classifiers**: AI models themselves are used to filter the pre-training corpus for quality <a class="yt-timestamp" data-t="03:35">[03:35]</a>.
*   **Deduplication**: Multiple rounds of deduplication are performed at various levels, including using language models to compare paragraph embeddings for content similarity <a class="yt-timestamp" data-t="02:56">[02:56]</a>.
*   **Markdown Removal**: A surprising finding was that Markdown is harmful to model performance when primarily trained on web data, leading to its removal from the training corpus <a class="yt-timestamp" data-t="03:40">[03:40]</a>.

## Data Mix and Annealing
The proportion of different data sources in the pre-training data mix is carefully determined <a class="yt-timestamp" data-t="03:48">[03:48]</a>.
*   **Categorization**: A classifier categorizes text blobs into one of a hundred different categories <a class="yt-timestamp" data-t="03:53">[03:53]</a>.
*   **Downsampling**: Categories that appear too frequently, like arts and entertainment, are downsampled to maintain balance <a class="yt-timestamp" data-t="03:57">[03:57]</a>.
*   **Scaling Law Experiments**: Small models are trained on various data mixes to predict the performance of a large model on that mix, allowing for hyperparameter sweeping at lower model sizes <a class="yt-timestamp" data-t="03:40">[03:40]</a>.
*   **Data Composition**: Ultimately, the data mix comprised 50% general knowledge, 25% math, 17% code, and 8% multilingual data <a class="yt-timestamp" data-t="03:56">[03:56]</a>.
*   **Annealing**: The training process involves "annealing" the data mix, upsampling high-quality data in select domains <a class="yt-timestamp" data-t="04:13">[04:13]</a>. Notably, for the flagship 405B model, these specific in-domain training samples yielded negligible improvements, suggesting that larger models possess strong in-context learning and reasoning capabilities, simplifying the training process <a class="yt-timestamp" data-t="03:21">[03:21]</a>. This implies that as models scale, the need for "weird tricks" reduces, potentially easing the path to AGI <a class="yt-timestamp" data-t="03:58">[03:58]</a>.

## Training Scale
Llama 3.1 was trained on over 15 trillion tokens of data, representing a 10x increase compared to Llama 2 <a class="yt-timestamp" data-t="01:40">[01:40]</a> <a class="yt-timestamp" data-t="01:54">[01:54]</a>. The training involved 3.8 x 10^25 flops, a 50x increase in compute compared to Llama 2 <a class="yt-timestamp" data-t="01:51">[01:51]</a>.

### Training Stages and Parameters
The training recipe includes three stages: initial pre-training, long-context pre-training, and annealing <a class="yt-timestamp" data-t="01:21">[01:21]</a>. Parameters like batch size, context length, and the percentage of non-English data are changed gradually throughout the pre-training process <a class="yt-timestamp" data-t="01:29">[01:29]</a>. The context window increases in six stages from 8K to 128K tokens <a class="yt-timestamp" data-t="01:46">[01:46]</a>.

## Scaling Laws (Hypotheses)
The concept of "scaling laws" in AI models is viewed more as "scaling hypotheses" <a class="yt-timestamp" data-t="01:33">[01:33]</a> <a class="yt-timestamp" data-t="01:38">[01:38]</a>. While small models often show predictive trends for larger models' performance (e.g., on the ARC challenge) <a class="yt-timestamp" data-t="04:37">[04:37]</a>, these laws can be noisy and unreliable, suggesting they may not continue their trends indefinitely <a class="yt-timestamp" data-t="01:56">[01:56]</a>. The current S-curve of language model performance appears to be flattening out, indicating that new breakthroughs, potentially involving [[finetuning_and_training_curriculums_in_ai_models | linear attention models]] or multimodal architectures, are needed to achieve further substantial improvements <a class="yt-timestamp" data-t="04:51">[04:51]</a> <a class="yt-timestamp" data-t="05:25">[05:25]</a>.

## Synthetic Data Generation
[[synthetic data sets for training AI | Synthetic data generation]] plays a crucial role, especially for domains where outputs can be easily verified, such as code and math <a class="yt-timestamp" data-t="01:27">[01:27]</a> <a class="yt-timestamp" data-t="03:12">[03:12]</a> <a class="yt-timestamp" data-t="03:46">[03:46]</a>.
*   **Self-Improvement Flywheel**: An iterative self-improvement flywheel is employed, where the latest model checkpoint is used to generate more training data, creating a feedback loop <a class="yt-timestamp" data-t="02:51">[02:51]</a> <a class="yt-timestamp" data-t="03:49">[03:49]</a>. This process was also pioneered by Meta for models like the Segment Anything Model <a class="yt-timestamp" data-t="02:51">[02:51]</a>.
*   **Code Generation**: For code, the model generates synthetic examples (e.g., LeetCode problems), which are then verified using parsers, linters, and unit tests executed in a containerized environment <a class="yt-timestamp" data-t="03:25">[03:25]</a> <a class="yt-timestamp" data-t="03:28">[03:28]</a>. If a solution fails, the model is prompted to revise it <a class="yt-timestamp" data-t="03:38">[03:38]</a>.
*   **Language Translation**: To address performance gaps in less common programming languages, Python examples are translated into other languages like PHP to supplement training data <a class="yt-timestamp" data-t="03:15">[03:15]</a>.
*   **Model as Judge**: The model acts as its own reward model, assessing and assigning binary scores for code correctness and style <a class="yt-timestamp" data-t="03:39">[03:39]</a>.

## Human Feedback and Annotation Evolution
The complexity of human annotation for post-training has increased significantly <a class="yt-timestamp" data-t="02:22">[02:22]</a>. Annotators perform multi-turn dialogues, providing nuanced feedback by ranking responses (e.g., "way better," "better," "slightly better," "marginally better") and actively editing preferred responses <a class="yt-timestamp" data-t="02:23">[02:23]</a> <a class="yt-timestamp" data-t="03:30">[03:30]</a>. This requires high-level annotators for complex tasks <a class="yt-timestamp" data-t="02:55">[02:55]</a>. However, for long context models, human annotation becomes impractical due to tedious and time-consuming reading, leading to a predominant reliance on [[synthetic data sets for training AI]] <a class="yt-timestamp" data-t="04:33">[04:33]</a>.

## Multimodal Experiments
While Llama 3.1 is primarily a language model, Meta conducted experiments to integrate image, video, and speech capabilities <a class="yt-timestamp" data-t="01:24">[01:24]</a>. This was achieved through a compositional approach, using separate pre-trained encoders (e.g., Clip for images <a class="yt-timestamp" data-t="02:11">[02:11]</a> <a class="yt-timestamp" data-t="02:59">[02:59]</a>, Conformer for speech <a class="yt-timestamp" data-t="02:22">[02:22]</a>) and adapters to connect their outputs to the language model <a class="yt-timestamp" data-t="01:53">[01:53]</a>. Text extraction from images using proprietary OCR was also used to augment labels <a class="yt-timestamp" data-t="02:10">[02:10]</a>. This approach is more aligned with traditional Vision Language Models (VLMs) rather than the deeper integration seen in models like Chameleon <a class="yt-timestamp" data-t="02:19">[02:19]</a>.