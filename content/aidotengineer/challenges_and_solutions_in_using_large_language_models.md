---
title: Challenges and solutions in using large language models
videoId: 0vBKv9yAQi4
---

From: [[aidotengineer]] <br/> 

## Introduction to Conversational AI and Sierra

Sierra is a conversational AI platform designed for businesses, broadening its reach from primarily chat experiences and customer service to include phone interactions, sales, subscription management, and product recommendations <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. Sierra aims to help businesses build and improve AI agents that interact with customers across various touchpoints <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Evolution of AI and the "AI Caves"

The current pace of AI development is rapid, with significant advancements occurring even within the last few years <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Reflecting on earlier periods, 2016 felt like the "AI caves" where the focus was on helping computers distinguish between objects like Chihuahuas and blueberry muffins, or dogs and bagels/mops/fried chicken <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This work led to the first version of Google Lens <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.

Early challenges with models like Google Lens involved inconsistency; sometimes it was accurate, sometimes it wasn't, feeling like a "slot machine" <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This highlights the non-determinism of inputs and outputs, which remains a characteristic of building with AI <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. Present-day Google Lens demonstrates mind-blowing capabilities, achieved through consistent, step-by-step iteration over a decade <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

Looking back further to 2012, early breakthroughs like Google Brain identifying cat videos on YouTube involved models with about a billion parameters, a significant achievement then compared to today's frontier models of a trillion parameters <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

## Challenges in Utilizing Large Language Models

The core challenge in building with large language models (LLMs) is that they are like "building on top of a foundation of jello" <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>. Unlike traditional software which is deterministic, fast, cheap, rigid, and governed by 'if statements,' LLMs possess distinct characteristics:
*   **Non-deterministic**: Outputs can vary even with the same inputs <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Slow and Expensive**: Running LLMs can be computationally intensive and costly <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Flexible and Creative**: They can reason through problems <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
*   **Unpredictable**: LLMs remind us of ourselves in their unpredictability <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.
*   **Limitations**: They can be slow and "not that great at math" <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.

The rapid pace of advancement in the AI space means that models are constantly being upgraded, and new paradigms like reasoning models and multimodality emerge, requiring continuous adaptation <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.

One specific area of `[[challenges_in_building_ai_voice_agents | challenges in building AI voice agents]]` involves handling latency, tone, and phrasing in multimodal models <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. Building robust voice agents goes beyond simply wiring components together; it requires considering how a human would perform under similar conditions (e.g., receiving transcribed text with delay and having to respond immediately) <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.

## Solutions: Sierra's Agent Development Life Cycle (ADLC)

To address these challenges, Sierra developed the Agent Development Life Cycle (ADLC), a process for building and improving AI agents that borrows from the traditional Software Development Life Cycle (SDLC) but invents new concepts where necessary <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

### Core Principles of ADLC

*   **Agents as Products**: Sierra believes every agent is a product, requiring a fully featured developer platform and customer experience operations platform <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. This allows for continuous improvement similar to mobile apps or websites <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.
*   **Iterative Refinement**: The ADLC emphasizes iterative refinement with customers in production to maximize productivity and robustness <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

### Key Components of ADLC

1.  **Quality Assurance (QA)**:
    *   **Experience Manager**: Customers have access to Sierra's Experience Manager, allowing them to review every conversation and high-level performance reports of the agent in real-time <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>.
    *   **Feedback Loop**: Users can provide feedback on issues (e.g., incorrect inventory information), which leads to an issue being filed <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
    *   **Test Creation and Release**: Each issue leads to a test being created. Once the test passes, a new release can be deployed <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. This process allows agents to accumulate hundreds, then thousands, of tests over time, leading to significant improvement <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
    *   **Opportunities for Delight**: Beyond fixing mistakes, the system identifies opportunities for agents to go "above and beyond" to delight customers <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

2.  **AI in the Life Cycle**: While initially manual, Sierra is now integrating AI into each part of the ADLC to speed up improvements <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

3.  **Scalability**: The ADLC becomes more effective for larger customers, where velocity and change management are crucial for handling tens of millions of requests <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

4.  **Leveraging Reasoning Models**: Reasoning models act as a "force multiplier" within the ADLC, making AI application more effective in development, testing, and QA <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.

### Responsive AI Agents and Empathy in Design

Sierra's approach to voice agents is analogous to responsive web design, where a single underlying platform and agent code can adapt to different channels (chat, voice) and modalities <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>. This allows for channel-specific customization (e.g., phrasing, parallelizing requests for lower latency) while maintaining core functionality <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>.

A key aspect of building with AI is developing empathy for large language models, understanding their unpredictable, slow, and mathematically challenged nature <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>. This empathy allows designers to better understand what it means to build a good experience for these agents <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. The goal is to create robust and rich experiences by providing LLMs with similar inputs and experiences that humans have <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

## Case Studies

*   **Chubbies**: Partnered with Sierra to deploy an AI agent named Duncan Smothers. Duncan helps customers with sizing, inventory tracking, package tracking, and refunds, demonstrating the agent's capability to take autonomous actions beyond just answering questions <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>. This resulted in helping more customers more quickly with higher satisfaction <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.
*   **SiriusXM**: A large customer benefiting from Sierra's voice capabilities, enabling them to answer customer calls immediately <a class="yt-timestamp" data-t="00:15:36">[00:15:36]</a>.