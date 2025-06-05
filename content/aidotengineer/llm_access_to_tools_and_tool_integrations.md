---
title: LLM access to tools and tool integrations
videoId: Nqb7JTx0Pqo
---

From: [[aidotengineer]] <br/> 

Large Language Models (LLMs) can be significantly augmented by providing them with access to external tools, enabling them to perform actions beyond text generation, such as browsing websites or interacting with APIs <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This capability is crucial for building more sophisticated AI agents that can interact with the real world <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

## Model Context Protocol (MCP)

The Model Context Protocol (MCP) is a framework designed to provide services, primarily access to tools, to LLMs <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. MCP acts as both a store of information about tools and a service that runs the tools <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. When an LLM decides to use a tool, the MCP tool service takes the action (e.g., navigating a page) and returns a response containing the result or guidance for the LLM <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

Examples of MCP-supported tools include:
*   Browser use (navigating websites) <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>
*   Stripe <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   GitHub <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>
*   Gmail <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>

### Integration Points for LLM Tool Access

To enable an LLM to access tools via MCP, the language model is typically exposed as an API endpoint, often in the format of an OpenAI endpoint <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. This integration requires several key translations and considerations:
1.  **Tool Information Conversion**: Tool information from MCP services must be converted into lists of JSON tools, as expected by OpenAI endpoints <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
2.  **Tool Response Formatting**: The tool response must be converted into a format the LLM expects <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  **Tool Call Detection and Extraction**: When the LLM emits tokens or text indicating a tool call, this intention must be detected and extracted, often in a specific format like Hermes <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. This involves parsing the LLM's output, which typically includes XML tags containing JSON for the tool call <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

> [!example] Prompt Structure for Tool Calls
> A typical prompt structure sent to an LLM for tool calling includes:
> *   A system message describing how to make tool calls (e.g., passing JSON within `<tool_code>` XML tags) <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
> *   Information about available tools (e.g., the browser tool) <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
> *   User messages (e.g., "navigate to trellis.com") <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
> *   The assistant's response, which may include thinking steps, a tool call (e.g., navigating with the browser), or a text-based response <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.

## Data Collection for Fine-tuning

To improve the performance of an LLM in tool-use scenarios, [[evaluation_of_llms_using_realworld_scenarios | fine-tuning]] is performed using "traces" or logs from high-quality agent runs <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. These traces capture the full multi-turn interaction, including the LLM's reasoning and tool calls.

### Running an MCP Agent for Data Collection
An agent configured with MCP servers can generate these traces <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. The process involves:
1.  **Setting up an OpenAI-style endpoint**: For models like Quen, enabling features like reasoning and a reasoning parser helps in extracting the LLM's thought process <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>. The `--enable-tool-choice` argument allows the LLM to decide which tool to call <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
2.  **Configuring MCP Servers**: The agent loads tools from configured MCP servers <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>. For a browser, Playwright offers about 25 tools (e.g., navigate, switch tab, navigate to link) <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.
3.  **Interacting with the Agent**: Users provide prompts, and the agent responds by thinking, making tool calls, and providing text responses <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>. The browser itself can be run in non-headless mode to observe its actions <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
4.  **Logging Traces**: The agent logs runs with two main parts: a `messages` part (full conversation history) and a `tools` part (list of available tools) <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
5.  **Curating Traces**: Not all traces will be optimal. Manual adjustment of traces is possible to improve their quality for training <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. This can involve directly guiding the model with system prompts during collection, which can then be excluded from the training data <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

### Preparing Data for Fine-tuning
Once high-quality traces are collected, they are pushed to a dataset, often on platforms like Hugging Face Hub <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. A key step here is "unrolling the data" <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. If a conversation has multiple turns, it's unrolled into multiple rows in the dataset, each representing a full conversation up to that turn <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>. This approach generates more training data and ensures the model learns from intermediate reasoning steps <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.

## Fine-tuning the LLM for Tool Use

[[augmented_llm_architectures | Fine-tuning]] is performed to improve an LLM's ability to utilize tools <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>. The process typically involves:
1.  **Model Loading**: A base model (e.g., a 4-billion parameter Quen model) is loaded <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
2.  **Applying LoRA Adapters**: Instead of training all model parameters, low-rank adapters (LoRA) are applied to specific parts like attention modules and MLP layers <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. This makes fine-tuning more efficient and requires less VRAM <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>.
3.  **Data Preparation**: The collected traces (messages and tools) are passed into the model's chat template, which formats them into a single long string suitable for training <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>. This formatted string includes system messages, available tools, user prompts, assistant thinking, and tool calls/responses <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>.
4.  **Training**: The model is trained on this prepared dataset. Training parameters like batch size, learning rate, and optimizer are configured <a class="yt-timestamp" data-t="00:28:10">[00:28:10]</a>. For small datasets, batch sizes might be limited, leading to jumpy loss <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.
5.  **Evaluation**: After fine-tuning, the model's performance is re-evaluated to see if its ability to call tools has improved <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>. Ideally, a separate evaluation set and logging with tools like TensorBoard would be used for a more robust assessment <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>.
6.  **Saving and Deploying**: The fine-tuned model and tokenizer can be saved and pushed to a model hub. The adapters can be merged with the base model to create a new inference endpoint <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>.

### Relation to Reinforcement Learning
While reinforcement learning (RL) techniques like GRPO can automate trace generation and reward-based systems for LLMs, it's beneficial to first perform supervised fine-tuning (SFT) on high-quality, manually curated traces <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>. An LLM that hasn't undergone SFT for a specific domain might struggle to generate sufficient successful traces for effective RL <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>. For RL, defining verifiable rewards requires systematically generated data with ground truths <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>.

> [!info] Further Resources
> All materials for this workshop are available in the Trellis Research AI Worlds Fair 2025 repo, specifically in the `MCP agent fine-tune` folder <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. More detailed videos on setting up and creating custom MCP servers are available on the Trellis Research YouTube channel <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.