---
title: Tech Stack for Local AI Applications
videoId: W5X34-QmdEQ
---

From: [[colemedin]] <br/> 
The choice between a local and managed services AI solution significantly impacts your [[tech_stack_for_managed_ai_services | tech stack]] and application directory <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. Understanding a good [[tech_stack_for_managed_ai_services | tech stack]] for local AI applications helps clarify the technologies involved <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. While there are numerous options, a suggested local [[developing_an_effective_ai_tech_stack | tech stack]] can work for most use cases <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Key Components of a Local AI Tech Stack

To ensure a sound infrastructure when [[setting_up_a_local_ai_cloud_stack | self-hosting]] an AI application, several essential components are recommended:

*   **Docker**
    Docker is crucial for guaranteeing a stable and consistent infrastructure when [[setting_up_a_local_ai_cloud_stack | self-hosting]] all components <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Large Language Model (LLM)**
    Ollama is recommended for hosting a wide variety of LLMs, such as Llama 3.1 70b <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Vector Database**
    Qdrant is a suitable choice for the vector database <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Authentication and Database**
    A self-hosted version of Supabase can be used for authentication and PostgreSQL <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. Additionally, PG Vector, an extension of PostgreSQL, can be used for RAG (Retrieval Augmented Generation) instead of Qdrant <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **No-Code Workflow Automations**
    n8n can be integrated for managing no-code workflow automations <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Caching**
    Redis is used for caching <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Considerations for Local Deployment

While [[tech_stack_for_managed_ai_services | managed services]] are quicker for proof of concepts, a local approach is often preferred when:

*   **Handling Sensitive Data**
    If the data being processed is sensitive and the application is for production, it is highly recommended to go local for nearly all components <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This prevents sensitive data from being fed into public LLMs like GPT, where it could be used for training and potentially regurgitated later <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. The same applies to databases in the cloud <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.
*   **Scaling for High User Numbers**
    For applications scaling to thousands of users, a local solution can be more cost-effective <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. The initial overhead of hosting a local LLM or RAG instance in the cloud might be higher, but managed services' free tiers make them cheaper until significant scaling occurs <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. If one has the expertise or desire to learn about [[setting_up_a_local_ai_cloud_stack | self-hosting]], going local is beneficial for scaling <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

It's important to note that a hybrid approach, combining both local and [[tech_stack_for_managed_ai_services | managed services]] for different components (e.g., self-hosting the LLM while using managed services for caching or vector databases), is also a very common and solid strategy <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. Recent advancements have made local models like Llama significantly more powerful, making local deployment an increasingly viable option <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.