---
title: Custom Model Building and Code Evaluation for AI Systems
videoId: 0ML7ZLMdcl4
---

From: [[aidotengineer]] <br/> 

John Kzi leads the AI Assistant team at Jane Street, a group focused on maximizing the value Jane Street derives from large language models (LLMs) <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Kzi's background is in Dev tools, having previously worked at GitHub <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. LLMs offer a unique opportunity due to their open-ended nature, allowing for the creation of almost anything imaginable <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The pace of creativity in employing LLMs is currently outpacing the progress of the models themselves <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Unique Challenges at Jane Street

Adopting off-the-shelf tooling for LLMs is challenging at Jane Street due to several internal choices <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>:

*   **OCaml as a Development Platform**: Jane Street primarily uses OCaml, a functional, powerful, but obscure language <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>. OCaml's common applications include theorem proving, formal verification, and writing programming languages <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Jane Street uses OCaml for nearly everything, including web applications (via `JS of OCaml` transpiler to JavaScript), Vim plugins (via `VAML` to Vimscript), and FPGA code (via `Hard Caml` instead of Verilog) <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>.
*   **LLM Proficiency in OCaml**: Existing LLMs are not proficient in OCaml, largely because the amount of OCaml code within Jane Street might exceed the total combined amount of OCaml code available globally for training <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Custom Internal Tooling**: The use of OCaml necessitated building internal tools, including custom build systems, a distributed build environment, and a code review system called Iron <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Monorepo and Mercurial**: All software is developed on a large monorepo application, which is stored in Mercurial instead of Git <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Editor Preference**: 67% of the firm uses Emacs, rather than more common editors like VS Code <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Ambitious LLM Application**: Jane Street aims to apply LLMs to various parts of their development flow, such as resolving merge conflicts, building feature descriptions, or identifying reviewers, without being limited by system boundaries <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Approach to LLMs

Jane Street's approach to LLMs, especially for developer tools, involves:

*   **Custom Models**: [[Building custom evaluations for better AI performance | Building custom models]] and methods for their construction <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.
*   **Editor Integrations**: Integrating LLMs into developer editors like VS Code, Emacs, and Neovim <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Model [[Testing and evaluation of AI models | Evaluation]]**: Developing capabilities to [[Improving AI evaluation methods | evaluate models]] and optimize their performance <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Custom Model Building

Training custom LLM models is an expensive and time-consuming endeavor with many potential pitfalls <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Inspiration and Initial Naivety

The team was inspired by Meta's CodeCompose project, which fine-tuned a model for Hack, a language similar to OCaml in its primary use by one company <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a> (Hack is incidentally implemented in OCaml) <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Initially, Jane Street naively believed they could simply fine-tune an off-the-shelf model with their code to make it understand their libraries and idioms <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

### Defining the Goal

It became clear that good outcomes require the model to see many examples in the specific shape of the questions it will be asked <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. Their primary goal was to enable the model to **generate diffs given a prompt** <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. This meant a user in an editor could describe a desired change, and the model would suggest a multi-file diff that:
*   Applies cleanly <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   Has a high likelihood of type-checking <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   Is around 100 lines, considered an ideal range for LLMs <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

The required training data shape for this task is **context, prompt, diff** <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.

### Data Collection Strategies

*   **Features (Pull Requests)**: Initially considered, but feature descriptions differ significantly from in-editor prompts (e.g., "fix that error") <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. Also, features are often very large (500-1000 lines), requiring automated ways to break them into smaller components <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Commits**: Smaller than features, but at Jane Street, commits are used as checkpoints rather than isolated, described changes <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. They also lack descriptions and are not isolated changes <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.
*   **Workspace Snapshotting (Successful Approach)**: This method involves taking snapshots of developer workstations every 20 seconds, along with their build status <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
    *   **Identifying Changes**: Patterns like "green to red to green" often indicate an isolated change where a developer broke and then fixed the build <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
    *   **Capturing Data**: By capturing the build error at the "red" state and the diff from "red" to "green", this data can be used to train the model to recover from mistakes <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
    *   **Generating Descriptions**: A large language model is used to write detailed descriptions of changes, which are then filtered down to approximate what a human would write <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Reinforcement Learning

After supervised training with collected data, reinforcement learning (RL) is crucial for aligning the model's output with human expectations of "good code" <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

*   **Defining "Good Code"**:
    *   Code that parses <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
    *   Code that type-checks (especially critical for OCaml as a statically typed language) <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
    *   Code that compiles and passes tests <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

*   **Code Evaluation Service (CES)**: To facilitate RL, Jane Street built CES, a service similar to a build service but optimized for speed <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
    *   **Process**: CES pre-warms a build to a "green" state at a specific revision <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. Workers then continuously take diffs from the model, apply them, determine if the build status turns red or green, and report success or error back <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
    *   **Outcome**: Over months of use, CES helped align the model to write code that compiles and passes tests <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

## [[Testing and evaluation of AI models | Evaluation]]

The same setup used for reinforcement learning can be leveraged for model [[Best practices for AI evaluation | evaluation]] <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. By holding out some RL data, one can [[Evaluation and feedback in AI systems | evaluate the model's ability]] to write working code <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

> [!NOTE] Importance of Meaningful [[Building custom evaluations for better AI performance | Evaluations]]
> Training can lead to catastrophic, yet sometimes humorous, results. For example, a code review model trained on human examples once responded with "I'll do it tomorrow" when given code to review <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. Meaningful [[Best practices for AI evaluation | evaluations]] are crucial to prevent models from going "off the rails" and wasting time and resources <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a>.

## Editor Integrations: AI Development Environment (Aid)

The ultimate test for models is their utility for human developers <a class="yt-timestamp" data-t="00:12:33">[00:12:33]</a>. Jane Street developed editor integrations to expose these models to their developers.

### Design Principles

When building these integrations, three key ideas were prioritized:

1.  **Code Reusability**: Avoid writing the same context building and prompting strategies three times for their supported editors (Neovim, VS Code, Emacs) <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.
2.  **Flexibility**: Maintain the ability to easily swap out models or prompting strategies, anticipating the eventual use of fine-tuned models <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Metrics Collection**: Collect real-world metrics like latency and diff application success rates to gauge the meaningfulness of the generated diffs <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>.

### Architecture: Aid as a Sidecar

The chosen architecture for the AI Development Environment (Aid) service places Aid as a sidecar application on the developer's machine <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>.

*   **Functionality**: Aid handles interactions with LLMs, constructs prompts, manages context, and monitors build status <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
*   **Editor Layers**: Thin layers are built on top of Aid for each individual editor <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   **Benefits**: This sidecar approach means changes to Aid do not require individual editor updates; Aid can be restarted on developer machines for immediate updates <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

### User Experience

*   **VS Code**: Aid integrates into the VS Code sidebar, similar to Copilot, allowing users to request and receive multi-file diffs through a visual interface <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   **Emacs**: For Emacs users, who prefer text buffers, the Aid experience is built into a Markdown buffer. Users can navigate, ask questions, and use keybinds to append content <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

### Aid's Flexibility and Value

Aid's architecture enables significant flexibility:
*   **Pluggable Components**: New models, context-building strategies, and even support for new editors can be plugged in <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>.
*   **Domain-Specific Tools**: Different areas of the company can supply custom tools, which become available across all supported editors without individual integrations <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.
*   **A/B Testing**: Aid allows A/B testing of different approaches, such as directing half the company to one model and the other half to another to compare acceptance rates <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.

Aid is a long-term investment, ensuring that any changes in LLMs can be managed in one central place downstream of the editors, making updates available everywhere efficiently <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

## Future Endeavors

The team is actively pursuing other areas, including:
*   Applying RAG (Retrieval-Augmented Generation) within editors <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.
*   Similar approaches to large-scale multi-agent workflows <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
*   Working more with reasoning models <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

Across all these efforts, the core principles remain: pluggability, building a strong foundation, and enabling other parts of the company to add domain-specific tooling <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.