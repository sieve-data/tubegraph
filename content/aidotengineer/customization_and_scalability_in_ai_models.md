---
title: Customization and scalability in AI models
videoId: aDj9sY2RoG8
---

From: [[aidotengineer]] <br/> 

NVIDIA's focus in enterprise-level speech AI model deployment is on delivering highly efficient, low-latency models for conversational AI, suitable even for embedded devices <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Their development approach emphasizes both variety and coverage, rejecting a "one model fits all" philosophy <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## Core Principles for Model Development
NVIDIA considers four main categories when developing models <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>:

*   **Robustness** <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>: Ensuring models perform well in diverse environments, including noisy settings and varying sound quality (e.g., telephonic audio, environmental contamination) <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Coverage** <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>: Addressing specific domain demands (medical, entertainment, call centers) and language requirements (monolingual, multilingual, dialect variations, code-switching) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Personalization** <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>: Tailoring models to exact customer needs, which can include target speaker AI, word boosting for uncommon vocabulary, and text normalization <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Deployment Cases** <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>: Balancing speed and accuracy trade-offs, and deciding between high model variety or efficiency-focused solutions <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Model Architectures for Diverse Needs
NVIDIA employs various model architectures to achieve its goals of efficiency, accuracy, and customization:

*   **CTC (Connectionist Temporal Classification) Models** <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>: Utilized for high-speed inference, especially in streaming environments due to their non-auto-regressive decoding <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **RNT (Recurrent Neural Transducer) / TDT (Transducer Decoder Transducer) Models** <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>: Used when higher accuracy is needed, incorporating auto-regressive streaming setups with an internal language model <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Attention Encoder-Decoder Setups** <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>: Offer the highest accuracy, suitable for non-streaming scenarios. These transformer decoders are capable of handling multiple tasks within a single model, such as speech translation, timestamp prediction, language identification, and speech recognition <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Fast Conformer** <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>: The fundamental architecture across all decoding platforms. It enables significant subsampling (80-millisecond compression), leading to smaller audio inputs, reduced memory load, more efficient training with quicker convergence, and faster inference <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This directly contributes to [[techniques_for_improving_ai_model_efficiency | improving AI model efficiency]].

### NVIDIA Reva Offerings
The Fast Conformer architecture underpins two main model offerings:

*   **Reva Parakeet** <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>: Focused on streaming speech recognition, using CTC and TDT models for fast and efficient recognition, including speech translation and target speaker ASR <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
*   **Reva Canary** <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>: Utilizes Fast Conformer models for accuracy and multitask modeling, prioritizing the best possible accuracy over speed <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

This comprehensive toolkit allows customers to choose between fast multitasking or high-accuracy models <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

## Advanced Customization and Accuracy Features
To further enhance model performance and usability, NVIDIA offers additional models and features:

*   **Derization Model Former (SoftFormer)** <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>: An end-to-end neural deriser that integrates speaker time stamps with speaker tokens, allowing for multi-speaker and target speaker ASR scenarios <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. This unified architecture can be [[finetuning_ai_models_for_specific_use_cases | fine-tuned]] with simple objectives <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
*   **Voice Activity Detection (VAD)** <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>: Detects speech segments to improve noise robustness <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **External Language Models** <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>: Enhance ASR transcription accuracy and customization <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Text Normalization (TN) and Inverse Text Normalization (ITN)** <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>: Convert spoken terms to written forms for better readability <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
*   **Punctuation and Capitalization (PNC)** <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>: Adds punctuation and capitalization to transcriptions for improved readability <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Speaker Diarization** <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>: Identifies multiple speakers in a conversation <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Word Boosting** <a class="yt-timestamp" data-t="00:15:16">[00:15:16]</a>: Improves recognition of product names, jargon, and context-specific knowledge <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.

This comprehensive approach to customization contributes to NVIDIA's high rankings on leaderboards, such as the Hugging Face Open ASR leaderboard <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

## Training for Robustness and Coverage
NVIDIA's training approach focuses on fundamental data development practices:

*   **Robust Data Sourcing** <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>: Emphasizes multilingual coverage, dialect sensitivity, and comprehensive language documentation <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Data Mix** <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>: Incorporates both open-source data (for variety and domain shift) and proprietary data (for high-quality entity data) <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   **Pseudo Labeling** <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>: Uses transcripts from top-of-the-line commercial models to leverage community advancements and internal releases <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   **Nemo Research Toolkit** <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>: An open-source library that provides tools for GPU maximalization, data bucketing, and high-speed data loading, enabling [[techniques_for_improving_ai_model_efficiency | efficient training]] <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>.
*   **Validation** <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>: Rigorous testing across open-source and proprietary data to minimize bias and ensure robustness across language categories before models reach end-users <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.

## Deployment for Scalability
Trained models are deployed through NVIDIA Reva via NVIDIA NIM for low latency and high throughput inference <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. This highlights [[scaling_ai_agents_in_production | scaling AI agents in production]] and [[leveraging_ai_tools_for_efficiency_and_scalability | leveraging AI tools for efficiency and scalability]].

*   **High-Performance Inference** <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>: Powered by NVIDIA TensorRT optimizations and the NVIDIA Triton inference server <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Deployment Versatility** <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>: Available as gRPC-based microservices for low-latency streaming and high-throughput offline use cases <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   **Containerization** <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>: NVIDIA Reva is fully containerized, allowing it to easily [[scaling_ai_agents_in_production | scale]] to hundreds of streams <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **Flexible Deployment Environments** <a class="yt-timestamp" data-t="00:13:56">[00:13:56]</a>: Can be run on-prem, in any cloud, at the edge, or on embedded platforms, supporting diverse applications like contact centers, consumer apps, and video conferencing <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   **NVIDIA NIM** <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>: Offers pre-built containers and industry-standard API support for custom models and optimized inference engines <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.

### Addressing Customization Pain Points
One common pain point in real-world scenarios is the need for deep customization due to domain-specific knowledge (e.g., medical terms, menu names, telephonic conditions) <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. NVIDIA Reva addresses this by offering customization features at every stage <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>. This includes the ability to [[finetuning_ai_models_for_specific_use_cases | fine-tune]] acoustic models (Parakeet/Canary based), external language models, punctuation models, and inverse text normalization models <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.

## Getting Started
NVIDIA Reva models are available in NVIDIA NIM, with resources such as quick start guides, developer forums, and [[finetuning_ai_models_for_specific_use_cases | fine-tuning]] guides for the Nemo framework provided <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. More information can be found at `build.envidia.com/explore/speech` <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.