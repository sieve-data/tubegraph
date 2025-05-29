---
title: Comparison of AI model hosting options
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

When working with large language models (LLMs), understanding the various hosting options is crucial, especially concerning [[running_ai_models_locally_and_data_privacy_considerations | data privacy]] and performance. This article explores different ways to host and interact with models like DeepSeek R1, comparing their advantages and disadvantages.

## DeepSeek.com (Direct Website & App)

DeepSeek R1 is a new reasoning model from China that has gained popularity due to its capabilities and being free to use on its official website, deepseek.com <a class="yt-timestamp" data-t="00:42:00">[00:42:00]</a>. It is reportedly on par with models like ChatGPT's 01 reasoning model <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.

*   **Pros**:
    *   Free to use <a class="yt-timestamp" data-t="01:04:00">[01:04:00]</a>.
    *   Offers web search capabilities <a class="yt-timestamp" data-t="04:21:00">[04:21:00]</a>.
*   **Cons**:
    *   **[[running_ai_models_locally_and_data_privacy_considerations | Data privacy]] Concerns**: Data sent to deepseek.com or its app is hosted in China and subject to Chinese laws and regulations. Users should be very careful about sensitive data <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. It's not advisable to input personal information like tax returns or medical records <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>, <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>.
    *   **Reliability Issues**: The server can be busy due to its popularity, leading to timeouts or failures <a class="yt-timestamp" data-t="07:36:00">[07:36:00]</a>.
*   **Use Case**: Best for public information or data that the user does not mind being sent to a third party outside their region <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>, <a class="yt-timestamp" data-t="20:38:00">[20:38:00]</a>.

## API Providers (Fireworks AI, Groq, OpenRouter)

Another option is to use an intermediary API provider that hosts the DeepSeek model or similar models. This offers better regional control over data.

*   **How it works**: Users can deploy a web UI (like Open Web UI) locally and connect it to these API providers using an API key. This routes the data through the provider's servers, which might be in a preferred region like North America <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>, <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>.
*   **Examples**:
    *   **Fireworks AI**: Currently hosts the DeepSeek model <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>. An app like Cursor uses the Fireworks API to host its DeepSeek model outside of China <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>.
    *   **Groq**: Hosts distilled versions of models, such as the distilled Llama 70B <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>. These models are incredibly fast due to Groq's API <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>.
    *   **OpenRouter**: Provides access to pretty much every model available, often with free credits to start <a class="yt-timestamp" data-t="38:31:00">[38:31:00]</a>.
*   **[[pricing_and_freetier_exploration_of_ai_coding_platforms | Pricing]]**: Fireworks AI costs around $8 per million tokens <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>. While this might seem small, token usage can add up quickly in workflows, research, or business operations <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>. [[comparisons_with_other_ai_tools | Compared to OpenAI's 01 Pro]], which might cost $15 for input and $60 for output per million tokens, Fireworks AI is significantly cheaper <a class="yt-timestamp" data-t="16:53:00">[16:53:00]</a>, <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>. Prices are expected to drop as models become more efficient <a class="yt-timestamp" data-t="18:03:00">[18:03:00]</a>.
*   **Pros**:
    *   Better [[running_ai_models_locally_and_data_privacy_considerations | data privacy]] control by choosing providers located in desired regions (e.g., North America, Europe) <a class="yt-timestamp" data-t="10:14:00">[10:14:00]</a>, <a class="yt-timestamp" data-t="16:29:00">[16:29:00]</a>.
    *   Generally more reliable and faster than direct DeepSeek website <a class="yt-timestamp" data-t="09:40:00">[09:40:00]</a>.
    *   Access to a wide variety of models <a class="yt-timestamp" data-t="39:01:00">[39:01:00]</a>.
*   **Cons**:
    *   Still relies on a third-party service, so data is not fully controlled by the user.
    *   Incurs costs based on token usage.

## Local Hosting (Your Machine & Mobile Devices)

The most secure option for [[running_ai_models_locally_and_data_privacy_considerations | data privacy]] and offline use is to run AI models directly on your local machine or mobile device.

*   **Desktop/Laptop Setup (Open Web UI + Ollama)**:
    *   **Open Web UI**: An excellent interface for running models locally <a class="yt-timestamp" data-t="22:54:00">[22:54:00]</a>. It functions similarly to ChatGPT interfaces <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.
    *   **Docker**: Required to run Open Web UI. It containers the entire app, simplifying setup <a class="yt-timestamp" data-t="23:02:00">[23:02:00]</a>.
    *   **Ollama**: Used to download and manage local AI models <a class="yt-timestamp" data-t="25:12:00">[25:12:00]</a>. Users can pull models like DeepSeek R1 directly from Ollama within Open Web UI <a class="yt-timestamp" data-t="26:37:00">[26:37:00]</a>.
    *   **Steps**:
        1.  Download and install Docker Desktop <a class="yt-timestamp" data-t="23:02:00">[23:02:00]</a>.
        2.  Pull the Open Web UI Docker container <a class="yt-timestamp" data-t="23:47:00">[23:47:00]</a>.
        3.  Run the container (use `gpus=all` for NVIDIA GPUs to leverage local processing power) <a class="yt-timestamp" data-t="24:00:00">[24:00:00]</a>.
        4.  Access the UI via `localhost:3000` <a class="yt-timestamp" data-t="24:47:00">[24:47:00]</a>.
        5.  Download and install Ollama <a class="yt-timestamp" data-t="25:18:00">[25:18:00]</a>.
        6.  Configure Open Web UI to connect to the Ollama API, then pull desired models <a class="yt-timestamp" data-t="25:55:00">[25:55:00]</a>.
    *   **Pros**:
        *   [[running_ai_models_locally_and_data_privacy_considerations | Complete data privacy]]: Data never leaves your machine <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.
        *   Can run offline, even on a plane <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>, <a class="yt-timestamp" data-t="33:25:00">[33:25:00]</a>.
        *   Users can experiment with various models available on Ollama <a class="yt-timestamp" data-t="32:07:00">[32:07:00]</a>.
    *   **Cons**:
        *   Requires technical setup and command-line interaction <a class="yt-timestamp" data-t="23:31:00">[23:31:00]</a>.
        *   Consumes local machine resources (RAM, GPU), which can be significant for larger models <a class="yt-timestamp" data-t="27:51:00">[27:51:00]</a>.
        *   Smaller, distilled models, while fast, may not provide the same level of detailed output as larger, full models <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>, <a class="yt-timestamp" data-t="33:11:00">[33:11:00]</a>.

*   **Mobile Hosting (Apollo App)**:
    *   **Apollo**: A paid mobile app that allows users to download and run AI models locally on their phones <a class="yt-timestamp" data-t="37:06:00">[37:06:00]</a>.
    *   **Features**: It has its own interface and allows downloading models directly, similar to Ollama <a class="yt-timestamp" data-t="37:32:00">[37:32:00]</a>. It can identify available memory and only offers models compatible with the device's capacity <a class="yt-timestamp" data-t="39:13:00">[39:13:00]</a>. Models are optimized for Apple silicon <a class="yt-timestamp" data-t="42:00:00">[42:00:00]</a>.
    *   **Pros**:
        *   [[running_ai_models_locally_and_data_privacy_considerations | Local execution on mobile devices]]: No internet connection needed once models are downloaded <a class="yt-timestamp" data-t="43:40:00">[43:40:00]</a>.
        *   Highly portable and convenient.
        *   Enables [[business_opportunities_using_ai_studio_and_machine_learning_models | innovative use cases]] like real-time assistance (e.g., medical emergencies, negotiation) on wearable devices <a class="yt-timestamp" data-t="44:00:00">[44:00:00]</a>.
    *   **Cons**:
        *   Paid app.
        *   Model size limitations based on phone memory (models can be several gigabytes) <a class="yt-timestamp" data-t="39:27:00">[39:27:00]</a>.
        *   Smaller models may not offer the same depth of reasoning as larger models.

## General AI Model Considerations

*   **Model Parameters**: Models with larger parameters (e.g., 600 billion+) tend to have more intelligence and provide better results, although they may take longer to process <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>. Distilled models are smaller, faster versions, but may yield less comprehensive outputs <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>.
*   **Temperature Setting**: This control influences the model's creativity. A lower temperature (e.g., 0.8 default down to 0) makes the model less likely to "hallucinate" and better at following instructions for logical reasoning (like coding) <a class="yt-timestamp" data-t="29:40:00">[29:40:00]</a>. A higher temperature (closer to 1) encourages extreme creativity for non-logical tasks like creative writing <a class="yt-timestamp" data-t="30:01:00">[30:01:00]</a>.
*   **Quantization Level**: Refers to the bit size (e.g., Q4 for 4 bits). A higher quantization level typically means more memory usage and potentially higher intelligence, impacting the quality of the output <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a>.
*   **Prompting**: Advanced chaining prompts can significantly leverage a model's thinking capabilities <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>. Tools like OpenAI's platform playground can help reconfigure and improve prompts <a class="yt-timestamp" data-t="18:31:00">[18:31:00]</a>. Reasoning models spend extra time paying attention to instructions, leading to more detailed outputs <a class="yt-timestamp" data-t="15:14:00">[15:14:00]</a>.

## Conclusion

The AI landscape is rapidly evolving, with new models and hosting options constantly emerging. While direct website access like DeepSeek.com offers ease of use and no upfront cost, it comes with significant [[running_ai_models_locally_and_data_privacy_considerations | data privacy]] risks. API providers like Fireworks AI and Groq offer a balance of performance, regional data control, and competitive [[pricing_and_freetier_exploration_of_ai_coding_platforms | pricing]]. For ultimate [[running_ai_models_locally_and_data_privacy_considerations | data privacy]] and control, local hosting via Open Web UI and Ollama provides the ability to run models offline and keep all data on your device, even on mobile.

The key is to select the right tool for the job, considering the specific use case, [[running_ai_models_locally_and_data_privacy_considerations | data sensitivity]], performance needs, and available resources <a class="yt-timestamp" data-t="42:45:00">[42:45:00]</a>. This exploration of different hosting options can inform [[identifying_ai_saas_startup_opportunities | business opportunities]] and help users gain an unfair advantage through efficiency and innovation <a class="yt-timestamp" data-t="13:05:00">[13:05:00]</a>.