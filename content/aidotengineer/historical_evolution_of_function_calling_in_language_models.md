---
title: Historical evolution of function calling in language models
videoId: KUEmEb71vzQ
---

From: [[aidotengineer]] <br/> 

[[function_calling_in_ai_models | Function calling]] is presented as a fundamental concept in AI and [[large_language_models_in_code_generation | language models]], enabling them to interact with external states and perform a wide range of actions beyond mere text generation <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. This concept is considered powerful enough to underpin much of the exciting developments in current AI <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.

## Early Language Models and Instruction Following Challenges

Initially, [[large_language_models_in_code_generation | language models]] like the original GPT, GPT-2, and GPT-3 operated primarily as text completion models <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Users provided input text, and the models would continue the sentence <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>. While innovative for generating natural-sounding language, getting these models to follow specific instructions proved difficult <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>. For example, a request like "What is the best way to get to the park?" might result in a continuation like "that is what Sally said yesterday," rather than a direct answer <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. To achieve instruction following, developers had to use "few-shot" prompting, structuring inputs with "question-answer" pairs <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Emergence of Instruction Following and Roles

A significant step forward was the introduction of InstructGPT, which enabled [[large_language_models_in_code_generation | language models]] to follow instructions directly <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. This was achieved through post-training, allowing models to understand and perform requested tasks <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Subsequently, the notion of "users" and "assistants" with distinct roles was introduced, also through post-training, to provide models with specific personas <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

## Early Implementations of Tooling

The concept of giving [[large_language_models_in_code_generation | language models]] additional tools to interact with external states marked a crucial point in their evolution <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

*   **WebGPT (2021)**: One of the first instances of [[function_calling_in_ai_models | function calling]] involved WebGPT, a version of GPT-3 trained to use a specific set of functions for web search <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This model generated actions (like search queries) which were then parsed, executed, and their results fed back into the model's context for further processing <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. Training involved human users completing tasks using commands, allowing the model to imitate user behavior and produce preferred responses <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This approach, however, was specific to pre-defined tools <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

*   **Meta's Approach (Any Tools)**: Meta developed a method to teach models how to use *any* tool, demonstrated with functions like QA, calculator, and translation <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. This clever technique involved analyzing log-probabilities to determine optimal points to insert function calls, which would reduce the perplexity of the generated sentence <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. This method required minimal human-labeled examples <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## General Function Calling (OpenAI, June 2023)

In June 2023, OpenAI launched general [[function_calling_in_ai_models | function calling]], where models were post-trained to inherently use tools <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. This eliminated the need for extensive example-giving, as models could now call functions based on a given syntax <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

## Core Concepts and Workflow

[[function_calling_in_ai_models | Function calling]] serves two primary purposes:
1.  **Fetching Data**: Reading APIs, retrieval, memory <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
2.  **Taking Action**: Writing to APIs, managing application state (UI, backend), and workflow actions (multi-step processes, meta-actions like changing prompts or handing off conversations) <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

The workflow involves:
1.  Defining the functions the model can use <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
2.  Providing user input <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>.
3.  The model *suggesting* a function call based on intent; it does not execute the function itself <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>.
4.  The developer is responsible for parsing the suggested call, executing the corresponding code, and providing the result back to the model <a class="yt-timestamp" data-t="00:11:24">[00:11:24]</a>.
5.  The model then uses this result to continue its generation <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

### Best Practices for Function Definition
*   Write clear descriptions for functions and parameters <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   Apply software engineering best practices, ensuring functions are intuitive and follow the principle of least privilege <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   Use enums and object structures to prevent the model from making invalid calls or representing invalid states <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

### Functions vs. Tools
In OpenAI's adopted definition, "functions" refer to the raw function calling mechanism where developers provide an interface and are responsible for execution <a class="yt-timestamp" data-t="01:14:06">[01:14:06]</a>. "Tools" are a superset of functions, encompassing functions as well as hosted solutions like code interpreters or file search <a class="yt-timestamp" data-t="01:14:16">[01:14:16]</a>.

## Advanced Use Cases and Implementation Patterns

The core mechanism of [[function_calling_in_ai_models | function calling]] enables complex behaviors:

*   **Agents as Loops**: [[implementing_function_calling_and_agents_in_ai | AI agents]] are fundamentally loops where the model continuously specifies tools, makes calls, processes results, and appends them to the conversation history until no more tool calls are needed <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>.
*   **Memory**: Simple memory can be implemented by storing information in a list or by reading/writing to a local JSON file via functions <a class="yt-timestamp" data-t="00:26:27">[00:26:27]</a>. More advanced memory systems can employ smart querying, retrieval augmented generation (RAG), or semantic similarity to load relevant memories <a class="yt-timestamp" data-t="00:32:04">[00:32:04]</a>. Consistency in stored memories can be managed by performing retrieval before storing, checking for semantic similarities, and using a model to identify and resolve contradictions or updates <a class="yt-timestamp" data-t="01:32:04">[01:32:04]</a>.
*   **Delegation**: Models can delegate tasks using:
    *   **Handoffs**: Transferring a conversation entirely to a different agent by replacing the system prompt and tools <a class="yt-timestamp" data-t="00:34:27">[00:34:27]</a>. This is useful for routing to specialized agents with specific function sets <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a>.
    *   **Nested Calls**: One function calling another, often overlooked but straightforward to implement <a class="yt-timestamp" data-t="00:34:37">[00:34:37]</a>.
    *   **Manager Tasks**: Delegating a complex task to a "smarter" model (e.g., GPT-4) via an API call within a function <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.
*   **Asynchronous Operations**: For long-running tasks like network calls, [[implementing_function_calling_and_agents_in_ai | agents]] can initiate tasks asynchronously and continue interacting with the user while the task runs in the background <a class="yt-timestamp" data-t="00:40:05">[00:40:05]</a>. This involves using `asyncio` to create non-blocking operations and a mechanism to check on task progress <a class="yt-timestamp" data-t="00:52:53">[00:52:53]</a>. The Real-time API inherently supports asynchronous functions, allowing models to call functions and continue the conversation without waiting for an immediate response <a class="yt-timestamp" data-t="01:39:55">[01:39:55]</a>.
*   **Self-Modifying/Self-Bootstrapping Agents**: By combining [[function_calling_in_ai_models | function calling]] with the ability to execute generated code, an agent can dynamically create and add new functions to its own toolset <a class="yt-timestamp" data-t="01:17:16">[01:17:16]</a>. This allows for runtime adaptation and expansion of capabilities, such as generating a calculator function on the fly <a class="yt-timestamp" data-t="01:25:54">[01:25:54]</a>.

## Challenges and Considerations

*   **Scaling Functions**: When dealing with dozens or hundreds of functions, strategies include:
    *   Using multiple agents, each with a specialized set of functions, and employing a triage mechanism to hand off conversations to the appropriate agent <a class="yt-timestamp" data-t="01:07:53">[01:07:53]</a>.
    *   Fine-tuning smaller models with a large number of functions <a class="yt-timestamp" data-t="01:08:30">[01:08:30]</a>.
    *   Dynamic function loading, where only the most relevant functions are loaded into context based on input or conversation <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>.
    *   A general rule of thumb suggests that models perform reliably with around 10-20 functions without extensive prompting, though fine-tuning can extend this significantly <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>.
*   **Function Calls within Thought Text**: For current OpenAI API models, [[function_calling_in_ai_models | function calls]] typically occur at the very end of the generation, and the internal "thought process" is not exposed <a class="yt-timestamp" data-t="01:09:36">[01:09:36]</a>.
*   **Real-time API Tricks**: [[current_and_future_trends_in_large_language_models | Real-time API]] models can be guided to exhibit specific behaviors by describing a "stay silent" function to control when the model waits for user input <a class="yt-timestamp" data-t="01:27:44">[01:27:44]</a>. They can also be instructed to read text according to XML tags, even without explicit training for this behavior, as an unintended consequence of their general language understanding <a class="yt-timestamp" data-t="01:29:12">[01:29:12]</a>.