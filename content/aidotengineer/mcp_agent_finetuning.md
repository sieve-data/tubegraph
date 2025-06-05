---
title: MCP agent finetuning
videoId: Nqb7JTx0Pqo
---

From: [[aidotengineer]] <br/> 

This article provides a guide to [[finetuning_language_models_with_mcp | finetuning language models with the Model Context Protocol (MCP)]], focusing on improving an agent's performance by leveraging high-quality reasoning traces and tool interactions <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. The process involves generating agent reasoning traces, saving multi-turn conversations and tool data, [[finetuning_ai_models_for_better_performance | finetuning a model]] (e.g., Quen 3), and evaluating the improved performance <a class="yt-timestamp" data-t="00:26:00">[00:26:00]</a>.

## Introduction to MCP

[[introduction_to_model_context_protocol_mcp | MCP (Model Context Protocol)]] is a protocol designed to provide services to Large Language Models (LLMs), primarily granting them access to tools <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. While the focus here is on browser use (LLMs navigating websites), MCPs exist for other services like Stripe, GitHub, and Gmail <a class="yt-timestamp" data-t="01:29:00">[01:29:00]</a>.

MCP performs several key functions <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>:
*   **Information Store**: It stores information about tools, helping the LLM understand how to make calls to them <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>.
*   **Tool Execution**: The [[technical_structure_and_features_of_mcp | MCP tool service]] runs the tools itself <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>.
*   **Response Return**: After an action, it returns a response containing the result or guidance for the LLM, enabling the LLM to make further tool calls or provide a text-based response <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.

## Integrating AI with Applications using MCP

To enable an LLM to interact with MCP services, it's typically exposed as an OpenAI-style API endpoint <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. This integration requires several points of translation <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>:
1.  **Tool Information Conversion**: MCP tool information must be converted into JSON lists, as expected by OpenAI endpoints <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.
2.  **Tool Response Formatting**: Tool responses need to be converted into a format the language model expects <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>.
3.  **Tool Call Detection**: When the LLM emits tokens or text to call a tool, the system must detect and extract this call, typically in a specific format like Hermes <a class="yt-timestamp" data-t="03:21:00">[03:21:00]</a>.

### Prompt Structure and Tool Calls

The interaction with the LLM is often managed through a specific prompt structure <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. A pseudo-prompt typically includes <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>:
*   **System Message**: Describes how the LLM should make tool calls (e.g., by passing JSONs within `<tool>` XML tags) <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
*   **User Message**: The initial query or instruction from the user <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.
*   **Assistant Response**: The LLM's response, which might involve thinking (generating "think tokens") and then deciding to call a tool or provide a text-based answer <a class="yt-timestamp" data-t="04:38:00">[04:38:00]</a>.

## [[finetuning_language_models_with_mcp | Finetuning Language Models with MCP]]

The process of [[finetuning_language_models_with_mcp | finetuning language models with MCP]] involves several stages, from data collection to model training and evaluation.

### 1. Data Collection

The first step is to generate high-quality traces from an MCP agent <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
*   **Endpoint Setup**: An OpenAI-style endpoint is required. For data generation, it's recommended to use a model that shares its reasoning traces, such as a Quen model (e.g., the 30B parameter Quen 3 model), as OpenAI models do not <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.
    *   This can be run on services like RunPod using a one-click affiliate template <a class="yt-timestamp" data-t="06:22:00">[06:22:00]</a>. Key configurations include enabling reasoning and a reasoning parser to extract thinking processes into JSON, setting max model length, and enabling automatic tool choice <a class="yt-timestamp" data-t="06:52:00">[06:52:00]</a>.
    *   The tool parser needs to be specified, such as the Hermes format, to extract tool calls into JSON <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.
*   **Running the Agent**: The agent interacts with MCP servers, which can be configured to load various tools (e.g., Playwright offers 25 browser-related tools like navigate, switch tab, etc.) <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>. For open-source models, it's generally recommended to use 25-50 tools to avoid confusion <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>.
*   **Trace Logging**: Agent runs generate logs with two parts: `messages` (full conversation history) and `tools` (list of available tools) <a class="yt-timestamp" data-t="12:06:00">[12:06:00]</a>. These traces are crucial for fine-tuning <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>.
*   **Trace Cleaning/Adjustment**: If an agent's trace isn't ideal, it can be manually adjusted (e.g., deleting user turns, combining sections) or guided with a system prompt during generation to produce cleaner traces <a class="yt-timestamp" data-t="15:12:00">[15:12:00]</a>. The goal is to obtain high-quality traces for training data <a class="yt-timestamp" data-t="16:23:00">[16:23:00]</a>.

### 2. Data Preparation for Fine-tuning

After collecting traces, the data needs to be prepared for training <a class="yt-timestamp" data-t="17:48:00">[17:48:00]</a>.
*   **Push to Hub**: Traces (tools and conversations) are pushed to a dataset on Hugging Face Hub <a class="yt-timestamp" data-t="17:51:00">[17:51:00]</a>.
*   **Unrolling Data**: For multi-turn conversations, the data is "unrolled" into multiple rows. For example, a three-turn conversation becomes three rows, allowing the model to train on different lengths of conversational context <a class="yt-timestamp" data-t="18:11:00">[18:11:00]</a>. This is particularly useful because the Quen template only includes reasoning from the most recent turn <a class="yt-timestamp" data-t="18:34:00">[18:34:00]</a>.
*   **Chat Template**: The `messages` and `tools` data are passed into a chat template, which converts them into a single long string of text, including system messages, tool descriptions, user messages, assistant responses, and tool calls <a class="yt-timestamp" data-t="23:40:00">[23:40:00]</a>.

### 3. Fine-tuning the Model

[[finetuning_ai_models_for_better_performance | Finetuning AI models for better performance]] involves loading the model, preparing it for training, and running the training process.
*   **Model Loading**: A smaller model (e.g., 4B parameter Quen model) is loaded for fine-tuning. Max sequence length should be set appropriately (e.g., 32,000) <a class="yt-timestamp" data-t="23:16:00">[23:16:00]</a>.
*   **Applying LoRA Adapters**: To save VRAM and train efficiently, LoRA (Low Rank Adapters) are applied to specific parts of the model (e.g., attention modules, MLP layers). This means only a small percentage of parameters are trained, while the main weights remain frozen <a class="yt-timestamp" data-t="23:50:00">[23:50:00]</a>.
*   **Training Parameters**:
    *   **Batch Size**: Often set to one due to VRAM limitations, though larger batch sizes (e.g., 32) are ideal for smoother training <a class="yt-timestamp" data-t="28:34:00">[28:34:00]</a>.
    *   **Epochs**: Often trained for a single epoch with a small dataset <a class="yt-timestamp" data-t="28:48:00">[28:48:00]</a>.
    *   **Learning Rate**: Relatively high for small models <a class="yt-timestamp" data-t="28:58:00">[28:58:00]</a>.
    *   **Optimizer**: AtomW 8-bit optimizer can be used to save VRAM <a class="yt-timestamp" data-t="29:03:00">[29:03:00]</a>.
*   **Manual Traces vs. RL**: It's highly recommended to start with supervised fine-tuning (SFT) using curated manual traces before considering reinforcement learning (RL) methods like GRPO. High-quality SFT data can significantly speed up subsequent RL training by ensuring the model generates useful traces early on <a class="yt-timestamp" data-t="32:00:00">[32:00:00]</a>.

### 4. Evaluation and Deployment

*   **Pre- and Post-Finetuning Inference**: Run inference on the model before and after fine-tuning to observe performance changes, especially on multi-step tasks where smaller, untrained models typically struggle <a class="yt-timestamp" data-t="25:54:00">[25:54:00]</a>.
*   **Model Saving and Pushing**: After training, the fine-tuned model and tokenizer can be saved and pushed to Hugging Face Hub, optionally merged to 16 bits <a class="yt-timestamp" data-t="30:30:00">[30:30:00]</a>. This allows direct deployment of the fine-tuned model as an inference endpoint by simply updating the model name in the RunPod configuration <a class="yt-timestamp" data-t="30:46:00">[30:46:00]</a>.
*   **Advanced Evaluation**: For more robust evaluation, a dedicated evaluation set (hundreds of traces), and logging with TensorBoard are recommended <a class="yt-timestamp" data-t="31:05:00">[31:05:00]</a>.

### Resources

All materials for this workshop are available online in the Trellis Research AI Worlds Fair 2025 GitHub repository, specifically in the `MCP agent fine-tune` folder <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>. Further details on [[technical_structure_and_features_of_mcp | setting up custom MCP servers]] can be found in other Trellis Research YouTube videos <a class="yt-timestamp" data-t="35:11:00">[35:11:00]</a>.