---
title: Finetuning language models with MCP
videoId: Nqb7JTx0Pqo
---

From: [[aidotengineer]] <br/> 

This article outlines a workshop on [[MCP agent finetuning | fine-tuning AI agents]] that interact with tools using the Model Context Protocol (MCP) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The goal is to generate high-quality agent reasoning traces, save tool interactions and multi-turn conversations, [[finetuning_ai_models_for_better_performance | fine-tune a model]] (specifically Quen 3 but applicable to others), and evaluate its improved performance <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. All materials are available in the `Trellis Research AI Worlds Fair 2025` repository, specifically in the `MCP agent fine-tune` folder <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## What is Model Context Protocol (MCP)?

[[integrating_ai_with_applications_using_model_context_protocol_mcp | Model Context Protocol (MCP)]] is a standardized way to provide services and access to tools for Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. While the focus here is on browser use (navigating websites), MCPs exist for various services like Stripe, GitHub, and Gmail <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

MCP performs several key functions:
*   **Information Storage**: It acts as a repository for information about tools, helping the LLM understand how to make calls to them <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Tool Execution**: The MCP tool service also runs the tools. When an LLM decides to call a tool, MCP executes the action (e.g., adding numbers, navigating a page) and returns a response that includes results or guiding information <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This allows the LLM to loop back for further tool calls or generate a text-based response <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Integrating LLMs with MCP using an OpenAI API Endpoint

To allow an LLM to access tools via MCP, the language model is typically exposed as an [[integrating_ai_with_applications_using_model_context_protocol_mcp | OpenAI API endpoint]] <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This is a common practice, as many models and libraries support this API style <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

There are specific points of integration and data translation required:
1.  **MCP to OpenAI Tool Format**: Tool information from MCP services must be converted into lists of JSON tools, as expected by OpenAI endpoints <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  **Tool Response Formatting**: The response from a tool must be converted into a format the language model expects <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  **Tool Call Detection and Extraction**: When the LLM emits tokens or text to call a tool, the agent needs to detect and extract this call <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. For the Quen model, the text indicating a tool call will be in Hermes format <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Prompt Structure for Tool Calls

The interaction between the LLM and tools is guided by a specific prompt structure:
*   **System Message**: Begins with a `system start` tag and describes how the LLM can make tool calls, typically by passing JSONs within `<tool>` XML tags <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. It informs the LLM about available tools (e.g., browser) and instructs it to return function calls as JSON inside `<tool call>` tags <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **User Message**: The initial request from the user (e.g., "navigate to trellis.com") <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Assistant Response**: The LLM's response, which might involve "thinking" (internal reasoning), making a tool call (e.g., `browser.navigate`), or providing a text-based answer if a task is complete <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

## Data Collection for Fine-tuning

Data collection is a crucial step for [[finetuning_ai_models_for_better_performance | fine-tuning]] LLMs. The process involves running an agent, capturing its interactions, and curating high-quality traces.

### Setting up the LLM Endpoint for Data Generation
It's recommended to use a consistent model for both data generation and [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. Since OpenAI models don't share their internal "thinking traces," a Quen model (specifically the 30 billion parameter mixture-of-experts model) is used to generate data <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.

The Quen model can be run on platforms like RunPod using a one-click affiliate template <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. The setup involves:
*   Running a Docker image for VLM <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   Enabling reasoning and a reasoning parser to extract thinking tokens into a JSON format <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   Setting a maximum model length (e.g., 32,000 tokens) and hosting on a specific port (e.g., 8000) <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   Enabling automatic tool choice, allowing the LLM to decide when and which tool to call <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   Specifying a tool parser (e.g., Hermes) to extract tool calls from the LLM's string output into the expected JSON format for the OpenAI API <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

The server's endpoint (RunPod Pod ID and port) is used to interact with the LLM <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. A `truncate` argument is used to limit the length of tool responses (e.g., accessibility trees from browser navigation) to manage context length for the LLM <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Running the Agent and Collecting Traces
The agent is run using `uv sync` to ensure requirements are met <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
The MCP server starts, loading configured tools (e.g., 25 Playwright browser tools like navigate, switch tab) <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. For open-source models, keeping the number of tools between 25-50 is advised to avoid confusing the LLM with excessive context <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

Users provide inputs (e.g., "navigate to trellis.com and read out the top two lines") <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. The agent then:
1.  Sends the user message to the LLM <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
2.  The LLM processes, generates thinking tokens (saved, not displayed for brevity) <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
3.  The LLM decides to call a tool (e.g., `browser.navigate`), which requires user approval in this setup <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
4.  Upon approval, the browser pops up (if not in headless mode) <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
5.  An accessibility tree (text description of the page) is sent back to the LLM <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
6.  The LLM uses this information, along with its reasoning, to formulate a final answer <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

Logs are saved by default, containing `messages` (full conversation history) and `tools` (list of available tools) <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. These structured logs are essential for [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

### Curating High-Quality Traces
For [[finetuning_ai_models_for_better_performance | fine-tuning]], it's crucial to collect *good* traces <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. While the model might struggle with complex tasks (e.g., multi-step navigation, tab switching), methods to improve traces include:
*   **Manual Adjustment**: Modifying or combining user/assistant turns in the trace retrospectively <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.
*   **System Prompts**: Providing a system prompt that directly explains how to perform a task and which tools to call <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This prompt can be excluded from the final training data once a nice trace is generated, as the goal is clean training data <a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.

## Preparing and Pushing Data to Hugging Face Hub

Once high-quality traces are collected, they are pushed to the Hugging Face Hub to create a dataset for [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.

### Unrolling Data
A subtle but important technique is "unrolling" the data <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. For multi-turn conversations, this means creating multiple rows in the dataset: one for the full conversation, one for the first two turns, and one for just the first turn <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>. This effectively generates more training examples from a single multi-turn trace <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>. The Quen template, for instance, only includes reasoning from the most recent turn, making unrolling beneficial <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.

### Process
The `push to hub` function is used, requiring a repo ID and the `unroll` flag if desired <a class="yt-timestamp" data-t="00:18:58">[00:18:58]</a>. The user needs to be logged into Hugging Face with write permissions <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

The resulting dataset contains fields like `ID`, `timestamp`, `model`, `messages` (the full conversation history), and `tools` (the list of tools available) <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>. The `messages` content for each row includes system messages, tool definitions, user requests, assistant reasoning, tool calls, and tool responses, with reasoning content explicitly extracted due to the reasoning parser being enabled <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.

## Finetuning the Model

The [[finetuning_ai_models_for_better_performance | fine-tuning]] process uses an [[fine_tuning_with_unsloth_and_sesame_model | Unsloth notebook]] <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

### Model Loading and Setup
*   A smaller model (e.g., 4 billion parameter Quen model) can be used for [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
*   The `max sequence length` needs to accommodate the potentially long conversation traces (e.g., 32,000 tokens) <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.
*   The model is set up for training by applying [[fine_tuning_with_unsloth_and_sesame_model | Lora adapters]] (Low Rank Adapters) to specific parts of the model, such as attention modules and MLP layers <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. This means only a small percentage of parameters are trained, with the main weights remaining frozen <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>.
*   A `rank` (e.g., 32) and `rescaled Lora` (to adapt learning rate based on adapter size) are configured <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.

### Data Preparation
The collected dataset is loaded <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. The `messages` and `tools` are passed into the model's chat template, which converts them into a single, long string of text <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>. This string includes the system message, available tools, user messages, assistant responses, and tool calls, forming the `text` field used for training <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.

### Training Parameters
*   **Batch Size**: Often set to 1 due to VRAM limitations, though larger batch sizes (e.g., 32 with more VRAM) are ideal for smoother training <a class="yt-timestamp" data-t="00:31:36">[00:31:36]</a>.
*   **Epochs**: Typically one epoch for initial fine-tuning with small datasets <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.
*   **Learning Rate**: Fairly high for small models <a class="yt-timestamp" data-t="00:28:58">[00:28:58]</a>.
*   **Optimizer**: AtomW 8-bit optimizer is used to save VRAM <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>.
*   **Learning Rate Schedule**: Constant learning rate for simplicity <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

### Evaluation and Deployment
Before [[finetuning_ai_models_for_better_performance | fine-tuning]], a baseline inference run is performed to evaluate the model's performance without training <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a>. After training, inference is run again to observe improvements in tool calling capabilities <a class="yt-timestamp" data-t="00:33:37">[00:33:37]</a>.

The fine-tuned model and tokenizer can then be saved and pushed to the Hugging Face Hub (merged to 16 bits) <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. This allows users to set up an inference endpoint using their fine-tuned model by simply swapping its name in the RunPod template <a class="yt-timestamp" data-t="00:30:46">[00:30:46]</a>.

### Considerations for Improvement
*   **Data Quantity**: More data (hundreds of traces) is recommended for better [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>.
*   **Evaluation Set**: Using a dedicated evaluation set to track performance during training <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>.
*   **Logging**: Employing tools like TensorBoard for better training progress visualization <a class="yt-timestamp" data-t="00:31:16">[00:31:16]</a>.
*   **Reinforcement Learning (RL)**: While [[agent_evaluation_using_model_conduct_protocol_mcp | reinforcement learning]] (e.g., GRPO) can automate trace generation and reward-based systems, supervised [[finetuning_ai_models_for_better_performance | fine-tuning]] (SFT) on high-quality manual traces is highly beneficial as a starting point. SFT helps the model generate correct traces more frequently, speeding up subsequent RL <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>. For RL, defining rewards requires a dataset with verifiable correct answers, which involves systematically generating data with ground truth <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.

[[finetuning_and_production_stability_of_open_ai_models | Finetuning]] with a curated set of traces can lead to significant performance improvements, especially for narrow, common, and important use cases <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.