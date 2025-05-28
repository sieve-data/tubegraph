---
title: Comparison and Evaluation of Code Llama and Other Language Models
videoId: Y0gYsq7tOnM
---

From: [[hu-po]] <br/> 

[[Introduction to Code Llama by Meta AI | Code Llama]], developed by [[Large Language Models and their applications | Meta AI]], is a family of large language models specifically designed for code generation and understanding <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. It is based on the previously released [[LLaMAAdapter and its role in adapting language models | Llama 2]] model <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This article evaluates [[Introduction to Code Llama by Meta AI | Code Llama]]'s performance against other models, including [[LLaMAAdapter and its role in adapting language models | Llama 2]] and [[Llama 31 performance and comparison to GPT 4 | GPT-4]], highlighting its unique features and training methodology.

## Code Llama: Family and Flavors
[[Introduction to Code Llama by Meta AI | Code Llama]] is released as a family of models, available in different sizes: 7 billion, 13 billion, and 34 billion parameters <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. The largest possible size (70 billion parameters) from [[LLaMAAdapter and its role in adapting language models | Llama 2]] was not released for [[Introduction to Code Llama by Meta AI | Code Llama]], potentially because 34 billion parameters is near the limit for local execution <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

The models come in "flavors" to cover a wide range of applications <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>:
*   **Foundation Models**: The original [[Introduction to Code Llama by Meta AI | Code Llama]] models, primarily designed for code completion <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. They function by completing text as if it were part of a training corpus and cannot handle conversational queries <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Python Specialization**: Additional fine-tuning on Python code <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Instruction Following (Instruct Models)**: Tuned for conversational style, allowing users to interleave text and code, and ask direct questions <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. For example, a 13B chat model can be asked to "write me fizzbuzz in Python" and will provide the code <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>.

### Key Features
*   **Infilling Capabilities**: The ability to fill in missing parts of code given surrounding context, crucial for real-time completion in code editors or docstring generation <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>, <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>. This feature enables predicting a middle part of a document given a prefix and suffix <a class="yt-timestamp" data-t="00:52:54">[00:52:54]</a>.
*   **Large Input Context**: Models are trained on sequences of 16,000 tokens and show improvements on inputs up to 100,000 tokens <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>, <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This allows for feeding an entire codebase, moving beyond snippet-based interactions <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a>. This was achieved by modifying the parameters of the Rotary Positional Embeddings (RoPE) <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>.
*   **Zero-Shot Instruction Following**: The ability to perform programming tasks without additional fine-tuning or extra context <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## [[evaluation metrics for language models | Evaluation Metrics]] and Benchmarks

[[Introduction to Code Llama by Meta AI | Code Llama]]'s performance is primarily measured using the following benchmarks:
*   **HumanEval**: Consists of 164 original programming problems assessing language comprehension, algorithms, and simple math <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. These are typically short, single-function problems similar to programming interview puzzles <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   **MBPP (Mostly Basic Python Programming)**: A dataset of about 1,000 crowdsourced Python programming problems solved by entry-level programmers, covering programming fundamentals <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

Performance on these benchmarks is reported using `pass@k` scores, where:
*   `pass@1`: The model provides the correct answer on the first attempt <a class="yt-timestamp" data-t="01:01:47">[01:01:47]</a>.
*   `pass@10`: The correct answer is found within 10 generated attempts <a class="yt-timestamp" data-t="01:01:52">[01:01:52]</a>.
*   `pass@100`: The correct answer is found within 100 generated attempts <a class="yt-timestamp" data-t="01:02:03">[01:02:03]</a>. Higher `k` values generally result in higher scores <a class="yt-timestamp" data-t="01:02:07">[01:02:07]</a>.

Other [[evaluation metrics for language models | evaluation metrics]] include:
*   **Perplexity**: Measures how well a probability distribution predicts a sample. A lower perplexity indicates better predictions <a class="yt-timestamp" data-t="01:15:23">[01:15:23]</a>.
*   **Synthetic Key Retrieval Tasks**: Tests a model's ability to retrieve a "secret key" hidden within a very long context (e.g., 16,000 tokens), indicating its long-range memory and comprehension <a class="yt-timestamp" data-t="01:16:10">[01:16:10]</a>.

## Comparison to Llama 2 and [[Llama 31 performance and comparison to GPT 4 | GPT-4]]

### Code Llama vs. [[LLaMAAdapter and its role in adapting language models | Llama 2]]
A significant finding is that [[Introduction to Code Llama by Meta AI | Code Llama Python]] 7B (the smallest Python-specialized version) outperforms the much larger, generic [[LLaMAAdapter and its role in adapting language models | Llama 2]] 70B model on HumanEval and MBPP <a class="yt-timestamp" data-t="01:05:05">[01:05:05]</a>. This demonstrates that a smaller, specialized [[Large Language Models and their applications | AI]] can currently outperform a larger, general [[Large Language Models and their applications | AI]] on specific domain tasks <a class="yt-timestamp" data-t="01:05:33">[01:05:33]</a>.

Initializing [[Introduction to Code Llama by Meta AI | Code Llama]] with [[LLaMAAdapter and its role in adapting language models | Llama 2]]'s weights (pre-training on generic text) significantly outperforms training a model with the same architecture purely on code from scratch <a class="yt-timestamp" data-t="02:22:11">[02:22:11]</a>. This suggests that the general knowledge acquired during pre-training on diverse internet data (including history, biology, and even personal conversations) improves the model's logical reasoning, making it better at specialized tasks like coding <a class="yt-timestamp" data-t="02:14:46">[02:14:46]</a>.

### Code Llama vs. [[Llama 31 performance and comparison to GPT 4 | GPT-4]] and Other Models
[[Introduction to Code Llama by Meta AI | Code Llama]] claims "state-of-the-art performance among open models" <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. This phrasing is critical because it explicitly excludes models like [[Llama 31 performance and comparison to GPT 4 | GPT-4]], which is not publicly available or open-source <a class="yt-timestamp" data-t="01:16:10">[01:16:10]</a>.

In direct comparisons:
*   On HumanEval, [[Introduction to Code Llama by Meta AI | Code Llama Instruct]] 34B achieved a `pass@1` score of 48% <a class="yt-timestamp" data-t="01:32:22">[01:32:22]</a>.
*   [[Llama 31 performance and comparison to GPT 4 | GPT-4]]'s `pass@1` score on HumanEval was 67% <a class="yt-timestamp" data-t="01:32:25">[01:32:25]</a>.
*   This indicates that [[Llama 31 performance and comparison to GPT 4 | GPT-4]] still significantly outperforms [[Introduction to Code Llama by Meta AI | Code Llama]] on these benchmarks, maintaining its position as a leading code generation model <a class="yt-timestamp" data-t="01:32:30">[01:32:30]</a>.
*   Compared to other "open" models like StarCoder, [[Introduction to Code Llama by Meta AI | Code Llama]] 34B shows competitive performance, surpassing StarCoder's 40% on HumanEval <a class="yt-timestamp" data-t="01:33:03">[01:33:03]</a>.

### Impact of Training Methodology
[[Introduction to Code Llama by Meta AI | Code Llama]] employs a "specialization pipeline" or curriculum for training, involving multiple fine-tuning steps <a class="yt-timestamp" data-t="01:56:56">[01:56:56]</a>:
1.  Pre-training on generic web data (Llama 2).
2.  Further training on code, specifically for infilling.
3.  Long context fine-tuning (extending context from 4,000 to 16,000 tokens) <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>.
4.  Instruction fine-tuning for chat capabilities <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>.

This multi-step approach is designed to balance long-range capabilities with training cost <a class="yt-timestamp" data-t="01:07:33">[01:07:33]</a>. While long context fine-tuning and infilling generally don't catastrophically degrade performance on short context benchmarks, there can be subtle impacts, suggesting a domain gap between different types of code tasks <a class="yt-timestamp" data-t="01:02:49">[01:02:49]</a>, <a class="yt-timestamp" data-t="01:30:37">[01:30:37]</a>.

The models use a mix of code-heavy and natural language data sets. The inclusion of natural language data, especially discussions about code, improves performance on benchmarks like MBPP <a class="yt-timestamp" data-t="00:47:02">[00:47:02]</a>, <a class="yt-timestamp" data-t="00:48:42">[00:48:42]</a>. For instruction tuning, [[Introduction to Code Llama by Meta AI | Code Llama]] leverages self-instruct data generation, where [[LLaMAAdapter and its role in adapting language models | Llama 2]] 70B generates interview-style programming questions, and [[Introduction to Code Llama by Meta AI | Code Llama]] 7B generates solutions which are then filtered by execution feedback via unit tests <a class="yt-timestamp" data-t="01:20:05">[01:20:05]</a>.

### "Open Source" Nature
Meta releases [[Introduction to Code Llama by Meta AI | Code Llama]] under a "permissive license" that allows for both research and commercial use, albeit with "weird cryptic" caveats <a class="yt-timestamp" data-t="00:49:57">[00:49:57]</a>. This contrasts with OpenAI's approach, which is famously "the opposite of open [[Large Language Models and their applications | AI]]" <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>.

A major point of contention is the secrecy surrounding the training data sets <a class="yt-timestamp" data-t="00:39:57">[00:39:57]</a>. While Meta allows access to the models, they do not disclose the full data set, which is crucial for understanding model behavior and potential vulnerabilities <a class="yt-timestamp" data-t="00:40:11">[00:40:11]</a>. Evidence suggests that [[Introduction to Code Llama by Meta AI | Code Llama]] was trained on data scraped from Stack Overflow, as it has been observed to output Stack Overflow usernames <a class="yt-timestamp" data-t="00:41:08">[00:41:08]</a>.

## The Future of [[Large Language Models and their applications | Language Models]] and Code
The results indicate a trend towards [[Large Language Models and their applications | LLMs]] becoming more generalized. While current fine-tuning on specific domains yields superior performance <a class="yt-timestamp" data-t="01:51:24">[01:51:24]</a>, there's a strong hypothesis that future, even larger general [[Large Language Models and their applications | LMs]] will eventually outperform all specialized models <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. This is partly due to the idea that "intelligence is compression"—larger models find higher-level semantic abstractions that unify different programming languages and, potentially, even different fields of human knowledge <a class="yt-timestamp" data-t="02:00:51">[02:00:51]</a>.

For practical application, the ability to control temperature (randomness of output) offers strategic advantages. A smaller model with a higher temperature can generate 100 diverse answers for `pass@100` and achieve higher scores than a larger model with a low temperature (designed for `pass@1`) <a class="yt-timestamp" data-t="01:47:54">[01:47:54]</a>. This suggests that for applications where multiple suggestions can be filtered (e.g., IDE auto-completion), smaller, more random models could be more efficient <a class="yt-timestamp" data-t="01:48:03">[01:48:03]</a>.

Ultimately, while [[Introduction to Code Llama by Meta AI | Code Llama]] represents a significant step forward for open-source code [[Large Language Models and their applications | LLMs]], the field continues to evolve rapidly, with a potential future where one massive, general model excels at everything <a class="yt-timestamp" data-t="02:02:51">[02:02:51]</a>.