---
title: Types and Features of AI Agents
videoId: LAjgtPENG4A
---

From: [[amiteshanand]] <br/> 

An [[introduction_to_ai_agents | AI agent]] is a piece of software or program designed with specific instructions to perform a particular task autonomously [00:01:10]. They can learn and adapt to user needs, taking actions and performing tasks by themselves based on predefined inputs and instructions [00:01:23].

## Difference between AI Agents and AI Chatbots

While both interact with users, there's a key [[difference_between_ai_agents_and_ai_chatbots | difference between an AI agent and an AI chatbot]] [00:00:44]:
*   **AI Chatbot**: A conversational interface that interacts with users through text or voice, often limited to predefined scripts, similar to ChatGPT or Gemini interfaces [00:00:49]. They are primarily for interaction to get information or produce results [00:01:04].
*   **AI Agent**: A software entity capable of performing tasks autonomously, learning, and adapting [00:01:21]. They take actions and execute tasks based on predefined instructions and inputs [00:01:27].

## Structure of AI Agents
[[introduction_to_ai_agents | AI agents]] are built with key components [00:01:46]:
*   **Perception**: The ability to make API calls or take data from users, going beyond simple tasks [00:01:51].
*   **Decision Making**: Utilizes an LLM (Large Language Model) or rule-based logic to make decisions [00:02:01].
*   **Action**: Performs actions such as executing tasks, generating outputs, or enabling users to download results [00:02:07].

## Types of AI Agents
There are three main types of [[introduction_to_ai_agents | AI agents]] [00:02:18]:
*   **Reactive Agents**: Simple rule-based systems, similar to chatbots, that perform one or two tasks based on defined inputs and instructions [00:02:28].
*   **Deliberative Agents**: Used for planning and reasoning, such as an Open-DP researcher that performs web searches, extracts, analyzes, and provides output [00:02:35]. They can also be multimodal, where different LLMs are used by an agent to perform various tasks, enabling multitasking based on predefined instructions and rules [00:02:51].
*   **Hybrid Agents**: A combination of both reactive and deliberative agents, capable of performing both simple and complex tasks based on their design [00:03:07].

## Applications of AI Agents
[[applications_and_implementation_of_ai_agents | AI agents]] have broad applications, including [00:03:14]:
*   Business automation [00:03:18]
*   Visualized systems [00:03:18]
*   Autonomous systems [00:03:19]
*   Sending emails based on defined rules and instructions [00:03:26]
*   Helping with coding or documentation generation for companies [00:03:56]
*   Assisting marketing teams [00:04:14]

## Key Features of AI Agents
The features an [[introduction_to_ai_agents | AI agent]] possesses depend on its purpose, whether it's for personal work or enterprise use cases [00:03:47]. Key features include:

### Memory
[[introduction_to_ai_agents | AI agents]] can have memory, such as chat-track memory, which retains context from previous conversations [00:04:29]. This allows the agent to perform subsequent tasks based on the context and memory retained from past interactions [00:04:42]. For instance, [[Building AI Agents with OpenAI SDK and Lyzr AI | Lyzr.ai]] offers short-term memory (retains context for the last 100 inferences) and long-term memory options [00:11:54].

### Tool Calling and Function Calling
*   **Tool Calling**: Enables [[introduction_to_ai_agents | AI agents]] to interact with external APIs, allowing tasks such as posting on social media platforms or retrieving real-time data [00:04:57]. This is an example of [[using_thirdparty_tools_in_ai_development | using third-party tools in AI development]] [00:05:07].
*   **Function Calling**: A similar concept to tool calling, it allows agents to perform specific operations tailored to unique requirements, enhancing versatility [00:05:13]. This can involve generating structured output and executing specific functions during a process [00:05:25].

### Security and Human-in-the-Loop
These are crucial features, particularly for ensuring reliability and control [00:05:31]:
*   **Human-in-the-Loop**: Involves human moderation and oversight to measure an agent's performance, ensuring accuracy and appropriateness before actions are executed [00:05:36]. This helps improve [[introduction_to_ai_agents | AI agent]] efficiency for complex tasks through collaborative decision-making with human judgment [00:06:05].
*   **Responsible AI Features**: Platforms like [[Building AI Agents with OpenAI SDK and Lyzr AI | Lyzr.ai]] offer features to enhance responsible AI use [00:12:27]:
    *   **Context Relevance**: Helps maintain relevance to the conversation context, preventing deviation to other topics [00:12:30].
    *   **Groundedness**: Ensures responses are accurate and grounded in the provided context and knowledge base [00:12:38].
    *   **Reflection**: Allows the agent to reflect on its responses and improve accuracy [00:12:59].
    *   **Safe AI**: Includes options to reduce potential biases (fairness and biases) and prevent toxic or harmful content (toxicity check) [00:13:05].

[[Building AI Agents with OpenAI SDK and Lyzr AI | Nebas AI Studio]] is mentioned as an LLM provider that offers over 30 models for building [[introduction_to_ai_agents | AI agents]] from scratch [00:08:38]. These models can be used with [[Building AI Agents with OpenAI SDK and Lyzr AI | OpenAI agent SDK]] or other agentic frameworks [00:08:47].