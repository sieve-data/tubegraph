---
title: Custom function calling in local AI models
videoId: PPDsrvuPhWQ
---

From: [[colemedin]] <br/> 

Function calling is a powerful capability in large language models (LLMs) like GPT and Claude, enabling them to interact seamlessly with external services by invoking functions defined by the user <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This allows AI applications to act as true [[function_calling_capabilities_in_ai_agents | AI agents]], booking meetings, searching the web, or interacting with CRMs <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. However, lightweight and [[comparison_of_local_and_cloudbased_ai_models | local AI models]] like Meta's Llama or Microsoft's Phi typically lack this built-in feature <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. Implementing custom function calling allows any model, regardless of its size, to gain this capability, enabling the creation of nimble [[function_calling_capabilities_in_ai_agents | AI agent]] applications that run anywhere without constant reliance on larger, cloud-based models <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>.

## Why Custom Function Calling?

While [[comparison_between_local_and_large_ai_models | large AI models]] like GPT and Claude come with inherent function calling abilities, [[comparison_between_local_and_large_ai_models | local models]] such as Meta's Llama 3 or Microsoft's Phi do not <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This limitation prevents them from interacting with external services, a core feature for building robust [[function_calling_capabilities_in_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Custom function calling bridges this gap, allowing developers to augment any small or [[comparison_of_local_and_cloudbased_ai_models | local AI model]] with the ability to perform actions via external tools, thereby reducing reliance on large commercial APIs <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Implementation Overview

This approach focuses on augmenting [[comparison_of_local_and_cloudbased_ai_models | local AI models]] with custom function calling using a Python-based [[tech_stack_for_local_ai_applications | tech stack]] involving Streamlit and LangChain <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The example utilizes a lightweight version of Meta's Llama 3 model obtained from Hugging Face <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The complete code is available on GitHub under the `local_llm_tool_calling` folder, including example environment variables and a `requirements.txt` file for setup <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Setting Up the Environment and Model

1.  **Import Python Packages**: A variety of packages are imported, relevant to Streamlit, LangChain, and other functionalities <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
2.  **Environment Variables**: Crucial variables like the model name and Hugging Face API tokens are loaded from an `.env` file <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
3.  **Model Definition**: The AI model is defined based on an environment variable, defaulting to the lightweight Meta Llama 3 <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   The `@streamlit.cache_resource` decorator is used to prevent the model from being redefined on every Streamlit rerun, saving resources <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.
    *   Models can be accessed via Hugging Face Endpoints (serverless API for quick use) or run truly locally using `huggingface_pipeline.from_model_id` (requires significant local resources and download time) <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.

### Defining Tools and Descriptions

To enable the AI agent to interact with external services, specific tools must be defined.
*   **Asana Integration**: As an example, an Asana integration is used, allowing the AI to create tasks within the Asana task management platform <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. A function `create_asana_task` is defined that accepts a task name and a due date <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Tool Mapping**: A Python dictionary maps function names (e.g., `'create_asana_task'`) to their actual function objects, allowing for easy expansion with multiple tools <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   **Tool Descriptions**: For each tool, a description is generated using its docstring <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. This docstring provides the AI with essential context: the function's purpose, how to call it, its required arguments and types, and what it returns <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. This ensures the AI knows when and how to use the tool <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

### Crafting the System Prompt and JSON Schema

A critical aspect of custom function calling is explicitly instructing the AI on the expected output format <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
*   **Structured Output**: The AI must return responses in a specific JSON schema to indicate when it intends to use a tool and what arguments to use <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. This also allows for the invocation of multiple tools within a single prompt <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **LangChain Parser**: LangChain's `JsonOutputParser` is used to enforce this schema <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. The schema includes two main keys:
    *   `tool_calls`: A list of objects, each with `name` (function name) and `arguments` (function arguments) <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. This array is populated if a tool call is needed, otherwise it's empty <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
    *   `content`: Raw text to be returned to the user if no tool call is made, or as part of the overall response <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **Schema Validation**: The parser validates the AI's response against this schema, throwing an error if it doesn't conform <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. This ensures predictable output, mitigating hallucinations <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Injecting Tools**: The `tool_descriptions` array is dumped into the system prompt, providing the AI with all the necessary information about available tools and the required output format <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### Prompting the Local AI Agent Function (`prompt_AI`)

This function handles the interaction with the [[comparison_of_local_and_cloudbased_ai_models | local AI model]] and the execution of tool calls <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
1.  **Error Handling & Retries**:
    *   A recursion limit prevents infinite loops if the AI repeatedly fails to conform to the schema <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   If the AI's output doesn't match the parser's schema, the function retries by incrementing `nested_calls` and invoking itself again <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
2.  **Preventing Hallucinations**: An array of `invoked_tools` is maintained to prevent [[comparison_between_local_and_large_ai_models | local models]] from hallucinating and invoking the same tool call multiple times <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.
3.  **Chatbot Invocation**: The chatbot is invoked using `chat_huggingface` (or `chat_openai` for GPT models) <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.
4.  **Processing Response**:
    *   If the `tool_calls` array in the `AI_response` is populated (meaning its length is greater than zero), the function iterates through each tool call <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.
    *   For each tool call, the corresponding function is invoked using the extracted arguments <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
    *   The result of the tool invocation is added as an internal 'thought' message for the AI, not displayed to the user, to inform its subsequent responses <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   The tool is added to `invoked_tools` to prevent re-invocation <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>.
    *   After all tool calls, the AI generates a user-facing response based on the tool's result <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.
    *   If no tool calls are necessary (e.g., a simple greeting), the `content` from the AI response is returned directly to the user <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>.

### Streamlit UI Integration

The `main` function orchestrates the Streamlit user interface:
1.  **UI Initialization**: Sets the Streamlit UI title <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
2.  **Session State**: Initializes the session state with an initial system message that contains the injected tool descriptions and schema information <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. This provides the AI with its initial context for tool calling <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
3.  **Chat History Display**: Displays the chat history, excluding the AI's internal 'thoughts' <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
4.  **User Interaction**: When the user inputs text into the chat, the `prompt_AI` function is called to get a response and invoke any required tools. The response is then displayed in the UI <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

## Demonstration and Verification

To run the [[building_and_deploying_custom_ai_front_ends | local AI agent chatbot]], navigate to the `local_llm_tool_calling` directory in the terminal and execute `streamlit run local_agent_with_ui.py` <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.

1.  **Initial Chatbot State**: The chatbot displays the system message, showing the directions for JSON output and the defined tool (e.g., `create_asana_task`) with its detailed docstring <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
2.  **Basic Interaction**: A greeting like "Hi how can you help me" elicits a response where `tool_calls` is empty, and only the `content` (raw text) is returned <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>.
3.  **Tool Invocation**: A command like "I need to mow the lawn by Saturday" triggers the `create_asana_task` function <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
    *   The AI responds confirming the task creation and its due date <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
4.  **Verification**: The task "Mow the lawn" with the correct due date is confirmed to be created in Asana <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. This demonstrates that a [[comparison_of_local_and_cloudbased_ai_models | local AI model]] (Llama 3) can successfully perform external actions via custom function calling <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>. This method is adaptable to other [[comparison_of_local_and_cloudbased_ai_models | local AI models]] like Microsoft Phi or those used with Olama <a class="yt-timestamp" data-t="00:14:36">[00:14:36]</a>.

## Limitations and Future Outlook

While powerful, it's important to note that [[comparison_between_local_and_large_ai_models | local models]] are generally not as robust as GPT or Claude <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. This can manifest as:
*   **Hallucinations**: [[comparison_between_local_and_large_ai_models | Local models]] may sometimes produce incorrect JSON outputs or call functions in unexpected ways <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>. The implemented checks (retries, tracking invoked tools) help mitigate these issues <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Inconsistencies**: Their performance in handling complex prompts might be less consistent <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

However, as [[extending_local_ai_infrastructure | AI technology advances]], [[comparison_between_local_and_large_ai_models | local models]] are expected to catch up in their capabilities, making custom function calling an increasingly valuable tool for developers to extend the functionality of any [[incorporating_ai_models_and_databases_in_a_local_setup | local AI setup]] <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.