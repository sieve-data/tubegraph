---
title: Open source AI models and data privacy
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

Ray Fernando, a 12-year ex-Apple engineer, discusses [[creating_a_defensible_ai_startup | building an AI startup]] and the implications of using open-source AI models, particularly regarding data privacy <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## DeepSeek R1 and Reasoning Models

DeepSeek R1 is a new reasoning model that has gained popularity because it is open source and free to use on their website, DeepSeek.com <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. This model, developed in China, is considered to be on par with ChatGPT's 01 reasoning model <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Reasoning models are advanced because they can "think and reason," potentially leading to superhuman capabilities <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

## [[Concerns about data privacy with Chinese AI tools | Concerns about Data Privacy with Chinese AI Tools]]

A significant caveat when using DeepSeek.com directly or its app is that the service is currently hosted in China <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. This means that any data sent to DeepSeek.com is subject to Chinese laws and regulations <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. Users should exercise caution and avoid inputting sensitive data like tax returns or medical records into the system, as it may not be governed by the user's local privacy laws and could potentially be exposed <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>, <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>.

## Alternatives for Enhanced Data Privacy

To mitigate data privacy concerns, several alternatives exist that allow users to leverage the power of these models without sending data to potentially undesirable regions:

### Using Web UIs with API Providers

Instead of directly using DeepSeek.com, users can utilize web UIs that connect to API providers <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>. These providers often host the models in different regions (e.g., North America) <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **Examples of providers:** Fireworks AI <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>, Groq <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>, and OpenRouter <a class="yt-timestamp" data-t="00:38:33">[00:38:33]</a>.
*   **Implementation:** Tools like Open Web UI can connect to these APIs using an API key and the model string <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>, allowing data to remain in the desired region <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Cost:** API costs, such as Fireworks AI at approximately $8 per million tokens, are generally significantly cheaper than some OpenAI models <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>, <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>. These costs can add up quickly for businesses or frequent users <a class="yt-timestamp" data-t="00:17:49">[00:17:49]</a>.

### [[Running AI models locally and on mobile | Running AI Models Locally and on Mobile]]

Running models locally on a personal machine ensures that data never leaves the device <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This option provides the highest level of data privacy and allows for offline use, such as during a flight <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Setup for desktop (Mac/PC):**
    1.  **Docker:** Download and install Docker Desktop <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
    2.  **Open Web UI:** This is the recommended interface <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>. The setup involves pulling and running a Docker container via terminal commands <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>. NVIDIA users can enable GPU acceleration for efficiency <a class="yt-timestamp" data-t="00:24:14">[00:24:14]</a>.
    3.  **Ollama:** Download Ollama to easily download and manage local AI models <a class="yt-timestamp" data-t="00:25:15">[00:25:15]</a>. Ollama models can then be selected within Open Web UI <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a>.
*   **Performance:** Local models, such as the 7-billion parameter DeepSeek R1, consume local machine resources (RAM, GPU) but can still perform impressive analysis on large texts <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>. Smaller, "distilled" versions of models run faster but may offer less detailed results <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **On Mobile Devices:** The Apollo app allows users to download and run AI models locally on their phones <a class="yt-timestamp" data-t="00:37:04">[00:37:04]</a>. These models are optimized for Apple hardware, enabling on-device reasoning without an internet connection <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>. However, model size depends on device memory <a class="yt-timestamp" data-t="00:39:16">[00:39:16]</a>.

## Utilizing AI Models for Business and Creative Tasks

These reasoning models offer significant advantages for various tasks:
*   **Content Generation:** [[using_ai_models_and_apis_for_image_generation | Utilizing AI models and APIs for image generation]] allows for the generation of content like blog posts from video transcripts, including detailed analysis, geopolitical implications, future predictions, and even graphs <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. The output can be human-level in quality, similar to what a senior writer or research engineer would produce <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   **Efficiency:** The ability to automate complex tasks, such as transcribing and analyzing videos, can save significant human energy and provide an "unfair advantage" in business by improving efficiency and reducing costs <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>, <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
*   **Advanced Prompting:**
    *   **Prompt Engineering:** OpenAI's platform offers a playground to refine prompts, transforming simple instructions into detailed, chained thoughts for more efficient model output <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>. Key elements include defining desired instructions, expected output, and what to avoid <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
    *   **Temperature Setting:** Adjusting the model's "temperature" controls its creativity. Lower temperatures (e.g., 0.0) lead to more logical, instruction-following responses, while higher temperatures (e.g., 1.0) encourage more creative and "out-of-the-box" thinking <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>.
*   **[[Operator AI capabilities and limitations | Operator AI Capabilities and Limitations]]:** Future models, like GPT-4o, are expected to understand audio, tone, cadence, and even micro-expressions, opening up new possibilities for applications in areas like negotiation or emergency response <a class="yt-timestamp" data-t="00:46:13">[00:46:13]</a>, <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

## Conclusion

Understanding where your data is going and how to use different AI models and hosting options is crucial <a class="yt-timestamp" data-t="00:47:48">[00:47:48]</a>. The landscape of AI is rapidly evolving, with new models and hosting providers constantly emerging <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. Experimenting with these models and learning prompting techniques can lead to innovative [[sustainable_business_models_in_ai | business models]] and applications <a class="yt-timestamp" data-t="00:48:49">[00:48:49]</a>.