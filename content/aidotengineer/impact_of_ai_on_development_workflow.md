---
title: Impact of AI on development workflow
videoId: 9u6xvcNJaxc
---

From: [[aidotengineer]] <br/> 

The integration of Artificial intelligence (AI) into the software development lifecycle has led to a significant shift, prompting a move towards what is known as "AI-native development" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This new paradigm introduces a different set of practices and workflows, impacting how developers interact with their tasks and collaborate <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

Technology has evolved rapidly from simple Large Language Models (LLMs) to advanced applications like Retrieval-Augmented Generation (RAG) and indexing codebases, integrating functions and ultimately leading to the emergence of AI agents and even teams of agents <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. This evolution mirrors the explosion seen with cloud-native development, introducing new ways of working <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. With AI, existing tasks are either replaced, enhanced, or entirely new tasks emerge, fundamentally changing the development process <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

This transformation can be distilled into four core patterns <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## Four Patterns of AI-Native Development

While the developer remains at the center, the patterns shift their roles into different areas of the software development ecosystem <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

### 1. From Producer to Manager

Historically, developers have been the primary producers of code. With AI, agents are increasingly responsible for code generation, shifting the developer's role to managing these agents <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>. This change is already visible, as developers spend less time coding and more time reviewing <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. This increases the cognitive load during review, requiring developers to focus more on the "thinking work" <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.

To mitigate this increased cognitive load, new review methods are emerging:
*   **Summarized Reviews**: Instead of clunky "diff views" or verbose "chat views," new review interfaces strip content down to a summary, allowing developers to quickly approve or reject changes <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Step-by-Step Review**: For reviewing multiple files, a structured, step-by-step flow helps manage the review process <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Visual Reviews**: Reviewing diagrams that illustrate changes is often easier and more efficient than reviewing lines of text, making it simpler to spot errors and impacts <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

This leads to the concept of a "moldable development environment," where Integrated Development Environments (IDEs) adapt to the specific code review and domain at hand, moving beyond endless streams of text <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

Furthermore, the management role extends to:
*   **Autocommitting**: Some systems automatically commit code if the impact is low or risk is accepted, allowing developers to review only if they disagree <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   **Checkpoints for Agents**: For longer-running agents, checkpoints allow developers to jump in at specific points to regenerate code, avoiding repetitive reviews <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Setting Constraints and Permissions**: Similar to a human manager, developers can set rules, lock files, and define permissions for AI agents, establishing "guardrails" for their actions <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Cost Monitoring**: As agents run longer, monitoring the cost of their operations becomes crucial, turning developers into managers of AI-driven expenses <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

This pattern shifts the developer from a code producer to an operations manager, focusing on the work being done by a team of agents <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

### 2. From Implementation to Intent

The second pattern involves a shift from caring about the explicit implementation details to specifying the *intent* to AI agents <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. Developers articulate what they want the agents to build, and the agents figure out the how <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>.

Key aspects of this shift include:
*   **Specification Files**: Simple markdown files can serve as specification files, added to prompts to provide detailed requirements without rewriting them repeatedly <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>. This helps build shared functional or technical specifications <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.
*   **AI-Generated Plans**: AI can help build a step-by-step plan based on desired outcomes, moving towards task-oriented development <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Intent-Based Coding**: The focus moves away from chat-based text completion towards defining tasks that translate into specifications, plans, and ultimately, code <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Specification-Centric Tools**: Entire tools are becoming specification-centric, where functional, technical, and security requirements are the primary inputs, and the workflow revolves around these specifications, potentially with less direct code interaction <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Program Manager Role**: Developers may transition to roles akin to program managers, managing the overall process rather than the minute coding details <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

This pattern moves the developer towards a QA or architect role, focusing on defining the "what" rather than the "how" <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

### 3. From Delivery to Discovery

With AI handling much of the delivery (through pipelines, managers, and specifications), developers increasingly focus on discovering the *right intent*—exploring ideas and working through problems <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

This involves:
*   **Rapid Prototyping**: AI enables much faster design and prototyping, allowing for quick exploration of different ideas and iterations <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Multiple Iterations and Versions**: AI can generate multiple versions or iterations, enabling developers to choose the best one and suggesting ideas they might not have considered <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Refined Design-to-Code Loop**: The process of designing, coding, redesigning, and modifying code becomes a refined loop focused on discovery and exploration <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Customer-Driven Prototyping**: AI allows even customers to "vibe code" their desired interfaces on top of existing products, acting as a form of "A/B testing on steroids" to refine the perfect product <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

This shifts the developer role more towards a product owner, focusing on understanding and exploring what needs to be built <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

### 4. From Data to Knowledge

The final pattern involves transforming all learned insights and produced content during the development process into captured knowledge <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. The goal is to capture knowledge to avoid solving the same problems repeatedly <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

Sources of knowledge include:
*   **Production Issues**: Learning from what goes wrong in production and feeding that back into code improvements <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Incident Response**: Extracting lessons from incidents, identifying failures, and establishing new guidelines or technology improvements <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
*   **Code as Lessons**: Turning existing code into lessons to reduce onboarding time for new team members or preserve knowledge when someone leaves <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
*   **Feature Memory**: Tracking past feature attempts, decisions, and outcomes in a "feature memory" to prevent redundant efforts and preserve architectural decisions <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

Ideally, this knowledge capture happens "in the flow" – as developers chat and code, AI agents can identify and save important information as knowledge <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. This creates a beneficial loop where both humans and AI learn simultaneously, using that knowledge to answer questions and improve future coding solutions <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

This pattern transforms developers into data engineers, focusing on turning data into actionable knowledge <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

## Conclusion

These four patterns illustrate that the [[impact_of_ai_coding_agents_on_software_engineering | Impact of AI coding agents on software engineering]] goes beyond simply helping developers type faster <a class="yt-timestamp" data-t="00:13:14">[00:13:14]</a>. It enables developers to become more like senior developers, engaging in activities beyond mere coding: managing operations, specifying intent, discovering product needs, and capturing organizational knowledge <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>. This shift highlights the [[benefits_and_challenges_of_using_ai_in_workflow | benefits and challenges of using AI in workflow]] and the broader [[ai_in_workflow_automation_and_augmentation | AI in workflow automation and augmentation]]. The landscape of tools supporting this new paradigm is rapidly expanding, with hundreds of tools available to explore these new ways of working <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>.