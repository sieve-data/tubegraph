---
title: Data handling and preparing training datasets for LLMs
videoId: Nqb7JTx0Pqo
---

From: [[aidotengineer]] <br/> 

This guide outlines the process of collecting, handling, and preparing high-quality reasoning traces from agents for fine-tuning Large Language Models (LLMs) [00:00:26]. The materials discussed are available online in the Trellis Research AI Worlds Fair 2025 repository, specifically in the MCP agent fine-tune folder [00:00:45].

## Core Concepts

### Model Context Protocol (MCP)
MCP, or Model Context Protocol, is a protocol designed to provide services, primarily access to tools, for LLMs [00:01:02]. This allows an LLM to interact with external functionalities, such as using a browser to navigate websites [00:01:23]. Examples of other MCPs include integrations for Stripe, GitHub, and Gmail [00:01:31].

MCP serves several functions:
*   **Information Store:** It stores information about tools, guiding the LLM on how to call or utilize them [00:01:47].
*   **Tool Execution:** The MCP tool service runs the tools, taking action when an LLM decides to make a call (e.g., navigating to a page) [00:01:57].
*   **Response Return:** It returns a response containing the result of the action or additional guidance for the LLM to continue its process [00:02:07].

### LLM API Exposure
To enable interaction, the language model is exposed as an API, typically in the widely adopted OpenAI endpoint format [00:02:27]. This allows various models and libraries to make use of this API style [00:02:41].

Integrating this API endpoint requires handling a few points of integration or translation [00:02:51]:
1.  **Tool Information Conversion:** Tool information from MCP services must be converted into lists of JSON tools, which is the expected format for OpenAI endpoints [00:03:02].
2.  **Tool Response Conversion:** The tool response needs to be converted into a format the language model expects [00:03:11].
3.  **Tool Call Extraction:** When the LLM calls a tool by emitting tokens or text, the system must detect and extract the tool call. For Quen models, this text often takes the Hermes format [00:03:21].

### Prompt Structure
A typical prompt structure sent to the LLM includes [00:03:46]:
*   **System Message:** Starts with a system start tag and describes to the LLM how to make tool calls (e.g., by passing JSONs within `<tool_code>` XML tags) [00:03:58]. It instructs the LLM to return function calls as JSON inside `<tool_code_call>` tags [00:04:20].
*   **User Message:** The initial request from the user (e.g., "navigate to trellis.com") [00:04:33].
*   **Assistant Response:** The LLM's response, which may include thinking steps, a tool call, or a text-based response if the task is complete [00:04:37].

## Data Collection
The process begins with running an agent to generate sample traces or logs [00:00:26].

### Setting up the LLM Endpoint for Data Generation
*   **Endpoint Type:** An OpenAI-style endpoint is required [00:05:40].
*   **Model Consistency:** It's recommended to maintain consistency between the model used to generate data and the model intended for fine-tuning. For instance, using a Quen type agent to generate traces if a Quen model will be fine-tuned later [00:05:54].
*   **Reasoning Traces:** Open-source models like Quen are preferred over OpenAI models because they share their thinking traces, which are crucial for training [00:06:04].
*   **Example Model:** The 30 billion parameter Quen model (a mixture of experts model) is used, running on RunPod via a one-click affiliate template [00:06:13].
*   **Endpoint Configuration:**
    *   Docker image for VLM [00:06:47].
    *   Enabling reasoning and a reasoning parser to extract reasoning into a JSON-type style [00:06:52].
    *   Setting max model length (e.g., 32,000 tokens) [00:07:09].
    *   Hosting on a specific port (e.g., 8000) [00:07:11].
    *   Enabling automatic tool choice for the LLM [00:07:16].
    *   Specifying the tool parser (e.g., Hermes) to extract tool calls into JSON format [00:07:22].

### Running the Agent
The agent is run using a base URL (including the pod ID and port number) and can truncate the length of tool responses (e.g., accessibility trees from browser navigation) [00:08:26]. Running the agent involves:
1.  **Syncing Requirements:** Using `uv sync` [00:09:25].
2.  **Starting MCP Server:** The agent starts the MCP server, which is configured in a config file and can load multiple tools (e.g., 25 Playwright tools like `navigate`, `switch tab`) [00:09:37]. For open-source models, it's advised to limit tools to 25-50 to avoid confusing the LLM [00:10:01].
3.  **User Input:** Providing tasks like "navigate to trellis.com and read out the top two lines" [00:10:15].
4.  **Observation:** The LLM thinks, decides on a tool call, and, with approval, the browser pops up (if not in headless mode) [00:10:25]. The accessibility structure of the page is sent back to the LLM as a tool response [00:11:41].

### Tracing and Logging
By default, when the agent runs, traces are logged with two main parts: `messages` and `tools` [00:12:06]. This structure is essential for fine-tuning [00:12:17].

*   **`tools`:** Contains a list of all available tools (e.g., 26 browser tools) [00:12:22].
*   **`messages`:** Stores the full conversation history, including:
    *   User requests [00:12:29].
    *   Assistant's thinking process (extracted as reasoning due to the reasoning parser) [00:12:34].
    *   Tool calls made by the assistant [00:12:43].
    *   Tool responses, which include details from the tool's action (e.g., truncated page content) [00:12:45].
    *   Assistant's final answer or next action based on the tool response [00:12:59].

These traces are considered "very nice" and are kept for fine-tuning [00:13:05]. The goal is to collect multiple such high-quality traces [00:13:24].

### Data Curation and Quality Control
*   **Manual Adjustment:** Traces can be manually adjusted if the LLM doesn't follow the desired path. This might involve deleting user turns or combining sections [00:17:10].
*   **System Prompts:** A system prompt can be passed to directly guide the LLM on how to perform a task and which tools to call. This helps in generating a "nice tidy trace" which then can be used for training without including the system prompt itself [00:16:03]. The goal is to obtain high-quality traces for training data [00:16:23].

## Preparing Training Datasets
Collected traces are pushed to the Hugging Face Hub to create a dataset for fine-tuning [00:17:51].

### Unrolling Data
A subtle but important point for training is "unrolling" the data [00:18:11]. This means that if a conversation has multiple turns (e.g., three back-and-forths), it is unrolled into multiple rows in the dataset [00:18:22]:
*   One row with all three turns.
*   One row with the first two turns.
*   One row with just the first turn.

This provides multiple training examples from a single multi-turn conversation, effectively giving "three for the price of one" [00:18:28]. This is also important because the Quen template will always include the reasoning from the most recent turn, so unrolling ensures older reasoning is part of different training steps [00:18:37].

### Pushing to Hugging Face Hub
The `push to hub` function is used to upload the collected `tools` and `messages` to a dataset on Hugging Face Hub [00:17:59]. This requires being logged in with write permissions [00:19:10].

The resulting dataset contains fields like `id`, `timestamp`, `model`, `messages`, and `tools`, along with a flag indicating if it's truncated (unrolled) [00:19:33]. The `messages` field will contain the full conversation turns, and reasoning content is extracted separately [00:20:04].

### Data Templating
For fine-tuning, the messages and tools are templated into a single long string of text [00:20:50]. This formatted string is what the trainer consumes [00:24:12]. This template is available in the model's tokenizer config on Hugging Face [00:24:41].

The templated string typically starts with a system message, lists available tools (which can be very long, e.g., 26 tools), then includes the user message, assistant message, tool calls, and so on [00:25:27].

## Fine-tuning Considerations
The prepared data is then used to fine-tune a model, such as the 4 billion parameter Quen model [00:23:16].

### Model Setup
*   **Model Loading:** A specific model is loaded (e.g., the 4B Quen model) [00:23:16].
*   **Sequence Length:** The max sequence length must be large enough (e.g., 32,000) to accommodate the long templated strings [00:23:21].
*   **Precision:** Models are often run in full precision (16 bits) [00:23:43].
*   **Parameter Efficient Fine-Tuning (PEFT):** Instead of training all parameters, adapters like Low Rank Adapters (LoRA) are applied to specific parts (e.g., attention modules, MLP layers) [00:23:50]. This trains only a small percentage of parameters (e.g., 1.62%) [00:30:15].

### Training Parameters
*   **Dataset:** The prepared dataset (e.g., nine rows after unrolling) is passed to the trainer [00:28:10].
*   **Batch Size:** Due to VRAM limitations or small dataset size, a batch size of one might be used, though a larger batch size (e.g., 32) is ideal for smoothing training loss [00:28:34].
*   **Epochs:** Training might be done for a single epoch [00:28:48].
*   **Warm-up Steps:** Warm-up steps might not be needed for very small datasets [00:28:51].
*   **Optimizer:** An optimizer like AtomW 8-bit can be used to save VRAM [00:29:03].
*   **Learning Rate:** A constant learning rate, possibly high for small models, is applied [00:29:00].

### Evaluation
*   **Baseline Inference:** It's important to run inference on the raw model *before* fine-tuning to establish a baseline performance [00:25:55].
*   **Post-Training Inference:** After fine-tuning, inference is run again to observe performance improvements. Even with noisy training due to small datasets, the model can still correctly call tools [00:34:03].
*   **Robust Evaluation:** A more elaborate evaluation setup is needed, potentially running the model on an endpoint and assessing rollouts in a workspace [00:34:07].
*   **Logging:** For more advanced implementations, logging with TensorBoard and splitting data into an evaluation set is recommended [00:31:16].

### Saving and Deploying the Fine-tuned Model
After training, the model and tokenizer can be saved [00:30:30]. The model can also be pushed to Hugging Face Hub, potentially merged to 16 bits [00:30:35]. The fine-tuned model's name can then be used to update an inference endpoint [00:30:51].

### Reinforcement Learning (RL) vs. Supervised Fine-Tuning (SFT)
While reinforcement learning (RL) techniques like GRPO could be used for automated trace generation and reward-based systems, it's strongly recommended to start with manual curation of high-quality traces and perform Supervised Fine-Tuning (SFT) first [00:32:00]. SFT on high-quality traces helps the model learn the domain and avoids struggling to find positive rewards during RL, significantly speeding up subsequent RL training [00:32:32]. For RL, defining rewards requires a dataset with verifiable correct answers [00:32:52].

Even without moving to RL, significant performance improvements can be achieved with a small number of curated examples (e.g., 50-100 traces), especially for common, important, or narrow use cases [00:34:47].