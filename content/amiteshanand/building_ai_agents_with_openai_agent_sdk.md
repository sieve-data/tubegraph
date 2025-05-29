---
title: Building AI Agents with OpenAI Agent SDK
videoId: LAjgtPENG4A
---

From: [[amiteshanand]] <br/> 

This article explores how to build [[understanding_ai_agents | AI agents]], specifically focusing on development using the OpenAI Agent SDK. It also highlights the differences between [[differences_between_ai_agents_and_ai_chatbots | AI agents]] and [[differences_between_ai_agents_and_ai_chatbots | AI chatbots]], key features of agents, and demonstrates building an email-sending agent with the OpenAI Agent SDK.

## Understanding AI Agents
[[understanding_ai_agents | AI agents]] are software entities or programs designed with specific instructions to perform tasks autonomously, learning and adapting to user needs <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. They take actions and execute tasks based on predefined inputs and instructions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This contrasts with [[differences_between_ai_agents_and_ai_chatbots | AI chatbots]], which are conversational interfaces limited to predefined scripts, primarily for interaction to get information or transform data <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

### Key Components of AI Agents
[[key_features_and_applications_of_ai_agents | AI agents]] are structured around three core components:
*   **Perception:** Ability to make API calls or take data from users with additional functionalities beyond simple tasks <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Decision Making:** Utilizes an LLM model or rule-based logic to decide on actions <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   **Action:** Executes tasks, generates outputs, or allows users to download results <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

### Types of AI Agents
There are three main types of [[understanding_ai_agents | AI agents]]:
*   **Reactive Agents:** Simple, rule-based systems that perform one or two tasks based on defined input and instructions, similar to chatbots <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Deliberative Agents:** Used for planning and reasoning, such as a researcher agent that performs web searches, extracts, analyzes, and provides output <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. These can also be multimodal, using multiple LLMs for multitasking <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Hybrid Agents:** Combine aspects of both reactive and deliberative agents, capable of handling both simple and complex tasks <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

### Key Features of AI Agents
[[key_features_and_applications_of_ai_agents | AI agents]] can incorporate various features depending on their purpose:
*   **Memory:** Agents can retain context from previous conversations (chat/rag memory) to perform subsequent tasks more effectively <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Tool Calling:** Enables agents to interact with external APIs for tasks like social media posting or real-time data retrieval <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.
*   **Function Calling:** Allows agents to execute custom functions tailored to unique requirements, enhancing versatility by generating structured outputs <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
*   **Security and Human-in-Loop:** Involves human oversight for moderation, ensuring accuracy and appropriateness before actions are executed, which improves AI efficiency for complex tasks <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.

## Building AI Agents with OpenAI Agent SDK

Developers can build [[understanding_ai_agents | AI agents]] from scratch using frameworks like OpenAI Agent SDK, Podcentric, or KOI <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Other SDKs include Ano, Penteci, and Lime Chain <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This method involves coding everything from scratch <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

### Tools Used for a Demo

A demo illustrating an email-sending agent built with the OpenAI Agent SDK utilized the following tools:
*   **OpenAI Agent SDK:** The primary framework for building the agent <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.
*   **Navius AI Studio:** Used to access a variety of AI models (over 30 options) beyond those typically available directly from OpenAI, such as Meta Llama 3.1 8B <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   **Resend:** An email provider that allows programmatic email sending <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>.

### Steps to Build an Email Sending Agent

#### 1. Install Libraries
The first step involves installing necessary libraries: `openai-agents` and `resend` <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

#### 2. Set Up Environment Variables
Environment variables for Navius AI and Resend API keys must be configured <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.

#### 3. Import Required Modules
Essential modules from `asyncio` for asynchronous operations, `openai` client, and the `agents` SDK are imported <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.

#### 4. Configure Navius AI Client
To use Navius AI models with the OpenAI SDK, the base URL is set to `https://api.navius.ai/v1` and the desired model name (e.g., `meta-llama-3.1-8b-instant`) is defined <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. A custom model provider is also defined to specify the model being used with the OpenAI SDK <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>.

#### 5. Define Email Sending Tool
A custom function tool is created to send emails via Resend. This function specifies the recipient (`to`), subject (`subject`), and HTML body (`html_body`) of the email <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>.

#### 6. Create and Run the Email Agent
An agent is initialized with instructions. For the demo, the instruction was to "only respond in a human-like tone" <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>. A conversational prompt, such as "Send an email to studio1.tegmail.com with subject test email and the body demo for the video," is then given to the agent <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. The agent processes this, and if successful, sends the email <a class="yt-timestamp" data-t="00:17:59">[00:17:59]</a>.

This demonstrates how to build an [[understanding_ai_agents | AI agent]] from scratch using the OpenAI Agent SDK for a specific task like email sending, integrating with external tools and models. This approach contrasts with low-code platforms such as [[using_lyzr_ai_for_lowcode_ai_agent_development | Lyzr.ai]], which offer a more streamlined way to build and deploy agents with less coding <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>.