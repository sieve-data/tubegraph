---
title: Llama 2 architecture and training
videoId: 1ZwXkw9_Xq8
---

From: [[hu-po]] <br/> 

Llama 2 is a collection of pre-trained and fine-tuned Large Language Models (LLMs) developed and released by Meta <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. It represents a significant step as the "first open source big competitive LLM" <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>, available for both research and commercial use <a class="yt-timestamp" data-t="02:34:06">[02:34:06]</a>.

## Model Availability and Access
Llama 2 models are available in various sizes, ranging from 7 billion to 70 billion parameters <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Users can download these models via Meta's website by filling out a form, then using a `download.sh` script <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

Available versions include:
*   7B model (smaller, base model) <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>
*   7B chat model (fine-tuned for dialogue) <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
*   13B model <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
*   13B chat model <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
*   70B model <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>
*   70B chat model <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>

Notably, a 34B model was used for evaluations but is not publicly offered, possibly due to differing training setups or safety concerns <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>, <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>. The 13B model is suggested as a "sweet spot" for performance and local usability <a class="yt-timestamp" data-t="01:03:09">[01:03:09]</a>, <a class="yt-timestamp" data-t="02:42:41">[02:42:41]</a>.

## [[impact_of_architecture_on_training_and_inference | Architecture and Improvements]]
Llama 2 builds upon the autoregressive Transformer architecture used in Llama 1 <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>, <a class="yt-timestamp" data-t="00:26:22">[00:26:22]</a>. Key architectural elements include:
*   **Pre-normalization**: Using RMS Norm before the Transformer block <a class="yt-timestamp" data-t="00:26:25">[00:26:25]</a>.
*   **Activation function**: SwiGLU <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>.
*   **Positional embeddings**: Rotary Positional Embeddings (RoPE) <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>.
*   **Increased Context Length**: The context window for Llama 2 was doubled from 2048 to 4096 tokens <a class="yt-timestamp" data-t="00:29:16">[00:29:16]</a>. This is particularly useful for longer histories, summarization, and understanding longer documents <a class="yt-timestamp" data-t="00:30:11">[00:30:11]</a>.
*   **Grouped Query Attention (GQA)**: A modification to the attention mechanism designed to reduce the memory cost associated with KV (key-value) cache size, especially with increasing context windows or batch sizes <a class="yt-timestamp" data-t="00:33:15">[00:33:15]</a>. GQA allows sharing key and value projections across multiple heads without significant performance degradation <a class="yt-timestamp" data-t="00:33:38">[00:33:38]</a>. The 8 KV projections variant of GQA performed comparably to the Multi-Head Attention (MHA) baseline and better than Multi-Query Attention (MQA) variants <a class="yt-timestamp" data-t="00:35:51">[00:35:51]</a>, <a class="yt-timestamp" data-t="00:37:01">[00:37:01]</a>. This choice optimizes for inference latency, especially when deploying on multiple GPUs <a class="yt-timestamp" data-t="00:37:50">[00:37:50]</a>, <a class="yt-timestamp" data-t="00:41:10">[00:41:10]</a>.

## [[LLM Large Language Models development | Training Process]]
Llama 2 was trained through a two-stage process: pre-training and fine-tuning <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.

### Pre-training
The models were pre-trained on a new mix of publicly available online data, explicitly excluding data from Meta's products or services <a class="yt-timestamp" data-t="02:22:52">[02:22:52]</a>, <a class="yt-timestamp" data-t="02:23:55">[02:23:55]</a>.
*   **Data Size**: The pre-training corpus was increased by 40%, totaling two trillion tokens <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>, <a class="yt-timestamp" data-t="02:34:45">[02:34:45]</a>.
*   **Data Cleaning and Mixing**: Robust data cleaning was performed, and factual resources were up-sampled to "increase knowledge and dampen hallucinations" <a class="yt-timestamp" data-t="02:24:04">[02:24:04]</a>, <a class="yt-timestamp" data-t="02:24:46">[02:24:46]</a>.
*   **Hyperparameters**:
    *   Optimizer: AdamW <a class="yt-timestamp" data-t="02:42:51">[02:42:51]</a>.
    *   Learning Rate Schedule: Cosine decay with a 2000-step warm-up period, decaying to 10% of the maximum learning rate <a class="yt-timestamp" data-t="02:43:05">[02:43:05]</a>, <a class="yt-timestamp" data-t="02:44:15">[02:44:15]</a>.
    *   Weight Decay: 0.1 <a class="yt-timestamp" data-t="02:44:29">[02:44:29]</a>.
    *   Gradient Clipping: 1 <a class="yt-timestamp" data-t="02:44:32">[02:44:32]</a>.
*   **Tokenizer**: The same byte-pair encoding tokenizer as Llama 1 was used, specifically SentencePiece tokenizer from 2018 <a class="yt-timestamp" data-t="02:50:01">[02:50:01]</a>, <a class="yt-timestamp" data-t="02:51:24">[02:51:24]</a>. Numbers are split into individual digits (e.g., 2016 becomes '2', '0', '1', '6'), and unknown UTF-8 characters are decomposed into bytes <a class="yt-timestamp" data-t="02:51:32">[02:51:32]</a>. The vocabulary size is 32,000 tokens <a class="yt-timestamp" data-t="02:52:17">[02:52:17]</a>.
*   **Training Observation**: The models did not show signs of saturation, indicating they could have been trained for longer <a class="yt-timestamp" data-t="02:47:32">[02:47:32]</a>.

### Fine-tuning (Llama 2 Chat)
The chat-optimized models, called Llama 2 Chat, underwent extensive fine-tuning using alignment techniques, including supervised fine-tuning (SFT) and [[LLM Large Language Models development | Reinforcement Learning from Human Feedback]] (RLHF) <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>, <a class="yt-timestamp" data-t="03:17:18">[03:17:18]</a>.

#### Supervised Fine-Tuning (SFT)
*   **Data**: Focused on collecting "several thousand examples of high quality SFT data" (27,540 annotations) from vendor-based annotation efforts, specifically excluding Meta user data <a class="yt-timestamp" data-t="01:05:44">[01:05:44]</a>, <a class="yt-timestamp" data-t="01:07:17">[01:07:17]</a>. They found a limited set of clean instruction tuning data sufficient for high quality <a class="yt-timestamp" data-t="01:06:33">[01:06:33]</a>.
*   **Process**: Trained with a cosine learning rate schedule (initial 2e-5), weight decay (0.1), batch size of 64, and sequence length of 4096 tokens <a class="yt-timestamp" data-t="01:08:32">[01:08:32]</a>. Prompts and answers were concatenated, separated by a special token <a class="yt-timestamp" data-t="01:08:46">[01:08:46]</a>.

#### [[LLM Large Language Models development | Reinforcement Learning from Human Feedback]] (RLHF)
RLHF further aligns the fine-tuned language model with human preferences <a class="yt-timestamp" data-t="01:10:36">[01:10:36]</a>.
*   **Human Preference Data**: Collected using a binary comparison protocol, where human annotators chose between two model outputs (significantly better, better, slightly better, negligibly better, or unsure) <a class="yt-timestamp" data-t="01:12:02">[01:12:02]</a>.
*   **Reward Models**: Two separate reward models were trained: one for "helpfulness" and another for "safety" <a class="yt-timestamp" data-t="02:17:35">[02:17:35]</a>, <a class="yt-timestamp" data-t="01:17:35">[01:17:35]</a>.
*   **Training Objective**: Used a binary ranking loss, modified with a margin component to assign more discrepant scores, especially for separable responses <a class="yt-timestamp" data-t="01:18:05">[01:18:05]</a>, <a class="yt-timestamp" data-t="01:19:37">[01:19:37]</a>.
*   **Iterative Fine-Tuning**: Successive versions of RLHF models (V1 to V5) were trained as more human preference data was collected. This process involved the model iteratively creating data for its own training <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.
*   **Algorithm**: Proximal Policy Optimization (PPO) was used for the RL algorithm <a class="yt-timestamp" data-t="01:30:16">[01:30:16]</a>. It trains the policy (the LLM itself) to maximize a reward function that balances helpfulness and safety, while also penalizing it for drifting too far from the original policy (using KL Divergence) <a class="yt-timestamp" data-t="01:33:35">[01:33:35]</a>, <a class="yt-timestamp" data-t="01:35:08">[01:35:08]</a>.

#### [[Prompt Engineering using LLMs | Ghost Attention (GAtt)]]
A technique introduced to improve multi-turn consistency where the model tends to forget initial instructions after a few turns of dialogue <a class="yt-timestamp" data-t="01:43:15">[01:43:15]</a>. GAtt synthetically concatenates the initial system instruction (e.g., "Always answer in emojis") to all user messages within a conversation during training <a class="yt-timestamp" data-t="01:44:12">[01:44:12]</a>, <a class="yt-timestamp" data-t="01:44:56">[01:44:56]</a>. This ensures the model maintains high attention activations to the instruction throughout long dialogues <a class="yt-timestamp" data-t="01:50:03">[01:50:03]</a>.

#### Safety Fine-Tuning and Context Distillation
*   **Objective**: To generate safer model responses <a class="yt-timestamp" data-t="02:05:01">[02:05:01]</a>.
*   **Method**: Involves "prefixing a prompt with a safety prompt" (e.g., "You are a safe and responsible assistant") and then fine-tuning the model on the resulting safer responses *without* the pre-prompt <a class="yt-timestamp" data-t="02:05:17">[02:05:17]</a>. This effectively "distills the safety pre-prompt into the model" <a class="yt-timestamp" data-t="02:05:29">[02:05:29]</a>.

## [[Hardware for AI training and deployment | Hardware and Carbon Footprint]]
Llama 2 models were pre-trained on Meta's Research SuperCluster (RSC) and internal production clusters <a class="yt-timestamp" data-t="02:52:28">[02:52:28]</a>. Both clusters utilize Nvidia A100 GPUs <a class="yt-timestamp" data-t="02:52:36">[02:52:36]</a>.
*   **Interconnects**: RSC uses Nvidia Quantum Infiniband, while the production cluster uses RoCE (RDMA over Converged Ethernet) <a class="yt-timestamp" data-t="02:52:44">[02:52:44]</a>. Both achieve 200 gigabytes per second <a class="yt-timestamp" data-t="02:53:25">[02:53:25]</a>. RoCE is a more affordable alternative that scales almost as well as Infiniband up to 2000 GPUs <a class="yt-timestamp" data-t="02:55:28">[02:55:28]</a>.
*   **Power Consumption**: RSC GPUs consume 400 watts, while production cluster GPUs consume 350 watts <a class="yt-timestamp" data-t="02:53:30">[02:53:30]</a>. This suggests that RSC's better cooling allows for higher power draw and faster operation <a class="yt-timestamp" data-t="02:54:39">[02:54:39]</a>.
*   **Carbon Footprint**: The paper includes calculations for the carbon emissions associated with training the models, a common practice in LLM development <a class="yt-timestamp" data-t="02:57:15">[02:57:15]</a>.

## [[llama_31_performance_and_comparison_with_gpt_models | Performance and Evaluation]]
Llama 2's performance was evaluated against both open-source and closed-source models.
*   **Human Evaluation**: Human evaluators compared model generations on around 4,000 prompts for helpfulness and safety <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
    *   Llama 2 consistently outperformed Falcon 40B <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
    *   Llama 2 70B performed "about the same" as Google's Palm Bison <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
    *   Llama 2 70B was "pretty much on par" with [[Comparison of LLaMA with other models | ChatGPT-3.5]] <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   **Model-based Evaluation**: [[Llama 31 performance and comparison with GPT models | GPT-4]] was used as a "more capable model" to judge the quality of responses <a class="yt-timestamp" data-t="01:11:44">[01:11:44]</a>. Llama 2 was found to be better than [[Comparison of LLaMA with other models | GPT-3.5]], Palm Bison, and Falcon 40B in terms of both helpfulness and safety according to [[Llama 31 performance and comparison with GPT models | GPT-4]] <a class="yt-timestamp" data-t="01:17:18">[01:17:18]</a>.
*   **Safety Evaluation**: Llama 2 Chat models achieved low violation rates for safety, although the 34B model showed a peculiar higher violation rate compared to 13B and 70B <a class="yt-timestamp" data-t="01:16:46">[01:16:46]</a>.
*   **Academic Benchmarks**: [[Llama 31 performance and comparison with GPT models | Llama 2]] lagged behind [[Llama 31 performance and comparison with GPT models | GPT-4]] on benchmarks like MMLU and GSM8K (grade school math word problems) <a class="yt-timestamp" data-t="00:59:19">[00:59:19]</a>, <a class="yt-timestamp" data-t="01:00:38">[01:00:38]</a>. The paper suggests [[Llama 31 performance and comparison with GPT models | GPT-4]]'s ensemble nature might contribute to its superior performance on these tasks <a class="yt-timestamp" data-t="01:01:29">[01:01:29]</a>.
*   **Emergent Capabilities**: Llama 2 demonstrates emergent capabilities like time awareness and tool use, the latter enabling it to understand and utilize API arguments through semantics alone <a class="yt-timestamp" data-t="02:26:19">[02:26:19]</a>, <a class="yt-timestamp" data-t="02:27:07">[02:27:07]</a>.

## Ethical Considerations and Release Strategy
The paper devotes significant attention to safety and ethical considerations, with over 15 pages dedicated to these topics <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>, <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Biases**: Acknowledges biases in pre-training data, such as pronoun bias, which can reflect real-world societal biases <a class="yt-timestamp" data-t="01:59:50">[01:59:50]</a>.
*   **Data Toxicity**: Measures toxicity using a HateBERT classifier trained on the ToxiGen dataset <a class="yt-timestamp" data-t="02:03:37">[02:03:37]</a>.
*   **Red Teaming**: Meta conducted extensive red teaming, involving 350 internal employees, contractors, and external vendors with diverse expertise (cybersecurity, election fraud, ethics, creative writing, etc.) <a class="yt-timestamp" data-t="02:12:10">[02:12:10]</a>, <a class="yt-timestamp" data-t="02:12:40">[02:12:40]</a>. These teams actively probed the model for potential harmful outputs across various risk categories, including sexually explicit content, hate speech, and unqualified advice <a class="yt-timestamp" data-t="02:13:16">[02:13:16]</a>, <a class="yt-timestamp" data-t="02:16:21">[02:16:21]</a>. They found that creative writing requests were often a reliable way to bypass safety mechanisms <a class="yt-timestamp" data-t="02:15:35">[02:15:35]</a>.
*   **Release Strategy**: Meta chose an open-release approach, making Llama 2 available for commercial use under an acceptable use policy <a class="yt-timestamp" data-t="02:34:04">[02:34:04]</a>, <a class="yt-timestamp" data-t="02:34:16">[02:34:16]</a>. They advocate for open collaboration to identify and mitigate risks, believing it fosters innovation and accelerates progress by decentralizing AI expertise and consolidating costs <a class="yt-timestamp" data-t="02:34:25">[02:34:25]</a>, <a class="yt-timestamp" data-t="02:35:20">[02:35:20]</a>.

> "Many companies have opted to build AI behind closed door we're releasing llama2 to openly encourage responsible AI Innovation based on our experience and open approach draws upon the collective wisdom diversity and Ingenuity of the AI practitioner Community to realize the benefits of this technology." <a class="yt-timestamp" data-t="02:34:24">[02:34:24]</a>

This open release is framed as a means to make [[LLM Large Language Models development | LLM Large Language Models development | LLM Large Language Models development | LLM Large Language Models development | Large Language Models (LLMs)]] more accessible and accelerate their development <a class="yt-timestamp" data-t="02:35:11">[02:35:11]</a>.