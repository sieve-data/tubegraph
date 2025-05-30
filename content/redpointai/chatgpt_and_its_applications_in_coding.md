---
title: ChatGPT and its applications in coding
videoId: gwgDDkLFvd0
---

From: [[redpointai]] <br/> 

Logan Kilpatrick, the first AI hire at OpenAI, highlights the extensive applications of ChatGPT, particularly in coding and software development. His role at OpenAI focuses on enhancing the developer platform, a task where ChatGPT has proven indispensable <a class="yt-timestamp" data-t="00:54:54">[00:54:54]</a>.

## Personal and Professional Use of ChatGPT in Coding

Kilpatrick, despite not having a classical computer science background as a software engineer or being a web development expert, uses ChatGPT extensively in his work <a class="yt-timestamp" data-t="00:51:00">[01:00:00]</a>. He estimates that approximately 90% of the features he ships are built using ChatGPT-generated code <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This reliance on AI allows him to go "beyond what I would normally be able to do" without spending excessive hours on documentation for frameworks like React <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. He finds significant value in its ability to generate "true coding things" daily <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

The models, including GPT-4, provide significant freedom for engineers <a class="yt-timestamp" data-t="00:01:18">[01:18]</a>. The ability to quickly translate ideas into functional code without deep domain expertise is a major benefit <a class="yt-timestamp" data-t="00:01:07">[01:07]</a>.

## Impact on Developers and Software Engineering

Kilpatrick emphasizes that AI coding tools are becoming "table stakes" for developers <a class="yt-timestamp" data-t="00:55:08">[00:55:08]</a>. He asserts that an average developer using AI tools can outperform some of the best in the world without them <a class="yt-timestamp" data-t="00:55:10">[00:55:10]</a>. This capability amplifies a developer's ability to build anything they can imagine, a stark contrast to two years prior <a class="yt-timestamp" data-t="00:55:20">[00:55:20]</a>.

He strongly advises all developers to use tools like ChatGPT and [[GitHub Copilot and its impact on software development | GitHub Copilot]] <a class="yt-timestamp" data-t="00:54:57">[00:54:57]</a>. The continuous evolution of models suggests that in the coming years, individuals will have the capability to build almost any product or service due to the extensive assistance provided by these models <a class="yt-timestamp" data-t="00:55:31">[00:55:31]</a>.

### Key Tools and Concepts:

*   **Code Interpreter**: Six months prior to the interview, code interpreter was not available in the API, but it has since become one of the most exciting features for developers to build into their products <a class="yt-timestamp" data-t="00:03:00">[03:00]</a>.
*   **Assistance API**: Kilpatrick believes the Assistance API will be a long-term significant offering, enabling many more experiences a year from now <a class="yt-timestamp" data-t="00:02:10">[02:10]</a> <a class="yt-timestamp" data-t="00:02:48">[02:48]</a>.
*   **Fine-tuning**: Fine-tuning models like GPT-3.5 can achieve GPT-4 level performance with prompt engineering, leading to token savings <a class="yt-timestamp" data-t="00:05:58">[05:58]</a>.
*   **Function Calling**: A crucial use case that enables most interesting production applications <a class="yt-timestamp" data-t="00:49:51">[49:51]</a>. Fine-tuning GPT-3.5 for function calling works very well, allowing developers to remove function tokens from prompts, reducing costs <a class="yt-timestamp" data-t="00:06:49">[06:49]</a>.
*   **Custom Models**: While expensive ($2-3 million), custom models are useful for domains where base models lack sufficient data, such as legal or medical fields <a class="yt-timestamp" data-t="00:07:40">[07:40]</a> <a class="yt-timestamp" data-t="00:08:17">[08:17]</a>. They also allow for more compute-efficient models by removing unnecessary training data <a class="yt-timestamp" data-t="00:10:06">[10:06]</a>. However, building them requires significant data (billions of tokens) and machine learning expertise <a class="yt-timestamp" data-t="00:10:44">[10:44]</a>. OpenAI's custom model program offers hand-holding from their research teams for companies lacking world-class ML teams <a class="yt-timestamp" data-t="00:11:15">[11:15]</a>.
*   **Multimodal AI**: While still early for vision use cases, the future will involve significant multimodal capabilities <a class="yt-timestamp" data-t="00:21:55">[03:21]</a>. The current state of vision models is comparable to GPT-3.5, and a "GPT-4" level leap is needed for more robust applications, especially for detailed understanding of positional relationships between objects <a class="yt-timestamp" data-t="00:04:06">[04:06]</a>.
*   **Prompt Engineering**: Despite talk of its "death," prompt engineering persists in being quite useful <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>. Its fundamental nature is communication, and models like DALL-E 3 demonstrate a future where the model translates a concise user prompt into a more verbose, revised prompt for better results, reducing user friction <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.
*   **Observability**: Kilpatrick considers observability "underhyped" and crucial for developers to understand how models are functioning <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>. Many developers use third-party observability products due to OpenAI's current lack of a detailed dashboard for API usage <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

## Comparison with Open Source Models

Kilpatrick, a proponent of open source, believes that OpenAI's models will consistently outperform open source alternatives due to the immense cost and engineering work involved in training large models <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. However, open source models like Llama offer greater customization and fine-tuning options, including the ability to apply techniques like Reinforcement Learning from Human Feedback (RLHF), which are not yet available in OpenAI's standard offerings <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>.

## Challenges and Future Outlook

*   **Robustness and Reliability**: Enterprises face challenges in ensuring LLM robustness and reliability, often requiring third-party orchestration frameworks and guardrails. OpenAI aims to solve many of these problems upstream <a class="yt-timestamp" data-t="00:45:08">[00:45:08]</a>.
*   **Latency**: High latency remains a significant barrier for many use cases where users cannot wait several seconds for a response <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a>. Improving inference speed and increasing GPU availability are key objectives for 2024 <a class="yt-timestamp" data-t="00:46:23">[00:46:23]</a>.
*   **User Experience (UX)**: A fundamental challenge for ChatGPT is that users often don't know what to do next <a class="yt-timestamp" data-t="00:56:50">[00:56:50]</a>.
*   **Agents**: While there was a hype cycle for agents (e.g., AutoGPT, BabyAGI), Kilpatrick emphasizes the need for significant internet infrastructure work to authenticate humans versus AI agents to prevent misuse and ensure responsible deployment <a class="yt-timestamp" data-t="00:35:44">[00:35:44]</a>. The current environment is not ready for wide-ranging autonomous agents, and a gradual transition is necessary <a class="yt-timestamp" data-t="00:36:11">[00:36:11]</a>.
*   **Model Evals**: The process of evaluating new models is a "huge pain" <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>. Kilpatrick is excited about startups that can solve the "eval problem," as it's critical for users to know how a new model will impact their specific use case <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>. Learning often happens by examining failure points, which is hard to automate <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.

## OpenAI's Strategy and Growth

OpenAI's product footprint is vast, serving diverse users and use cases <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>. Prioritization balances clear developer demands (like API key-based usage data) with fundamental needs like reliability, which is a Northstar <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a> <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Shipping new capabilities often takes precedence due to engineering resource constraints <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. As the team grows, there will be more time to address "rough edges" like dashboards and monitoring, leading to a true Enterprise platform in 2024 <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>.

Kilpatrick notes the fascinating growth of OpenAI, describing it as an "endless amount of work" despite rapid hiring <a class="yt-timestamp" data-t="00:50:45">[00:50:45]</a>. The company has expanded from a small engineering team for the entire API to multiple specialized teams for capabilities, fine-tuning, and enterprise offerings <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>.

## General Advice for AI Adoption

For those "AI curious" but overwhelmed, Kilpatrick advises:
1.  **Identify Pain Points**: Audit your job or daily life for tasks you dislike or want to improve <a class="yt-timestamp" data-t="00:54:24">[00:54:24]</a>.
2.  **Integrate AI into Workflows**: Make using AI tools a habit by incorporating them into daily routines <a class="yt-timestamp" data-t="00:56:03">[00:56:03]</a>.
3.  **Be an Ambassador**: Share your experiences and insights with others <a class="yt-timestamp" data-t="00:54:15">[00:54:15]</a>.

Ultimately, the goal is for AI to assist users in their existing workflows, rather than requiring them to adopt new platforms <a class="yt-timestamp" data-t="00:32:01">[00:32:01]</a>. This is exemplified by [[Application in email management and coding | Microsoft's Copilot strategy]], embedding AI directly into widely used applications <a class="yt-timestamp" data-t="00:34:45">[00:34:45]</a>.