---
title: Embedding and production deployment of AI agents
videoId: Xifzdn7zW3A
---

From: [[colemedin]] <br/> 

[[building_ai_agents | Building Advanced AI agents]] with Retrieval Augmented Generation (RAG) is not limited to complex, custom-coded applications <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Workflow automation tools like n8n, combined with libraries such as [[understanding_ai_agents | LangChain]], enable the creation of full-blown RAG AI agents with zero lines of code <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Self-Hosting and Scalability with n8n

n8n is a workflow automation tool similar to make.com or Zapier, but it offers the significant advantage of self-hosting <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This eliminates the need to pay hundreds of dollars a month for services like Zapier <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Additionally, n8n can scale infinitely, making it suitable for production environments <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Testing and Iteration during Development

n8n simplifies [[deploying_and_testing_ai_agents_quickly | quickly testing AI agents]] by providing a chat window directly within its user interface <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. This allows for easy iteration on prompts, tools, or vector databases during the development process <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Production Considerations for AI Agents

For [[secure_deployment_of_ai_agents | building production-grade AI agents]], especially those utilizing RAG, several factors regarding memory and vector store management should be considered:

### Persistent Chat Memory
While local chat memory stored on the n8n instance is suitable for demonstrations, for production, persistent storage options are recommended <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Options include:
*   **PostgreSQL chat memory**: Utilizes a SQL table to manage conversations <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Redis**: Another option for chat memory <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

### Persistent Vector Stores
Similar to chat memory, for production environments, it is advisable to use external, persistent vector stores rather than in-memory ones <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Recommended options include:
*   **Supabase Vector Store**: Highly recommended for managing both RAG and chat memories in one place <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This helps avoid issues related to workflow ID prefixes that occur with in-memory vector stores <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.
*   **Pinecone Vector Store**: Another viable option <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Workflow Management for Data Insertion and Retrieval
When using in-memory vector stores, a technical consideration arises: the memory key is prefixed by the workflow ID to avoid collisions <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>. This means that data insertion and retrieval operations for the vector database must occur within the exact same workflow for the data to be accessible by the agent <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.

> [!NOTE] Workaround for In-Memory Vector Stores
> To handle the workflow ID prefix issue when using in-memory vector stores, a separate workflow can be used as a tool that then hooks back into the original workflow containing the AI agent. This ensures that data insertions and retrievals happen within the same workflow context <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>.

If a production vector database like Supabase is used, this particular issue is circumvented because the memory key can be defined more dynamically without being prefixed by the workflow ID <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>.

## [[building_and_deploying_custom_ai_front_ends | Embedding AI Agents]]

n8n allows for easy embedding of AI agents as chat widgets on websites <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>. By accessing the "more info" section of the chat window in n8n, an embed code can be copied and pasted directly into an HTML editor or website <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. This enables the AI agent to function as a chatbot on a website, similar to common customer service widgets <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.

Further topics such as [[configuring_ai_agents_for_cloud_deployment | configuring AI agents for cloud deployment]] and [[deploying_and_scaling_ai_agents_with_docker | deploying and scaling AI agents with Docker]] are areas for future exploration to enhance production readiness <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.