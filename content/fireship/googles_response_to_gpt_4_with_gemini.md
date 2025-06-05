---
title: Googles response to GPT 4 with Gemini
videoId: q5qAVmXSecQ
---

From: [[fireship]] <br/> 

In the "great AI war of 2023," Google faced significant challenges from Microsoft's advancements, particularly with GPT-4, which captured the public's imagination in the artificial intelligence age <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. As a response, Google unveiled its highly anticipated [[google_gemini_15_ai_model | Gemini model]] on December 7th, 2023, designed to surpass GPT-4 in numerous benchmarks <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## Introducing Gemini

The [[google_gemini_15_ai_model | Gemini model]] was first introduced publicly at Google I/O, where Sundar Pichai described it as AI applying AI to rigorously test AI with AI <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. [[google_gemini_15_ai_model | Gemini]] is a [[multimodal_capabilities_of_gemini | multimodal]] large language model intended to replace previous models like Lambda and Palm 2 <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. Similar to GPT-4, its [[multimodal_capabilities_of_gemini | multimodal]] nature means it is trained not only on text but also on sound, images, and video <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Multimodal Capabilities in Action

Google's demonstrations of [[google_gemini_15_ai_model | Gemini]] highlight its advanced [[multimodal_capabilities_of_gemini | multimodal]] abilities:
*   **Real-time Video Understanding**: [[google_gemini_15_ai_model | Gemini]] can recognize actions in a video feed and respond instantly, such as identifying a duck being drawn <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. This capability extends to multiple languages <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
*   **Object Tracking**: It can keep track of objects in an ongoing video feed, demonstrating an ability to follow an object, like a ball under cups, even after they are scrambled <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.
*   **Connect the Dots**: [[google_gemini_15_ai_model | Gemini]] can perform tasks like connecting dots <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   **Multimodal Outputs**: It supports [[multimodal_capabilities_of_gemini | multimodal]] outputs, including generating images on the fly, similar to Stable Diffusion, and creating music based on prompts <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This includes image-to-audio generation <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Logic and Spatial Reasoning**: [[google_gemini_15_ai_model | Gemini]] excels at logic and spatial reasoning, demonstrated by its ability to determine which car would go faster based on aerodynamics from two pictures <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Impact on Engineering Professions

[[google_gemini_15_ai_model | Gemini]]'s advanced capabilities suggest future applications where civil engineers could take a picture of land, and the AI could instantly generate bridge blueprints <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

Google also introduced AlphaCode 2, an AI model that outperforms 90% of competitive programmers <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>. This includes solving highly complex, abstract problems often found in Codeforces competitions <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. AlphaCode 2 can break down problems into smaller parts using techniques like dynamic programming <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Gemini Models and Availability

[[google_gemini_15_ai_model | Gemini]] is available in three sizes:
*   **Nano**: The smallest version, designed for embedding on devices like Android phones <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Pro**: A general-purpose model, currently available in the Bard chatbot in the United States <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. While Bard has improved significantly, it is noted as not yet matching GPT-4 Pro <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Ultra**: The largest and most powerful model in the [[google_gemini_15_ai_model | Gemini]] family <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. This version will not be available until 2024, pending additional safety tests <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## Performance Benchmarks

In [[geminis_performance_benchmarks | performance benchmarks]], [[google_gemini_15_ai_model | Gemini]] models show mixed results in [[comparison_between_gemini_and_gpt_4 | comparison with GPT-4]]:
*   [[google_gemini_15_ai_model | Gemini]] Pro generally underperforms GPT-4 in most situations <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   [[google_gemini_15_ai_model | Gemini]] Ultra, however, outperforms GPT-4 in almost every category <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
    *   Notably, [[google_gemini_15_ai_model | Gemini]] Ultra is the first model to surpass human experts on the Massive Multitask Language Understanding (MMLU) test, which is a multiple-choice test covering a wide range of subjects, similar to the SATs for AI <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
    *   Surprisingly, [[google_gemini_15_ai_model | Gemini]] Ultra underperforms GPT-4 on the Hellaswag benchmark <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. This benchmark evaluates common-sense natural language understanding by having the AI complete vague or ambiguous sentences, a task humans find easy but is crucial for an AI to feel "human-like" <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## Training Infrastructure and Data

To train [[google_gemini_15_ai_model | Gemini]], Google utilized its newly unveiled version 5 Tensor Processing Units (TPUs) <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. These TPUs are deployed in super PODs, each containing 4,096 chips <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Each super POD features a dedicated optical switch for rapid data transfer between pods, allowing for parallel training <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. They can dynamically reconfigure into 3D torus topologies, or "shape shift into donuts," to reduce latency between chips <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The scale of [[google_gemini_15_ai_model | Gemini]] Ultra's training required communication across multiple data centers <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

The training dataset for [[google_gemini_15_ai_model | Gemini]] comprises nearly everything available on the internet, including web pages, YouTube videos, scientific papers, and books <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This data is filtered for quality, and then reinforcement learning through human feedback is used to fine-tune the model and mitigate hallucinations <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.