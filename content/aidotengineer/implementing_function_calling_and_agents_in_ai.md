---
title: Implementing function calling and agents in AI
videoId: KUEmEb71vzQ
---

From: [[aidotengineer]] <br/> 

This article explores the concepts and practical implementations of [[function_calling_in_ai_models | function calling]] and [[components_of_ai_agents | AI agents]], drawing insights from a workshop led by Elan, from OpenAI's developer experience team <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The core argument is that [[function_calling_in_ai_models | function calling]] is fundamental to much of the exciting advancements in AI today <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

## A Brief History of Tool Use in Language Models

The evolution of language models and their ability to interact with external tools can be traced through several stages:

*   **Text Completion** <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>: Early models like GPT, GPT-2, and GPT-3 primarily completed text based on input <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. Getting them to follow instructions was difficult, often requiring "few-shot" examples (e.g., "Question, Answer, Question, Answer") <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Instruction Following (InstructGPT)** <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>: OpenAI introduced InstructGPT, which enabled models to actually perform tasks specified in prompts, rather than just completing text <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Roles and Personas** <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>: The introduction of "user" and "assistant" roles, achieved through post-training, allowed models to adopt specific personas <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   **External Tools** <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>: The ability to provide models with additional tools for interacting with external states marked a significant step <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   **WebGPT (2021)** <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>: An early version of GPT-3 was trained to use specific web search functions. This was one of the first instances where the model generated actions, which were then parsed and used to re-introduce context <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
    *   **Meta's Toolformer (2022)** <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>: Meta developed a method to teach models how to use *any* tools, using techniques like analyzing log probabilities to strategically insert [[function_calling_in_ai_models | function calls]] <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>, <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
    *   **OpenAI General Function Calling (June 2023)** <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>: OpenAI launched generalized [[function_calling_in_ai_models | function calling]], where models were post-trained to use tools via a specific syntax, making it widely accessible <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

## Function Calling: A Crash Course

[[function_calling_in_ai_models | Function calling]] serves two main purposes:
1.  **Fetching Data** <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>: This includes reading APIs, retrieval, or accessing memory.
2.  **Taking Action** <a class="yt-timestamp" data-t="00:10:30">[00:10:30]</a>: This involves writing to APIs, managing application state (UI, frontend, backend), or executing workflow actions <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### How it Works

The core mechanism involves a loop <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>:
1.  You provide the model with a list of available functions and the user's input <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
2.  The model tells you its *intent* to use a function (it does not execute the function itself) <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
3.  You are responsible for parsing the model's intent, executing the actual code, and then providing the result back to the model <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>.
4.  The model uses this result in its subsequent generation <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

### Best Practices

*   **Clear Function Descriptions** <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>: Explain the purpose of each parameter and use a system prompt with examples <a class="yt-timestamp" data-t="00:12:18">[00:12:18]</a>.
*   **Software Engineering Principles** <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>: Make functions intuitive and follow the principle of least privilege <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. If a human can't easily understand how to use it, the model might struggle too <a class="yt-timestamp" data-t="00:12:36">[00:12:36]</a>.
*   **Enums and Object Structure** <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>: Use these to prevent the model from making invalid calls or representing invalid states <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

### Functions vs. Tools

The terms "functions" and "tools" are often used interchangeably, but a distinction can be made:
*   **Functions:** Refer to the raw [[function_calling_in_ai_models | function calling]] interface, where you provide a schema and are responsible for execution <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.
*   **Tools:** A broader category that includes functions, but also hosted solutions like code interpreters or file search capabilities <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

## Agents as Loops

The fundamental concept of an [[components_of_ai_agents | AI agent]] is often described as a "loop" <a class="yt-timestamp" data-t="00:20:19">[00:20:19]</a>. This loop involves:
1.  Specifying available tools to the model <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.
2.  Calling the model to get a message <a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>.
3.  Handling any tool calls the model suggests <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.
4.  Appending the results back to the conversation <a class="yt-timestamp" data-t="00:20:33">[00:20:33]</a>.
5.  Repeating until no more tool calls are suggested <a class="yt-timestamp" data-t="00:20:37">[00:20:37]</a>.

This simple loop forms the basis for more complex agent behaviors <a class="yt-timestamp" data-t="00:20:39">[00:20:39]</a>.

## Building and Improving AI Agents

### Implementing Memory

A simple form of memory can be implemented by maintaining a list of past interactions or relevant information.

> [!TIP] Simple Memory Implementation
> Memory can be as simple as a Python list <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>. Functions can be used to `add_to_memory` and `get_memory` <a class="yt-timestamp" data-t="00:27:00">[00:27:00]</a>. For persistence, this memory can be stored in a local JSON file, read at the beginning, and written out after updates <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>.
>
> **Example:** An agent remembers a user's height after being told, and can recall it in a later conversation even after restarting <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>, <a class="yt-timestamp" data-t="00:31:39">[00:31:39]</a>.

For more advanced memory, one could implement "smart querying" using retrieval or semantic similarity to load only the most relevant memories <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>. To enforce consistency in stored memories, especially for contradictory information (e.g., project status changing from "not ready" to "done"), consider:
*   Doing a retrieval search for similar memories before storing a new one <a class="yt-timestamp" data-t="01:32:11">[01:32:11]</a>.
*   Using a model to explicitly check if a new memory updates or contradicts an existing one <a class="yt-timestamp" data-t="01:32:21">[01:32:21]</a>.
*   Employing timestamps for memories and creating explicit "chains of updates" (nodes pointing from older to newer information) to manage evolving data <a class="yt-timestamp" data-t="01:32:54">[01:32:54]</a>, <a class="yt-timestamp" data-t="01:33:08">[01:33:08]</a>.

### Delegation

[[role_of_ai_agents_in_planning_and_executing_tasks | Agents]] can delegate tasks in several ways:

*   **Handoffs** <a class="yt-timestamp" data-t="00:34:27">[00:34:27]</a>: A conversation is entirely swapped to a different agent, which involves replacing the system prompt and tools <a class="yt-timestamp" data-t="00:34:30">[00:34:30]</a>.
*   **Nested Calls** <a class="yt-timestamp" data-t="00:34:37">[00:34:37]</a>: One function call triggers another, often overlooked for its simplicity and effectiveness <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>.
*   **Manager Tasks** <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>: More asynchronous delegation, where a primary agent manages tasks given to other agents <a class="yt-timestamp" data-t="00:34:46">[00:34:46]</a>.

> [!EXAMPLE] Delegating to a Smarter Model
> An agent can be given a function, `delegate_to_smarter_model`, which makes an API request to a more powerful model (e.g., GPT-4) for difficult tasks <a class="yt-timestamp" data-t="00:35:00">[00:35:00]</a>, <a class="yt-timestamp" data-t="00:35:36">[00:35:36]</a>. This allows the primary agent to offload complex computations or creative writing tasks, improving its overall capability <a class="yt-timestamp" data-t="00:37:05">[00:37:05]</a>, <a class="yt-timestamp" data-t="00:38:03">[00:38:03]</a>.

### Asynchronous Operations

To prevent the user experience from being blocked while a delegated task is running, asynchronous operations are crucial.

The problem with synchronous function calls is that they block the main loop, making the user wait for all tasks to complete <a class="yt-timestamp" data-t="00:40:49">[00:40:49]</a>, <a class="yt-timestamp" data-t="00:51:52">[00:51:52]</a>.

> [!TIP] Implementing Asynchronous Function Calling
> Use `asyncio.sleep` (or equivalent for API calls) to simulate non-blocking operations <a class="yt-timestamp" data-t="00:52:53">[00:52:53]</a>. The key is to separate user input from the background processing of messages, often using a message queue <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>. When a model makes multiple tool calls, these can be run in parallel using `asyncio.gather` <a class="yt-timestamp" data-t="00:46:35">[00:46:35]</a>.

This allows the agent to continue interacting with the user while tasks run in the background. To track these background tasks, a `create_task` function can generate a unique task ID, and a `check_task` function can retrieve the status of a specific task by its ID <a class="yt-timestamp" data-t="00:55:17">[00:55:17]</a>.

> [!EXAMPLE] Asynchronous Task Management
> An agent can create a task (e.g., to fetch weather for a city) <a class="yt-timestamp" data-t="00:57:10">[00:57:10]</a>. While the task runs in the background (with a simulated delay), the user can continue chatting with the agent <a class="yt-timestamp" data-t="00:57:59">[00:57:59]</a>. The user can then explicitly ask to `check_tasks` to see if the task has completed and get the result <a class="yt-timestamp" data-t="00:58:05">[00:58:05]</a>. This demonstrates how an agent can manage multiple concurrent operations <a class="yt-timestamp" data-t="01:00:34">[01:00:34]</a>.

## Advanced and Experimental Concepts

### Self-Modifying Agents (Tool Writing Agents)

It's possible to create an agent that can write its own functions and then immediately use them <a class="yt-timestamp" data-t="01:17:16">[01:17:16]</a>. This involves having a function that takes a string representation of Python code, evaluates it, and adds the resulting function object to the agent's available tools <a class="yt-timestamp" data-t="01:22:56">[01:22:56]</a>.

> [!WARNING] Security Risk
> Using `eval` or `exec` in a production environment or with untrusted input is extremely dangerous and can lead to severe security vulnerabilities <a class="yt-timestamp" data-t="01:19:55">[01:19:55]</a>, <a class="yt-timestamp" data-t="01:21:31">[01:21:31]</a>.

> [!EXAMPLE] Building a Calculator On-the-Fly
> An agent is instructed to "make itself a little calculator" <a class="yt-timestamp" data-t="01:25:59">[01:25:59]</a>. It then generates Python code for a `calculate` function, adds it to its tools, and can immediately use it to perform calculations requested by the user <a class="yt-timestamp" data-t="01:26:09">[01:26:09]</a>.

### Real-Time API Tricks

For conversational AI, especially with voice interfaces, specific tricks can enhance the experience:

*   **"Stay Silent" Function** <a class="yt-timestamp" data-t="01:27:46">[01:27:46]</a>: Use a [[function_calling_in_ai_models | function call]] to let the model decide if the user is truly done talking, even if the voice activity detection (VAD) triggers. This allows for natural pauses or interruptions without prematurely ending the model's turn <a class="yt-timestamp" data-t="01:27:55">[01:27:55]</a>.
*   **XML Tag Control** <a class="yt-timestamp" data-t="01:29:15">[01:29:15]</a>: By providing the model with a script containing XML tags (e.g., `<break time="500ms"/>`), it can learn to follow specific speaking styles or pauses, even if not explicitly trained for it <a class="yt-timestamp" data-t="01:29:17">[01:29:17]</a>, <a class="yt-timestamp" data-t="01:30:23">[01:30:23]</a>.

## Key Considerations for Implementing AI Agents

*   **Managing Numerous Functions**: When dealing with dozens or hundreds of functions, consider:
    *   **Multi-agent architectures** <a class="yt-timestamp" data-t="01:07:53">[01:07:53]</a>: Split responsibilities or function groupings across different agents, invoking the correct agent for specific tasks <a class="yt-timestamp" data-t="01:07:59">[01:07:59]</a>. This is a primary use case for [[building_and_improving_ai_agents | agents]] and handoffs <a class="yt-timestamp" data-t="01:15:22">[01:15:22]</a>.
    *   **Fine-tuning** <a class="yt-timestamp" data-t="01:08:30">[01:08:30]</a>: Smaller models can be fine-tuned to work with a large number of functions (e.g., 120 functions with GPT-3.5) <a class="yt-timestamp" data-t="01:08:35">[01:08:35]</a>.
    *   **Dynamic Function Loading** <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>: Based on input or conversation, load only the most relevant functions into memory or context <a class="yt-timestamp" data-t="01:08:54">[01:08:54]</a>.
*   **Performance with Many Tools**: While there are no hard limits on the number of functions or parallel calls, a general rule of thumb for reliable performance without extensive prompting is 10-20 functions <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>, <a class="yt-timestamp" data-t="01:16:46">[01:16:46]</a>.
*   **Vision Models and Thought Text**: For models like GPT-4, [[function_calling_in_ai_models | function calls]] typically happen at the very end of the generation process, as the internal "chain of thought" is not exposed for direct [[function_calling_in_ai_models | function calls]] within it <a class="yt-timestamp" data-t="01:09:36">[01:09:36]</a>, <a class="yt-timestamp" data-t="01:10:12">[01:10:12]</a>.
*   **Designing Agent Projects**: Many frameworks exist for [[developing_and_optimizing_ai_agents | developing and optimizing AI agents]] (e.g., Swarm, Pydantic-AI) <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>, <a class="yt-timestamp" data-t="01:06:17">[01:06:17]</a>. However, it's also feasible to implement a basic agent loop with minimal code (around 70 lines), allowing for granular control and avoiding unnecessary dependencies <a class="yt-timestamp" data-t="01:06:33">[01:06:33]</a>.

> [!INFO] Further Exploration
> Many of the discussed concepts, like memory and delegation, can be extended to significant complexity, evolving into full operating systems for managing agent behavior <a class="yt-timestamp" data-t="01:31:55">[01:31:55]</a>.