---
title: Enhancing AI agents with RAG technology
videoId: 7dKQPbSXiB8
---

From: [[colemedin]] <br/> 

An [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] has been developed that can search through meeting notes or summaries and create tasks based on identified action items <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This agent utilizes a user-friendly chatbot interface <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a> and is designed to streamline task management by automating the conversion of meeting action items into organized tasks <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Building on Previous [[Retrieval augmented generation RAG in AI | RAG]] Implementation

This [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] is an extension of a previous [[retrieval_augmented_generation_rag_in_ai | RAG]] implementation demonstrated in an earlier AI agent Master Class video <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. While the prior implementation was a good starting point, it had several key flaws that are addressed in this enhanced version <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>:

*   **Intelligent [[Retrieval augmented generation RAG in AI | RAG]] Usage**
    *   **Previous Flaw:** The prior [[retrieval_augmented_generation_rag_in_ai | RAG]] implementation always performed a document search, regardless of the user's prompt, assuming all questions were about the documents <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
    *   **Current Enhancement:** The new [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] intelligently determines if it needs to search documents or can answer a question directly <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. This represents an improvement in [[improving_rag_ai_agent_accuracy | accuracy]] and efficiency.
*   **Integration with Other Tools**
    *   **Previous Flaw:** The former [[retrieval_augmented_generation_rag_in_ai | RAG]] implementation was standalone and did not interact with other tools or APIs <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   **Current Enhancement:** This new agent integrates with external APIs like Asana to create tasks <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Efficient Vector Database Loading**
    *   **Previous Flaw:** The vector database and documents were loaded into memory every time the chatbot ran, which was inefficient <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
    *   **Current Enhancement:** The vector database is now stored locally, eliminating the need to load documents repeatedly <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

## Creating a Local Vector Database

The first step in [[rag_ai_agent_development | AI agent development]] is to create and populate a local vector database <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Document Preparation
Meeting notes, including PDF and text documents, are used as the data source for the vector database <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. These are the same simulated notes used in the previous AI agents Master Class video <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Implementation Steps
1.  **Import Packages:** Necessary packages, primarily from LangChain, are imported for embedding functions, Chroma (the vector database), and document loading/chunking <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
2.  **Load Environment Variables:** Environment variables are loaded, including the directory path for the documents (defaulting to the meeting notes folder) <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
3.  **Define Document Loading Function:** A function is created using LangChain's directory loader to load all documents from the specified folder <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. This loader supports various formats like PDF, text, HTML, Markdown, and Word documents <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
4.  **Chunk Documents:** Documents are split into smaller chunks (e.g., 1,000 characters per chunk) to optimize the data returned to the Large Language Model (LLM) during a search <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
5.  **Instantiate Chroma DB:**
    *   Documents are retrieved using the defined function <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
    *   An embedding function is created using an open-source Hugging Face embedding model <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
    *   Chroma is instantiated and saved to a local `chroma_DB` folder, which contains a SQLite file and other necessary data <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

Once this script is run, the vector database is stored locally, allowing the [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] to load it without re-processing documents each time <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Integrating [[Retrieval augmented generation RAG in AI | RAG]] into the [[rag_ai_agent_development | AI Agent]]

The next step involves integrating the [[retrieval_augmented_generation_rag_in_ai | RAG]] capabilities into the existing Asana-integrated [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

### Loading the Chroma Instance
A function is created to load the previously stored Chroma instance <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This involves:
1.  Creating the same embedding function instance used during database creation <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
2.  Instantiating Chroma by pointing to the saved `chroma_DB` folder and passing the embedding function <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>.

### Defining the Document Query Tool
A new function, `query_documents`, is created as a tool for the [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]], similar to the Asana tools <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   **Docstring:** A docstring instructs the LLM on when and how to use this tool, including its arguments (the question) and expected returns (closest matching text from documents) <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   **Similarity Search:** The tool performs a similarity search on the Chroma instance, returning the top three matching documents using cosine similarity <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
*   **Formatting and Return:** The matched documents are formatted and returned <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

This `query_documents` tool gives the LLM the ability to search through meeting notes <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Finally, this new tool is added to the agent's mapping, making it part of the [[retrieval_augmented_generation_rag_in_ai_agents | AI agent's]] capabilities <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

## Demonstration and Benefits

The enhanced [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] can now be tested through a Streamlit UI <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

### Use Case: Wellness Program
1.  **Information Retrieval:** A user can ask a question about the wellness program mentioned in meeting notes, such as "What's included in the wellness program?" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. The agent intelligently uses [[retrieval_augmented_generation_rag_in_ai | RAG]] to retrieve the information, confirming that Emily proposed yoga sessions and mental health resources <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
2.  **Task Creation:** The retrieved information can then be used to create tasks in Asana <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. For example, the user can request to "create a new project in Asana called wellness program and make both of these a task" <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. The agent successfully creates the "wellness program" project in Asana with "Mental Health Resources" and "Yoga Sessions" as tasks <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

This demonstrates the agent's power to combine [[retrieval_augmented_generation_rag_in_ai | RAG]] capabilities with external tool interactions, allowing complex, multi-step requests within a single prompt <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.

### Advantages
*   **Time Saving:** Eliminates the manual process of searching through documents and transcribing action items into task management systems <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.
*   **Improved Organization:** Reduces friction in capturing action items from meetings, leading to better organization and reduced risk of neglecting tasks <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Efficiency:** Automates "grunt work," allowing users to stay efficient and minimize dropped responsibilities <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Future Enhancements
Future plans include extending this [[retrieval_augmented_generation_rag_in_ai_agents | AI agent]] to the cloud, allowing documents to be stored in services like Google Drive and the vector database to be hosted remotely, transforming it into a production application <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. This represents [[advanced_rag_implementation_techniques | advanced RAG implementation techniques]] beyond the local setup.