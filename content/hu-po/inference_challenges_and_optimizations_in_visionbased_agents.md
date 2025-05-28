---
title: Inference challenges and optimizations in visionbased agents
videoId: 5qkjxDzEaaw
---

From: [[hu-po]] <br/> 

Vision-based agents, particularly those leveraging [[vision_language_models_in_ai_agents | Vision Language Models]] (VLMs), are central to the future of AI applications. The development of these models involves continuous improvements in underlying components, but also significant [[challenges_and_strategies_for_training_largescale_vision_language_models | challenges]] in efficiently deploying them for real-world inference scenarios <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Evolution of Vision Encoders
Vision encoders are the initial neural network modules that process an image, functioning similarly to the visual cortex of a VLM <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Recent research, such as Apple's "Multimodal Auto-Regressive Pre-training of Large Vision Encoders," demonstrates that these encoders can be effectively pre-trained using a simple auto-regressive objective, much like language models <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. This contrasts with traditional contrastive losses used in models like CLIP <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.

The auto-regressive approach involves pairing a vision encoder with a multimodal decoder that generates raw image patches and text tokens <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. The encoder converts an image into a vector representation, which the decoder then reconstructs in patches <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. This method achieves high accuracy, for example, 89.5% on ImageNet 1K, indicating strong performance even with a frozen "trunk" (the lowest part of the encoder) <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.

Crucially, the scaling properties observed in Large Language Models (LLMs) also apply to vision encoders trained with this auto-regressive objective <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. Increasing parameters consistently improves validation loss, suggesting that vision encoders will continue to become more capable over time as pre-training scale increases <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>.

## Inference Challenges
Despite advancements in pre-training, inferencing with VLMs presents significant [[challenges_and_improvements_in_animated_ai_models | challenges]], particularly in achieving efficiency on devices like mobile phones <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. A primary issue is the high latency caused by the large number of input tokens, predominantly from images <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. When an image is processed, it's typically cut into many patches, each converted into a vision token, which then needs to be fed into the language model <a class="yt-timestamp" data-t="00:15:17">[00:15:17]</a>.

## Optimization Strategies for Inference
To mitigate latency and improve efficiency for mobile deployments, several strategies are employed:

*   **Downsizing LLMs or Reducing Visual Tokens**: One can either decrease the size of the LLM or reduce the number of input image tokens <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>. Surprisingly, for visual reasoning tasks, the optimal strategy for inference is often to use the largest LLM that fits the budget while minimizing visual token count, sometimes even to a single token <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>. This means a single token might represent an entire image <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>.

*   **Pipeline Parallelism**: This involves running the vision embedding module (vision encoder) and the vision Transformer on different processing units simultaneously, such as the CPU and NPU (Neural Processing Unit) respectively <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This parallel processing helps speed up inference <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

*   **Batching Image Patches**: Instead of sequentially processing each image patch, they can be processed in batches on the NPU, further accelerating the vision encoder inference <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. Experiments suggest that processing four patches per batch can deliver the fastest performance <a class="yt-timestamp" data-t="01:29:02">[01:29:02]</a>.

*   **Token Reduction Methods**: To reduce the number of tokens coming out of the vision encoder, techniques like filtering out visual tokens with low similarity to a class token (a token representing the entire image) or using a "token packer" with cross-attention to compress tokens are used <a class="yt-timestamp" data-t="00:20:52">[00:20:52]</a>.

*   **Caching Text Input Tokens**: In use cases where the same text instruction (e.g., "what is in this image?") is repeatedly given, the corresponding text input tokens can be calculated once and then cached instead of recalculating them every time <a class="yt-timestamp" data-t="00:22:55">[00:22:55]</a>. This reduces redundant computation, although its effectiveness depends on hardware and memory architecture <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.

## Task-Specific Optimizations
The optimal inference strategy varies significantly depending on the task <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a>. For tasks like Optical Character Recognition (OCR), reducing the number of visual tokens can be detrimental to performance, as fine-grained detail is needed to identify letters <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>. In contrast, for general visual reasoning, fewer tokens might suffice, as the gist of the image is often enough <a class="yt-timestamp" data-t="00:25:31">[00:25:31]</a>.

## Application: GUI Agents
A significant future use case for [[vision_language_models_in_ai_agents | Vision Language Models]] is in Graphical User Interface (GUI) agents <a class="yt-timestamp" data-t="00:26:49">[00:26:49]</a>. These agents interact with digital devices through human-like mouse and keyboard actions, observing the GUI through screenshots <a class="yt-timestamp" data-t="00:27:31">[00:27:31]</a>. This approach bypasses the need for custom APIs for AI, as companies might prefer maintaining a single GUI for both humans and agents <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.

GUI agents often maintain an extensive context of historical screenshots, which can be stored as vision tokens rather than raw image frames to save computational cost <a class="yt-timestamp" data-t="00:30:39">[00:30:39]</a>. This further incentivizes the use of fewer visual tokens <a class="yt-timestamp" data-t="00:31:01">[00:31:01]</a>.

However, the [[current_state_of_ai_agents_and_their_limitations | current state of AI agents and their limitations]] in GUI interaction can be inconsistent; an agent might fail on a simple task like updating a phone number in a Word document, yet succeed at a more complex sequence of actions in a video game with an unusual UI <a class="yt-timestamp" data-t="00:31:56">[00:31:56]</a>. This highlights the "weirdness" in their current capabilities <a class="yt-timestamp" data-t="00:34:01">[00:34:01]</a>.

## [[Future directions and implications of AI in vision language models | Future Directions and Implications]]
### Self-Improvement
Models are increasingly capable of self-improvement. Techniques like "minimum Bayes risk" allow models to sample multiple outputs, score them based on consistency, and then use these scores for supervised fine-tuning or preference optimization <a class="yt-timestamp" data-t="00:43:47">[00:43:47]</a>. This approach can automatically generate high-quality reasoning trace datasets, outperforming methods relying on human-produced data <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>. This evidence suggests that AI models can become "smarter" by training on their own outputs <a class="yt-timestamp" data-t="00:49:26">[00:49:26]</a>.

### Imagining Futures
Beyond structured reasoning, advanced agents may leverage generative models to imagine future observations or screen states <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>. By generating video sequences based on current observations, an agent can use these "hallucinated images" to update its internal beliefs and plan more effectively <a class="yt-timestamp" data-t="00:54:26">[00:54:26]</a>. This "look-ahead" capability, while compute-intensive, can lead to better decision-making <a class="yt-timestamp" data-t="00:53:24">[00:53:24]</a>.

### The "Arms Race" of Inference
There's an ongoing "arms race" between hardware and software in AI inference <a class="yt-timestamp" data-t="01:05:50">[01:05:50]</a>. Hardware developers strive to increase tokens per second, while AI researchers push for more complex reasoning traces and imagined outputs, requiring more tokens and compute <a class="yt-timestamp" data-t="01:06:05">[01:06:05]</a>. The goal is to perform millions of token generations and complex chain-of-thoughts in the blink of an eye, leading to faster and more intelligent agent actions <a class="yt-timestamp" data-t="01:06:42">[01:06:42]</a>.

### Data Collection and Privacy
The widespread adoption of vision-based agents, particularly GUI agents, raises concerns about privacy. Devices might send frequent screenshots to cloud servers for processing, allowing companies to gather extensive data on user interactions <a class="yt-timestamp" data-t="01:12:21">[01:12:21]</a>. This trend of decreasing privacy appears to be accelerating <a class="yt-timestamp" data-t="01:20:30">[01:20:30]</a>. While local, federated learning approaches could offer privacy, the competitive advantage of vast cloud-based data collection makes this path less certain <a class="yt-timestamp" data-t="01:11:15">[01:11:15]</a>.

The future of AI will involve a dynamic interplay between continuous improvements in [[comparison_of_vision_architectures | Vision Language Models]], innovative inference optimizations, and the evolving applications of visual reasoning in agents, potentially leading to self-improving AI that can even simulate future scenarios to enhance its decisions <a class="yt-timestamp" data-t="01:25:23">[01:25:23]</a>.