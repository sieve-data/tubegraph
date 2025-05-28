---
title: Llama 31 performance and comparison to GPT 4
videoId: _TghtP0ZyoM
---

From: [[hu-po]] <br/> 

Llama 3.1, the latest iteration of Meta's Llama 3 models, represents a significant development in the field of large language models, particularly in the open-source domain <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>, <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. The paper detailing Llama 3.1 is 90 pages long, providing extensive information on its development and capabilities <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>, <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

## Overall Performance and Comparison to GPT-4

Llama 3.1 is positioned as being on par with [[gpt4_ensemble_model_structure | GPT-4]] across many benchmarks <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>. The 405B parameter version of Llama 3.1 either beats or is within one percentage point of [[gpt4_ensemble_model_structure | GPT-4]] on most benchmarks <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

In human evaluations, Llama 3.1's win rate against [[gpt4_ensemble_model_structure | GPT-4]] is within the margin of error on nearly all capabilities <a class="yt-timestamp" data-t="01:57:01">[01:57:01]</a>.

Specific performance highlights include:
*   **Tool Use**: Llama 3.1 outperforms [[gpt4_ensemble_model_structure | GPT-4]] by 10 percentage points in tool use benchmarks <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **Multi-turn Reasoning and Coding**: Llama 3.1 also outperforms [[gpt4_ensemble_model_structure | GPT-4]] in these areas <a class="yt-timestamp" data-t="01:57:10">[01:57:10]</a>.
*   **Multilingual Prompts**: However, Llama 3.1 underperforms [[gpt4_ensemble_model_structure | GPT-4]] on multilingual prompts <a class="yt-timestamp" data-t="01:57:15">[01:57:15]</a>.

### Benchmark Limitations
The presented benchmarks for Llama 3.1, as well as other models, come with caveats:
*   Benchmarks are often "cheesed," meaning they use techniques like few-shot learning and Chain of Thought prompting, which can inflate scores <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>, <a class="yt-timestamp" data-t="01:50:08">[01:50:08]</a>.
*   **Label Variance**: The model's accuracy significantly drops when alternative, less common tokens are used for answer choices (e.g., "OE" instead of "A"), indicating fragility and a lack of true reasoning <a class="yt-timestamp" data-t="01:50:35">[01:50:35]</a>, <a class="yt-timestamp" data-t="01:52:23">[01:52:23]</a>.
*   **Contamination**: Many benchmarks exist within the pre-training corpus, meaning models are essentially memorizing the answers rather than reasoning, which further diminishes their trustworthiness <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a>, <a class="yt-timestamp" data-t="01:54:04">[01:54:04]</a>.

## Architecture and Training

Llama 3.1's performance gains are primarily attributed to improvements in data quality and diversity, rather than significant changes to the model architecture <a class="yt-timestamp" data-t="01:38:34">[01:38:34]</a>. It uses a standard dense Transformer model architecture, almost identical to Llama 2, with only minor algorithmic differences <a class="yt-timestamp" data-t="01:16:07">[01:16:07]</a>, <a class="yt-timestamp" data-t="01:16:14">[01:16:14]</a>.

### Data
*   **Scale**: Llama 3.1 was trained on over 15 trillion tokens of training data, which is 10 times the amount used for Llama 2 <a class="yt-timestamp" data-t="01:16:40">[01:16:40]</a>, <a class="yt-timestamp" data-t="01:17:06">[01:17:06]</a>.
*   **Data Curation**: The training process involved careful pre-processing and data curation pipelines <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This includes:
    *   Deduplication at various levels <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>.
    *   Filtering out adult content and documents with excessive outlier tokens <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>, <a class="yt-timestamp" data-t="00:32:03">[00:32:03]</a>.
    *   Removal of markdown markers, as markdown was found to be harmful to performance when training on web data <a class="yt-timestamp" data-t="00:30:42">[00:30:42]</a>, <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>.
*   **Data Mix**: The data mix was determined using scaling law experiments on smaller models <a class="yt-timestamp" data-t="00:34:40">[00:34:40]</a>. The final mix consists of:
    *   50% general knowledge <a class="yt-timestamp" data-t="00:35:59">[00:35:59]</a>
    *   25% math <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>
    *   17% code <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>
    *   8% multilingual data <a class="yt-timestamp" data-t="00:36:02">[00:36:02]</a>

### Training Process
The training involved a complex, dynamic curriculum:
*   **Initial Pre-training**: Standard cosine learning rate schedule, starting with a lower batch size and context size <a class="yt-timestamp" data-t="01:17:27">[01:17:27]</a>, <a class="yt-timestamp" data-t="01:17:31">[01:17:31]</a>.
*   **Long Context Pre-training**: The context window was gradually increased in six stages, from 8K tokens up to 128K tokens <a class="yt-timestamp" data-t="01:18:47">[01:18:47]</a>, <a class="yt-timestamp" data-t="01:18:51">[01:18:51]</a>.
*   **Annealing**: The percentage of non-English data was also increased over time <a class="yt-timestamp" data-t="01:17:48">[01:17:48]</a>.
*   **Tokenization**: Llama 3.1 uses a tokenizer similar to Tiktoken, with a vocabulary size of 128,000 tokens, achieving a compression factor of approximately 3.94 characters per token <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>, <a class="yt-timestamp" data-t="00:41:24">[00:41:24]</a>.

### Post-Training and Expert Models
Post-training, referred to as "post-training" or "instruction tuning," heavily utilizes a reward model and [[llamaadapter_and_its_role_in_adapting_language_models | Direct Preference Optimization (DPO)]] <a class="yt-timestamp" data-t="01:19:09">[01:19:09]</a>, <a class="yt-timestamp" data-t="01:19:52">[01:19:52]</a>.
*   **Synthetic Data Generation**: A significant portion of the training data is model-generated, particularly for areas like coding and math, where correctness can be heuristically verified <a class="yt-timestamp" data-t="01:24:40">[01:24:40]</a>, <a class="yt-timestamp" data-t="01:31:06">[01:31:06]</a>. This includes [[introduction_to_code_llama_by_meta_ai | using Llama 3]]'s code expert to generate large quantities of synthetic supervised fine-tuning dialogues <a class="yt-timestamp" data-t="01:31:53">[01:31:53]</a>.
*   **Human Annotation**: Human annotators provide preference data, often through multi-turn dialogues, editing preferred responses and rating them (e.g., "way better," "slightly better") <a class="yt-timestamp" data-t="01:21:20">[01:21:20]</a>, <a class="yt-timestamp" data-t="01:23:30">[01:23:30]</a>.
*   **Expert Models**: Separate "expert" models are trained by branching off the main pre-training run and continuing training on domain-specific data:
    *   **Code Expert**: Trained on a 1 trillion token mix of mostly code data, with Python being a high-priority language <a class="yt-timestamp" data-t="01:28:12">[01:28:12]</a>, <a class="yt-timestamp" data-t="01:28:20">[01:28:20]</a>. This includes execution feedback for auto-correction <a class="yt-timestamp" data-t="01:32:53">[01:32:53]</a>.
    *   **Multilingual Expert**: Trained on a data mix consisting of 90% multilingual tokens <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. Supported languages include English, Spanish, Hindi, Portuguese, Thai, and Vietnamese <a class="yt-timestamp" data-t="01:34:51">[01:34:51]</a>.

### Tool Usage
Llama 3.1 integrates external tools like search engines and code interpreters to expand its task-solving capabilities <a class="yt-timestamp" data-t="01:37:30">[01:37:30]</a>. This allows it to separate "knowledge" from "reasoning" <a class="yt-timestamp" data-t="01:38:17">[01:38:17]</a>. Tools supported include Brave Search, a Python interpreter, and the Wolfram Alpha API <a class="yt-timestamp" data-t="01:38:41">[01:38:41]</a>, <a class="yt-timestamp" data-t="01:38:52">[01:38:52]</a>, <a class="yt-timestamp" data-t="01:39:02">[01:39:02]</a>. Tool definitions and calls are converted to a JSON format, similar to other model APIs <a class="yt-timestamp" data-t="01:47:16">[01:47:16]</a>.

## Inference Efficiency

Llama 3.1 employs techniques like pipeline parallelism and [[performance_and_implications_of_quantized_language_models | FP8 quantization]] to enhance inference efficiency <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

*   **Pipeline Parallelism**: The model is partitioned vertically across different GPUs, with different devices processing different stages of the model <a class="yt-timestamp" data-t="01:59:02">[01:59:02]</a>, <a class="yt-timestamp" data-t="02:00:51">[02:00:51]</a>.
*   **[[performance_and_implications_of_quantized_language_models | FP8 Quantization]]**: Llama 3.1 leverages the native [[performance_and_implications_of_quantized_language_models | FP8 support]] of H100 GPUs for low-precision inference <a class="yt-timestamp" data-t="02:02:23">[02:02:23]</a>.
    *   While the 405B model in BF16 (Brain Float 16) precision doesn't fit on a single server node (requiring two nodes or 16 GPUs), [[performance_and_implications_of_quantized_language_models | FP8 quantization]] allows it to fit on a single node (8 GPUs) <a class="yt-timestamp" data-t="01:59:25">[01:59:25]</a>, <a class="yt-timestamp" data-t="02:06:57">[02:06:57]</a>.
    *   This significantly improves throughput due to faster communication within a single node compared to across multiple nodes <a class="yt-timestamp" data-t="02:07:02">[02:07:02]</a>, <a class="yt-timestamp" data-t="02:07:11">[02:07:11]</a>.
    *   Most parameters and activations in the Feed Forward Network (FFN) layers are quantized, while self-attention layers are not <a class="yt-timestamp" data-t="02:02:58">[02:02:58]</a>. The first and last Transformer layers also do not undergo quantization <a class="yt-timestamp" data-t="02:03:16">[02:03:16]</a>.

## Multimodal Experiments

While Llama 3.1 is primarily a language model, Meta also conducted experiments on integrating multimodal capabilities, although these seem to be in active development and not part of the main release <a class="yt-timestamp" data-t="01:37:34">[01:37:34]</a>, <a class="yt-timestamp" data-t="02:25:05">[02:25:05]</a>.

*   **Compositional Approach**: Separate encoders are used for image and speech modalities, which are then connected to the language model via adapters <a class="yt-timestamp" data-t="02:08:45">[02:08:45]</a>, <a class="yt-timestamp" data-t="02:09:10">[02:09:10]</a>.
*   **Image Encoder**: A Vision Transformer (ViT) acts as the image encoder, using CLIP for image-text pairs <a class="yt-timestamp" data-t="02:09:02">[02:09:02]</a>, <a class="yt-timestamp" data-t="02:11:07">[02:11:07]</a>. OCR is used to extract text from images to augment captions <a class="yt-timestamp" data-t="02:10:34">[02:10:34]</a>.
*   **Speech Encoder**: A Conformer model is used as the speech encoder <a class="yt-timestamp" data-t="02:19:22">[02:19:22]</a>.
*   **Training Details**: Gradient accumulation for multimodal training is performed in FP32 due to numerical instabilities encountered with lower precision <a class="yt-timestamp" data-t="02:13:50">[02:13:50]</a>, <a class="yt-timestamp" data-t="02:13:56">[02:13:56]</a>.
*   **Data Augmentation**: Existing academic datasets are converted into question-answer pairs using templates or LLM rewriting. Text-based LLMs generate question-answer pairs, then text representations are replaced with corresponding images to create synthetic multimodal data <a class="yt-timestamp" data-t="02:14:14">[02:14:14]</a>, <a class="yt-timestamp" data-t="02:15:00">[02:15:00]</a>.

## Conclusion

The development of high-quality foundation models like Llama 3.1 is still in its early stages <a class="yt-timestamp" data-t="02:21:30">[02:21:30]</a>. The success of Llama 3.1 underscores the importance of high-quality data scale and simplicity in architecture <a class="yt-timestamp" data-t="02:22:56">[02:22:56]</a>, <a class="yt-timestamp" data-t="02:23:00">[02:23:00]</a>. Future improvements might stem from breakthroughs in multimodal architectures, advanced energy solutions for data centers, or other unexpected areas, rather than just scaling up existing Transformer designs <a class="yt-timestamp" data-t="02:21:52">[02:21:52]</a>, <a class="yt-timestamp" data-t="02:28:17">[02:28:17]</a>, <a class="yt-timestamp" data-t="02:29:16">[02:29:16]</a>.