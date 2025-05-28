---
title: Multimodal large language models vs vision language models
videoId: viiB3JmK21M
---

From: [[hu-po]] <br/> 

The terminology surrounding advanced language models has evolved, leading to some debate regarding precise definitions. Specifically, the terms "Multimodal Large Language Models" (MLLMs) and "Vision Language Models" (VLMs) are often used to describe similar capabilities, though with nuanced differences in their strict application.

## Defining the Terms

### Vision Language Models (VLMs)
A [[Challenges and improvements in vision language models | Vision Language Model]] (VLM) is a specific type of [[multimodal_capabilities_in_language_models | multimodal]] model that processes and generates information using two primary modalities: vision (images) and language (text) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This term is widely adopted within the research community for models that specialize in understanding and generating text based on visual input <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. For instance, tasks like visual question answering (VQA) and image captioning fall under the domain of VLMs <a class="yt-timestamp" data-t="00:26:58">[00:26:58]</a>.

### Multimodal Large Language Models (MLLMs)
The term [[multimodal_capabilities_in_language_models | Multimodal Large Language Model]] (MLLM) is broader. "Multimodal" implies the capability to handle *multiple* modalities, which could include images, text, audio, vibration data, or other forms of input <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. "[[LLM Large Language Models development | Large Language Models]]" (LLMs) originally referred to their significant size compared to earlier models, though the "large" aspect has somewhat lost its distinct meaning as most models developed now are considered large <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>.

In a strict sense, an MLLM capable of handling only vision and text is, by definition, a VLM <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

## The Semantic Debate: Apple's MM1 and Terminology
Apple's new MM1 model, released on March 14, 2024, is an example that highlights this terminological discussion <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. Despite the model primarily processing image and text data, Apple chose to title their paper "multimodal pre-training" <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a> and refers to MM1 as a [[multimodal_capabilities_in_language_models | multimodal Large Language Model]] <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

The speaker notes that, given MM1's input modalities are limited to vision and language, "[[Challenges and improvements in vision language models | Vision Language Model]]" would be the more accurate and concise term <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. The choice to use "[[multimodal_capabilities_in_language_models | multimodal Large Language Model]]" might be a strategic move by Apple to "own the category" and "own the SEO" for future developments, similar to how they rebranded "Virtual Reality" headsets as "spatial computing" <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

Despite this semantic preference, the Apple MM1 paper is considered "extremely extensive" and "very comprehensive" in its detail regarding architecture components, data choices, and experimental ablations <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. This openness is unusual for Apple, a company traditionally known for its secrecy <a class="yt-timestamp" data-t="00:04:23">[00:04:23]</a>, <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.

## MM1's Modalities and Capabilities

Apple's MM1 family of models, scaling up to 30 billion parameters, are described as consuming "image and Text data and produce text" <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>, <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. This confirms their current operation within the vision and language modalities.

Key capabilities of MM1 include:
*   **Enhanced in-context learning** <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>
*   **Multi-image reasoning** <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>
*   **Few-shot Chain of Thought prompting** <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>
*   **Optical Character Recognition (OCR)**, even on challenging or small text <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>, <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>
*   **Counting objects** <a class="yt-timestamp" data-t="00:12:24">[00:12:24]</a>
*   **Ability to say "no" or identify non-existent objects**, demonstrating a reduction in common language model hallucinations <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>, <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>
*   **Interleaving of text and images** in input <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>

The choice of terminology between MLLM and VLM for models like MM1 remains a point of academic and industry discussion, with the more precise term "VLM" preferred when only vision and language modalities are involved.