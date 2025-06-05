---
title: Robustness and coverage in AI models
videoId: aDj9sY2RoG8
---

From: [[aidotengineer]] <br/> 

NVIDIA's speech AI team, Nvidia Revo, focuses on enterprise-level speech AI model deployment, aiming to provide customers with the best possible conversational AI [00:00:33]. Their models are designed for low latency and high efficiency, suitable for embedded devices [00:00:56].

When developing AI models, NVIDIA concentrates on four key categories: robustness, coverage, personalization, and deployment cases [00:01:06].

## Focus Areas for Model Development

### Robustness
Robustness addresses whether models function effectively in diverse environments, including noisy versus clean settings [00:01:13]. Considerations include the desired sound quality and environmental factors such as telephony noise or other contaminants [00:01:21].

### Coverage
Coverage pertains to fulfilling the specific domain needs of the customer base [00:01:31]. This includes domains like medical, entertainment, or call center operations [00:01:36]. Language demands are also crucial, encompassing monolingual versus multilingual development, the influence of dialect, and the need to accommodate code switching [00:01:42].

### Personalization
NVIDIA ensures customers receive models tailored to their exact needs [00:01:58]. This may involve focusing on target speaker AI, word boosting for uncommon vocabulary, or using text normalization FST models for precise output [00:02:07].

### Deployment Cases
Deployment focuses on the trade-off between speed and accuracy [00:02:21]. The goal is to determine which is more critical, or if a middle ground is preferred [00:02:26]. Another aspect is whether models should offer high variety or prioritize efficiency [00:02:31].

## Model Architectures and Offerings

NVIDIA employs various [[evolution_and_limitations_of_ai_models | model architectures]] to meet these demands:
*   **CTC Models**: Used for high-speed inference, especially in streaming environments due to their non-auto regression decoding [00:02:51].
*   **R&T/TDT Models**: When higher [[ensuring_ai_accuracy_and_reducing_errors | accuracy]] is needed and non-auto regression is not ideal, these models utilize an encoder with an internal LM for auto regressive streaming setups [00:03:15].
*   **Attention Encoder Decoder Setups**: For even greater [[ensuring_ai_accuracy_and_reducing_errors | accuracy]] without streaming concerns, these are similar to models like Whisper and GPT [00:03:42]. They excel at accommodating multiple tasks within a single model, such as speech translation, timestamp prediction, language identification, and speech recognition, via simple prompt changes [00:04:06].

The fundamental architecture across all decoding platforms is the **Fast Conformer** [00:04:31]. Empirical trials showed that the original conformer model could be significantly subsampled, enabling 80-millisecond compression instead of the conventional 40-millisecond time-step compression [00:04:34]. This allows for smaller audio inputs, lightens memory load during training, and makes training more efficient by achieving quicker convergence with less data [00:04:54]. It also facilitates fast inference by chunking data into 80-millisecond time steps [00:05:12].

NVIDIA's model offerings are split into two options:
*   **Reva Parakeet**: Focuses on streaming speech recognition using CTC and TDT models for fast and efficient recognition, including speech translation and target speaker ASR [00:05:31]. The parakeet ASR model can be extended for multi-speaker and target speaker scenarios by integrating the softformer, an end-to-end neural diarizer [00:06:57]. This unified architecture allows for fine-tuning similar to any ASR model training [00:07:44].
*   **Reva Canary**: Utilizes Fast Conformer models, prioritizing [[ensuring_ai_accuracy_and_reducing_errors | accuracy]] and multi-task modeling over speed, though strong speed is still pursued [00:06:00].

## Improving Model Accuracy and Readability

NVIDIA offers additional models and features to enhance [[ensuring_ai_accuracy_and_reducing_errors | accuracy]], customization, and readability:
*   **Voice Activity Detection (VAD)**: Detects speech segments for better noise robustness using Marblet-based VAD models [00:08:34].
*   **External Language Models**: Leverages n-gram-based language models in Reva pipelines for improved ASR transcription [[ensuring_ai_accuracy_and_reducing_errors | accuracy]] and customization [00:08:47].
*   **Text Normalization (TN) and Inverse Text Normalization (ITN)**: Converts spoken terms to written forms for better readability using WFSD-based ITN models [00:09:01].
*   **Punctuation and Capitalization (PNC)**: Adds punctuation and capitalization to transcriptions for enhanced readability, supported by BERT-based PNC models [00:09:15].
*   **Speaker Diarization**: Identifies multiple speakers in conversations, with Zoo for-based speaker diarization models available in cascade models and upcoming end-to-end models [00:09:28].

## Data Sourcing and Validation

NVIDIA's training approach emphasizes fundamental data development:
*   **Data Sourcing**: Focuses on robustness, multilingual coverage, and dialect sensitivity [00:11:08]. They gather extensive language documentation to guide data acquisition [00:11:23]. Both open-source and proprietary data are incorporated; open-source data supports variety and domain shift, while proprietary data focuses on high-quality entity data [00:11:30]. Pseudo-labeling is used, leveraging transcripts from top-of-the-line commercial models to benefit from community and internal developments [00:11:44].
*   **Training Tools**: The open-source Nemo research toolkit is used for model training, offering GPU maximalization, data bucketing, and high-speed data loading via the Latte backend [00:12:07]. Most data is stored on an object store infrastructure for quick migration between cluster settings [00:12:41].
*   **[[testing_and_evaluation_of_ai_models | Validation]]**: Involves a mix of open-source and proprietary data to ensure models are extensively tested for bias and domain performance across all language categories before reaching end-users, aiming for maximum robustness [00:12:51].

## Deployment and Customization

Trained models are deployed to Nvidia Reva via Nvidia NIM for low latency and high throughput inference [00:13:22]. This high performance is powered by Nvidia Tensor optimizations and the Nvidia Triton inference server [00:13:31]. Nvidia Reva is fully containerized, allowing for easy scaling to hundreds of streams and deployment on-premise, in any cloud, at the edge, or on embedded platforms [00:13:50]. This supports diverse applications like contact centers, consumer applications, and video conferencing [00:14:07].

NVIDIA NIM provides pre-built containers with industry-standard API support for custom models and optimized inference engines [00:14:16]. Customization is a key feature, as real-world scenarios often require domain-specific knowledge, such as medical terms, menu names, or handling telephonic and noisy environments [00:14:29]. Nvidia Reva offers customization features at every stage, including fine-tuning acoustic models (Parakeet and Canary-based), n-gram external language models, punctuation models, and inverse text normalization models [00:14:56]. Word boosting is also offered to improve recognition of product names, jargon, and context-specific knowledge [00:15:16].

This focus on customization and variety has led to the majority of the top five models on the Hugging Face Open ASR leaderboard coming from NVIDIA [00:09:52]. An example demonstrates [[ensuring_ai_accuracy_and_reducing_errors | accurate]] transcription of a song, even in a noisy setting [00:10:19].