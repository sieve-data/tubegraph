---
title: Integrating AI agents with Asana for task creation
videoId: 7dKQPbSXiB8
---

From: [[colemedin]] <br/> 

This article details how to [[building_an_ai_agent_for_task_management | build an AI agent]] capable of searching meeting notes and summaries to create tasks in Asana based on identified action items <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This system aims to keep tasks organized and save significant time, especially since many tasks originate from meetings <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Enhancements to AI Agent Implementation

This AI agent is an extension of a previous RAG (Retrieval Augmented Generation) implementation, addressing several key flaws <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>:

*   **Intelligent RAG Determination:** The previous RAG implementation always used RAG, regardless of the user prompt, assuming a question about documents <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. The enhanced agent intelligently determines if it needs to search documents or if it can answer directly <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **External API Integration:** The prior RAG was limited to document retrieval <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This new agent integrates with external APIs, such as [[integration_with_asana_for_project_organization | Asana]], to perform actions like task creation <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Local Vector Database Storage:** Previously, the vector database and documents were loaded into memory every time the chatbot ran, which was inefficient <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The improved approach stores the vector database locally, eliminating the need to reload documents with each script run <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Building the Local Vector Database

The first step in creating this powerful [[building_an_ai_agent_for_task_management | AI agent]] is to create and load a local vector database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Document Preparation
Meeting notes, including PDF and text documents (generated using GPT for testing), are used as source material <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. These are the same notes used in previous RAG introduction videos <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Database Creation Process
LangChain packages are utilized for embedding functions, Chroma (the vector database), document loading, and chunking <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

1.  **Load Environment Variables:** Defines the directory for loading documents, defaulting to a "meeting notes" folder <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
2.  **Load Documents:** A function uses LangChain's directory loader to load all documents from the specified folder <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   The directory loader supports PDF, text, HTML, Markdown, and Word documents <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. LangChain also offers custom loaders for other file formats <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
3.  **Split Documents into Chunks:** Documents are split into manageable chunks, typically 1,000 characters per chunk, to avoid returning entire documents to the large language model <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
4.  **Create and Save Vector Database:** An open-source Hugging Face embedding model is used to create the embedding function <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. Chroma is then instantiated and saved to a local "chroma DB" folder, containing a SQL light file and other data <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. Once this script is run, the [[building_an_ai_agent_for_task_management | AI agent]] can load this pre-populated Chroma DB instance efficiently <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Integrating RAG into the AI Agent

The [[building_an_ai_agent_for_task_management | AI agent]] is enhanced with RAG capabilities, allowing it to search documents in addition to [[implementing_ai_agents_to_interact_with_asana | interacting with Asana]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

1.  **Loading Chroma Instance:** A function loads the Chroma instance from the locally saved "chroma DB" folder <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. It reuses the same embedding model used during document loading <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. This eliminates the need to reload documents <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
2.  **Creating a Document Query Tool:** A new tool function is created to query documents <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
    *   This tool uses a doc string to inform the large language model (LLM) on how and when to use it, including expected arguments (e.g., "question") <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
    *   It performs a similarity search using the Chroma instance, returning the top three matching documents based on cosine similarity <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
3.  **Adding Tool to AI Agent:** This document query tool is added to the agent's existing tool mapping, dynamically integrating it into the [[building_an_ai_agent_for_task_management | AI agent's]] [[capabilities_of_ai_in_task_creation_and_management | capabilities]] <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Demonstration and Benefits

The [[building_an_ai_agent_for_task_management | AI agent]] can be interacted with via a Streamlit UI <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Use Case: Wellness Program Task Creation
The agent can answer specific questions about meeting notes, such as details on a "wellness program" proposed by Emily <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. It can retrieve information like "yoga sessions and Mental Health Resources" <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

Building on this, the agent can then be instructed to:
*   Create a new project in [[integration_with_asana_for_project_organization | Asana]] called "Wellness Program" <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.
*   Make "yoga sessions" and "Mental Health Resources" tasks within that project <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.

This demonstrates the powerful connection where information retrieved via RAG can directly drive task creation in [[integration_with_asana_for_project_organization | Asana]] <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. The entire process can even be condensed into a single prompt <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

Upon verification in Asana, a new "Wellness Program" project is created with "Mental Health Resources" and "Yoga Sessions" as tasks, both defaulted to due today <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Benefits of the AI Agent
*   **Time Savings:** Eliminates the need to manually search documents for action items and copy them into a task management system like Asana <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Increased Organization:** Reduces the friction of reviewing meeting notes for action items, leading to better task organization and fewer overlooked items <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   **Efficiency:** Automates "grunt work," allowing individuals to focus on higher-value activities <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Future Extensions

Future developments plan to extend this [[building_an_ai_agent_for_task_management | AI agent]] into the cloud, enabling documents to reside in [[integrating_ai_agents_with_services_like_slack_and_google_drive | Google Drive]] and the vector database to be hosted remotely, creating a production-ready application <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.