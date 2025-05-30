---
title: Setting up AI agents with LangChain and Streamlit
videoId: PPDsrvuPhWQ
---

From: [[colemedin]] <br/> 

Function calling is a powerful feature of modern large language models (LLMs) like GPT and Claude, enabling them to interact with external services through user-defined functions [00:00:00]. This capability allows LLMs to perform actions such as booking meetings, interacting with CRMs, or searching the web, transforming them into true [[setting_up_ai_agents_with_python_and_langchain | AI agents]] [00:00:07].

However, smaller, local models like Meta's Llama or Microsoft's Phi lack built-in function calling capabilities [00:00:24]. This article details how to implement custom function calling for any model, enabling even lightweight models to build powerful [[setting_up_ai_agents_with_python_and_langgraph | AI agent]] applications that can run anywhere without constant reliance on larger LLMs [00:00:37].

## Key Components and Setup

The demonstration focuses on custom function calling and local models, primarily using a lightweight version of Meta's Llama 3 from Hugging Face [00:01:11]. The full code is available on GitHub in the `local_llm_tool_calling` folder [00:01:27].

### Environment and Dependencies
To follow along, users will need to set up environment variables, including model details and Hugging Face API tokens, and install required Python packages from a `requirements.txt` file [00:01:39].

### Defining the Model
The LLM model is defined based on an environment variable, defaulting to a lightweight version of Meta's Llama [00:02:22]. The system can also use GPT for performance comparison [00:03:42].

The `streamlit.cache_resource` decorator is used to prevent the model from being redefined on every [[using_langchain_and_streamlit_for_rag_development | Streamlit]] rerun, which would be expensive for local models [00:03:26]. Hugging Face Endpoints are used for quick serverless API access, but the code can be easily swapped to run models truly locally by using `huggingface_pipeline.from_model_id` [00:03:55].

### External Service Integration (Asana Example)
To demonstrate interaction with an external service, Asana, a task management platform, is used [00:02:34]. The example focuses on the AI agent's ability to create tasks in Asana [00:02:47]. A Python function `create_asana_task` is defined, which takes a task name and due date to create a task in Asana [00:02:56].

### Tool Definitions
A dictionary maps function names to their actual Python function objects [00:04:33]. This setup allows for easy expansion to include multiple tools [00:04:49]. For each tool, a description is created that includes the function's name and its docstring [00:05:00]. This docstring provides the AI with all necessary context: what the function does, how to call it, its arguments, their types, and what it returns [00:05:07].

### Crafting the Prompt and Schema
A crucial part of enabling custom function calling is explicitly instructing the AI on how to return a response [00:05:40]. The AI's response must conform to a specific JSON schema using a [[setting_up_ai_agents_with_python_and_langchain | LangChain]] parser [00:06:01].

The schema has two main keys:
*   `tool_calls`: A list of tool calls, where each call has a `name` and `arguments` [00:06:12]. This array is populated if the AI needs to make any tool calls [00:06:24].
*   `content`: Raw text to be returned to the user [00:06:20].

The system prompt for the AI includes directions on how to output a response that conforms to this schema [00:06:38]. The tool descriptions are injected into the system prompt, providing the AI with the necessary information about available custom functions [00:06:55].

## The `prompt_AI` Function

This function handles the interaction with the local [[building_ai_agent_workflows_with_langgraph | AI agent]]. It takes a list of messages and incorporates logic for retries and preventing duplicate tool calls [00:07:21].

Key aspects of the `prompt_AI` function:
*   **Recursion for Retries**: If the AI's output doesn't conform to the defined JSON schema, the function retries by incrementing a `nested_calls` counter, preventing infinite loops [00:07:26].
*   **JSON Output Parser**: It uses [[setting_up_ai_agents_with_python_and_langchain | LangChain]]'s `JsonOutputParser` with the specified schema, ensuring that the AI's response is a valid JSON object [00:08:04]. This guarantees that the `tool_calls` and `content` fields are always present and correctly structured [00:08:43].
*   **Tool Invocation**: If the `tool_calls` array is not empty, the function iterates through each tool call [00:09:08]. It retrieves the actual function object using the `tool_name` from the parsed response and invokes it with the provided arguments [00:09:44].
*   **Handling Hallucinations**: Local models may sometimes hallucinate and attempt to invoke the same tool multiple times [00:07:39]. The function maintains a list of `invoked_tools` to prevent duplicate calls, like creating the same Asana task twice [00:10:08].
*   **Generating User Response**: After tool calls are made (or if no tool calls are needed), the AI generates a response for the user based on the tool's output or the initial content [00:10:31].

## Streamlit UI (`main` function)

The `main` function sets up the [[using_langchain_and_streamlit_for_rag_development | Streamlit]] user interface for the chatbot [00:11:11].
*   It initializes the [[using_langchain_and_streamlit_for_rag_development | Streamlit]] UI with a title and sets up the session state for messages [00:11:16].
*   The initial system message, containing the tool descriptions and schema details for custom function calling, is injected into the chat history [00:11:24].
*   [[using_langchain_and_streamlit_for_rag_development | Streamlit]] components display the chat history (excluding internal AI "thoughts") [00:11:48].
*   User input via a `chat_input` component triggers the `prompt_AI` function to get a response and invoke any required tools, then displays the response in the UI [00:12:00].

## Demonstration

The [[developing_ai_tools_with_streamlit_and_gpt | Streamlit]] application can be run from the terminal using `streamlit run local_agent_with_ui.py` [00:12:27].

Upon launching, the chatbot displays the system message, showing the directions for JSON output and the description of the `create_asana_task` tool, including its docstring [00:12:54].

*   **Initial Query**: A basic message like "Hi, how can you help me?" results in a JSON response with an empty `tool_calls` array and a content message, as no tool invocation is needed [00:13:37].
*   **Tool Invocation**: When prompted with "I need to mow the lawn by Saturday," the Llama 3 model processes the request and invokes the `create_asana_task` function [00:13:57]. The application then displays a confirmation message, "Task mow the lawn has been created in Asana and is due on the 13th" [00:14:10]. Verification in Asana confirms the task's creation [00:14:20].

This demonstrates custom function calling with a local model, showing that any model can be augmented with this capability [00:14:34].

## Considerations for Local Models

While custom function calling is now possible for any model, it's important to note that local models, such as Llama and Phi, are not as powerful as GPT or Claude [00:15:11]. This can lead to:
*   **Hallucinations**: Inconsistencies in output, such as incorrect JSON formatting [00:15:18].
*   **Function Call Errors**: Sometimes the models may call functions incorrectly [00:15:24].

Despite these challenges, the ability to implement custom function calling for any model is a significant development, and local models are continuously improving [00:15:28]. This technique is a valuable tool for building flexible and powerful [[building_ai_agents_using_pantic_ai_and_lang_graph | AI agents]] [00:15:35].