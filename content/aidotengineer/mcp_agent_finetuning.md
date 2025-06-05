---
title: MCP agent finetuning
videoId: Nqb7JTx0Pqo
---

From: [[aidotengineer]] <br/> 

[[mcp_agent_finetuning | MCP agent fine-tuning]] is a workshop topic that focuses on running an agent with access to tools via [[model_context_protocol_mcp | MCP]] servers, taking traces or logs from high-quality runs, and using them to fine-tune and improve a model's performance <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. By the end of such a workshop, participants should be able to generate high-quality [[model_context_protocol_mcp | MCP]] agent reasoning traces, save tools and multi-turn traces, fine-tune models like Quen 3, and evaluate the performance improvement <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. All materials for this process are available online in the Trellis Research AI Worlds Fair 2025 repository, specifically in the `MCP agent fine-tune` folder <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

## Introduction to [[model_context_protocol_mcp | Model Context Protocol (MCP)]]

[[model_context_protocol_mcp | MCP]], or [[model_context_protocol_mcp | Model Context Protocol]], is a protocol designed for providing services, primarily access to tools, to Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>, <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

### How [[model_context_protocol_mcp | MCP]] Works
[[model_context_protocol_mcp | MCP]] performs several key functions <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>:
*   **Information Storage**: It stores information about tools, which helps the LLM understand how to make calls to or use them <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Tool Execution**: The [[model_context_protocol_mcp | MCP]] tool service also runs the tools. When an LLM decides to make a call, the [[model_context_protocol_mcp | MCP]] service executes the action (e.g., adding numbers, navigating a page) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Response Return**: It then returns a response containing details of the result or helpful guidance for the LLM, allowing the LLM to loop back for another tool call or provide a text-based response <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

For example, a common tool is browser use, enabling an LLM to navigate websites. Other [[model_context_protocol_mcp | MCP]]s exist for services like Stripe, GitHub, and Gmail <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

### API Integration
To facilitate interaction, the language model is exposed as an API endpoint, typically in an OpenAI-compatible format <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>. This integration requires specific conversions and translations <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>:
1.  **Tool Information Conversion**: Tool information from [[model_context_protocol_mcp | MCP]] services must be converted into lists of JSON tools, as expected by OpenAI endpoints <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  **Tool Response Formatting**: The tool response needs to be converted into a format the language model expects <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  **Tool Call Detection**: When the language model calls a tool by emitting tokens or text, the system must detect and extract the tool call, often in a specific format like Hermes, even if using a different model like Quen <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Prompt Structure
A typical prompt sent to the LLM begins with a system message, describing how to make tool calls (e.g., by passing JSONs within `<tool>` XML tags) <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. The LLM is informed about available tools and the required format for function calls (e.g., JSON inside `<tool_call>` tags) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. Following the system message, a user message initiates a task (e.g., "navigate to trellis.com"). The assistant then responds, potentially by thinking and calling a tool (e.g., navigating a browser) or by providing a text-based answer if the task is complete <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.

## Data Collection for Fine-tuning

The process starts with data collection, where the agent is run to generate sample traces <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Setting Up the Endpoint
An OpenAI-style endpoint is required <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. For generating traces, it is recommended to use a model consistent with the one intended for fine-tuning, such as a Quen type agent, because OpenAI models do not share their thinking traces <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.

A 30 billion parameter Quen model (mixture of experts) is suggested, which can be run on services like RunPod using a one-click affiliate template <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

Key configurations for the endpoint include <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>:
*   **Docker Image**: Using a Docker image for VLM.
*   **Model**: Running the Quen model.
*   **Reasoning**: Enabling reasoning and a reasoning parser to detect and extract "think tokens" as JSON <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Max Model Length**: Setting the max model length to 32,000.
*   **Port**: Hosting on port 8,000, which needs to be exposed <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.
*   **Automatic Tool Choice**: Enabling the LLM to decide whether and which tool to call <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   **Tool Parser**: Specifying how to extract the tool call into JSON format (e.g., Hermes format) <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Running the Agent and Collecting Traces
The agent is run using the specified model and base URL (containing the pod ID and port number) <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>. A `truncate` argument can be used to limit the length of tool responses, such as accessibility trees returned by browser navigation tools <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

The agent starts by loading configured [[model_context_protocol_mcp | MCP]] servers and their tools (e.g., Playwright offers 25 browser tools like navigate, resize, etc.) <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. For open-source models, it's generally recommended to use no more than 25-50 tools to avoid confusing the LLM <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

When the agent runs a task (e.g., "navigate to trellis.com and read out the top two lines"), the user message goes to the LLM, which thinks, generates thinking tokens (not shown for brevity), and then proposes a tool call <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. After user approval, a browser may pop up (if not in headless mode), and the accessibility structure of the page is sent to the LLM for processing <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

Logs are generated by default when the agent runs, containing two parts: `messages` (full conversation history) and `tools` (a list of available tools) <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. These logs are crucial for fine-tuning <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

### Curating Traces
For fine-tuning, the goal is to obtain nice, tidy traces <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.
*   **Manual Adjustment**: Traces can be manually adjusted if the agent doesn't follow the desired path, or parts of user and assistant turns can be combined <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.
*   **System Prompts**: A system prompt can be passed to guide the LLM more directly on how to perform a task and which tools to call, improving trace quality without needing to include the system prompt in the final training data <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

### Pushing Data to Hugging Face Hub
Collected traces are pushed to Hugging Face Hub to create a dataset for fine-tuning, which includes both tools and conversations <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.

A "subtle point" is `unrolling the data` <a class="yt-timestamp" data-t="00:18:11">[00:18:11]</a>. For multi-turn conversations, the data is unrolled into multiple rows (e.g., three back-and-forths unroll into three rows: one with all turns, one with two, and one with just the first turn) <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. This ensures that the model trains on intermediate reasoning steps, as the Quen template typically only includes reasoning from the most recent turn <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

## Fine-tuning the Model

After data collection, the next step is fine-tuning the LLM using the curated traces <a class="yt-timestamp" data-t="00:22:45">[00:22:45]</a>.

### Model Loading and Setup
A smaller model, such as a 4 billion parameter Quen model, can be trained, though larger models might yield better performance <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>. The max sequence length needs to be sufficiently large (e.g., 32,000) <a class="yt-timestamp" data-t="00:23:21">[00:23:21]</a>. Training can be done in full precision (16 bits) <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>.

For training, only adapters are trained, not all parameters. These are Low Rank Adapters (Lora) applied to attention modules and MLP layers <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. A rank of 32 for adapter matrices is used, and `rescaled Laura` adapts the learning rate based on adapter size <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>.

### Data Preparation for Training
The dataset loaded from Hugging Face Hub, typically consisting of nine rows after unrolling <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>, is used. The `chat template` converts the tools and messages into a single long string, which becomes the input `text` field for training <a class="yt-timestamp" data-t="00:24:34">[00:24:34]</a>. This formatted string includes the system message, tools available, user messages, assistant messages, and tool calls <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.

### Training Parameters
Training is performed with a batch size of one, often due to VRAM limitations, which can lead to a jumpy training loss <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>. A single epoch of training is typical for small datasets <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. Other parameters include:
*   **Learning Rate**: Fairly high for a small model.
*   **Optimizer**: AtomW 8-bit optimizer to save VRAM.
*   **Learning Rate Schedule**: Constant learning rate <a class="yt-timestamp" data-t="00:28:58">[00:28:58]</a>.

During training, only a small percentage of parameters (e.g., 1.62%) are trained through adapters, while the main weights remain frozen <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>.

### Evaluation and Improvements
While a more advanced implementation would include an evaluation set (e.g., a few hundred traces, splitting some for eval) and logging with TensorBoard, this simplified process focuses on demonstrating the principle <a class="yt-timestamp" data-t="00:31:04">[00:31:04]</a>.

#### Reinforcement Learning (RL) Considerations
While not the primary focus, [[mcps_role_in_augmented_llm_systems | reinforcement learning]] (RL) can automate trace generation or use reward-based systems <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. However, it's recommended to start with manual, curated traces via Supervised Fine-Tuning (SFT) because it significantly speeds up subsequent RL training <a class="yt-timestamp" data-t="00:32:11">[00:32:11]</a>. Without initial SFT, a model might struggle to generate correct answers and thus rarely receive positive rewards <a class="yt-timestamp" data-t="00:32:30">[00:32:30]</a>. For GRPO (Generalized Policy Optimization), rewards must be defined, requiring a dataset with verifiable answers (e.g., specific text on obscure websites) <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.

### Saving and Pushing the Fine-tuned Model
After training, the model and tokenizer can be saved <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. The model can also be pushed to Hugging Face Hub, optionally merged to 16 bits <a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>. The fine-tuned model's name can then replace the base model in the inference endpoint configuration, creating a ready-to-use endpoint <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>.

## Conclusion
[[mcp_agent_finetuning | MCP agent fine-tuning]] allows for significant performance improvements, especially for specific, narrow use cases, even with a relatively small number of curated examples (e.g., 50-100 traces) <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>.

Further details on [[model_context_protocol_mcp | MCP]] and custom server setup can be found in related Trellis Research YouTube videos <a class="yt-timestamp" data-t="00:35:13">[00:35:13]</a>.