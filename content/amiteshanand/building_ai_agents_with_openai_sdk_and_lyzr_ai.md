---
title: Building AI Agents with OpenAI SDK and Lyzr AI
videoId: LAjgtPENG4A
---

From: [[amiteshanand]] <br/> 

This article explores the concept of [[introduction_to_ai_agents | AI agents]], differentiating them from chatbots, detailing their structure, types, and [[applications_and_implementation_of_ai_agents | applications]], and outlining key [[types_and_features_of_ai_agents | features]]. It also provides practical demonstrations of building [[introduction_to_ai_agents | AI agents]] using both code-based frameworks like OpenAI Agent SDK and low-code platforms such as [[using_lovable_ai_app_builder | Lyzr.ai]].

## What are AI Agents? <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>

An [[introduction_to_ai_agents | AI agent]] is a piece of software or program built with specific instructions to perform a particular task autonomously, learning and adapting to user needs <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. They take actions and perform tasks by themselves based on predefined inputs and instructions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### AI Agent vs. AI Chatbot <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>

*   **AI Chatbot:** A conversational interface that interacts with users via text or voice, often limited to predefined scripts. Examples include the ChatGPT and Gemini interfaces <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. They are typically used for tasks like uploading pictures, asking for result production, or transforming images <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **AI Agent:** A software entity designed to perform tasks autonomously, learning and adapting to user needs <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. They can take actions and perform tasks based on predefined inputs and instructions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### AI Agent Structure and Components <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>

Key components of an [[introduction_to_ai_agents | AI agent]] include:
*   **Perception:** The ability to perform API calls or take data from users with advanced capabilities beyond simple tasks <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Decision Making:** This can involve using an LLM model or rule-based logic <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Action:** Executing tasks, generating outputs, or allowing users to download results <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Types of AI Agents <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>

While there can be many types, three main types of [[types_and_features_of_ai_agents | AI agents]] are:
*   **Reactive Agents:** Simple rule-based systems that perform one or two tasks based on defined input and instructions, similar to chatbots <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.
*   **Deliberative Agents:** Used for planning and reasoning, such as an OpenAI researcher agent that performs web searches, extracts information, analyzes it with an LLM, and provides output <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. They can also be multimodal agents that use multiple LLMs for multitasking based on predefined instructions and rules <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Hybrid Agents:** A combination of both reactive and deliberative agents, capable of performing both simple and complex tasks <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Applications of AI Agents <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>

[[applications_and_implementation_of_ai_agents | AI agents]] have broad applications, including:
*   Business automation <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>
*   Visualized systems <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>
*   Autonomous systems <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>
*   Sending emails <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>
*   Assisting with coding <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>
*   Accelerating documentation generation <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>
*   Marketing tasks <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>

### Key Features of AI Agents <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>

The [[types_and_features_of_ai_agents | features of AI agents]] depend on their purpose, whether for personal or enterprise use cases <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
*   **Memory:**
    *   **Chat/Short-Term Memory:** Retains context from previous conversations, helping the agent perform subsequent tasks based on past interactions <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
    *   **Long-Term Memory:** Allows the agent to retain memory over extended periods <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
*   **Tool Calling / API Integration:** Enables [[types_and_features_of_ai_agents | AI agents]] to interact with external APIs for tasks like posting on social media or retrieving real-time data <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Custom Function Execution:** Allows agents to perform specific operations tailored to unique requirements, enhancing versatility, such as generating structured output <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.
*   **Security & Human-in-Loop:**
    *   **Human-in-Loop:** Involves human moderation and oversight to measure agent performance, ensuring accuracy and appropriateness before actions are executed <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. This feature helps improve [[types_and_features_of_ai_agents | AI agent]] efficiency for complex tasks through collaborative decision-making with human judgment <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.
    *   **Responsible AI:** Includes options like context relevance (maintaining conversation context), groundedness (answers based on provided context/knowledge), fairness and biases (reducing potential biases), and toxicity checks (preventing harmful content) <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
    *   **Reflection:** Enables agents to reflect on their responses and improve accuracy <a class="yt-timestamp" data-t="00:12:59">[00:13:05]</a>.

## Building AI Agents with OpenAI SDK (Code-based Demo) <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>

This demonstration focuses on building an email sending agent using the OpenAI Agent SDK.

### Tools Used <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>
*   **OpenAI Agent SDK:** A framework for building agentic applications <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.
*   **Navius AI Studio:** Used for obtaining various AI models to perform agentic tasks, beyond models limited to OpenAI <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   **Resend:** An email provider that allows programmatic email sending <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

### Implementation Steps <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>
1.  **Install Libraries:** Install `openai-agents` and `resend` libraries <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
2.  **Set Environment Variables:** Configure API keys for Navius and Resend <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
3.  **Import Modules:** Import essential modules for async operations, OpenAI client, and Agent SDK <a class="yt-timestamp" data-t="00:16:08">[00:16:08]</a>.
4.  **Configure Navius AI Client:** Define the base URL and the desired model (e.g., `metalama 3.18`) from Navius AI Studio, as OpenAI SDK typically uses OpenAI models only <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>.
5.  **Define Custom Model Provider:** Specify the custom model provider (e.g., `metalama 3.18`) since an external model is being used with OpenAI SDK <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.
6.  **Define Email Sending Tool:** Create a function tool to send emails via Resend, specifying parameters like recipient, subject, and HTML body <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.
7.  **Create and Run the Email Agent:**
    *   Assign a name and instructions to the agent (e.g., "only respond in hypoo").
    *   Provide a human-like conversational prompt to the agent (e.g., "Send an email to studio1.tegmail.com with subject test email at the body demo for the video") <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>.
    *   The agent processes the instruction, uses the defined email sending tool, and sends the email <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.

### Demo Result <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>
The agent successfully sent an email to the specified address with the given subject and body, confirming its functionality <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>.

## Building AI Agents with Lyzr AI (Low-code Demo) <a class="yt-timestamp" data-t="00:22:22">[00:22:22]</a>

[[using_lovable_ai_app_builder | Lyzr.ai]] is an agent infrastructure platform that allows users to build and deploy [[introduction_to_ai_agents | AI agents]] with a low-code approach <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.

### Lyzr AI Platform Features <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>
*   **Deployment Options:** Agents can be deployed on Lyzr's cloud or self-hosted for on-premises security <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
*   **Pre-built Agents Hub:** Provides existing agents for various domains like banking, sales, and marketing <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **API Documentation:** Developers can use Lyzr's API documentation and code base to build agents from scratch <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
*   **Lyzr Academy:** Offers courses related to [[introduction_to_ai_agents | AI agents]], allowing users to learn and connect with community members <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.

### Implementation Steps (LLM Pricing Agent) <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>
1.  **Create Agent:**
    *   **Name & Description:** Provide a unique name (e.g., "LLM pricing agent") and a description of its function <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
    *   **LLM Provider & Model:** Select an LLM provider (e.g., Groq) and a specific model (e.g., Lama 3.2) <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.
    *   **Agent Role & Instructions:** Define the agent's role (e.g., "an expert LLM pricing and provider") and detailed instructions on how it should assist users in comparing and selecting cost-effective LLM options <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. Lyzr's "Improve" feature can refine these instructions <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
2.  **Configure Tools:** Integrate external tools like Discord, GitHub, or Perplexity by providing API keys <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.
3.  **Knowledge Base:**
    *   Enable a knowledge base for the agent to use while answering questions <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.
    *   Create a new knowledge base (e.g., "LLM provider") with a unique name <a class="yt-timestamp" data-t="00:21:20">[00:21:20]</a>.
    *   Choose a vector store (e.g., Quadrant, Web) and embedding model (e.g., text embedding three small) <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>.
    *   Upload files (PDF, DOCS, TXT) or crawl website URLs (e.g., `artificialanalysis.com`) to provide relevant data for the agent <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a>.
    *   Set chunking parameters to retrieve relevant information from the knowledge base <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.
4.  **Memory & Humanization:**
    *   Enable short-term memory to retain contextual information from recent chats <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
    *   Enable humanizer to add a human-like tone to the agent's responses <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.
5.  **Responsible AI Features:** Enable options like context relevance, fairness and biases, and toxicity checks to ensure accurate and appropriate responses <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.
6.  **Deploy Agent:** Once configured, the agent can be launched as an app <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.

### Demo Result <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>
The agent successfully uses the provided knowledge base to answer questions about LLM pricing and providers, demonstrating its ability to compare and select cost-effective options based on the trained data <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>. If the information is not in its knowledge base, it will state that it cannot provide it <a class="yt-timestamp" data-t="00:28:36">[00:28:36]</a>.

Lyzr also provides agent JSON and inference APIs, allowing developers to integrate their low-code agents into custom applications or build agents from scratch using Lyzr's APIs <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.