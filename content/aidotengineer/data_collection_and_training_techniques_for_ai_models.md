---
title: Data Collection and Training Techniques for AI Models
videoId: 0ML7ZLMdcl4
---

From: [[aidotengineer]] <br/> 

John Kzi, from Jane Street's AI assistant team, focuses on maximizing value from large language models (LLMs) within the company <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. His background in Dev tools, including a long tenure at GitHub, highlights the transformative potential of LLMs due to their open-ended nature and rapid progress <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## Unique Challenges with AI Adoption at Jane Street

Jane Street faces specific challenges that make the adoption of off-the-shelf AI tooling difficult <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

### OCaml as a Development Platform
The primary hurdle is the company's pervasive use of OCaml, a powerful, functional, but obscure language <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. OCaml is typically used in theorem proving, formal verification, and writing programming languages <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Jane Street uses OCaml for almost everything, even transpiling it for web applications (JS of OCaml), Vim plugins (Vaml), and FPGA code (HardCaml) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

### Limitations of Current AI Models
Off-the-shelf models are not proficient in OCaml, primarily because the amount of OCaml code within Jane Street likely exceeds the total available OCaml data for training worldwide <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### Jane Street's Custom Tooling and Environment
The company's unique development environment further complicates matters:
*   Custom build systems and distributed build environments <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>
*   An internal code review system called Iron <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>
*   A giant monorepo application stored in Mercurial instead of Git <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>
*   A majority of the firm (67%) uses Emacs as their primary editor <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>

### Desire for Deep Integration
Jane Street aims to apply LLMs to various parts of their development flow, such as resolving merge conflicts, building feature descriptions, or identifying reviewers, without being limited by system boundaries <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Approach to Custom Models and Training

To address these challenges, Jane Street focuses on [[custom_model_building_and_code_evaluation_for_ai_systems | custom model building]], editor integrations, and robust [[testing_and_evaluation_of_ai_models | evaluation]] methods <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

### Inspiration from Meta's CodeCompose
The decision to train custom models, despite the cost and complexity, was influenced by Meta's CodeCompose project <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. CodeCompose fine-tuned a model for Hack, a language similar to OCaml in its primary use within a single company <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. (Interestingly, Hack is implemented in OCaml <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>).

### Defining the Model's Goal
Initially, a naive approach of showing an off-the-shelf model existing code proved ineffective <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. To achieve good outcomes, models need examples in the specific shape of the desired question <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Jane Street's goal became: generating multi-file diffs (e.g., modifying test, `.ml`, and `.mli` files) given a prompt from an editor <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. These diffs needed to apply cleanly and ideally type-check, targeting changes up to 100 lines <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

### Data Collection for Training

To achieve this, training data needed to reflect the "context, prompt, diff" shape <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

*   **Challenges with existing data**:
    *   **Features (pull requests)**: While containing descriptions and diffs, their descriptions are too formal (multiple paragraphs) compared to typical editor prompts like "fix that error" <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. They are also often too large, requiring an automated way to break them into smaller components <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    *   **Commits**: At Jane Street, commits are used as checkpoints, not isolated changes, and lack descriptions <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.

*   **Workspace Snapshotting (Primary [[innovations_in_ai_training_methods_and_new_benchmarks | Training Method]])**:
    *   Snapshots of developer workstations are taken frequently (e.g., every 20 seconds) along with their build status <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
    *   A "Green to Red to Green" pattern in the build status often indicates an isolated change <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
    *   The build error at the "Red" state becomes the prompt, and the diff from "Red to Green" becomes the training data to help the model recover from mistakes <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
    *   Descriptions for these diffs are generated by an LLM, then filtered down to match the expected human-written prompt style <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### Reinforcement Learning and Evaluation

After supervised training, reinforcement learning is critical to align the model with human expectations of "good code" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

*   **Definition of "Good Code"**:
    *   Parsable OCaml code <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>
    *   Type-checks <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>
    *   Compiles and passes tests <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>

*   **Code Evaluation Service (CES)**:
    *   A custom service built for efficient code evaluation during the reinforcement learning phase <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
    *   It pre-warms a build to a "green" state <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    *   Workers continually apply diffs generated by the model and report whether the build turns red or green <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
    *   This continuous feedback helps align the model to write code that compiles and passes tests <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
    *   The same setup is used for model [[testing_and_evaluation_of_ai_models | evaluation]], by holding out some of the reinforcement learning data <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

*   **Importance of Meaningful [[best_practices_for_ai_evaluation | Evaluation]]**:
    *   Training can lead to "catastrophic but hilarious results," such as a code review model responding "I'll do it tomorrow" because it was trained on human examples containing such phrases <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
    *   Meaningful evaluations are crucial to prevent models from going off-the-rails and wasting time/money <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

## Editor Integrations and Deployment

The ultimate test for models is whether they work for humans <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>. Jane Street developed an **AI Development Environment (AID)** to expose models to developers <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

### Design Principles for AID
1.  **Single Codebase**: Avoid writing the same context and prompting strategies three times for NeoVim, VS Code, and Emacs <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
2.  **Flexibility**: Allow swapping models or prompting strategies easily, anticipating future fine-tuned models <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Metrics Collection**: Gather real-world data on latency and diff application success to assess meaningfulness for users <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

### AID Architecture and [[strategies_for_ai_model_deployment | Deployment]]
*   AID acts as a sidecar application on the developer's machine <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.
*   It handles all prompt construction, context building, and integrates with build status <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   Thin layers are written on top of AID for each editor (VS Code, Emacs, NeoVim) <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   This architecture allows changes to AID to be deployed by simply restarting the service on all machines, without requiring editor restarts <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

### Editor-Specific User Interfaces
*   **VS Code**: Presents a visual sidebar similar to GitHub Copilot, allowing multifile diff requests <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Emacs**: The AI experience is integrated into a markdown buffer, catering to Emacs users' preference for text-based interaction and key binds for appending content <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

### Benefits of AID
*   **Pluggability**: Allows swapping in new models, changing context building, adding support for new editors, and incorporating domain-specific tools across all editors simultaneously <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **A/B Testing**: Enables A/B testing different approaches, e.g., sending 50% of users to one model and 50% to another to compare acceptance rates <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.
*   **Investment Payoff**: AID ensures that improvements in LLMs can be rapidly propagated to all developers by updating a single component downstream of the editors <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

## Ongoing Work and [[best_practices_for_building_ai_systems | Best Practices for AI Systems]]
The team continues to explore new applications, including applying RAG (Retrieval-Augmented Generation) within editors, developing large-scale multi-agent workflows ([[best_practices_and_lessons_learned_in_ai_agent_development | AI agent development]]), and working with reasoning models <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The core approach remains consistent: maintain pluggability, build a strong foundation, and enable other teams to contribute domain-specific tooling <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.