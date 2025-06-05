---
title: LinkedIns GenAI platform development
videoId: n9rjuBuShko
---

From: [[aidotengineer]] <br/> 

LinkedIn has embarked on a significant journey to build its own Generative AI (GenAI) platform, supporting a rapidly evolving suite of AI-powered products <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This platform aims to provide a unified interface for a complex GenAI ecosystem, enabling developers to build applications efficiently and responsibly <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>, <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.

## Evolution of LinkedIn's GenAI Products & Platform

The development of LinkedIn's GenAI platform has been an iterative process, growing piece by piece to meet the demands of increasingly sophisticated AI applications <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.

### Early 2023: Collaborative Articles

LinkedIn launched its first formal GenAI feature, "Collaborative Articles," in early 2023 <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This was a straightforward prompt-in, string-out application leveraging the GPT-4 model from [[OpenAIs approach to integrating AI in enterprises | OpenAI]] to create long-form content <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

At this stage, the team built core components like a gateway for centralized model access and Python notebooks for prompt engineering <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. However, there were two distinct tech stacks: Java for the online phase and Python for the backend <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This initial setup was not considered a full platform <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

A key [[challenges_in_implementing_gen_ai_projects | limitation]] of this simple approach was its inability to inject rich data into the product experience <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

### Mid 2023: Co-pilot/Coach

In mid-2023, LinkedIn began developing its second generation of GenAI products, internally called "co-pilot" or "coach" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. An example is a feature that analyzes a user's profile and job description to provide personalized recommendations on job fit, using a Retrieval-Augmented Generation (RAG) process <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

This phase saw the beginning of building core platform capabilities <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>:
*   **Python SDK:** Built on top of the LangChain framework to orchestrate LLM calls and integrate with LinkedIn's large-scale infrastructure <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>. This allowed developers to easily assemble applications <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Unified Tech Stack:** The decision was made to unify the tech stack due to the cost and errors involved in transferring Python prompts to Java <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Python was eventually chosen as the primary language <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   **Prompt Management:** Investment in "prompt source of truth" helped developers version their prompts and provide structure to meta-prompts <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Conversational Memory:** An infrastructure to track LLM interactions and retrieved content, injecting them into the final product to enable conversational bots <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

### Late 2023/Early 2024: Multi-Agent Systems

More recently, LinkedIn launched its first real multi-agent system, the "LinkedIn HR Assistant" <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. This system automates tedious tasks for recruiters, such as posting jobs, evaluating candidates, and reaching out to them <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

The platform evolved into an agent platform with enhanced capabilities <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>:
*   **Distributed Agent Orchestration Layer:** The Python SDK was extended to support large-scale distributed agent execution, handling complex scenarios like retry logic and traffic shifting <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Skill Registry:** An investment was made in a skill registry, providing tools for developers to publish their APIs as "skills" that agents can discover and invoke easily <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>. This is critical for agents to perform actions <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.
*   **Experiential Memory:** In addition to conversational memory, the platform introduced experiential memory—a storage for extracting, analyzing, and inferring tacit knowledge from agent-user interactions <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. This memory is organized into working, long-term, and collective layers to make agents aware of their surroundings <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
*   **Operability Investment:** Recognizing the autonomous and unpredictable nature of agents, LinkedIn invested in operability <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>. An in-house solution built on OpenTelemetry tracks low-level telemetry data, allowing for replaying agent calls and analytics to guide future optimization <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

## Components of the GenAI Platform

LinkedIn's GenAI platform is structured into four main layers <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>:
1.  Orchestration
2.  Prompt Engineering Tools
3.  Skills Invocation
4.  Content and Memory Management

Beyond these core components, the broader LinkedIn GenAI ecosystem includes sister teams working on modeling (e.g., fine-tuning [[use_of_open_source_tools_for_ai_development | open source models]]), responsible AI (ensuring agents behave according to policy), and AI/machine learning infrastructure for hosting models <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.

## Value Proposition of the Platform

The primary value of LinkedIn's GenAI platform is to serve as a unified interface for this complex ecosystem <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   **Simplified Access:** Developers can leverage the platform to quickly access the entire GenAI ecosystem without needing to understand every individual component <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. For instance, developers can switch between [[OpenAIs approach to integrating AI in enterprises | OpenAI models]] and internal models by changing a single parameter in their SDK code, significantly reducing [[integration_of_mcp_with_ai_applications | infrastructure integration complexity]] <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Enforcing Best Practices and Governance:** The centralized platform provides a mechanism to enforce [[best_practices_for_building_gen_ai_teams | best practices]] and governance, ensuring applications are built efficiently and responsibly <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

## Why a Dedicated GenAI Platform is Critical

Building an in-house GenAI platform is deemed critical for success <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. GenAI systems are fundamentally different from traditional AI systems <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>:
*   **Blurred Lines:** In traditional AI, there's a clear separation between model optimization and model serving, allowing AI engineers and product engineers to work on different tech stacks <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>. In GenAI, this line disappears; everyone can optimize overall system performance, creating new [[challenges_in_implementing_gen_ai_projects | challenges]] for tooling and [[best_practices_for_building_gen_ai_teams | best practices]] <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Compound AI Systems:** GenAI and agent systems are "compound AI systems," defined as tackling AI tasks using multiple interacting components, including multiple model calls, retrievers, or external tools <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. This requires skills across both AI engineering and product engineering <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **Bridging Skill Gaps:** The GenAI application platform serves to bridge the skill gaps between AI engineers and product engineers <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## Building a GenAI Team

Recruiting for a GenAI platform team can be challenging due to the specialized and evolving nature of the field <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.

### Ideal Candidate (The "Unicorn")
An ideal candidate possesses a rare combination of skills <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>:
*   Strong software engineering skills, particularly in [[leveraging_existing_infrastructure_for_ai_integration | infrastructure integration]] <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
*   Good developer product management skills for interface design <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
*   AI and data science background to understand the latest techniques <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   Hands-on and capable of learning rapidly <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>.

### Realistic Hiring Principles
Given the difficulty in finding a single "unicorn," LinkedIn follows several principles <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>:
1.  **Prioritize Software Engineering:** Core software engineering skills are prioritized over AI expertise <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
2.  **Hire for Potential:** Due to the fast-evolving nature of GenAI, experience can quickly become outdated. Hiring for potential allows individuals to adapt and grow <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
3.  **Build a Diversified Team:** Instead of seeking one person with all qualifications, LinkedIn hires a diverse team including full-stack software engineers, data scientists, AI engineers, data engineers, fresh graduates from top research universities, and individuals from startup backgrounds <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. This diverse team collaborates, allowing engineers to pick up new skills and evolve into ideal candidates <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
4.  **Emphasize Critical Thinking:** The GenAI landscape changes rapidly; solutions can become outdated in less than six months <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. The team constantly evaluates [[use_of_open_source_tools_for_ai_development | open source packages]], engages with vendors, and proactively deprecates solutions <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

## Key Takeaways for GenAI Platform Development

### Tech Stack Choice
*   **Python is Recommended:** LinkedIn strongly recommends Python. While they started with Java and Python, Python was chosen due to its prevalence in research and [[use_of_open_source_tools_for_ai_development | open source]] communities, and its scalability <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.

### Key Components to Build
*   **Prompt Source of Truth:** Essential for robust version control of prompts, which are akin to traditional model parameters. This is critical for operational stability to prevent accidental production edits and negative side effects <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Memory:** A crucial component for injecting rich data into the agent experience <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>.
*   **Uplifting APIs into Skills:** In the agent era, converting existing APIs into easily callable skills for agents is vital, requiring surrounding tooling and infrastructure <a class="yt-timestamp" data-t="00:15:42">[00:15:42]</a>.

### Scaling and Adoption
*   **Start Small, Solve Immediate Needs:** Instead of attempting to build a full-fledged platform initially, begin by addressing immediate needs. LinkedIn started with a simple Python library for orchestration and gradually expanded <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.
*   **Focus on Infrastructure and Scalable Solutions:** Leverage existing infrastructure where possible. For instance, LinkedIn successfully used its [[integration_of_mcp_with_ai_applications | messaging infrastructure]] as a memory layer, which proved both cost-efficient and scalable <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. This highlights the importance of [[leveraging_existing_infrastructure_for_ai_integration | leveraging existing infrastructure for AI integration]].
*   **Prioritize Developer Experience:** The ultimate goal of the platform is to maximize developer productivity <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>. Adoption is key for success, so align the technology with developers' existing workflows to ease the transition and promote success <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>. This is part of [[leadership_and_organizational_strategies_for_ai_integration | leadership and organizational strategies for AI integration]].

More technical details on LinkedIn's GenAI platform development can be found on their engineering blog <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>.