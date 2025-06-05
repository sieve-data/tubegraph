---
title: AI native development patterns
videoId: 9u6xvcNJaxc
---

From: [[aidotengineer]] <br/> 

AI native development signifies a shift in how software engineering workflows are approached, moving beyond merely [[ai_enhanced_vs_ai_native_businesses | sprinkling AI]] on existing processes to fundamentally redefine practices <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The rapid advancement from simple Large Language Models (LLMs) to RAG (Retrieval-Augmented Generation), code indexing, and the emergence of agents and teams of agents has driven this evolution <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This new paradigm impacts tasks by either replacing, enhancing, or introducing new responsibilities for developers <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

Four key patterns define this shift in AI native development <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>:

## 1. From Producer to Manager

Historically, developers have been the primary producers of code <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. With AI agents now capable of producing code, the developer's role is evolving into managing these agents <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

Key aspects of this shift include:
*   **Increased Review Time & Cognitive Load**: While coding time decreases due to AI generation, the time spent reviewing code increases, elevating the cognitive load on developers <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
*   **New Review Methods**: To mitigate cognitive load, new review methods are emerging, such as:
    *   Summary views that strip down code to essential elements for quick "yes/no" decisions <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Step-by-step reviews for multiple files, breaking down the process into a clear flow <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
    *   Visual reviews, like generating diagrams of code changes, which are easier to spot errors in compared to raw text <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
*   **Moldable Development Environments**: Integrated Development Environments (IDEs) are expected to adapt to specific code review needs, domains, and specifics, rather than presenting endless streams of text <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Automated Commit Acceptance**: Some approaches propose auto-committing AI-generated code based on heuristics, allowing for post-commit review if issues arise <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
*   **Checkpoints for Longer-Running Agents**: For extended AI agent operations, checkpoints allow developers to intervene or regenerate from specific points, avoiding repeated full reviews of the entire thought process <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Setting Constraints and Permissions**: Developers, much like managers, define rules for AI agents, such as locking files or specifying permissions to control what the AI can and cannot do <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Cost Monitoring**: As AI operations become longer-running, monitoring the cost of AI agent activities (e.g., per prompt or task) becomes an important management consideration <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

## 2. From Implementation to Intent

This pattern involves a shift from developers focusing on the detailed implementation of code to primarily specifying the desired intent to AI agents <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

Key aspects of this shift include:
*   **Specification Files**: Simple markdown files or similar documents can serve as explicit specification files, defining functional or technical requirements that the AI uses to generate code, reducing repetitive prompting <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **AI-Generated Plans**: AI tools can translate developer intent into step-by-step execution plans <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Intent-Based Coding**: The focus moves from chat-based interactions or text completion to defining tasks and allowing the AI to build a plan and generate the code <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
*   **Specification-Centric Workflows**: Entire development workflows can become specification-centric, where functional, technical, and security requirements are primarily defined through specifications, and the code generation process is largely abstracted <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Program Manager Role**: Developers may evolve into a role akin to a program manager, overseeing the process rather than deeply engaging with the code itself <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

## 3. From Delivery to Discovery

This pattern emphasizes discovering the right problems to solve and ideas to build, rather than solely focusing on delivering code to production <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

Key aspects of this shift include:
*   **Accelerated Prototyping**: AI can rapidly design and create prototypes, enabling faster exploration of ideas and requirements <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Multiple Iterations and Suggestions**: AI can generate multiple versions and iterations of designs or features, allowing developers to choose the best option and suggesting ideas they might not have considered <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Refined Discovery Process**: The entire design-to-code process becomes an iterative loop focused on exploration and refinement <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
*   **Customer Vibe Coding**: Customers could potentially use AI to "vibe code" or directly interact with interfaces, allowing them to adapt products to their needs, similar to an A/B testing approach on steroids <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>. This aligns with [[ai_accelerated_need_finding | AI accelerated need finding]].

## 4. From Data to Knowledge

This pattern focuses on transforming insights gained throughout the development process and beyond into valuable, accessible knowledge <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

Key aspects of this shift include:
*   **Learning from Production Issues**: Knowledge can be extracted from production incidents, informing future code changes <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>.
*   **Incident Response Lessons**: AI can help derive lessons from incident responses, identifying failures, guiding new guidelines, or highlighting technologies for improvement <a class="yt-timestamp" data-t="00:10:58">[00:11:00]</a>.
*   **Code as Lessons**: Code itself can be transformed into lessons, reducing onboarding time for new team members or capturing knowledge from departing personnel <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. This relates to [[ai_integration_in_documentation_teams | AI integration in documentation teams]].
*   **Feature Memory**: Maintaining a "feature memory" tracks past feature attempts and decisions, preventing re-exploration of dismissed ideas and preserving architectural choices <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
*   **In-Flow Knowledge Capture**: AI agents can suggest saving important information as knowledge during real-time chat and coding interactions, creating a beneficial learning loop for both humans and AI <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **Knowledge Application**: Captured knowledge can be used to answer questions from others and improve future code solutions <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.

## Conclusion

These four patterns — Producer to Manager, Implementation to Intent, Delivery to Discovery, and Data to Knowledge — illustrate how AI reshapes the developer's role <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Developers move into areas traditionally associated with operations (managing), quality assurance/architecture (specifying intent), product ownership (discovery), and data engineering (knowledge capture) <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>. Ultimately, AI enables developers to operate more like highly experienced senior developers, extending beyond mere "faster typing" to encompass broader strategic and intellectual contributions <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.

For further exploration of AI native development tools and concepts, resources like nativedev.io curate a landscape of hundreds of tools <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>.