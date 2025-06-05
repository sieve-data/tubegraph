---
title: History of function calling in language models
videoId: KUEmEb71vzQ
---

From: [[aidotengineer]] <br/> 

[[function_calling_in_ai | Function calling]] in [[large_language_model_interpretability | large language models]] has evolved significantly, moving from simple text completion to enabling complex interactions with external systems and advanced agentic behaviors <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. This capability allows models to generate structured data that represents actions, which can then be parsed and executed by external code <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.

## Early Language Models: Text Completion <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>
The earliest generations of [[using_language_models_to_generate_text | language models]], such as the original GPT, GPT-2, and GPT-3, were primarily "base models" designed for text completion <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. Users would provide an input text, and the model would simply continue the sentence <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. While impressive for generating human-like language, getting these models to follow specific instructions was challenging <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. For example, setting up a chatbot was non-trivial, often requiring "few-shot" prompting where users provided examples of questions and answers to guide the model <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## Evolution to Instruction Following and Roles
*   **InstructGPT**: OpenAI introduced "instruction following" with InstructGPT, allowing models to directly perform what users asked, rather than just completing text <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   **User and Assistant Roles**: Later, the concept of distinct "user" and "assistant" roles was introduced, primarily through post-training, giving models specific personas in a conversation <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

## Early Integration of External Tools
The ability to interact with external states via additional tools was a significant leap <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
*   **WebGPT (2021)**: One of the first instances of [[function_calling_in_ai | function calling]] in OpenAI was through WebGPT, a version of GPT-3 trained to use a specific set of functions for web search <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. This marked a shift from merely generating text to generating *actions* that were then parsed and re-introduced into the model's context <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>. WebGPT was trained by allowing users to complete tasks using commands in an interface, teaching the model to imitate user behavior and produce preferred responses <a class="yt-timestamp" data-t="07:21:00">[07:21:00]</a>. However, this approach was very specific to the tools it was trained on <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>.

*   **Meta's Toolformer (Undated, post-WebGPT)**: Meta (then Facebook) introduced a method to teach models how to use *any* tools <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. Their "Toolformer" paper used a clever technique involving log-probabilities to determine where a [[function_calling_in_ai | function call]] would best reduce the perplexity of a sentence, thereby improving the model's ability to integrate tool usage effectively <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>. This approach required minimal human-labeled examples <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

## General Function Calling by OpenAI (June 2023)
In June 2023, OpenAI launched general [[function_calling_in_ai | function calling]] <a class="yt-timestamp" data-t="09:23:00">[09:23:00]</a>. The models were post-trained to use tools, meaning developers no longer needed to provide many examples; the models could call functions based on a defined syntax <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>. This generalized capability made [[function_calling_in_ai | function calling]] a powerful foundation for various AI applications <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.

## Modern Concepts and Practical Applications
Today, [[function_calling_in_ai | function calling]] serves two main purposes: fetching data (e.g., reading APIs, retrieval, memory) and taking action (e.g., writing via APIs, managing application state, workflow actions) <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>.

### Function vs. Tool
Within OpenAI's API, "functions" are the raw [[function_calling_in_ai | function calling]] interfaces provided by the user, where the user is responsible for executing the code <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>. "Tools" are a superset of functions, encompassing functions as well as hosted solutions like code interpreters or file search <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.

### Agents and Loops
Modern AI agents are often conceptualized as "loops" where the model iteratively calls functions, processes results, and continues the conversation or task <a class="yt-timestamp" data-t="20:20:00">[20:20:00]</a>. This includes complex behaviors like:
*   **Memory**: Implementing basic memory can be as simple as functions to add and retrieve text from a list, which can then be persisted (e.g., to a JSON file) <a class="yt-timestamp" data-t="26:27:00">[26:27:00]</a>. More advanced memory systems might involve [[large_language_model_interpretability | semantic similarity]] and retrieval <a class="yt-timestamp" data-t="32:07:00">[32:07:00]</a>.
*   **Delegation and Asynchrony**: [[integration_of_large_language_models_in_development | Agents]] can delegate tasks to other models or processes, enabling asynchronous operations <a class="yt-timestamp" data-t="34:07:00">[34:07:00]</a>. This allows the primary interaction to continue while a delegated task runs in the background, with the results being integrated once available <a class="yt-timestamp" data-t="39:53:00">[39:53:00]</a>.
*   **Routing and Handoffs**: For applications with dozens or hundreds of functions, multi-agent patterns become useful <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>. A "triage" agent can route tasks to specialized agents, each with a focused set of functions <a class="yt-timestamp" data-t="11:10:00">[11:10:00]</a>. This is often achieved through "handoffs," where the conversation context and tools are swapped to a different agent <a class="yt-timestamp" data-t="34:27:00">[34:27:00]</a>.
*   **Self-Modifying Agents**: Advanced applications can involve agents capable of generating and adding new functions to their own toolset at runtime <a class="yt-timestamp" data-t="17:15:00">[17:15:00]</a>. While powerful, this capability carries significant security risks due to the use of functions like `exec()` <a class="yt-timestamp" data-t="26:36:00">[26:36:00]</a>.

The evolution of [[function_calling_in_ai | function calling]] underscores a fundamental shift in how [[large_language_model_interpretability | language models]] interact with the world, transforming them from mere text generators into versatile tools capable of dynamic action and complex workflows <a class="yt-timestamp" data-t="09:50:00">[09:50:00]</a>.