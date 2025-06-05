---
title: Integration of large language models in development
videoId: 0ML7ZLMdcl4
---

From: [[aidotengineer]] <br/> 

John Kzi leads the AI Assistant team at Jane Street, which aims to maximize the value Jane Street can derive from [[Large language models and selfimprovement | large language models]] (LLMs) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Kzi's background is primarily in dev tools, having worked at GitHub and other development tool companies <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. He views LLMs as presenting a significant opportunity due to their open-ended nature, allowing the creation of almost anything imaginable <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The pace of progress in models is only outmatched by the creativity in how to employ them <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Unique [[Challenges and solutions in using large language models | Challenges]] at Jane Street <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>

Jane Street's specific operational choices make adopting off-the-shelf tooling more difficult than for other companies <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

The primary challenges include:

*   **OCaml as a Development Platform**: Jane Street primarily uses OCaml, a powerful but obscure functional language <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. OCaml is often used in theorem proving, formal verification, or to write programming languages <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Jane Street uses OCaml for almost everything, including:
    *   Web applications, transpiling OCaml bytecode to JavaScript via `JS of OCaml` <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   Vim plugins, transpiling OCaml to Vimscript via `Vim OCaml` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   FPGA code, written in an OCaml library called `HardCaml` instead of Verilog <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Model Limitations with OCaml**: Existing LLMs are not proficient in OCaml, mainly due to the limited amount of OCaml data available for training in the public domain <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Jane Street's internal OCaml codebase may even exceed the total combined OCaml code outside their walls <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
*   **Self-Imposed Complexity**: Jane Street has built its own:
    *   Build systems <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Distributed build environment <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   Code review system, called "Iron" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   Software is developed on a giant monorepo, stored in Mercurial instead of Git <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
    *   Approximately 67% of the firm uses Emacs as their primary editor <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Aspiration for Deep LLM Integration**: The company desires to apply LLMs across various parts of their development workflow (e.g., resolving merge conflicts, building feature descriptions, identifying code reviewers) without being constrained by system boundaries <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

## Jane Street's Approach to LLMs in Developer Tools <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>

Jane Street's strategy focuses on:
*   [[Building and deploying large language models | Building custom models]] <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   Developing robust editor integrations <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   Establishing comprehensive model evaluation capabilities <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Custom Model Development <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>

While training models is expensive and complex <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>, Jane Street was encouraged by Meta's "Code Compose" paper, which detailed successful fine-tuning of a model for Hack, a language primarily used at one company (similar to OCaml's niche use) <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. (Interestingly, Hack is implemented in OCaml <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>).

Initially, they naively thought they could fine-tune an off-the-shelf model by simply showing it their code <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. However, it became clear that models need to see examples in the specific "shape" of the questions they are expected to answer <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.

**Goal**: The team's primary goal was to generate diffs given a prompt <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. This meant a user in an editor could describe a desired change, and the model would suggest a multi-file diff (e.g., modifying a test file, an `.ml` file, and an `.mli` header file) <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. The diffs needed to apply cleanly and have a high likelihood of type-checking successfully, targeting changes up to 100 lines <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

**Training Data Shape**: To achieve this, training data needed to be in the form of: `context`, `prompt`, `diff` <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

#### Data Collection Strategy <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>

*   **Initial Ideas (and why they failed)**:
    *   **Features (Pull Requests)**: While features in their "Iron" code review system contain human-written descriptions and code diffs <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>, their descriptions are too verbose for editor prompts (e.g., multi-paragraphs vs. "fix that error") <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. Also, features are often very large (500-1000 lines), requiring automated splitting <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    *   **Commits**: Jane Street uses commits as checkpoints, not isolated changes with descriptions <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>. They also share the problem of not being isolated changes <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Workspace Snapshotting**: This is the chosen approach <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
    *   Snapshots of developer workstations are taken frequently (e.g., every 20 seconds) <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.
    *   Build status (errors, green) is also snapshotted <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
    *   Patterns like "green to red to green" builds often indicate an isolated change <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
    *   A "red to green" transition signifies a developer fixing an error <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. The build error at the "red" state and the diff from "red" to "green" are used as training data to help the model recover from mistakes <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
    *   **Description Generation**: [[Using language models to generate text | Large language models]] were used to generate detailed descriptions of changes, which were then filtered down to human-like prompt levels <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

#### Reinforcement Learning and Defining "Good Code" <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>

After supervised training, reinforcement learning aligns the model with what humans consider "good code" <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Good OCaml code is defined as:
*   Parsable <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   Type-checks successfully <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   Compiles and passes tests <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

To facilitate this, Jane Street built the **Code Evaluation Service (CES)** <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
*   CES acts as a faster build service <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
*   It pre-warms a build to a "green" state <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   Workers continuously take diffs from the model, apply them, and determine if the build status turns red or green <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   This feedback loop, used over months, helps align the model to write code that actually compiles and passes tests <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

### Model Evaluation <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>

The same CES setup used for reinforcement learning is also used for evaluating models <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. By holding out some RL data, they can test the model's ability to write functional code <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

**Importance of Meaningful Evaluations**:
Training can have "catastrophic but hilarious" results <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>. For example, a code review model trained on human examples once responded to a review request with "I'll do it tomorrow" <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Meaningful evaluations are crucial to prevent models from going "off the rails" and wasting resources <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

### Editor Integrations: The AI Development Environment (AID) <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>

The ultimate test for models is human utility <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. Jane Street built editor integrations to expose these models to developers.

**Integration Goals**:
1.  **Write Once**: Avoid rewriting context-building and prompting strategies for each supported editor (Neovim, VS Code, Emacs) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
2.  **Maintain Flexibility**: Allow swapping models or prompting strategies easily, anticipating future fine-tuned models <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Collect Metrics**: Gather real-world data on latency and diff application success to gauge effectiveness <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

**Architecture: AID as a Sidecar Application**:
*   The AI Development Environment (AID) handles prompt construction, context building, and build status visibility <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>.
*   Thin layers are built on top of AID for each editor <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   AID runs as a sidecar application on the developer's machine <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. This allows changes to AID to be deployed and restarted on all machines without requiring developers to restart their editors <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

**Editor Experiences**:
*   **VS Code**: A visual sidebar interface, similar to Copilot, allows asking for and receiving multi-file diffs <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Emacs**: The AID experience is integrated into a Markdown buffer, allowing users to interact via text, ask questions, and use keybinds to append content <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

**AID's Flexibility and Future**:
AID's architecture makes it highly pluggable <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>, enabling:
*   Swapping in new models <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.
*   Changes to context building strategies <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   Adding support for new editors <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   Integrating domain-specific tools from different company areas, making them available across all editors without individual integrations <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
*   A/B testing different approaches (e.g., routing 50% of users to one model and 50% to another to determine acceptance rates) <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

AID represents a long-term investment, allowing Jane Street to quickly adapt to changes in [[development_of_qwen_large_language_models | large language models]] by modifying a single component downstream of the editors <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

### Future Directions <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>

Jane Street is also exploring:
*   Applying Retrieval-Augmented Generation (RAG) within editors <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.
*   Large-scale multi-agent workflows <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
*   Working with reasoning models <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

Their consistent approach involves maintaining pluggability, building a strong foundation, and enabling other parts of the company to contribute domain-specific tooling <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.