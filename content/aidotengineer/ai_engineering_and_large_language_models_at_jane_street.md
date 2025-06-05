---
title: AI Engineering and Large Language Models at Jane Street
videoId: 0ML7ZLMdcl4
---

From: [[aidotengineer]] <br/> 

John Kzi is part of the AI Assistant team at Jane Street, which aims to maximize the value Jane Street can derive from [[building_and_scaling_large_language_models | large language models]] (LLMs) <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Kzi's career has been spent in Dev tools, including time at GitHub <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. LLMs offer significant opportunities due to their open-ended nature, allowing for the creation of almost anything imaginable <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Unique Challenges at Jane Street

Jane Street's adoption of off-the-shelf tooling for LLMs is more difficult than for other companies <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. This difficulty stems from several factors:

*   **OCaml as Development Platform**: Jane Street uses OCaml extensively for development <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. OCaml is a powerful functional language, but it is obscure, primarily used in areas like theorem proving, formal verification, and programming language development <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
    *   **OCaml Transpilers**: For web applications, Jane Street writes OCaml and uses `JS of OCaml` to transpile to JavaScript <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. For Vim plugins, they use `Vaml` to transpile OCaml to Vim script <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. Even FPGA code is written using the `HardCaml` OCaml library instead of Verilog <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
    *   **LLM Proficiency**: [[large_language_models_in_ai_agents | Large language models]] are not proficient in OCaml, largely due to the limited amount of public OCaml training data compared to the volume of OCaml code within Jane Street <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Internal Tooling and Infrastructure**: Jane Street has built its own build systems, distributed build environment, and a code review system called "Iron" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Monorepo and Mercurial**: All software is developed on a giant monorepo application, which is stored in Mercurial instead of Git <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Editor Preference**: 67% of the firm uses Emacs, which is less common than editors like VS Code <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Ambitious Goals**: The team aims to apply [[large_language_models_in_ai_agents | large language models]] to various parts of the development flow, such as resolving merge conflicts, building feature descriptions, or identifying code reviewers <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. They want seamless integration across systems <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Approach to Large Language Models in Developer Tools

Jane Street's approach to [[building_and_scaling_large_language_models | large language models]] in developer tools involves:

1.  Building custom models <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
2.  Developing editor integrations <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
3.  Creating capabilities to evaluate and optimize model performance <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Training Custom Models

Training models is expensive and time-consuming <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>. The motivation to train custom models came partly from reading Meta's "Code Compose" paper, which detailed fine-tuning a model for Hack, a language similar to OCaml in its primary use by one company <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. (Interestingly, Hack is implemented in OCaml <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.)

Initially, the team naively believed they could fine-tune an off-the-shelf model by showing it their code <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. However, achieving good results requires the model to see examples in the specific "shape" of the questions one wants to ask <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

The specific goal for their custom model was to generate diffs given a prompt <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This means a user in an editor could describe a desired change, and the model would suggest a potentially multi-file diff (e.g., modifying test, `.ml`, and `.mli` files) <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. The diffs needed to apply cleanly and have a high likelihood of type-checking <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. They targeted diffs up to 100 lines <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

#### Data Collection

To train for this task, they needed data in the "context-prompt-diff" format <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

*   **Features (Pull Requests)**: Initially considered, but feature descriptions differ from how users would prompt in an editor, and features are often too large (500-1000 lines) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Commits**: Also considered, but Jane Street uses commits as checkpoints, so they lack descriptions and are not isolated changes <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Workspace Snapshotting**: The chosen approach involves taking snapshots of developer workstations every 20 seconds throughout the workday <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This also captures the build status (error or green) <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
    *   **Identifying Isolated Changes**: Patterns like "green to red to green" build statuses often indicate an isolated change where a developer broke the build and then fixed it <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
    *   **Generating Descriptions**: The build error at the "red" state is captured and paired with the diff from "red to green" as training data <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. A [[large_language_models_in_ai_agents | large language model]] is then used to write a detailed description of the change, which is filtered down to a human-like length <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

#### Reinforcement Learning

After supervised training, [[reinforcement_learning_in_large_language_models | reinforcement learning]] (RL) is used to align the model's output with human notions of "good code" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. "Good code" is defined as:

*   Code that parses <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   Code that type-checks (especially in statically typed OCaml) <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   Code that compiles and passes tests <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

To facilitate RL, they built the **Code Evaluation Service (CES)**, which acts like a fast build service <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. CES pre-warms a build, and then workers continuously take diffs from the model, apply them, and report whether the build status turns red or green <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This continuous feedback over months helps align the model to write compiling and passing code <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This same setup is also used for evaluating model performance <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

An example of training going "off the rails" involved a code review model that, after months of training, responded with "I'll do it tomorrow," as it was trained on human examples <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Meaningful evaluations are crucial to prevent such issues <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

### Editor Integrations: The AI Development Environment (AID)

The ultimate test for models is human usability <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. When building editor integrations, three goals were paramount:

1.  **Single Implementation**: Avoid writing the same context-building and prompting strategies three times for different editors (Neovim, VS Code, Emacs) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
2.  **Flexibility**: Maintain the ability to swap models or prompting strategies (e.g., from an off-the-shelf model to a fine-tuned one) <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Metrics Collection**: Gather real-world data on latency and diff application success rates from developers' editors <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

The solution was the **AI Development Environment (AID)** service <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>. AID handles prompt and context construction, and integrates with build status, abstracting these complexities from the editors <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. Thin layers are built on top of AID for each individual editor <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

*   **Sidecar Architecture**: AID runs as a sidecar application on the developer's machine <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. This allows changes to AID to be deployed and restarted on all machines without requiring users to restart their editors <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   **Editor Examples**:
    *   **VS Code**: AID integrates into the VS Code sidebar, providing a visual interface for asking questions and receiving multifile diffs <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
    *   **Emacs**: For Emacs users, who prefer text buffers, the AID experience is built into a Markdown buffer. Users can move around, ask questions, and use keybinds to append content <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
*   **Benefits of AID Architecture**:
    *   **Pluggability**: Allows swapping in new models, changing context building, and adding support for new editors or [[domain_specific_language_models_in_finance | domain-specific tools]] without rewriting editor integrations <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
    *   **A/B Testing**: Enables A/B testing of different approaches by sending portions of the company to different models and comparing acceptance rates <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.
    *   **Adaptability**: AID is an investment that pays off over time, as changes in [[large_language_models_in_ai_agents | large language models]] can be implemented in one place and deployed everywhere <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

## Broader Applications

The team is actively pursuing other [[experiments_with_large_language_models_and_ai_assisted_work | AI-assisted work]] initiatives, including:

*   New ways to apply Retrieval Augmented Generation (RAG) within editors <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.
*   Applying similar approaches to large-scale multi-agent workflows <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.
*   Increasing work with reasoning models <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

The consistent approach across these initiatives is to maintain pluggability, build a strong foundation, and enable other parts of the company to add their [[domain_specific_language_models_in_finance | domain-specific tooling]] <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.