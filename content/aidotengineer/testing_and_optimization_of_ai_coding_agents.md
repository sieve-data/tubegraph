---
title: Testing and optimization of AI coding agents
videoId: Iw_3cRf3lnM
---

From: [[aidotengineer]] <br/> 

AI coding agents are emerging as a dominant force in software engineering, with projections indicating their widespread adoption by 2025 [01:00:00]. Augment, a company specializing in AI-powered developer tools, has developed an AI coding agent that has largely built itself, contributing over 90% of its 20,000 lines of code with human oversight [01:21:00]. This agent is expected to be released soon [01:54:00].

## Agent's Role in Self-Improvement
The AI coding agent demonstrates capabilities that span core feature implementation, test generation, and self-optimization.

### Implementing Core Features
The agent is capable of helping build [[integration_of_ai_coding_agents_with_thirdparty_tools | third-party integrations]] needed for its function as a software engineer, such as interacting with Slack, Linear, Jira, Notion, and Google search [01:40:00]. After initial integrations were added manually, the agent could implement new ones, like Google search, by identifying the correct files and interfaces within its own codebase [02:06:00]. In one instance, while adding a Linear integration, the agent autonomously used its previously written Google search integration to find the Linear API documentation, as it was not pre-memorized by its foundation model [02:21:00].

### Writing Tests
The agent can generate unit tests for its features, for example, creating unit tests for the Google search integration upon request [02:37:00]. This functionality is enabled by providing the agent with fundamental process management tools, allowing it to run and interact with subprocesses, manage infinite loops, and read output [02:48:00].

### Performing Optimization
The agent can profile and optimize its own performance [03:14:00]. When the agent was observed to be slow, it was tasked with profiling itself [03:16:00]. Utilizing its tools, it added print statements to its codebase, ran sub-copies of itself, and analyzed the output [03:22:00]. It discovered a bottleneck where repository files were being loaded and hashed synchronously [03:32:00]. To resolve this, the agent implemented a process pool for these operations and added a stress test to confirm the fix, significantly speeding up its processes [03:40:00]. This self-optimization capability is a less common example of AI agent functionality compared to feature or test writing [03:04:00].

## The Critical Role of Testing
[[testing_and_evaluation_of_ai_models | Testing and evaluation of AI models]] are paramount for the reliability and autonomy of AI agents.

### Challenges in Testing
AI agents, like humans, can make mistakes, especially in complex, hard-to-test scenarios [01:57:00]. An example cited is a race condition in a cache save function written by the agent [01:10:00]. This function, designed to prevent explicit failures from race conditions with a lock around JSON dumping, failed to account for a read-before-write scenario, leading to cache overwrites when multiple agents ran in parallel [01:43:00]. This issue was not caught by a test and was only discovered due to unexpected runtime behavior [01:12:00]. This highlights the necessity of thorough testing, particularly for less-tested parts of the codebase [01:14:00].

### Benefits of Robust Testing
[[test_driven_development_for_ai_agents | Test driven development for AI agents]] is crucial for enabling greater autonomy. Internal benchmarks show a significant improvement in bug-fixing performance when agents can run tests [01:51:00]. While a six-month upgrade to the foundation model improved a bug-fixing benchmark score by 4%, adding the ability for the agent to suggest fixes, run tests, and iterate up to four times led to a 20% gain on the same benchmark [01:25:00]. This demonstrates that better tests directly enable more autonomy and make agents "smarter" [01:49:00].

## Lessons Learned in AI Agent Development
Through their journey in [[building_and_improving_ai_agents | building and improving AI agents]], Augment has gathered several [[best_practices_and_lessons_learned_in_ai_agent_development | best practices and lessons learned in AI agent development]].

*   **Context is King:** A powerful and scalable "context engine" that provides access to various types of information (Slack, codebase, etc.) is critical for AI coding tools, regardless of LLM quality [01:07:00]. This context, combined with strong reasoning capabilities from foundation models and a safe code execution environment, forms the foundation for effective agent development [01:33:00]. The value of context sources is multiplicative; having access to both codebase and Slack, for instance, is four times as useful as having only one [01:53:00].
*   **Onboarding Agents is Crucial:** Just like human engineers, agents need to be "onboarded" to an organization's specific tools and practices [01:21:00]. This involves providing a knowledge base containing information the agent doesn't natively understand, such as internal tools (e.g., Graphite version control), tool stacks, test procedures, and style guides [01:28:00]. By dynamically searching this knowledge base, agents can learn and adapt to specific organizational contexts [01:03:00].
*   **Code Becomes Cheap:** When AI agents can write code efficiently, the bottleneck shifts from engineering hours to product insights and good design [01:15:00]. This allows for the exploration of more ideas and a focus on rapidly gathering customer feedback [01:27:00].
*   **Natural Language Interaction:** With a robust codebase awareness, users can provide natural language instructions, similar to communicating with a human engineer, and the agent can interpret and act upon them, such as "instrument agent's Google Search tool with logs" [01:41:00].
*   **Beyond Code Tasks:** Agents can perform tasks beyond writing code within the software development lifecycle [01:57:00]. Examples include reviewing pull requests and generating announcements, or even creating data visualizations from internal data [01:03:00].

## Future Outlook
The landscape of software engineering is rapidly changing with the advent of AI agents [01:57:00]. There's a compounding effect where agents are beginning to help build themselves, accelerating their improvement [01:11:00]. While code remains essential as a specification of systems, the human relationship with it is evolving [01:20:00]. Good test harnesses are becoming more critical than ever, especially for less-tested parts of the codebase [01:25:00]. The calculus of product development is also changing, with a greater emphasis on product work, gathering customer feedback, and building insights as code becomes cheaper to write [01:37:00].