---
title: Data privacy and concerns with international servers
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

The rise of advanced AI models, such as DeepSeek R1, brings significant discussions around [[security_and_privacy_concerns_with_ai_applications | data privacy]] and the implications of international data hosting. Ray Fernando, an ex-Apple engineer, highlights key considerations for users and businesses when interacting with AI services hosted in different regions. <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

## Understanding Data Residency and Jurisdiction

DeepSeek R1, a reasoning model originating from China, is gaining popularity for being open-source and free to use on its website. <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a> However, its hosting location presents a critical caveat for users. When accessing deepseek.com or its associated app, data is sent to a region in China. <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a> <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>

### Risks of International Data Transfer

A primary concern is that different countries operate under their own rules, laws, and regulations regarding data. <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>

> "I would be very careful as far as anything you put into this system as far as if you have any sensitive data because it would not belong to a region that you know you may live in or have control in." <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>

This means that sensitive information, such as tax returns or medical records, should not be input into systems like deepseek.com if users are concerned about their data potentially being exposed or subjected to foreign laws. <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a> <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a> <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>

## Alternatives for Enhanced Data Privacy

To mitigate risks associated with international data hosting, several alternatives are available:

### 1. API Providers in Controlled Regions

Certain API providers host AI models in specific geographic regions, allowing users to keep their data within desired jurisdictions, such as North America or Europe. <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a> <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>

*   **Perplexity.ai:** Some models are built into Perplexity, which is hosted in the United States. <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a> <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>
*   **Fireworks AI:** Cursor, a coding app, uses the Fireworks API, which is not hosted in China. <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a> <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a> Fireworks AI currently hosts the DeepSeek model and allows access via API key, meaning data is processed in North America. <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a> <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>
*   **Groq:** Another hosting provider that offers models, including a distilled version of Llama 70B, which is incredibly fast. <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>
*   **Open Router:** Offers access to various models, including DeepSeek R1, with free credits. <a class="yt-timestamp" data-t="00:38:57">[00:38:57]</a> <a class="yt-timestamp" data-t="00:40:08">[00:40:08]</a>

Utilizing these providers ensures that data remains within regions with preferred data laws and regulations, which is crucial for businesses. <a class="yt-timestamp" data-t="00:16:27">[00:16:27]</a>

### 2. Local Model Hosting

Running AI models locally on a personal machine provides the highest level of [[security_and_privacy_concerns_with_ai_applications | data privacy]], as data never leaves the device. <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>

*   **Open Web UI & Docker:** Open Web UI is a user interface similar to ChatGPT that can be set up locally using Docker. <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a> This involves pulling and running a Docker container, with options to utilize a GPU for better performance on systems like NVIDIA. <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a> <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>
*   **Ollama:** After setting up Open Web UI, Ollama.com is recommended to download local AI models, such as DeepSeek R1, onto the machine. <a class="yt-timestamp" data-t="00:25:09">[00:25:09]</a> <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a> These models run entirely on the local device, consuming local resources like RAM. <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a> <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a> This allows for powerful analysis even without an internet connection, such as during a flight. <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>
*   **Apollo App:** For mobile devices (specifically Apple hardware with MLX infrastructure), the Apollo app allows users to download and run AI models locally. <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a> <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a> These mobile-optimized models, though smaller (e.g., 1.5GB), still offer reasoning capabilities directly on the phone, ensuring data remains on the device. <a class="yt-timestamp" data-t="00:41:40">[00:41:40]</a> <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>

## The "AI Arms Race" and Future Considerations

The rapid advancement of AI models like DeepSeek R1, especially those with reasoning capabilities, is driving an "AI arms race." <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a> The demand for GPUs and hosting services to run these large parameter models (e.g., 600+ billion parameters) is immense. <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a> Companies like Fireworks and Groq are striving to meet this demand, often offering these models at lower costs than established providers like OpenAI. <a class="yt-timestamp" data-t="00:16:05">[00:16:05]</a>

As AI technology becomes more efficient, model prices are expected to drop significantly. <a class="yt-timestamp" data-t="00:18:03">[00:18:03]</a> The future may see even more powerful models, like OpenAI's upcoming 03 and Omni models, offering advanced features such as understanding audio, tone, and cadence, which could revolutionize applications in areas like negotiation or healthcare. <a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a>

## Conclusion

Understanding where data is processed and stored is paramount when engaging with AI applications. While free services like DeepSeek's website offer powerful capabilities, users must be mindful of the [[security_and_privacy_concerns_with_ai_applications | data privacy]] implications of using international servers. Alternatives such as region-specific API providers and local hosting solutions empower users to leverage AI's intelligence while maintaining control over their sensitive information. <a class="yt-timestamp" data-t="00:47:48">[00:47:48]</a>