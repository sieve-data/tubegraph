---
title: Memory management and delegation in AI
videoId: KUEmEb71vzQ
---

From: [[aidotengineer]] <br/> 

This article explores fundamental concepts in AI agent development, focusing on [[Function calling in AI | function calling]], [[Stateful Agents and AI Memory Management | memory management]], and [[Dynamic planning and execution in AI | delegation]] through asynchronous operations. The discussion is led by Elan from the OpenAI developer experience team, highlighting practical implementations and best practices.

## A Brief History of Function Calling

The evolution of language models and their abstractions began with text completion, where models like the original GPT, GPT2, and GPT3 would continue sentences based on input text [01:52:00]. Getting these models to follow specific instructions was initially challenging, often requiring structured prompts like "question, answer, question, answer" for few-shot learning [02:42:43].

Instruction following was later introduced with InstructGPT, allowing models to directly perform requested actions rather than just completing text [02:52:00]. This progressed to the introduction of user and assistant roles through post-training, where models gained specific personas [03:02:00].

The notion of giving models additional tools to interact with external states emerged later [03:14:00]. Early examples include:
*   **WebGPT (2021)**: A version of GPT3 trained by OpenAI to use a specific set of functions for web search, demonstrating the generation of actions rather than just text [03:38:00]. The model learned to imitate user behavior and produce preferred responses by observing task completion using commands [07:35:00].
*   **Meta's tool-use paper**: This work focused on teaching models to use *any* tools, such as calculators or translation services, by analyzing log probabilities to retroactively insert function calls [08:05:00].
*   **OpenAI's General Function Calling (June 2023)**: This capability was launched with models pre-trained or post-trained to understand and use a standardized function syntax, allowing them to call functions directly without extensive examples [09:23:00].

## Function Calling Crash Course

[[Function calling in AI | Function calling]] serves two main purposes:
1.  **Fetching data**: This includes reading APIs, retrieval, or accessing [[Stateful Agents and AI Memory Management | memory]] [01:27:00].
2.  **Taking action**: This involves writing to APIs, managing application state (like UI, frontend, backend), or executing workflow actions (multi-step processes, meta-actions like switching prompts, loading tools, or handing off conversations) [01:28:00].

When a model is provided with functions it can use and user input, it determines *what* function it wants to call and its arguments, but it does not *execute* the function itself [01:11:00]. The developer is responsible for parsing the model's intent, executing the corresponding code, and providing the result back to the model for further generation [01:24:00].

### Best Practices for Function Calling

*   **Write clear functions**: Explain the purpose of each parameter, use a system prompt, and include examples [01:18:00].
*   **Apply software engineering best practices**:
    *   Functions should be intuitive and follow the "function of least principle" [01:31:00]. If a human struggles to use it, the model likely will too [01:36:00].
    *   Use enums and object structures to prevent the model from making invalid calls or representing invalid states [01:48:00].

### Functions vs. Tools

While often used interchangeably, "functions" refer to the raw function calling interface where the developer executes the code [01:40:00]. "Tools" are a superset of functions that also include hosted solutions like code interpreters or file search [01:18:00].

## Agents are Loops

At its core, an AI agent operates as a loop [01:20:20]. The basic structure involves:
1.  Specifying the available tools to the model [01:25:00].
2.  Calling the model with the current messages [01:26:00].
3.  Getting the message and printing it [01:29:00].
4.  Handling any tool calls that the model indicates [01:30:00].
5.  Appending the results back to the message history [01:31:00].
6.  Breaking the loop when there are no more tool calls [01:37:00].

This loop allows the model to process information, decide on actions, and integrate the results into its ongoing conversation or task [01:39:00].

### [[Stateful Agents and AI Memory Management | Memory Management]]

A very basic form of [[Stateful Agents and AI Memory Management | memory]] can be implemented using a simple Python list [02:26:00]. The concept aims to simplify complexity often added to such components [02:44:00].

**Implementation Example:**
*   A `memory` list to store information.
*   An `add_to_memory` function to append factual information from the user (e.g., about themselves or their preferences) [02:28:00].
*   A `get_memory` function to retrieve stored information [02:26:00].
*   Memory can be persisted by writing it to a local JSON file at the end of a session and reading it in at the beginning [02:49:00]. This allows the agent to recall information across sessions [03:31:00].

**Advanced Memory Concepts:**
*   **Smart Querying / Retrieval-Augmented Generation (RAG)**: Instead of loading all memory, use semantic similarity or search to retrieve only the most relevant memories for a given query [03:12:00].
*   **Consistency Enforcement**: To ensure consistency in stored memories, one approach is to perform a retrieval for similar memories before storing a new one [01:32:11]. The model can then explicitly check if the new memory updates or contradicts existing ones [01:32:21]. This can involve tracking timestamps or creating direct "nodes" linking updated memories to their previous versions, allowing for either the latest information or the full history to be presented [01:32:52].

### [[Dynamic planning and execution in AI | Delegation]] and [[Efficiency and smart execution engines in AI applications | Asynchrony]]

[[Dynamic planning and execution in AI | Delegation]] involves an agent handing off tasks or leveraging other models/functions for specific operations.

**Forms of Delegation:**
*   **Handoffs**: Taking a conversation and fully swapping it to a different agent, which involves replacing the system prompt and tools [03:27:00].
*   **Nested calls**: Functions calling other functions, often the easiest to implement [03:39:00].
*   **Manager tasks**: More complex [[Efficiency and smart execution engines in AI applications | asynchronous]] delegation where a manager agent oversees tasks [03:43:00].

**Implementing Basic Delegation:**
An agent can be equipped with a function (e.g., `delegate_to_smarter_model`) that makes a direct API request to a more powerful model (e.g., `gpt-4`) for difficult tasks [03:52:00]. The agent's function description can guide it to use this delegation when appropriate (e.g., "if the user asks something difficult") [03:35:00].

**Asynchronous Execution:**
When a model delegates a task, it shouldn't have to wait idly for the result [03:49:00]. [[Efficiency and smart execution engines in AI applications | Asynchronous]] programming allows the system to continue processing user input or other tasks while a delegated task runs in the background [03:53:00].

*   **Non-blocking operations**: Using `asyncio.sleep` (or similar for API calls) allows the program to yield control and perform other operations instead of blocking the entire process [05:20:00].
*   **Parallel execution**: Multiple function calls (e.g., getting weather for five cities) can be executed in parallel using `asyncio.gather` for network calls, significantly reducing total waiting time compared to sequential execution [05:22:00].
*   **Task Management**:
    *   **Creating tasks**: A function can generate a unique task ID, assign the delegated operation (e.g., calling another model) to that ID, and immediately return a "response pending" status with the task ID [05:40:00].
    *   **Checking tasks**: Another function allows the agent to query the status of a task using its ID, retrieving the result once it's complete [05:30:00].
    *   This pattern creates a system where the agent can initiate background tasks, continue interacting with the user, and check on task progress at will [05:58:00].

### Router Patterns (Multi-Agent Handoffs)

For scenarios with dozens or hundreds of functions, a [[Best practices for building AI agents | router pattern]] helps the model efficiently select the right tool [01:07:57].

*   **Multiple Agents**: Define multiple agents, each responsible for a specific grouping of related functions (e.g., an "email functions agent" with `send_email` and `check_email`, and a "calendar agent" with `create_event`) [01:11:00].
*   **Triage Agent**: A primary agent acts as a "triage" or routing agent. This agent is given "transfer" functions (e.g., `transfer_to_email_agent`) that direct the conversation to the appropriate specialized agent [01:13:00].
*   **Seamless Handoff**: The triage agent can immediately transfer control to the relevant agent, potentially even inferring and calling the correct function directly if the user's intent is clear from the initial prompt [01:45:00]. This creates a fast, multi-hop interaction that feels like an immediate response to the user [01:15:10].
*   **Scalability**: This pattern helps manage large numbers of functions by breaking them into manageable, specialized groups [01:08:00]. While fine-tuning smaller models with hundreds of functions is possible, a more reliable approach for large tool libraries is often to use multi-agent routing [01:08:00].

## Generated Code Agents

A particularly interesting application is an agent that can write its own functions during a conversation [01:17:09].

*   **Dynamic Function Creation**: The agent defines a function (e.g., `add_tool`) that takes a Python string representing a function's implementation. Using `exec` (with security caveats), this string can be evaluated and added to the agent's available tools [01:19:00].
*   **Self-Modification**: The agent can then call these newly created functions directly. For example, it could write a simple "hello" function or even a calculator function on the fly and then use it immediately within the same conversation [02:26:00].
*   **Safety Concerns**: This approach is inherently dangerous due to the use of `exec` and should not be used in production environments without strict sandboxing and security measures [02:36:00].

## Real-time API Tricks

Beyond standard chat interactions, function calling can be applied to real-time scenarios like voice assistants.

*   **"Stay Silent" Function**: To prevent a real-time API from cutting off a user who pauses mid-sentence, a `stay_silent` function can be used [02:27:00]. When the model detects a potential pause (e.g., via Voice Activity Detection), it can call this function to verify if the user is truly done talking, allowing for more natural interruptions and pauses [02:44:00].
*   **Script Following with XML Tags**: Although not strictly function calling, models can be prompted to follow a specific script by providing XML tags [02:12:00]. For instance, providing a script with `<s>` and `<e>` tags for start and end, along with descriptions for various voice effects, can lead to the model delivering the script with surprising fidelity to the instructions [02:29:00]. This leverages the model's understanding of structured data to influence its output delivery style [02:35:00].

## Q&A Highlights

*   **Generator for Nested Calls**: It is possible to implement agents as Python generators, yielding results at each step (e.g., each function call) to surface progress and handle events from multiple agents [03:52:00].
*   **AI Project Design Patterns**: While many frameworks exist (e.g., Swarm, Pydantic AI), implementing a custom agent loop can be lightweight and provide granular control, especially for simple projects [06:07:00].
*   **Tool Library Size**: A general rule of thumb for effective tool performance without extensive prompting is typically 10 to 20 functions [01:16:17]. However, with fine-tuning, models like GPT-3.5 have been shown to work well with over 100 functions in latency-sensitive applications [01:16:27]. For larger numbers, consider splitting functionality across multiple agents or dynamically loading relevant functions [01:08:00].
*   **Function Calls in Vision Models**: Currently, OpenAI's API does not expose a "thought" process, and function calls happen at the very end of the model's generation, not within an internal chain of thought [01:09:36].
*   **Parallel Function Calls**: There are no hard limits on the number of parallel function calls that can be requested [01:16:05].