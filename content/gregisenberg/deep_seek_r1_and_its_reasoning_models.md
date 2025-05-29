---
title: Deep Seek R1 and its reasoning models
videoId: i9kTrcf-gDQ
---

From: [[gregisenberg]] <br/> 

Deep Seek R1 is a new [[AI models for business efficiency | reasoning model]] developed by Deep Seek, a company based in China <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. This model stands out for its advanced capabilities, including the ability to think and reason, potentially leading to superhuman performance <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It has been made open source for public study and is considered to be on par with ChatGPT's 01 reasoning model <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. A significant factor in its popularity is that it is free to use on the Deep Seek website (deepseek.com) <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## Capabilities and Advantages

Deep Seek R1's reasoning models are designed to think through large amounts of text, effectively acting like an administrative assistant that processes information on your behalf <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

Key capabilities include:
*   **Transcript Analysis** The model can analyze video transcripts to generate detailed blog posts <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. This includes identifying key details, discussing geopolitical implications, making future predictions, and even creating graphs and SEO enhancements <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>, <a class="yt-timestamp" data-t="00:12:59">[00:12:59]</a>.
*   **High-Quality Output** The generated content is often described as being at a "human level incredible," comparable to the work of a senior writer or research engineer who has spent considerable time analyzing information <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>, <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   **Configurable Instructions** Users can configure instructions to get specific output types, such as graphs <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>.
*   **Attention to Detail** Unlike some other models, Deep Seek R1's reasoning models spend extra time paying attention to detailed instructions, ensuring every specification is met <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>. This level of detail makes it a "game-changer" for content generation <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

This [[competitive_approach_to_ai_usage | strategic use of AI models]] allows businesses to achieve an unfair advantage by being highly efficient and keeping costs low, ultimately creating better products <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

## Data Privacy and Hosting Options

While Deep Seek R1 offers powerful capabilities, understanding its hosting and data privacy implications is crucial, especially for business users <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

### Direct Use via deepseek.com
Using deepseek.com directly means your data is sent to and hosted in China <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>. This raises concerns about data privacy, as data sent to another country falls under that country's rules and regulations <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. Users should exercise extreme caution and avoid inputting sensitive data like tax returns or medical records <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>, <a class="yt-timestamp" data-t="00:21:57">[00:21:57]</a>. The free website can also experience reliability issues due to high demand <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

### API Providers
To mitigate data privacy concerns and improve reliability, Deep Seek R1 can be accessed via API providers:
*   **Fireworks AI**: This provider hosts the Deep Seek model, often in regions like North America, ensuring data doesn't go to China <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>, <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>.
*   **Groq**: Another provider that hosts a distilled version of the Deep Seek model, known for its incredible speed <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>, <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

These API services typically have pricing models based on tokens used, with Fireworks AI being significantly cheaper than OpenAI's 01 Pro model <a class="yt-timestamp" data-t="00:16:49">[00:16:49]</a>.

### Local Hosting
For maximum data privacy and control, Deep Seek R1 can be run locally on your machine <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This allows for private business use by professionals such as lawyers or doctors <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **Open Web UI**: This is recommended as the best interface for local hosting <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>.
*   **Docker**: Required to set up and run Open Web UI <a class="yt-timestamp" data-t="00:23:03">[00:23:03]</a>.
*   **Ollama**: Used to download and manage local AI models, including Deep Seek R1 <a class="yt-timestamp" data-t="00:25:12">[00:25:12]</a>. Ollama allows users to run different models and experiment with them based on their use cases <a class="yt-timestamp" data-t="00:32:07">[00:32:07]</a>.

Running models locally uses your machine's resources, particularly RAM and GPU, but ensures data remains on your device and can even be used offline, such as on a plane <a class="yt-timestamp" data-t="00:22:21">[00:22:21]</a>, <a class="yt-timestamp" data-t="00:28:08">[00:28:08]</a>.

## Prompting and Model Usage

[[Using AI models strategically for better content | Effective prompting]] is key to leveraging Deep Seek R1's capabilities. The model benefits from advanced chaining prompts that allow it to think through complex tasks <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. OpenAI's platform.openai.com provides a playground where users can describe a desired prompt, and the platform will reconfigure it to be more efficient for the language model, aiding in generating long chains of thought or reason <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.

When designing prompts, consider:
*   Desired instructions and expected output type <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   What outputs you *don't* want <a class="yt-timestamp" data-t="00:19:38">[00:19:38]</a>.

### Temperature Setting
A crucial setting to tweak is "temperature" <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>:
*   **Lower Temperature (e.g., 0.8 default to lower)**: Makes the model "hallucinate less," causing it to follow instructions more closely and not veer off into tangents <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>. This is useful for logical reasoning tasks, especially coding <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.
*   **Higher Temperature (e.g., up to 1)**: Encourages extreme creativity <a class="yt-timestamp" data-t="00:30:01">[00:30:01]</a>. Useful for creative writing or non-logical reasoning where out-of-the-box thinking is desired <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>.

## Technical Details and Considerations

*   **Model Parameters**: Larger parameter models (e.g., 600 billion+) indicate more intelligence but take longer to process <a class="yt-timestamp" data-t="00:07:01">[00:07:01]</a>.
*   **Distilled Models**: These are smaller, faster versions of larger models, taking the "essence" of the original. While efficient, they may not offer the same depth of thought or detailed results as full models <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Groq, for instance, hosts a distilled version of Deep Seek <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Quantization**: This refers to the number of bits used for model data (e.g., Q4 for 4-bit). Higher quantization levels generally mean more memory and potentially better intelligence, though the specific output quality varies and requires experimentation <a class="yt-timestamp" data-t="00:36:12">[00:36:12]</a>.

## Mobile Usage

The **Apollo** app (paid) allows users to download and run Deep Seek models directly on their mobile devices, similar to Ollama <a class="yt-timestamp" data-t="00:37:06">[00:37:06]</a>. This offers the benefits of local AI (offline use, privacy) on a portable device <a class="yt-timestamp" data-t="00:42:09">[00:42:09]</a>. Model sizes can be significant (e.g., 4GB), and device memory limits what models can be run <a class="yt-timestamp" data-t="00:39:27">[00:39:27]</a>. Smaller, optimized models (e.g., for Apple silicon) are efficient for mobile use <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>.

## Future Outlook

The emergence of powerful reasoning models like Deep Seek R1 signifies a new era in AI, often referred to as an "AI arms race" <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>. These models, alongside advancements like OpenAI's GPT-4o (Omni) models that understand audio and tone <a class="yt-timestamp" data-t="00:46:16">[00:46:16]</a>, open up vast opportunities for innovation.

There's a significant demand for robust hosting providers for these large models <a class="yt-timestamp" data-t="00:15:54">[00:15:54]</a>. The ability to run powerful AI locally on devices, even watches, suggests a future where AI can provide real-time assistance, such as emergency response support by analyzing audio situations and providing relevant information <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

For aspiring entrepreneurs, identifying the right AI model for a specific task and understanding its capabilities can lead to a competitive advantage and [[Framework for Identifying AI SaaS Opportunities | multi-million dollar startup ideas]] <a class="yt-timestamp" data-t="00:13:29">[00:13:29]</a>, <a class="yt-timestamp" data-t="00:48:57">[00:48:57]</a>. The key is to experiment with different models, understand their strengths for various use cases, and focus on practical applications <a class="yt-timestamp" data-t="00:42:45">[00:42:45]</a>. The field is rapidly evolving, and continuous learning and experimentation are encouraged <a class="yt-timestamp" data-t="00:50:38">[00:50:38]</a>.