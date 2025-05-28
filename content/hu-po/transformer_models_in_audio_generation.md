---
title: Transformer models in audio generation
videoId: SodPUNBFeMY
---

From: [[hu-po]] <br/> 

MusicGen is a recent paper from Meta AI Research that introduces a simple and controllable model for conditional music generation. It was released around the second week of July 2023 <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. The project includes a GitHub repository called "audiocraft", a Colab notebook, and a Hugging Face demo, allowing users to describe music and condition it on text or MP3 files <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. MusicGen is notably implemented using PyTorch 2.0 and Python 3.9 <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The inference code and model weights (around 6 gigabytes, stored using Git LFS) are publicly available <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>, <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Core Concepts

### Conditional Music Generation
The primary task of MusicGen is to generate musical pieces based on a given text description <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. It can also be conditioned on melodic features <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. Generating music is challenging due to the need for modeling long-range sequences and the high sampling rates required for music (e.g., 44 kHz for music vs. 16 kHz for speech) <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Music also contains complex structures from harmonies and melodies across different instruments, and human listeners are highly sensitive to disharmony <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

### Single-Stage [[transformerbased_model_architectures | Transformer-based Model Architectures]]
Unlike prior generative models that often use hierarchical or cascading approaches (e.g., generating a coarse version then refining it), MusicGen uses a single-stage [[transformerbased_model_architectures | Transformer-based model architectures]] for inference <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>, <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>. This means it generates the final product in one step <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>. The model is an autoregressive [[transformerbased_model_architectures | Transformer-based]] decoder <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

### Discrete Music Representation via Tokens
To make audio modeling tractable, MusicGen represents audio signals as multiple streams of discrete tokens <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. This is achieved using the EnCodec audio tokenizer <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>.
<a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>
> [!NOTE] EnCodec
> EnCodec is a convolutional autoencoder that quantizes its latent space using [[quantization_techniques_for_transformers | Residual Vector Quantization]] (RVQ) <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a>. It converts raw audio (e.g., 32 kHz sample rate) into a sequence of tokens at a much lower frame rate (e.g., 50 Hz) <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>, <a class="yt-timestamp" data-t="01:28:02">[01:28:02]</a>.

#### [[quantization_techniques_for_transformers | Residual Vector Quantization]] (RVQ)
RVQ involves multiple quantization levels (e.g., four in MusicGen) <a class="yt-timestamp" data-t="01:28:55">[01:28:55]</a>. Each subsequent quantizer encodes the quantization error (residual) left by the previous one <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>, <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>. The first code book (quantization level) is the most important, containing the overwhelming majority of the signal <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>, <a class="yt-timestamp" data-t="00:36:43">[00:36:43]</a>.

#### Codebook Interleaving Patterns
After quantization, MusicGen works with multiple parallel discrete token sequences, one for each code book <a class="yt-timestamp" data-t="00:35:06">[00:35:06]</a>.
*   **Flattening:** A straightforward approach is to flatten all code books into a single sequence, predicting them sequentially. While this can yield good quality, it significantly increases computational complexity and the number of autoregressive steps <a class="yt-timestamp" data-t="00:45:07">[00:45:07]</a>, <a class="yt-timestamp" data-t="00:46:03">[00:46:03]</a>, <a class="yt-timestamp" data-t="02:00:07">[02:00:07]</a>.
*   **Delayed Interleaving:** MusicGen introduces a "delay interleaving pattern" <a class="yt-timestamp" data-t="01:16:16">[01:16:16]</a>. This strategy applies a delay between code books, allowing some to be predicted in parallel, which saves computation time, especially for long sequences <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>, <a class="yt-timestamp" data-t="00:53:39">[00:53:39]</a>, <a class="yt-timestamp" data-t="00:55:09">[00:55:09]</a>, <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. For example, less important code books (2, 3, 4) might be shifted by one step relative to the most important first code book <a class="yt-timestamp" data-t="02:13:54">[02:13:54]</a>. This approach drastically reduces the number of autoregressive steps compared to flattening <a class="yt-timestamp" data-t="02:00:28">[02:00:28]</a>.

## Conditioning Methods

### Text Conditioning
Text descriptions are turned into an embedding vector using pre-trained text encoders <a class="yt-timestamp" data-t="01:06:08">[01:06:08]</a>. MusicGen experiments with T5, Flan-T5, and CLAP (a joint text-audio representation) <a class="yt-timestamp" data-t="01:06:51">[01:06:51]</a>. The chosen text encoder can significantly impact performance <a class="yt-timestamp" data-t="02:16:02">[02:16:02]</a>.
Text augmentation techniques such as omitting stop words, lemmatization, and word dropout are used <a class="yt-timestamp" data-t="01:39:59">[01:39:59]</a>. Additional metadata like musical key, tempo, and instruments can also be concatenated to the text description <a class="yt-timestamp" data-t="01:40:12">[01:40:12]</a>.

### Melody Conditioning
MusicGen supports conditioning on melodic features from an input audio track <a class="yt-timestamp" data-t="01:08:50">[01:08:50]</a>. This is done by converting the melody into a chromogram (a 2D image representation of audio frequency over time) <a class="yt-timestamp" data-t="01:09:11">[01:09:11]</a>. To create a manageable 1D sequence for conditioning, MusicGen quantizes the chromogram by taking the argmax of the dominant time-frequency bin at each step <a class="yt-timestamp" data-t="01:10:26">[01:10:26]</a>, <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>. This process is unsupervised, avoiding the need for costly supervised data <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>. The chromogram data is then provided as a prefix to the [[transformerbased_model_architectures | Transformer]] input <a class="yt-timestamp" data-t="01:17:36">[01:17:36]</a>.

## Model Architecture
The MusicGen model is an autoregressive [[transformerbased_model_architectures | Transformer-based]] decoder <a class="yt-timestamp" data-t="01:19:22">[01:19:22]</a>.
*   **Positional Embedding:** A sinusoidal embedding is added to encode the current time step within the sequence <a class="yt-timestamp" data-t="01:15:33">[01:15:33]</a>.
*   **Attention Blocks:** Each layer includes a causal self-attention block and a cross-attention block <a class="yt-timestamp" data-t="01:16:13">[01:16:13]</a>, fed with the text/melody conditioning signal <a class="yt-timestamp" data-t="01:17:04">[01:17:04]</a>.
*   **Feedforward Network:** A fully connected block consisting of linear layers and a ReLU activation is used at the end of each layer <a class="yt-timestamp" data-t="01:18:49">[01:18:49]</a>.
*   **Residual Connections and Normalization:** Residual skip connections are used around the fully connected blocks, and layer normalization (pre-norm) is applied to each block before being summed <a class="yt-timestamp" data-t="01:19:40">[01:19:40]</a>.
*   **Output:** The [[transformerbased_model_architectures | Transformer]] decoder outputs logits, which are predictions for the values of the quantized audio tokens within the selected codebook pattern <a class="yt-timestamp" data-t="01:21:07">[01:21:07]</a>. Each codebook has a specific linear layer to output its logits <a class="yt-timestamp" data-t="01:25:02">[01:25:02]</a>.

### Training
MusicGen was trained on 20,000 hours of licensed music, including an internal dataset as well as Shutterstock and Pond5 music data <a class="yt-timestamp" data-t="01:41:18">[01:41:18]</a>.
*   **Audio Crops:** Models are trained on 30-second audio crops sampled randomly from full tracks <a class="yt-timestamp" data-t="01:34:05">[01:34:05]</a>.
*   **Optimization:** Training was conducted for 1 million steps using AdamW optimizer with a batch size of 192 <a class="yt-timestamp" data-t="01:34:10">[01:34:10]</a>. Techniques like decoupled weight decay (0.1) and gradient clipping (1.0) were applied <a class="yt-timestamp" data-t="01:34:21">[01:34:21]</a>.
*   **Learning Rate Schedule:** A cosine learning rate schedule with a 4,000-step warm-up was used <a class="yt-timestamp" data-t="01:36:56">[01:36:56]</a>.
*   **Mixed Precision:** Training uses mixed precision (float16 and bfloat16) to optimize memory and speed <a class="yt-timestamp" data-t="01:38:10">[01:38:10]</a>.
*   **Sampling:** For inference, top-k sampling is employed <a class="yt-timestamp" data-t="01:39:28">[01:39:28]</a>.

## Evaluation and Results
MusicGen evaluates its performance using both objective and subjective metrics on benchmarks like MusicCaps <a class="yt-timestamp" data-t="01:47:26">[01:47:26]</a>.
*   **Objective Metrics:** These include Fréchet Audio Distance (FAD) and KL Divergence <a class="yt-timestamp" data-t="01:48:42">[01:48:42]</a>. A new metric, Chroma Cosine Similarity, was introduced to measure melody alignment <a class="yt-timestamp" data-t="01:58:43">[01:58:43]</a>.
*   **Subjective Metrics:** Human evaluators (via Amazon Mechanical Turk) rated the overall quality (OVL) and relevance to text input (Rel) on a scale of 1-100 <a class="yt-timestamp" data-t="01:53:33">[01:53:33]</a>. Melody match was also rated <a class="yt-timestamp" data-t="01:59:30">[01:59:30]</a>.

### Key Findings:
*   **Model Size:** Scaling the model size (from 300 million to 3.3 billion parameters) shows slightly better objective scores, but human ratings do not significantly improve, suggesting a 300 million parameter model might be sufficient <a class="yt-timestamp" data-t="02:01:11">[02:01:11]</a>, <a class="yt-timestamp" data-t="02:01:27">[02:01:27]</a>.
*   **Codebook Patterns:** While flattening achieves good scores, the delay interleaving pattern provides similar performance at a significantly reduced computational cost <a class="yt-timestamp" data-t="01:59:51">[01:59:51]</a>, <a class="yt-timestamp" data-t="02:04:10">[02:04:10]</a>.
*   **Melody Conditioning Impact:** Adding melody conditioning can degrade objective metrics, but it does not significantly affect human ratings <a class="yt-timestamp" data-t="01:58:30">[01:58:30]</a>. Human evaluation suggests it successfully generates music that follows a given melody <a class="yt-timestamp" data-t="01:59:37">[01:59:37]</a>.
*   **Text Encoder Importance:** The choice of text encoder (e.g., T5 vs. Flan-T5 vs. CLAP) appears to be as, if not more, important than other architectural choices for text-conditioned generation <a class="yt-timestamp" data-t="02:16:02">[02:16:02]</a>.

## Related Work and Ethical Considerations
MusicGen builds upon recent advancements in self-supervised audio representation learning, sequential modeling, and audio synthesis <a class="yt-timestamp" data-t="00:11:02">[00:11:02]</a>. Previous models like MusicLM have used hierarchical approaches <a class="yt-timestamp" data-t="00:46:55">[00:46:55]</a>. The paper notes a trend towards using [[diffusion_models_and_transformers | diffusion models]] for audio generation, sometimes by [[finetuning_with_quantized_models | fine-tuning]] [[transformer_architecture_in_image_processing | image generation models]] (like Stable Diffusion) to generate spectrograms <a class="yt-timestamp" data-t="02:08:24">[02:08:24]</a>.

> [!WARNING] Ethical Challenges
> Large-scale generative models present ethical challenges, including potential lack of diversity in training datasets (e.g., larger proportion of Western-style music) and unfair competition for artists <a class="yt-timestamp" data-t="02:11:14">[02:11:14]</a>. The authors advocate for open research to ensure equal access to these models <a class="yt-timestamp" data-t="02:12:42">[02:12:42]</a>.
> [!INFO] Data Licensing
> Meta AI has an agreement with Shutterstock to use their music data for training, a partnership also extended to OpenAI and LG AI Research <a class="yt-timestamp" data-t="02:11:20">[02:11:20]</a>.