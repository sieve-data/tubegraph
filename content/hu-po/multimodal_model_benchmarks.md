---
title: Multimodal model benchmarks
videoId: 27cjzGgyxtw
---

From: [[hu-po]] <br/> 

Evaluating [[multimodal_capabilities_in_language_models | multimodal models]] involves various approaches, from automated tests to human evaluations, with recent advancements highlighting new challenges and standards for [[comparison_with_other_multimodal_ai_models | comparison]].

## Evolution of Multimodal Model Benchmarking

Initially, [[multimodal_capabilities_in_language_models | multimodal models]] often relied on separate vision encoders and language models "glued together" and then fine-tuned [00:08:01](<a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. This approach allowed for [[multimodal_large_language_models_vs_vision_language_models | Vision Language Models (VLMs)]] capable of consuming images and text and outputting text [01:34:09](<a class="yt-timestamp" data-t="01:34:09">[01:34:09]</a>. Benchmarking these models primarily focused on their text-only output capabilities given multimodal input [01:09:30](<a class="yt-timestamp" data-t="01:09:30">[01:09:30]</a>.

However, newer models like [[chameleon_mixed_modal_model | Chameleon]] introduce complex capabilities, such as generating interleaved text and images [00:05:59](<a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>, making direct comparisons with older benchmarks challenging [01:10:20](<a class="yt-timestamp" data-t="01:10:20">[01:10:20]</a>.

## Current Benchmarking Methods

### Human Evaluation

The "gold standard" for evaluating [[multimodal_capabilities_in_language_models | multimodal models]] is human evaluation, particularly pairwise comparisons [01:13:15](<a class="yt-timestamp" data-t="01:13:15">[01:13:15]</a>. This method involves third-party services where humans compare outputs from different models without knowing which model produced them [01:13:19](<a class="yt-timestamp" data-t="01:13:19">[01:13:19]</a>.

For instance, [[chameleon_mixed_modal_model | Chameleon]] 34B was compared against GPT-4V and Gemini Pro using this method [01:12:51](<a class="yt-timestamp" data-t="01:12:51">[01:12:51]</a>:
*   **Chameleon 34B vs. GPT-4V:**
    *   Chameleon beats GPT-4V: 46% [01:13:43](<a class="yt-timestamp" data-t="01:13:43">[01:13:43]</a>
    *   About the same: 30% [01:13:45](<a class="yt-timestamp" data-t="01:13:45">[01:13:45]</a>
    *   GPT-4V is better: 22% [01:13:46](<a class="yt-timestamp" data-t="01:13:46">[01:13:46]</a>
This result suggests [[chameleon_mixed_modal_model | Chameleon]] is potentially state-of-the-art for [[multimodal_capabilities_in_language_models | multimodal models]] [00:07:04](<a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

#### Challenges in Human Evaluation for New Models
Models like [[chameleon_mixed_modal_model | Chameleon]] that generate interleaved text and images pose a challenge for comparison with models like GPT-4V or Gemini Pro, which only output text [01:09:30](<a class="yt-timestamp" data-t="01:09:30">[01:09:30]</a>. To compare them, GPT-4V was augmented with an image generation model (DALL-E 3) to produce image captions that could then be rendered into images [01:09:47](<a class="yt-timestamp" data-t="01:09:47">[01:09:47]</a>. This highlights the lack of standard benchmarks for models with mixed-modal output capabilities [01:10:20](<a class="yt-timestamp" data-t="01:10:20">[01:10:20]</a>.

### Automatic Benchmarks

Traditional automatic benchmarks, while useful, can be "gamed" or overfit to [01:13:01](<a class="yt-timestamp" data-t="01:13:01">[01:13:01]</a>. These benchmarks typically involve running automated tests and generating scores [01:13:04](<a class="yt-timestamp" data-t="01:13:04">[01:13:04]</a>.

However, the speaker notes that "the benchmarks are becoming increasingly meaningless" due to varying methodologies (e.g., zero-shot vs. multi-shot) that are often not explicitly disclosed [01:16:41](<a class="yt-timestamp" data-t="01:16:41">[01:16:41]</a>. Qualitative improvements and actual model capabilities are often more indicative of progress [01:17:00](<a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

## Key Findings Related to Benchmarking

### Impact of Language Model Quality
For [[multimodal_large_language_models_vs_vision_language_models | Vision Language Models (VLMs)]] that glue a vision encoder to a language model, the quality of the pre-trained language model significantly impacts performance [02:25:50](<a class="yt-timestamp" data-t="02:25:50">[02:25:50]</a>. Switching from Llama 17B to Mistral 7B, for instance, led to a 5% improvement in score, indicating the importance of a strong language model backbone in such architectures [02:26:01](<a class="yt-timestamp" data-t="02:26:01">[02:26:01]</a>.

### Limitations in OCR for Images
Both [[chameleon_mixed_modal_model | Chameleon]] and hugging face's Idefix models struggle with accurately extracting tiny text from images, indicating a common weakness in image tokenization and reconstruction for high-resolution text [01:54:54](<a class="yt-timestamp" data-t="01:54:54">[01:54:54]</a>, [03:08:12](<a class="yt-timestamp" data-t="03:08:12">[03:08:12]</a>.

### Benefits of Interleaved Training
Training on mixed modalities (e.g., interleaved mixtures of image, text, and code) can lead to better performance even on unimodal benchmarks [01:11:48](<a class="yt-timestamp" data-t="01:11:48">[01:11:48]</a>. This suggests that the information gained from different modalities can transfer and enhance understanding across specific domains, making a [[building_multimodal_models | multimodal]] approach superior to training a language model purely on text [01:11:58](<a class="yt-timestamp" data-t="01:11:58">[01:11:58]</a>.

## The Future of Benchmarking

As [[multimodal_capabilities_in_language_models | multimodal models]] advance towards capabilities like consuming and outputting video and audio in an interleaved fashion, current benchmarking methods will need to evolve. The goal is an "end-to-end trained from scratch, early fusion [[multimodal_capabilities_in_language_models | multimodal]] model with chunked audio and video" [01:17:19](<a class="yt-timestamp" data-t="01:17:19">[01:17:19]</a>. This will require new metrics and evaluation paradigms to capture the full spectrum of these advanced capabilities.