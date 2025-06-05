---
title: Unified interfaces for AI ecosystems
videoId: n9rjuBuShko
---

From: [[aidotengineer]] <br/> 

LinkedIn has embarked on a significant journey to build its Gen AI platform, recognizing its critical role in the evolving landscape of AI agents <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>, <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. The core purpose of this platform is to provide a [[model_context_protocol_and_ai_integration | unified interface]] for a complex AI ecosystem, simplifying development for engineers <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>.

## LinkedIn's Gen AI Platform Journey

### Collaborative Articles (Early 2023)

LinkedIn's initial formal Gen AI feature, launched in early 2023, was "Collaborative Articles" <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>. This feature used the GPT-4 model to create long-form articles, inviting members to comment on them <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. At this stage, the team developed key components, including:
*   A gateway for centralized model access <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>.
*   Python notebooks for prompt engineering <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>.

However, this early phase suffered from limitations, such as two distinct tech stacks (Java for online, Python for backend) and a lack of capability to inject rich data into the product experience, preventing it from being considered a true platform <a class="yt-timestamp" data-t="02:13:00">[02:13:00]</a>, <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>, <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

### Co-pilot/Coach (Mid 2023)

By mid-2023, LinkedIn began developing its second generation of Gen AI products, internally known as "Co-pilot" or "Coach" <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. An example is a feature that provides personalized job fit recommendations based on a user's profile and job descriptions, leveraging a RAG (Retrieval Augmented Generation) process <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>, <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.

This phase marked the start of building core platform capabilities:
*   **Python SDK**: Central to the platform, built on top of the LangChain framework to orchestrate LLM calls and integrate with large-scale infrastructure <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.
*   **Unified Tech Stack**: Recognizing the high cost and error potential of transferring Python prompts to Java, the tech stack was unified to Python <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>.
*   **Prompt Management**: Investment began in a "prompt source of truth" module to help developers version their prompts and provide structure around meta-prompts <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.
*   **Conversational Memory**: An infrastructure was developed to track LLM interactions and retrieval content, injecting it into the final product to enable conversational bots <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a>.

### Multi-Agent Systems (Late 2023/Early 2024)

LinkedIn launched its first true [[Multimodal AI Systems | multi-agent system]], the "LinkedIn HR Assistant," in late 2023/early 2024 <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>, <a class="yt-timestamp" data-t="04:35:00">[04:35:00]</a>. This system assists recruiters by automating tedious tasks like job posting, candidate evaluation, and outreach <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.

The platform evolved significantly to support these [[future_of_ai_agent_ecosystems | AI agents]]:
*   **Distributed Agent Orchestration**: The Python SDK was extended into a large-scale, distributed agent orchestration layer to handle complex scenarios like retries and traffic shifts <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.
*   **Skill Registry**: A key investment was made in a skill registry, providing tools for developers to publish APIs as "skills" that agents can discover and invoke easily <a class="yt-timestamp" data-t="05:45:00">[05:45:00]</a>.
*   **Experiential Memory**: Beyond conversational memory, the platform added experiential memory, a storage system to extract, analyze, and infer tacit knowledge from agent-user interactions <a class="yt-timestamp" data-t="06:14:00">[06:14:00]</a>. This memory is organized into working, long-term, and collective layers to help agents understand their context <a class="yt-timestamp" data-t="06:35:00">[06:35:00]</a>.
*   **Operability**: Recognizing the autonomous and unpredictable nature of agents, operability became crucial <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>. An in-house solution built on OpenTelemetry tracks low-level telemetry data for replaying agent calls and guiding future optimization <a class="yt-timestamp" data-t="07:10:00">[07:10:00]</a>.

## Components of the Gen AI Platform

The LinkedIn Gen AI platform can be categorized into four main layers <a class="yt-timestamp" data-t="07:39:00">[07:39:00]</a>:
1.  **Orchestration** <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>
2.  **Prompt Engineering** <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>
3.  **Tools and Skills Invocation** <a class="yt-timestamp" data-t="07:49:00">[07:49:00]</a>
4.  **Content and Memory Management** <a class="yt-timestamp" data-t="07:50:00">[07:50:00]</a>

Supporting this, sister teams build out other crucial aspects of the LinkedIn Gen AI ecosystem <a class="yt-timestamp" data-t="07:56:00">[07:56:00]</a>:
*   **Modeling Layer**: Fine-tuning open-source models <a class="yt-timestamp" data-t="08:02:00">[08:02:00]</a>.
*   **Responsible AI Layers**: Ensuring agent behavior adheres to policies and standards <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
*   **AI Platform/Machine Learning Infrastructure**: Hosting the models <a class="yt-timestamp" data-t="08:14:00">[08:14:00]</a>.

## Value Proposition: A Unified Interface

The primary value of LinkedIn's Gen AI platform is to act as a [[model_context_protocol_and_ai_integration | unified interface]] for this complex ecosystem <a class="yt-timestamp" data-t="08:23:00">[08:23:00]</a>. This means developers don't need to understand every individual component, but can instead leverage the platform for quick access to the entire ecosystem <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a>. For example, a single parameter in the SDK can switch between OpenAI models and internal models, significantly reducing infrastructure integration complexity <a class="yt-timestamp" data-t="08:50:00">[08:50:00]</a>.

Furthermore, this centralized platform enforces [[best_practices_for_building_ai_agents | best practices]] and governance, ensuring applications are built efficiently and responsibly <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

## Why a Unified Platform is Critical

LinkedIn believes that Gen AI systems are fundamentally different from traditional AI systems <a class="yt-timestamp" data-t="09:55:00">[09:55:00]</a>. In traditional AI, there's a clear separation between model optimization and serving, allowing AI and product engineers to operate on different tech stacks <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>. However, in Gen AI systems, this line blurs, with everyone contributing to overall system performance optimization, creating new tooling and [[best_practices_for_building_ai_agents | best practice]] challenges <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.

Gen AI and agent systems are considered "compound AI systems" <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>, defined as systems tackling AI tasks using multiple interacting components, including multiple calls to models, retrievers, or external tools <a class="yt-timestamp" data-t="10:55:00">[10:55:00]</a>. This requires skills across both AI and product engineering <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>. The Gen AI app platform is crucial to bridge this skill gap <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.

## Building and Scaling the Platform

### Hiring Principles for the Team

When building a Gen AI platform team, LinkedIn prioritizes certain qualities <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a>:
*   **Strong Software Engineering Skills**: Prioritized over pure AI expertise <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>.
*   **Potential over Experience/Degrees**: Given the rapid evolution of the field, the ability to learn is more valuable than potentially outdated experience <a class="yt-timestamp" data-t="13:03:00">[13:03:00]</a>.
*   **Diversified Team**: Instead of seeking "unicorn" engineers with all qualifications, LinkedIn hires a diversified team (full-stack software engineers, data scientists, AI engineers, data engineers, fresh grads, startup backgrounds) <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>. Collaboration helps individuals pick up new skills <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
*   **Critical Thinking**: The team consistently evaluates new open-source packages, engages with vendors, and proactively deprecates solutions, understanding that current builds may be obsolete within a year <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>.

### Key Platform Components to Build

Based on their experience, LinkedIn highlights critical components for a Gen AI platform <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>:
*   **Prompt Source of Truth**: Essential for robust version control of prompts, similar to model parameters, ensuring operational stability <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a>.
*   **Memory**: A key component to inject rich data into the agent experience <a class="yt-timestamp" data-t="15:26:00">[15:26:00]</a>.
*   **APIs as Skills**: In the agent era, uplifting APIs into easily callable skills for agents is crucial, requiring surrounding tooling and infrastructure <a class="yt-timestamp" data-t="15:42:00">[15:42:00]</a>.
*   **Python Preference**: Python is strongly recommended due to its prevalence in research and open-source communities, and its scalability <a class="yt-timestamp" data-t="14:37:00">[14:37:00]</a>.

### Scaling and Adoption Strategies

For successful adoption and scaling of the platform, LinkedIn recommends:
*   **Solving Immediate Needs**: Start by addressing immediate problems (e.g., a simple Python library for orchestration) rather than building a full-fledged platform from the outset <a class="yt-timestamp" data-t="16:04:00">[16:04:00]</a>.
*   **Focus on Infrastructure and Scalability**: Leverage existing robust infrastructure, such as LinkedIn's messaging infrastructure for a memory layer, for both cost efficiency and scalability <a class="yt-timestamp" data-t="16:29:00">[16:29:00]</a>.
*   **Developer Experience ([[usercentric_ai_design_and_feedback_loops | User-centric AI design and feedback loops]])**: The platform's success hinges on developer adoption. Design the platform to align with existing developer workflows to ease [[enhancing_existing_systems_with_ai_capabilities | integration of mCP with AI Applications | adoption]] and boost productivity <a class="yt-timestamp" data-t="16:46:00">[16:46:00]</a>.

More technical details are available in LinkedIn's engineering blog posts <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>.