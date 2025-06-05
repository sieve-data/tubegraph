---
title: Nvidia AI model deployment and architecture
videoId: aDj9sY2RoG8
---

From: [[aidotengineer]] <br/> 

Nvidia focuses on the development and deployment of enterprise-level speech AI models <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Their aim is to enable customers to deliver the best possible conversational AI solutions <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. Key aspects of their work include speech translation, text-to-speech development, and speech recognition <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. A primary focus is on creating low-latency, highly efficient models suitable for embedded devices <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## Model Development Philosophy

Nvidia's model development revolves around four core categories <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>:

*   **Robustness**: Models are designed to perform effectively in both noisy and clean environments <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, accounting for sound quality, telephone audio, and environmental contamination <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Coverage**: Development considers various domains like medical, entertainment, and call centers <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. They address language demands (monolingual or multilingual), dialect variations, and code-switching <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Personalization**: Models are tailored to specific customer needs, which can involve target speaker AI, word boosting for uncommon vocabulary, or text normalization using FST models <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Deployment**: This category focuses on the trade-off between speed and accuracy <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>, and whether models should prioritize high variety or efficiency <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## Model Architectures

Nvidia utilizes several model types to achieve its goals <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>:

*   **CTC Models**: Used for high-speed inference, especially in streaming environments due to their non-auto aggressive decoding <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **RNT (Recurrent Neural Transducer) / TDT Models**: Employed when higher accuracy is needed than what non-auto aggressive methods can provide <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. These use an audio encoder output with an internal language model for auto aggressive streaming setups <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Attention Encoder-Decoder Setups**: Offered for maximum accuracy when streaming is not a primary concern <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. These models, akin to Whisper and LLMs, are effective for multiple tasks within a single model, including speech translation, timestamp prediction, language identification, and speech recognition <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

The fundamental architecture unifying these decoding platforms is the **Fast Conformer** <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>. Through empirical trials, Nvidia found that the conformer model can be significantly subsampled, achieving 80-millisecond compression instead of the conventional 40-millisecond step <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. This innovation leads to smaller audio inputs, reduced memory load during training, more efficient training with quicker convergence, and faster inference due to 80-millisecond time steps <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

## Riva Model Offerings

Nvidia's model offerings are divided into two main categories:

*   **Riva Parakeet**: Focuses on streaming speech recognition cases, utilizing CTC and TDT models <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. It is designed for fast and efficient recognition, handling speech recognition, speech translation, and target speaker ASR <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.
    *   The Parakeet ASR model can be extended to multi-speaker and target speaker scenarios by integrating the **Diarization Model Softformer** <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. The Softformer is an end-to-end neural diarizer that identifies who speaks first <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. It acts as a bridge between speaker timestamp information from diarization and speaker tokens recognizable by the ASR model <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. By fusing ASR encoder embedding and Softformer embedding through a speaker kernel, it addresses the "who spoke what and when" problem <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. This unified architecture can be applied in parallel joint manner or as a cascade system <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Riva Canary**: Utilizes Fast Conformer models, emphasizing accuracy and multitask modeling <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. It aims for the best possible accuracy, with speed being a secondary consideration <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

Nvidia's approach prioritizes providing the right model for the specific need, focusing on variety and coverage rather than a "one model fits all" philosophy <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

## Additional Models and Tools for Accuracy and Customization

To further enhance accuracy, customization, and readability, Nvidia offers additional models <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>:

*   **Voice Activity Detection (VAD)**: Detects speech segments to improve noise robustness <a class="yt-timestamp" data-t="00:08:34">[00:08:34]</a>, including MarbleNet-based VAD models <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.
*   **External Language Models**: Resource for ASR transcription, improving accuracy and customization <a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>, including n-gram based language models in Riva pipelines <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
*   **Text Normalization and Inverse Text Normalization (ITN)**: Converts spoken terms to written forms for better readability <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>, including WFST-based ITN models <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.
*   **Punctuation and Capitalization (PNC)**: Adds punctuation and capitalization to transcriptions for improved readability <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>, supporting BERT-based PNC models <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Speaker Diarization**: Identifies multiple speakers in a conversation <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>, with Zoo-based speaker diarization models available in cascade models and upcoming end-to-end models <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

This level of customization has contributed to Nvidia models ranking highly on leaderboards like the Hugging Face Open ASR <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>.

## Training Process

Nvidia's training approach emphasizes foundational principles <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>:

*   **Data Sourcing**: Focuses on robustness, multilingual coverage, and dialect sensitivity <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. They acquire extensive language documentation to guide data selection <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>. Both open-source data (for variety and domain shift) and proprietary data (for high-quality entity data) are incorporated <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Pseudo-labeling**: Involves using top-tier commercial models to generate transcripts, leveraging community and internal developments <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.
*   **Training Tools**: The open-source **Nemo research toolkit** is used for model training <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>. It includes tools for GPU maximalization, data bucketing, and high-speed data loading via the Latte backend <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. Data is often stored on object store infrastructure for quick migration between cluster settings <a class="yt-timestamp" data-t="00:12:41">[00:12:41]</a>.
*   **Validation**: Involves a mix of open-source and proprietary data to ensure extensive bias and domain testing across language categories before models reach end-users <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.

## Deployment

Trained models are deployed through **Nvidia Riva** via **Nvidia NIM** for low-latency and high-throughput inference <a class="yt-timestamp" data-t="00:13:22">[00:13:22]</a>.

*   **High Performance**: Inference is powered by Nvidia Tensor optimizations and the Nvidia Triton inference server <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Accessibility**: Available as a gRPC-based microservice for low-latency streaming and high-throughput offline use cases <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   **Scalability**: Nvidia Riva is fully containerized and can easily scale to hundreds of parallel streams <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **Flexibility**: It can run on-prem, in any cloud, at the edge, or on embedded platforms to support diverse applications like contact centers, consumer applications, and video conferencing <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
*   **Nvidia NIM**: Offers pre-built containers and industry-standard API support for custom models and optimized inference engines <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.

### Customization in Deployment

Customization is a critical aspect, as every application often requires specific domain knowledge <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a> (e.g., medical terms, menu names, telephonic conditions) <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>. Nvidia Riva offers customization features at every stage <a class="yt-timestamp" data-t="00:14:56">[00:14:56]</a>:

*   **Fine-tuning**: Acoustic models (Parakeet and Canary-based), external language models (n-gram), punctuation models, and inverse text normalization models can be fine-tuned <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   **Word Boosting**: Offered to improve recognition of product names, jargon, and context-specific knowledge <a class="yt-timestamp" data-t="00:15:18">[00:15:18]</a>.

## Resources

Nvidia Riva models are available through Nvidia NIM <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>. Users can find more available models and quick start guides at `build.nvidia.com/explore/speech` <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>, along with developer forums and fine-tuning guides for models in the Nemo frameworks <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.