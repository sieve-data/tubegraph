---
title: Vision language connectors and architectures
videoId: BJ98vicRYHg
---

From: [[hu-po]] <br/> 

[[vision_language_models_and_their_advancements | Vision language models]] (VLMs), also known as Large Multimodal Models (LMMs), combine visual and linguistic understanding capabilities <a class="yt-timestamp" data-t="01:02:32">[01:02:32]</a>. The LLaVA (Large Language and Visual Assistant) model is highlighted as a leading [[opensource_advancements_in_visionlanguage_models | open-source VLM]] <a class="yt-timestamp" data-t="03:13:08">[03:13:08]</a>.

## LLaVA Architecture: A Simple yet Powerful Design
LLaVA is an end-to-end trained large multimodal model that integrates a vision encoder and a Large Language Model (LLM) for general-purpose visual and language understanding <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a> <a class="yt-timestamp" data-t="05:30:30">[05:30:30]</a> <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>. Its core components are designed to work together, even though they are largely pre-trained independently <a class="yt-timestamp" data-t="01:10:40">[01:10:40]</a>.

The architecture consists of three main parts:
1.  **Vision Encoder (Vision Backbone / Vision Tower)** <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a> <a class="yt-timestamp" data-t="01:15:17">[01:15:17]</a>: Processes raw images to create a rich feature representation <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>.
2.  **Large Language Model (LLM)**: Handles textual input and generates responses.
3.  **Vision Language Connector (Projection Matrix)**: Links the visual and linguistic components <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.

![[LLaVA Model Architecture.png]]

### The Vision Encoder
LLaVA utilizes a pre-trained CLIP (Contrastive Language-Image Pre-training) ViT (Vision Transformer) L/14 model <a class="yt-timestamp" data-t="07:29:00">[07:29:00]</a>.
*   **CLIP's Function**: CLIP is trained using a contrastive loss, pulling together related images and text in an embedding space, and pushing apart unrelated ones <a class="yt-timestamp" data-t="08:57:00">[08:57:00]</a>. This process creates an embedding space where similar text and images are closer together, providing rich features <a class="yt-timestamp" data-t="09:11:00">[09:11:11]</a>.
*   **Vision Transformer (ViT)**: The ViT takes an image and divides it into small patches, treating them like a sequence of tokens in a sentence <a class="yt-timestamp" data-t="07:45:00">[07:45:00]</a> <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.
*   **Resolution Improvements**: An enhancement in LLaVA 1.5 involved using a CLIP model with a slightly larger image resolution (336x336 pixels) compared to the original 224x224 <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a> <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>. This scaling of input image resolution allows the LLM to see more details <a class="yt-timestamp" data-t="01:14:41">[01:40:41]</a>.

### The Language Model
The LLM component in LLaVA is Vicuna, a variant of the LLaMA model.
*   **Vicuna 1.5**: This model, specifically the 13B (billion) parameter version, is fine-tuned on GPT-4 answers <a class="yt-timestamp" data-t="01:00:27">[01:00:27]</a> <a class="yt-timestamp" data-t="01:00:46">[01:00:46]</a> <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>.
*   **GPT-4 Influence**: The use of GPT-4 generated data for fine-tuning Vicuna causes LLaVA to exhibit similar behaviors and nuance to GPT-4 <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

### The Vision Language Connector
This component bridges the vision encoder and the LLM.
*   **Simple Design**: LLaVA uses a simple Multi-Layer Perceptron (MLP) as its vision-language connector <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a> <a class="yt-timestamp" data-t="01:14:59">[01:14:59]</a>. This is essentially a fully connected neural network with a few layers <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>.
*   **Projection Matrix**: The connector is implemented as a trainable projection matrix (W) that converts visual features into language embedding tokens <a class="yt-timestamp" data-t="01:33:53">[01:33:53]</a> <a class="yt-timestamp" data-t="01:34:00">[01:34:00]</a>. These tokens have the same dimensionality as the word embedding space of the language model <a class="yt-timestamp" data-t="01:34:44">[01:34:44]</a>.
*   **Lightweight and Cost-Effective**: This simple projection scheme is lightweight, allowing for quick iteration on data-centric experiments <a class="yt-timestamp" data-t="01:34:25">[01:34:25]</a>. Only the parameters of this MLP are trained from scratch, while the vision encoder and LLM remain frozen during the initial training stage <a class="yt-timestamp" data-t="01:34:05">[01:34:05]</a>.
*   **Evolution of Connector**: The original LLaVA paper used a single-layer linear projection, while LLaVA 1.5 improved this to a two-layer MLP, which enhanced multimodal capabilities <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a> <a class="yt-timestamp" data-t="01:15:06">[01:15:06]</a>.

### Interaction of Components
The image is consumed by the vision encoder, which outputs visual tokens <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>. These visual tokens are then fed through the vision-language connector (MLP), which transforms them into a format compatible with the language model's embedding space <a class="yt-timestamp" data-t="01:34:44">[01:34:44]</a>. The language model then processes these visual tokens alongside the encoded text, treating them as a continuous sequence to generate the final output answer <a class="yt-timestamp" data-t="01:41:15">[01:41:15]</a>.

## Training and Data Strategy
LLaVA's success is heavily attributed to its training recipe and data mixture <a class="yt-timestamp" data-t="01:06:42">[01:06:42]</a>.
*   **Two-Stage Instruction Tuning**:
    1.  **Stage 1: Pre-training for Feature Alignment**: Involves training the projection matrix (W) using a filtered subset of CC3M image-text pairs <a class="yt-timestamp" data-t="01:46:14">[01:46:14]</a>. This stage treats each image-text pair as a single-turn conversation where the model learns to describe the image <a class="yt-timestamp" data-t="01:46:24">[01:46:24]</a>. During this stage, both the vision encoder and the LLM weights are frozen <a class="yt-timestamp" data-t="01:46:57">[01:46:57]</a>. This process aligns image features with the pre-trained LLM word embedding space, effectively training a "compatible visual tokenizer" for the frozen LLM <a class="yt-timestamp" data-t="01:48:31">[01:48:31]</a>.
    2.  **Stage 2: Fine-tuning**: The projection layer and parts of the LLM (specifically, a LoRA adapter merged with Vicuna) are updated <a class="yt-timestamp" data-t="01:49:18">[01:49:18]</a> <a class="yt-timestamp" data-t="01:50:50">[01:50:50]</a>. This stage uses a diverse mixture of visual question answering (VQA) data, including data synthetically generated by GPT-4 and existing VQA datasets with modified prompt engineering <a class="yt-timestamp" data-t="01:51:27">[01:51:27]</a> <a class="yt-timestamp" data-t="01:55:38">[01:55:38]</a>. The training on this multi-turn conversational data enables LLaVA's chat abilities <a class="yt-timestamp" data-t="01:51:09">[01:51:09]</a>.
*   **Data-Centric Approach**: The focus shifts from complex model architectures to strategic data mixing and effective fine-tuning <a class="yt-timestamp" data-t="01:06:05">[01:06:05]</a>. This approach makes [[vision_language_models_and_key_differences | LLaVA]] highly accessible for research <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>.

## Performance and Comparisons
LLaVA 1.5 achieves state-of-the-art results across 11 different benchmarks using only publicly available data and significantly less compute and training data compared to other methods <a class="yt-timestamp" data-t="00:59:00">[00:59:00]</a> <a class="yt-timestamp" data-t="01:00:15">[01:00:15]</a> <a class="yt-timestamp" data-t="01:32:40">[01:32:40]</a>.

*   **Relative Performance**: LLaVA shows impressive multimodal chat abilities, sometimes exhibiting behaviors similar to GPT-4V on unseen images and instructions <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.
*   **Against GPT-4V**: While LLaVA is highly capable, a direct [[comparison_of_different_vision_language_models | comparison]] with GPT-4V shows that GPT-4V might have a higher-resolution vision encoder, allowing it to read very tiny text that LLaVA cannot <a class="yt-timestamp" data-t="01:18:12">[01:18:12]</a>.
*   **Open-Source Advantage**: Unlike proprietary models like GPT-4V, LLaVA provides full transparency, releasing its code, model weights, data mixture, and training scripts, making it fully reproducible and affordable for future research <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.

## [[challenges_and_future_directions_in_vision_language_modeling | Challenges and Future Directions]]
The paper acknowledges several [[challenges_and_improvements_in_vision_language_models | limitations]] and potential future work:
*   **Data Scaling**: Further pre-training on larger image-text datasets and generating more instruction-following data could increase concept coverage <a class="yt-timestamp" data-t="01:53:41">[01:53:41]</a>.
*   **Alternative Vision Models**: Connecting LLaVA with other powerful vision models like the Segment Anything Model (SAM) could explore different types of visual understanding <a class="yt-timestamp" data-t="01:54:22">[01:54:22]</a>. An ensemble of different vision encoders feeding into the language model is also suggested <a class="yt-timestamp" data-t="01:56:01">[01:56:01]</a>.
*   **Context Length**: LLaVA's current architecture is not yet capable of processing multiple images due to context length limitations and lack of specific instruction-following data for such scenarios <a class="yt-timestamp" data-t="01:40:39">[01:40:39]</a>.
*   **Problem Solving Capabilities**: While proficient in following complex instructions, LLaVA's problem-solving capabilities can still be limited in certain domains <a class="yt-timestamp" data-t="01:40:51">[01:40:51]</a>.
*   **Hallucination**: LLaVA is not exempt from occasionally disseminating misinformation or "hallucinating" <a class="yt-timestamp" data-t="01:40:56">[01:40:56]</a>. Incorporating negative examples in training data, where the assistant tells the user they are wrong, helps mitigate this <a class="yt-timestamp" data-t="01:38:12">[01:38:12]</a>.
*   **Prompt Engineering**: The precise wording and formatting of prompts ("system messages") are extremely important and can significantly impact the model's output <a class="yt-timestamp" data-t="01:38:30">[01:38:30]</a>. This suggests that prompt engineering will remain a crucial skill for interacting with [[vision_language_models_and_encoders | LLMs and VLMs]] <a class="yt-timestamp" data-t="01:43:01">[01:43:01]</a>.

The simplicity of LLaVA's architecture, combined with its impressive results, suggests that effective integration of powerful pre-trained components and well-curated instruction-tuning data is a highly promising direction for [[application_of_vision_language_models_in_robotics | VLM advancements]] <a class="yt-timestamp" data-t="01:35:00">[01:35:00]</a>.