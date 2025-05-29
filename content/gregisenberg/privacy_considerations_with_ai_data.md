---
title: Privacy considerations with AI data
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

When utilizing advanced AI models like DeepSeek's reasoning models, it's crucial to understand the implications of data privacy and where your information is processed and stored <a class="yt-timestamp" data-t="01:39:07">[01:39:07]</a>. This is especially important for business-sensitive data <a class="yt-timestamp" data-t="01:40:48">[01:40:48]</a>.

## Deepseek.com and Data Hosting

DeepSeek's official website, deepseek.com, is currently hosted in China <a class="yt-timestamp" data-t="02:28:09">[02:28:09]</a>. When you use deepseek.com or download their app, your computer sends data to a region in China <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

> [!CAUTION] Data Sovereignty
> Different countries have their own rules, laws, and regulations regarding data <a class="yt-timestamp" data-t="02:50:07">[02:50:07]</a>. Therefore, exercise caution with any sensitive data placed into the system, as it will be subject to Chinese regulations, not necessarily those of your residing country <a class="yt-timestamp" data-t="02:55:04">[02:55:04]</a>. Avoid putting sensitive personal information, like tax returns or medical records, on deepseek.com <a class="yt-timestamp" data-t="05:19:07">[05:19:07]</a>, <a class="yt-timestamp" data-t="21:57:07">[21:57:07]</a>.

## Alternatives for Data Hosting

To maintain data privacy and control its location, several alternatives are available:

### 1. Using API Providers
Many AI models, including DeepSeek, are available through API providers that host their services in different regions <a class="yt-timestamp" data-t="03:06:03">[03:06:03]</a>.

*   **Fireworks AI**: This provider hosts the DeepSeek model and allows access via API keys. For instance, the coding app Cursor uses the Fireworks API to host DeepSeek models outside of China <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. When using Fireworks AI, your data resides in North America <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>. The pricing for Fireworks AI is approximately $8 per million tokens <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>.
*   **Groq**: Groq also hosts a distilled version of the DeepSeek model (Llama 70b) <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>. This version is noted for its incredible speed <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>.
*   **Open Router**: This API provider also offers access to various models, including DeepSeek R1, with some free credits available <a class="yt-timestamp" data-t="38:57:00">[38:57:00]</a>. It's an alternative to sending data directly to DeepSeek's servers <a class="yt-timestamp" data-t="40:34:00">[40:34:00]</a>.

To set up an API connection using Open Web UI:
1.  Go to the "User" section, then "Admin Panel," and "Settings."
2.  In the "Connections" area, add a new connection.
3.  Input the base URL (e.g., `api.fireworks.ai/inference/v1` for Fireworks AI or `api.groq.com/openai/v1` for Groq) and your generated API key <a class="yt-timestamp" data-t="34:15:00">[34:15:00]</a>, <a class="yt-timestamp" data-t="35:28:00">[35:28:00]</a>.
4.  The models available from these providers will then appear in your model selection list <a class="yt-timestamp" data-t="35:36:00">[35:36:00]</a>, <a class="yt-timestamp" data-t="35:43:00">[35:43:00]</a>.

### 2. Running Models Locally
For maximum data privacy, you can run AI models directly on your own machine. This ensures your data never leaves your device <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

*   **Open Web UI (Desktop)**: This is a highly recommended interface for running models locally <a class="yt-timestamp" data-t="22:54:00">[22:54:00]</a>.
    *   **Requirements**: Download Docker Desktop <a class="yt-timestamp" data-t="23:00:00">[23:00:00]</a>.
    *   **Setup**:
        1.  Pull the Open Web UI Docker container using a provided command <a class="yt-timestamp" data-t="23:47:00">[23:47:00]</a>.
        2.  Run the container using a specified command, optionally including GPU support for NVIDIA cards <a class="yt-timestamp" data-t="24:00:00">[24:04:00]</a>.
        3.  Access the interface via `localhost:3000` in your web browser <a class="yt-timestamp" data-t="24:47:00">[24:47:00]</a>.
    *   **Model Management**: Download models locally using Ollama (ollama.com) <a class="yt-timestamp" data-t="25:12:00">[25:12:00]</a>. Ollama allows you to manage and run various local models like DeepSeek R1 <a class="yt-timestamp" data-t="25:47:00">[25:47:00]</a>. These models will appear in Open Web UI's model list <a class="yt-timestamp" data-t="36:03:00">[36:03:00]</a>.
    *   **Performance**: Running models locally can consume significant RAM, especially for larger models <a class="yt-timestamp" data-t="28:00:00">[28:00:00]</a>. However, smaller, distilled models (e.g., 7 billion parameter models) can still perform impressive analysis locally <a class="yt-timestamp" data-t="29:00:00">[29:00:00]</a>.

*   **Apollo App (Mobile)**: For mobile devices, the Apollo app (available on app stores) allows you to download and run AI models locally on your phone <a class="yt-timestamp" data-t="37:18:00">[37:18:00]</a>.
    *   **Functionality**: Apollo enables you to download models directly, similar to Ollama <a class="yt-timestamp" data-t="37:29:00">[37:29:00]</a>. The app indicates which models are compatible with your device's memory <a class="yt-timestamp" data-t="39:16:00">[39:16:00]</a>.
    *   **Optimized for Apple Hardware**: Models running on Apple devices are often optimized for Apple silicon, ensuring efficient local operation <a class="yt-timestamp" data-t="41:57:00">[41:57:00]</a>.
    *   **Use Case**: This allows for reasoning model capabilities even without an internet connection <a class="yt-timestamp" data-t="43:40:00">[43:40:00]</a>. [[innovative_ai_functionalities_in_apps | Embedding AI to enhance app functionality]] on mobile devices can open up new possibilities, like emergency response applications that process audio locally <a class="yt-timestamp" data-t="44:00:00">[44:00:00]</a>.

## Conclusion

Understanding where your data goes is a critical privacy consideration when working with AI models <a class="yt-timestamp" data-t="48:48:00">[48:48:00]</a>. While free online services might be convenient, they can pose privacy risks <a class="yt-timestamp" data-t="48:00:00">[48:00:00]</a>. Utilizing API providers or running models locally offers greater control over data sovereignty <a class="yt-timestamp" data-t="48:06:00">[48:06:00]</a>. Experimentation with different models and hosting options is key to finding the right tool for your specific use case, balancing performance, cost, and data privacy needs <a class="yt-timestamp" data-t="42:45:00">[42:45:00]</a>, <a class="yt-timestamp" data-t="48:49:00">[48:49:00]</a>. The rapid advancements in AI models and hosting solutions present both [[challenges_and_opportunities_in_adopting_ai | challenges and opportunities in adopting AI]] <a class="yt-timestamp" data-t="15:52:00">[15:52:00]</a>.