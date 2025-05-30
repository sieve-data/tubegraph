---
title: Use of Hugging Face and local models like Llama 3
videoId: PPDsrvuPhWQ
---

From: [[colemedin]] <br/> 

The latest large language models (LLMs) such as GPT and Claude possess a powerful feature called function calling, which enables them to interact seamlessly with external services through user-created functions <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This capability allows AI applications to perform actions like interacting with CRMs, booking meetings, or searching the web, transforming them into true [[hugging_face_and_anthropic_definitions_of_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## The Challenge with Lightweight Local Models
Lightweight and [[working_with_local_large_language_models | local models]], such as Meta's Llama <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a> or Microsoft's Phi, typically lack built-in function calling capabilities <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This absence means they cannot natively interact with external services in the same way as the larger, proprietary models <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Custom Function Calling Implementation
To overcome this limitation, [[custom_function_calling_in_local_ai_models | custom function calling]] can be implemented, enabling any model, regardless of its size, to leverage this power <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This allows for the creation of nimble [[hugging_face_and_anthropic_definitions_of_ai_agents | AI agent]] applications that can run anywhere without constant reliance on larger models <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

### Model Selection and Access
The primary model used for demonstration is a lightweight version of Meta's [[using_llama_for_llms | Llama 3]] <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. Models can be accessed via:
*   **Hugging Face Endpoint**: Used for quick serverless API access to models <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   **Local Execution**: Models can be run truly locally, though this requires significant computer resources and download time <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>. The code can be easily swapped to use `huggingface_pipeline.from_model_ID` for local execution <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

### Environment Setup
To replicate the environment, a GitHub repository is provided containing:
*   An example environment variable file <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   A `requirements.txt` file listing all necessary Python packages <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
*   Essential environment variables include the model name and Hugging Face API tokens <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

### Integrating External Services and Defining Tools
To demonstrate the interaction with an external service, Asana (a task management platform) is used <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. The AI agent is given the ability to create tasks in Asana <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Tools are defined as a mapping between a function name and its actual Python function object <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. The `docstring` of each function is crucial as it provides the AI with all necessary context: what the function does, how to call it, its arguments and their types, and what it returns <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This setup is designed to be easily extensible for multiple tools <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

### Crafting the Prompt and Response Handling
A meticulously crafted prompt is essential to instruct the AI on how to return a response <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>. This ensures the AI's output is not just raw text but conforms to a specific JSON schema <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

The schema includes two main keys:
*   `tool_calls`: A list of tool calls, each containing the `name` of the tool and its `arguments` <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
*   `content`: Raw text to be returned directly to the user if no tool calls are needed <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>.

[[combining_lightweight_models_with_reasoning_llms | LangChain's JSON output parser]] is used to validate the AI's response against this schema <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. If the AI's output doesn't match the schema, a recursion mechanism retries the prompt <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. This robust parsing ensures that the AI's response is a reliable JSON object, mitigating issues like hallucinations and inconsistencies often seen in LLMs <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

The tool descriptions are injected into the system prompt, providing the AI with the initial context it needs for function calling <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>.

### The `prompt_AI` Function Logic
The core `prompt_AI` function:
*   Manages message history <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.
*   Implements recursion for retries if the AI output doesn't conform to the schema <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   Keeps track of already invoked tool calls to prevent repetitive or hallucinated calls by [[working_with_local_large_language_models | local models]] <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.
*   Invokes functions based on the parsed tool calls, adding the result as an internal "thought" for the AI <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   Generates a user-facing response based on tool invocation results or direct content if no tools were called <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Streamlit UI Integration
A Streamlit UI is used to interact with the [[integration_of_small_agents_with_hugging_face_and_olama | local AI agent chatbot]] <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. The UI displays the chat history, excluding the AI's internal thoughts <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. User input triggers the `prompt_AI` function, and the response is displayed <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. The initial system message, containing the tool descriptions and schema, provides the necessary context to the AI for tool calling <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

## Demonstration
Using a lightweight version of [[building_a_powerful_chatbot_using_llama_3_1_405b | Llama 3]] from Hugging Face, the chatbot can successfully create a task in Asana <a class="yt-timestamp" data-t="00:13:33">[00:13:33]</a>. For example, a request like "I need to mow the lawn by Saturday" leads the AI to invoke the `create_asana_task` function, resulting in a verified task creation in Asana <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.

## Considerations
While custom function calling significantly enhances local models, it's important to note that [[using_local_language_models_llm_for_code_generation | local models]] are generally not as powerful as GPT or Claude <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. This can manifest in issues like:
*   **Hallucinations**: Incorrect JSON output or repeated tool calls <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
*   **Inconsistencies**: Variations in how functions are called <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

Despite these limitations, the ability to implement [[using_local_large_language_models_with_autod_dev | custom function calling]] for any model, including those from Hugging Face or [[integration_of_small_agents_with_hugging_face_and_olama | Ollama]], provides a valuable tool for developers <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. As AI technology advances, [[working_with_local_large_language_models | local models]] are expected to catch up in their ability to handle complex prompts and functions <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.