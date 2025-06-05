---
title: Function calling in AI
videoId: KUEmEb71vzQ
---

From: [[aidotengineer]] <br/> 

Function calling is a core concept in [[AI integration and tool calling | AI and language models]], allowing models to interact with external systems and perform actions <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. It enables language models to generate structured data that can be used to invoke functions, fetch information, or trigger specific actions <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## A Brief History of Function Calling

The evolution of language models and their ability to perform actions has progressed through several stages:
*   **Text Completion** Initially, models like GPT, GPT2, and GPT3 were "base models" that would simply continue input text <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>. Getting them to follow specific instructions was challenging <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>.
*   **Instruction Following** With InstructGPT, models were introduced that could actually perform actions based on given input, rather than just completing sentences <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>.
*   **Roles and Personas** The introduction of "users," "assistants," and distinct "roles" through post-training allowed models to gain specific personas <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>.
*   **External Tool Interaction** Eventually, the notion of providing models with additional [[Tool Usage and Development in AI Frameworks | tools]] to interact with external states emerged <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

Early implementations of function calling include:
*   **WebGPT (2021)**: This version of GPT3 was specifically trained to use a defined set of functions for web search, enabling it to generate actions rather than just text <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>. The model learned to imitate user behavior and produce preferred responses by observing users perform searches <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.
*   **Meta's Any-Tool Approach**: Meta developed a method to teach models to use *any* [[Tool Usage and Development in AI Frameworks | tools]], such as calculators or translation services, by analyzing log probabilities to retroactively insert function calls <a class="yt-timestamp" data-t="08:07:00">[08:07:00]</a>. This approach required minimal human-labeled examples <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>.
*   **OpenAI's General Function Calling (June 2023)**: OpenAI launched a generalized function calling capability, where models are pre-trained (or post-trained) to use [[Tool Usage and Development in AI Frameworks | tools]] based on a defined syntax, removing the need for extensive example-giving by developers <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>.

The speaker argues that function calling is fundamental to "all the exciting stuff that's happening today" in [[AI integration and tool calling | AI]], being a "powerful" mechanism <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.

## Core Concepts of Function Calling

Function calling serves two main purposes <a class="yt-timestamp" data-t="01:22:00">[01:22:00]</a>:
1.  **Fetching Data**: This includes reading APIs, retrieval processes, and accessing memory <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>.
2.  **Taking Action**: This involves writing to APIs, managing application state (UI, frontend, backend), and executing workflow actions (multi-step processes, or meta-actions like switching prompts or handing off conversations) <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.

The process of function calling generally follows these steps <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>:
1.  You inform the model which functions it can use <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.
2.  The model communicates its *intent* to use a function and its arguments, but it does *not* execute the function itself <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
3.  You are responsible for parsing the model's intent, executing the corresponding code, and providing the result back to the model <a class="yt-timestamp" data-t="01:24:00">[01:24:00]</a>.
4.  The model then uses this result in its subsequent generation <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>.

[!NOTE]
A distinction is made between "functions" and "[[Tool Usage and Development in AI Frameworks | tools]]": "Functions" refer to the raw function calling interface where you provide an interface and are responsible for execution. "[[Tool Usage and Development in AI Frameworks | Tools]]" is a superset that includes functions, along with hosted solutions like code interpreters or file search <a class="yt-timestamp" data-t="01:36:16">[01:36:16]</a>.

## Best Practices for Function Calling

Adhering to software engineering best practices is crucial when defining functions for AI models <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>:
*   **Clear Function Descriptions**: Explain the purpose of each parameter clearly <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.
*   **Intuitive Design**: Functions should be intuitive and follow the principle of least astonishment <a class="yt-timestamp" data-t="02:31:00">[02:31:00]</a>. If a human struggles to understand it, the model likely will too <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.
*   **Structured Parameters**: Use enums and object structures to prevent the model from making invalid calls or representing invalid states <a class="yt-timestamp" data-t="02:48:00">[02:48:00]</a>.

## Function Calling in AI Agents

[[Building effective AI agents | AI agents]] are fundamentally "loops" <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. A basic agent operates by:
1.  Specifying [[Tool Usage and Development in AI Frameworks | tools]] to the model <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.
2.  Calling the model and receiving its message <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a>.
3.  Handling any tool calls suggested by the model <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.
4.  Appending the results back into the conversation history <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.
5.  Continuing this loop until no more tool calls are made <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>.

This simple loop allows agents to perform multi-step operations and interact with external systems.

## Memory Management using Function Calling

[[Memory management and delegation in AI | Memory]] can be implemented using functions, often as simply as managing a list of stored information <a class="yt-timestamp" data-t="02:27:00">[02:27:00]</a>. For instance, `add_to_memory` and `get_memory` functions can be exposed to the model <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. The description of these functions can guide the model on when to use them, e.g., when the user provides factual information about themselves <a class="yt-timestamp" data-t="02:33:00">[02:33:00]</a>.

A simple demonstration involves:
1.  Defining `add_to_memory` and `get_memory` functions.
2.  Persisting this memory to a local JSON file that is read at the beginning and written out after each interaction <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>.
3.  When the user provides personal information, the model calls `add_to_memory`.
4.  Later, when asked about that information, the model calls `get_memory` to retrieve it <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

More advanced [[Memory management and delegation in AI | memory]] systems can involve:
*   **Smart Querying**: Instead of loading all memory, use techniques like semantic similarity or search (e.g., embeddings) to retrieve only relevant pieces <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>.
*   **Consistency Enforcement**: When storing new memory, perform a retrieval to find similar memories and use the model to explicitly check for updates or contradictions <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. Timestamps can also help in managing conflicting information <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>.

## Delegation and Asynchrony

[[Memory management and delegation in AI | Delegation]] in [[Building effective AI agents | AI agents]] involves tasks being passed to other models or processes <a class="yt-timestamp" data-t="03:05:00">[03:05:00]</a>. Forms of delegation include <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>:
*   **Handoffs**: Transferring a conversation entirely to a different agent, often by replacing the system prompt and [[Tool Usage and Development in AI Frameworks | tools]] <a class="yt-timestamp" data-t="03:27:00">[03:27:00]</a>.
*   **Nested Calls**: One function call leads to another, often the easiest to implement <a class="yt-timestamp" data-t="03:39:00">[03:39:00]</a>.
*   **Manager Tasks**: A more [[Dynamic planning and execution in AI | asynchronous]] approach where a manager agent oversees sub-tasks <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>.

[[Dynamic planning and execution in AI | Asynchronous]] function calls are crucial for improving user experience, preventing the user from waiting for long-running tasks <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>. By running tasks in parallel, the total waiting time can be significantly reduced <a class="yt-timestamp" data-t="05:35:00">[05:35:00]</a>.

To implement [[Dynamic planning and execution in AI | asynchronous]] delegation:
1.  **Separate I/O**: Separate user input handling from message processing, often using websockets or similar mechanisms <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>.
2.  **Parallel Execution**: Use `asyncio` to run multiple tool calls (e.g., network calls to other models) concurrently <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>.
3.  **Task Management**: Implement `create_task` and `check_task` functions. The model calls `create_task`, receives a task ID, and can then query the status of that task asynchronously without blocking the main conversation <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>. This allows the user to continue interacting with the model while background tasks are being processed <a class="yt-timestamp" data-t="05:58:00">[05:58:00]</a>.

## Dynamic Function Generation (Bootstrapping)

A "super unsafe" but illustrative demonstration shows an [[Building effective AI agents | AI agent]] writing and then using its own functions <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. This involves:
1.  Defining an `add_tool` function that takes a Python string representing a function's implementation.
2.  Using `exec()` (caution advised due to security risks) to evaluate the string and make the function available to the agent <a class="yt-timestamp" data-t="01:21:31">[01:21:31]</a>.
3.  The agent can then be prompted to "make yourself a little calculator" or other tools, which it generates and incorporates into its capabilities <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

## Real-time API and Function Calling

Function calling plays a significant role in real-time [[AI integration and tool calling | AI applications]], particularly with voice models:
*   **"Stay Silent" Function**: To prevent the model from interrupting too early in a real-time conversation, a "stay silent" function can be implemented <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>. The model can be prompted to call this function when the user might not be done talking, allowing for natural pauses without premature responses <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   **Structured Speech Output**: Models can be prompted to follow specific XML tags to output speech in a particular way (e.g., for pauses or tone changes), even if not explicitly trained for it. This allows for more controlled real-time audio generation <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.
*   **Native Asynchronous Functions**: Real-time APIs often natively support [[Dynamic planning and execution in AI | asynchronous]] functions, allowing the model to call a function, receive no immediate response, and continue the conversation until the function's result is ready <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. This contrasts with chat conversations where the flow can be halted.

## Addressing Advanced Use Cases

Several advanced scenarios and questions related to [[Using tools and function calls with AI SDK | function calling]] were discussed:
*   **Managing Dozens or Hundreds of Functions**:
    *   **Multi-Agent Architecture**: Divide responsibilities among multiple [[Building effective AI agents | agents]], each with a cluster of related functions <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. This creates a "glorified triage" system <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
    *   **Fine-tuning**: For specific and latency-sensitive cases, fine-tuning smaller models with a large number of functions (e.g., 120 functions with GPT 3.5) can be effective <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>.
    *   **Dynamic Function Loading**: Based on input or conversation, load only the most relevant functions into context, potentially using embeddings or a two-step function call approach <a class="yt-timestamp" data-t="01:51:00">[01:51:00]</a>.
*   **Router Patterns**: Implementing router patterns can involve having a "triage" agent that decides which specialized agent (e.g., email agent, calendar agent) should handle the user's request, effectively routing the conversation and potentially performing a handoff <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Generators for Nested Calls**: It is possible and often the "right way" to implement [[Building effective AI agents | agents]] as generators to yield results at each step, allowing for better tracking of progress and events from multiple concurrent agents <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.
*   **Tool Call Limits**: There are generally no hard limits on the number of functions or parallel function calls, but practical performance often limits effective tool libraries to 10-20 functions without extensive fine-tuning or complex routing <a class="yt-timestamp" data-t="01:05:00">[01:05:00]</a>.
*   **Vision Models and Tools**: For vision models, function calls currently occur at the very end of the model's processing and are not exposed within its internal "thought" process or chain of thought <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>.

## Conclusion

The speaker emphasizes that function calling is a remarkably powerful and versatile mechanism within [[Importance of tool calling for AI agents | AI agent development]], capable of handling complex scenarios like [[Memory management and delegation in AI | memory]], [[Memory management and delegation in AI | delegation]], and [[Dynamic planning and execution in AI | asynchronous]] operations with relatively simple, first-principles implementations <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. While frameworks exist to abstract some complexity, granular control can often be achieved with minimal lines of code <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. The ability for an [[Building effective AI agents | AI]] to even write and integrate its own [[Tool Usage and Development in AI Frameworks | tools]] highlights the profound impact of [[Using tools and function calls with AI SDK | function calling]] on [[Buzzwords in AI | AI capabilities]] <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.