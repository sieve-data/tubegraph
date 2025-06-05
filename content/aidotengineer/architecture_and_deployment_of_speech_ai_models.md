---
title: Architecture and deployment of speech AI models
videoId: aDj9sY2RoG8
---

From: [[aidotengineer]] <br/> 

Nvidia's approach to speech AI aims to eliminate "awkward AI transcripts" by focusing on robust model development, deployment, and customization <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The Nvidia Riva platform specializes in [[Commercial and enterprise application of open AI models | enterprise-level]] speech AI model deployment, covering speech translation, text-to-speech, and speech recognition <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. The primary focus is on low-latency, highly efficient models suitable for embedded devices <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

## Key Focus Areas in Model Development
Nvidia centers its model development around four main categories <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>:

*   **Robustness**: Models are designed to perform effectively in diverse sound environments, including noisy settings and telephone calls, by accounting for various environmental contamination factors <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Coverage**: Development considers customer domains (e.g., medical, entertainment, call center) and language demands, supporting both monolingual and multilingual development, dialect variations, and code-switching <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Personalization**: Customers can tailor models to their specific needs through features like target speaker AI, word boosting for uncommon vocabulary, and text normalization <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Deployment Cases**: Considerations include the trade-off between speed and accuracy, and whether models should prioritize high variety or [[Cost and efficiency in deploying AI systems | efficiency]] <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Model Architectures

Nvidia utilizes several core model architectures for speech AI <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>:

*   **CTC (Connectionist Temporal Classification) Models**: These are preferred for high-speed inference, especially in streaming environments, due to their non-auto-regressive decoding <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **RNT (Recurrent Neural Transducer) / TDT (Transducer) Models**: When higher accuracy is needed beyond non-auto-regression, RNT/TDT models (an Nvidia variant) are used. They employ an encoder's audio output with an internal language model for auto-regressive streaming setups <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **Attention Encoder-Decoder Setups**: For even greater accuracy, particularly when streaming is not a primary concern, these models (similar to Whisper, ChatGPT, LLMs) are offered <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. They excel at accommodating multiple tasks within a single model, such as speech translation, timestamp prediction, language identification, and speech recognition, often with simple prompt changes <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

### The Fast Conformer Backbone
A unifying tool across Nvidia's decoding platforms is the **Fast Conformer** architecture <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Through empirical trials, it was found that the original Conformer model could be greatly sub-sampled, allowing for 80-millisecond compression instead of the conventional 40-millisecond time step compression <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This innovation leads to:
*   Smaller audio inputs and reduced memory load during training <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.
*   More efficient training with quicker convergence and less data <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
*   Faster inference due to data chunking into 80-millisecond time steps <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.

## Nvidia Reva Offerings
Nvidia's model offerings are split into two main options:

*   **Reva Parakeet**: Focuses on streaming speech recognition cases, utilizing CTC and TDT models for fast and [[Cost and efficiency in deploying AI systems | efficient]] recognition, including target speaker ASR <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Reva Canary**: Incorporates Fast Conformer models, prioritizing accuracy and multitask modeling where speed is less critical <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.

This dual approach provides customers with a comprehensive toolkit offering a mixture of fast, multitasking, or high-accuracy models, emphasizing variety and coverage over a one-model-fits-all solution <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

### Multi-Speaker and Target Speaker ASR
The Parakeet ASR model can be extended to multi-speaker and target speaker scenarios by integrating the Softformer diarization model <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. Softformer is an end-to-end neural diarizer that identifies "who comes first" <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. It acts as a bridge between speaker time stamps from diarization and speaker tokens recognizable by the ASR model <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. By fusing ASR encoder embedding and Softformer embedding through a speaker kernel, it addresses the "who spoke what and when" problem <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This unified architecture can be fine-tuned with simple ASR model training objectives <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

Depending on whether an optional query audio is fed, the model can conduct target speaker ASR or single/multi-speaker ASR tasks <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. The unified model architecture can be applied in both parallel joint and cascade systems <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

## Additional Models and Enhancements
To further improve accuracy, customization, and readability, Nvidia offers additional models <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>:
*   **Voice Activity Detection (VAD)**: Detects speech segments for better noise robustness, available in MarbleNet-based VAD models <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>.
*   **External Language Models**: Encompasses N-gram based language models within Reva pipelines for enhanced ASR transcription accuracy and customization <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>.
*   **Text Normalization (TN) and Inverse Text Normalization (ITN)**: Converts spoken terms to written forms for readability, using WFST-based ITN models <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Punctuation Capitalization (PNC)**: Adds punctuation and capitalization to transcriptions for better readability, supported by BERT-based PNC models <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>.
*   **Speaker Diarization**: Identifies multiple speakers in a conversation, available as a cascade system with Zoho-based models, and upcoming end-to-end models <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.

This level of customization contributes to Nvidia models frequently ranking among the top on leaderboards like the Hugging Face Open ASR leaderboard <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.

## Training and Data Philosophy
Nvidia emphasizes fundamental [[Best Practices for Building AI Systems | data development practices]] <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>:
*   **Data Sourcing**: Focuses on robustness, multilingual coverage, and dialect sensitivity <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Extensive language documentation is gathered to guide data acquisition <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
*   **Data Integration**: Combines both open-source data (for variety and domain shift) and proprietary data (for high-quality entity data) <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Pseudo Labeling**: Utilizes transcripts from top commercial models to benefit from community and internal developments <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.

For training, standard, openly available tools are primarily used <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>. The **Nemo research toolkit**, an open-source library, is employed for model training, offering GPU maximalization, data bucketing, and high-speed data loading via the Latte backend <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. Data is stored on an object store infrastructure to facilitate quick migration between different cluster settings <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.

Validation involves a mix of open-source and proprietary data to ensure models are extensively tested for bias and domain across various language categories before reaching end-users, ensuring maximum robustness <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.

## Deployment and Customization
Trained models are deployed through Nvidia Riva using **Nvidia NIM** for low latency and high throughput inference <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>. High-performance inference is enabled by Nvidia Tensor optimizations and the Nvidia Triton Inference Server <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>.

Nvidia Riva is fully containerized and designed for [[Building scalable AI systems | scalability]], capable of handling hundreds of parallel streams <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. It can be run on-premise, in any cloud, at the edge, or on embedded platforms <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>, supporting diverse applications such as contact centers, consumer applications, and video conferencing <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. Nvidia NIM provides pre-built containers and industry-standard API support for custom models and optimized inference engines <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

Customer customization is a critical focus, as every application demands domain-specific knowledge (e.g., medical terms, menu names, telephonic conditions) <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. Nvidia Riva offers customization features at every stage <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>:
*   Fine-tuning of acoustic models (Parakeet and Canary-based models) <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   Fine-tuning of external language models, punctuation models, and inverse text normalization models <a class="yt-timestamp" data-t="00:15:10">[00:15:10]</a>.
*   Word boosting for improved recognition of product names, jargon, and context-specific knowledge <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

### Getting Started
Nvidia Riva models are available through Nvidia NIM <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. More information and available models can be found at `build.envidia.com/explore/speech` <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. Resources include a quick starter guide, a developer forum, and a fine-tuning guide for models within the Nemo frameworks <a class="yt-timestamp" data-t="00:15:57">[00:15:57]</a>.