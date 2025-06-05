---
title: Coding large language models and Rust
videoId: bbq0b_FpYEY
---

From: [[aidotengineer]] <br/> 

## Rust as the Language of AGI
The speaker, Michael Yu, proposes that [[rust_programming_language_for_ai_development | Rust]] is the language of Artificial General Intelligence (AGI) because it is well-suited for [[large_language_models_in_code_generation | AI coders]] and their human assistants <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. He believes the future will be "AI first, human second" in terms of code generation <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Why Rust is Suited for AI
[[rust_programming_language_for_ai_development | Rust]] is a programming language that recently celebrated its 10th anniversary <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. It has consistently been ranked as the "most beloved" programming language in Stack Overflow's developer survey for the past decade <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. While admired (82% admiration rate) <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, its "desired to use" rate is lower, indicating a hesitation among human developers <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.

### [[challenges_and_benefits_of_using_rust | Challenges and Benefits for Humans]]
For humans, [[rust_programming_language_for_ai_development | Rust]] has a very steep learning curve <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. Its powerful compiler forces developers to write correct and optimized code from the outset, which can be difficult for beginners <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Unlike languages like C++, Python, or JavaScript (which may not even have compilers), Rust prevents bug-prone practices <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Once mastered, however, it becomes easier to write correct code in [[rust_programming_language_for_ai_development | Rust]] than in other languages <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. This human-centric preference often leads to the use of languages like Python or JavaScript for quicker results, despite potential bugs or maintenance issues <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

### Benefits for AI
OpenAI Chairman Brett Taylor noted that while humans prefer Python, [[rust_programming_language_for_ai_development | Rust]] is better suited for machines <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
It is more efficient and structurally oriented due to its strong compiler checking and type system, making it more rigorous <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. A significant advantage is the tight feedback loop provided by the [[rust_programming_language_for_ai_development | Rust]] compiler <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Once a [[rust_programming_language_for_ai_development | Rust]] project compiles, there's a high likelihood it will run correctly as intended, which is not true for many other languages <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

This property makes [[rust_programming_language_for_ai_development | Rust]] ideal for AI <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>:
*   **Reward Function:** The compiler's acceptance of code acts as a strong reward function for [[large_language_models_in_code_generation | large language models]] (LLMs), similar to reinforcement learning in AlphaGo or AlphaZero <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>. It forces AI to generate correct code <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.
*   **AI Code Generation:** If AI will write most code in the future, [[rust_programming_language_for_ai_development | Rust]] is preferred over human-comprehensible but less rigorous languages like Python or JavaScript <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. [[rust_programming_language_for_ai_development | Rust]] is friendly to AI and reasonably friendly to humans for verification <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

## The [[rust_coder_project_and_ai_integration | Rust Coder Project]]
The [[rust_coder_project_and_ai_integration | Rust Coder project]] was initiated with the goal of teaching [[rust_programming_language_for_ai_development | Rust]] to AI and enabling AI to generate better [[rust_programming_language_for_ai_development | Rust]] code <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. The project is sponsored by Linux Foundation internship grants and uses educational materials from the [[rust_programming_language_for_ai_development | Rust]] Foundation <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

Its goals include:
*   **For Humans:** Making it easier to learn [[rust_programming_language_for_ai_development | Rust]], write code, and work with [[rust_programming_language_for_ai_development | Rust]] in IDEs using AI assistants <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   **For Machines:** Enabling the generation of [[rust_programming_language_for_ai_development | Rust]] code on the fly <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. The path to AGI may involve code generators, where an LLM can either call APIs or generate code to perform tasks <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. The project aims to make it easier for machines to generate correct [[rust_programming_language_for_ai_development | Rust]] code and verify its correctness with the compiler <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### Demos of [[rust_coder_project_and_ai_integration | Rust Coder]]
#### 1. Helping Humans Learn [[rust_programming_language_for_ai_development | Rust]]
This demo showcases an AI agent that assists in learning [[rust_programming_language_for_ai_development | Rust]] <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. The process involves:
*   Taking [[rust_programming_language_for_ai_development | Rust]] educational materials.
*   Generating hundreds of common [[rust_programming_language_for_ai_development | Rust]] development tasks.
*   Building a knowledge base using embeddings and a vector database.
*   Allowing users to ask programming questions or tasks to the AI agent, which provides a [[rust_programming_language_for_ai_development | Rust]] answer <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

In a demonstration, the Chemcoder model running on the Gaia network within the Cursor IDE successfully writes a [[rust_programming_language_for_ai_development | Rust]] program to convert numbers to different bases, including explanations of the code's structure and functions <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. This system has been used by over a thousand developers in a university-based [[rust_programming_language_for_ai_development | Rust]] boot camp, consistently solving exam questions in one shot <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.

#### 2. Helping Humans Code [[rust_programming_language_for_ai_development | Rust]] in an IDE
The [[rust_coder_project_and_ai_integration | Rust Coder]] project integrated an MCP (Machine Code Programming) server into the Cursor IDE <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. This local [[rust_coder_project_and_ai_integration | Rust Coder]] MCP server (running on localhost:3000) provides two key tools:
*   **`generate`**: Given a description and requirements, this tool generates an entire [[rust_programming_language_for_ai_development | Rust]] project, leveraging a vector database with common algorithms and [[rust_programming_language_for_ai_development | Rust]] use cases as templates <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   **`compile and fix`**: This tool takes [[rust_programming_language_for_ai_development | Rust]] project files, sends them to the MCP server for compilation with its own [[rust_programming_language_for_ai_development | Rust]] compiler <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. If errors are encountered, it uses its own [[large_language_models_in_code_generation | large language model]] to identify and fix the source code, repeating the process until compilation is successful <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

A demo illustrates `compile and fix` correcting a simple syntax error (missing closing bracket) in a "Hello, world!" program <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. The tool's advantage lies in its fully integrated solution with a knowledge base of [[rust_programming_language_for_ai_development | Rust]] compiler error messages and their fixes <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This knowledge base grows as it learns from fixes, making it more intelligent over time for [[rust_programming_language_for_ai_development | Rust]] development than generic [[large_language_models_in_code_generation | coding large language models]] <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

## The Future: MCP for Machines and AGI
Historically, computer interfaces evolved from human-centric UIs (web, desktop, mobile) to API-first approaches where other computers consumed services <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. With the advent of [[large_language_models_in_code_generation | large language models]], "Tools" (like MCP) represent a new way for applications to be consumed, with LLMs acting as users <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

The vision for the [[rust_coder_project_and_ai_integration | Rust Coder project]] is to provide these services (like [[rust_programming_language_for_ai_development | Rust]] compilation and LLM-based bug fixing) as tools for other [[large_language_models_in_code_generation | large language models]] to use <a class="yt-timestamp" data-t="00:23:41">[00:23:41]</a>. This enables a future where AI agents can:
*   Generate [[rust_programming_language_for_ai_development | Rust]] code on the fly for complex tasks (e.g., controlling a drone) <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.
*   Automatically compile and debug the code until it works <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>.
*   Execute tasks entirely without human intervention, with reasonable guarantees of code correctness <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.
This is considered a long-term vision for [[automation_and_rust_in_agi_development | AGI development]] <a class="yt-timestamp" data-t="00:24:30">[00:24:30]</a>.

## Tech Stack: Local Rust Project
The [[rust_coder_project_and_ai_integration | Rust Coder]] is part of a program called "Local Rust," which provides [[rust_programming_language_for_ai_development | Rust]] tools for computers through APIs (for workflow engines) and MCP services (for [[large_language_models_in_ai_agents | autonomous agents]] and LLMs) <a class="yt-timestamp" data-t="00:25:05">[00:25:05]</a>.

Key components and features:
*   **Easy Installation**: Clonable GitHub repository with a Docker Compose script for spinning up all containers <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>.
*   **APIs**:
    *   `generate`: Accepts a JSON object with description and requirements to generate [[rust_programming_language_for_ai_development | Rust]] project files <a class="yt-timestamp" data-t="00:26:26">[00:26:26]</a>.
    *   `compile and fix`: Takes a flattened text file of project files, runs the [[rust_programming_language_for_ai_development | Rust]] compiler and an LLM to fix errors, and returns the corrected project <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>.
*   **MCP Service**: Integrates with modern agent frameworks, allowing LLMs to use standard tool calls for [[rust_programming_language_for_ai_development | Rust]] code generation and error fixing <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>.
*   **Llama Edge Project**: An underlying Linux Foundation project that runs [[building_and_scaling_large_language_models | large language models]] and other AI models (YOLO, Whisper, TTS, Stable Diffusion) across various GPUs and MPUs <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. It has a small runtime (tens of megabytes), unlike PyTorch <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
*   **Integrated Knowledge Base**: A core part of the system that includes vortex search (Elasticsearch, TiDB) and vector search (Qdrant) with various vector embedding models <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>. It contains a self-improving knowledge base of [[rust_programming_language_for_ai_development | Rust]] compiler error messages and their fixes <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.
*   **Gaia Network**: A product built on Llama Edge, which turns into an MCP server using the Open MCP proxy <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>.
*   **Optimized Prompts**: Prompts are tailored to specific [[building_and_scaling_large_language_models | large language models]] (e.g., Gamma 3 model without a system prompt) <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

The project is a work in progress, with ongoing Linux Foundation internships, and encourages community contributions to expand its knowledge base and functionalities <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>. The belief is that [[rust_programming_language_for_ai_development | Rust]] is the best language for [[large_language_models_in_code_generation | AI coders]] on the path to AGI <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>.