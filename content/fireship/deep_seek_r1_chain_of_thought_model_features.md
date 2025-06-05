---
title: Deep Seek R1 Chain of Thought model features
videoId: -2k1rcRzsLA
---

From: [[fireship]] <br/> 

China recently released DeepSeek R1, a state-of-the-art, free, and open-source [[artificial_intelligence_and_reasoning_models | Chain of Thought reasoning model]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Its performance rivals that of [[overview_of_openais_o1_model | OpenAI's o1 model]] <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. DeepSeek R1 is an MIT-licensed model, allowing for free and commercial use in personal applications <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>.

## [[comparison_of_deep_seek_r1_and_openai_o1_models | Comparison to OpenAI o1]]

The release of DeepSeek R1 marks a significant step for open-source AI, quickly catching up to models like [[overview_of_openais_o1_model | OpenAI's o1]] <a class="yt-timestamp" data-t="01:44:03">[01:44:03]</a>. Benchmarks indicate that DeepSeek R1 is on par with [[overview_of_openais_o1_model | OpenAI o1]], and in some areas like math and software engineering, it even surpasses it <a class="yt-timestamp" data-t="01:48:58">[01:48:58]</a>. However, it's advised to approach benchmarks with caution, as evidenced by Epic AI, a company providing a popular math benchmark, recently disclosing funding from OpenAI <a class="yt-timestamp" data-t="01:57:12">[01:57:12]</a>.

## Core Feature: Chain of Thought Reasoning

DeepSeek R1 is a [[artificial_intelligence_and_reasoning_models | Chain of Thought model]] <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>. When prompting such models, it is crucial to keep the input concise and direct, as the model is designed to perform its own thinking process <a class="yt-timestamp" data-t="03:30:45">[03:30:45]</a>. For instance, when solving a math problem, DeepSeek R1 will first display all the intermediate thinking steps before presenting the final solution <a class="yt-timestamp" data-t="03:41:40">[03:41:40]</a>.

[[applications_of_chain_of_thought_models | Chain of Thought models]] like DeepSeek R1 excel in complex problem-solving scenarios <a class="yt-timestamp" data-t="03:53:14">[03:53:14]</a>. They are particularly effective for:
*   Advanced math problems <a class="yt-timestamp" data-t="03:56:58">[03:56:58]</a>
*   Puzzles <a class="yt-timestamp" data-t="03:57:51">[03:57:51]</a>
*   Coding problems that demand detailed planning <a class="yt-timestamp" data-t="03:58:36">[03:58:36]</a>

## Training Methodology: Reinforcement Learning

A distinguishing feature of DeepSeek R1 is its training approach, which avoids supervised fine-tuning in favor of direct [[reinforcement_learning_and_chain_of_thought_in_ai_models | reinforcement learning]] <a class="yt-timestamp" data-t="02:37:06">[02:37:06]</a>.

*   **Supervised Fine-tuning (Traditional Approach)**: Typically involves showing a model numerous examples with step-by-step solutions and then evaluating the answers with another model or human <a class="yt-timestamp" data-t="02:44:17">[02:44:17]</a>.
*   **DeepSeek R1's Direct Reinforcement Learning**: The model is provided with examples but without pre-shown solutions <a class="yt-timestamp" data-t="02:57:04">[02:57:04]</a>. It then attempts various solutions on its own, learning and reinforcing itself by eventually discovering the correct answer <a class="yt-timestamp" data-t="03:01:07">[03:01:07]</a>. This process mimics human-like reasoning capabilities <a class="yt-timestamp" data-t="03:06:21">[03:06:21]</a>.

DeepSeek's brief paper describes this algorithm: for each problem, the AI generates multiple potential answers (outputs). These answers are grouped and assigned a reward score, allowing the AI to adjust its approach to favor answers with higher scores <a class="yt-timestamp" data-t="03:14:13">[03:14:13]</a>.

## Technical Details and Accessibility

DeepSeek R1 offers various parameter sizes:
*   A 7 billion parameter model is approximately 4.7 GB <a class="yt-timestamp" data-t="02:20:47">[02:20:47]</a>.
*   For its full capability, the model boasts 671 billion parameters, requiring over 400 GB and substantial hardware <a class="yt-timestamp" data-t="02:24:08">[02:24:08]</a>.
*   A 32 billion parameter version is comparable to [[overview_of_openais_o1_model | o1 mini]] <a class="yt-timestamp" data-t="02:32:06">[02:32:06]</a>.

The model is accessible via a web-based UI <a class="yt-timestamp" data-t="02:13:30">[02:13:30]</a>, Hugging Face <a class="yt-timestamp" data-t="02:15:37">[02:15:37]</a>, or can be downloaded locally using tools like Ollama <a class="yt-timestamp" data-t="02:17:50">[02:17:50]</a>.