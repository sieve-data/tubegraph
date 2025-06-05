---
title: Multiagent Systems and Their Applications
videoId: n9rjuBuShko
---

From: [[aidotengineer]] <br/> 

This article explores the journey of building LinkedIn's Generative AI (GenAI) platform, focusing on the evolution and application of [[multiagent_system | multiagent systems]] within the company's products and infrastructure <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. It details the progression from simple GenAI features to complex [[multiagent_system | multiagent systems]] and the critical platform components required to support them <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## LinkedIn's GenAI Product Evolution

LinkedIn's GenAI journey began in 2023 with the launch of its first formal GenAI feature, collaborative articles <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This feature was a straightforward prompt-in, string-out application leveraging the GPT-4 model to create long-form articles <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Initially, the supporting infrastructure included a gateway for centralized model access and Python notebooks for prompt engineering <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. At this stage, two different tech stacks were used: Java for the online phase and Python for the backend <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This initial setup was not considered a full platform <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### Second Generation: Co-Pilot or Coach

By mid-2023, LinkedIn realized the limitations of the simple approach, particularly its inability to inject rich data into the product experience <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This led to the development of the second generation of GenAI products, internally referred to as co-pilot or coach <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. An example is a feature that analyzes a user's profile and a job description, using a RAG (Retrieval Augmented Generation) process to provide personalized recommendations on job fit <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

At this stage, platform capabilities began to emerge <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Key developments included:
*   **Python SDK:** A Python SDK was built on top of the popular LangChain framework to orchestrate LLM calls and integrate with LinkedIn's large-scale infrastructure <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This allowed developers to easily assemble applications <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Unified Tech Stack:** The company unified its tech stack, primarily to Python, realizing the cost and error potential of transferring Python prompts to Java <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Prompt Management:** Investment began in prompt management, or "prompt source of truth," as a sub-module to help developers version their prompts and provide structure to meta-prompts <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Conversational Memory:** A critical infrastructure piece, conversational memory, was introduced to track LLM interactions and retrieval content, injecting it into the final product to enable conversational bots <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Multiagent Systems and Applications

In the last year, LinkedIn launched its first "real" [[multiagent_system | multiagent system]] called the LinkedIn AI Assistant <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. This [[multiagent_system | multiagent system]] is designed to assist recruiters, automating tedious tasks such as posting jobs, evaluating candidates, and reaching out to them <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

The GenAI platform further evolved to support [[multiagent_system | multiagent systems]] <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Key advancements included:
*   **Distributed Agent Orchestration Layer:** The Python SDK was extended into a large-scale [[multiagent_orchestration_for_ai_copilot_development | distributed agent orchestration layer]] <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. This layer handles distributed agent execution and complex scenarios like retry logic and traffic shifts <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.
*   **Skill Registry:** Recognizing that skills (APIs) are a key aspect for agents to perform actions, LinkedIn invested in a skill registry <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This registry provides tools for developers to publish their APIs, facilitating skill discovery and invocation within applications <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
*   **Experiential Memory:** Beyond conversational memory, the platform introduced experiential memory <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This memory storage extracts, analyzes, and infers tacit knowledge from interactions between agents and users <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Memories are organized into different layers, including working, long-term, and collective memories, to enhance agent awareness <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Operability:** As agents are autonomous and can decide which APIs or LLMs to call, predicting their behavior is challenging <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. To address this, LinkedIn invested in operability, building an in-house solution on OpenTelemetry to track low-level telemetry data <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This data allows for replaying agent calls and an analytics layer guides future optimization of agent systems <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>.

## Components of the GenAI Platform for Multiagent Systems

The LinkedIn GenAI platform, particularly for [[multiagent_systems_in_technical_workflows | multiagent systems]], can be classified into four key layers <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>:
1.  **Orchestration** <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>
2.  **Prompt Engineering** <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>
3.  **Tools and Skills Invocation** <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>
4.  **Content and Memory Management** <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>

The platform provides a unified interface for a complex GenAI ecosystem, abstracting away the underlying complexities of modeling, responsible AI, and machine learning infrastructure <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. For instance, developers can switch between OpenAI models and internal models by changing a single parameter in one line of code <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This centralized platform also enforces best practices and governance, ensuring efficient and responsible application development <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## The Criticality of a Dedicated Platform for Agent Systems

A dedicated platform for [[multiagent_system | multiagent systems]] is considered critical because GenAI represents a fundamentally different AI system compared to traditional ones <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. In traditional AI, there's a clear separation between model optimization and model serving, allowing AI engineers and product engineers to work on different tech stacks <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. However, in GenAI systems, this line blurs, with everyone becoming an engineer who can optimize overall system performance <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

GenAI and [[multiagent_system | agent systems]] are viewed as "compound AI systems" <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.

> "A compound AI system can be defined as a system which tackles AI tasks using multiple interacting components including multiple cost to model retrievers or external tools." <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>

This necessitates a platform to bridge the skill gaps between AI engineers and product engineers <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

## Building and Scaling Multiagent Systems

### Talent Acquisition and Team Building
Hiring for [[developing_and_optimizing_ai_agents | developing and optimizing AI agents]] requires a unique blend of skills <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. Ideal candidates are strong software engineers capable of infrastructure integration, with good developer product management (PM) skills for interface design, and an AI/data science background to understand the latest techniques <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. They must be hands-on and adaptable to new techniques <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.

Realistically, trade-offs are made in hiring, following principles like:
*   **Prioritizing Software Engineering:** Stronger software engineering skills are prioritized over AI expertise <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Hiring for Potential:** Given the rapid evolution of the field, hiring for potential rather than outdated experience or degrees is crucial <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Diversified Teams:** Instead of finding a single "unicorn" engineer, building a diversified team with full-stack software engineers, data scientists, AI engineers, data engineers, fresh graduates, and startup veterans has proven effective <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. Collaboration helps team members pick up new skills and grow into ideal candidates <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **Critical Thinking:** The team consistently evaluates the latest open-source packages, engages with vendors, and proactively deprecates solutions, as technologies can become outdated within a year or less <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

### Key Technical Takeaways for Multiagent Systems
*   **Python for Tech Stack:** Python is strongly recommended due to its prevalence in research and open-source communities, and its proven scalability <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   **Prompt Source of Truth:** A robust system for version controlling prompts is critical for operational stability, similar to managing traditional model parameters <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   **Memory Management:** Memory is a key component for [[integration_of_ai_agents_into_existing_infrastructure | injecting rich data]] into the agent experience <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   **API Uplifting to Skills:** In the agent era, uplifting existing APIs into easily callable skills for agents is a new and crucial component, requiring supporting tooling and infrastructure <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

### Scaling and Adoption Strategies
To scale and ensure adoption of [[multiagent_system | multiagent systems]] and platforms:
*   **Solve Immediate Needs:** Start by solving immediate needs rather than attempting to build a full-fledged platform from the outset <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>. For example, LinkedIn began with a simple Python library for orchestration, which then grew into more components <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **Focus on Infrastructure and Scalability:** Leverage existing robust infrastructure, such as LinkedIn's messaging infrastructure for a memory layer, to ensure cost-efficiency and scalability <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
*   **Prioritize Developer Experience:** The platform's primary goal is to help developers be productive <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. Aligning technology with developers' existing workflows is key to ease adoption and success <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.

More technical details on LinkedIn's GenAI platform journey are available in their engineering blog posts <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.