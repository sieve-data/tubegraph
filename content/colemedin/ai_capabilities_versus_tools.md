---
title: AI capabilities versus tools
videoId: wAzBl6xllzE
---

From: [[colemedin]] <br/> 

As 2025 approaches, the field of artificial intelligence continues its rapid acceleration, showing no signs of slowing down <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This relentless pace can be overwhelming, making it challenging to determine what to focus on, whether you're a non-technical individual, a developer, or a business owner <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. New [[ai_coding_assistants_and_their_productivity_benefits | AI coding assistants]], large language models (LLMs), and [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agent frameworks]] are released almost weekly <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>, leading to concerns about the relevance of learned skills in the near future <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## The Fundamental Mindset: Capabilities, Not Tools

To navigate this landscape, a crucial mindset shift is required: focusing on **capabilities, not tools** <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This philosophy, advocated by an intelligent VP with multiple PhDs and patents in deep learning, machine learning, and generative AI, emphasizes focusing on higher-leverage, bigger-picture skills rather than a multitude of disparate, low-leverage ones <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.

The core idea is to concentrate on "what can I do with AI?" rather than "how can I work with these specific tools to do things with AI?" <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. While AI can already perform tasks like coding and creating animations <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>, the tools used for these tasks are constantly being replaced <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. Investing significant time into mastering a tool that might become irrelevant in a month is not worthwhile <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. This principle is especially true in the age of AI, where higher-leverage skills ensure relevance amidst rapid industry changes <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

It's important to note that learning specific tools remains vital for implementation; one must still choose an LLM, an agent framework, or an automation tool <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. However, the priority should not be mastering these tools, but rather understanding the broader capabilities they enable <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>.

### A Personal Illustration

The speaker recounts a personal experience that highlights this point. Before college, they chose to spend weeks diving into advanced C++ topics like static polymorphism and inheritance structures <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This proved to be a waste of time, as C++ is no longer used, and the technical depth was unnecessary <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. In contrast, the following summer, they focused on high-leverage skills in deep learning and machine learning, learning how models function and how to work with AI across any language, rather than focusing on specific frameworks like TensorFlow or Keras <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This capability-focused approach proved to be "super valuable stuff" <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

## High-Leverage Skills to Focus On in AI

Several high-leverage skills align with the "capabilities, not tools" philosophy and are crucial for success in AI going into 2025:

### AI Agents
[[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]] are projected to be a major focus for 2025, with large companies like Microsoft, LangChain, Nvidia, Anthropic, and OpenAI identifying them as the future of AI <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>. Innovations in 2024, such as establishing best practices in architecture and creating powerful LLMs capable of complex agentic workflows, have laid the groundwork <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.

Focusing on capabilities for agents means diving into:
*   [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | Agent architecture best practices]] <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
*   Understanding when to build an agent yourself versus using a platform like OpenAI Assistants <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>

These skills are high-leverage and agnostic to the specific framework or tool used <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. While tools like CrewAI, Pydantic, or n8n are good to learn, they should not be the primary focus <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

Anthropic's December 19th article on "building effective agents" is highlighted as a key resource for understanding different architectures and best practices <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. It covers fundamental concepts like knowledge bases, retrieval tools, chat memory, and advanced architectures such as prompt chaining, routing, parallelization, orchestration workers (master agents), and evaluators (important for reducing hallucinations) <a class="yt-timestamp" data-t="00:09:22">[00:09:22]</a>.

### Reasoning LLMs
Reasoning LLMs are considered the second most important area of focus <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>. These models, also referred to by terms like "Chain of Thought" or "inference time compute," can reason with themselves about a prompt before providing a final answer <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.

Examples of reasoning LLMs include:
*   03 and 01 by OpenAI <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>
*   QWQ open-source model from Quen <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>
*   Gemini 2.0 Flash <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>

They are powerful because they address significant problems in generative AI: hallucinations and poor decision-making by LLMs acting as agents <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. The future involves combining reasoning LLMs with smaller, faster LLMs for strong and efficient agentic workflows <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>, and incorporating domain-specific LLMs into these architectures <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

Practically, the skill to invest in is learning how to prompt and work with these reasoning LLMs, as their behavior differs from normal LLMs due to their chain of thought process <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. This includes understanding how to efficiently use them as agents and integrate them into [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | agent architectures]] <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.

### Local Large Language Models
Understanding and working with local LLMs is a distinct skill set <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>. This involves comprehending hardware requirements, fine-tuning models on personal datasets, and knowing when to use them over cloud-based LLMs <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. While closed LLMs like Claude and GPT are currently superior, the gap with local models (e.g., Quen, Llama, Deep Seek V3) is rapidly closing <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

Advantages of local LLMs include:
*   **Fine-tuning:** Ability to train models on specific data for better performance on a use case <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.
*   **Utmost data privacy:** Running on one's own infrastructure <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
*   **Better cost:** Often cheaper due to no API costs <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>.
*   **Speed:** Potentially faster with good hardware due to no network delays <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>.
*   **Flexibility:** More open-source options available from platforms like Hugging Face or Ollama <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.

### Finding Your [[ai_development_tools | AI Tech Stack]]
To leverage AI capabilities, it's necessary to build an [[ai_development_tools | AI Tech Stack]] – a collection of tools and services combined to create a system <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>. While this involves tools, the "capabilities over tools" principle still applies by aiming for simplicity and reuse.

Resources, often found as diagrams online, categorize different components of an [[ai_development_tools | AI Tech Stack]] (LLM, hosting, database, etc.) and provide options for each <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. The key is to find what works for your needs and stick with it, avoiding extensive research into every service <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. The "Keep It Simple, Stupid" (KISS) and "Don't Repeat Yourself" (DRY) principles are important here <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>. The biggest decision in building an [[ai_development_tools | AI Tech Stack]] is whether to go local (hosting models and infrastructure yourself) or use cloud services <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.

The speaker's personal [[ai_development_tools | AI Tech Stack]] as of late 2024 / early 2025 includes:
*   **LLMs:** Deep Seek V3, Quen, Llama (local), Gemini 2.0 Flash, Claude Haiku (cloud), 01 (advanced reasoning) <a class="yt-timestamp" data-t="00:20:44">[00:20:44]</a>.
*   **Languages:** Python and JavaScript <a class="yt-timestamp" data-t="00:21:13">[00:21:13]</a>.
*   **[[ai_coding_assistants_and_their_productivity_benefits | AI Coding Assistants]]:** [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]], Wind Surf, Cursor <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.
*   **[[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI Agent Frameworks]]:** [[integration_of_mcp_in_ai_tools | Pydantic AI]], LangGraph, Flowise (prototyping) <a class="yt-timestamp" data-t="00:21:26">[00:21:26]</a>.
*   **Database:** Supabase (PostgreSQL with PGVector for RAG) <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.
*   **Automations:** Voiceflow, n8n <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.
*   **Containerization:** Docker <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>.
*   **Hosting:** Digital Ocean (general purpose), RunPod (LLM machines) <a class="yt-timestamp" data-t="00:22:06">[00:22:06]</a>.
*   **Development/Testing:** Playwright, Pytest, [[integration_of_mcp_in_ai_tools | Pydantic AI]], Codo Cover <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.
*   **CI/CD:** GitHub Actions <a class="yt-timestamp" data-t="00:22:32">[00:22:32]</a>.
*   **LLM Evaluation:** Custom agents with [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]], Ragos (for RAG pipelines), Phoenix (for agent tool calling) <a class="yt-timestamp" data-t="00:22:38">[00:22:38]</a>.
*   **Search:** Brave, Firecall, Perplexity, Search One API <a class="yt-timestamp" data-t="00:23:12">[00:23:12]</a>.

This stack is dynamic and subject to change <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>.

### Working with Large Language Models
Mastering how to work with LLMs is a high-leverage skill, encompassing:
*   **Prompt Engineering:** Learning techniques like single-shot, multi-shot, and Chain of Thought prompting <a class="yt-timestamp" data-t="00:23:48">[00:23:48]</a>. While specific prompting for one LLM is low-leverage, understanding overarching techniques is crucial <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>.
*   **Working with [[ai_coding_assistants_and_their_productivity_benefits | AI Coding Assistants]]:** Leveraging tools like [[ai_coding_assistants_like_bolt_and_their_limitations | Bolt.DIY]] and AI IDEs like Wind Surf and Cursor to enhance programming productivity <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>.
*   **Human-in-the-loop:** As [[ai_agents_and_tool_integration_for_effective_knowledge_retrieval | AI agents]] become more capable, enabling human approval for certain actions will be vital <a class="yt-timestamp" data-t="00:24:45">[00:24:45]</a>. Tools like LangGraph facilitate this complex interaction <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.
*   **Leveraging Massive Context Windows:** Models like Gemini already allow millions of words in prompts, and this capability will become more widespread in 2025 <a class="yt-timestamp" data-t="00:25:16">[00:25:16]</a>. Learning how to take advantage of such extensive context is a new paradigm for working with LLMs <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.

## The Importance of Community
Beyond specific skills, finding an [[future_work_and_feature_requests_for_ai_tools | AI Community]] is equally important for learning and growth <a class="yt-timestamp" data-t="00:27:03">[00:27:03]</a>. The "network is your net worth" saying applies to AI, emphasizing the value of collective learning and support <a class="yt-timestamp" data-t="00:27:12">[00:27:12]</a>. Engaging with others in a community ensures continuous mastery of high-leverage capabilities <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.