---
title: Rust Coder project and AI integration
videoId: bbq0b_FpYEY
---

From: [[aidotengineer]] <br/> 

The [[rust_programming_language_for_ai_development | Rust programming language]] is positioned as "the language of AGI" (Artificial General Intelligence) due to its unique characteristics that make it highly suitable for AI coders and their human assistants <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The focus is on an "AI first, human second" approach, reflecting the evolving landscape of code generation <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Michael Yu, the speaker, is involved in this initiative and showcases the Rust Coder project <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Why Rust for AI?

[[challenges_and_benefits_of_using_rust | Rust]] has celebrated its 10-year anniversary and has consistently been the most beloved programming language in Stack Overflow's developer surveys <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. It is highly admired by developers, with an 82% admiration rate, significantly higher than other languages <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. However, its "desired" usage (how much people want to use it) is lower than Python, although surprisingly higher than Go <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

The main reason for this discrepancy is [[challenges_and_benefits_of_using_rust | Rust's steep learning curve for humans]] <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Its powerful compiler forces developers to write correct and optimized code from the outset, unlike languages like C++, Python, or JavaScript that are more forgiving of initial errors <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. While challenging initially, mastering Rust leads to writing more correct code more easily <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

### Rust's Suitability for AI
While humans prefer languages like Python for their ease of writing and quicker results, [[automation_and_rust_in_agi_development | Rust is better suited for machines]] <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. Brett Taylor, Chairman of OpenAI, noted Rust's efficiency and structural orientation, which benefits from strong compiler checking and a robust type system <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

A key advantage for AI is Rust's tight feedback loop provided by its compiler <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Many Rust developers experience [[testing_and_optimization_of_ai_coding_agents | little debugging once a project compiles]], indicating a high likelihood of correct execution <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This property allows the [[testing_and_optimization_of_ai_coding_agents | Rust compiler to provide a very good feedback loop for AI]], creating an effective "reward function" for reinforcement learning models, similar to AlphaGo <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

Therefore, [[automation_and_rust_in_agi_development | Rust is a perfect fit for AI code generators]] <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. In a future where [[automation_and_rust_in_agi_development | most code is written by AI]], generating human-incomprehensible Python or JavaScript may not be ideal. Instead, AI-generated Rust code, which is verifiable for correctness, becomes highly valuable <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.

## The Rust Coder Project

The Rust Coder project aims to [[automation_and_rust_in_agi_development | teach Rust to AI]] and enable AI to generate better Rust code <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. It is sponsored by two internship grants from the Linux Foundation and utilizes educational materials from the Rust Foundation <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

### Goals
*   **For humans**:
    *   Make learning Rust easier through AI assistants <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   Simplify writing code with Rust <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   Improve Rust's usability within IDEs <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   **For machines**:
    *   Enable the generation of Rust code on the fly <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
    *   Support the belief that [[automation_and_rust_in_agi_development | the path to AGI may come from code generators]] <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
    *   Facilitate machines generating correct Rust code by working with the compiler <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### Demos

#### Demo 1: Helping Humans Learn Rust
This demo illustrates how Rust Coder assists students in learning Rust by solving complex programming problems <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   **Process**: Rust educational materials are used to generate hundreds of common Rust developer tasks <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. These tasks are built into a knowledge base using embeddings in a vector database <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **Example**: A student needs to write a Rust program to convert numbers to different bases <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.
    *   Using Cursor's AI assistant panel, the student provides the question along with input/output examples and specifies Rust as the language <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.
    *   The CHV coder model, running on Gaia network, immediately generates the Rust code and an explanation of its structure and functions <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
    *   The generated code successfully compiles and runs, providing the correct result <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Impact**: This project is used by over a thousand developers in a university-based Rust camp <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. Rust Coder can solve and explain exam questions in one shot <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>.

#### Demo 2: Helping Humans Code Rust in the IDE
This demo focuses on the [[integration_of_ai_into_development_environments_and_editors | integration of AI into Development Environments and Editors]] to assist with Rust coding, particularly bug fixing <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
*   **MCP Server**: Rust Coder includes an MCP (Machine Code Protocol) server, allowing it to integrate with IDEs like Cursor <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. This server runs locally <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.
*   **Tools Provided**:
    *   `generate`: Takes a description and requirements to generate a complete Rust project. It uses a vector database of common algorithms and Rust use cases to find templates and modify them <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
    *   `compile and fix`: Takes Rust project files, compiles them using its own Rust compiler, and if errors are found, uses its [[coding_large_language_models_and_rust | coding large language model]] to identify and fix the source code <a class="yt-timestamp" data-t="00:13:26">[00:13:26]</a>. This process repeats until the code compiles correctly <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.
*   **Example**: Fixing a simple syntax error in a "hello world" Rust project <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>.
    *   The user requests the AI agent to compile and fix the Rust project <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.
    *   The Cursor IDE calls the `compile and fix` MCP tool <a class="yt-timestamp" data-t="00:15:09">[00:15:09]</a>.
    *   The tool identifies the missing parenthesis, suggests the fix, and the code becomes compilable <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
*   **Advantage**: Unlike generic [[application_of_open_ai_models_in_coding_with_agencies like copilot | coding large language models]] (like those in Cursor designed for Python/JavaScript), Rust Coder's MCP server is a fully integrated solution with its own knowledge base of Rust compiler error messages and how to fix them <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>. This knowledge base grows over time as it learns from user interactions and external contributions, allowing it to fix more complex issues <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

## How it Works: The Tech Stack

The Rust Coder project is built on an integrated stack of several open-source tools <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>:
*   **[[coding_large_language_models_and_rust | Coding Large Language Models]] (LLMs)**: Configurable to use either commercial or open-source models, such as the Chairman Coder model, optimized with prompts tailored to the specific model <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   **Self-Improving Knowledge Base**: A core part of the system is its knowledge base of Rust compiler error messages and their fixes <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. This database is designed to grow and become more intelligent over time through contributions <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   **Llama Edge Project**: This Linux Foundation project runs LLMs and other AI models (e.g., YOLO, Whisper, TTS, Stable Diffusion) across various GPUs and MPUs <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. It is much smaller than PyTorch, measured in tens of megabytes <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
*   **Integrated Knowledge Base**: Utilizes Vortex search with Elastic Search, TiDB, and Quadrant for vector search, along with various vector embedding models <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
*   **Gaia Network**: A product built on Llama Edge that packages these components <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
*   **Open MCP Proxy**: Used to turn the Gaia network into an MCP server, enabling tool calls for LLMs <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.

## Vision for the Future

The MCP (Machine Code Protocol) is primarily designed for machines, not just humans <a class="yt-timestamp" data-t="00:21:44">[00:21:44]</a>. In the progression of computer users from human-centric UIs (web, desktop, mobile) to API-first approaches for deterministic computer consumption, the era of "tools" for LLMs has emerged <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. These tools allow LLMs, which behave like humans but are fundamentally computers, to consume software services <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

Rust Coder provides services like Rust compiler service and LLM-based bug fixing as tools for other LLMs to use <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>. The long-term vision for Rust Coder is for [[automation_and_rust_in_agi_development | AI]] to generate and verify Rust code for complex autonomous tasks, such as directing a drone, entirely without human intervention but with guarantees of correctness <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. This aligns with the belief that [[automation_and_rust_in_agi_development | AI coders are the road to AGI]], and [[rust_programming_language_for_ai_development | Rust is the best language for them]] <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>.

## Getting Started and Contribution

The Rust Coder project is part of a larger initiative called "Local Rust," which aims to provide Rust tools for computers <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>. It offers both APIs (for workflow engines and deterministic software) and MCP services (for large language models and autonomous agents) <a class="yt-timestamp" data-t="00:25:18">[00:25:18]</a>.

### Installation and Usage
*   **Installation**: The project's GitHub repository allows cloning, and it can be run using `docker compose up` with Docker Desktop <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>. It includes an embedded vector database <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>.
*   **APIs**:
    *   **Generate**: A JSON object with description and requirements can be passed to generate Rust project files <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.
    *   **Compile and Fix Errors**: Project files can be sent as a single flat text file to the API, which compiles, fixes errors using the LLM, and returns the corrected project <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.
*   **MCP Service**: The MCP service provides similar functionality via command-line MCP clients or by [[integration_of_ai_coding_agents_with_thirdparty_tools | integrating with modern agent frameworks]] <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.

The project is a work in progress, with ongoing Linux Foundation internships contributing to its development. Contributions are welcome to expand the knowledge base, enhance intelligence, and create more functionalities for other agents <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>.