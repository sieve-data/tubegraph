---
title: Comparison between local and large AI models
videoId: PPDsrvuPhWQ
---

From: [[colemedin]] <br/> 

[[comparison_of_local_and_cloudbased_ai_models | Function calling]] is a powerful feature in the latest large language models (LLMs) such as GPT and Claude, enabling them to interact seamlessly with external services through user-defined functions [00:00:00]. This capability allows AI applications to act as true [[running_ai_agents_on_local_machines | AI agents]], performing actions like interacting with a CRM, booking meetings, or searching the web [00:00:07].

## Limitations of Local LLMs
Lightweight [[working_with_local_large_language_models | local large language models]] like Meta's Llama and Microsoft's Phi typically do not have built-in [[comparison_of_local_and_cloudbased_ai_models | function calling]] capabilities, which means they lose out on the power of interacting with external services [00:00:26]. This distinction highlights a key [[differences_in_architecture_and_functionality_of_ai_models | difference between local and cloud-based models]], where the latter often provide more advanced out-of-the-box features.

## Enabling Custom Function Calling for Local LLMs
To overcome the limitations of local models, custom [[comparison_of_local_and_cloudbased_ai_models | function calling]] can be implemented, allowing any model, regardless of its size, to leverage this power [00:00:37]. This enables the development of nimble [[running_ai_agents_on_local_machines | AI agent applications]] that can run anywhere without constant reliance on larger, cloud-based models like GPT and Claude [00:00:45].

### Key Components of Custom Function Calling

The implementation involves several steps to equip [[working_with_local_large_language_models | local LLMs]] with [[comparison_of_local_and_cloudbased_ai_models | function calling]]:

1.  **Model Acquisition and Management**
    *   Models can be sourced from platforms like Hugging Face, using their serverless API for quick access [00:01:15].
    *   For truly [[working_with_local_large_language_models | local operation]], models can be downloaded and run directly on a machine, though this requires significant local resources [00:04:01].
    *   Streamlit's `cache_resource` decorator is used to prevent re-downloading or re-defining the model every time the application reruns, which would be resource-intensive [00:03:26].

2.  **Defining Tools**
    *   External services are exposed to the AI agent as "tools" [00:02:44]. For demonstration, an Asana task creation function is used as an example tool [00:02:46].
    *   A dictionary maps the function name to its actual Python object, allowing for easy expansion with multiple tools [00:04:33].

3.  **Tool Descriptions and Context**
    *   Each tool requires a descriptive docstring that the AI can understand [00:05:00].
    *   This docstring provides the AI with crucial context, including the function's purpose, how to call it, required arguments and their types, and what it returns [00:05:07]. This information is injected into the system prompt [00:05:29].

4.  **Crafting the Prompt and Response Schema**
    *   A carefully crafted prompt is essential to instruct the AI on how to return a response that can be parsed for [[comparison_of_local_and_cloudbased_ai_models | tool calls]] [00:05:36].
    *   LangChain's parser is used to ensure the AI's response conforms to a specific JSON schema [00:06:01].
    *   The schema includes two main keys:
        *   `tool_calls`: A list of objects, each containing the `name` of the tool and its `arguments` [00:06:12]. This array is populated if a tool call is needed [00:06:24].
        *   `content`: Raw text to be displayed to the user [00:06:18]. This is used when no tool call is required [00:10:54].

5.  **Robust Error Handling and Recursion**
    *   A function `prompt_ai` handles the interaction, including recursion to retry if the AI's output does not conform to the expected JSON schema [00:07:27]. This ensures that the parsed response is always a valid JSON object [00:08:42].
    *   To prevent [[differences_in_architecture_and_functionality_of_ai_models | local models]] from hallucinating and invoking the same tool multiple times, a check is implemented to track already invoked tools [00:07:40].

6.  **UI and Interaction**
    *   Streamlit is used to build a simple user interface for the chatbot [00:11:16].
    *   The initial system message, containing the tool descriptions and expected JSON schema, provides the AI with the necessary context from the start [00:11:24].
    *   User input triggers the `prompt_ai` function, which processes the request, invokes any required tools, and displays the response in the UI [00:12:01].

### Demonstration
In a practical demonstration, a [[working_with_local_large_language_models | local Llama 3 model]] was successfully used to create a task in Asana [00:13:33]. When prompted with "I need to mow the lawn by Saturday," the AI agent, augmented with custom [[comparison_of_local_and_cloudbased_ai_models | function calling]], created a task in Asana with the correct name and due date [00:14:10]. This demonstrates that [[strategies_for_scaling_ai_with_local_llms | custom tooling enables]] a [[working_with_local_large_language_models | local LLM]] to interact with external services, a capability typically reserved for larger, cloud-based models [00:14:34].

## Challenges and Considerations for Local LLMs
While custom [[comparison_of_local_and_cloudbased_ai_models | function calling]] greatly enhances [[working_with_local_large_language_models | local models]], it's important to acknowledge their limitations compared to powerful models like GPT and Claude [00:15:11]. [[comparing_local_and_cloudbased_large_language_models | Local models]] may exhibit:
*   **Hallucinations:** Sometimes producing incorrect JSON output or attempting to call functions in unexpected ways [00:15:18].
*   **Inconsistencies:** Less predictable behavior in complex prompts [00:15:24].

These issues necessitate workarounds like recursion and checks to ensure reliable operation [00:15:22]. However, as [[differences_in_architecture_and_functionality_of_ai_models | AI technology]] advances, [[working_with_local_large_language_models | local models]] are expected to catch up in their ability to handle complex prompts and reduce these inconsistencies [00:15:28].

This approach of [[incorporating_ai_models_and_databases_in_a_local_setup | augmenting local models with custom functions]] is a valuable tool for developers looking to build robust [[running_ai_agents_on_local_machines | AI agents]] that can run anywhere [00:15:35].