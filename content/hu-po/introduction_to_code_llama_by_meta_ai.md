---
title: Introduction to Code Llama by Meta AI
videoId: Y0gYsq7tOnM
---

From: [[hu-po]] <br/> 

Code Llama is a family of large language models (LLMs) developed by [[Meta AI research | Meta AI]] specifically for code generation and understanding <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. Released relatively recently after Llama 2, Code Llama is described as a fine-tuned version of Llama 2 optimized for coding tasks <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. It is provided under a permissive license that allows for both research and commercial use, although its licensing terms have been noted for being "weird" and "cryptic" compared to standard open-source licenses <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Model Variants and Architecture

Code Llama is offered as a family of models in three different sizes: 7 billion parameters (7B), 13 billion parameters (13B), and 34 billion parameters (34B) <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>. Notably, a 70 billion parameter version, which exists for the generic Llama 2 model, was not released, possibly because 34B is considered the practical limit for local execution on powerful home computers <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

The development of Code Llama is based on "gradually specializing and increasing the capabilities of Llama 2 by applying a cascade of training and fine-tuning steps" <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>. This multi-stage process, often referred to as a "curriculum," involves:
1.  **Foundation Model (Llama 2):** Trained on a vast corpus of generic web and internet data to predict the next token <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.
2.  **Code Training:** Further training on a "code-heavy data set" of 500 billion tokens <a class="yt-timestamp" data-t="00:39:42">[00:39:42]</a>. This includes specifically infilling <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
3.  **Long Context Training:** Further training on longer sequences of code <a class="yt-timestamp" data-t="00:19:16">[00:19:16]</a>.
4.  **Instruction Fine-Tuning:** Tuning for conversational, question-answering styles <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.

Meta's research suggests that initializing with a [[foundation_models_in_ai | foundation model]] like Llama 2 outperforms models with the same architecture trained solely on code from scratch <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>. This implies that the broad knowledge gained from diverse internet data contributes to better code understanding and generation capabilities <a class="yt-timestamp" data-t="00:21:42">[00:21:42]</a>.

## Key Capabilities

Code Llama offers several specialized "flavors" to cover a wide range of applications <a class="yt-timestamp" data-t="00:27:11">[00:27:11]</a>:

*   **Foundation Models (`Code Llama`):** The base models, capable of completing text or code, intended to complete code as if it were part of the training corpus <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   **Python Specialization (`Code Llama Python`):** Additional fine-tuning on Python code <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Instruction Following (`Code Llama Instruct`):** Models tuned for conversational interactions, allowing users to interleave text and code, making them suitable for chat-based interfaces <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.

### Infilling

Code Llama models (7B and 13B) support infilling based on surrounding context <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>. This capability allows the model to fill in missing parts of a program, given the code before and after the missing section <a class="yt-timestamp" data-t="00:52:53">[00:52:53]</a>. This is crucial for real-time code completion in integrated development environments (IDEs) and for tasks like docstring generation <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>. Infilling training involves "causal masking," where parts of a training sequence are moved to the end, and the reordered sequence is predicted auto-regressively <a class="yt-timestamp" data-t="00:53:10">[00:53:10]</a>.

### Large Input Contexts

Code Llama supports large input contexts, which is vital for coding workflows involving large codebases <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>. The models are trained on sequences of 16,000 tokens and demonstrate improvements on inputs up to 100,000 tokens <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. This is a significant increase from Llama 2's 4,000 token limit <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>.

The increased context length is achieved by modifying the parameters of the Rotary Positional Embeddings (RoPE) <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>. Specifically, the base period of the `theta` parameter within RoPE is increased from 10,000 to 1 million for fine-tuning <a class="yt-timestamp" data-t="01:13:01">[01:13:01]</a>. This simple modification allows the model to extrapolate to longer sequences without requiring architectural changes <a class="yt-timestamp" data-t="01:56:02">[01:56:02]</a>.

### Zero-Shot Instruction Following

Code Llama models demonstrate zero-shot instruction following abilities for programming tasks, meaning they can respond to prompts without additional fine-tuning or explicit context <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. The instruction-tuned models (Code Llama Instruct) are trained on proprietary instruction data, including [[ai_and_reinforcement_learning | reinforcement learning from human feedback]] (RLHF), which focuses on helpfulness and safety <a class="yt-timestamp" data-t="01:18:20">[01:18:20]</a>. A notable aspect of their training for coding tasks is the use of "execution feedback" instead of human feedback, where the correctness of generated code is verified by running unit tests <a class="yt-timestamp" data-t="01:20:05">[01:20:05]</a>.

## Performance and [[comparison_and_evaluation_of_code_llama_and_other_language_models | Comparison]]

Code Llama achieves state-of-the-art performance among open models on several code benchmarks, including HumanEval and Mostly Basic Python Programming (MBPP) <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.
*   **HumanEval:** A dataset of 164 original programming problems assessing language comprehension, algorithms, and simple math <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.
*   **MBPP:** A dataset of approximately 1,000 crowdsourced Python programming problems <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

> [!NOTE] Benchmark Limitations
> These benchmarks often involve small, self-contained "programming puzzles" similar to interview questions rather than complex real-world coding tasks. The transcript notes that models trained on these types of problems may semantically "copy-paste" solutions from their training corpus rather than demonstrating fundamental understanding <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

A significant finding is that Code Llama Python 7B outperforms the much larger, generic Llama 2 70B model on HumanEval and MBPP <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. This highlights the benefit of domain-specific fine-tuning, though the speaker speculates this trend may not continue indefinitely as general LLMs become even larger <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

In [[comparison_and_evaluation_of_code_llama_and_other_language_models | comparison]] to closed-source models, Code Llama's 34B model achieves a pass@1 score of 48% on HumanEval, which is lower than [[llama_31_performance_and_comparison_to_gpt_4 | GPT-4]]'s 67% <a class="yt-timestamp" data-t="01:32:20">[01:32:20]</a>. However, Code Llama outperforms other publicly available models across various benchmarks <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>.

## Training Details and Hyperparameters

The training process for Code Llama involves specific hyperparameters:
*   **Optimizer:** AdamW <a class="yt-timestamp" data-t="01:24:37">[01:24:37]</a>.
*   **Learning Rate Schedule:** Cosine schedule with 1,000 warm-up steps <a class="yt-timestamp" data-t="01:24:47">[01:24:47]</a>. The final learning rate is set to 1/30th of the peak <a class="yt-timestamp" data-t="01:26:19">[01:26:19]</a>. Initial learning rates range from 3e-4 to 1e-4 depending on the model size and stage <a class="yt-timestamp" data-t="01:28:44">[01:28:44]</a>.
*   **Batch Size:** Ranges from 4 million tokens for initial code training to 2 million tokens for long context fine-tuning (for 7B/13B models) <a class="yt-timestamp" data-t="01:26:51">[01:26:51]</a>.
*   **Training Steps:** Up to 10,000 gradient steps, with some configurations adjusted to 11,000 for 34B and 3,000 for Code Llama models to avoid instabilities <a class="yt-timestamp" data-t="01:30:10">[01:30:10]</a>.

The models are trained on a predominantly "near deduplicated" code-heavy dataset <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>. While the exact composition is not fully disclosed, an 8% portion of the samples comes from natural language data related to code (e.g., discussions, questions, answers) to help the model retain natural language understanding <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>. There is evidence suggesting the training data includes content from platforms like Stack Overflow <a class="yt-timestamp" data-t="00:41:33">[00:41:33]</a>.

For instruction tuning, some data is synthetically generated by prompting Llama 2 70B to create interview-style programming questions and then generating Python solutions and unit tests, validating them with execution feedback <a class="yt-timestamp" data-t="02:02:29">[02:02:29]</a>. This approach for generating synthetic data using LLMs is becoming increasingly common <a class="yt-timestamp" data-t="01:34:54">[01:34:54]</a>.

## Broader Implications

### The Bitter Lesson and Future of AI

The development of Code Llama and its performance further reinforce the "bitter lesson," a concept suggesting that simple, scalable methods often outperform complex, human-engineered ones in the long run <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. The ability of a smaller, code-tuned model to surpass a larger general model is presented as a temporary pattern. It is speculated that as GPUs become more powerful and data sets grow, a single, massive general-purpose LLM trained on "literally every single piece of text in the world" will eventually outperform specialized models for specific tasks, including coding <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. This suggests a future where all human knowledge, from coding to medicine, converges into a single, higher-level abstraction within a sufficiently large model <a class="yt-timestamp" data-t="02:01:42">[02:01:42]</a>.

### [[challenges_of_code_generation_using_ai | Challenges of Code Generation]] and Workflow

While Code Llama excels at programming puzzles, the [[challenges_of_code_generation_using_ai | challenges of code generation using AI]] in real-world scenarios remain. The current workflow of copying code snippets, asking questions, and pasting back is cumbersome <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. Infilling capabilities are seen as a superior solution, allowing for more seamless integration into IDEs by automatically completing code based on the surrounding context <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.

Concerns exist regarding safety tuning in instruction-following models, as attempts to prevent unsafe or biased outputs can make models less helpful and more "sycophantic" <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>. The speaker suggests that safety integration might need to occur earlier in the training pipeline, rather than as a final fine-tuning step, to avoid "castrating" the models' utility <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>.

### The Debate on Open Source and Data Transparency

Despite being presented as "open," Code Llama's underlying training data is not fully disclosed <a class="yt-timestamp" data-t="00:39:50">[00:39:50]</a>. This lack of transparency is a broader issue in the LLM landscape, as knowing the dataset is crucial for understanding and interpreting model behavior <a class="yt-timestamp" data-t="00:40:11">[00:40:11]</a>. The secrecy likely stems from legal concerns regarding data scraping and intellectual property rights <a class="yt-timestamp" data-t="00:42:07">[00:42:07]</a>. The use of "unnatural instructions" for synthetic data generation points towards a future where data augmentation and synthetic data could democratize LLM training by reducing reliance on proprietary datasets <a class="yt-timestamp" data-t="01:35:08">[01:35:08]</a>.

Code Llama represents a significant step in developing specialized large language models for coding, demonstrating the power of fine-tuning [[foundation_models_in_ai | foundation models]] and pushing the boundaries of context length for practical applications.