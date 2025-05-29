---
title: Using Lyzr AI for Lowcode AI Agent Development
videoId: LAjgtPENG4A
---

From: [[amiteshanand]] <br/> 

[[understanding_ai_agents | AI agents]] are software entities that autonomously perform tasks, learn, and adapt to user needs based on predefined inputs and instructions <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. While agents can be built from scratch using code with frameworks like [[building_ai_agents_with_openai_agent_sdk | OpenAI Agent SDK]], they can also be developed using low-code platforms like Lyzr AI <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a> <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## What is Lyzr AI?
Lyzr AI is an agent infrastructure platform designed for building an AI workforce <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. It allows users to build and deploy [[understanding_ai_agents | AI agents]] on their cloud or opt for self-hosting versions for on-premises deployment <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a> <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

## Key Features of Lyzr AI
Lyzr AI offers a comprehensive dashboard and features that simplify the development of [[understanding_ai_agents | AI agents]]:

*   **Pre-built Agent Hub**
    Lyzr AI includes a hub with pre-built agents for various domains like banking, sales, and marketing <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. The platform also showcases community-built and featured apps that users can utilize or adapt <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

*   **Agent Configuration Options**
    When building an agent, users can configure several parameters:
    *   **Name and Description** Define the agent's identity and purpose <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
    *   **LLM Provider and Model Selection** Choose from various LLM providers and models (e.g., Groq, Llama 3.2, OpenAI models like GPT-4, 3.5, 40) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a> <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a> <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.
    *   **Agent Role and Instructions** Clearly define the agent's role and provide structured instructions for its tasks. Lyzr AI offers an "Improve" feature to refine these instructions for better [[understanding_ai_agents | AI agent]] performance <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a> <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a> <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.

*   **Tool Integration**
    Lyzr AI enables integration with external tools like Discord, GitHub, or Perplexity AI through API keys, allowing agents to perform tasks such as posting on social media or retrieving real-time data <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a> <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a> <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>.

*   **Knowledge Base**
    Users can upload documents (PDF, DOCS, TXT) or provide website URLs to create a knowledge base that the agent uses to answer questions and perform tasks <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a> <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. This ensures answers are specific to the provided context <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. Chunking settings can be adjusted to retrieve the most relevant information <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.

*   **Memory Management**
    Lyzr AI supports:
    *   **Shorter Memory:** Retains contextual memory for the last 100 inferences <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a> <a class="yt-timestamp" data-t="00:24:29">[00:24:29]</a>.
    *   **Long-Term Memory:** For retaining context over extended periods <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.

*   **Humanizer Option**
    This feature allows users to add a human-like tone to the [[understanding_ai_agents | AI agent]]'s responses, overriding its predefined rules <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a> <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.

*   **Responsible AI Features**
    Lyzr AI includes settings for:
    *   **Context Relevance:** Maintains relevance to the conversation topic <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a> <a class="yt-timestamp" data-t="00:24:56">[00:24:56]</a>.
    *   **Groundedness:** Ensures responses are based on provided context and knowledge <a class="yt-timestamp" data-t="00:12:38">[00:12:38]</a>.
    *   **Reflection:** Enables the agent to reflect on its responses and improve accuracy <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
    *   **Safe AI:** Options to reduce potential biases (fairness and biases) and prevent toxic or harmful content (toxicity check) <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a> <a class="yt-timestamp" data-t="00:25:03">[00:25:03]</a>.
    *   **Human-in-the-Loop:** A forthcoming feature that allows human oversight to ensure accuracy and appropriateness before actions are executed <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>.

*   **API Documentation**
    For developers, Lyzr AI provides comprehensive API documentation, allowing for [[using_ai_models_for_coding_assistance | building AI agents]] from scratch using Lyzr Agent APIs and inference modules <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a> <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>. This enables users to leverage Lyzr's backend while retaining full coding control.

*   **Lyzr Academy**
    Lyzr Academy offers courses and a community space for users to learn about [[understanding_ai_agents | AI agents]] and connect with other members [[optimizing_ai_research_tools | building Lyzr agents]] <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>. Upcoming events and tutorials are also listed <a class="yt-timestamp" data-t="00:29:47">[00:29:47]</a>.

## Building an LLM Pricing Agent with Lyzr AI
To demonstrate [[building_an_aipowered_app_without_coding | building an AI-powered app without coding]], an LLM pricing agent can be created on the Lyzr AI dashboard <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a> <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.

1.  **Agent Setup:**
    *   Name the agent (e.g., "LLM Pricing Agent") and provide a description, such as "provides pricing for LLM models or provider names" <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>.
    *   Select an LLM provider (e.g., Groq) and a specific model (e.g., Llama 3.2) <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.
    *   Define the agent's role (e.g., "expert LLM pricing and provider") and detailed instructions for guiding users in comparing and selecting cost-effective LLM options <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a> <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. The "Improve" feature can refine these instructions <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
    *   Optionally, configure tools like Perplexity AI, although this step can be skipped for simplicity <a class="yt-timestamp" data-t="00:20:14">[00:20:14]</a>. Example outputs can also be provided to structure responses <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>.

2.  **Knowledge Base Creation:**
    *   Enable the knowledge base feature and create a new one (e.g., "LLM provider") <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>.
    *   Upload files (PDF, DOCS, TXT) or crawl website URLs (e.g., artificial-analysis.com) to populate the knowledge base with relevant data <a class="yt-timestamp" data-t="00:22:08">[00:22:08]</a> <a class="yt-timestamp" data-t="00:23:27">[00:23:27]</a>.
    *   Configure chunking settings, such as retrieving 10 most relevant chunks <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>.

3.  **Additional Features:**
    *   Enable shorter memory to allow the agent to retain context from recent conversations <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>.
    *   Activate Humanizer for a more human-like response tone <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.
    *   Ensure responsible [[understanding_ai_agents | AI]] options like context relevance, fairness, and toxicity checks are configured <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.

4.  **Deployment and Interaction:**
    *   Once configured, the agent can be launched as an app <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.
    *   Users can interact with the deployed agent through a simple interface, asking questions related to LLM pricing and providers. The agent will respond based on its knowledge base and instructions <a class="yt-timestamp" data-t="00:27:01">[00:27:01]</a>.

## Comparison with Code-Based Development
While Lyzr AI enables rapid [[building_an_aipowered_app_without_coding | low-code agent development]] (as quickly as 10 minutes <a class="yt-timestamp" data-t="00:29:18">[00:29:18]</a>), [[building_ai_agents_with_openai_agent_sdk | building AI agents with OpenAI Agent SDK]] or other SDKs requires coding everything from scratch <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. For example, an email-sending agent can be implemented using [[building_ai_agents_with_openai_agent_sdk | OpenAI Agent SDK]], Navius AI Studio for models, and Resend for email services, requiring manual setup of environment variables, client configuration, and defining custom tools <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. Lyzr AI abstracts much of this complexity, making it accessible for non-developers <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.