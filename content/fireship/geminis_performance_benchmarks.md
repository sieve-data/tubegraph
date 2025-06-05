---
title: Geminis performance benchmarks
videoId: q5qAVmXSecQ
---

From: [[fireship]] <br/> 

[[google_gemini_15_ai_model | Google Gemini]] was unleashed on December 7th, 2023, as Google's highly anticipated response to Microsoft's blitz attack in the "great AI war of 2023" that saw [[comparison_between_gemini_and_gpt_4 | GPT 4]] capture the Zeitgeist of the AI age <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Multimodal Capabilities
[[google_gemini_15_ai_model | Gemini]] is a [[multimodal_capabilities_of_gemini | multimodal]] large language model, meaning it is trained not only on text but also on sound, images, and video <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Google's demonstrations showcase its advanced capabilities:
*   **Real-time Recognition**: It can recognize actions in a video feed and respond in real time, such as identifying a duck being drawn <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This function supports multiple languages <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Tracking and Spatial Reasoning**: [[google_gemini_15_ai_model | Gemini]] can keep track of objects in an ongoing video feed, like following a ball under scrambled cups, and perform tasks like connect-the-dots <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Multimodal Outputs**: It can generate images on the fly, similar to Stable Diffusion, and create music from prompts, including image-to-audio generation <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. It's described as an "anything-to-anything" model <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Logic and Spatial Reasoning**: [[google_gemini_15_ai_model | Gemini]] can use images to deduce which car would go faster based on aerodynamics, hinting at future applications like generating bridge blueprints from land pictures for civil engineers <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

## Gemini Versions
[[google_gemini_15_ai_model | Gemini]] is available in three sizes:
*   **Nano**: The smallest version, designed for embedding on devices like Android phones <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   **Pro**: A more general-purpose model <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Ultra**: The largest and most powerful version <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

## Current Availability
As of December 2023, users in the United States can use [[google_gemini_15_ai_model | Gemini]] Pro in the Bard chatbot <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. While Bard has significantly improved, the Pro version is currently not as good as [[comparison_between_gemini_and_gpt_4 | GPT 4]] Pro <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.

## Benchmark Performance
In direct benchmark comparisons:
*   [[google_gemini_15_ai_model | Gemini]] Pro generally underperforms [[comparison_between_gemini_and_gpt_4 | GPT 4]] <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   [[google_gemini_15_ai_model | Gemini]] Ultra, however, outperforms [[comparison_between_gemini_and_gpt_4 | GPT 4]] in almost every category <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.

Notably:
*   **MMLU (Massive Multitask Language Understanding)**: [[google_gemini_15_ai_model | Gemini]] Ultra is the first model to outperform human experts on this benchmark, which is a multiple-choice test across a wide array of subjects, similar to the SATs for AI <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **HellaSwag Benchmark**: Surprisingly, [[google_gemini_15_ai_model | Gemini]] Ultra underperforms [[comparison_between_gemini_and_gpt_4 | GPT 4]] on the HellaSwag benchmark <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This benchmark evaluates common-sense natural language by requiring the AI to finish vague or ambiguous sentences, a task humans find easy but is crucial for an AI to feel human-like <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## Coding Benchmarks
Google also unveiled AlphaCode 2, an AI model that performs better than 90% of competitive programmers, tackling highly complex, abstract problems often found in platforms like Codeforces <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. AlphaCode 2 can break down problems into smaller sub-problems using techniques like dynamic programming <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Training Infrastructure and Data
[[google_gemini_15_ai_model | Gemini]] was trained using Google's newly unveiled version 5 Tensor Processing Units (TPUs), deployed in super PODs of 4,096 chips each <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. These super PODs have dedicated optical switches for quick data transfer and can dynamically reconfigure into 3D torus topologies to reduce latency <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. The scale of [[google_gemini_15_ai_model | Gemini]] Ultra's training required communication between multiple data centers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

The training dataset for [[google_gemini_15_ai_model | Gemini]] includes a vast array of internet content, such as web pages, YouTube videos, scientific papers, and books <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This data is filtered for quality, and reinforcement learning through human feedback is used to fine-tune its quality and reduce hallucinations <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

## Future Availability
While the Nano and Pro models were made available on Google Cloud on December 13th, the [[google_gemini_15_ai_model | Gemini]] Ultra Pro Max version will not be available until 2024, pending additional safety tests and its achievement of 100% on the "Hell Woke Benchmark" <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.