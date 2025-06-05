---
title: Comparison of Deep Seek R1 and OpenAI o1 models
videoId: -2k1rcRzsLA
---

From: [[fireship]] <br/> 

China has released DeepSeek R1, a state-of-the-art, free, and open-source Chain of Thought reasoning model. Its performance is noted to rival [[overview_of_openais_o1_model | OpenAI's o1 model]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. While [[overview_of_openais_o1_model | OpenAI o1]] currently costs $200 per month for access <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>, [[deepseek_r1_vs_ai_giants | DeepSeek R1]] is available freely and commercially <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Performance and Availability

[[overview_of_openais_o1_model | OpenAI's o1 model]] was considered a significant step forward in the AI race upon its release <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. However, the open-source community, through [[deepseek_r1_vs_ai_giants | DeepSeek R1]], quickly caught up <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

*   **Benchmarks**: According to benchmarks, [[deepseek_r1_vs_ai_giants | DeepSeek R1]] is on par with [[overview_of_openais_o1_model | OpenAI o1]] and even surpasses it in areas like math and software engineering <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   **Benchmark Skepticism**: It is advised to be cautious about trusting benchmarks, as a company providing a popular math benchmark, Epic AI, recently disclosed it was funded by [[overview_of_openais_o1_model | OpenAI]] <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Accessibility**: [[deepseek_r1_vs_ai_giants | DeepSeek R1]] offers a web-based user interface, can be utilized on platforms like Hugging Face, or downloaded locally using tools such as Olama <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

## Model Parameters and Hardware

[[deepseek_r1_vs_ai_giants | DeepSeek R1]] comes in various parameter sizes:

*   A 7 billion parameter model weighs approximately 4.7 GB <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   Its full potential, with 671 billion parameters, requires over 400 GB of storage and heavy-duty hardware <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   A 32 billion parameter version of [[deepseek_r1_vs_ai_giants | DeepSeek R1]] is considered comparable to [[overview_of_openais_o1_model | o1 mini]] <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Training Methodology

A key distinction of [[deepseek_r1_vs_ai_giants | DeepSeek R1]] is its training approach:

*   **Direct Reinforcement Learning**: Unlike models that might use supervised fine-tuning, [[deepseek_r1_vs_ai_giants | DeepSeek R1]] utilizes direct reinforcement learning <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   **Learning Process**: In this method, the model is given examples without solutions and attempts various approaches. It learns and reinforces itself by eventually discovering the correct solution, similar to human reasoning <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. A brief paper describing the algorithm explains that the AI generates multiple answers for each problem, groups them, and receives a reward score to adjust its approach for higher-scoring answers <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **Supervised Fine-Tuning (Comparison)**: Supervised fine-tuning typically involves showing the model examples with step-by-step solutions and evaluating answers with another model or a human <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## Chain of Thought Capabilities

Both [[deepseek_r1_vs_ai_giants | DeepSeek R1]] and [[overview_of_openais_o1_model | o1]] are Chain of Thought models <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

*   **Prompting**: When prompting such models, it's essential to keep the prompt concise and direct. The design allows the model to perform its own thinking <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.
*   **Output**: For problems like math questions, the model first displays its thinking steps before presenting the final solution <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   **Use Cases**: Chain of Thought models are particularly effective for complex problem-solving, advanced math, puzzles, or coding problems that require detailed planning <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.