---
title: Multiagent systems in AI
videoId: n9rjuBuShko
---

From: [[aidotengineer]] <br/> 

LinkedIn has embarked on a comprehensive journey to develop and integrate [[the_role_and_definition_of_agents_in_ai | AI agent]] capabilities into its platform, evolving from simple Generative AI (GenAI) features to complex [[MultiAgent Systems and APIBased Communication | multiagent systems]]. This evolution necessitated the creation of a robust GenAI platform to support and unify these advancements <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Early GenAI Product Experiences

In 2023, LinkedIn launched its first formal GenAI feature: **Collaborative Articles** <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This was a straightforward "prompt-in, string-out" application, leveraging GPT-4 to create long-form articles and invite member comments <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. At this stage, the team built core components like a centralized model access gateway and Python notebooks for prompt engineering, but operated with dual tech stacks (Java for online, Python for backend) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

By mid-2023, LinkedIn recognized limitations, particularly the inability to inject rich internal data into the product experience <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>. This led to the development of the second generation of GenAI products, internally referred to as **co-pilot or coach systems** <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. An example is the personalized recommendation feature that analyzes a user's profile and job description, using a Retrieval Augmented Generation (RAG) process to assess job fit <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

Key platform capabilities emerged during this phase:
*   **Python SDK**: Built on top of a popular framework, this SDK orchestrates Large Language Model (LLM) calls and integrates with LinkedIn's large-scale infrastructure, enabling developers to assemble applications more easily <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.
*   **Unified Tech Stack**: Recognizing the cost and errors associated with transferring Python prompts to Java, the tech stack began unifying <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Prompt Management**: Investment in a "prompt source of truth" sub-module helped developers version prompts and structure meta-prompts <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Conversational Memory**: This infrastructure tracks LLM interactions and retrieval content, injecting it into the final product to enable conversational bot experiences <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Evolution to Multiagent Systems

In the last year, LinkedIn launched its first true [[MultiAgent Systems and APIBased Communication | multiagent system]]: the **LinkedIn HR Assistant** <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. This system assists recruiters by automating tedious tasks such as job posting, candidate evaluation, and outreach <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

The platform further evolved to support these advanced [[the_role_and_definition_of_agents_in_ai | AI agent]] capabilities:
*   **Distributed Agent Orchestration**: The Python SDK was extended into a large-scale [[multiagent_orchestration_in_ai_copilot_systems | distributed agent orchestration layer]], handling distributed execution, retry logic, and traffic shifts for complex agent scenarios <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Skill Registry**: A key investment was made in a skill registry, providing tools for developers to publish APIs into a centralized hub. This registry handles skill discovery and invocation, making it easy for applications to call APIs and perform tasks <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. [[The role and definition of agents in AI | Agents]] are expected to perform actions, making skills/APIs a critical component <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Experiential Memory**: Beyond conversational memory, the platform introduced [[the_role_and_definition_of_agents_in_ai | experiential memory]]. This storage system extracts, analyzes, and infers tacit knowledge from interactions between the [[the_role_and_definition_of_agents_in_ai | agent]] and the user <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This memory is organized into different layers, including working, long-term, and collective memories, enhancing the [[the_role_and_definition_of_agents_in_ai | agent's]] awareness of surrounding content <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Operability**: Due to the autonomous nature of [[the_role_and_definition_of_agents_in_ai | agents]]—their ability to decide which APIs or LLMs to call—predicting their behavior is challenging <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. LinkedIn invested in an in-house operability solution, built on OpenTelemetry, to track low-level telemetry data. This data enables replaying [[the_role_and_definition_of_agents_in_ai | agent]] calls and provides analytics to guide future optimization of [[the_role_and_definition_of_agents_in_ai | agent systems]] <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## LinkedIn GenAI Platform Architecture

The GenAI platform's components are broadly classified into four layers <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>:
1.  **Orchestration** <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>
2.  **Prompt Engineering** <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>
3.  **Tools and Skills Invocation** <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>
4.  **Content and Memory Management** <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>

This platform serves as a unified interface for a complex GenAI ecosystem, which also includes modeling layers (e.g., fine-tuning open-source models), responsible AI layers (ensuring [[the_role_and_definition_of_agents_in_ai | agent]] adherence to policies), and core AI/Machine Learning infrastructure <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. The platform's key value proposition is simplifying developer access to this entire ecosystem, for instance, by allowing model switching with a single line of code <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. It also provides a centralized point to enforce best practices and governance, ensuring efficient and responsible application development <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Why a GenAI/Agent Platform is Critical

LinkedIn believes a dedicated GenAI platform is critical for success because [[the_role_and_definition_of_agents_in_ai | Generative AI systems]], particularly [[the_role_and_definition_of_agents_in_ai | agent systems]], differ fundamentally from traditional AI systems <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>. In traditional AI, there's a clear separation between model optimization and serving phases, allowing AI engineers and product engineers to work on separate tech stacks <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.

However, in [[the_role_and_definition_of_agents_in_ai | GenAI systems]], this line blurs; everyone becomes an engineer who can optimize overall system performance, creating new tooling and best practice challenges <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. [[The role and definition of agents in AI | Agent systems]] are considered "compound AI systems" (as defined by Berkeley AI Research lab), tackling tasks using multiple interacting components like models, retrievers, or external tools <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. The GenAI app platform aims to bridge the skill gap between AI engineers and product engineers <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

## [[Development and Challenges of AI Agents | Building and Scaling AI Agent Solutions]]

### Hiring Principles for Agent Development Teams
Building a team for [[development_and_challenges_of_ai_agents | AI agent development]] is challenging due to the need for a rare combination of skills <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. Ideal candidates are strong software engineers with infrastructure integration skills, developer PM skills for interface design, and AI/data science backgrounds to understand the latest techniques, while remaining hands-on <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

LinkedIn's hiring principles include:
*   **Prioritize Software Engineering**: Strong software engineering skills are prioritized over AI expertise <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Hire for Potential**: Given the rapid evolution of the field, potential is valued over outdated experience or degrees <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **Diversified Teams**: Instead of seeking "unicorns," LinkedIn builds diversified teams comprising full-stack engineers, data scientists, AI engineers, data engineers, fresh graduates from research universities, and individuals with startup backgrounds. Collaboration within these teams helps engineers acquire new skills <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.
*   **Critical Thinking**: The team constantly evaluates new open-source packages, engages with vendors, and proactively deprecates existing solutions, acknowledging that current solutions may be outdated within a year <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

### Technical Recommendations and Key Takeaways
*   **Tech Stack Choice**: Python is strongly recommended due to its prevalence in research and open-source communities, and its scalability <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   **Key Components to Build**:
    *   **Prompt Source of Truth**: A robust version control system for prompts is critical for operational stability <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
    *   **Memory**: Essential for injecting rich data into the [[the_role_and_definition_of_agents_in_ai | agent]] experience <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
    *   **Skills/APIs**: Uplifting internal APIs into easily callable skills for [[the_role_and_definition_of_agents_in_ai | agents]], supported by surrounding tooling and infrastructure <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.
*   **Scaling and Adoption Strategies**:
    *   **Solve Immediate Needs**: Start by addressing immediate problems (e.g., a simple Python library for orchestration) rather than attempting to build a full-fledged platform initially <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
    *   **Infrastructure and Scalability**: Focus on building scalable infrastructure, like leveraging existing messaging infrastructure for the memory layer <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
    *   **Developer Experience (DX)**: Prioritize DX to ensure developer adoption. Design the platform to align with existing workflows, easing adoption and increasing success <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>.

This strategic approach to [[developing_ai_agents_and_agentic_workflows | developing AI agents and agentic workflows]] emphasizes iterative development, strong foundational engineering, and a focus on both technical excellence and developer productivity to build a robust and scalable GenAI ecosystem. For more technical details, readers can consult the LinkedIn Engineering blog post by Cake S and the presenter <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.