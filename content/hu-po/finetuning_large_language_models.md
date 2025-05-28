---
title: Finetuning large language models
videoId: pov3pLFMOPY
---

From: [[hu-po]] <br/> 
The finetuning of [[LLM Large Language Models development | large language models]] (LLMs) is a critical process for enhancing their performance and adapting them to specific tasks or desired behaviors. However, this process often comes with prohibitive memory and computational costs, especially for very large models [00:17:09].

## Challenges of Finetuning LLMs
Traditionally, finetuning LLMs like the LLaMA 65B model at 16-bit precision can demand over 780 gigabytes (GB) of GPU memory [00:17:15]. This massive memory requirement necessitates the use of multiple server racks with dozens of high-memory GPUs (e.g., 12 A100 GPUs), making full finetuning inaccessible for most researchers and smaller organizations [00:17:41]. While [[Large language models and inference efficiency | quantization]] methods have been effective for reducing memory footprints during inference, they typically break down during training, leading to performance degradation [00:18:11].

## Q-LoRA: An Efficient Finetuning Approach
Q-LoRA is an efficient finetuning approach that significantly reduces memory usage, enabling the finetuning of a 65 billion parameter model on a single 48 GB GPU while preserving full 16-bit finetuning task performance [00:04:26]. This approach aims to make [[Finetuning machine learning models | finetuning]] accessible on consumer-grade GPUs [00:07:37].

Q-LoRA achieves its efficiency through several key innovations:

*   **4-bit NormalFloat (NF4)**: This is a new, information-theoretically optimal data type for normally distributed weights [00:10:31]. It yields better empirical results than standard 4-bit integers and 4-bit floats, especially for neural network weights that tend to follow a zero-centered normal distribution [01:12:21]. By normalizing weights to a range of -1 to 1, NF4 maximizes precision within the limited 4-bit space [01:07:43], avoiding the need for extensive quantile estimation [01:11:55].
*   **Double Quantization (DQ)**: This technique further reduces memory footprint by quantizing the *quantization constants* themselves [01:17:40]. These constants, originally stored as 32-bit floats, are compressed to 8-bit floats after being centered around zero [01:25:38]. This saves approximately 0.37 bits per parameter, translating to about 3 GB for a 765 GB model [01:27:41].
*   **Paged Optimizers**: These manage memory spikes that occur during gradient checkpointing by leveraging Nvidia Unified Memory [01:03:39]. This feature allows optimizer states to be automatically evicted to CPU RAM when GPU memory runs out, preventing "out of memory" (OOM) errors that commonly hinder finetuning of large models [01:33:41]. While paging might introduce slowdowns, it provides the same training speed as regular optimizers for certain batch sizes [01:50:09].

### The Role of Low-Rank Adapters (LoRA)
Q-LoRA utilizes [[Large Language Models and Optimization | LoRA]], a method that significantly reduces memory requirements by using a small set of trainable parameters called "adapters" [00:53:47]. The original LLaMA model weights remain "frozen" (unchanged), and gradients are pushed only into these tiny LoRA adapters [00:06:26].

While LoRA is parameter-efficient, the bulk of memory consumption in LLM finetuning comes from activation gradients, not the LoRA parameters themselves [00:59:11]. Q-LoRA's innovations address this by:

*   Storing the base model weights in 4-bit NF4 precision, and de-quantizing them to 16-bit (BFloat16) only during the forward and backward passes for computation [01:03:51].
*   Training the LoRA parameters themselves in 16-bit BFloat16 precision, ensuring high fidelity during the update process [01:37:51].
*   Applying LoRA adapters to *all* linear Transformer block layers, which has been found to be critical for matching full 16-bit finetuning performance [01:59:07]. The specific projection dimension (R) of the LoRA adapters does not significantly affect performance [02:00:20].

## Performance and Accessibility
Q-LoRA allows the finetuning of a 65 billion parameter model in approximately 24 hours on a single professional GPU [00:09:11]. This significantly reduces the time and compute resources, making advanced [[advancements_in_language_models | language model]] research accessible to individuals and academic institutions without needing extensive server racks or industry partnerships [00:09:59].

Q-LoRA consistently matches 16-bit full finetuning performance, demonstrating that performance loss due to aggressive quantization can be fully recovered through adapter finetuning after quantization [02:08:47]. This suggests that it is more beneficial to use a larger base model with lower precision (e.g., a 4-bit 65B LLaMA) than a smaller model with higher precision (e.g., a 32-bit 7B LLaMA) [02:13:52].

## Evaluation and Benchmarking
The Guanaco family of models, finetuned with Q-LoRA, has demonstrated strong performance, even outperforming previously openly released models on the Vicuna Benchmark [00:08:08]. The largest Guanaco model achieved 99.3% of ChatGPT's performance level on this benchmark [00:08:35].

The research also conducted extensive [[large_language_models_in_machine_learning_research | ablation studies]], training over a thousand models with various configurations [00:33:28]. Key findings include:

*   **Data Quality over Quantity**: High-quality instruction data is far more important than the sheer size of the dataset for achieving state-of-the-art results [01:14:30]. For instance, a 9,000-example dataset outperformed a 450,000-example dataset in instruction following [00:34:31].
*   **Benchmark Limitations**: Current chatbot benchmarks are not always trustworthy or accurate [01:15:16]. For example, strong performance on the MMLU (Massive Multitask Language Understanding) benchmark does not necessarily imply strong chatbot performance, and vice versa [02:30:23].
*   **Automated Evaluation**: While GPT-4 evaluations offer a cheap and reasonable alternative to human evaluation, they also have noticeable biases, such as assigning higher scores to models appearing first in its prompt [02:41:50]. However, human and GPT-4 rankings largely agree on model performance, making automated evaluation a somewhat reliable tool [02:29:00].

### Theory of Mind and Model Consistency
Q-LoRA finetuned models exhibit capabilities akin to a "theory of mind," allowing them to infer what external agents might be thinking [02:40:22]. This emergent ability, observed in models like Guanaco, is considered a step towards more sophisticated AI [02:41:07]. While models can consistently answer factual questions, their reliability decreases with more obscure queries, often maintaining unwarranted confidence [02:37:46].

## Future Implications
The advancements in Q-LoRA hold significant implications for the future of [[finetuning_machine_learning_models | finetuning machine learning models]] and the broader AI community:

*   **Open-Source AI**: By making finetuning of large models feasible on consumer hardware, Q-LoRA empowers small independent researchers and the open-source community to contribute to state-of-the-art AI development, fostering competition with large industry labs [02:58:10].
*   **Aggressive Quantization**: The ability to recover performance after quantization through adapter finetuning suggests that even more aggressive quantization (e.g., 3-bit base models) might be possible in the future [02:57:05].
*   **Research Directions**: This work opens new avenues for research, including exploring [[Training and Finetuning of Language Models for Code | multilingual training]] for performance improvement [02:43:15], developing better, less biased benchmarks [02:31:57], and applying similar quantization-plus-adapter strategies to other domains like [[finetuning_audio_generation_models | vision models]] (e.g., stable diffusion control nets) [02:14:58].