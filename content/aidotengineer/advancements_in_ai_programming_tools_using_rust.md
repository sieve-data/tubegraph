---
title: Advancements in AI programming tools using Rust
videoId: bbq0b_FpYEY
---

From: [[aidotengineer]] <br/> 

Rust is increasingly recognized as a key language for artificial general intelligence (AGI), particularly in the context of [[tool_usage_and_development_in_ai_frameworks|AI programming tools]] and code generation <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The focus is shifting towards AI-first development, where human assistance supports AI coders rather than the other way around <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Why Rust for AI?

Rust, a programming language celebrating its 10th anniversary, has been consistently voted the "most beloved programming language" in Stack Overflow's developer surveys for the past decade <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. Despite its popularity among developers, its adoption rate for new projects isn't as high as languages like Python or JavaScript <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This is primarily due to Rust's steep [[rust_learning_curve_for_ai_and_human_coders|learning curve]] for humans <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

The difficulty for humans stems from Rust's powerful compiler, which rigorously enforces correct and optimized code from the outset <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Unlike C++, Python, or JavaScript, Rust's strong type system and strict checks prevent common bugs and non-optimal practices early in the development cycle <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Once a Rust project compiles, there is a very high likelihood it will run correctly as intended, reducing the need for extensive debugging <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

This characteristic makes Rust uniquely suited for machines, particularly AI code generators <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. As Brett Taylor, Chairman of OpenAI, noted, while humans prefer Python for its ease of writing, Rust's structural orientation and strong compiler checking make it ideal for machines <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. The compiler provides a tight and clear feedback loop, acting as an excellent "reward function" for [[developing_ai_agents_for_productivity|AI agents]] in a reinforcement learning context <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. This allows AI models to quickly learn and generate correct, high-quality code <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. In a future where AI writes most code, Rust could be the optimal language due to its correctness verification and efficiency, rather than human readability <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## The [[rust_coder_project_for_aigenerated_code|Rust Coder Project]]

The [[rust_coder_project_for_aigenerated_code|Rust Coder]] project aims to bridge the gap by teaching Rust to AI and enabling AI to generate superior Rust code <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Sponsored by Linux Foundation internship grants and utilizing educational materials from the Rust Foundation, the project has dual goals:

*   **For Humans**: To make learning Rust easier, assist in writing Rust code, and improve the experience of working with Rust in integrated development environments (IDEs) <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **For Machines**: To facilitate the on-the-fly generation of correct Rust code <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. This aligns with the belief that the path to [[role_of_rust_in_artificial_general_intelligence|AGI]] may come from advanced code generators that can plan, execute, and verify tasks by generating code <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

### Demos and Features

#### Helping Humans Learn Rust

The project incorporates Rust educational materials and hundreds of common Rust development tasks into a knowledge base using embeddings and a vector database <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. This system allows users to ask programming questions or define tasks, and the AI agent can provide Rust answers and code <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

A demonstration showed a `CHV Coder` model running on the Gaia network, accessed via the Cursor IDE, solving a complex problem of converting numbers to different bases in Rust <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>. The AI not only generated the correct code but also provided a detailed explanation of its structure and functions <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>. This approach has been successfully used by over a thousand developers in a university-based Rust bootcamp, where the system consistently solves complex exam questions and explains the solutions <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

#### Helping Humans Code in IDEs (MCP Server)

For more advanced human assistance within IDEs, the [[rust_coder_project_for_aigenerated_code|Rust Coder]] project integrates an MCP (Multi-Modal Compute Protocol) server into IDEs like Cursor <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. This server provides several MCP tools:

*   **`generate`**: Given a description and requirements, this tool can generate an entire Rust project. It leverages a vector database containing common Rust algorithms and use cases to find templates and modify them accordingly <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **`compile and fix`**: This powerful tool allows users to submit Rust project files to the MCP server. The server then compiles the code using its own Rust compiler. If compilation errors are encountered, it uses its integrated large language model (LLM) to identify and fix the source code, repeating the compile-fix cycle until the code compiles correctly <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>.

A demo illustrated the `compile and fix` tool correcting a simple syntax error in a "Hello World" Rust program <a class="yt-timestamp" data-t="00:14:32">[00:14:32]</a>. The tool intelligently identifies the error, suggests the fix, and allows the IDE to apply it <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>. A key advantage of this tool is its fully integrated solution with a dedicated knowledge base of Rust compiler error messages and their fixes <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This knowledge base is self-improving, learning from interactions and contributions to become more intelligent over time in fixing complex Rust issues <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

### Underlying Technology Stack

The [[rust_coder_project_for_aigenerated_code|Rust Coder]] project is built on an [[use_of_open_source_tools_for_ai_development|open source]] technology stack <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>:

*   **LlamaEdge**: A Linux Foundation project that runs large language models and other AI models (e.g., Yolo, Whisper, TTS, Stable Diffusion) across various GPUs and MPUs. Notably, its runtime is much smaller than PyTorch, measured in tens of megabytes <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.
*   **Integrated Knowledge Base**: A core component that includes vortex search (using Elastic Search and TiDB) and vector search (using Qdrant), along with various configurable vector embedding models <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
*   **Gaia Network**: A product built on LlamaEdge that packages these components <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
*   **Open MCP Proxy**: Used to turn the system into an MCP server, enabling [[using_tools_and_function_calls_with_ai_sdk|tool usage and development in AI frameworks]] <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>.

## Future Vision: Machines as Users

Historically, computers were primarily designed for human interaction (web, desktop, mobile UIs) <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>. The "API first" era shifted this, making other deterministic computers the primary consumers of services (e.g., Stripe, Twilio) <a class="yt-timestamp" data-t="00:22:19">[00:22:19]</a>. With the advent of large language models, a new paradigm emerges where LLMs themselves become the "users" of software through [[using_tools_and_function_calls_with_ai_sdk|tool calls]] <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

The [[rust_coder_project_for_aigenerated_code|Rust Coder]] project aligns with this vision by providing Rust compiler services and LLM-based bug-fixing services as tools for other LLMs to consume <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>. The long-term vision is for AI systems to autonomously generate complex Rust code, compile and debug it, and then deploy it for real-world tasks, such as directing a drone, all without human intervention but with strong guarantees of correctness <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. This represents a significant step towards achieving [[role_of_rust_in_artificial_general_intelligence|AGI]] through the power of AI-generated code <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.

## Getting Started

The [[rust_coder_project_for_aigenerated_code|Rust Coder]] is part of the "Local Rust" program, a set of Rust tools designed for computers <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>. It offers both traditional APIs for workflow engines and deterministic software, and MCP services for interaction with large language models, crucial for autonomous agents <a class="yt-timestamp" data-t="00:25:18">[00:25:18]</a>.

Installation is straightforward via its GitHub repository, using Docker Compose to spin up all necessary containers and connect to specified coding LLMs <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>. Users can interact with it via web service APIs (e.g., `generate` to create Rust projects from JSON descriptions, `compile and fix` to submit code for automated debugging) or through MCP clients within modern agent frameworks <a class="yt-timestamp" data-t="00:26:09">[00:26:09]</a>.

The project is an ongoing effort, with continuous development and a strong encouragement for community contributions to expand its knowledge base and functionalities <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>.