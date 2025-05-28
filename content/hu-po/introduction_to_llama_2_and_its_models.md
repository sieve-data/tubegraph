---
title: Introduction to Llama 2 and its models
videoId: 1ZwXkw9_Xq8
---

From: [[hu-po]] <br/> 

Llama 2 is Meta's [[use_of_large_language_models_llms_in_robotics | Large Language Model (LLM)]] (similar to ChatGPT, Claude, or Bard) that was released as an open foundation and fine-tuned chat model <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. It is notably the first openly competitive [[use_of_large_language_models_llms_in_robotics | LLM]] <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Unlike its predecessor, Llama 1, which was leaked, Llama 2 is officially available for public use <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Accessing Llama 2
Llama 2 models can be downloaded from Meta's website by filling out a form <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. Users can then run a `download.sh` script to obtain different versions <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### Model Variants
Llama 2 is released in various sizes, including 7 billion (7B), 13 billion (13B), and 70 billion (70B) parameters <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. There was an unreleased 34B model which showed higher safety violations in evaluations, possibly due to different training <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>, <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

The models come in two main types:
*   **Normal models (pre-trained)**: These are the base [[pretraining_and_data_set_details_of_llama_2 | Llama 2]] models, which Meta suspects are somewhat filtered for safety <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Chat models (fine-tuned)**: Optimized for dialogue use cases and are explicitly filtered <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>, <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

## Model Architecture and Training
[[pretraining_and_data_set_details_of_llama_2 | Llama 2]] uses an optimized auto-regressive Transformer architecture <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. Key architectural differences from Llama 1 include:
*   **Increased context length**: Doubled from 2,048 tokens to 4,096 tokens <a class="yt-timestamp" data-t="00:18:20">[00:18:20]</a>, <a class="yt-timestamp" data-t="00:29:16">[00:29:16]</a>. This is useful for longer conversations and documents <a class="yt-timestamp" data-t="00:30:13">[00:30:13]</a>.
*   **Grouped Query Attention (GQA)**: A modification to the attention mechanism that saves memory by sharing key and value projections across multiple attention heads, making inference more efficient, especially with larger context windows and batch sizes <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>, <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>, <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>. Llama 2 opted for GQA over Multi-Query Attention (MQA) or Multi-Head Attention (MHA) due to its comparable performance and better inference speed <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>, <a class="yt-timestamp" data-t="00:39:36">[00:39:36]</a>.
*   **Pre-normalization**: Using RMS Norm before the Transformer block <a class="yt-timestamp" data-t="00:26:25">[00:26:25]</a>.
*   **SwiGLU activation function**: A variant of the GLU activation <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>.
*   **Rotary Positional Embeddings (RoPE)** <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>.

### Pre-training Data and Process
[[pretraining_and_data_set_details_of_llama_2 | Llama 2]] was pre-trained on 2 trillion tokens of a "new mix of publicly available data" <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>, <a class="yt-timestamp" data-t="00:23:53">[00:23:53]</a>. Notably, this data *does not* include any data from Meta's products or services (e.g., Instagram, Facebook Chat) <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. The data underwent robust cleaning and filtering to remove personal information and increase knowledge while dampening hallucinations <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>, <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. Factual resources, likely textbooks, were up-sampled in the data mix <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>.

Llama 2 models were trained using the AdamW optimizer with a cosine learning rate schedule, warm-up steps, weight decay (0.1), and gradient clipping (1.0) <a class="yt-timestamp" data-t="00:42:51">[00:42:51]</a>. The training loss curves suggest that the models could have been trained for even longer without saturation, indicating further potential for improvement <a class="yt-timestamp" data-t="00:47:32">[00:47:32]</a>.

The tokenizer used is the same as Llama 1, employing a byte pair encoding algorithm (SentencePiece tokenizer from 2018) <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>. Numbers are split into individual digits, and unknown UTF-8 characters are decomposed into bytes. The total vocabulary size is 32,000 tokens <a class="yt-timestamp" data-t="00:51:32">[00:51:32]</a>, <a class="yt-timestamp" data-t="00:52:17">[00:52:17]</a>.

### Training Hardware and Carbon Footprint
Models were pre-trained on Meta's Research SuperCluster (RSC) and internal production clusters, both using Nvidia A100 GPUs <a class="yt-timestamp" data-t="00:52:28">[00:52:28]</a>.
*   **RSC**: Uses Nvidia Quantum InfiniBand interconnects and runs A100s at 400 watts per GPU <a class="yt-timestamp" data-t="00:52:41">[00:52:41]</a>.
*   **Production Cluster**: Equipped with RoCE (RDMA over Converged Ethernet) based on commodity Ethernet switches and runs A100s at 350 watts per GPU <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>.
Both interconnect solutions offer 200 gigabytes per second <a class="yt-timestamp" data-t="00:53:25">[00:53:25]</a>. RoCE was found to scale almost as well as InfiniBand up to 2,000 GPUs, making pre-training more "democratizable" <a class="yt-timestamp" data-t="00:55:24">[00:55:24]</a>.

## Fine-Tuning for Dialogue
[[pretraining_and_data_set_details_of_llama_2 | Llama 2]] chat models undergo several months of iterative alignment using:
*   **Supervised Fine-Tuning (SFT)**: Llama 2 started with publicly available instruction tuning data but focused on collecting a limited set of high-quality, human-annotated SFT data (around 27,540 annotations) to reach high quality <a class="yt-timestamp" data-t="01:05:22">[01:05:22]</a>, <a class="yt-timestamp" data-t="01:06:31">[01:06:31]</a>.
*   **Reinforcement Learning with Human Feedback (RLHF)**: This process trains the model to align with human preferences <a class="yt-timestamp" data-t="01:10:36">[01:10:36]</a>. Human annotators compare two model outputs and select their preference, which is used to train a "reward model" <a class="yt-timestamp" data-t="01:10:53">[01:10:53]</a>. The RLHF uses the Proximal Policy Optimization (PPO) algorithm <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
    *   **Reward Models (Helpfulness and Safety)**: Two separate reward models are trained: one for helpfulness and one for safety <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>, <a class="yt-timestamp" data-t="01:17:35">[01:17:35]</a>. This addresses the potential trade-off between being helpful and being safe <a class="yt-timestamp" data-t="01:27:52">[01:27:52]</a>. The reward models are trained for only one epoch to prevent overfitting <a class="yt-timestamp" data-t="01:23:06">[01:23:06]</a>, <a class="yt-timestamp" data-t="01:24:20">[01:24:20]</a>. Meta collected a large dataset of over 1.5 million human comparisons for reward modeling <a class="yt-timestamp" data-t="01:15:52">[01:15:52]</a>. Iterative fine-tuning (RLHF V1-V5) uses successive versions of the model to generate more data for the reward models <a class="yt-timestamp" data-t="01:29:11">[01:29:11]</a>.
*   **Ghost Attention (GAt)**: A technique to improve multi-turn consistency where initial instructions (system prompts) are synthetically concatenated to all user messages throughout the conversation during training <a class="yt-timestamp" data-t="01:43:10">[01:43:10]</a>, <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>. This ensures the model "remembers" its role or constraints across multiple turns <a class="yt-timestamp" data-t="01:43:17">[01:43:17]</a>, <a class="yt-timestamp" data-t="01:49:35">[01:49:35]</a>.

## Performance and Evaluation

### Benchmarks and Comparisons
[[pretraining_and_data_set_details_of_llama_2 | Llama 2]] chat models generally outperform other open-source chat models like Falcon 40B, MPT 7B, and Vicuna (a fine-tuned Llama 1 model) on most benchmarks <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>, <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>, <a class="yt-timestamp" data-t="02:43:24">[02:43:24]</a>.

Compared to closed-source models:
*   [[comparison_between_llama_31_and_gpt_4 | Llama 2]] is approximately on par with GPT-3.5 and Google's PaLM Bison model in human evaluations for helpfulness and safety <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>, <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   It still lags behind [[comparison_between_llama_31_and_gpt_4 | GPT-4]] on certain academic benchmarks, such as MMLU (Massive Multitask Language Understanding) and GSM8K (grade school math word problems) <a class="yt-timestamp" data-t="01:00:19">[01:00:19]</a>, <a class="yt-timestamp" data-t="01:01:16">[01:01:16]</a>.

### Evaluation Methods
*   **Human Evaluation**: Considered the "gold standard" for evaluating [[use_of_large_language_models_llms_in_robotics | LLMs]] <a class="yt-timestamp" data-t="01:21:18">[01:21:18]</a>, <a class="yt-timestamp" data-t="01:51:21">[01:51:21]</a>. Human annotators compare model generations on various prompts, rating for helpfulness and safety <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. Meta used 350 internal employees, contract workers, and external vendors for evaluations <a class="yt-timestamp" data-t="02:12:30">[02:12:30]</a>.
*   **AI-based Evaluation (GPT-4 as Judge)**: [[comparison_between_llama_31_and_gpt_4 | GPT-4]] was also used to evaluate [[pretraining_and_data_set_details_of_llama_2 | Llama 2]]'s performance against other models on helpfulness and safety <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>. However, the reliability of [[comparison_between_llama_31_and_gpt_4 | GPT-4]] as a judge is questioned due to potential unknown biases (e.g., preference for word length, sentence structure) <a class="yt-timestamp" data-t="01:12:07">[01:12:07]</a>, <a class="yt-timestamp" data-t="01:13:19">[01:13:19]</a>.

### Inter-rater Reliability (IRR)
Human evaluations showed an IRR between 0.37 and 0.5, suggesting a moderate level of agreement among annotators <a class="yt-timestamp" data-t="01:57:31">[01:57:31]</a>.

### Safety and Helpfulness Trade-off
[[pretraining_and_data_set_details_of_llama_2 | Llama 2]] addresses the tension between being maximally helpful and refusing unsafe prompts <a class="yt-timestamp" data-t="01:27:52">[01:27:52]</a>. The use of separate reward models for helpfulness and safety aims to improve both metrics simultaneously <a class="yt-timestamp" data-t="02:07:29">[02:07:29]</a>. However, highly safe models might become more conservative, leading to "false refusals" (incorrectly refusing legitimate prompts) <a class="yt-timestamp" data-t="02:09:16">[02:09:16]</a>, such as refusing a "Christmas crack" recipe due to the word "crack" <a class="yt-timestamp" data-t="02:09:37">[02:09:37]</a>.

## Limitations and Ethical Considerations

### Data Biases and Toxicity
The models reflect biases present in their pre-training data, which in turn reflect real-world biases (e.g., pronoun bias related to professions) <a class="yt-timestamp" data-t="01:58:28">[01:58:28]</a>, <a class="yt-timestamp" data-t="01:59:50">[01:59:50]</a>. This raises questions about whether to introduce synthetic data to mitigate biases or let the model accurately reflect real-world data <a class="yt-timestamp" data-t="02:01:50">[02:01:50]</a>. Toxicity prevalence was measured using a HateBERT classifier trained on the ToxiGen dataset <a class="yt-timestamp" data-t="02:03:37">[02:03:37]</a>.

### Red Teaming
Meta conducted extensive "red teaming" exercises with 350 internal employees, contractors, and external vendors (including cybersecurity, election fraud, ethics experts) to proactively identify risks and problematic uses <a class="yt-timestamp" data-t="02:12:10">[02:12:10]</a>. This involved probing the model for sexually explicit content, hate speech, and other harmful outputs <a class="yt-timestamp" data-t="02:13:16">[02:13:16]</a>. Red teamers found that creative writing requests or prompts hidden in "positive, progressive, and empowering" language could often bypass safety mechanisms <a class="yt-timestamp" data-t="02:15:35">[02:15:35]</a>.

## Responsible Release Strategy
Meta released [[pretraining_and_data_set_details_of_llama_2 | Llama 2]] for both research and commercial use, subject to an acceptable use policy <a class="yt-timestamp" data-t="02:34:04">[02:34:04]</a>. This open approach is intended to:
*   Encourage responsible AI innovation by leveraging collective wisdom <a class="yt-timestamp" data-t="02:34:27">[02:34:27]</a>.
*   Foster collaboration across academic researchers, civil society, policymakers, and industry <a class="yt-timestamp" data-t="02:34:41">[02:34:41]</a>.
*   Promote transparency and democratize access to foundational models <a class="yt-timestamp" data-t="02:35:13">[02:35:13]</a>.
*   Consolidate costs and eliminate barriers to entry, preventing the duplication of training efforts by multiple closed-source companies <a class="yt-timestamp" data-t="02:35:27">[02:35:27]</a>.

Meta acknowledges that [[use_of_large_language_models_llms_in_robotics | AI models]] can be misused, but believes that open science and collaboration are the best ways to mitigate risks and advance the field <a class="yt-timestamp" data-t="02:36:26">[02:36:26]</a>.

## Conclusion
[[pretraining_and_data_set_details_of_llama_2 | Llama 2]] represents a significant step in open-source [[use_of_large_language_models_llms_in_robotics | LLMs]], demonstrating competitiveness with existing open-source and some proprietary models <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>. While it still lags behind [[comparison_between_llama_31_and_gpt_4 | GPT-4]], Meta emphasized its detailed methods for alignment, helpfulness, and safety, and committed to further improvements in future work <a class="yt-timestamp" data-t="02:37:56">[02:37:56]</a>. The release fosters transparency and community collaboration, aiming to accelerate innovation and address the challenges of [[use_of_large_language_models_llms_in_robotics | AI]] development <a class="yt-timestamp" data-t="02:38:05">[02:38:05]</a>.