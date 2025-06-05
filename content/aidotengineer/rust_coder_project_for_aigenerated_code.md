---
title: Rust Coder project for AIgenerated code
videoId: bbq0b_FpYEY
---

From: [[aidotengineer]] <br/> 

The Rust Coder project is presented as a crucial initiative in the development of [[role_of_rust_in_artificial_general_intelligence | artificial general intelligence]] (AGI), advocating for Rust as the primary language for AI coders and their human assistants <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The philosophy behind this project is "AI first, human second" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Why Rust for AI Coders?

Rust, a programming language that recently celebrated its 10th anniversary, has consistently been recognized as the most beloved programming language in Stack Overflow's developer survey for the past decade <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. While Rust enjoys high admiration (82% love it), its desired-to-use rate is lower than Python, indicating that humans find it somewhat difficult or are hesitant to use it <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### The Human Challenge with Rust
For humans, Rust presents a very steep [[rust_learning_curve_for_ai_and_human_coders | steep learning curve]] <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. This difficulty stems from its powerful compiler, which rigorously enforces correct and optimized code from the outset <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Unlike languages such as Python or JavaScript, which may allow for quicker initial results despite being prone to bugs and difficult to maintain <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>, Rust demands precision. However, once mastered, writing correct code in Rust becomes significantly easier than in other languages <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.

### Rust's Suitability for AI
The rigorous nature of Rust, particularly its strong compiler checking and type system, makes it exceptionally well-suited for machines <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. The compiler provides a tight feedback loop, which is ideal for AI models, especially in reinforcement learning contexts <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. When a Rust project compiles successfully, there is a high likelihood it will run correctly as intended, minimizing the need for extensive [[coding_and_debugging_in_ai_workshops | debugging]] post-compilation <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. This provides a clear "reward function" for AI, where a correct answer is defined by what the compiler accepts <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.

If the future of code generation is dominated by AI, Rust is considered a perfect fit for [[advancements_in_ai_programming_tools_using_rust | AI code generators]] <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. While human-comprehensible languages like Python or JavaScript are beneficial for human developers, AI-generated code in Rust could be easier for AI to verify for correctness, even if it's harder for humans to directly understand <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## Rust Coder Project Goals

The Rust Coder project, sponsored by Linux Foundation internship grants <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>, aims to achieve several specific goals:

*   **For Humans**:
    *   Make it easier for [[advancements_in_ai_programming_tools_using_rust | AI assistants]] to help humans [[rust_learning_curve_for_ai_and_human_coders | learn Rust]] <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   Simplify writing code with Rust <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   Improve the experience of working with Rust in integrated development environments (IDEs) <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   **For Machines**:
    *   Enable the generation of Rust code on the fly <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   Facilitate machines in generating correct Rust code by working with the compiler to ensure correctness <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
    *   Contribute to the path of AGI through code generators <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.

## Rust Coder Features and Demos

### 1. Helping Humans Learn Rust
The project creates a knowledge base of Rust educational materials and common developer tasks, generating embeddings stored in a vector database <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. This system allows users to ask programming questions or define tasks, and an AI agent provides Rust-specific answers and code <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

A demo illustrates an AI agent solving a complex Rust programming problem (converting numbers to different bases), providing both the code and a detailed explanation of its structure and functions <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. This functionality is actively used by over a thousand developers in a university-based Rust camp <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

### 2. Assisting Humans in IDEs
The Rust Coder project integrates an MCP (Machine Code Protocol) server into IDEs like Cursor to assist with [[coding_and_debugging_in_ai_workshops | coding and debugging Rust]] <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. It offers two primary MCP tools:

*   **`generate`**: This tool takes a description and requirements to generate an entire Rust project <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. It leverages a vector database containing common algorithms and Rust use cases to find templates and modify them according to the input <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   **`compile and fix`**: This tool receives Rust project files, compiles them using its own Rust compiler, and if errors are encountered, uses its integrated large language model to identify and attempt to fix the source code <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. It repeats this process until the code compiles successfully <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

    A demo shows the `compile and fix` tool automatically correcting a syntax error in a simple "hello world" Rust project by adding a missing closing parenthesis <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>. The tool's knowledge base of Rust compiler error messages grows over time as it learns from user interactions and external solutions <a class="yt-timestamp" data-t="00:17:08">[00:17:08]</a>. This integrated solution is designed to be more effective for Rust problems than generic coding large language models <a class="yt-timestamp" data-t="00:17:50">[00:17:50]</a>.

## Underlying Technology Stack

The Rust Coder project is built on an open-source technology stack <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>:

*   **Coding Large Language Models**: It supports both commercial and open-source models, such as the `chancoder` model used in demonstrations <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. Prompts are optimized and tailored for each specific model <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.
*   **Self-Improving Knowledge Base**: A core component, this knowledge base stores Rust compiler error messages and their typical fixes <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. It utilizes:
    *   **Llama Age**: A Linux Foundation project that runs large language models and other AI models (e.g., YOLO, Whisper, Stable Diffusion) across various GPUs and MPUs <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. It's significantly smaller than PyTorch, measured in tens of megabytes <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
    *   **Vortex Search**: Used for integrated knowledge base, leveraging Elastic Search and TiDB <a class="yt-timestamp" data-t="00:20:43">[00:20:43]</a>.
    *   **Vector Search**: Utilizes Quadrant and various vector embedding models <a class="yt-timestamp" data-t="00:20:49">[00:20:49]</a>.
*   **GIA Network**: A product built on Llama Age that packages the knowledge base and models <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
*   **Open MCP Proxy**: Used to turn the GIA Network into an MCP server, enabling integration with other systems <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.

## Vision: Autonomous Machine-to-Machine Interaction

The long-term vision for Rust Coder extends beyond human-assisted development. While currently used for humans, MCP services are ultimately designed for machines <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>. In the evolving landscape of computing, where large language models behave like humans but are fundamentally computers, "tool calls" (like MCP) represent a new way for software to be consumed by users <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

The project envisions a future where autonomous agents use these services to generate and validate Rust code without human intervention <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>. For example, an AI controlling a drone could generate Rust code to direct its flight and behavior, automatically compile and [[coding_and_debugging_in_ai_workshops | debug]] it until it works, and then upload it to the drone <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. This approach offers reasonable guarantees of code correctness for AI-generated applications <a class="yt-timestamp" data-t="00:24:26">[00:24:26]</a>.

## Getting Started with Local Rust

The Rust Coder project is part of a broader program called "local rust," which provides Rust tools for computers <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>. It offers both APIs (for deterministic software programs and workflow engines) and MCP services (for large language models and autonomous agents) <a class="yt-timestamp" data-t="00:25:18">[00:25:18]</a>.

Installation is straightforward: clone the GitHub repository and run `docker compose up` where Docker Desktop is installed <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>. This spins up all necessary containers, connects to the specified coding large language model, and embeds a vector database <a class="yt-timestamp" data-t="00:25:54">[00:25:54]</a>.

Accessible services include:

*   **`generate` API**: Accepts a JSON object with description and requirements to generate Rust project files <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.
*   **`compile and fix` API**: Takes a flat text file of project files, runs the Rust compiler and large language model to fix errors, and returns the entire project in the same format <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.
*   **MCP Service**: Standard tool calls for modern agent frameworks, allowing large language models to determine when to generate or fix Rust code <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.

The project is continually evolving, with ongoing Linux Foundation internships contributing to its progress <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>. The belief remains that [[advancements_in_ai_programming_tools_using_rust | AI coders]] are the path to AGI, and Rust is the optimal language for them <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>. Contributions to expand the knowledge base and add more functionalities are welcomed <a class="yt-timestamp" data-t="00:28:59">[00:28:59]</a>.