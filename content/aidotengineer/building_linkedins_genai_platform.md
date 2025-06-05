---
title: Building LinkedIns GenAI Platform
videoId: n9rjuBuShko
---

From: [[aidotengineer]] <br/> 

This article outlines LinkedIn's journey in [[building_scalable_ai_systems | building and scaling]] their GenAI platform, focusing on its evolution, critical components, value proposition, and the approach to [[building_ai_teams | building AI teams]] for such an initiative.

## Introduction to the Journey <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>
The presentation details LinkedIn's experience in constructing its GenAI platform, covering the reasons for its development, the methodology used, and the current state of its construction <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. It also explores why such a platform is crucial in today's agent-driven world and offers tips on [[building_ai_teams | how to build and hire]] for a GenAI team <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

Before diving into the platform, understanding the GenAI product experience it supports is essential <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## LinkedIn's GenAI Product Evolution

### First Generation: Collaborative Articles (2023) <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>
In early 2023, LinkedIn launched its first formal GenAI feature: Collaborative Articles <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Functionality:** A straightforward prompt-in/string-out application leveraging the GPT-4 model to create long-form articles, inviting members to comment <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Initial Components:** The team built key backend components, including a gateway for centralized model access and Python notebooks for prompt engineering <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Tech Stack:** At this stage, two different tech stacks were used: Java for the online phase and Python for the backend <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This was not yet considered a platform <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   **Limitations:** This simple approach lacked the capability to inject LinkedIn's rich data into the product experience <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Second Generation: Co-pilot/Coach (Mid-2023) <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>
By mid-2023, development began on the second generation of GenAI products, internally referred to as "co-pilot" or "coach" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Example:** A popular experience involved looking at a user's profile and job description, then using a RAG (Retrieval Augmented Generation) process to provide personalized recommendations on job fit <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **Platform Capabilities:**
    *   **Python SDK:** A Python SDK was built on top of the LangChain framework to orchestrate LLM calls and integrate with LinkedIn's large-scale infrastructure <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. This allowed developers to easily assemble applications <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
    *   **Unified Tech Stack:** The company began unifying its tech stack, realizing the high cost and error potential of transferring Python prompts to Java <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
    *   **Prompt Management:** Investment began in prompt management, creating a "prompt source of truth" submodule for versioning prompts and providing structure for meta-prompts <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
    *   **Conversational Memory:** Critical infrastructure was built to track LLM interactions and retrieval content, then inject that content into the final product to enable conversational bots <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Multi-Agent System: LinkedIn H Assistant (Last Year/Current) <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>
More recently, LinkedIn launched its first real multi-agent system, the "LinkedIn H Assistant" <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **Functionality:** This system assists recruiters by automating tedious tasks like posting jobs, evaluating candidates, and outreach <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   **Platform Evolution:** The platform evolved into an [[building_agents_with_ai_sdk | agent platform]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>:
    *   **Distributed Agent Orchestration Layer:** The Python SDK was extended to support a large-scale, distributed agent orchestration layer, handling distributed execution, retry logic, and traffic shifting <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   **Skill Registry:** An investment was made in a skill registry, providing tools for developers to publish APIs as "skills" into a centralized registry. This registry addresses skill discovery and invocation problems, making API calls easy for applications <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
    *   **Experiential Memory:** Beyond conversational memory, the platform extended to "experiential memory," a storage solution that extracts, analyzes, and infers tacit knowledge from agent-user interactions <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This memory is organized into working, long-term, and collective layers to help agents understand surrounding context <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
    *   **Operability:** Recognizing the autonomous nature of agents (deciding which APIs or LLMs to call), operability became critical <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. An in-house solution was built on OpenTelemetry to track low-level telemetry data, allowing for agent call replay and an analytics layer to guide future optimizations <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

## LinkedIn's GenAI Platform Architecture

The platform's components are categorized into four layers <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>:
1.  **Orchestration:** Manages the flow and interaction of various components.
2.  **Prompt Engineering:** Tools for designing, managing, and optimizing prompts.
3.  **Tools and Skills Invocation:** Enables agents to call external APIs and tools (skills).
4.  **Content and Memory Management:** Handles conversational and experiential memory.

Beyond these core layers, sister teams contribute to the broader LinkedIn GenAI ecosystem <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>:
*   **Modeling Layer:** Fine-tunes open-source models <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Responsible AI Layer:** Ensures agents adhere to company policies and standards <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.
*   **AI Platform/Machine Learning Infrastructure Team:** Hosts the models <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.

## Value Proposition of the GenAI Platform

The key value of this GenAI platform is to serve as a unified interface for a complex ecosystem <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   **Simplified Development:** Developers don't need to understand every individual component, but can leverage the platform to quickly access the entire ecosystem <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. For example, switching between OpenAI and on-premise models can be done by changing a single parameter in one line of code within the SDK <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. This significantly reduces infrastructure integration complexity <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Best Practices and Governance:** As a centralized platform, it enforces best practices and governance, ensuring applications are built efficiently and responsibly <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Why a Dedicated GenAI Platform is Critical

LinkedIn believes a dedicated GenAI platform is essential due to the fundamental differences between GenAI and traditional AI systems <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Blurring of Phases:** In traditional AI, there's a clear distinction between model optimization and model serving, allowing AI engineers and product engineers to operate in separate tech stacks <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. In GenAI systems, this line disappears; everyone becomes an engineer who can optimize overall system performance, creating new challenges for tooling and best practices <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Compound AI Systems:** GenAI or agent systems are "compound AI systems," which tackle tasks using multiple interacting components, including models, retrievers, and external tools <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Bridging Skill Gaps:** The GenAI platform is critical for success because it bridges the skill gaps between AI engineers and product engineers <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.

## [[building_ai_teams | Building the GenAI Team]]

When [[building_ai_teams | building a GenAI team]], finding ideal candidates is challenging <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
*   **Ideal Candidate Profile:** A strong software engineer capable of building infrastructure integration, with good developer PM skills for interface design, and ideally an AI and data science background to understand the latest techniques. They should be quick learners and hands-on <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. Such candidates are rare "unicorns" <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.

### Realistic Hiring Principles <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>
LinkedIn follows these principles:
1.  **Prioritize Software Engineering Skills:** Strong software engineering skills are prioritized over AI expertise <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
2.  **Hire for Potential:** Given the fast-evolving nature of the field, hiring for potential rather than just experience or degrees is crucial, as much experience can quickly become outdated <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
3.  **Build a Diversified Team:** Instead of seeking a single individual with all qualifications, LinkedIn hires a diversified team (full-stack software engineers, data scientists, AI engineers, data engineers, recent graduates from research universities, and startup backgrounds) <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. This collaborative environment encourages engineers to pick up new skills and grow into ideal candidates <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
4.  **Emphasize Critical Thinking:** Teams are encouraged to constantly evaluate the latest open-source packages, engage with vendors, and proactively deprecate solutions, acknowledging that current builds may be outdated within a year <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

## Key Takeaways and Lessons Learned

### Tech Stack Choice <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>
*   **Python Recommendation:** LinkedIn strongly recommends Python. Despite starting with Java and Python, Python was ultimately chosen due to its prevalence in research and open-source communities, and its scalability <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.

### Key Components to Build <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>
1.  **Prompt Source of Truth:** Essential for robust version control of prompts, critical for operational stability <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
2.  **Memory:** A key component for injecting rich data into the agent experience <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
3.  **Skills:** In the agent era, uplifting existing APIs into easily callable skills for agents is crucial, requiring surrounding tooling and infrastructure <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

### [[building_and_scaling_ai_use_cases_for_enterprises | Scaling and Adoption]] <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>
*   **Start Small:** Instead of building a full-fledged platform from the outset, focus on solving immediate needs. LinkedIn began with a simple Python library for orchestration and gradually grew into the comprehensive platform <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.
*   **Focus on Infrastructure and Scalability:** Leverage existing enterprise infrastructure, such as LinkedIn's messaging infrastructure, as a memory layer, which proves both cost-efficient and scalable <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. This aligns with [[using_existing_enterprise_systems_for_ai_integration | using existing enterprise systems for AI integration]].
*   **Prioritize Developer Experience:** The platform's ultimate goal is to enhance developer productivity <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. Its adoption is key to success. Design the platform to align with developers' existing workflows to ease adoption and ensure success <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. This contributes to [[building_user_experiences_with_ai | building user experiences with AI]].

For more detailed technical information, readers are encouraged to check LinkedIn's engineering blog posts <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.