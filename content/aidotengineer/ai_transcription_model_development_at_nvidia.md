---
title: AI transcription model development at Nvidia
videoId: aDj9sY2RoG8
---

From: [[aidotengineer]] <br/> 

Nvidia's approach to AI transcription model development focuses on delivering highly efficient and robust conversational AI solutions for enterprise-level applications <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The development process emphasizes deployment and customization for a diverse customer base <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. These models are designed for low latency and high efficiency, suitable for deployment on embedded devices <a class="yt-timestamp" data="00:00:59">[00:00:59]</a>.

## Core Development Principles

Nvidia's model development at Nvidia focuses on four main categories:
*   **Robustness** <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>: Ensuring models perform well in both noisy and clean environments, accounting for varying sound quality, telephone audio, and environmental contamination factors <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>.
*   **Coverage** <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>: Addressing diverse customer domains (medical, entertainment, call center), language demands (monolingual or multilingual), dialects, and code-switching <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Personalization** <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>: Customizing models to meet specific customer needs, including target speaker AI, word boosting for uncommon vocabulary, and text normalization using FST models <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Deployment** <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>: Optimizing for the trade-off between speed and accuracy, and balancing model variety with efficiency for specific use cases <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

## Model Architectures

Nvidia utilizes several model architectures to achieve its goals:

*   **CTC (Connectionist Temporal Classification) Models** <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>: These non-autoregressive models are optimal for high-speed inference, particularly in streaming environments where data can be chunked and processed efficiently <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **R&T (Recurrent Neural Network Transducer) or TDT (Transformer Transducer) Models** <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>: For higher accuracy where non-autoregression is insufficient, these models use an encoder's audio output with an internal Language Model (LM) to enable autoregressive streaming setups <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Attention Encoder-Decoder Setups** <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>: These are used when maximum accuracy is required and streaming is not the primary concern <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>. They excel at accommodating multiple tasks within a single model, such as speech translation, timestamp prediction, language identification, and speech recognition, through simple prompt changes <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Fast Conformer** <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a>: This is the fundamental architecture unifying all decoding platforms <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Through empirical trials, it was found that the original conformer model can be subsampled further, achieving 80-millisecond compression instead of the conventional 40-millisecond step <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This reduces memory load during [[training_and_validation_of_nvidia_models | training]], increases training efficiency by allowing quicker convergence with less data, and enables faster inference by chunking data into 80-millisecond timesteps <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.

## Nvidia Reva Offerings

Nvidia's model offerings are split into two primary options:

*   **Reva Parakeet** <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>: Focuses on streaming speech recognition cases, utilizing CTC and TDT models <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. It is designed for fast and efficient recognition for tasks like speech recognition, speech translation, and target speaker ASR <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
*   **Reva Canary** <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>: Incorporates the Fast Conformer models and prioritizes accuracy and multitask modeling <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. It aims for the best possible accuracy, with speed being a secondary consideration <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

The overarching philosophy is to provide a variety of models to meet specific customer needs, rather than a "one model fits all" approach <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Advanced Capabilities

### Multi-speaker and Target Speaker ASR
The Parakeet ASR model can be extended for multi-speaker and target speaker scenarios by integrating the Softformer model <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. The Softformer is an end-to-end neural diarizer that follows the "rival timing principle" (who comes first) <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. It acts as a bridge between speaker timestamps from diarization and speaker tokens recognizable by the ASR model <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. The ASR encoder embedding and Softformer embedding are fused via a speaker kernel to address the "who spoke what and when" problem <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This unified architecture can be fine-tuned with a simple objective similar to ASR model training <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a> and can perform target speaker ASR or multi-speaker ASR depending on whether an optional query audio is provided <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This architecture can be applied in both parallel joint and cascade system manners <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### Ancillary Models for Accuracy & Readability
Additional models are offered to improve overall accuracy, customization, and readability:
*   **Voice Activity Detection (VAD)** <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>: Detects speech segments for better noise robustness, with models based on Marblet <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **External Language Models (LM)** <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>: Enhance ASR transcription for better accuracy and customization, including N-gram based LMs in the Reva pipelines <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Text Normalization and Inverse Text Normalization (ITN)** <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>: Convert spoken terms to written forms for readability, using WFSD-based ITN models <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Punctuation and Capitalization (PNC)** <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>: Adds punctuation and capitalization to transcriptions, supported by word-based PNC models <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.
*   **Speaker Diarization** <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>: Identifies multiple speakers in a conversation, with Zooform-based speaker diarization models available in both cascade and upcoming end-to-end models <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.

## Development Process

Nvidia's development process emphasizes robust data sourcing, efficient training, and thorough validation to ensure high-quality models.

### Data Sourcing
[[training_and_validation_of_nvidia_models | Training and validation of Nvidia models]] involves a focus on robustness and multilingual coverage with dialect sensitivity <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Nvidia incorporates both open-source and proprietary data:
*   **Open Source Data** <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>: Allows for variety and domain shift.
*   **Proprietary Data** <a class="yt-timestamp" data-t="00:11:37">[00:11:37]</a>: Focuses on high-quality entity data.

Pseudo-labeling is used, where transcripts from top-of-the-line commercial models are utilized to benefit from community and internal developments <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

### Training
[[training_and_validation_of_nvidia_models | Training and validation of Nvidia models]] utilizes standard, publicly available tools and processes <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>. The [[nvidias_nemo_microservices_for_generative_ai | Nemo research toolkit]], an open-source library, is used for model training <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. It includes tools for GPU maximization, data bucketing, and high-speed data loading via the Latte backend <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. The focus is on maximizing data utilization and ingestion speed across different settings <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. Most data is stored on an object store infrastructure for quick migration between cluster settings <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

### Validation
Validation also incorporates a mix of open-source and proprietary data to ensure comprehensive coverage <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. Before models reach end-users, they undergo extensive bias and domain testing across all language categories to ensure maximum robustness <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>.

## Deployment & Customization

### Nvidia Reva and NIM
Trained models are deployed to Nvidia Reva via [[nvidias_nemo_microservices_for_generative_ai | Nvidia NIM]] for low-latency and high-throughput inference <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. High-performance inference is powered by Nvidia Tensor optimizations and the Nvidia Triton inference server <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Nvidia Reva offers gRPC-based microservices for low-latency streaming and high-throughput offline use cases <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. It is fully containerized, allowing it to scale to hundreds of parallel streams and run on-prem, in any cloud, at the edge, or on embedded platforms <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This supports a variety of applications, including contact centers, consumer applications, and video conferencing <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. [[nvidias_nemo_microservices_for_generative_ai | Nvidia NIM]] also offers pre-built containers with industry-standard API support for custom models and optimized inference engines <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

### Customization Features
[[finetuning_and_production_stability_of_open_ai_models | Finetuning and production stability of open AI models]] is crucial, as real-world scenarios often require domain-specific knowledge (e.g., medical terms, menu names) and accommodation for telephonic or noisy environments <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. Nvidia Reva provides customization features at every stage <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>:
*   **Acoustic Model Fine-tuning** <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>: For both Parakeet-based and Canary-based models.
*   **External Language Model Fine-tuning** <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>: For N-gram, punctuation, and inverse text normalization models.
*   **Word Boosting** <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>: To improve recognition of product names, jargon, and context-specific knowledge <a class="yt-timestamp" data-t="00:15:24">[00:15:24]</a>.

The focus on customization and variety has led to Nvidia models frequently appearing among the top-ranked on the Hugging Face Open ASR leaderboard <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.