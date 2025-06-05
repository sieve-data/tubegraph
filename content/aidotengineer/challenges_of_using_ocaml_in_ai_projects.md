---
title: Challenges of using OCaml in AI projects
videoId: 0ML7ZLMdcl4
---

From: [[aidotengineer]] <br/> 

Working with OCaml in AI projects, particularly with large language models (LLMs), presents unique [[challenges_in_ai_development | challenges in AI development]] and [[challenges_in_building_ai_applications | challenges in building AI applications]] due to the language's obscure nature and the specific development environment at Jane Street <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. John Kzi from Jane Street's AI Assistant team highlights several key difficulties <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

## OCaml as a Development Platform
OCaml is described as a functional, powerful, but incredibly obscure language, primarily built in France <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. Its most common applications include theorem proving, formal verification, and writing programming languages <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. At Jane Street, OCaml is used for nearly everything <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>:
*   Web applications are written in OCaml and transpiled to JavaScript using `JS of OCaml` <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   Vim plugins are written in OCaml using `vaml` <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   FPGA code is written in OCaml using `Hardcaml` instead of Verilog <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

This pervasive use of OCaml creates significant [[challenges_in_ai_development | challenges]] for adopting off-the-shelf AI tooling <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>.

## Primary Reasons for OCaml-Related AI Challenges
According to John Kzi, the difficulties stem from a few core issues <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>:

### Model Limitations with OCaml
*   **Data Scarcity**: LLMs are generally not very good at OCaml <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This is not the fault of AI labs but a byproduct of the limited amount of OCaml data available for training <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. The amount of OCaml code within Jane Street likely exceeds the total combined amount existing outside its walls <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Jane Street's Unique Development Environment
The internal development choices at Jane Street, influenced by OCaml, further complicate AI integration <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>:
*   **Custom Tooling**: The company has built its own build systems, distributed build environment, and a code review system called Iron <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Monorepo and Version Control**: All software is developed on a giant monorepo application, stored in Mercurial instead of Git <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>.
*   **Editor Usage**: A significant portion (67%) of the firm uses Emacs, which differs from more common editors like VS Code <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### Ambitious Integration Goals
Jane Street aims to apply LLMs to various parts of their development flow, such as resolving merge conflicts, building feature descriptions, or identifying code reviewers <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This requires deep integration without being hampered by system boundaries <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

## [[challenges_in_ai_development | Challenges in AI Development]] and Training Custom Models
Training custom models for OCaml is expensive, time-consuming, and prone to errors <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. Initial attempts to replicate Meta's Code Compose project, which fine-tuned a model for Hack (a language similar to OCaml in its primary use at one company), proved difficult <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

### Data Collection and Shaping
*   **Need for Specific Training Data**: Fine-tuning a model for OCaml requires models to see many examples in the shape of the desired question <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>. The goal was to generate multi-file diffs (e.g., test, `.ml`, `.mli` files) given a natural language prompt, ensuring they apply cleanly and type-check <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Inadequacy of Existing Data**:
    *   **Features/Pull Requests**: While containing human descriptions and code diffs, feature descriptions differ significantly from short, in-editor prompts ("fix that error") <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>. They are also often too large (500-1000 lines), requiring automated ways to break them into smaller components <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    *   **Commits**: Commits at Jane Street are primarily used as checkpoints without descriptions and are not isolated changes <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Workspace Snapshotting**: The solution for data collection involves snapshotting developer workstations (e.g., every 20 seconds) along with build statuses <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. A "green to red to green" pattern often indicates an isolated change, and capturing the build error at the "red" state with the "red to green" diff provides valuable training data for recovery from mistakes <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. LLMs are used to generate detailed descriptions from these diffs, which are then filtered down to human-like prompt length <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Reinforcement Learning and Evaluation
*   **Defining "Good Code"**: For OCaml, "good code" means it parses correctly <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>, type-checks (due to static typing) <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>, compiles, and passes tests <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   **Code Evaluation Service (CES)**: To align the model with human-defined good code, a Code Evaluation Service (CES) was built <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. CES is a fast build service that pre-warms builds, applies diffs from the model, and reports whether the build status turns red or green <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. This iterative process helps the model write code that compiles and passes tests <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>. This same setup is also used for evaluating model performance <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.
*   **Ensuring Meaningful Evaluations**: Training can lead to "catastrophic but hilarious results" if evaluations are not meaningful <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. An example given was a code review model that, after months of training, responded with "I'll do it tomorrow," as it was trained on human examples including such phrases <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. This highlights the importance of robust evaluation to prevent wasted time and money <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>.

## [[technical_challenges_in_ai_agent_development | Technical Challenges in AI Agent Development]]: Editor Integrations
Exposing these OCaml-aware models to developers requires robust editor integrations. Key considerations for building these integrations included <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>:
1.  **Code Reusability**: Avoiding rewriting context and prompting strategies for each of the three supported editors: Neovim, VS Code, and Emacs <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.
2.  **Flexibility**: The ability to swap models or prompting strategies easily, anticipating the need for fine-tuned models <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
3.  **Metrics Collection**: Gathering real-world data on latency and diff application success to ensure the diffs are meaningful to users <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

### AI Development Environment (AID) Architecture
To address these [[challenges_in_ai_agent_development | challenges in AI agent development]], Jane Street developed AID (AI Development Environment), which acts as a sidecar application on developers' machines <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>:
*   AID handles prompt and context construction, and build status integration <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>.
*   Thin layers are written on top of AID for each editor <a class="yt-timestamp" data-t="00:13:49">[00:13:49]</a>.
*   This architecture allows changes to AID without requiring editor restarts, ensuring all developers get the most recent copy <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>.
*   Examples include a visual sidebar integration in VS Code and a markdown buffer integration in Emacs for diff requests <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

AID's pluggable architecture allows for swapping in new models, changing context building, adding support for new editors, and integrating domain-specific tools <a class="yt-timestamp" data-t="00:14:58">[00:14:58]</a>. It also facilitates A/B testing different approaches to determine which yields higher acceptance rates <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. This investment pays off over time, adapting to frequent changes in LLMs from a single point <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

## Conclusion
The [[challenges_in_creating_effective_ai_agents | challenges in creating effective AI agents]] and tools for OCaml at Jane Street stem from the language's obscurity and the company's highly customized development environment. By building custom models, advanced data collection techniques, and flexible evaluation and integration services like AID, Jane Street addresses these unique hurdles, laying a strong foundation for continued AI development in OCaml <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>.