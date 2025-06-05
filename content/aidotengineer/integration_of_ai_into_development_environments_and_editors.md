---
title: Integration of AI into Development Environments and Editors
videoId: 0ML7ZLMdcl4
---

From: [[aidotengineer]] <br/> 

Jane Street's AI Assistant team focuses on maximizing the value derived from large language models (LLMs) within the company <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. John Kzi, who has a background in Dev Tools, notes the "amazing opportunity" LLMs present due to their open-ended nature, allowing the creation of "anything that we can imagine" <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The rapid progress of models is only outpaced by the creativity in employing them <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Unique Development Environment Challenges

Adopting off-the-shelf AI tooling at Jane Street is challenging due to several unique internal choices <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>:

*   **OCaml as a Primary Language** <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>: OCaml is a powerful functional language, but it's obscure <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Its common applications are in theorem proving, formal verification, and writing programming languages <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Jane Street uses OCaml for "everything," including:
    *   Web applications (using `JS of OCaml` to transpile to JavaScript) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
    *   Vim plugins (using `Vaml` to transpile to Vim script) <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
    *   FPGA code (using `HardCaml` instead of Verilog) <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Lack of OCaml Training Data for LLMs** <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>: LLMs are not proficient in OCaml, largely because the amount of OCaml code within Jane Street likely exceeds the total combined amount available in the public domain for training <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Custom Internal Infrastructure** <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>:
    *   They built their own build systems and distributed build environment <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   An internal code review system called "Iron" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
    *   A single, giant monorepo stored in Mercurial instead of Git <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   67% of the firm uses Emacs, though VS Code is also used <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Ambitious AI Integration Goals** <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>: Jane Street wants to apply LLMs to various parts of their [[impact_of_ai_on_development_workflow | development workflow]], such as resolving merge conflicts, building feature descriptions, or identifying code reviewers <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. They seek seamless [[integration_of_ai_agents_into_existing_infrastructure | integration of AI agents into existing infrastructure]] without system boundaries <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## Approach to LLMs in Developer Tools

Jane Street's strategy for [[integrating_ai_into_natural_workflows | integrating AI into natural workflows]] in developer tools involves:

1.  **Building Custom Models** <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
2.  **Editor Integrations** (VS Code, Emacs, Neovim) <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
3.  **Model Evaluation** <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.

### Custom Model Development

Initially, the team was "naive," thinking they could easily fine-tune an off-the-shelf model by showing it their code <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. They learned from Meta's CodeCompose project, which fine-tuned a model for Hack, a language similar to OCaml in its niche use within one company <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. (Interestingly, Hack is implemented in OCaml <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>).

The key insight was that good outcomes require the model to see examples in the shape of the desired question <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

#### Defining the Goal
The primary goal was to generate diffs given a prompt <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. Users should be able to describe a desired change in their editor, and the model would suggest a multi-file diff (e.g., test file, `.ml`, `.mli` header file) <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. These diffs needed to apply cleanly and have a high likelihood of type-checking, ideally within a 100-line range <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

#### Data Collection
The process required collecting "context, prompt, diff" triplets as training data <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>:

*   **Challenges with existing data sources:**
    *   **Features (Pull Requests)**: While containing human descriptions and diffs, their descriptions are too verbose for in-editor prompts, and the diffs are often too large (500-1000 lines) <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
    *   **Commits**: At Jane Street, commits are used as checkpoints, not isolated changes, and lack descriptions <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.
*   **Solution: Workspace Snapshotting** <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>:
    *   Snapshots of developer workstations are taken frequently (e.g., every 20 seconds), along with the build status <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   "Green to Red to Green" build status patterns indicate isolated changes where a developer broke and then fixed the build <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
    *   The build error at the "Red" state and the diff from "Red" to "Green" are captured as training data for the model to recover from mistakes <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Generating Descriptions**: An LLM is used to write detailed descriptions of changes, which are then filtered down to approximate what a human would write in a short prompt <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

#### Reinforcement Learning (RL)
RL is crucial for aligning the model with what humans consider "good code" <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
Good code is defined as <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>:
*   Parsable <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   Type-checked (for statically typed OCaml) <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
*   Compilable and passes tests <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.

*   **Code Evaluation Service (CES)** <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>:
    *   Acts like a fast build service.
    *   A build is pre-warmed at a specific revision (green status) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
    *   Workers continuously take diffs from the model, apply them, and determine if the build turns red or green <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
    *   This feedback helps align the model over months to write code that compiles and passes tests <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

#### Evaluation
The same CES setup can be used for evaluation by holding out some RL data <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>. This allows them to assess whether the code generated by the model actually works <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. Meaningful evaluations are critical to prevent models from "going off the rails" and wasting resources <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a> (e.g., a code review model suggesting "I'll do it tomorrow" based on human examples <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>).

### Editor Integrations

The ultimate test for models is whether they work for humans <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>. The team built editor integrations with three main goals:

1.  **Avoid Redundancy**: Support Neovim, VS Code, and Emacs without writing context-building and prompting strategies three times <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
2.  **Maintain Flexibility**: Easily swap out models or prompting strategies <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Collect Metrics**: Gather real-world data on latency and diff application success rates <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

#### AI Development Environment (AID) Architecture
The chosen architecture involves an "AI Development Environment" (AID) service <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>:
*   LLMs are on one side, and AID handles prompt construction, context building, and accessing build status <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
*   Thin layers are built on top of AID for each individual editor <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   AID runs as a sidecar application on the developer's machine <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. This means changes to AID don't require developers to restart their editors, as the AID service can be restarted remotely <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

#### Editor Examples:
*   **VS Code**: AID integrates into the sidebar, offering multi-file diff suggestions through a visual interface <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Emacs**: For Emacs users accustomed to text buffers, the AID experience is built into a Markdown buffer, allowing users to move around, ask questions, and append content using keybinds <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

#### Benefits of AID Architecture:
*   **Pluggability**: Allows swapping new models, changing context building, and adding support for new editors (currently being done) <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **[[integration_of_ai_coding_agents_with_thirdparty_tools | Integration of AI coding agents with third-party tools]]**: Different areas of the company can supply [[developing_custom_ai_tools_and_functions | domain-specific tools]] that become available in all editors without individual integrations <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **A/B Testing**: Enables A/B testing different approaches, like sending 50% of the company to one model and 50% to another, to determine which achieves a higher acceptance rate <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

The AID architecture is a long-term [[scaling_ai_models_and_their_impact_on_development_tools | investment that pays off over time]], as any change in large language models can be applied in one central place and instantly made available everywhere <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. This foundational approach supports further work, including applying RAG (Retrieval Augmented Generation), multi-agent workflows, and reasoning models, while maintaining pluggability and allowing other parts of the company to add domain-specific tooling <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.