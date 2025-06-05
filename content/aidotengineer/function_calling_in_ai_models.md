---
title: Function calling in AI models
videoId: KUEmEb71vzQ
---

From: [[aidotengineer]] <br/> 

Function calling is a core concept in AI and language models, enabling them to interact with external systems and perform actions beyond text generation <a class="yt-timestamp" data-t="00:19:19">[00:19:19]</a>. It allows models to fetch data, take action, manage application state, and execute workflow actions <a class="yt-timestamp" data-t="01:09:55">[01:09:55]</a>.

## Historical Evolution of Function Calling
The evolution of patterns and abstractions with language models includes:
*   **Text Completion** Initially, models like the original GPT, GPT-2, and GPT-3 were base models that would continue an input text <a class="yt-timestamp" data-t="01:52:03">[01:52:03]</a>. Getting these models to follow instructions was challenging <a class="yt-timestamp" data-t="02:12:31">[02:12:31]</a>.
*   **Instruction Following** OpenAI introduced instruction following with InstructGPT, allowing models to perform specific tasks as requested <a class="yt-timestamp" data-t="02:52:16">[02:52:16]</a>.
*   **Roles (Users/Assistants)** The notion of users, assistants, and roles was introduced through post-training, giving models distinct personas <a class="yt-timestamp" data-t="03:02:40">[03:02:40]</a>.
*   **External Tools** The ability to provide additional tools to interact with external states was finally introduced <a class="yt-timestamp" data-t="03:12:40">[03:12:40]</a>. This marked a shift from merely generating text to generating actions <a class="yt-timestamp" data-t="07:05:07">[07:05:07]</a>.

Early instances of tool use include:
*   **WebGPT** (2021) OpenAI trained a version of GPT-3 called WebGPT to use a specific set of functions for web search <a class="yt-timestamp" data-t="06:44:03">[06:44:03]</a>. This involved generating actions, parsing them, and reintroducing results into the model's context <a class="yt-timestamp" data-t="07:08:06">[07:08:06]</a>.
*   **Meta's Tool-Using Models** Meta developed a method to teach models to use *any* tools, such as calculators, QA systems, and translators, by analyzing log probabilities to determine where to insert function calls <a class="yt-timestamp" data-t="08:07:04">[08:07:04]</a>. This technique allowed models to learn tool use with minimal human-labeled examples <a class="yt-timestamp" data-t="09:00:16">[09:00:16]</a>.
*   **General Function Calling** In June 2023, OpenAI launched general function calling, where models are post-trained to use tools by understanding a specific syntax <a class="yt-timestamp" data-t="09:22:56">[09:22:56]</a>.

Fundamentally, functions are considered powerful enough for most modern AI applications <a class="yt-timestamp" data-t="09:59:58">[09:59:58]</a>. This aligns with the [[importance_of_tool_calling_in_ai | importance of tool calling in AI]].

## How Function Calling Works: A Crash Course
Function calling primarily serves two purposes:
1.  **Fetching Data:** Reading APIs, retrieval, memory <a class="yt-timestamp" data-t="01:27:14">[01:27:14]</a>.
2.  **Taking Action:** Writing to APIs, managing application state (UI, front end, back end), and workflow actions <a class="yt-timestamp" data-t="01:29:16">[01:29:16]</a>.

The process of [[implementing_function_calling_and_agents_in_ai | implementing function calling in AI]] involves several steps:
1.  **Define Functions**: Inform the model about available functions and their schemas <a class="yt-timestamp" data-t="01:17:46">[01:17:46]</a>.
2.  **User Input**: Provide the user's input to the model <a class="yt-timestamp" data-t="01:19:10">[01:19:10]</a>.
3.  **Model Intent**: The model indicates its intent to call a specific function with arguments <a class="yt-timestamp" data-t="01:19:10">[01:19:10]</a>.
4.  **Execution (Developer Responsibility)**: The model *does not* execute the function itself. The developer is responsible for parsing the model's intent, executing the actual code, and handling the results <a class="yt-timestamp" data-t="01:19:54">[01:19:54]</a>.
5.  **Provide Result**: The result of the function execution is provided back to the model, which can then use it in its subsequent generation <a class="yt-timestamp" data-t="01:29:16">[01:29:16]</a>.

## Best Practices for Function Calling
Based on documentation, several best practices for [[developing_custom_ai_tools_and_functions | developing custom AI tools and functions]] are recommended:
*   **Clear Functions**: Write clear function descriptions and explain the purpose of each parameter <a class="yt-timestamp" data-t="01:51:30">[01:51:30]</a>.
*   **System Prompt & Examples**: Use a system prompt and include examples for better model understanding <a class="yt-timestamp" data-t="02:20:16">[02:20:16]</a>.
*   **Software Engineering Principles**: Apply good software engineering practices to make functions intuitive and follow the "function of least principle" <a class="yt-timestamp" data-t="02:27:26">[02:27:26]</a>.
*   **Enums and Object Structure**: Use enums and object structures to prevent the model from making invalid calls or representing invalid states <a class="yt-timestamp" data-t="02:49:15">[02:49:15]</a>.

## Applications of Function Calling

### Agents and Loops
At its simplest, an agent is a loop <a class="yt-timestamp" data-t="02:20:20">[02:20:20]</a>. This concept is foundational to [[agent_continuations_for_ai_workflows | agent continuations for AI workflows]]. The loop involves:
1.  Specifying tools to the model <a class="yt-timestamp" data-t="02:26:07">[02:26:07]</a>.
2.  Calling the model to get a message <a class="yt-timestamp" data-t="02:26:07">[02:26:07]</a>.
3.  Printing the message <a class="yt-timestamp" data-t="02:26:07">[02:26:07]</a>.
4.  Handling any tool calls <a class="yt-timestamp" data-t="02:26:07">[02:26:07]</a>.
5.  Appending the tool results <a class="yt-timestamp" data-t="02:26:07">[02:26:07]</a>.
6.  Breaking the loop when no more tool calls are needed <a class="yt-timestamp" data-t="02:26:07">[02:26:07]</a>.

### Memory
A basic form of memory can be implemented using a simple list <a class="yt-timestamp" data-t="02:27:26">[02:27:26]</a>. For example, functions `add_to_memory` and `get_memory` can be defined <a class="yt-timestamp" data-t="02:27:26">[02:27:26]</a>. To persist memory, it can be stored in a local JSON file, read at the beginning, and written out after each turn <a class="yt-timestamp" data-t="02:52:16">[02:52:16]</a>. This allows the model to recall previous interactions across sessions <a class="yt-timestamp" data-t="03:00:54">[03:00:54]</a>.

To enforce consistency or handle contradictions in stored memories, one approach is to:
*   Perform a retrieval (search) for semantically similar memories before storing new ones <a class="yt-timestamp" data-t="01:32:11">[01:32:11]</a>.
*   Use a model to explicitly check if a new memory updates or contradicts an existing one <a class="yt-timestamp" data-t="01:32:11">[01:32:11]</a>.
*   Represent updates as a chain of nodes, allowing the system to surface only the latest information or the entire history <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.

### Delegation
Function calling enables [[using_reasoning_models_and_tool_calls_in_ai | delegation of tasks]] to different models or agents. Forms of delegation include:
*   **Handoffs**: Transferring a conversation entirely to a different agent by replacing the system prompt and tools <a class="yt-timestamp" data-t="03:27:32">[03:27:32]</a>.
*   **Nested Calls**: An agent can call another function that, in turn, makes an API request to a "smarter model" for a harder task <a class="yt-timestamp" data-t="03:39:57">[03:39:57]</a>.
*   **Manager Tasks**: More asynchronous delegation, where a manager agent oversees tasks <a class="yt-timestamp" data-t="03:45:57">[03:45:57]</a>.

### Asynchronous Operations
Handling tasks asynchronously is crucial for maintaining a responsive user experience. While Python is single-threaded, `asyncio` can be used to manage non-blocking operations like network calls in parallel <a class="yt-timestamp" data-t="04:36:37">[04:36:37]</a>.

The general approach for asynchronous function calls:
1.  Define a `create_task` function that initiates a task (e.g., an API call) and returns a unique task ID <a class="yt-timestamp" data-t="04:47:04">[04:47:04]</a>.
2.  The model can then continue the conversation while the task runs in the background.
3.  A `check_tasks` function can be used to query the status of pending tasks and retrieve results once they are completed <a class="yt-timestamp" data-t="04:47:04">[04:47:04]</a>.

In the real-time API, asynchronous functions are supported natively. The model can call a function, receive no immediate response, and the conversation can continue until the function's result is available <a class="yt-timestamp" data-t="01:39:55">[01:39:55]</a>.

### Self-Modifying/Self-Bootstrapping Agents
A powerful application of function calling is enabling an agent to write and use its own tools during runtime. This can be achieved by having the model generate Python code for a new function, which is then dynamically evaluated (`exec`) and added to the agent's available tools <a class="yt-timestamp" data-t="01:21:31">[01:21:31]</a>. This concept aligns with [[custom_model_building_and_code_evaluation_for_ai_systems | custom model building and code evaluation]].
<br>
> [!caution] Security Warning
> Using `exec` or `eval` with arbitrary model-generated code is highly dangerous and should be avoided in production environments due to severe security risks <a class="yt-timestamp" data-t="01:26:37">[01:26:37]</a>.

### Routing and Multi-Agent Patterns
When dealing with dozens or hundreds of functions, effective tool calling can be achieved through [[implementing_function_calling_and_agents_in_ai | multi-agent patterns]] and routing:
*   **Multiple Agents**: Split responsibilities by having multiple agents, each with a specific grouping of functions <a class="yt-timestamp" data-t="01:07:53">[01:07:53]</a>.
*   **Triage Agent**: A primary "triage" agent can decide which specialized agent (e.g., an "email agent" or "calendar agent") to hand off the conversation to <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **Dynamic Function Loading**: Based on user input or conversation context, dynamically load the most likely relevant functions into memory or context. This can involve embeddings or a two-step function call process <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>.
*   **Fine-tuning**: For specific, latency-sensitive cases, models can be fine-tuned with hundreds of functions <a class="yt-timestamp" data-t="01:16:36">[01:16:36]</a>. However, a general rule of thumb suggests models perform well with 10-20 tools without extensive prompting <a class="yt-timestamp" data-t="01:16:20">[01:16:20]</a>.

### Real-time API Tricks
Function calling can also enhance real-time interactions, although these are not strictly function calls in the API:
*   **"Stay Silent" Function**: In real-time voice interactions, a model can use a "stay silent" function to decide if the user is truly done talking, preventing it from cutting off the user prematurely <a class="yt-timestamp" data-t="01:27:44">[01:27:44]</a>. This provides a more intelligent voice activity detection than simple triggers <a class="yt-timestamp" data-t="01:27:44">[01:27:44]</a>.
*   **XML Tag Guidance**: Models can be prompted to follow specific speaking styles or scripts using XML tags, even if they were not explicitly trained for it. This behavior is an emergent property of language understanding <a class="yt-timestamp" data-t="01:29:12">[01:29:12]</a>.

## Testing and Evaluation
The process of [[testing_and_evaluation_of_ai_models | testing and evaluation of AI models]] for function calling often involves live coding, debugging, and iterative refinement. Simple print statements can be used to observe the model's function calls and responses <a class="yt-timestamp" data-t="01:17:04">[01:17:04]</a>.