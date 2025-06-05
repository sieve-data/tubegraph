---
title: Model Context Protocol and tool integration
videoId: Nqb7JTx0Pqo
---

From: [[aidotengineer]] <br/> 

[[model_context_protocol_mcp | Model Context Protocol]] (MCP) is a framework designed to enable Large Language Models (LLMs) to access and utilize external tools and services <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This protocol facilitates the interaction between an LLM and various tools, allowing the model to perform actions beyond its inherent text generation capabilities <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Core Functionality of [[model_context_protocol_mcp | MCP]]
[[model_context_protocol_mcp | MCP]] serves two primary functions:
1.  **Information Store for Tools**: It acts as a repository of information about available tools, providing the LLM with the necessary details on how to make calls to these tools or otherwise utilize them <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
2.  **Tool Execution Service**: The [[model_context_protocol_mcp | MCP]] tool service is responsible for running the tools when an LLM decides to make a call <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. After executing an action (e.g., adding numbers, navigating a webpage), it returns a response containing the result or guidance for the LLM's next action <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

Common tools accessible via [[model_context_protocol_mcp | MCP]] include browser use for navigating websites, Stripe, GitHub, and Gmail integrations <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Integrating LLMs with [[model_context_protocol_mcp | MCP]]
To integrate an LLM with [[model_context_protocol_mcp | MCP]], the language model is typically exposed as an API, often in the style of an OpenAI endpoint <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This setup requires several points of integration and data translation <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>:
1.  **Tool Information Conversion**: Tool information received from [[model_context_protocol_mcp | MCP]] services must be converted into a list of JSON tools, as expected by OpenAI-style endpoints <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  **Tool Response Formatting**: The tool response must be converted into a format the LLM expects <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  **Tool Call Extraction**: When the LLM calls a tool by emitting tokens or text, the system must detect and extract the tool call from the text, specifically converting it from a format like Hermes into a JSON structure that the OpenAI API expects <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

## Prompt Structure for Tool Calls
The interaction with the LLM is managed through a specific prompt structure <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>:
*   **System Message**: This initial part of the prompt, enclosed in a `system start` tag, describes to the LLM how to make tool calls <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. It instructs the LLM to pass tool calls as JSON objects within `tool` XML tags <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **User Message**: This is the input from the user (e.g., "navigate to trellis.com") <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Assistant Response**: The assistant (LLM) responds, potentially performing "thinking" and then deciding to either call a tool (e.g., navigating with a browser) or provide a text-based response after completing a task <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

The entire conversation, including system messages, user inputs, assistant thinking, tool calls, and tool responses, forms a "trace" that is crucial for fine-tuning <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

## Agent Setup for Data Collection
To collect high-quality traces for fine-tuning, an agent is set up to interact with the [[model_context_protocol_mcp | MCP]] services <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.
*   **Repository**: All necessary materials and scripts are available in the `Trellis Research AI Worlds Fair 2025` repository, specifically in the `MCP agent fine-tune` folder <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   **Model Selection**: It is recommended to use a consistent model for both data generation and fine-tuning. For example, a Quen type agent is used to generate traces if a Quen model will be fine-tuned later <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. This is because OpenAI models typically do not share their "thinking" traces, which are valuable for training <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. A 30 billion parameter Quen model (mixture of experts) is suggested, running on a service like RunPod <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **Endpoint Configuration**: The LLM is configured as an OpenAI-style endpoint <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. Key configurations include:
    *   Enabling reasoning and a reasoning parser to extract "think tokens" into a JSON format <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
    *   Setting a `max model length` (e.g., 32,000 tokens) <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
    *   Enabling automatic tool choice, allowing the LLM to decide when and which tool to call <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
    *   Specifying a tool parser (e.g., Hermes) to extract tool calls into JSON format <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
*   **Tool Response Truncation**: A `truncate` argument can be used to limit the length of tool responses (e.g., browser accessibility trees) to manage context length for the LLM <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

## Running the Agent and Generating Traces
When the agent runs, it:
1.  Starts the [[model_context_protocol_mcp | MCP]] server, loading configured tools (e.g., 25 Playwright browser tools) <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
2.  Takes user input (e.g., "navigate to trellis.com and read out the top two lines") <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
3.  Sends the user message to the LLM, which then generates "thinking tokens" (reasoning) <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
4.  If the LLM decides to make a tool call (e.g., `browser.navigate`), it presents it for user approval <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
5.  Upon approval, the [[model_context_protocol_mcp | MCP]] executes the tool (e.g., opening a browser window if not in headless mode) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
6.  The tool returns a response (e.g., an accessibility tree of the webpage), which is sent back to the LLM <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
7.  The LLM then processes this information, potentially performing more thinking and producing a final text-based response <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.

All these interactions are logged as "traces," comprising the full conversation history (messages) and a list of available tools <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. These traces are invaluable for fine-tuning a smaller model to acquire similar capabilities <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>.

## Curating and Storing Traces
To optimize the fine-tuning process, traces can be curated:
*   **Manual Adjustment**: Traces can be manually adjusted if the LLM's behavior isn't ideal, either by deleting turns or combining sections <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   **System Prompts**: A guiding system prompt can be used during data generation to help the LLM create a "nice tidy trace" without needing to include the prompt in the final training data <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.
*   **Data Unrolling**: Multi-turn conversations are "unrolled" into multiple rows in the dataset. For instance, a three-turn conversation becomes three separate rows, each representing a different point in the conversation, allowing the model to train on various interaction lengths <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. This is particularly important because models like Quen only include reasoning from the most recent turn in their template <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>.
*   **Pushing to Hub**: The curated dataset, containing both tools and conversations, is pushed to a platform like Hugging Face Hub <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.

## Fine-tuning Process
The collected traces are then used for fine-tuning an LLM:
1.  **Environment Setup**: This often involves installing libraries like Unslo and setting up a runtime environment (e.g., on Colab or RunPod) <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.
2.  **Model Loading**: A smaller model, such as a 4 billion parameter Quen model, is loaded for fine-tuning <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
3.  **Applying Adapters**: Instead of training all parameters, adapters are applied to specific parts of the model, such as attention modules and MLP layers, using techniques like Low Rank Adapters (LoRA) <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. This freezes most of the main weights and only trains a small percentage of parameters <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>.
4.  **Data Preparation**: The previously collected dataset is loaded, and messages and tools are templated into a single long string of text, which serves as the input for training <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a>.
5.  **Training Parameters**:
    *   **Batch Size**: Often set to 1 due to VRAM limitations, though a larger batch size (e.g., 32) is ideal for smoother training <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.
    *   **Epochs**: A small number of epochs (e.g., one) can be used for initial training <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.
    *   **Learning Rate**: A relatively high learning rate can be used for smaller models <a class="yt-timestamp" data-t="00:28:58">[00:28:58]</a>.
    *   **Optimizer**: Optimizers like AtomW 8-bit can be used to save VRAM <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>.

## Reinforcement Learning (RL) Considerations
While the primary focus is supervised fine-tuning (SFT), [[agentic_frameworks_and_tool_integration | reinforcement learning]] (RL) can be used to further automate trace generation or improve performance. However, it's highly recommended to first perform SFT on high-quality, manually curated traces <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>. This initial SFT helps the model generate good traces more frequently, speeding up later RL training by ensuring it more often reaches scenarios where it receives a positive reward <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>. For RL, defining clear rewards based on verifiable correct answers is crucial <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.

## Post-Training and Evaluation
After fine-tuning:
*   **Saving and Pushing**: The fine-tuned model and tokenizer can be saved and optionally pushed to Hugging Face Hub, often merged into 16-bit format <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>.
*   **Inference Endpoint Update**: The name of the fine-tuned model can be swapped into the inference endpoint configuration, creating a ready-to-use endpoint with improved performance <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.
*   **Evaluation**: While complex evaluation setups are beyond the scope of a simple demonstration, one would typically run the fine-tuned model on the endpoint to assess its performance on new tasks <a class="yt-timestamp" data-t="00:34:07">[00:34:07]</a>.

Even with a small dataset (e.g., 50-100 examples), significant performance improvements can be achieved, especially for common or critical narrow use cases <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.

For more detailed information on [[model_context_protocol_mcp | MCP]] and creating custom servers, additional videos on the Trellis Research YouTube channel are available <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.