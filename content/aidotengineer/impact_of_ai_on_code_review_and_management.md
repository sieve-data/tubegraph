---
title: Impact of AI on Code Review and Management
videoId: 9u6xvcNJaxc
---

From: [[aidotengineer]] <br/> 

The advent of Generative AI (GenAI) has profoundly impacted the software development workflow, moving technology beyond simple Large Language Models (LLMs) to include RAG (Retrieval-Augmented Generation), code indexing, and sophisticated agents [00:00:16]. This shift necessitates new "AI native" practices, fundamentally changing how developers work [00:00:47]. Tasks are now either replaced, enhanced, or new ones emerge entirely [00:01:14].

One of the most significant shifts is the transition of developers from "producers" to "managers" of code [00:02:13]. Instead of primarily writing code, developers increasingly manage AI agents that generate it [00:02:21].

## Shift from Producer to Manager

As AI takes on more code generation, developers spend less time coding and more time reviewing [00:02:36]. This leads to an increase in cognitive load during reviews, as developers are now responsible for the "thinking work" involved in validating AI-generated code [00:02:45].

### Enhancing Code Review for AI-Generated Code

To mitigate the increased cognitive load during code review, new approaches are emerging:

*   **Improved Review Interfaces**
    *   Traditional diff views (red/green) and chat views are often clunky or verbose for reviewing AI-generated code [00:03:05].
    *   The "what matters" view summarizes changes, allowing for quick "yes/no" decisions [00:03:12].
    *   For reviewing multiple files, a step-by-step breakdown of the review process helps manage complexity [00:03:34].
    *   Reviewing visual diagrams of changes, rather than just text, makes errors and impacts easier to spot [00:03:51].
*   **Moldable Development Environments**
    *   Integrated Development Environments (IDEs) are expected to adapt to specific code review needs and domains, moving beyond endless streams of text to reduce cognitive load [00:04:08].

### Managing AI Agents and Workflow

Beyond the review process itself, AI also impacts the broader management of code development:

*   **Automated Commits**
    *   AI can auto-commit code, potentially based on heuristics for low risk or impact [00:04:36]. Manual review becomes an option if an issue is detected [00:04:40].
*   **Managing Longer-Running Agents**
    *   AI agents now have checkpoints, allowing developers to jump into a specific point in the generation process and regenerate code from there. This reduces the need to review entire iterative cycles [00:05:05].
*   **Setting Constraints and Guardrails**
    *   Developers can define rules and permissions for AI agents, similar to how a manager sets guidelines for a human team. This includes locking files or specifying areas AI should not touch [00:05:27].
*   **Cost Monitoring**
    *   With longer-running AI agents, monitoring costs becomes important, as it's no longer just about a single prompt but the continuous operation of the agent [00:05:49].

This shift from producer to manager is just one of four emerging patterns in AI native development, where developers operate more like operations specialists [00:12:45], QA specialists [00:12:51], product owners [00:12:57], and data engineers [00:13:02]. These roles are often encompassed by senior developers, illustrating that AI's impact extends far beyond mere "faster typing" [00:13:05].

For more information on the landscape of tools supporting AI native development, resources like nativedev.io curate a comprehensive list of tools focusing on the intersection of coding, software engineering, and AI [00:13:21].