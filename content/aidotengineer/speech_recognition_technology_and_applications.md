---
title: Speech recognition technology and applications
videoId: aDj9sY2RoG8
---

From: [[aidotengineer]] <br/> 

Nvidia Speech AI focuses on enterprise-level speech AI model deployment. Their goal is to enable customers to provide the best possible [[conversational_ai_applications_in_business | conversational AI]] at an enterprise level <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>. This includes speech translation, text-to-speech development, and speech recognition <a class="yt-timestamp" data-t="00:39:00">[00:39:00]</a>. A primary focus is on low-latency, highly efficient models that can be used on embedded devices <a class="yt-timestamp" data-t="00:56:00">[00:56:00]</a>.

## Core Principles of Nvidia Speech AI Model Development

Nvidia's model development revolves around four key categories <a class="yt-timestamp" data-t="01:08:00">[01:08:00]</a>:

*   **Robustness**: Models are designed to work effectively in both noisy and clean environments, accounting for varying sound quality and environmental contamination factors like telephony <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.
*   **Coverage**: The aim is to meet diverse customer demands across various domains (e.g., medical, entertainment, call center-based) and language demands, including monolingual, multilingual, dialectal variations, and code-switching <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.
*   **Personalization**: Customers can tailor models to their exact needs, which may involve [[voice_cloning_and_finetuning_techniques | target speaker AI]], word boosting for uncommon vocabulary, or text normalization FST models for specific outputs <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>.
*   **Deployment Cases**: Considerations include the trade-off between speed and accuracy, and whether models should prioritize high variety or efficiency <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.

## Model Architectures

Nvidia utilizes several model types for speech AI applications <a class="yt-timestamp" data-t="02:41:00">[02:41:00]</a>:

*   **CTC (Connectionist Temporal Classification) Models**: These models are favored for high-speed inference, especially in streaming environments, due to their non-auto-regressive decoding <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   **RNT (Recurrent Neural Transducer) / TDT Models**: When higher accuracy is required beyond what non-auto-regression can provide, RNT or the Nvidia-developed TDT variants are used. These feature auto-regressive streaming setups by integrating an audio encoder with an internal language model <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.
*   **Attention Encoder-Decoder Setups**: For maximum accuracy, where streaming is not a primary concern, these models (like Whisper, ChatGPT, LLM) are employed. They are highly accurate, accommodate multiple tasks within a single model (e.g., speech translation, timestamp prediction, language identification, speech recognition) with simple prompt changes, and require less focus on alignment <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   **Fast Conformer**: This serves as the fundamental architecture across all decoding platforms. It significantly subsamples the original conformer model, enabling 80-millisecond compression instead of the conventional 40-millisecond step. This reduces memory load during training, makes training more efficient with quicker convergence on less data, and allows for very fast inference due to chunking data into smaller time steps <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.

### Nvidia Reva Offerings

Nvidia's model offerings are split into two primary options <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>:

*   **Reva Parakeet**: This focuses on streaming speech recognition cases, utilizing CTC and TDT models for fast and efficient recognition, [[voice_ai_and_its_applications_in_enhancing_customer_experience | speech translation]], and [[voice_cloning_and_finetuning_techniques | target speaker ASR]] <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.
*   **Reva Canary**: This option employs fast conformer models, prioritizing accuracy and multitask modeling, even if it means slightly less focus on speed <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>.

The overarching philosophy is to provide a variety of models to meet specific needs rather than a "one model fits all" approach <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

## Enhancements for Accuracy and Customization

Additional models and features are offered to improve accuracy, customization, and readability of transcripts <a class="yt-timestamp" data-t="08:27:00">[08:27:00]</a>:

*   **Speaker Diarization (Softformer)**: The Parakeet ASR model can be extended for multi-speaker and [[voice_cloning_and_finetuning_techniques | target speaker]] scenarios using the Softformer. This end-to-end neural diarizer functions on the "who comes first" principle, bridging speaker timestamps from diarization with speaker tokens recognized by the ASR model <a class="yt-timestamp" data-t="07:00:00">[07:00:00]</a>. It can be fine-tuned with a simple objective similar to ASR model training <a class="yt-timestamp" data-t="07:44:00">[07:44:00]</a>.
*   **Voice Activity Detection (VAD)**: Detects speech segments to improve noise robustness. Nvidia offers VAD models based on MarbleNet <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.
*   **External Language Models (LMs)**: Resources like n-gram-based language models are used to enhance ASR transcription for better accuracy and customization <a class="yt-timestamp" data-t="08:47:00">[08:47:00]</a>.
*   **Text Normalization (TN) and Inverse Text Normalization (ITN)**: Converts spoken terms to written forms for improved readability. WFST-based ITN models are supported <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>.
*   **Punctuation and Capitalization (PNC)**: Adds punctuation and capitalization to transcriptions for better readability, using BERT-based PNC models <a class="yt-timestamp" data-t="09:14:00">[09:14:00]</a>.
*   **Speaker Diarization**: Identifies multiple speakers in a conversation. ZooFormer-based speaker diarization models are available in cascade systems, with upcoming end-to-end models <a class="yt-timestamp" data-t="09:28:00">[09:28:00]</a>.
*   **Word Boosting**: Offered to improve recognition of product names, jargon, and context-specific knowledge <a class="yt-timestamp" data-t="15:16:00">[15:16:00]</a>.

Nvidia's approach to customization and variety contributes to its strong performance, with the majority of top models on the Hugging Face Open ASR leaderboard coming from Nvidia <a class="yt-timestamp" data-t="09:52:00">[09:52:00]</a>.

> "Living for the now. Long as time allows. I'mma keep on switching different styles. Keep creative on a cloud. Sweat is on my brow cuz I'm running on these tracks just to keep them running back. You know the drill back and I've been practicing my craft. Dedicate this to Kobe. What could be a bigger legacy to" <a class="yt-timestamp" data-t="10:25:00">[10:25:00]</a>
> — A demonstration of accurate transcription even in a noisy setting <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>.

## Development Process

Nvidia focuses on fundamental practices for data development and training <a class="yt-timestamp" data-t="11:06:00">[11:06:00]</a>.

*   **Data Sourcing**:
    *   Emphasis on robustness, multilingual coverage, and dialect sensitivity <a class="yt-timestamp" data-t="11:14:00">[11:14:00]</a>.
    *   Incorporation of both open-source data (for variety and domain shift) and proprietary data (for high-quality entity data) <a class="yt-timestamp" data-t="11:30:00">[11:30:00]</a>.
    *   Utilization of pseudo-labeling, where transcripts are generated using top-of-the-line commercial models, benefiting from community advancements <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>.
*   **Training**:
    *   The Nemo research toolkit, an open-source library, is used for model training <a class="yt-timestamp" data-t="12:07:00">[12:07:00]</a>.
    *   Tools within Nemo support GPU maximalization, data bucketing, and high-speed data loading via the Latte backend <a class="yt-timestamp" data-t="12:20:00">[12:20:00]</a>.
    *   Data is stored on an object store infrastructure for quick migration between different cluster settings <a class="yt-timestamp" data-t="12:41:00">[12:41:00]</a>.
*   **Validation**:
    *   A mixture of open-source and proprietary data is used <a class="yt-timestamp" data-t="12:52:00">[12:52:00]</a>.
    *   Rigorous bias and domain testing are conducted across all language categories to ensure model robustness before release to end-users <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>.

## Deployment with Nvidia Reva and NIM

Trained models are deployed through Nvidia Reva using Nvidia NIM for low-latency and high-throughput inference <a class="yt-timestamp" data-t="13:22:00">[13:22:00]</a>.

*   **High Performance Inference**: Powered by Nvidia TensorRT optimizations and the Nvidia Triton Inference Server <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>.
*   **Availability**: Offered via gRPC-based microservices for low-latency streaming and high-throughput offline use cases <a class="yt-timestamp" data-t="13:42:00">[13:42:00]</a>.
*   **Scalability**: Nvidia Reva is fully containerized and can easily scale to hundreds of parallel streams <a class="yt-timestamp" data-t="13:50:00">[13:50:00]</a>.
*   **Deployment Environments**: Can be run on-premise, in any cloud, at the edge, or on embedded platforms <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.
*   **Applications**: Supports various applications including contact centers, consumer applications, and video conferencing <a class="yt-timestamp" data-t="14:06:00">[14:06:00]</a>.
*   **Nvidia NIM**: Provides pre-built containers, industry-standard API support for custom models, and optimized inference engines <a class="yt-timestamp" data-t="14:16:00">[14:16:00]</a>.

Customization is a key feature in real-world scenarios due to varying domain knowledge requirements (e.g., medical terms, menu names, telephonic conditions, noisy environments in contact centers) <a class="yt-timestamp" data-t="14:27:00">[14:27:00]</a>. Nvidia Reva offers customization at every stage, allowing fine-tuning of acoustic models (Parakeet and Canary-based), external language models, punctuation models, and inverse text normalization models <a class="yt-timestamp" data-t="14:55:00">[14:55:00]</a>.

## Getting Started

Nvidia Reva models are available in Nvidia NIM. Users can explore available models at `build.envidia.com/explore/speech` <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>. Resources include a quick start guide, developer forum, and a fine-tuning guide for models within the Nemo framework <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>.