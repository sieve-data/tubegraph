---
title: Custom model training and reinforcement learning
videoId: 0ML7ZLMdcl4
---

From: [[aidotengineer]] <br/> 

Jane Street, a global quantitative trading firm, faces unique challenges in adopting off-the-shelf [[large_language_models_and_selfimprovement | large language models]] (LLMs) due to its specialized technology stack. To maximize the value derived from LLMs, the firm has invested in custom model training and sophisticated reinforcement learning strategies <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Challenges with Off-the-Shelf AI Models

Jane Street's primary development platform is OCaml, an obscure functional language <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. OCaml's common applications include theorem proving, formal verification, and writing programming languages <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Jane Street uses OCaml for nearly everything, even transpiling it to JavaScript for web applications (using `JS of OCaml`), Vim script for plugins (using `VAML`), and for FPGA code (using `Hardcaml`) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.

This unique environment presents several difficulties for integrating generic [[ai_models_and_training_methods | AI models and training methods]]:
*   **Limited OCaml Data:** [[AI models and training methods | Models]] are not proficient in OCaml, largely because the amount of OCaml code within Jane Street likely exceeds the total combined amount of OCaml code available globally for [[ai_model_training_and_inference | model training]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Custom Internal Systems:** Jane Street has built its own development tools, including custom build systems, a distributed build environment, and an internal code review system called "Iron" <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. They use a giant monorepo stored in Mercurial (not Git), and 67% of the firm uses Emacs as their primary editor <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Desire for Deep Integration:** Jane Street aims to apply LLMs to various development flows, such as resolving merge conflicts, generating feature descriptions, or identifying code reviewers, without being limited by system boundaries <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. This requires significant [[customization_and_scalability_in_ai_models | customization and scalability in AI models]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Jane Street's Approach to Custom Model Training

Despite the expense and complexity, Jane Street decided to train custom models <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. This decision was influenced by a Meta paper on "Code Compose," which detailed successful [[finetuning_ai_models_for_specific_use_cases | finetuning for a language (Hack)]] primarily used at one company, similar to OCaml's status <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.

The initial naive assumption that simply showing a model a bunch of internal code would yield a capable model proved incorrect <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>. Success requires providing the model with examples structured in the "shape" of the questions one intends to ask <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

### Defining the Goal: Generating Diffs

Jane Street's primary goal for their custom model was to generate code diffs based on a user's prompt within an editor <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. These diffs needed to:
*   Potentially span multiple files (e.g., test, `.ml`, and `.mli` files) <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   Apply cleanly <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
*   Have a high likelihood of type-checking after application <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   Target a range of up to 100 lines as an ideal scope for LLM capabilities <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

### Data Collection: Workspace Snapshotting

To achieve this, training data was required in a "context, prompt, diff" format <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Standard internal "features" (similar to pull requests) and commits were deemed unsuitable due to their large size, detailed descriptions (unlike in-editor prompts), or lack of descriptions <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.

The solution implemented was **workspace snapshotting**:
*   Snapshots of developer workstations are taken frequently (e.g., every 20 seconds) <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   Simultaneously, snapshots of the build status (error or green) are recorded <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   Patterns like "green to red to green" build status transitions often indicate an isolated change where a developer fixed an error <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   The build error at the "red" state and the diff from "red" to "green" are captured and used as training data, allowing the model to learn how to recover from mistakes <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Prompt Generation:** LLMs are used to generate detailed descriptions of the changes, which are then filtered down to emulate typical human-written prompts for the training data <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Reinforcement Learning

After supervised training, reinforcement learning (RL) is crucial for aligning the model's output with human judgments of "good code" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

**Definition of "Good Code" for RL:**
*   **Parses Correctly:** Code must successfully pass through the OCaml parser <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Type-Checks:** In a statically typed language like OCaml, good code must type-check when applied to a base revision <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Compiles and Passes Tests:** The gold standard is code that compiles and passes all associated tests <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

**Code Evaluation Service (CES):**
Jane Street built the Code Evaluation Service (CES) to facilitate this RL phase <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>. CES is a build service designed for speed:
*   It pre-warms a build at a specific, green revision <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   Workers continuously receive diffs from the model, apply them, and determine if the build status turns red or remains green <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   This feedback loop, utilized over months, continuously improves the model's ability to generate code that compiles and passes tests <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

### Evaluation

The same setup used for reinforcement learning can be used for model evaluation <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. By holding out some RL data, Jane Street can assess a model's performance by providing it a problem, letting it write code, and then verifying if the generated code works <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

Meaningful evaluations are crucial to prevent models from producing "catastrophic but hilarious" results, such as a code review model suggesting "I'll do it tomorrow" because it was trained on human examples <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>.

## Editor Integrations: The AI Development Environment (Aid)

To expose these custom models to developers, Jane Street built editor integrations with three main goals:
1.  **Avoid Redundancy:** Write context and prompting strategies once, rather than separately for Neovim, VS Code, and Emacs <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
2.  **Maintain Flexibility:** Easily swap out different models or prompting strategies as needed, anticipating future [[future_directions_in_ai_model_training_and_scaling | finetuned models]] <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Collect Metrics:** Gather real-world data on latency and diff application success rates from within the developer's editor <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

The chosen architecture is the **AI Development Environment (Aid)** service, which runs as a sidecar application on the developer's machine <a class="yt-timestamp" data-t="00:13:32">[00:13:32]</a>. Aid handles prompt construction, context building, and build status checks <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. Thin layers are then built on top of Aid for each specific editor <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>. This allows changes to Aid to be instantly deployed by restarting the service, without requiring developers to restart their editors <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.

Aid's pluggable architecture supports:
*   Swapping in new models <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   Modifying context building <a class="yt-timestamp" data-t="00:15:05">[00:15:05]</a>.
*   Adding support for new editors <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.
*   Integrating domain-specific tools from different company areas, making them available across all editors without individual integrations <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

Aid also enables A/B testing different approaches, such as directing different segments of the company to distinct models to compare acceptance rates <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. This provides a robust foundation for [[strategies_for_adapting_ai_models_and_prompts | adapting AI models and prompts]] as the field evolves <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>.