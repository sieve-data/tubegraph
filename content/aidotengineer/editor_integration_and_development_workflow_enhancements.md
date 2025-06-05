---
title: Editor integration and development workflow enhancements
videoId: 0ML7ZLMdcl4
---

From: [[aidotengineer]] <br/> 

At Jane Street, the AI Assistant team, led by John Kzi, aims to maximize the value derived from large language models (LLMs) in development tools <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. LLMs offer a unique opportunity for open-ended tool development, limited primarily by creativity <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>.

## Unique Development Environment Challenges

Jane Street's adoption of off-the-shelf tooling for LLMs is complicated by several factors:
*   **OCaml as a Primary Language**: OCaml is a powerful, functional, but obscure language, primarily used in theorem proving or formal verification <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. Jane Street uses OCaml for almost everything, including web applications (transpiled to JavaScript via JS of OCaml), Vim plugins (transpiled to Vimscript via VAML), and FPGA code (HardCaml) <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>.
*   **LLM Proficiency with OCaml**: Models generally perform poorly with OCaml because the amount of OCaml code within Jane Street's internal systems likely exceeds the total combined amount of OCaml code available globally for training <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.
*   **Internal Tooling**: The company has built its own custom tools, including build systems, a distributed build environment, and a code review system called Iron <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>.
*   **Monorepo and Version Control**: All software is developed on a giant monorepo, which is stored in Mercurial, not Git <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.
*   **Editor Preference**: A significant portion (67%) of the firm uses Emacs, contrasting with more common editors like VS Code <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
*   **Ambitious Goals**: There's a desire to deeply integrate LLMs across the entire development flow for tasks like resolving merge conflicts, generating feature descriptions, or identifying code reviewers, without being constrained by system boundaries <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>.

## Approach to LLMs in Developer Tools

Jane Street's strategy focuses on:
*   Building custom models <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.
*   Developing robust editor integrations <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.
*   Establishing comprehensive model [[iterative_improvement_of_evaluation_processes | evaluation]] processes <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.

### Building Custom Models for Diff Generation

Inspired by Meta's CodeCompose project, which fine-tuned models for Hack (another language primarily used at one company) <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>, Jane Street set a goal: to generate diffs from a prompt within the editor <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>. These diffs should ideally be multi-file, apply cleanly, typecheck, and be up to 100 lines long <a class="yt-timestamp" data-t="05:43:00">[05:43:00]</a>.

The process involves two main phases:

#### 1. Supervised Training Data Collection

To train models effectively, examples in the specific "Context + Prompt + Diff" shape are needed <a class="yt-timestamp" data-t="06:16:00">[06:16:00]</a>. Traditional data sources proved unsuitable:
*   **Code Review System (Iron)**: While containing descriptions and diffs, descriptions are too detailed (like pull request descriptions) and diffs are often too large for single-shot generation (500-1000 lines) <a class="yt-timestamp" data-t="07:01:00">[07:01:00]</a>.
*   **Commits**: Commits are used as checkpoints rather than isolated changes and lack descriptions <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>.

**Workspace Snapshotting**: The solution was to capture "isolated changes" by periodically snapshotting developer workstations (e.g., every 20 seconds) and their build status <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>. A "Green-to-Red-to-Green" pattern in the build status often signifies an isolated change where a developer introduced a bug and then fixed it <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. By capturing the build error at the "Red" state and the diff to the "Green" state, training data for error recovery is created <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. An LLM is then used to generate a concise, human-like description for the prompt part of this training data <a class="yt-timestamp" data-t="09:08:00">[09:08:00]</a>.

#### 2. Reinforcement Learning

This phase aligns the model's output with human notions of "good code" <a class="yt-timestamp" data-t="09:31:00">[09:31:00]</a>. "Good code" is defined as:
*   Parsable by the OCaml parser <a class="yt-timestamp" data-t="09:47:00">[09:47:00]</a>.
*   Type-checks successfully <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>.
*   Compiles and passes tests <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>.

**Code Evaluation Service (CES)**: A "build service" called CES was developed for this purpose <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>. It pre-warms a build, and then workers apply diffs from the model, checking if the build status remains green <a class="yt-timestamp" data-t="10:47:00">[10:47:00]</a>. This continuous feedback loop over months helps align the model to generate compilable and test-passing code <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>. This setup is also used for [[iterative_improvement_of_evaluation_processes | model evaluation]] <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.

> [!EXAMPLE] Training Challenges
> A code review model, trained on human examples, once responded to a code review request with "I'll do it tomorrow" <a class="yt-timestamp" data-t="12:08:00">[12:08:00]</a>. This highlights the importance of meaningful [[iterative_improvement_of_evaluation_processes | evaluations]] to prevent models from going "off the rails" <a class="yt-timestamp" data-t="12:22:00">[12:22:02]</a>.

### Editor Integrations: The AI Development Environment (Aid)

The real test for models is their utility for humans <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>. Jane Street's editor integrations are built with three key ideas:
1.  **Write Once, Integrate Across Editors**: Avoid re-writing context and prompting strategies for different editors (Neovim, VS Code, Emacs) <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.
2.  **Maintain Flexibility**: Be able to easily swap models or prompting strategies <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>.
3.  **Collect Metrics**: Gather real-world data on latency and diff application success <a class="yt-timestamp" data-t="13:17:00">[13:17:00]</a>.

**Architecture of Aid**: The AI Development Environment (Aid) acts as a sidecar application on the developer's machine <a class="yt-timestamp" data-t="13:55:00">[13:55:00]</a>.
*   Aid handles prompt construction, context building, and build status integration <a class="yt-timestamp" data-t="13:41:00">[13:41:00]</a>.
*   Thin layers are built on top of Aid for each editor <a class="yt-timestamp" data-t="13:49:00">[13:49:00]</a>.
*   Changes to Aid can be deployed by restarting the service, without requiring editor restarts <a class="yt-timestamp" data-t="14:00:00">[14:00:00]</a>.

**Editor-Specific Implementations**:
*   **VS Code**: Integrates into the sidebar, similar to Copilot, providing a visual interface for multi-file diffs <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.
*   **Emacs**: The Aid experience is integrated directly into a markdown buffer, allowing users to interact with text buffers and use familiar keybinds to append content <a class="yt-timestamp" data-t="14:35:00">[14:35:00]</a>.

## Benefits and Future Directions

Aid's architecture enables significant flexibility:
*   **Pluggable Components**: New models, context-building methods, and editor support can be easily integrated <a class="yt-timestamp" data-t="14:58:00">[14:58:00]</a>.
*   **[[using_offtheshelf_tools_for_app_enhancement | Domain-Specific Tooling]]**: Different areas of the company can supply specific tools that become available across all integrated editors without individual integrations <a class="yt-timestamp" data-t="15:15:00">[15:15:00]</a>.
*   **A/B Testing**: Different approaches can be A/B tested (e.g., sending 50% of users to one model vs. another) to determine which yields higher acceptance rates <a class="yt-timestamp" data-t="15:28:00">[15:28:00]</a>.
*   **Iterative Improvement**: Aid is an investment that pays off over time, allowing rapid adaptation to changes in LLM technology <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.

The team is also exploring other avenues, including applying RAG (Retrieval-Augmented Generation) within editors, large-scale multi-[[developing_ai_agents_and_agentic_workflows | agentic workflows]], and [[ai_integration_and_tool_calling | reasoning models]] <a class="yt-timestamp" data-t="16:03:00">[16:03:00]</a>. The core philosophy remains consistent: maintain pluggability, build a strong foundation, and enable the rest of the company to contribute domain-specific tooling <a class="yt-timestamp" data-t="16:16:00">[16:16:00]</a>.