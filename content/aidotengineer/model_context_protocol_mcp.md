---
title: Model context protocol MCP
videoId: Nqb7JTx0Pqo
---

From: [[aidotengineer]] <br/> 

The [[Model context protocol mCP overview | Model Context Protocol (MCP)]] is a standardized approach designed to enable Large Language Models (LLMs) to access and utilize external tools and services <a class="yt-timestamp" data-t="01:20:23">[01:20:23]</a>. It acts as a bridge, allowing LLMs to extend their capabilities beyond pure text generation by interacting with the broader digital environment <a class="yt-timestamp" data-t="01:04:27">[01:04:27]</a>.

## Core Functionality
MCP serves two primary functions:
*   **Tool Information Store** It maintains a repository of information about available tools, detailing how an LLM can make calls to these tools and utilize them <a class="yt-timestamp" data-t="01:47:27">[01:47:27]</a>.
*   **Tool Service Runner** The MCP tool service actively runs the tools. When an LLM decides to perform an action through a tool, MCP executes that action and returns a response containing the result or additional guidance for the LLM <a class="yt-timestamp" data-t="01:57:27">[01:57:27]</a>. This allows the LLM to either make further tool calls or generate a text-based response <a class="yt-timestamp" data-t="02:14:27">[02:14:27]</a>.

### Examples of Tools
MCP can facilitate access to a wide array of tools and services, including:
*   Browser navigation <a class="yt-timestamp" data-t="01:26:28">[01:26:28]</a>
*   Stripe <a class="yt-timestamp" data-t="01:31:27">[01:31:27]</a>
*   GitHub <a class="yt-timestamp" data-t="01:32:27">[01:32:27]</a>
*   Gmail <a class="yt-timestamp" data-t="01:33:27">[01:33:27]</a>

## Integration with LLMs
To integrate with LLMs, particularly those exposed as an OpenAI-style API endpoint, several translation steps are necessary <a class="yt-timestamp" data-t="02:29:27">[02:29:27]</a>:
1.  **Tool Information Conversion** Tool information received from MCP services must be converted into JSON lists, as this is the format expected by OpenAI endpoints <a class="yt-timestamp" data-t="03:02:27">[03:02:27]</a>.
2.  **Tool Response Formatting** The response from a tool call needs to be converted into a format that the LLM understands and expects <a class="yt-timestamp" data-t="03:11:27">[03:11:27]</a>.
3.  **Tool Call Extraction** When the LLM emits tokens or text, the system must detect and extract if it intends to make a tool call. For example, a Quen model might emit tool calls in a specific "Hermes format" within XML tags, which then needs to be parsed into JSON <a class="yt-timestamp" data-t="03:21:27">[03:21:27]</a>.

## Agent Fine-Tuning with MCP
The [[Model context protocol and AI integration | Model Context Protocol]] plays a crucial role in the fine-tuning of [[Development and adoption of MCP | agent-based systems]] <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The process involves:

### Generating Traces
*   Running an agent that uses [[mCPs Role in Augmented LLM Systems | MCP servers]] to access tools <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
*   Collecting "traces" or logs from high-quality runs of the agent <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>. These traces capture the interaction between the LLM, the tools, and the full conversation history <a class="yt-timestamp" data-t="12:12:06">[12:12:06]</a>.
*   Traces include the tools used and the multi-turn conversations <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.
*   For models like Quen, reasoning tokens are parsed separately and saved in the traces <a class="yt-timestamp" data-t="06:52:27">[06:52:27]</a>.

### Data Preparation for Fine-tuning
*   Traces are logged with two parts: messages and tools <a class="yt-timestamp" data-t="12:12:06">[12:12:06]</a>.
*   **Unrolling the data:** For multi-turn conversations (e.g., three back-and-forths), the data is "unrolled" into multiple rows, allowing training on each turn as a distinct example <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>. This provides more training data from a single interaction <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>.
*   The raw messages and tools are templated into a single long string for training <a class="yt-timestamp" data-t="25:12:00">[25:12:00]</a>.

### Fine-Tuning the Model
*   The collected traces are used to fine-tune and improve the performance of the LLM <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>.
*   This typically involves training adapters, such as Low-Rank Adapters (LoRA), on specific parts of the model <a class="yt-timestamp" data-t="23:50:00">[23:50:00]</a>.
*   Fine-tuning with even a small number of high-quality traces (e.g., 50-100) can lead to significant performance improvements, especially for specific, common, or important use cases <a class="yt-timestamp" data-t="34:48:00">[34:48:00]</a>.
*   Supervised fine-tuning (SFT) on curated traces is beneficial even if reinforcement learning (RL) is planned later, as it provides a strong starting point and speeds up training <a class="yt-timestamp" data-t="32:23:00">[32:23:00]</a>.

## Prompt Structure for MCP Interaction
A typical prompt structure for an LLM interacting via MCP includes <a class="yt-timestamp" data-t="03:46:27">[03:46:27]</a>:
*   **System Message**: This initial message instructs the LLM on how to make tool calls, typically by passing JSON objects within specific XML tags (e.g., `<tool_code>`...`</tool_code>`) <a class="yt-timestamp" data-t="03:56:27">[03:56:27]</a>. It also informs the LLM about the available tools (e.g., browser) <a class="yt-timestamp" data-t="04:15:27">[04:15:27]</a>.
*   **User Message**: The user's input or request to the agent (e.g., "navigate to trellis.com and read out the top two lines") <a class="yt-timestamp" data-t="04:33:27">[04:33:27]</a>.
*   **Assistant Response**: The LLM's response, which may involve internal "thinking" (not always displayed), followed by a decision to call a tool or provide a text-based answer <a class="yt-timestamp" data-t="04:38:27">[04:38:27]</a>.
*   **Tool Response**: The output from the tool, such as an accessibility tree (a text description of a webpage) from a browser navigation tool <a class="yt-timestamp" data-t="08:51:27">[08:51:27]</a>. This response can be truncated if very long to manage context window limitations <a class="yt-timestamp" data-t="09:09:00">[09:09:00]</a>.

While many tools might be available (e.g., Playwright offers 25 browser tools like navigate, switch tab, click), for open-source models, it's generally recommended to limit the number of tools (e.g., 25-50) to prevent the LLM from becoming confused by excessive context <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>.