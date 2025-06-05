---
title: Traces and logs for performance improvement
videoId: Nqb7JTx0Pqo
---

From: [[aidotengineer]] <br/> 

This article outlines how to generate, collect, and use high-quality traces and logs from Model Context Protocol (MCP) agent runs to [[finetuning_ai_models_for_better_performance | fine-tune]] and improve the performance of a language model <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. The materials for this process are available online in the Trellis Research AI Worlds Fair 2025 repository, specifically in the "MCP agent fine-tune" folder <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Understanding Model Context Protocol (MCP)

MCP (Model Context Protocol) is a protocol designed to provide services, primarily access to tools, to Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The workshop specifically focuses on browser use, allowing an LLM to navigate websites <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Other MCP services exist for platforms like Stripe, GitHub, and Gmail <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.

MCP performs several functions:
*   **Information Store**: It stores information about tools, helping the LLM understand how to make calls or use them <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Tool Execution**: The MCP tool service runs the tools. When an LLM decides to make a call, MCP executes the action (e.g., navigating to a page) and returns a response containing the result or guidance for the LLM <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

### LLM Integration and Tool Interaction

The language model is exposed as an OpenAI-style API endpoint, which is a common standard <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. Integrating this API endpoint requires specific translations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>:
1.  Converting tool information from MCP services into lists of JSON tools, as expected by OpenAI endpoints <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  Converting the tool response into a format the language model expects <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  Detecting and extracting tool calls from the LLM's emitted tokens or text, specifically in Hermes format for the Quen model <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

The prompt structure for the LLM includes a system message that describes how to make tool calls by passing JSONs within tool XML tags <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>. The LLM then uses this to respond, either by thinking and calling a tool or by providing a text-based response <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

## Data Collection: Generating High-Quality Traces and Logs

The data collection process involves running an agent to generate sample runs <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Setting up the Agent
1.  **Endpoint**: An OpenAI-style endpoint is required <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. For consistency between data generation and [[finetuning_ai_models_for_better_performance | fine-tuning]], a Quen type agent is used, specifically the 30 billion parameter mixture-of-experts model <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This model can be run on platforms like RunPod <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
2.  **Configuration**: The Docker image for VLM is run, enabling reasoning and a reasoning parser to extract thinking processes into a JSON format <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>. Automatic tool choice is enabled, allowing the LLM to decide which tool to call <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. A Hermes-specific tool parser is used to extract tool calls into the OpenAI API's expected JSON format <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. Port 8000 is exposed for serving the model <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
3.  **Truncation**: The `truncate` argument can be used to limit the length of tool responses, especially for browser accessibility trees, to avoid excessively long contexts for the LLM <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Running the Agent and Collecting Logs
The agent interacts with the user, taking inputs and generating responses. During this process, the agent's actions, thinking, and tool calls are logged <a class="yt-timestamp" data-t="00:09:35">[00:09:35]</a>.
*   The MCP server is started, loading configured tools (e.g., 25 Playwright browser tools) <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>.
*   User input prompts the LLM to think and decide on actions, such as navigating to a website <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   Tool calls are made by the LLM and require approval <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>. The browser pops up (unless in headless mode) to perform the action <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   Logs are saved, typically in two parts: `messages` (full conversation history including user requests, assistant thinking, and final answers) and `tools` (a list of available tools) <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. This structure is essential for [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

### Curating Traces
Not all traces will be perfect. Users can manually adjust traces by deleting or combining user turns to create a cleaner, more direct trace <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>. A system prompt can also be used to guide the model very directly during trace generation, which can then be excluded from the final training data <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The goal is to obtain nice, tidy traces for training data <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.

### Pushing Data to Hugging Face Hub
Collected traces (tools and conversations) are pushed to a Hugging Face dataset <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
*   **Unrolling Data**: To train on multiple turns, a subtle technique called "unrolling" is used. If a conversation has, for example, three back-and-forths, it's unrolled into three rows: one with all turns, one with the last two, and one with just the final turn. This effectively multiplies the training data <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>.
*   The unrolled data set will contain `ID`, `timestamp`, `model`, `messages`, and `tools` <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>. The `messages` field extracts reasoning content because the reasoning parser was enabled <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.

## Fine-tuning the Model

The collected and curated traces are then used to [[finetuning_ai_models_for_better_performance | fine-tune]] the LLM.

### Model Loading and Preparation
1.  **Model Selection**: A smaller model, like the 4 billion parameter Quen model, is chosen for [[finetuning_ai_models_for_better_performance | fine-tuning]] <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>. A larger sequence length (e.g., 32,000) is maintained <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>.
2.  **Benchmark**: Before [[finetuning_ai_models_for_better_performance | fine-tuning]], an initial run is performed to benchmark the model's performance without fine-tuning <a class="yt-timestamp" data-t="00:24:03">[00:24:03]</a>.
3.  **Data Loading**: The dataset from Hugging Face is loaded <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>.
4.  **Chat Template**: The `chat_template` takes the tools and messages and combines them into a single, long string of formatted text <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>. This string includes the system message, tools list, user message, assistant message, and tool calls <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>. The longest row length is checked to ensure it doesn't exceed the model's maximum length <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>.
5.  **LoRA Adapters**: The model is prepared for [[finetuning_ai_models_for_better_performance | fine-tuning]] by applying Low Rank Adapters (LoRA) to specific parts of the model (attention modules and MLP layers) <a class="yt-timestamp" data-t="00:27:37">[00:27:37]</a>. This trains only a small percentage of parameters, keeping the main weights frozen <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>.

### Training the Model
*   The model is trained using the prepared dataset <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>.
*   A batch size of one is used due to VRAM limitations, which can make the training loss jumpy <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.
*   Training typically runs for one epoch <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.
*   A high learning rate and an AtomW 8-bit optimizer are used <a class="yt-timestamp" data-t="00:28:58">[00:28:58]</a>.
*   [[finetuning_ai_models_for_better_performance | Supervised fine-tuning]] on high-quality traces is recommended even before considering reinforcement learning (RL) methods like GRPO, as it significantly speeds up subsequent RL training <a class="yt-timestamp" data-t="00:32:20">[00:32:20]</a>.

### Post-Training and Evaluation
After training, the model's performance is re-evaluated <a class="yt-timestamp" data-t="00:33:34">[00:33:34]</a>. Even with limited data, the fine-tuned model should show improved capability in calling tools correctly <a class="yt-timestamp" data-t="00:34:03">[00:34:03]</a>. For comprehensive evaluation, a more elaborate setup with an evaluation set, more data (hundreds of traces), and logging with TensorBoard is recommended <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>.

The fine-tuned model and tokenizer can be saved and optionally pushed to Hugging Face Hub, where they can be merged to 16 bits and used to update an inference endpoint <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>.

This process, even with a small number of carefully curated examples (e.g., 50-100), can lead to significant improvements in performance for specific use cases <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.