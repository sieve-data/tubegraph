---
title: Future Directions for Multimodal and AGI Development
videoId: 27cjzGgyxtw
---

From: [[hu-po]] <br/> 

Recent advancements in AI models, particularly in the realm of [[multimodal_language_models | multimodal language models]], are rapidly reshaping the landscape of artificial intelligence. Key players like Meta, Google DeepMind, and OpenAI are pushing the boundaries of what these models can perceive and generate, leading towards what many speculate to be the cusp of Artificial General Intelligence (AGI) <a class="yt-timestamp" data-t="01:38:35">[01:38:35]</a>.

## Evolution of Multimodal Architectures

The development of [[overview_of_multimodal_models | multimodal models]] has seen a significant shift from component-based integration to more holistic, end-to-end training approaches.

### Traditional Vision Language Model (VLM) Approach
Historically, [[recent_advancements_in_multimodal_model_architectures | recent advancements in multimodal model architectures]] in the open-source community, exemplified by Hugging Face's efforts with **iFix 2**, have focused on combining pre-trained components <a class="yt-timestamp" data-t="02:29:59">[02:29:59]</a>. This approach involves:
*   **Gluing Components Together** Developers use pre-trained vision encoders (like Dino or Clip) and pre-trained large language models (LLMs like Llama 17B or Mistral 7B), connecting them with a small "projection layer" or "adapter" <a class="yt-timestamp" data-t="08:13:13">[08:13:13]</a><a class="yt-timestamp" data-t="08:52:27">[08:52:27]</a>. This strategy is primarily driven by limited computational resources, as it avoids the immense cost of training from scratch <a class="yt-timestamp" data-t="10:20:21">[10:20:21]</a>.
*   **Performance within Size Category** iFix 2, an 8-billion parameter model, achieves "state-of-the-art within its size category," meaning it performs well for its scale but not necessarily against much larger, proprietary models <a class="yt-timestamp" data-t="02:59:58">[02:59:58]</a><a class="yt-timestamp" data-t="02:10:04">[02:10:04]</a>.
*   **Limitations** These models often struggle with tasks like accurately extracting tiny text from images due to the lossy nature of vision tokenizers <a class="yt-timestamp" data-t="03:04:14">[03:04:14]</a><a class="yt-timestamp" data-t="03:11:06">[03:11:06]</a>. The choice of the language model backbone significantly impacts performance in this "gluing" approach <a class="yt-timestamp" data-t="02:59:58">[02:59:58]</a>.

### Early Fusion with Meta's Chameleon
Meta's **Chameleon** represents a shift towards "early fusion" and end-to-end training <a class="yt-timestamp" data-t="03:05:05">[03:05:05]</a>.
*   **Approach** Chameleon is a family of early-fusion, token-based mixed-modal models, trained from scratch on an interleaved mixture of modalities <a class="yt-timestamp" data-t="07:08:42">[07:08:42]</a><a class="yt-timestamp" data-t="07:11:15">[07:11:15]</a>. This means modalities (like text and images) are immediately converted into tokens and fed into a single, shared model <a class="yt-timestamp" data-t="07:20:41">[07:20:41]</a>.
*   **Capabilities** It handles tasks such as visual question answering, image captioning, text generation, image generation, and novel "long-form mixed-modal generation," which involves generating interleaved text and images <a class="yt-timestamp" data-t="05:27:07">[05:27:07]</a><a class="yt-timestamp" data-t="05:59:15">[05:59:15]</a>.
*   **Performance** Chameleon 34B outperforms Llama 2 in text-only tasks and matches or exceeds the performance of much larger models like Gemini Pro and GPT-4V in multimodal tasks <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a><a class="yt-timestamp" data-t="11:25:27">[11:25:27]</a>. Human evaluations show a preference for Chameleon 34B over GPT-4V, making it a potential [[stateoftheart_video_generation_and_multimodal_models | state-of-the-art multimodal model]] <a class="yt-timestamp" data-t="06:51:30">[06:51:30]</a><a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   **Training Scale** This feat is achieved by training on a monstrous scale, utilizing Meta's Research Supercluster (over 3,000 Nvidia A100 GPUs) for millions of GPU hours <a class="yt-timestamp" data-t="03:32:04">[03:32:04]</a><a class="yt-timestamp" data-t="03:38:40">[03:38:40]</a>.

### Advanced Multimodal Integration with Google DeepMind's Mirasol 3B
Google DeepMind's **Mirasol 3B** paper explores even more complex multimodal integration, focusing on video and audio <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
*   **Approach** Mirasol 3B consumes video, audio, and text, outputting text <a class="yt-timestamp" data-t="04:27:32">[04:27:32]</a><a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>. It uses a "combiner" mechanism to jointly encode video and audio, then project them into tokens for an LLM <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>.
*   **Audio Handling Trick** A clever trick is representing audio as a spectrogram, effectively turning it into an image, allowing the same Vision Transformer (ViT) backbone to encode both video and audio <a class="yt-timestamp" data-t="05:09:00">[05:09:00]</a>. This requires training the encoder from scratch <a class="yt-timestamp" data-t="05:15:00">[05:15:00]</a>.
*   **Token Turing Machine (External Memory)** A crucial, often overlooked, aspect of Mirasol 3B is its "Token Turing Machine" <a class="yt-timestamp" data-t="05:59:15">[05:59:15]</a>. This recurrent sequential model with Transformers maintains an external memory, enabling the model to store and retrieve information beyond its immediate context <a class="yt-timestamp" data-t="05:58:34">[05:58:34]</a><a class="yt-timestamp" data-t="05:59:51">[05:59:51]</a>. This reduces computational complexity from O(T^2) to O(T) relative to time, making it efficient for longer sequences <a class="yt-timestamp" data-t="01:03:03">[01:03:03]</a>. This concept aligns with the observed "memory" in models like GPT-4o, where past events are recalled <a class="yt-timestamp" data-t="01:04:46">[01:04:46]</a><a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>.

## Key Advancements and Features

### Interleaved Generation
Chameleon's ability to generate interleaved text and images is a significant step, moving beyond models that only output text from multimodal inputs <a class="yt-timestamp" data-t="05:59:15">[05:59:15]</a><a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. This capability introduces new challenges in inference, such as managing conditional flow for different tokenizers and ensuring full image generation before switching modalities <a class="yt-timestamp" data-t="05:40:00">[05:40:00]</a>.

### Tokenization Innovations
Training new image and text tokenizers from scratch is essential for these end-to-end models <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. While text tokenizer vocabulary sizes are relatively stable (around 65,000), image tokenizers are still in early stages, with codebook sizes around 8,192 <a class="yt-timestamp" data-t="01:17:42">[01:17:42]</a>. There's an expectation that visual token codebook sizes will eventually exceed text vocabulary sizes <a class="yt-timestamp" data-t="01:18:40">[01:18:40]</a>.

### The Token Turing Machine (External Memory)
The concept of an external, learnable memory, as seen in Mirasol 3B's Token Turing Machine, is crucial for developing [[developments_in_multiturn_conversational_AI | developments in multiturn conversational AI]] and AI agents that can remember past interactions <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. This moves models from being stateless to stateful during inference, allowing for more complex and contextually rich behaviors <a class="yt-timestamp" data-t="01:11:34">[01:11:34]</a>.

## Challenges in Multimodal Development

### Logit Drift
When training a single model from scratch to handle and generate multiple modalities, a new problem emerges: "logit drift" or modalities competing with each other <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a><a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>. Modalities with significantly varying entropy (e.g., images vs. text) can bias the model's predictions. Meta addresses this with architectural tweaks like query-key normalization and specific dropout layers <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a><a class="yt-timestamp" data-t="01:40:37">[01:40:37]</a>.

### Inference Complexity with Memory
Introducing an external memory (like the Token Turing Machine) significantly increases the complexity of inference <a class="yt-timestamp" data-t="01:12:07">[01:12:07]</a>. Managing memory placement (GPU RAM vs. database) and retrieval for long-term context becomes a major engineering challenge <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.

### Data and Compute Requirements
The ability to train end-to-end [[multimodal_language_models | multimodal language models]] from scratch is currently limited to companies with massive budgets and infrastructure. Meta's use of 3,000+ A100 GPUs and a specialized high-speed networking stack (Nvidia Quantum Infiniband) highlights the significant investment required <a class="yt-timestamp" data-t="03:38:40">[03:38:40]</a><a class="yt-timestamp" data-t="04:11:00">[04:11:00]</a>. This creates a bifurcation in AI research, with smaller groups and open-source communities reliant on pre-trained models <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.

## Future Outlook and AGI Implications

The trajectory of [[future_directions_and_potential_breakthroughs_in_AI_models | future directions and potential breakthroughs in AI models]] points towards increasingly capable [[multimodal_language_models | multimodal language models]].

### Fully Interleaved Multimodal Input/Output
The ultimate goal is an end-to-end model that consumes and outputs interleaved video, audio, and text <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a><a class="yt-timestamp" data-t="01:12:07">[01:12:07]</a>. While GPT-4o and Google's Astra currently take multimodal input and primarily output audio/text, a model that can generate video in real-time would be transformative <a class="yt-timestamp" data-t="01:17:39">[01:17:39]</a><a class="yt-timestamp" data-t="01:18:00">[01:18:00]</a>. This would allow for human-like conversational interfaces, where an AI can be seen and heard, resembling a video call with a person <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

### Beyond 2D: Towards 3D and Robotics
The evolution won't stop at 2D video. The [[future_potential_and_direction_for_generative_3d_technology | future potential and direction for generative 3D technology]] suggests models will output 3D representations (like Gaussian Splats) for VR/AR applications <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. Furthermore, these models could output "control tokens" directly to robots, enabling end-to-end control and interaction in physical environments <a class="yt-timestamp" data-t="01:19:02">[01:19:02]</a><a class="yt-timestamp" data-t="01:19:15">[01:19:15]</a>. This hints at the [[potential_future_impacts_and_predictions_of_ai_agents | potential future impacts and predictions of AI agents]].

### The "Bitter Lesson" and Simplification
The underlying principle driving these advancements is the "bitter lesson": rather than engineering complex, modular systems, the most effective approach is to simplify the architecture (e.g., a single end-to-end Transformer) and scale up data and compute <a class="yt-timestamp" data-t="01:30:18">[01:30:18]</a><a class="yt-timestamp" data-t="01:30:57">[01:30:57]</a>. This implies a future where increasingly general and powerful AI models emerge from sheer scale.

### Impact on Research Landscape
The current trends suggest that [[future_directions_and_implications_of_ai_in_vision_language_models | future directions and implications of AI in vision language models]] research might become increasingly dominated by large organizations with vast computational resources <a class="yt-timestamp" data-t="01:44:04">[01:44:04]</a>. The findings from smaller, budget-constrained research might quickly become irrelevant as larger models redefine the state of the art <a class="yt-timestamp" data-t="01:45:01">[01:45:01]</a>. However, even with this challenge, individual researchers can still contribute by exploring specific aspects and finding personal fulfillment in the pursuit of knowledge <a class="yt-timestamp" data-t="01:46:03">[01:46:03]</a>.