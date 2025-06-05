---
title: Customization and personalization in speech AI
videoId: aDj9sY2RoG8
---

From: [[aidotengineer]] <br/> 

NVIDIA's approach to Speech AI development focuses on providing highly customizable and personalized models rather than a "one model fits all" solution. This strategy aims to meet diverse customer needs across various domains and deployment scenarios <a class="yt-timestamp" data-t="06:41:00">[06:41:00]</a>. NVIDIA Reva specializes in enterprise-level speech AI model deployment, covering areas like speech translation, text-to-speech, and speech recognition to enable optimal conversational AI for customers <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.

## Core Development Principles

NVIDIA emphasizes four key categories in model development to ensure high levels of customization and performance:

*   **Robustness** Models are designed to perform well in varying sound environments, including noisy settings, and account for factors like sound quality and environmental contamination <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **Coverage** Addressing diverse customer domains such as medical, entertainment, or call centers, and supporting various language demands like monolingual or multilingual development, dialects, and code-switching <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   **Personalization** Tailoring models to exact customer needs, including [[challenges_in_building_ai_voice_agents | target speaker AI]], word boosting for uncommon vocabulary, and text normalization using FST models <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
*   **Deployment** Optimizing for factors like speed and accuracy trade-offs, model variety, and efficiency, particularly for use on embedded devices <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## Model Architectures for Customization

NVIDIA's speech AI models are built on a foundation that allows for diverse configurations to meet specific demands:

*   **Fast Conformer Architecture** This serves as the fundamental backbone across various decoding platforms. It significantly subsamples conventional time steps, resulting in smaller audio inputs, reduced memory load during training, quicker convergence with less data, and faster inference <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.
*   **Reva Parakeet** Focused on streaming speech recognition, this offering includes CTC (Connectionist Temporal Classification) and TDT (Transformer Decoder Transducer) models. It prioritizes high-speed inference, especially in streaming environments, for tasks like speech recognition, speech translation, and target speaker ASR <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
*   **Reva Canary** This offering prioritizes accuracy and multitask modeling, utilizing fast conformer models. It's designed for scenarios where the highest possible accuracy is required, even if it means less focus on raw speed <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.
*   **Softformer for Speaker Diarization** The successful Parakeet ASR model can be extended for multi-speaker and target speaker scenarios by integrating the Softformer, an end-to-end neural diarizer. This model acts as a bridge between speaker timestamps from diarization and speaker tokens recognizable by the ASR model, enabling "who spoke what and when" functionality <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. It can perform target speaker ASR or single/multi-speaker ASR tasks by feeding optional query audio <a class="yt-timestamp" data-t="07:58:00">[07:58:00]</a>.

## Additional Customization and Readability Models

To further enhance accuracy, customization, and readability, NVIDIA offers several additional models:

*   **Voice Activity Detection (VAD)** Detects speech segments for improved noise robustness <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>.
*   **External Language Models (LM)** Augment ASR transcription for better accuracy and customization, including N-gram based language models <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.
*   **Text Normalization (TN) and Inverse Text Normalization (ITN)** Converts spoken terms to written forms for improved readability, utilizing WFSD-based ITN models <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
*   **Punctuation and Capitalization (PNC)** Adds punctuation and capitalization to transcriptions for better readability, supported by board-based PNC models <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a>.
*   **Speaker Diarization** Identifies multiple speakers in a conversation, with Zooform-based models available in both cascade and upcoming end-to-end configurations <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.

## Addressing Customer Pain Points

[[challenges_in_building_ai_voice_agents | Customization]] is a critical aspect for customers, as each application often requires specific domain knowledge, such as medical terms in healthcare, menu names in food ordering, or handling telephonic and noisy environments in contact centers <a class="yt-timestamp" data-t="14:29:00">[14:29:00]</a>. NVIDIA Reva addresses these challenges by offering customization features at every stage of model development:

*   **Fine-tuning** Acoustic models (Parakeet and Canary based), external language models, punctuation models, and inverse text normalization models can all be fine-tuned <a class="yt-timestamp" data-t="15:00:00">[15:00:00]</a>.
*   **Word Boosting** This feature helps recognize specific product names, jargon, and context-specific knowledge more accurately <a class="yt-timestamp" data-t="15:16:00">[15:16:00]</a>.

## Impact and Deployment

The focus on customization and variety has led to NVIDIA models consistently ranking highly, with the majority of the top five models on the Hugging Face Open ASR leaderboard coming from NVIDIA <a class="yt-timestamp" data-t="09:57:00">[09:57:00]</a>.

[[architecture_and_deployment_of_speech_ai_models | Trained models]] are deployed to NVIDIA Reva through NVIDIA NIM for low-latency, high-throughput inference, powered by NVIDIA Tensor optimizations and the NVIDIA Triton Inference Server <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>. Reva is fully containerized and can scale to hundreds of parallel streams, running on-prem, in any cloud, at the edge, or on embedded platforms. This supports a wide range of applications including contact centers, consumer applications, and video conferencing <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>. NVIDIA NIM provides pre-built containers and industry-standard API support for custom models and optimized inference engines <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>.