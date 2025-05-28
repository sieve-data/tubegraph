---
title: Synthetic Audio Data Sets
videoId: x3fX7v7xjUA
---

From: [[hu-po]] <br/> 

## The Shift from Pipeline Systems to Integrated Models
Traditional spoken dialogue systems relied on a pipeline of independent components: voice activity recognition, speech recognition (ASR), textual dialogue (NLU/LLM), and speech-to-speech (TTS) <a class="yt-timestamp" data-t="00:49:57">[00:49:57]</a>. This cascading approach led to significant latency, often several seconds, making natural conversations impossible <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. Furthermore, crucial [[paralinguistic information such as emotion and accent|transformer_models_in_audio_generation]] was lost as audio was converted to text and then back to speech <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

New models like Moshi and Llama Omni aim to solve this by integrating these components into a single system, often [[transformer_models_in_audio_generation | Transformer-based]] <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. These integrated models require novel training approaches, heavily leveraging [[synthetic data sets for training AI | synthetic data sets]].

## Generating Synthetic Audio Data
The creation of [[synthetic data sets for training AI | synthetic audio data sets]] is a central theme in developing advanced speech-to-speech models like Moshi and Llama Omni <a class="yt-timestamp" data-t="01:29:52">[01:29:52]</a>.

### Process
Research indicates that [[Data Generation for AI Models | synthetic data generation for AI models]] in the audio domain involves converting existing text data into speech data <a class="yt-timestamp" data-t="00:43:56">[00:43:56]</a>. This process often includes:
*   **Text Transformation** <a class="yt-timestamp" data-t="00:35:04">[00:35:04]</a>:
    *   Adding appropriate filler words like "Hey" or "so" <a class="yt-timestamp" data-t="00:35:11">[00:35:11]</a>.
    *   Converting non-text symbols into their corresponding spoken forms <a class="yt-timestamp" data-t="00:35:16">[00:35:16]</a>.
    *   Modifying text-based responses (which tend to be lengthy and complex) to be more suitable for spoken interaction, avoiding non-verbal elements like ordered lists or parentheses <a class="yt-timestamp" data-t="00:35:25">[00:35:25]</a>.
*   **TTS Conversion** <a class="yt-timestamp" data-t="00:35:56">[00:35:56]</a>: Using a Text-to-Speech (TTS) model, such as Cozy Voice 300M sft, to convert the modified text into speech <a class="yt-timestamp" data-t="00:35:59">[00:35:59]</a>. This can involve randomly selecting male or female voices <a class="yt-timestamp" data-t="00:36:31">[00:36:31]</a> or conditioning the TTS on a specific actor's voice to ensure a consistent voice for the AI (e.g., Moshi's voice) <a class="yt-timestamp" data-t="00:37:46">[00:37:46]</a>.
*   **Data Augmentation** <a class="yt-timestamp" data-t="01:28:37">[01:28:37]</a>: Introducing misspellings, noise, or low-quality audio to make the model robust to real-world imperfections <a class="yt-timestamp" data-t="01:29:01">[01:29:01]</a>. Generating questions with false or misleading facts to train the model to correct the user, and creating safety conversations for ethical refusal <a class="yt-timestamp" data-t="01:29:29">[01:29:29]</a>.

### Data Sources and Models
*   **Moshi** <a class="yt-timestamp" data-t="01:23:14">[01:23:14]</a>:
    *   Combines various text data sources like Wikipedia, WikiBooks, WikiSource, WikiNews, and Stack Exchange <a class="yt-timestamp" data-t="01:28:29">[01:28:29]</a>.
    *   Uses different "crawls" (snapshots) of these sources to account for changes over time <a class="yt-timestamp" data-t="01:28:46">[01:28:46]</a>.
    *   Leverages an audio collection of 7 million hours, transcribed with [[open_ai_whisper | Whisper]] <a class="yt-timestamp" data-t="01:18:54">[01:18:54]</a>.
    *   The 2,000-hour Fisher dataset, collected in 2004, is crucial because its conversations were recorded on separate channels, providing ground truth separated streams for training <a class="yt-timestamp" data-t="01:21:04">[01:21:04]</a>. This dataset, originally 8 kHz, is upsampled to 24 kHz using Audio SR (Audio Super Resolution) <a class="yt-timestamp" data-t="01:21:47">[01:21:47]</a>.
    *   Uses a TTS to create 20,000 hours of [[synthetic_data_generation_in_ai_training | synthetic speech data]] for Moshi's consistent voice <a class="yt-timestamp" data-t="01:37:41">[01:37:41]</a>.
    *   Further fine-tuned on 170 hours of natural and scripted conversations for higher quality <a class="yt-timestamp" data-t="01:22:36">[01:22:36]</a>.
*   **Llama Omni** <a class="yt-timestamp" data-t="01:13:14">[01:13:14]</a>:
    *   Uses instruction tuning datasets like 50k instructions from Alpaca and UltraChat <a class="yt-timestamp" data-t="00:36:05">[00:36:05]</a>.
    *   Relies heavily on [[open_ai_whisper | Whisper]] Large V3, which itself was trained on 1 million hours of weakly labeled audio and 4 million hours of pseudo-labeled audio collected using Whisper Large V2 <a class="yt-timestamp" data-t="01:13:05">[01:13:05]</a>. This illustrates the recursive nature of AI development where previous models create data for future ones <a class="yt-timestamp" data-t="01:13:14">[01:13:14]</a>.
    *   Can "get away with" a smaller 200k synthetic speech instruction dataset due to its reliance on robust pre-trained models <a class="yt-timestamp" data-t="01:13:27">[01:13:27]</a>.

## Quality and the Sim-to-Real Gap
A key factor enabling the success of [[synthetic_data_generation_in_ai_training | synthetic audio data sets]] is the minimal "Sim-to-Real Gap" in audio as a modality <a class="yt-timestamp" data-t="01:43:33">[01:43:33]</a>. Unlike vision or robotics, where simulations often struggle to perfectly replicate real-world physics and complexities, synthetic audio can be remarkably close to real audio <a class="yt-timestamp" data-t="01:43:57">[01:43:57]</a>. This means that models trained primarily on [[synthetic data sets for training AI | synthetic data]] can still achieve state-of-the-art performance <a class="yt-timestamp" data-t="01:44:03">[01:44:03]</a>.

## Implications for AI Development
The widespread and effective use of [[synthetic data sets for training AI | synthetic data sets]] in advanced audio models suggests a paradigm shift in AI research <a class="yt-timestamp" data-t="01:31:58">[01:31:58]</a>:
*   **AI Improving Itself** <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>: The process of using existing AI models (like Whisper or TTS models) to generate massive amounts of data for training new AI models is a tangible example of AI "improving itself" <a class="yt-timestamp" data-t="01:33:07">[01:33:07]</a>. This cycle means that research is no longer solely limited by the availability of human-generated data <a class="yt-timestamp" data-t="01:31:40">[01:31:40]</a>.
*   **The "Data Flywheel" is Moot** <a class="yt-timestamp" data-t="01:30:15">[01:30:15]</a>: The traditional venture capital idea that having more users leads to more data, which leads to better AI, forming a "moat" around a company, may no longer hold true <a class="yt-timestamp" data-t="01:30:25">[01:30:25]</a>. If AI can effectively generate its own training data, the need for vast amounts of user-generated data diminishes, potentially democratizing AI development and reducing the power of companies relying on exclusive data access <a class="yt-timestamp" data-t="01:31:38">[01:31:38]</a>.