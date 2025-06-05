---
title: Developing custom AI tools and functions
videoId: KUEmEb71vzQ
---

From: [[aidotengineer]] <br/> 

## Introduction to Function Calling

Function calling is a core concept in AI and language models that allows models to interact with external states and perform actions beyond text generation <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. It enables language models to fetch data, take actions, manage application state, and execute workflow actions <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.

### Evolution of Tool Use in AI

The progression of language models demonstrates an [[evolution_of_ai_engineering_and_tools | evolution of AI engineering and tools]] towards better integration with external functionalities:
*   **Text Completion (Original GPT models)**: Early models like GPT, GPT2, and GPT3 were base models that would continue input text <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. Getting them to follow specific instructions was difficult <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.
*   **Instruction Following (InstructGPT)**: OpenAI introduced instruction following, allowing models to perform actions based on given input rather than just completing text <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. This also led to the introduction of user and assistant roles <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>.
*   **Early Tool Integration (WebGPT)**: Around 2021, WebGPT, a version of GPT3, was trained to use a specific set of functions for web search <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. This marked an early instance of models generating actions that were then parsed and used to interact with external states <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>.
*   **Any Tool Use (Meta)**: Meta developed a method to teach models how to use any tools, leveraging log probability analysis to retroactively insert function calls where they would reduce sentence perplexity <a class="yt-timestamp" data-t="08:05:00">[08:05:00]</a>. This approach minimized the need for human-labeled examples <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.
*   **General Function Calling (OpenAI, June 2023)**: OpenAI launched general function calling, where models were post-trained to use tools without requiring extensive examples <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>. This allows models to call functions based on a defined syntax <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>.

### Purposes of Function Calling

[[using_tools_and_function_calling_in_ai_sdk | Function calling serves two main purposes]] <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>:
*   **Fetching Data**: This includes reading APIs, retrieval, and accessing memory <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.
*   **Taking Action**: This involves using APIs to write, managing application state (UI, frontend, backend), and performing workflow actions (multi-step processes, or even meta-actions like switching prompts or handing off conversations) <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>.

### How Function Calling Works

The process involves several steps <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>:
1.  **Define Functions**: Inform the model about the available functions it can use <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.
2.  **Model Suggests**: The model indicates its intent to use a function <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. It does not execute the function itself <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
3.  **User Executes**: The developer is responsible for parsing the model's intent, executing the code, and processing the result <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.
4.  **Provide Result**: The result of the function execution is provided back to the model, which can then use it in its generation <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.

### Best Practices for Writing Functions

When writing functions for AI models, [[best_practices_for_building_ai_systems | best practices for building AI systems]] include <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>:
*   **Clarity**: Write clear function descriptions and explain the purpose of each parameter <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>. Use a system prompt and include examples <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>.
*   **Software Engineering Principles**: Apply established software engineering best practices <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. Functions should be intuitive and follow the principle of least authority <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>.
*   **Validation**: Use enums and object structures to prevent the model from making invalid calls or representing invalid states <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

### Functions vs. Tools

The distinction between "functions" and "tools" is subtle <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>:
*   **Functions**: Refers to the raw function calling mechanism, where the developer provides an interface and is responsible for executing the code <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.
*   **Tools**: A superset that includes functions, but also encompasses hosted solutions like code interpreter or file search <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.

## Implementing AI Agents

[[developing_and_optimizing_ai_agents | Developing and optimizing AI agents]] often involves structuring them as loops that continuously interact with the model and handle tool calls <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.

A basic agent loop typically <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>:
1.  Specifies the available tools.
2.  Calls the language model.
3.  Receives and prints the message.
4.  Handles any tool calls suggested by the model.
5.  Appends the results back to the conversation.
6.  Continues looping until no more tool calls are suggested <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.

One useful utility is `functions_to_schema`, which converts a raw Python function object into the correct schema for the model <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

## Memory Management

Implementing memory for AI agents can range from simple to complex:
*   **Basic Memory**: A simple list can serve as memory, storing factual information about the user or their preferences. This can be stored in a local JSON file, read at the beginning, and written out after each turn <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
*   **Advanced Memory (RAG)**: For more sophisticated memory, one can implement smart querying and retrieval augmented generation (RAG) workflows <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. Instead of loading all memory, use semantic similarity or search to retrieve only relevant information <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.
*   **Ensuring Consistency**: To enforce consistency and resolve contradictions in stored memories, one approach is to perform a retrieval for similar memories before storing new information <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. An explicit check with the model can determine if the new memory updates or contradicts existing ones <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>. Using timestamps and creating explicit chains of updates can help track memory evolution and allow for presenting the latest or full history <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

## Delegation and Multi-Agent Patterns

Delegation involves having one agent or function pass a task to another, more specialized agent or function. This is a key aspect of [[developing_and_optimizing_ai_agents | developing and optimizing AI agents]].
*   **Nested Calls**: One function can directly call another AI model for a harder task (e.g., delegating to a "smarter model") <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>.
*   **Handoffs**: This involves completely swapping the conversation and tools to a different agent, which is essentially replacing the system prompt and tools <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
*   **Manager Tasks**: More asynchronous forms of delegation can involve a manager agent overseeing and assigning tasks <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.

### Routing Patterns for Many Functions

When dealing with dozens or hundreds of functions, [[scaling_ai_models_and_their_impact_on_development_tools | scaling AI models and their impact on development tools]] and efficient tool calling becomes crucial <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
*   **Multiple Agents**: Divide responsibilities by creating multiple agents, each with a focused set of related functions (e.g., an "email agent" and a "calendar agent") <a class="yt-timestamp" data-t="01:07:53">[01:07:53]</a>. A primary "triage" agent can then use special "transfer" functions to hand off the conversation to the appropriate specialized agent <a class="yt-timestamp" data-t="01:12:57">[01:12:57]</a>. This is a common primary use case for agents and handoffs <a class="yt-timestamp" data-t="01:15:20">[01:15:20]</a>.
*   **Fine-tuning**: For highly latency-sensitive cases with many functions (e.g., 120 functions with GPT-3.5), [[building_custom_evaluations_for_better_ai_performance | fine-tuning]] smaller models can improve performance <a class="yt-timestamp" data-t="01:08:30">[01:08:30]</a>.
*   **Dynamic Function Loading**: Based on user input or conversation context, dynamically load only the most relevant functions into memory or context. This can be achieved with embeddings or a two-step function call, where a function loads more functions, essentially acting as a handoff <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>.
*   **Rule of Thumb**: While fine-tuning allows for more, generally, it's advised not to exceed 10-20 functions with a single agent without extensive prompting or specific evaluations <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>.

## Asynchronous Operations

Asynchronous operations are essential for maintaining responsiveness, especially when dealing with network calls or potentially long-running tasks. This is crucial for [[integration_of_ai_coding_agents_with_thirdparty_tools | integrating AI coding agents with third-party tools]].
*   **Necessity**: In a blocking loop, long-running tasks (like multiple API calls) will cause the entire interaction to freeze <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. Asynchronous handling allows other operations to continue while a task runs in the background <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.
*   **Implementation**: Using `asyncio` in Python allows for non-blocking operations. Functions can be set up to `await` results, but the overall system can continue processing other inputs <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>.
*   **Delegated Tasks**: A pattern involves creating a task with a unique ID, returning a "response pending" status, and then having a separate function (`check_tasks`) to query the status of running tasks <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. This enables the model to continue interacting with the user while tasks complete in the background <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>.
*   **Real-time API**: OpenAI's real-time API inherently supports asynchronous functions. The model can call a function, get no immediate response, and continue the conversation until the function's response is ready, at which point it's seamlessly injected <a class="yt-timestamp" data-t="01:39:50">[01:39:50]</a>.

## Self-Modifying Agents (Generating Tools)

A powerful and experimental concept is an agent that can write its own functions <a class="yt-timestamp" data-t="01:15:30">[01:15:30]</a>.
*   **Mechanism**: A function can be created that takes a string representation of a Python function's implementation. Using Python's `exec` (with caution due to security risks) can interpret this string and add the newly defined function to the agent's available tools <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
*   **Example**: An agent could be prompted to "make yourself a little calculator" and then proceed to define and use a `calculate` function based on its own code generation <a class="yt-timestamp" data-t="01:25:59">[01:25:59]</a>. This capability demonstrates the dynamic and extensible nature of [[integration_of_ai_coding_agents_with_thirdparty_tools | AI coding agents]].

## Real-time API Specifics

When building real-time AI interactions (e.g., voice assistants), specific function calling techniques can enhance user experience:
*   **"Stay Silent" Function**: To prevent the model from interrupting a user who is merely pausing, a `stay_silent` function can be used. This function, triggered by voice activity detection (VAD), allows the model to verify if the user is truly done talking before responding <a class="yt-timestamp" data-t="01:27:12">[01:27:12]</a>. The model can be prompted to call this function when the user "is not quite done talking" <a class="yt-timestamp" data-t="01:28:09">[01:28:09]</a>.
*   **XML Tag Guidance**: Although not strictly function calling, models can be guided to speak in specific ways (e.g., controlling tone or pacing) by embedding instructions within XML tags in the generated script <a class="yt-timestamp" data-t="01:29:12">[01:29:12]</a>. This is a behavioral consequence of training rather than explicit function execution <a class="yt-timestamp" data-t="01:30:27">[01:30:27]</a>.

## User Feedback and Iteration

The interactive nature of [[user_feedback_and_ai_development | user feedback and AI development]] is highlighted throughout the development process, allowing for real-time adjustments and exploration of different implementations <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>. Prototyping tools like Swarm or Pydantic AI can be useful, but for granular control and lightweight implementations, developers often write their own loops <a class="yt-timestamp" data-t="01:06:14">[01:06:14]</a>.