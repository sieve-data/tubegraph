---
title: Use of LLMs with browser navigation and other services
videoId: Nqb7JTx0Pqo
---

From: [[aidotengineer]] <br/> 

The Model Context Protocol (MCP) is a protocol designed to provide services to Large Language Models (LLMs), primarily enabling them to access and utilize various tools <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. This capability allows LLMs to interact with external systems and perform complex tasks beyond their inherent knowledge.

## How MCP Works

MCP functions as both a repository of information about tools and a service that executes these tools <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

1.  **Information Store**: MCP holds details that help the LLM understand how to make calls to the tools <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
2.  **Tool Execution**: When an LLM decides to make a tool call, the MCP tool service takes the action (e.g., navigating a webpage, processing a payment) <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
3.  **Response Return**: After executing the tool, MCP returns a response to the LLM, which includes details of the result or additional guidance <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>. This allows the LLM to loop back, make another tool call, or provide a text-based response <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Services and Tools

While the primary focus is on browser use, MCP supports various other services:

*   **Browser Navigation**: This is a key application, enabling an LLM to navigate through websites <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. When an LLM navigates to a page, an "accessibility tree" (a text description of the page) is returned to the LLM, allowing it to read the content <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Other Services**: MCPs exist for platforms like Stripe, GitHub, and Gmail <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. Users can substitute these into examples to explore different functionalities <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. Playwright, for instance, offers 25 tools for browser interaction, including navigation, switching tabs, and clicking links <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

### Limitations on Tool Count
For open-source models, it is generally recommended not to use more than 25 to 50 tools, as a larger number of tools can confuse the LLM due to excessive context <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. More capable models like Claude might handle up to 200 tools <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

## [[integration_of_llm_with_creative_tools | Integrating LLMs with MCP]]

To enable an LLM to utilize MCP tools, the language model is typically exposed as an OpenAI-style API endpoint <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This requires several points of integration and data translation:

1.  **MCP Tool Information to JSON**: Tool information from MCP services must be converted into lists of JSON tools, as expected by OpenAI endpoints <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This conversion happens when preparing tools for the LLM <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.
2.  **Tool Response Formatting**: The tool response received from MCP needs to be converted into a format the language model expects <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
3.  **Tool Call Extraction**: When the LLM calls a tool by emitting tokens or text, the system must detect and extract whether it wants to make a tool call <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. The text format for tool calls, such as the Hermes format for a Quen model, needs to be correctly parsed into JSON <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.

### Prompt Structure
The interaction with the LLM involves a specific prompt structure:

*   **System Message**: This part, often enclosed in `system start` and `system end` tags, describes to the LLM how to make tool calls, typically by passing JSON objects within XML tags like `<tool_code>` <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. It informs the LLM about available tools and the expected format for function calls <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **User Message**: The user's request (e.g., "navigate to trellis.com") is provided <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>.
*   **Assistant Response**: The assistant (LLM) responds, potentially by thinking and then deciding to call a tool (e.g., navigating to a URL) or providing a text-based answer if a task is completed <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

## Fine-tuning LLMs for Tool Use

To improve an LLM's performance with tool use, a process of fine-tuning using high-quality reasoning traces is employed <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

### Data Collection
High-quality MCP agent reasoning traces are generated and saved, including the tools used and multi-turn conversation histories <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. This data is crucial for fine-tuning.

*   **Model Consistency**: It's recommended to maintain consistency between the model used to generate the data and the model intended for fine-tuning <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>. OpenAI models typically do not share their thinking traces, making open-source models like Quen more suitable for data generation <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   **Reasoning Parsing**: When generating data, enabling reasoning and a reasoning parser ensures that `think` tokens from the model are detected and extracted into a JSON format within the response <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   **Trace Truncation**: Tool responses, especially from browser navigation (accessibility trees), can be very long <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>. Truncating these responses can manage context length, though it means the LLM might not see the full page content <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.
*   **Manual Adjustment**: Traces can be manually adjusted to clean up noise or guide the LLM if it doesn't follow desired actions <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>. A system prompt can be used during data generation to direct the LLM on tool calls, which can then be excluded from the final training data <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.
*   **Unrolling Data**: For multi-turn conversations, the data is "unrolled" into multiple rows. For example, three turns are expanded into three rows, providing more training data points <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. This is important because the Quen template typically only includes reasoning from the most recent turn <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

### Fine-tuning Process
Once data is collected, it is prepared for fine-tuning:

*   **Model Loading**: Models like the 4-billion parameter Quen model can be trained, with considerations for sequence length and GPU memory <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
*   **Applying Adapters**: Instead of training all parameters, low-rank adapters (Lora) are applied to specific parts of the model, such as attention modules and MLP layers <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. This makes fine-tuning more efficient and requires less VRAM <a class="yt-timestamp" data-t="00:27:39">[00:27:39]</a>.
*   **Data Formatting**: The collected messages and tools are templated into a single long string of text for the trainer <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.
*   **Training Parameters**: Training often uses a small batch size (e.g., one) due to VRAM limitations, making the training loss "jumpy" <a class="yt-timestamp" data-t="00:28:35">[00:28:35]</a>. Training for one epoch with a relatively high learning rate is common for small models <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. Only a small percentage of parameters (e.g., 1.62%) are trained, with the main weights frozen <a class="yt-timestamp" data-t="00:30:15">[00:30:15]</a>.
*   **Evaluation**: After fine-tuning, the model's performance is re-evaluated to see if the tool calling and reasoning capabilities have improved <a class="yt-timestamp" data-t="00:33:40">[00:33:40]</a>.

### Beyond Supervised Fine-Tuning
While the focus is on Supervised Fine-Tuning (SFT) using high-quality manual traces, [[benchmarking_llms_for_software_development | reinforcement learning]] (RL) methods like GRPO can be used later <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>. However, it is highly beneficial to perform SFT on high-quality traces first, as this helps the model avoid struggling and speeds up later RL training <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>. For RL, defining rewards requires a dataset with verifiable correct answers, which can be challenging to systematically generate <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>.

Even without moving to RL, significant [[future_of_creative_tools_with_mcp_and_llm | performance improvements]] can be achieved with a relatively small number of curated examples (e.g., 50-100 traces), especially for common or critical use cases <a class="yt-timestamp" data-t="00:34:48">[00:34:48]</a>.