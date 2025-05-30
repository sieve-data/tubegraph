---
title: Prompt engineering and modularity in AI systems
videoId: nC25io4cYlM
---

From: [[customaistudio]] <br/> 

## Introduction to AI Agents
The concept of an executive agent plays off the idea of an executive assistant, and many individuals are [[building_efficient_ai_agents_with_prompts | building these personal agents]] and demonstrating their construction [00:00:06]. These demonstrations often involve sprawling workflows [00:00:19]. Personal agents are popular for demos because they can be directly prompted to perform a task, unlike many other agentic systems that operate autonomously in the background [00:00:30]. This direct interaction makes them easier to build and showcase [00:00:53].

## The "Mallerie" Executive Agent
Mallerie is an executive agent designed to be an extension of the user, functioning as a "second brain" [01:17:08].

### Capabilities and Data Management
Mallerie aims to create a comprehensive [[data_management_and_prompt_engineering_for_ai_agents | data sandbox]] for the agent, encompassing all data streaming into and being created by an individual or business [02:09:09]. This includes textual data and potentially images [02:27:30]. All captured data is ingested into a database, synced with a vector database, allowing the agent to perform Retrieval Augmented Generation (RAG) when needed [01:26:00]. This [[data_management_and_prompt_engineering_for_ai_agents | data capture]] is crucial for providing the agent with the necessary context to perform actions, such as sending follow-up messages or generating proposals based on prior conversations [01:44:00].

### Integrated Tech Stack
Mallerie is integrated with various tools to perform actions, including:
*   Email (sending/receiving) [02:38:00]
*   Calendar (actions, retrieving events) [02:40:00]
*   Slack (responding in channels) [02:45:00]
*   Google Drive (copying, creating, retrieving files) [02:53:00]
*   Proposal generator [02:59:00]
*   Internet search [03:03:00]

The system is designed to be interchangeable, allowing for integration with Microsoft Suite tools instead of Google's, for example [03:32:00]. Future integrations could include client portals like Co-Pilot or other platforms such as Instantly or Airtable [03:07:00].

### Tools Used in Development
The [[tools_and_resources_for_building_ai_agents | development of Mallerie]] utilizes several key tools:
*   **Airtable:** Used for configuring and managing the agent [03:40:00].
*   **n8n:** The primary platform where the agent is built and operates [03:45:00].
*   **OpenAI:** Provides the Large Language Model (LLM) [03:49:00].
*   **Pinecone:** Serves as the vector database [03:51:00].
*   **Supabase:** The central "source of truth" database for contacts and conversational data, which syncs with Pinecone [03:54:00].
*   **Tavily:** Used for internet searches, specifically built for LLMs [04:03:00].

## Super Agent Architecture: A Modular Approach
The "Super Agent Architecture" is a distinct approach to [[building_deterministic_logic_and_modular_ai_systems | building deterministic logic and modular AI systems]], differing from the sprawling, hard-to-debug workflows often seen in other AI automation agencies [04:30:00].

### Standardizing Workflows with "Playbooks"
The core concept of this architecture is to standardize almost every piece of an agentic workflow and system, with the exception of the prompting [04:58:00]. This is achieved through a "Playbook," which is essentially a collection of various prompts designed to handle different scenarios [05:12:00]. When a specific scenario is triggered, the relevant prompt is pulled from the Playbook and used by the agent to execute the task [05:22:00].

### Benefits of Modularity
This modular approach offers several advantages:
*   **Concise and Precise Prompts:** Prompts can be kept focused on specific tasks [05:35:00].
*   **Observability and Testing:** By breaking down tasks, it becomes easier to observe the agent's activity log and determine if a specific task was executed correctly [05:50:00]. This is crucial for [[importance_of_model_selection_and_testing_in_ai_systems | testing the ability and scaling capabilities]] [05:43:00].
*   **Improved Reliability:** Large, monolithic prompts that try to account for all scenarios tend to have lower reliability [06:03:00].
*   **Scalability:** The system is designed to be scalable. By integrating the agent with an entire tech stack and syncing all generated data, the agent can function as a capable "employee" of the business, understanding context and taking actions [06:23:00].

## Challenges and Future Outlook

### Prompt Engineering Nuances
A significant [[challenges_in_ai_prompt_engineering_and_development | challenge in AI prompt engineering]] is finding the "Goldilocks zone" where prompts are precise and concise, while also giving the agent the modularity and ability to pull context as needed [07:38:00]. Over-packing prompts with too much context without the ability to dynamically retrieve it decreases reliability [07:25:00]. Conversely, putting too much onus on the LLM to figure things out without sufficient prompting leads to poor output [07:17:00].

### The Human-AI Communication Gap
One of the primary [[challenges_in_developing_autonomous_ai_agents | challenges in developing autonomous AI agents]] is the communication mechanism between users and LLMs [03:07:00]. LLMs can be overly literal, leading to miscommunication where a human would understand intent, but an LLM requires very precise instructions [03:09:00]. The goal is to build scaffolding around the system to ensure user intent is accurately interpreted by the LLM [03:47:00]. One method used to address this is pairing LLMs, where one generates output and another checks it, which can significantly improve reasoning or content generation [03:02:00].

### Importance of Testing and Reliability
Live demonstrations of AI agents often reveal their "finicky" nature and the need for rigorous testing [02:23:00]. Assuming an agent will work without proper testing leads to unreliability [02:30:00]. Most AI agent videos online showcase Proofs of Concept (POCs) rather than fully production-ready systems [04:20:00].

For a system to be production-ready:
1.  **Understand Liability Points:** Identify scenarios where tasks are executed and understand where reliability might break down [04:33:00].
2.  **Add Checks:** Implement multiple checks from other LLMs or include "human-in-the-loop" interventions at critical junctures [04:42:00].
3.  **Extensive Prompt Testing:** Prompts must be manually tested repeatedly (hundreds of times) [04:50:00]. This involves analyzing the output and the steps taken, benchmarking against desired performance levels (e.g., aiming for 90%+ effectiveness) [04:56:00].
The initial stage of testing is always ensuring the underlying tooling works correctly [04:06:00].

### Future Development Road Map
The current roadmap for improving agentic systems includes:
*   **User Interaction and User Interface:** Finding the "unlock moment" for agentic systems, similar to how ChatGPT popularized LLMs by providing an accessible user interface [01:58:00].
*   **Agentic Database:** Enhancing the contextual data available to the agent for reliable and quality output [01:29:00].
*   **Improved Human-LLM Communication:** Addressing the literal interpretation by LLMs and bridging the communication gap [03:07:00].

The development of AI agent technology is emerging, with no pre-defined path. Organizations are experimenting and learning as they go, with every new piece of data helping to refine and improve precision [03:47:00]. The vision is to create a "Jarvis-like" autonomous system that can indefinitely expand its capabilities without human limitations [02:00:00].