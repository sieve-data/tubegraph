---
title: Evolution and limitations of AI models
videoId: U3MVU6JpocU
---

From: [[aidotengineer]] <br/> 

The field of Artificial Intelligence (AI) has seen rapid transformation, with significant advancements in model capabilities alongside persistent challenges and evolving limitations <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Understanding the [[History and Evolution of AI|evolution of AI]] models involves examining both their progress and the inherent constraints that continue to shape their development.

## Early AI Models and Initial Limitations
In 2023, many AI applications were characterized as "AI wrappers," leading to arguments about their lack of a defensible strategy <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Despite these initial perceptions, the rapid adoption of AI, particularly in areas like coding, demonstrated a clear path for disruption by these models <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

However, [[Challenges with early AI models and improvements|early AI models]] faced significant [[Limitations of current AI models in software engineering|limitations of current AI models in software engineering]] regarding their performance:
*   **Hallucinations** remain a concern <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   **Overfitting** continues to be a problem <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   Developers required more **structured outputs** from models <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

For years, making models larger and feeding them more data consistently improved their intelligence <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. However, this approach eventually "hit a wall," with improvements slowing down as models reached their [[scaling AI models and their impact on development tools|limits on existing tasks]], regardless of additional data <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. Big jumps in performance, similar to the leap between GPT-3.5 and GPT-4, began to slow down <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## Advancements in AI Model Technology
Recent [[Advancements in AI model technology and performance|advancements in AI model technology]] have pushed the field forward through new training methods:
*   **Real Reinforcement Learning**: Models like DeepSeek R1 have been trained without labeled data, learning autonomously <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. OpenAI reportedly uses this method for their reasoning models like 01 and 03 <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Chain of Thought**: Reasoning models now employ Chain of Thought thinking at inference time, allowing them to "think" before generating answers, which helps solve complex reasoning problems <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Expanded Capabilities**: Model providers are enhancing models with capabilities such as advanced tool use, research functionalities, and near-perfect OCR accuracy (e.g., Gemini 2.0 Flash) <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.

## Challenges in Testing and Evaluation
Despite these advancements, traditional benchmarks for [[Testing and evaluation of AI models|testing and evaluation of AI models]] have become saturated <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. New benchmarks are being introduced to capture the performance of reasoning models, such as the Humanities last exam, which measures performance on truly difficult tasks <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. Even the latest smart models still struggle with these complex challenges <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

## Beyond Model Performance: Orchestration and Techniques
Success in AI products now relies less on the models alone and more on how systems are built around them <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This has led to the [[Evolution of AI engineering and tools|evolution of AI engineering and tools]] and new techniques:
*   **Advanced Prompting**: Techniques like Chain of Thought for better model interactions <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Retrieval Augmented Generation (RAG)**: Important for grounding model responses with proprietary data <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Memory**: Crucial for multi-threaded conversations to maintain context <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Long Context Windows**: Enabled new use cases <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Graph RAG**: For hierarchical responses <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   **Agentic RAG**: To make workflows more powerful and autonomous <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

The process of [[Challenges with current AI implementation|building reliable AI agents]] heavily emphasizes a [[Test Driven Development for AI|test-driven development approach]] to identify the optimal combination of techniques, models, and logic for specific use cases <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.

## Current Limitations of Advanced Agentic AI
While AI is moving towards more autonomous agents, a "fully creative workflow" (L4) where AI acts as an "inventor" and creates its own new workflows or utilities is currently "out of reach" <a class="yt-timestamp" data-t="00:20:08">[00:20:08]</a>. This is due to existing model constraints:
*   **Overfitting**: Models tend to stick closely to their training data <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.
*   **Inductive Bias**: Models make assumptions based on their training data, which can limit their ability to innovate in novel ways <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>.

The goal remains AI that can invent, improve, and solve problems in ways not previously conceived <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. While there is significant innovation happening in less advanced agentic levels (L1 and L2), L3 and L4 are still constrained by current model capabilities and surrounding logic <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>.