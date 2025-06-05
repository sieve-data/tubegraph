---
title: Adaptation of OCaml in Developer Tools and Challenges
videoId: 0ML7ZLMdcl4
---

From: [[aidotengineer]] <br/> 

John Kzi, from the AI Assistant team at Jane Street, focuses on maximizing the value Jane Street derives from [[coding_large_language_models_and_Rust | large language models]] (LLMs) <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Kzi's background is entirely in Dev tools, including time at GitHub <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. LLMs offer a significant opportunity due to their open-ended nature, allowing the creation of almost anything imaginable, with human creativity being the primary limiter to their employment <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

However, Jane Street has made specific choices that complicate the adoption of off-the-shelf tooling <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## OCaml as a Core Development Platform

The main reason for these difficulties is Jane Street's extensive use of OCaml as its primary development platform <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### What is OCaml?
OCaml is described as a functional and powerful language, but also "incredibly obscure" <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Developed in France, its most common applications include theorem proving, formal verification, and writing programming languages <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.

### OCaml's Pervasive Use at Jane Street
At Jane Street, OCaml is used for nearly everything <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>:
*   **Web Applications:** Instead of JavaScript, they write OCaml and use `JS of OCaml`, which is an OCaml bytecode to JavaScript transpiler <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Vim Plugins:** While Vim plugins typically require Vim script, Jane Street uses `Vaml`, an OCaml to Vim script transpiler <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **FPGA Code:** Even for FPGA code, developers write in `Hardcaml`, an OCaml library, rather than Verilog <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

## [[challenges_and_considerations_in_tool_creation_and_execution | Challenges with LLM Tooling and OCaml]]

Several factors make off-the-shelf LLM tools poorly suited for OCaml at Jane Street <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>:

1.  **LLM Proficiency in OCaml:** Models are "just not very good at OCaml" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This is due to the limited training data available for OCaml globally, with the internal OCaml codebase at Jane Street potentially exceeding the total combined amount of OCaml code outside their walls <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
2.  **Self-Imposed Complexity:** Jane Street's unique development environment further complicates matters <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>:
    *   **Custom Build Systems:** They built their own <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   **Distributed Build Environment:** They built their own <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
    *   **Code Review System:** An internal system called "Iron" <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   **Monorepo:** Software is developed on a giant monorepo application <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   **Version Control:** The monorepo is stored in Mercurial, not Git <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
    *   **Editor Preference:** 67% of the firm uses Emacs, with VS Code also used but less popular <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
3.  **Desire for Broad LLM Application:** Jane Street aims to apply LLMs to various parts of their development flow, such as resolving merge conflicts, building feature descriptions, or identifying reviewers <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. This requires integration across different systems, without being hampered by boundaries <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Jane Street's Approach to LLM Development for OCaml

Jane Street's strategy involves custom models and a tailored evaluation process.

### Custom Model Development
Inspired by Meta's CodeCompose project, which fine-tuned a model for Hack (a language similar to OCaml in its niche, primarily company-specific use) <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>, Jane Street sought to replicate these results for OCaml <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. The initial naive assumption was that showing an off-the-shelf model their code would result in a model that understood their libraries and idioms <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

However, obtaining good outcomes requires the model to see many examples in the shape of the desired question <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

#### Goal: Generate Diffs
The primary goal was to enable users in an editor to describe a desired change and have the model suggest a potentially multifile diff <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. These diffs needed to apply cleanly and have a good likelihood of type-checking, targeting up to 100 lines as an ideal range <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

#### Training Data Collection
Training data needs to be in the "context, prompt, diff" shape <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   **Challenges with existing data:**
    *   **Features (Pull Requests):** While they have descriptions and diffs, their descriptions differ significantly from what a user would type in an editor (e.g., "fix that error") <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. They are also often very large (500-1000 lines), requiring automated parsing into smaller components <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    *   **Commits:** Used as checkpoints, commits lack descriptions and are not isolated changes <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Workspace Snapshotting:** The solution was to take snapshots of developer workstations every 20 seconds throughout the workday, including build status <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
    *   **Pattern Recognition:** A "green to red to green" build status often indicates an isolated change where a developer broke and then fixed the build <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
    *   **Training Data Extraction:** By capturing the build error at the "red" state and the diff from "red to green," this data can be used to train the model to recover from mistakes <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
    *   **Description Generation:** A separate LLM is used to generate detailed descriptions of changes, which are then filtered down to match the conciseness of human prompts <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

#### Reinforcement Learning (RL)
RL aligns the model's output with what humans consider "good code" <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
*   **Definition of "Good Code" for OCaml:**
    *   **Parses:** Must successfully pass through the OCaml parser <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
    *   **Type Checks:** For statically typed OCaml, the code must pass the type checker when applied to a base revision <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
    *   **Compiles and Passes Tests:** The gold standard is code that compiles and passes tests <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **Code Evaluation Service (CES):** This service is central to the RL phase <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
    *   **Functionality:** Similar to a build service, it pre-warms a build at a specific revision <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.
    *   **Workers:** Workers continuously take diffs from the model, apply them, determine if the build status turns red or green, and report the success or error back <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
    *   **Outcome:** Over months of use, this service helps align the model to write code that compiles and passes tests <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Evaluation:** The same setup used for RL can be used for evaluation by holding out some RL data <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
    *   **Importance of Meaningful Evaluation:** A notable anecdote highlights this: A code review model, trained on human examples, once responded to a review with "I'll do it tomorrow," because humans often use such phrases <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>. Meaningful evaluations are crucial to prevent models from going "off the rails" and wasting time/money <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

## Editor Integrations: The AI Development Environment (AiDE)

The ultimate test for models is whether they work for humans <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. Jane Street built editor integrations to expose these models to developers.

### Design Principles
When building these integrations, three ideas were paramount <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>:
1.  **Avoid Redundancy:** Support for three editors (Neovim, VS Code, Emacs) meant avoiding writing context-building and prompting strategies three times <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
2.  **Maintain Flexibility:** The ability to swap models or prompting strategies was essential, especially as they anticipated moving from general LLMs to fine-tuned models <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Collect Metrics:** Crucial metrics for developers include latency and whether generated diffs actually apply <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

### AiDE Architecture
The chosen architecture for the AI Development Environment (AiDE) is simplified as follows <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>:
*   LLMs are on one side.
*   AiDE handles prompt construction, context building, and build status integration <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>.
*   Thin layers are written on top of AiDE for each individual editor <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.

#### Benefits of AiDE as a Sidecar Application
AiDE runs as a sidecar application on the developer's machine <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>. This means changes to AiDE do not require individual editor updates or restarts; restarting the AiDE service updates everyone <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

#### Editor Examples
*   **VS Code:** AiDE works within the VS Code sidebar, offering a visual interface for multifile diffs <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Emacs:** For Emacs developers who prefer text buffers, the AiDE experience is built into a Markdown buffer, allowing users to move around, ask questions, and apply changes via key binds <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

### Flexibility and A/B Testing
AiDE's pluggable architecture allows for <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>:
*   Swapping in new models <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   Changing context building strategies <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   Adding support for new editors (currently underway) <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   Integrating [[open_sourcing_and_applications_in_realworld_tasks | domain-specific tools]] from different company areas, which then become available across all editors without individual integrations <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.

AiDE also facilitates A/B testing, allowing Jane Street to send different segments of the company to different models and compare acceptance rates <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. This investment pays off as any change in LLMs can be managed in one place and deployed everywhere <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

The team is also exploring new ways to apply RAG (Retrieval Augmented Generation) within editors, large-scale multi-agent workflows, and reasoning models <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The core approach remains the same: keep things pluggable, build a strong foundation, and enable the rest of the company to add [[developing_and_using_software_automation_tools | domain-specific tooling]] <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.