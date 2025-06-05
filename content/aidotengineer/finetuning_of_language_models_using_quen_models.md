---
title: Finetuning of language models using Quen models
videoId: Nqb7JTx0Pqo
---

From: [[aidotengineer]] <br/> 

The process of [[finetuning_ai_models_for_specific_use_cases | fine-tuning]] a language model (LLM) involves taking traces or logs from high-quality runs and using them to improve the model's performance <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. This workshop specifically demonstrates how to [[finetuning_ai_models_for_specific_use_cases | fine-tune]] a Qwen model <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>.

## Why Qwen Models for Finetuning?
It is recommended to maintain consistency between the model used to generate data and the model intended for [[finetuning_ai_models_for_specific_use_cases | fine-tuning]] <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>. While a stronger model could, in principle, be used to generate data, OpenAI models do not share their [[large_language_model_interpretability | thinking traces]] <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. Qwen models, however, can share their [[large_language_model_interpretability | reasoning traces]], making them suitable for this purpose <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

Specific Qwen models mentioned include:
*   Qwen 3 <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>
*   The 30 billion parameter Qwen model (with 3 billion activated parameters, a mixture of experts model) for data generation <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   The 4 billion parameter Qwen model for [[finetuning_ai_models_for_specific_use_cases | training]] <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.

## Data Collection for Finetuning
The first step in [[evaluations_and_finetuning_in_ai_development | finetuning]] is to generate high-quality [[large_language_model_interpretability | reasoning traces]] <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. These traces include the tools used and the multi-turn conversation history <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

### Setting up the Qwen Endpoint
To collect data, Qwen models are exposed as OpenAI-style endpoints <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This involves:
*   Running a Docker image for VLM with the Qwen model <a class="yt-timestamp" data-t="00:06:47">[00:06:47]</a>.
*   Enabling [[large_language_model_interpretability | reasoning]] and a [[large_language_model_interpretability | reasoning parser]] to extract thinking tokens into a JSON format <a class="yt-timestamp" data-t="00:06:52">[00:06:52]</a>.
*   Setting `max_model_length` to 32,000 <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   Enabling automatic tool choice for the LLM <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>.
*   Specifying a tool parser (e.g., Hermes format) to extract tool calls from the LLM's text output into JSON <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This addresses the conversion from language model string to OpenAI API-expected JSON format <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   Exposing port 8000 for the server <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

### Agent Operation and Trace Generation
An agent is run with the Qwen model endpoint <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   The agent connects to [[switching_between_language_models_with_unified_interfaces | Model Context Protocol (MCP)]] servers, which provide access to tools like a browser <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.
*   MCP stores information on tools (how the LLM can make calls) and runs the tools, returning responses to the LLM <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Tool information from MCP services must be converted into JSON lists for OpenAI endpoints <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Similarly, tool responses must be converted into a format the LLM expects <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   When the LLM makes a tool call by emitting text, the system detects and extracts this call <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   The tool response, such as an accessibility tree from browser use, can be very long, so it is often truncated for brevity during data collection <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   The LLM's prompt includes a system message instructing it on how to make tool calls (e.g., by passing JSONs within XML tags) <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.
*   Traces are logged by default, including `messages` (full conversation history) and `tools` (list of available tools) <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>. The [[large_language_model_interpretability | reasoning content]] is extracted separately <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.
*   Users can manually adjust traces for better quality or pass a system prompt to guide the model <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. The goal is to generate clean traces for [[finetuning_ai_models_for_specific_use_cases | training data]] <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>.

### Data Preparation for Finetuning
*   **Unrolling Data:** For multi-turn conversations, the data is "unrolled" into multiple rows. For example, a three-turn conversation yields three rows, providing more training data from a single interaction <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. This is important because the Qwen template only includes reasoning from the most recent turn <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.
*   **Pushing to Hugging Face Hub:** The collected tools and messages are pushed to a dataset on Hugging Face Hub <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>. The dataset typically contains columns for `ID`, `timestamp`, `model`, `messages`, and `tools` <a class="yt-timestamp" data-t="00:19:33">[00:19:33]</a>.

## Finetuning Process
The actual [[finetuning_ai_models_for_specific_use_cases | finetuning]] is performed in a notebook, often based on Unslaught's [[development_of_qwen_large_language_models | Qwen fine-tuning]] notebook <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

1.  **Load Model:** A smaller Qwen model, such as the 4 billion parameter version, is loaded <a class="yt-timestamp" data-t="00:23:16">[00:23:16]</a>.
2.  **Prepare Data:** The collected dataset from Hugging Face Hub is loaded <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>. The `messages` and `tools` are passed into a chat template that converts them into a single long string of text <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>.
3.  **Apply LoRA Adapters:** The model is prepared for [[finetuning_ai_models_for_specific_use_cases | fine-tuning]] by applying Low-Rank Adapters (LoRA) to specific parts of the model (e.g., attention modules and MLP layers) <a class="yt-timestamp" data-t="00:23:50">[00:23:50]</a>. This allows training only a small percentage of parameters, keeping most of the main weights frozen <a class="yt-timestamp" data-t="00:30:17">[00:30:17]</a>.
4.  **Training Configuration:**
    *   **Batch Size:** Often set to one due to VRAM limitations, though larger batch sizes (e.g., 32) are ideal for smoother training <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.
    *   **Epochs:** Typically trained for one epoch initially <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.
    *   **Learning Rate:** Fairly high for small models <a class="yt-timestamp" data-t="00:28:58">[00:28:58]</a>.
    *   **Optimizer:** AtomW 8-bit optimizer can be used to save VRAM <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>.
5.  **Run Training:** The model is trained using the prepared data <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>.
6.  **Evaluate Performance:** After [[finetuning_ai_models_for_specific_use_cases | training]], inference is run again to compare performance <a class="yt-timestamp" data-t="00:29:34">[00:29:34]</a>. A more elaborate setup with an evaluation set and TensorBoard logging is recommended for robust evaluation <a class="yt-timestamp" data-t="00:31:04">[00:31:04]</a>.
7.  **Save and Deploy:** The [[finetuning_ai_models_for_specific_use_cases | fine-tuned]] model and tokenizer can be saved and pushed to Hugging Face Hub, allowing it to be used as an inference endpoint <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>.

## Related Concepts
*   **[[switching_between_language_models_with_unified_interfaces | Model Context Protocol (MCP)]]**: A protocol for providing services, like tool access, to LLMs <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.
*   **Reinforcement Learning (RL)**: While [[finetuning_ai_models_for_specific_use_cases | supervised fine-tuning]] (SFT) with manual traces is recommended first, RL techniques like GRPO can be applied later <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>. SFT on high-quality traces speeds up subsequent RL training <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>. RL requires defining rewards based on verifiably correct answers <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>.
*   **Tool Calls**: The mechanism by which the LLM interacts with external services or functions <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. For open-source models, it's advised to limit the number of tools to 25-50 to avoid confusing the LLM <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.