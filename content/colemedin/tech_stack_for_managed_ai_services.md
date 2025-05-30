---
title: Tech Stack for Managed AI Services
videoId: W5X34-QmdEQ
---

From: [[colemedin]] <br/> 

When developing AI agents, solutions can be built using either local self-hosted options or managed services <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. Managed services are cloud-based offerings that handle the infrastructure and maintenance of AI components, allowing developers to focus more on the application logic <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>. The choice between managed and local services significantly impacts an application's [[developing_an_effective_ai_tech_stack | tech stack]] and overall direction <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.

## Components of a Managed AI Tech Stack

A typical [[developing_an_effective_ai_tech_stack | tech stack]] for managed AI services includes:

*   **Large Language Model (LLM)**: Options such as Claude, GPT, or Grok <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>. The choice depends on the specific use case <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>.
*   **Vector Database**: Services like Pinecone or Qdrant can be used <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.
*   **Authentication and Postgres**: A hosted version of Supabase provides these functionalities. PG Vector can also be used as a PostgreSQL extension for RAG (Retrieval Augmented Generation) instead of a dedicated vector database <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>.
*   **No-code workflow automations**: Cloud n8n is suitable for managing these <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
*   **Caching**: Redis.io offers hosted Redis caching <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

Many components in a managed services [[developing_an_effective_ai_tech_stack | tech stack]] may share similar names or functions with those in a [[tech_stack_for_local_ai_applications | local AI tech stack]], which can facilitate migration if a project scales from a proof of concept to a production application <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

## When to Choose Managed AI Services

Managed services are often the preferred choice in several scenarios, guiding the [[choosing_cloud_providers_for_local_ai_deployment | decision-making process for AI solutions]]:

*   **Proof of Concept (POC)**:
    *   Managed services enable much quicker setup and deployment for preliminary builds <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.
    *   This allows for rapid iteration and the ability to quickly discard a concept if it doesn't meet business needs, avoiding time wasted on local setup <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>.
    *   Even with sensitive data, POCs can be built by mocking data or removing sensitive elements for testing <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.
    *   Similarities in [[developing_an_effective_ai_tech_stack | tech stack]] between managed and local options make it easier to start with a managed POC and migrate to a local production application later <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.
*   **Need for Latest Technology**:
    *   If an application requires the most powerful LLMs (e.g., Claude 3.5 Sonnet, GPT-4) to handle complex user requests, advanced tool calling, or specific structured output requirements, managed services are typically necessary <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a>.
    *   The computational resources needed for these advanced models are often too intense to run locally <a class="yt-timestamp" data-t="07:04:00">[07:04:00]</a>.
*   **Limited Scaling Requirements**:
    *   For applications not expected to scale to thousands of users, managed services can initially be more cost-effective <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>.
    *   This is largely due to the generous free tiers offered by providers like Pinecone or Supabase <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.
*   **Convenience**:
    *   Many companies opt for managed services for the convenience they offer, even if it entails higher costs as they scale beyond initial thresholds <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>. This is generally acceptable if the data is not sensitive <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.

### Hybrid Approach

A common and effective strategy for many businesses is a [[local_vs_managed_ai_solutions | hybrid approach]], combining both local and managed services. For instance, caching and vector databases might utilize managed services, while the LLM remains self-hosted <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. While the [[comparison_of_ai_frameworks | decision-making process]] often simplifies the discussion to "all local" or "all managed," a hybrid model is often a robust and practical solution <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. Ultimately, the decision should still lean towards being "more local" or "more managed" services in general <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.