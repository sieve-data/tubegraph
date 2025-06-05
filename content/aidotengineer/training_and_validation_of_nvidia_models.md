---
title: Training and validation of Nvidia models
videoId: aDj9sY2RoG8
---

From: [[aidotengineer]] <br/> 

Nvidia's approach to developing AI models for speech AI focuses on creating highly efficient, low-latency, and robust models for enterprise-level deployment <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The team, known as Nvidia Riva, provides solutions for speech translation, text-to-speech development, and speech recognition, aiming to offer the best possible conversational AI <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## Model Development Philosophy

Nvidia's model development is guided by four key categories <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>:

*   **Robustness**: Models are designed to perform well in both noisy and clean environments, accounting for factors like telephone sound quality and environmental contamination <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Coverage**: Development considers various domains (medical, entertainment, call centers), language demands (monolingual or multilingual), dialects, and code-switching <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Personalization**: Customers can tailor models to their specific needs, including target speaker AI, word boosting for uncommon vocabulary, and text normalization using FST models <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Deployment**: Focus is placed on the trade-off between speed and accuracy, and whether models should prioritize high variety or efficiency for specific embedded devices <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

This philosophy emphasizes variety and coverage rather than a one-model-fits-all approach <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.

## Model Architectures

Nvidia utilizes several model architectures, often unified by a core component:

*   **CTC Models**: Used for high-speed inference, especially in streaming environments, due to their non-auto-regressive decoding <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **RNT/TDT Models**: An Nvidia variant of RNT, these models use an encoder's audio output with an internal language model for auto-regressive streaming setups, balancing speed and accuracy <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **Attention Encoder-Decoder Setups**: Offered for higher accuracy when streaming is not a primary concern. These models (similar to Whisper, ChatGPT, LLMs) excel at accommodating multiple tasks within a single model, such as speech translation, timestamp prediction, language identification, and speech recognition <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.

The unifying tool across these decoding platforms is the **Fast Conformer** architecture <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Through empirical trials, it was found that the original Conformer model could be significantly subsampled, achieving 80-millisecond compression instead of the conventional 40-millisecond time step compression <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>. This innovation allows for smaller audio inputs, lightens memory load during training, makes training more efficient with quicker convergence (requiring less data), and enables faster inference due to 80-millisecond time steps <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

Nvidia's model offerings are split into two options:
*   **Riva Parakeet**: Focuses on streaming speech recognition using CTC and TDT models for fast and efficient recognition, including speech translation and target speaker ASR <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Riva Canary**: Utilizes Fast Conformer models for high accuracy and multitask modeling, prioritizing accuracy over speed <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

Additional models are offered to improve accuracy, [[Custom Model Building and Code Evaluation for AI Systems | customization]], and readability <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>:
*   **Voice Activity Detection (VAD)**: Detects speech segments for better noise robustness using MarbleNet-based VAD models <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **External Language Models**: EnGram-based models enhance ASR transcription accuracy and allow for [[Custom Model Building and Code Evaluation for AI Systems | customization]] <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Text Normalization (TN) and Inverse Text Normalization (ITN)**: Convert spoken terms to written forms for readability using WFST-based ITN models <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Punctuation and Capitalization (PNC)**: Adds punctuation and capitalization to transcriptions for readability using BERT-based PNC models <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Speaker Diarization**: Identifies multiple speakers in a conversation, with models like Zoo for based speaker diarization available in cascade systems <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. The Parakeet ASR model can be extended for multi-speaker and target speaker scenarios by integrating the [[AI transcription model development at Nvidia | Softformer]] diarization model, an end-to-end neural diarizer following the arrival time principle <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. This Softformer acts as a bridge between speaker timestamps from diarization and speaker tokens recognizable by the ASR model <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## Data Collection and Training Techniques for AI Models

[[Data Collection and Training Techniques for AI Models | Data collection]] and training at Nvidia focus on fundamentals to meet demand <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
*   **Data Sourcing**: Emphasis is placed on robustness, multilingual coverage, and dialect sensitivity <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Extensive language documentation is gathered to define appropriate data spans <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
*   **Data Types**: Both open-source and proprietary data are incorporated. Open-source data aids in achieving variety and domain shift, while proprietary data ensures high-quality entity data <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Pseudo-labeling**: Transcripts from top-of-the-line commercially available models are used to benefit from community and internal developments <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

For [[Innovations in AI training methods and new benchmarks | training]], standard available tools are primarily used <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. The Nemo research toolkit, an open-source library, is utilized for model training <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. Nemo provides tools for GPU maximalization, data bucketing, and high-speed data loading via the Latte backend <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. This approach allows for maximizing data and ingestion speed across different settings <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>. Most data is stored on an object store infrastructure, enabling quick migration between cluster settings <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

## Testing and Evaluation of AI Models

[[Testing and evaluation of AI models | Validation]] mirrors the training philosophy, focusing on a diverse mixture of open-source and proprietary data <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. Before models reach end-users, they undergo extensive bias and domain testing across all possible language categories <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This rigorous [[Testing and evaluation of AI models | testing]] ensures models are as robust as possible <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

## Deployment and Customization

Trained models are deployed via Nvidia Riva through Nvidia NIM for low-latency and high-throughput inference <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. High-performance inference is powered by Nvidia Tensor optimizations and the Nvidia Triton inference server <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. These services are available for gRPC-based microservices, supporting both low-latency streaming and high-throughput offline use cases <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

Nvidia Riva is fully containerized and can scale to hundreds of parallel streams, deployable on-premises, in any cloud, at the edge, or on embedded platforms <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. This supports a variety of applications including contact centers, consumer applications, and video conferencing <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>. Nvidia NIM offers pre-built containers with industry-standard API support for [[Custom Model Building and Code Evaluation for AI Systems | custom models]] and optimized inference engines <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.

[[Finetuning and production stability of open AI models | Customization]] is a significant focus, as real-world scenarios often require domain-specific knowledge (e.g., medical terms, menu names, telephonic conditions) <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>. Nvidia Riva offers [[Finetuning and production stability of open AI models | customization]] features at every stage <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>:
*   [[Finetuning and production stability of open AI models | Fine-tuning]] acoustic models from Parakeet or Canary base models <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   [[Finetuning and production stability of open AI models | Fine-tuning]] EnGram external language models, punctuation models, and inverse text normalization models <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
*   Offering word boosting to improve recognition of product names, jargon, and context-specific knowledge <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

This comprehensive toolkit, focusing on customization and variety, has led to Nvidia models dominating the Hugging Face Open ASR leaderboard, with the majority of top-five models originating from Nvidia <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.