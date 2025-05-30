---
title: Agentic workflows in insurance industry
videoId: vuKCZxhD4lU
---

From: [[customaistudio]] <br/> 

## Overview
The insurance industry is a prime candidate for [[Agentic Workflows and Team Productivity | agentic workflows]] due to significant bottlenecks in quoting processes. Full-time staff traditionally spend considerable time manually filling out the same forms across multiple insurance carriers to generate quotes, a task that can take up to an hour for just two carriers [00:09:57]. This tedious work prevents staff from engaging in more valuable activities [00:14:14].

The solution proposed is to implement [[workflow_and_task_automation_using_ai_agents | AI agents]] to automate this tedious leg work, rather than replacing human staff [00:10:27]. This approach aims to streamline the process, allowing human agents to focus on client interaction and decision-making based on the compiled quotes [00:10:31].

### The "Hope" Agent Workflow

The core of this [[automating_business_processes_with_ai_agents | agentic workflow]] is an AI agent named "Hope" [00:12:52]. The system operates through a user-friendly chat interface [00:12:47].

1.  **Initial Interaction and Data Collection**:
    *   A React application, connected via Superbase's edge functions to Naden, handles the user interface [00:13:08].
    *   When a user requests a quote (e.g., "I need a quote for John Smith" <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>), Hope first identifies the customer in the agency's database (like Applied Epic CRM) [00:13:56].
    *   Hope collects existing customer information and identifies any missing details [00:14:08]. This information is displayed in a UI pane, allowing the human user to review and correct it, ensuring data accuracy [00:13:30].

2.  **Carrier Interaction with Sub-Agents**:
    *   Hope then proceeds to apply the collected information to various insurance carriers (e.g., Progressive, Safeco) [00:14:15].
    *   Crucially, the system employs "little agents" dedicated to each carrier [00:14:50]. These sub-agents interact with the respective carrier's APIs to generate quotes [00:15:21].
    *   These carrier-specific agents can navigate decision trees (e.g., asking if a client owns a boat <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>) relevant to their carrier's quoting process [00:14:37].

3.  **Human-in-the-Loop for Missing Information**:
    *   If a carrier agent encounters a missing piece of information needed for a quote, it communicates this back to Hope [00:15:00].
    *   Hope, being the sole agent directly interacting with the human user, then bubbles up the request to obtain the necessary information [00:14:45]. This ensures a seamless "human-in-the-loop" interaction for critical data points.

4.  **Quote Delivery and Integration**:
    *   Once the carrier agents retrieve the quotes, Hope brings them back to the human user [00:16:11].
    *   The human's primary role shifts to verifying the data's correctness and the quote's accuracy [00:16:05].
    *   Ultimately, the goal is for these AI-generated quotes to be populated and attached directly back into the agency's CRM, appearing as if a human had processed them [00:17:19].

### Technical Implementation

The system is built on a robust technical stack:
*   **Frontend**: Utilizes Cursor and a React application for the user interface [00:10:38]. Lovable is also used for marketing-side UI pieces [00:53:11].
*   **Backend & Database**: Superbase serves as the backend, providing database capabilities, edge functions, real-time updates, authentication, encrypted storage, and row-level security [00:10:44], [00:21:03], [00:27:37].
*   **Automation Platform**: Naden orchestrates the workflows and interactions between agents and tools [00:11:00], [00:13:16], [00:23:20].
*   **Large Language Model (LLM)**: OpenAI, specifically Chat GPD, is leveraged for AI capabilities [00:24:41], [00:28:45].
*   **Communication & Memory**: A "message bus" table within Superbase tracks all transactions and communications between Hope, the human, and carrier agents, creating a comprehensive audit trail [00:25:36], [00:26:09]. This system allows for asynchronous communication between agents, ensuring that even if a human takes two days to respond, the workflow can pick up where it left off [00:35:30].

The current prototype uses synchronous calls for proof-of-concept, but future iterations will focus on asynchronous workflows to handle delays in human responses [00:36:51].

### Compliance and Data Handling

Dealing with Personally Identifiable Information (PII) in insurance requires careful handling [00:20:41]. The system addresses this by:
*   Encrypting all data at rest within Superbase [00:21:03].
*   Implementing strict row-level security [00:21:07].
*   Ensuring that all underlying tools and platforms (Naden, Superbase, Lovable) are compliant, which accounts for 90% of the compliance requirements [00:22:44]. The remaining 10% relies on adherence to data handling guidelines by the development team [00:22:51].

### Future Vision: Human Plus AI and Marketplaces

The developers behind this project, Sanctify, believe in the thesis of "human plus AI," where humans remain essential, especially for compliance and discretionary tasks [00:33:39].

Four pillars underpin their future vision:
1.  **Marketplace**: Envisioned as a "Fiverr for humans" where AI agents are the buyers [00:38:07].
2.  **Smart Contracts & Ledger**: AI agents, with a defined budget, would seek out human experts (e.g., lawyers, certified professionals) based on their compliance certifications, historical success rates, and acceptance rates via a smart ledger [00:38:16]. This facilitates a gig-economy model for specialized human tasks, potentially reducing the need for full-time employees for every specific certification [00:52:01].
3.  **Work Distribution**: AI agents can coordinate and assign tasks to internal or external human workers based on their skills and availability [00:49:03].
4.  **Contracts**: Formalizing agreements for AI-human interactions.

This model allows AI to handle the bulk of the work, but when a task requires human discretion, creativity, or compliance sign-off, the AI can seamlessly defer to a qualified human. This prevents AI from generating purely derivative content and ensures a "human voice" in the output [00:43:17]. It also shifts the nature of human work from menial tasks to expert review and decision-making [00:41:45].

This framework leverages technologies like MCP (Multi-Agent Communication Protocol) servers, which allow various AI platforms (LaneChain, Claude, Naden) to interact with a centralized toolbox of human-facing tasks [00:32:51]. This self-discoverable tool registry enables AI agents to dynamically find and utilize human expertise as needed [00:32:53].

The concept of AI agents making purchases and transactions could significantly alter marketing and content creation, moving from human-focused persuasion to optimizing for LLM buying mechanisms [00:45:33].