---
title: Function calling in large language models
videoId: PPDsrvuPhWQ
---

From: [[colemedin]] <br/> 

Function calling is a powerful feature in advanced [[reasoning_large_language_models_and_their_impact | large language models]] (LLMs) like GPT and Claude <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It enables LLMs to interact with external services by generating structured calls to user-defined functions <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. This capability transforms LLM applications into true [[ai_agents_and_large_language_models | AI agents]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Capabilities of Function Calling

Through function calling, LLMs can perform a wide range of actions on a user's behalf, such as:
*   Interacting with a Customer Relationship Management (CRM) system <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>
*   Booking meetings on a calendar <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>
*   Searching the web <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>

## [[challenges_with_large_language_models | Challenges with Large Language Models]] and Function Calling

While powerful, function calling is not natively built into lightweight, [[working_with_local_large_language_models | local models]] like Meta's Llama or Microsoft's Phi <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. This means that out-of-the-box, these smaller models cannot leverage the same external interaction capabilities as their larger counterparts <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## Custom Function Calling for Local LLMs

It is possible to implement custom function calling for any [[working_with_local_large_language_models | local model]], regardless of its size <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This allows for the creation of nimble [[ai_agents_and_large_language_models | AI agent applications]] that can run anywhere without constant reliance on larger, proprietary models <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. The approach typically focuses on integrating custom function calling with [[working_with_local_large_language_models | local models]] sourced from platforms like Hugging Face <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. A common model used for this is a lightweight version of Meta's Llama 3 <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.

### Implementation Overview

The process involves several key steps to enable custom function calling:

1.  **Environment Setup**:
    *   Code is typically provided in a GitHub repository, including example environment variable files and `requirements.txt` for Python packages <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
    *   Environment variables usually include model names and Hugging Face API tokens <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

2.  **Model Definition**:
    *   The LLM model is defined, often defaulting to a lightweight Llama version <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
    *   Options for GPT are included for performance comparison <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    *   Models can be accessed via Hugging Face Endpoint (serverless API) or truly run locally using `huggingface_pipeline.from_model_id` for self-hosting <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>.
    *   Streamlit's `@st.cache_resource` decorator is used to prevent re-initializing the model on every rerun of the application <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

3.  **Integrating with External Services**:
    *   To demonstrate, an external service like Asana (a task management platform) can be used <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
    *   A function, e.g., `create_asana_task`, is defined to interact with the service, taking parameters like `task_name` and `due_date` <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This allows the [[ai_agents_and_large_language_models | AI agent]] to create tasks in Asana <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

4.  **Defining Tools**:
    *   A dictionary maps function names to their actual function objects in the Python script <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>. This structure makes it easy to add multiple tools <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
    *   For each tool, a detailed description is created, including the function name and its doc string <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. The doc string provides the AI with crucial context on what the function does, how to call it, its arguments and types, and what it returns <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

5.  **Crafting the Prompt**:
    *   The tool descriptions are injected into the LLM's system prompt <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. This is critical for the AI to understand the available tools <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
    *   The prompt must explicitly instruct the AI on how to format its response, typically adhering to a specific JSON schema <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   The schema defines two main keys: `tool_calls` (a list of objects, each with `name` and `arguments`) and `content` (raw text for the user) <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. This allows for invoking multiple tools within one prompt <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

6.  **Processing AI Responses**:
    *   A parser (e.g., LangChain's JSON output parser) is used to validate the AI's response against the defined JSON schema <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
    *   If the AI's output doesn't conform to the schema, a retry mechanism with recursion is implemented to guide the AI to correct its output <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>. This ensures the response is a reliable JSON object <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
    *   The system checks if the `tool_calls` array is populated <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>. If so, it iterates through each tool call, retrieves the corresponding function, and invokes it with the provided arguments <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
    *   To prevent [[limitations_of_large_language_models | hallucinations]] where local models might try to invoke the same tool multiple times, an array of "invoked tools" is maintained <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.
    *   The result of tool calls is added as a "thought" message for the AI, informing it of the outcome without displaying it to the user <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
    *   If no tools are called, the `content` from the AI's response is directly returned to the user <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.

7.  **User Interface (UI)**:
    *   A UI framework like Streamlit can be used to create a chatbot interface <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
    *   The initial system message, containing the tool descriptions and schema, is loaded into the session state to provide the AI with context <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
    *   The chat history is displayed, excluding internal AI "thoughts" <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
    *   User input triggers the `prompt_ai` function, and the response (either raw text or tool-invoked output) is displayed <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.

### Demonstration

To demonstrate, a user can interact with the [[working_with_local_large_language_models | local LLM]] (e.g., Llama 3) via the chatbot UI <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Initially, a general greeting might result in a textual response without tool calls <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. However, a request like "I need to mow the lawn by Saturday" <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a> will trigger the `create_asana_task` function <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. The LLM will then confirm the task creation, and the user can verify the task in Asana <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.

## [[limitations_of_large_language_models | Limitations of Large Language Models]] and Future Outlook

While custom function calling for [[working_with_local_large_language_models | local models]] is effective, it's important to note that [[working_with_local_large_language_models | local models]] are generally not as powerful as leading models like GPT or Claude <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. This can manifest in:
*   **Hallucinations**: Incorrect JSON output or attempting to call functions incorrectly <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.
*   **Inconsistencies**: Unusual function call patterns <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

Despite these [[limitations_of_large_language_models | challenges]], the ability to implement custom function calling for any model is a valuable skill <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>. As AI technology advances, [[working_with_local_large_language_models | local models]] are expected to catch up in their capability to handle complex prompts and reliably perform function calls <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>.