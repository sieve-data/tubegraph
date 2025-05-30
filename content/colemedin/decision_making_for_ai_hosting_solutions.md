---
title: Decision Making for AI Hosting Solutions
videoId: W5X34-QmdEQ
---

From: [[colemedin]] <br/> 

The debate between [[local_vs_managed_ai_solutions | local self-hosted]] and managed AI solutions is significant, influencing the entire [[developing_an_effective_ai_tech_stack | AI tech stack]] and application development direction <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. Making an informed decision is crucial for building effective AI applications <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Overview of AI Tech Stacks

Understanding the technologies involved in both [[local_vs_managed_ai_solutions | local]] and [[tech_stack_for_managed_ai_services | managed AI services]] is key to making a choice <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. While many options exist, the following are common suggestions for most use cases <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### Local AI Tech Stack
A recommended [[setting_up_a_local_ai_cloud_stack | local AI cloud stack]] for self-hosting includes:
*   **Infrastructure:** Docker, to ensure a sound infrastructure for self-hosting <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **LLM:** Ollama, capable of hosting various large language models like Llama 3.1 70b <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.
*   **Vector Database:** Qdrant <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
*   **Authentication & Database:** Self-hosted Supabase for authentication and PostgreSQL <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. PG Vector can be used as a PostgreSQL extension for RAG instead of Qdrant <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Workflow Automations:** n8n for no-code workflows <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Caching:** Redis <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Managed AI Services Tech Stack
The [[tech_stack_for_managed_ai_services | tech stack for managed AI services]] often shares similar names with the local stack, making migration easier <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. This stack generally includes:
*   **LLM:** Claude, GPT, or Groq, depending on the specific use case <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   **Vector Database:** Pinecone or Qdrant <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Authentication & Database:** Hosted Supabase for PostgreSQL and authentication <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. PG Vector can also replace Pinecone or Qdrant for RAG <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **Workflow Automations:** Cloud n8n for no-code workflows <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **Caching:** Redis.io for hosted caching <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Decision Tree for AI Hosting Solutions

Choosing between [[local_vs_managed_ai_solutions | local]] and managed services can be simplified using a decision tree. It's important to note that a [[hybrid_approach_in_ai_deployments | hybrid approach in AI deployments]], where some components are managed and others self-hosted (e.g., managed caching/vector database with a self-hosted LLM), is a very common and solid strategy <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The decision tree, however, simplifies the choice by focusing on the extremes (all local or all managed) <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

### 1. Is it a Simple Proof of Concept (POC)?
*   **Yes (Go Managed):** For a POC, managed services are much quicker to set up <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This allows for rapid development and iteration, enabling quick assessment of whether the concept is viable for the business without spending excessive time on local setup <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. Using similar technologies between managed and local stacks facilitates an easy migration to local if the POC proves successful <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. Even with sensitive data, mocking or removing sensitive parts is possible for POCs <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

*   **No (It's a Production Application):** Proceed to the next question <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

### 2. Is Your Data Sensitive?
*   **Yes (Go Local):** If building a production application with sensitive data, self-hosting almost everything locally is highly recommended <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. This prevents sensitive information from being fed into public LLMs like GPT, where it could be used for training and potentially regurgitated later <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. This also applies to [[database_setup_and_management_for_ai_agents | databases in the cloud]] <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

*   **No (Data is Not Sensitive):** Proceed to the next question <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### 3. Do You Need the Latest and Greatest Technology (LLMs)?
*   **Yes (Go Managed):** If the application requires the most powerful LLMs (e.g., Claude 3.5 Sonnet, GPT-4) for complex tasks like advanced tool calling or specific structured output, managed services are typically necessary <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. The compute resources needed for these models are often too intense to run locally <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. This requirement is usually determined during the POC phase <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

*   **No (Local Models Suffice):** If local models like Llama 3 70b or Mistral can handle the requirements, proceed to the next question <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

### 4. Are You Scaling Your App to More Than 1,000 Users?
*   **No (Go Managed):** If the application will not scale heavily (e.g., less than 1,000 users) and data is not sensitive, managed services can be cheaper <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>. The initial overhead of setting up a [[choosing_cloud_providers_for_local_ai_deployment | cloud instance]] to host local LLMs or RAG components can be more expensive due to the generous free tiers offered by managed services like Pinecone or Supabase <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

*   **Yes (Go Local for Cost-Effectiveness, or Managed for Convenience):** If scaling to thousands of users, self-hosting becomes very cost-effective <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>. As long as the knowledge to host locally is available or desired, going local is recommended for high-scale applications with non-sensitive data <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. However, some companies prioritize the convenience of managed services over cost savings, even at scale, provided data is not sensitive <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This relates to the [[cost_comparison_of_grock_ai_service_and_selfhosted_solutions | cost comparison of Groq AI service and self-hosted solutions]] and other providers.

## Conclusion

This decision tree helps in navigating the complexities of [[deploying_ai_applications_to_the_cloud | deploying AI applications to the cloud]] or keeping them local <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>. While opinions vary, especially on the definition of "sensitive data" <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>, going local is generally a good idea, particularly as local models like Llama become more powerful <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.