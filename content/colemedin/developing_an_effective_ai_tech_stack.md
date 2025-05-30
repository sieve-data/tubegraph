---
title: Developing an effective AI tech stack
videoId: wAzBl6xllzE
---

From: [[colemedin]] <br/> 

An essential skill to cultivate in the rapidly evolving AI landscape is understanding and managing your [[tech_stack_for_managed_ai_services | AI Tech Stack]] <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. This involves identifying and leveraging a collection of tools and services that integrate to solve real-world problems <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

## Capabilities Over Tools
When approaching AI development, it is crucial to prioritize "capabilities not tools" <a class="yt-timestamp" data-t="02:39:53">[02:39:53]</a>. This philosophy, emphasized by a VP with multiple PhDs in deep learning and machine learning, suggests focusing on higher-leverage skills rather than mastering disparate, low-leverage tools <a class="yt-timestamp" data-t="03:02:05">[03:02:05]</a>. While learning specific tools is still necessary, the goal is to understand what AI can *do* (its capabilities) rather than getting bogged down in the intricacies of specific tools that may quickly become irrelevant <a class="yt-timestamp" data-t="03:22:25">[03:22:25]</a>. This is especially true given the constant emergence of new AI coding assistants, large language models (LLMs), and [[frameworks_and_tools_for_ai_agent_development | AI agent frameworks]] <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.

> "Focus on capabilities, not tools" <a class="yt-timestamp" data-t="02:39:53">[02:39:53]</a>
> This means focusing on the bigger picture, higher-leverage skills instead of a bunch of disparate, low-leverage skills <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>.

For instance, spending weeks mastering advanced C++ topics proved to be a waste of time, whereas learning deep learning and machine learning principles (like how models work and how to interact with AI in any language) was highly valuable due to its high-leverage nature <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.

## Components of an AI Tech Stack
An [[tech_stack_for_managed_ai_services | AI Tech Stack]] typically includes various categories:
*   LLM <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>
*   Hosting <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>
*   Database <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>
*   Knowledge Engines (for Retrieval Augmented Generation - RAG) <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>
*   Cloud Providers <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>

Online resources, often in the form of diagrams, provide numerous options for each category, serving as a starting point for research <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

## Choosing Your Tech Stack
When selecting components for your [[tech_stack_for_managed_ai_services | AI Tech Stack]], it's important to:
*   **Not overthink it**: Adhere to the "Keep it Simple, Stupid" (KISS) principle <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.
*   **Engineer for simplicity and reuse**: Follow the "Don't Repeat Yourself" (DRY) principle by choosing technologies that can be used across multiple use cases <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.

### Local vs. Cloud LLMs
The most significant decision in [[tech_stack_for_managed_ai_services | AI Tech Stack]] development is whether to adopt a [[tech_stack_for_local_ai_applications | local LLM setup]] or a cloud-based approach <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. While closed LLMs like Claude and GPT currently outperform [[tech_stack_for_local_ai_applications | local LLMs]], the performance gap is rapidly diminishing <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

**Advantages of Local LLMs**:
*   **Fine-tuning**: Ability to train models on your specific data for better performance on your use case <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.
*   **Data Privacy**: Utmost control as the LLM runs on your own infrastructure <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
*   **Cost**: Often more cost-effective as you pay for hardware/hosting instead of API costs <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.
*   **Speed**: Can be faster due to the absence of network delays <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **Flexibility**: More available options compared to closed LLMs <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

After deciding between local or cloud, you can research and test different services for each category (e.g., using a quick Proof of Concept) to find what works best for your needs <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.

## Example AI Tech Stack
An example of an [[tech_stack_for_managed_ai_services | AI Tech Stack]] includes:
*   **Large Language Models**:
    *   DeepSeek V3 <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>
    *   Qwen <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>
    *   Llama <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a> (for local use)
    *   Gemini 2.0 Flash <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>
    *   Claude Haiku <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a> (for fast/cheap cloud models)
    *   GPT-4 <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a> (for advanced reasoning)
*   **Languages**: Python, JavaScript, with Go being considered <a class="yt-timestamp" data-t="00:21:12">[00:21:12]</a>.
*   **AI Coding Assistants**: Bolt.DIY, Windsurf, Cursor <a class="yt-timestamp" data-t="00:21:19">[00:21:19]</a>.
*   **AI Agent Frameworks**: Pydantic-AI, LangGraph, and Flowise for prototyping <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
*   **Database**: Supabase (utilizing Postgres with PGVector for RAG) <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.
*   **Automations**: Voiceflow, n8n <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.
*   **Containerization**: Docker <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>.
*   **Hosting**: DigitalOcean (general purpose), RunPod (for cloud machines running LLMs) <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
*   **Development & Testing**: Playwright, Pytest, Pydantic-AI, CodiumCover <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.
*   **CI/CD**: GitHub Actions <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>.
*   **LLM Evaluation**: Custom agents using Bolt.DIY, Ragas, Phoenix <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>.
*   **Search**: Brave, Firecrawl, Perplexity AI, SearchOne API <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>.

## Integrating with High-Leverage Skills
The [[tech_stack_for_managed_ai_services | AI Tech Stack]] enables the implementation of other critical skills:
*   **Working with LLMs**: Prompt engineering techniques like single-shot, multi-shot, and Chain of Thought prompting are high-leverage and universally applicable across various LLMs <a class="yt-timestamp" data-t="02:39:50">[02:39:50]</a>.
*   **AI Coding Assistants**: Learning to use AI coding assistants is vital as they represent the future of development, allowing even non-technical users to build applications <a class="yt-timestamp" data-t="02:41:48">[02:41:48]</a>.
*   **Human-in-the-Loop**: As [[frameworks_and_tools_for_ai_agent_development | AI agents]] become more capable, understanding how to integrate human approval for certain actions is crucial <a class="yt-timestamp" data-t="02:44:50">[02:44:50]</a>. Tools like LangGraph facilitate this complex interaction <a class="yt-timestamp" data-t="02:49:58">[02:49:58]</a>.
*   **Massive Context Windows**: With models like Gemini supporting millions of words in prompts, leveraging these expanded context windows opens new paradigms for interacting with LLMs <a class="yt-timestamp" data-t="02:51:50">[02:51:50]</a>.

Ultimately, having a well-defined and flexible [[tech_stack_for_managed_ai_services | AI Tech Stack]] facilitates the practical application of these high-leverage AI skills and contributes to a robust [[creating_a_robust_ai_agent_development_environment | AI agent development environment]] <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.