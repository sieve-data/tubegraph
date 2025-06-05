---
title: Rust programming language for AI development
videoId: bbq0b_FpYEY
---

From: [[aidotengineer]] <br/> 

Rust is presented as the language of Artificial General Intelligence (AGI) due to its unique characteristics, making it particularly suitable for AI coders and their human assistants <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This perspective emphasizes an "AI first, human second" approach, reflecting the evolving landscape of technology <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. Michael Yu, the speaker, is involved in the [[rust_coder_project_and_ai_integration | Rust Coder]] project, which aims to leverage Rust for AI development <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## The Appeal and Challenges of Rust

Rust, a programming language that recently celebrated its 10th anniversary, has consistently been ranked as the most beloved programming language in Stack Overflow's developer surveys for the past decade <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. In recent surveys, Rust holds an 82% admiration rate, significantly higher than other languages like Python, JavaScript, SQL, HTML, TypeScript, and Go <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

Despite its high admiration, the "desired" metric (how much people want to actually use it) for Rust is not as high as Python, although it surpasses Go <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This discrepancy points to a significant challenge for human developers: Rust has a very steep learning curve <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### Why Rust is Hard for Humans
Rust's difficulty for humans stems from its powerful compiler, which "forces you to do the right thing" by ensuring correct and optimized code from the outset <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Unlike languages like C++, Python, or JavaScript, which are more permissive, Rust's strong type system and rigorous checks prevent common bugs and sub-optimal practices <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. While this leads to more correct and efficient code once mastered, the initial learning barrier is substantial <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

Human developers often prefer languages that are easy to write, even if they might contain bugs or be harder to maintain, prioritizing quick results <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This explains the popularity of Python and JavaScript <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Rust as the Language for Machines
Brett Taylor, Chairman of OpenAI, has suggested that while humans prefer Python, Rust is better suited for machines <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Benefits for AI
Rust's advantages for AI include:
*   **Efficiency**: It's more efficient than many other languages <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   **Structural Orientation**: Its rigorous structure, strong compiler checking, and strong type system make it ideal for machines <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Tight Feedback Loop**: The Rust compiler provides a very tight feedback loop <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. A significant experience for Rust developers is that once a project compiles, there's a high likelihood it will run correctly as intended, a characteristic not shared by many other languages <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Reward Function for AI**: This property of the compiler offers a strong feedback mechanism for AI, creating an excellent "reward function" for reinforcement learning <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>. The compiler's acceptance of code serves as a clear "correct answer" for the AI model <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **Optimal for AI Code Generators**: Rust is a perfect fit for AI code generators because it forces AI to generate correct and optimized code <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>. If AI is to write most code, choosing a language that is easy for AI and allows for easy verification of correctness, like Rust, is crucial <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

## [[rust_coder_project_and_ai_integration | Rust Coder Project]]

The [[rust_coder_project_and_ai_integration | Rust Coder]] project was initiated with the specific goal of teaching Rust to AI and enabling AI to generate better Rust code <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. It is sponsored by internship grants from the Linux Foundation and uses educational materials from the Rust Foundation <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

### Goals of [[rust_coder_project_and_ai_integration | Rust Coder]]
*   **For Humans**:
    *   Make learning Rust easier with AI assistance <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
    *   Facilitate writing and working with Rust code in IDEs <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
*   **For Machines**:
    *   Enable on-the-fly generation of Rust code <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
    *   Support the belief that the path to AGI may come from code generators, where LLMs can generate and execute code to perform tasks <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    *   Facilitate machines generating correct Rust code by working with the compiler <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### Demos of [[rust_coder_project_and_ai_integration | Rust Coder]]

#### Demo 1: Helping Humans Learn Rust
This demo showcases how [[rust_coder_project_and_ai_integration | Rust Coder]] assists humans in learning Rust <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>. The process involves taking Rust education materials, generating hundreds of common Rust development tasks, building a knowledge base with embeddings and a vector database, and then allowing users to ask programming questions or tasks to an AI agent that provides Rust answers <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

*   **Example**: A complex problem of converting numbers to different bases was given to a `chancoder` model running on the Gaia network, accessed via the Cursor IDE <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
*   The AI agent immediately provided the answer and the Rust code, followed by explanations of its structure and functions <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   The generated code compiled and ran correctly <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   This project is used by over a thousand developers in university-based Rust boot camps, successfully solving exam questions in one shot and explaining solutions to learners <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.

#### Demo 2: AI-Assisted Coding in IDE with MCP Server
This demo focuses on helping humans code Rust within an IDE, using an MCP (Multi-Agent Communication Protocol) server integrated into Cursor IDE <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.

Two key MCP tools are provided:
1.  **`generate`**: Allows users to provide a description and requirements to generate an entire Rust project. It uses a vector database of common algorithms and Rust use cases to find and modify templates <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
2.  **`compile_and_fix`**: Takes Rust project files, sends them to the MCP server for compilation with its own Rust compiler <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. If an error is encountered, it uses its own [[coding_large_language_models_and_rust | coding large language model]] to diagnose and attempt to fix the source code, repeating the process until successful <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.

*   **Example**: A simple "Hello World" Rust project with a missing closing parenthesis was sent to the `compile_and_fix` tool <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
*   The Cursor IDE identified the best tool to call was `compile_and_fix` <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>.
*   The tool quickly returned the corrected code, which the IDE then applied <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.
*   The request sends the `Cargo.toml` and `main.rs` files, and the response returns the entire corrected package source code <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### [[challenges_and_insights_in_developing_ai_coding_agents | Advantages of Rust Coder's Fix Tool]]
The `rust_coder` MCP server offers a fully integrated solution with its own knowledge base of Rust compiler error messages and how to fix them <a class="yt-timestamp" data-t="00:17:02">[00:17:02]</a>. This knowledge base also grows as it's used, learning from failures and new solutions <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. This integrated stack, including its own prompt, knowledge base, and [[coding_large_language_models_and_rust | large language model]], allows it to become significantly more intelligent over time in Rust development compared to generic [[coding_large_language_models_and_rust | coding large language models]] optimized for Python or JavaScript <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>.

## Technical Stack of [[rust_coder_project_and_ai_integration | Rust Coder]]
The underlying technology stack for [[rust_coder_project_and_ai_integration | Rust Coder]] is entirely open-source <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>:
*   **Coding Large Language Models**: Configurable for commercial or open-source models, such as `chancoder`, with prompts optimized for specific models <a class="yt-timestamp" data-t="00:18:40">[00:18:40]</a>.
*   **Self-Improving Knowledge Base**: A core part of the system, it contains Rust compiler error messages and examples of how to fix them <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. Users are encouraged to contribute to this knowledge base for continuous improvement <a class="yt-timestamp" data-t="00:19:29">[00:19:29]</a>.
*   **Llama Edge Project**: A Linux Foundation project that runs LLMs and other AI models (e.g., YOLO, Whisper, TTS, Stable Diffusion) across various GPUs and MPUs <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>. It's much smaller in runtime size (tens of megabytes) compared to PyTorch (gigabytes) <a class="yt-timestamp" data-t="00:20:25">[00:20:25]</a>.
*   **Gaia Network**: A product built on Llama Edge that integrates the knowledge base <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>.
*   **Integrated Knowledge Base**: Utilizes Vortex search (Elastic Search, TiDB) and vector search (Qdrant) with various vector embedding models <a class="yt-timestamp" data-t="00:20:36">[00:20:36]</a>.
*   **Open MCP Proxy**: Used to turn the system into an MCP server <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.

## The Future: Machines as Primary Users with Tools

The presentation highlights a shift in software consumption:
*   **Early Days (Human-centric)**: Focus on Web, Desktop, Mobile UIs designed for human interaction (eyes, fingers) <a class="yt-timestamp" data-t="00:21:54">[00:21:54]</a>.
*   **API Era (Deterministic Computer Consumers)**: API-first approach where software services are consumed by other computers or workflow engines (e.g., Stripe, Twilio) <a class="yt-timestamp" data-t="00:22:16">[00:22:16]</a>.
*   **LLM Era (AI Consumers with Tools)**: The emergence of tools and MCPs means that large language models, behaving like humans but being computers, become the users consuming software services <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

This vision suggests a future where systems like [[rust_coder_project_and_ai_integration | Rust Coder]] provide services (e.g., Rust compilation, bug fixing) as tools for other LLMs <a class="yt-timestamp" data-t="00:23:29">[00:23:29]</a>. A long-term vision for the [[rust_coder_project_and_ai_integration | Rust Coder]] project is to enable an AI to control a drone by generating and automatically debugging Rust code that directs the drone's behavior, with reasonable guarantees of correctness, entirely without human intervention <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. This represents a significant step towards AGI through [[automation_and_rust_in_agi_development | automation and Rust in AGI development]] <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>.

## Local Rust Program

[[rust_coder_project_and_ai_integration | Rust Coder]] is part of a larger program called "Local Rust," which provides a set of Rust tools for computers <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>. It offers both APIs for workflow engines and deterministic software, and MCP services for large language models, both of which are crucial for autonomous agents <a class="yt-timestamp" data-t="00:25:18">[00:25:18]</a>.

### Installation and Usage
Local Rust is easy to install and run. Users can clone its GitHub repository and use a Docker Compose script to spin up all necessary containers and connect to specified [[coding_large_language_models_and_rust | coding large language models]] <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>. It includes an embedded vector database <a class="yt-timestamp" data-t="00:26:04">[00:26:04]</a>.

It exposes web service APIs for `generate` (generating Rust project files from description/requirements) and `compile_and_fix` (compiling and fixing errors in a Rust project by sending flat text files of code and receiving the corrected project back) <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>. It also provides MCP services accessible via command-line clients or integrated into modern agent frameworks <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>.

The project is an ongoing work in progress, with continued development tracked on GitHub, and contributions are welcomed <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>. The belief remains that [[automation_and_rust_in_agi_development | AI coders]] are the path to AGI, and Rust is the optimal language for them, being far superior to Python or JavaScript for AI <a class="yt-timestamp" data-t="00:28:49">[00:28:49]</a>. The goal is to build a larger, smarter knowledge base and expand functionalities for other agents <a class="yt-timestamp" data-t="00:28:59">[00:28:59]</a>.