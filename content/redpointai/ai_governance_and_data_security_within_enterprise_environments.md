---
title: AI governance and data security within enterprise environments
videoId: FhIPUFZhKzI
---

From: [[redpointai]] <br/> 

Enterprises embarking on AI adoption face significant considerations regarding governance and data security to ensure safe and trustworthy deployment of AI technologies <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>. Baris Gencel, Head of AI at Snowflake, highlights the critical steps companies take to integrate AI effectively and securely into their operations <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Establishing Trust and Control
The initial step for many large companies involves their [[ai_policy_and_regulation_implications | AI governance boards]] to ensure comfort with the chosen AI platform <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. A primary focus is on [[trust_and_data_security_in_ai | trust]] and ensuring that [[trust_and_data_security_in_ai | data security]] and data governance principles are respected, with acceptable [[ai_policy_and_regulation_implications | policies]] in place for the company <a class="yt-timestamp" data-t="00:13:18">[00:13:18]</a>. Snowflake addresses these concerns by running AI systems directly next to the data within its secure environment, offering reassurances to companies <a class="yt-timestamp" data-t="00:13:35">[00:13:35]</a>.

## Snowflake's Integrated Approach
Snowflake's core offering, Cortex, serves as an inference engine that runs large language models, including its own Arctic model and others from providers like Mistral and Meta <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. A significant value proposition is the ability to run all models and inference directly inside Snowflake, right next to the customer's data <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.

For customers who opt to use external models, Snowflake provides solutions, though this is not the default configuration <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.

### Granular Access Controls
[[Trust and data security in AI | Governance]] is built from the ground up at Snowflake, allowing customers to set very granular access controls <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>. This means access to database objects can be precisely granted <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

An example given is an HR chatbot where responses must differ based on who asks the question, necessitating very little room for hallucination or [[trust_and_data_security_in_ai | data leakage]] <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. For AI applications like search, access controls are deeply integrated, ensuring the search system only provides access to documents a user is authorized to view <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. Snowflake leverages its existing access controls for data, so if a user cannot access data, they do not receive it through the AI system <a class="yt-timestamp" data-t="00:18:42">[00:18:42]</a>. Many customers spend years setting up their data governance, which then becomes a huge advantage for building AI on top of it <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.

## Addressing Challenges in AI Deployment
Despite the progress, several [[challenges_in_enterprise_ai_deployment | challenges]] remain in widespread [[enterprise_ai_adoption_challenges | enterprise AI adoption]]:

*   **Hallucinations:** [[Enterprise AI adoption challenges | Hallucinations]] are still a concern <a class="yt-timestamp" data-t="00:28:05">[00:28:05]</a>. In regulated industries, these can be catastrophic <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
*   **Measurement and Quality:** Measurement of AI system performance is not yet mature <a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>. Achieving high quality in complex scenarios, such as text-to-SQL, remains a concern <a class="yt-timestamp" data-t="00:28:18">[00:28:18]</a>.
*   **User Comfort:** Product innovation is needed to help end-users become comfortable with AI answers that may not always be right, and to provide mechanisms for checking correctness <a class="yt-timestamp" data-t="00:15:49">[00:15:49]</a>.
*   **Unchartered Territory:** Agentic systems are emerging, representing new and unchartered territory for businesses <a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>.

### Evaluation and Observability
To build high-quality production systems, enterprises need robust evaluation platforms <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. Snowflake's acquisition of TruEra, and its open-source product TRU Lens, provides an observability and LLM evaluation platform that helps customers assess system performance at scale, often using LLMs as judges <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>. This eases concerns about evaluating systems, which is crucial for moving from proofs-of-concept (POCs) to production deployments <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>.

## Policy and Guardrails
Companies require reassurances and guardrails on what models can do, especially since responses are unscripted <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>. This includes ensuring alignment from both a [[ai_policy_and_regulation_implications | policy]] perspective and a brand perspective <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. Snowflake provides additional guardrails through products like Cortex Guard, which utilizes technologies such as Llama Guard <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>.

While internal use cases for productivity and analysis are transitioning from POCs to production, external use cases still require more confidence before large-scale deployment <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>. The timeline for widespread internal deployments depends on increasing comfort with the technology and continued product innovation <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.