---
title: Realtime API and asynchronous function handling
videoId: KUEmEb71vzQ
---

From: [[aidotengineer]] <br/> 

[[realtime_aidriven_fraud_detection_techniques | Realtime AI-driven fraud detection techniques]] and [[managing_asynchronous_experiences_in_chatbots | managing asynchronous experiences in chatbots]] are enabled by robust asynchronous function handling, particularly within the context of the OpenAI Realtime API. This allows models to perform actions in the background without interrupting the user's conversational flow <a class="yt-timestamp" data-t="00:50:02">[00:50:02]</a>.

## Evolution of AI Model Interaction
The ability of large language models (LLMs) to interact with external tools and manage asynchronous operations has evolved significantly <a class="yt-timestamp" data-t="01:16:05">[01:16:05]</a>:
*   **Text Completion** Initially, models like GPT-1, GPT-2, and GPT-3 were base models that simply continued input text <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>. Getting them to follow instructions was difficult, often requiring "few-shot" examples within the prompt <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.
*   **Instruction Following** With InstructGPT, models could be given input and would perform actions as requested <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. This introduced roles like "users" and "assistants" through post-training <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
*   **Tool/Function Calling** Eventually, models were equipped with the ability to use external tools to interact with outside systems <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>. Early examples include WebGPT (2021), a GPT-3 version trained for web search, which generated actions that were then parsed and fed back into the model's context <a class="yt-timestamp" data-t="06:44:00">[06:44:00]</a>. Meta also developed methods to teach models to use *any* tools, such as calculators or translation services, by analyzing log probabilities to insert function calls optimally <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. OpenAI launched general [[developing_custom_ai_tools_and_functions | function calling]] in June 2023, where models are pre-trained to use specific tool syntax <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

## Function Calling Fundamentals
[[using_tools_and_function_calling_in_ai_sdk | Function calling]] serves two main purposes: fetching data (e.g., from APIs, retrieval, memory) and taking action (e.g., writing to APIs, managing application state, performing [[agent_continuations_for_ai_workflows | multi-step workflow actions]]) <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.

The process of function calling involves:
1.  **Model receives tools and user input.** You define which functions the model can use <a class="yt-timestamp" data-t="11:03:00">[11:03:00]</a>.
2.  **Model outputs intent.** The model suggests which function to call and with what arguments <a class="yt-timestamp" data-t="11:12:00">[11:12:00]</a>.
3.  **Host system executes function.** The host system (your code) is responsible for parsing the model's intent, executing the actual function code, and handling the result <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>. The model itself does not execute the function <a class="yt-timestamp" data-t="11:17:00">[11:17:00]</a>.
4.  **Result returned to model.** The result is provided back to the model for its next generation <a class="yt-timestamp" data-t="11:29:00">[11:29:00]</a>.

### Best Practices for Functions
*   **Clear Descriptions:** Write clear descriptions for functions and their parameters <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.
*   **Software Engineering Principles:** Apply best practices:
    *   Functions should be intuitive <a class="yt-timestamp" data-t="12:31:00">[12:31:00]</a>.
    *   Follow the "function of least principle" <a class="yt-timestamp" data-t="12:33:00">[12:33:00]</a>.
    *   Use enums and object structures to prevent the model from making invalid calls <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.

## Asynchronous Function Handling
A common challenge in building AI applications is managing operations that take time, such as API calls or complex computations <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. If these operations are synchronous, they block the model's interaction, leading to a poor user experience <a class="yt-timestamp" data-t="03:49:00">[03:49:00]</a>.

### The Problem with Blocking Operations
In a synchronous loop, if the model needs to call multiple functions that each take a significant amount of time (e.g., 10 seconds), the total waiting time for the user will be the sum of those times <a class="yt-timestamp" data-t="00:52:37">[00:52:37]</a>.

### Introducing Asynchrony with `asyncio`
Python's `asyncio` library allows for concurrent execution of operations, particularly effective for I/O-bound tasks like network calls <a class="yt-timestamp" data-t="00:53:37">[00:53:37]</a>. By using `asyncio.sleep` instead of `time.sleep`, multiple tasks can be scheduled to run in parallel, reducing the total waiting time significantly <a class="yt-timestamp" data-t="00:53:01">[00:53:01]</a>.

### Managing Background Tasks: The "Task" Pattern
Even with `asyncio`, the model might still wait for all parallel tasks to complete before responding, which is undesirable for interactive conversations <a class="yt-timestamp" data-t="00:54:06">[00:54:06]</a>. A more advanced pattern involves:
1.  **`create_task` function:** The model can call a `create_task` function, which spins off a long-running operation (e.g., a complex model call) in the background and immediately returns a unique task ID <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>. This allows the conversation to continue <a class="yt-timestamp" data-t="00:57:59">[00:57:59]</a>.
2.  **`check_task` function:** The model or user can later call a `check_task` function with the task ID to inquire about the status and retrieve the result once the background operation is complete <a class="yt-timestamp" data-t="00:55:35">[00:55:35]</a>. This decouples the execution of the task from the immediate conversational flow <a class="yt-timestamp" data-t="00:58:05">[00:58:05]</a>.

This pattern forms the basis for [[full_stack_ai_engineering_in_serverless_environments | full-stack AI engineering in serverless environments]] and managing [[limitations_of_current_serverless_providers_for_longrunning_workflows | long-running workflows]] effectively <a class="yt-timestamp" data-t="00:59:07">[00:59:07]</a>.

### Realtime API's Native Asynchronous Handling
The OpenAI Realtime API takes asynchronous function handling a step further by supporting it natively <a class="yt-timestamp" data-t="01:39:55">[01:39:55]</a>.
*   **Non-Blocking Calls:** When the model calls a function within the Realtime API, it does not halt the conversation <a class="yt-timestamp" data-t="01:40:02">[01:40:02]</a>. The user can continue talking, and the model will continue to respond, even if the function's result is not yet available <a class="yt-timestamp" data-t="01:40:05">[01:40:05]</a>.
*   **Contextual Understanding:** This capability is crucial because, unlike traditional chat conversations, the flow of a real-time interaction cannot be arbitrarily paused. The Realtime API models were specifically trained to handle these asynchronous functions gracefully <a class="yt-timestamp" data-t="01:40:11">[01:40:11]</a>.

Additionally, the Realtime API can be influenced by specific "tricks":
*   **`stay_silent` Function:** To control the model's speaking turns, a `stay_silent` function can be provided. This allows the model to decide whether to continue speaking or wait, based on its interpretation of the user's speech, rather than relying solely on Voice Activity Detection (VAD) <a class="yt-timestamp" data-t="01:27:44">[01:27:44]</a>.
*   **XML Tag Guidance:** Although not strictly [[dynamic_vs_static_tool_calling | function calling]], the Realtime API can sometimes interpret and follow instructions embedded in XML tags within a script, allowing for specific speech patterns (e.g., pacing, tone) <a class="yt-timestamp" data-t="01:29:12">[01:29:12]</a>.

## Dynamic Tool Creation
An experimental and inherently unsafe feature demonstrated is the ability for an agent to dynamically write and use its own functions at runtime <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>. By providing a function that takes a Python string representing a function's implementation, and using `exec` (with extreme caution due to security risks), the agent can effectively "bootstrap" new capabilities <a class="yt-timestamp" data-t="01:19:40">[01:19:40]</a>. This allows for self-extending AI systems.

## Memory and State Management
Asynchronous functions are vital for managing memory and state in AI applications. A simple form of memory can be a list of past interactions, but for more sophisticated use cases:
*   **Storing Memory:** Functions can be used to add information to memory <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. This memory can be persisted (e.g., in a local JSON file) and loaded at the beginning of a session <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.
*   **Retrieval Augmented Generation (RAG):** Instead of loading all memory, more advanced systems can perform "smart querying" using retrieval techniques (like semantic similarity or search) to load only the most relevant memories for the current context <a class="yt-timestamp" data-t="03:09:00">[03:09:00]</a>.
*   **Consistency:** To enforce consistency in stored memories, one approach is to perform a retrieval for similar memories before storing a new one and then explicitly check for contradictions or updates using the model. Timestamps and explicit "chains of updates" can help manage evolving information <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

## Multi-Agent Systems and Routing
For applications involving dozens or hundreds of functions, [[dynamic_vs_static_tool_calling | multi-agent patterns]] become crucial for efficient function calling and routing <a class="yt-timestamp" data-t="01:07:53">[01:07:53]</a>.
*   **Responsibility Split:** Functions can be grouped and assigned to different agents, each specializing in a set of related tasks (e.g., an "email agent" with email functions, a "calendar agent" with calendar functions) <a class="yt-timestamp" data-t="01:11:16">[01:11:16]</a>.
*   **Handoffs:** A primary "triage agent" can then use "transfer functions" to hand off the conversation and context to the appropriate specialized agent <a class="yt-timestamp" data-t="01:13:01">[01:13:01]</a>. This can create a seamless experience where the initial agent routes the request, and the specialized agent immediately performs the action <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>.
*   **Dynamic Function Loading:** Alternatively, functions can be dynamically loaded into memory or context based on the user's input or the ongoing conversation, potentially using embeddings or a two-step function call process <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>.

While there are no hard limits on the number of functions a model can handle in one iteration, a general rule of thumb for reliable performance without extensive prompting is around 10-20 functions <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>. Fine-tuning can extend this significantly, with successful cases reported for over 100 functions <a class="yt-timestamp" data-t="01:16:36">[01:16:36]</a>.