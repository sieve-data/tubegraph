---
title: Handling eviction processes with chatbots
videoId: 1g0MQamOXoY
---

From: [[customaistudio]] <br/> 

This article details the process of building and deploying a chatbot designed to assist renters in navigating the eviction process in Massachusetts. The project transitioned from using Voiceflow to In8, aiming for a more robust and automated solution. <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>

## Project Overview

The core purpose of the chatbot is to provide renters with a reliable knowledge base to help them understand and manage the eviction process. <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a> The goal is to inform users so they are better prepared when seeking legal counsel, potentially getting them "80% there" before speaking with an attorney. <a class="yt-timestamp" data-t="00:14:05">[00:14:05]</a>

The development process involved setting up a [[using_vector_databases_for_chatbots | vector database]], uploading relevant data, configuring an AI agent, and testing its functionality. <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>

## Technology Stack

The project leverages several key technologies:
*   **In8:** The primary platform for building the automation and AI agent. <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>
*   **Pinecone:** Used as the [[using_vector_databases_for_chatbots | vector database]] to store and retrieve data. <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>
*   **Google Drive:** The initial source for raw data documents. <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>
*   **OpenAI:** Utilized for embedding models (Text Embedding Three Small) and the chat model (GPT-40 Omni). <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>, <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a> This showcases [[leveraging_ai_like_chatgpt_to_handle_specific_tasks | leveraging AI like ChatGPT to handle specific tasks]].

## Data Preparation and Ingestion

A crucial step involves preparing the knowledge base for the chatbot:
1.  **Document Collection:** All necessary documents related to the eviction process were downloaded. <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>
2.  **Data Structuring:** English versions of documents were extracted and converted into `.txt` files. This preprocessing is vital for achieving the best results from the [[using_vector_databases_for_chatbots | vector database]]. <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>
3.  **Automation Setup in In8:**
    *   A workflow was created to search for and download the prepared `.txt` files from Google Drive. <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>
    *   The downloaded files are then uploaded into the Pinecone [[using_vector_databases_for_chatbots | vector database]]. <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>
    *   A "loop" was implemented in the In8 workflow to process each file individually, preventing system breaks that could occur from attempting to process too much data at once. <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>, <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>

### Vector Database Configuration

The Pinecone index was named "data" and configured to use the `text-embedding-3-small` model, which must match the embedding model used by OpenAI. <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>, <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a> A namespace called "all data" was created to store all general information. <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>

> [!tip] Namespaces for Data Segmentation
> When retrieving data, specifying a namespace means the search is limited to that namespace. To allow the agent to search all data, it's currently necessary to duplicate the data in a "all data" namespace in addition to individual, segmented namespaces. <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a> This is a strategy for [[data_management_and_prompt_engineering_for_ai_agents | data management]] in [[optimizing_chatbots_with_apis_and_namespaces | optimizing chatbots with APIs and namespaces]].

## Building the AI Agent

The chatbot's core functionality resides within the [[building_efficient_ai_agents_with_prompts | AI agent]] configured in In8:
*   **Agent Type:** A "conversational agent" was chosen, suitable for dialogue-based interactions. <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>
*   **Debugging:** The "return immediate steps" option was enabled to provide step-by-step logs, aiding in troubleshooting. <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>
*   **Chat Model:** OpenAI's GPT-40 Omni was selected as the chat model. <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>
*   **Window Buffer Memory:** Set to five, providing the model with context from past messages in the conversation. <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>
*   **Vector Store Tool:** This tool connects the agent to the Pinecone database. It's configured to provide "relevant and useful answers" about navigating the eviction process. <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>, <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>

## Chatbot Functionality and Testing

The chatbot was tested with specific queries related to eviction scenarios:
*   **Query Example 1:** "I received a summons and a complaint, what should I do now?" <a class="yt-timestamp" data-t="00:12:49">[00:12:49]</a>
    *   **Response:** The chatbot provided structured steps including reading the document carefully and understanding deadlines. <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>
*   **Query Example 2:** "The document I received says I need to move out in seven days, what do I do?" <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>
    *   **Response:** The chatbot advised reviewing the notice, knowing rights, seeking legal advice, communicating with the landlord, preparing to move, documenting everything, and considering filing a court motion. <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>

### Log Analysis
The logs showed a consistent flow:
1.  The model reads the user message and existing "window buffer memory." <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>, <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>
2.  The vector store tool is triggered with the user's query. <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>, <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>
3.  The vector store model retrieves relevant information. <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>, <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>
4.  The agent's primary model processes the retrieved information and generates the final response to the user. <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>, <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>

## Future Enhancements and Challenges

While the basic chatbot functionality is established, several areas are identified for future improvement:
*   **Document Upload and Analysis:** Allowing users to upload documents for the system to read and identify the type of notice (e.g., summons, motion hearing) would be a significant enhancement. <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>
*   **Actionable Advice:** Expanding the chatbot's ability to recommend specific actions based on document types (e.g., settling, going to court, moving out, paying). <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>
*   **Personalization:** Adding features for more tailored responses. <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>
*   **Dynamic Namespace Selection:** Implementing logic for the agent to dynamically understand which part of the data a user is asking about and retrieve from the most relevant namespace. <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a> This relates to [[optimizing_chatbots_with_apis_and_namespaces | optimizing chatbots with APIs and namespaces]].
*   **Advanced Actions:** Integrating actions like providing attorney contact information from a database or sending follow-up emails after conversations to provide further assistance. <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a> This aligns with [[workflow_and_task_automation_using_ai_agents | workflow and task automation using AI agents]] and [[automating_business_processes_with_ai_agents | automating business processes with AI agents]].

> [!info] Time Consumption
> While getting a bare-bones agent running is quick (around 18 minutes for setup), the most time-consuming activity is refining the details to make the system work exceptionally well. The initial 80% of functionality is straightforward, but achieving the last 20% of perfection requires significant iteration and testing. <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a>, <a class="yt-timestamp" data-t="00:18:17">[00:18:17]</a>