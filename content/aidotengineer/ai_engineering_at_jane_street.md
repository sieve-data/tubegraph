---
title: AI Engineering at Jane Street
videoId: 0ML7ZLMdcl4
---

From: [[aidotengineer]] <br/> 

At Jane Street, the AI Assistant team is focused on maximizing the value derived from [[large_language_models | large language models]] (LLMs) across the firm, particularly within developer tools <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. John Kzi, who has a background in developer tools, highlights the open-ended opportunities LLMs present, allowing for the creation of virtually anything imaginable <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The pace of progress in models is only outstripped by the creativity in their application <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Unique Challenges

Jane Street faces specific challenges that make the adoption of off-the-shelf AI tooling difficult <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
Their primary development platform is OCaml, a powerful yet obscure functional language used in theorem proving, formal verification, and programming language development <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. Jane Street uses OCaml for almost everything, including web applications (via JS of OCaml transpiler), Vim plugins (via Viml transpiler), and even FPGA code (via Hardcaml) <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

The main reasons market tools are unsuitable for OCaml include:
*   **Model Proficiency**: LLMs are generally not proficient in OCaml, largely due to the limited amount of public training data available for the language <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>. Jane Street's internal OCaml codebase likely exceeds the total combined OCaml code existing outside its walls <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Internal Systems**: The company has built its own core development infrastructure, including build systems, a distributed build environment, and a code review system called Iron <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>. They operate on a giant monorepo stored in Mercurial instead of Git <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. Additionally, 67% of the firm uses Emacs as their primary editor <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Aspiration**: The team wants the flexibility to apply LLMs across various parts of their development flow without being hampered by system boundaries, for tasks like resolving merge conflicts, generating feature descriptions, or identifying code reviewers <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.

## Approach to Large Language Models in Dev Tools

Jane Street's approach involves building custom models, integrating them into editors, and developing robust evaluation capabilities <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Custom Model Building
Training custom models, though expensive and time-consuming, was validated after reading Meta's "Code Compose" paper <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. This project detailed fine-tuning a model for Hack, a language similar to OCaml in its primary usage within a single company <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.

Their initial naive assumption that showing a model their code would instantly yield a better version was incorrect <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Effective model training requires providing examples in the shape of the desired output <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

The specific goal for their model was to generate diffs given a prompt <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. Users should be able to describe a desired change in an editor, and the model would suggest a multi-file diff (e.g., modifying test, `.ml`, and `.mli` files) <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. These diffs needed to apply cleanly, be likely to type-check, and ideally be up to 100 lines long <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

#### Data Collection
To achieve this, they needed training data in the "context-prompt-diff" format <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Features/Pull Requests (Iron)**: While their internal code review system "Iron" (similar to pull requests) contains human-written descriptions and diffs, these are generally too large (often 500-1000 lines) and the descriptions are too detailed, unlike the concise prompts a user would give in an editor <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
*   **Commits**: Commits are smaller but are used as checkpoints rather than isolated changes with descriptions <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
*   **Workspace Snapshotting**: The chosen approach involves taking snapshots of developer workstations every 20 seconds, along with the build status <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. A "green-to-red-to-green" build pattern often indicates an isolated change where a developer broke and then fixed the build <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. Capturing the build error at the "red" state and the diff from "red" to "green" provides valuable training data for error recovery <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.
*   **Description Generation**: LLMs are used to generate detailed descriptions of changes, which are then filtered down to approximate human-like prompt brevity <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

#### Reinforcement Learning
Reinforcement learning aligns the model's output with human notions of "good code" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Definition of Good Code**:
    *   Code that parses <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
    *   For OCaml, statically typed code that type-checks <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
    *   Code that compiles and passes tests <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Code Evaluation Service (CES)**: To facilitate reinforcement learning, they built CES <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. This service pre-warms builds to a green state, then workers apply diffs from the model and report whether the build status turns red or green <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Over months, this continuous process helps the model learn to write code that compiles and passes tests <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

### Model Evaluation
The same CES setup used for reinforcement learning can be leveraged for model evaluation by holding out some of the RL data <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. This allows testing the model's ability to write functional code <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. The importance of meaningful evaluations is underscored by an anecdote where an early code review model, trained on human examples, responded with "I'll do it tomorrow" <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

## Editor Integrations
The ultimate test of these models is their utility for human developers <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
When building editor integrations, three main goals were considered:
1.  **Avoid Duplication**: Support for NeoVim, VS Code, and Emacs required a single implementation for context building and prompting strategies <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
2.  **Maintain Flexibility**: The architecture needed to allow swapping models or prompting strategies as needed <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Collect Metrics**: Measure latency and diff application success to understand real-world user experience <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>.

### AI Development Environment (AID)
The chosen architecture features an AI Development Environment (AID) service as a sidecar application on the developer's machine <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.
*   AID handles prompt and context construction, and build status observation <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>.
*   Thin layers are written on top of AID for each editor <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   This sidecar approach means changes to AID can be deployed and restarted centrally, updating all developers without requiring individual editor restarts <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

#### Editor Examples
*   **VS Code**: AID integrates into the sidebar, similar to Copilot, allowing users to ask for and receive multi-file diffs through a visual interface <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   **Emacs**: For Emacs users, who prefer text-based workflows, the AID experience is built into a Markdown buffer, allowing users to interact with text, ask questions, and append content via keybinds <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

### Benefits of AID Architecture
*   **Pluggability**: AID allows seamless swapping of models, changes to context building, and support for new editors <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **Domain-Specific Tools**: Different parts of the company can supply specific tools that become available across all editors without needing individual integrations <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **A/B Testing**: The architecture supports A/B testing different approaches, such as routing portions of the company to different models and comparing acceptance rates <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.
*   **Adaptability**: AID provides a strong foundation that pays off over time, enabling rapid adaptation to changes in [[large_language_models | large language models]] <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

## Broader Applications
Beyond developer tools, the team is exploring other applications of LLMs, including new ways to apply RAG (Retrieval-Augmented Generation) within editors, large-scale multi-agent workflows, and work with reasoning models <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. The consistent approach across all these initiatives is to maintain pluggability, build a strong foundation, and enable the rest of the company to contribute domain-specific tooling <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.