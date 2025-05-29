---
title: Integrating multiple AI tools with Google ADK
videoId: FYhKah8FpAg
---

From: [[amiteshanand]] <br/> 

The [[building_ai_agents_with_google_adk | Google Agent Development Kit (ADK)]] is presented as a flexible and modular framework designed for developing and deploying AI agents [00:04:54]. It supports integration with popular Large Language Models (LLMs) and open-source tools, focusing on seamless interaction with the Google ecosystem and Gemini models [00:04:58]. However, it can also be integrated with other LLMs and third-party tools [00:05:15].

## Key Features and Setup
The [[features_of_google_agent_development_kit | Google ADK]] offers a multi-agent architecture, a rich tool ecosystem, and is deployment-ready with built-in evaluation capabilities [00:05:28]. Installation is straightforward using `pip install Google-ADK` [00:05:21].

## Agent-to-Agent Protocol
Google introduced an open agent-to-agent (A2A) protocol on April 9, 2025, to facilitate interaction and collaboration between agents for performing multiple tasks [00:01:47]. This protocol enables client agents and remote agents to work together securely, managing tasks, state, user experience, negotiation, and capability discovery [00:02:02]. While the Model Context Protocol (MCP) focuses on tool and resource collaboration, A2A protocol is specifically for dynamic, multimodal communication between different agents [00:03:54].

The A2A protocol supports various frameworks, including [[agent_development_kit_introduction_and_usage | Google ADK]] and other agent frameworks like LangChain or [[building_ai_agents_with_openai_agent_sdk | OpenAI Agent SDK]] [00:03:33].

## Agent Types in Google ADK
Within the [[agent_development_kit_introduction_and_usage | Agent Development Kit]], an agent is defined as a self-contained execution unit designed to act autonomously to achieve specific goals [00:06:09]. Agents can perform tasks, interact with users, utilize external tools, and coordinate with other agents [00:06:15]. Google ADK extends its base agent into three core categories:
*   **LLM-based agents:** These agents use LLMs as their core engine for understanding language, reasoning, planning, generating responses, and dynamically deciding actions [00:06:38].
*   **Workflow agents:** These specialized agents control the execution flow of other agents in predefined patterns, including sequential, parallel, or loop-based operations [00:06:51]. They may or may not use LLMs [00:07:42].
*   **Custom agents:** Created by directly extending the base agent, these allow for implementing unique operational logic, specific control flows, or specialized integrations not covered by standard types [00:06:56].

The sequential agent is a type of workflow agent that executes its sub-agents in the order they are specified [00:08:27]. An example is summarizing a web page, which requires first getting the page content before summarizing it [00:08:42].

## Demonstrating a Multi-Agent Pipeline with Google ADK
A [[sequential_agent_demo_with_google_adk | full-fledged agent demo built with Google ADK]] showcases a multi-agent AI trend analyzer, orchestrating a chain of five agents using Google ADK's sequential agent feature [00:09:42]. This pipeline integrates various LLMs and external tools.

### LLM Integration via LightLLM
Google ADK allows the use of other LLM providers through LightLLM, which enables compatibility by prefixing non-Google models with `openai` [00:10:47]. For this demo, [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI Studio]] is used for inference, specifically leveraging the LMAN demo ultra model by Nvidia [00:00:34] and Meta Llama 3.1 8B Instruct [00:00:45]. For the final analysis agent, the Nvidia Lama 3.1 253B Neotron Ultra model is utilized [00:14:40].

### Integrated External Tools
The demo utilizes several external tools to enhance agent capabilities:
*   **XA:** This tool provides search APIs and functionalities, allowing LLMs to gain better context from search results [00:00:53]. In the demo, XA is used to fetch the latest AI-related news from X (formerly Twitter) [00:10:04].
*   **DE:** Similar to XA, DE is used for specific data points [00:01:06]. In the demo, it retrieves benchmark data and specific model-related data points from the artificial analysis website [00:10:09].
*   **Firecrawl:** This tool scrapes data from various websites [00:01:17]. It offers features like scraping, crawling, mapping, extracting, and has agent and llm.txt features [00:01:22]. Firecrawl is used to scrape content from the [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI]] website [00:10:15].

### The Five-Agent Pipeline
The [[setting_up_a_sequential_agent_workflow_using_google_adk | sequential agent workflow using Google ADK]] pipeline in the demo consists of five agents:
1.  **XA Agent:** Fetches the latest updates about AI advancements from X (Twitter) using the `XA search AI` tool [00:12:51].
2.  **DE Agent:** Searches artificial analysis websites for AI benchmarks and LLM statistics using the `DE search analysis` tool [00:13:14].
3.  **Summary Agent:** Combines and formats the results from the XA and DE agents into a concise summary [00:13:30].
4.  **Firecrawl Agent:** Scrapes content from the [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI Studio]] homepage using the `Firecrawl scrap NS` tool to provide raw data [00:13:43].
5.  **Analysis Agent:** Utilizes the Nvidia Neotron Ultra model to analyze the combined summary from Agent 3 and the scraped data from Agent 4, providing insights and recommendations [00:14:10]. This agent aims to provide comparative analysis between models like OpenAI's and [[integration_of_nebius_ai_for_advanced_ai_functionalities | Nebius AI]]'s offerings [00:20:34].

The entire pipeline is orchestrated by a main sequential agent named "AI pipeline agent" [00:15:22].

## Google ADK Web UI
[[features_of_google_agent_development_kit | Google ADK]] also provides a web UI that allows users to run agents and visualize their execution flow [00:22:38]. This UI can be accessed locally, typically at `localhost:8000` [00:23:37]. It provides a visual flowchart showing how tasks are transferred between different agents, for instance, a root agent delegating tasks to a search agent [00:24:30].