---
title: Protein structure prediction using large language models
videoId: I_ll4L9TpU4
---

From: [[hu-po]] <br/> 

Meta's research introduces a new approach to the evolutionary scale prediction of atomic protein structure using a [[Large Language Models and their applications | language model]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. This effort positions Meta as a significant contender in using deep learning for biological applications, akin to DeepMind's AlphaFold <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. The core idea involves direct inference of protein structure from its primary amino acid sequence using [[Large Language Models and their applications | large language models]] <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## ESM2: The Protein Language Model

ESM2 is built upon [[Large Language Models and their applications | large-scale attention-based architectures]], specifically Transformer architectures, which are prevalent in [[Large Language Models and their applications | LLMs]] <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Training Objective

ESM2 is trained using a masked language modeling objective <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>. This involves masking out parts of a protein sequence and training the model to predict the missing amino acids <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>. This approach is similar to the "next token prediction" used to train general [[Large Language Models and their applications | LLMs]] <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. The method is unsupervised, allowing for the creation of vast training data from existing protein databases <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>.

### Model Scale and Data

Meta trained ESM2 models up to 15 billion parameters, making them the largest [[Large Language Models and their applications | language models]] of proteins to date <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. They developed various model sizes, ranging from 8 million to 15 billion parameters <a class="yt-timestamp" data-t="00:45:38">[00:45:38]</a>, <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>.

The models were trained on amino acid sequences <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a> from large datasets, including:
*   UniRef50 and UniRef90, totaling 650 million unique sequences <a class="yt-timestamp" data-t="00:32:25">[00:32:25]</a>, <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>, <a class="yt-timestamp" data-t="00:32:35">[00:32:35]</a>.
*   MGnify90, which comprises over 617 million structures <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. MGnify is a microbiome analysis resource from the European Bioinformatics Institute, often funded through government and research initiatives <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>, <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
*   UniProt, a comprehensive resource for protein sequence and annotation data, also funded by government and non-profit organizations <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>, <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>, <a class="yt-timestamp" data-t="01:24:40">[01:24:40]</a>.

### Performance Measurement

Perplexity is used to quantify how well the model understands protein sequences <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. A low perplexity indicates a high predictive capability <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>. For example, the 8 million parameter model has a perplexity of 10, while the 15 billion parameter model achieves 6.37 <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>, <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>, <a class="yt-timestamp" data-t="00:47:19">[00:47:19]</a>.

The larger models generally exhibit better performance across various metrics <a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>. There are non-linear improvements, often referred to as "emergence points" or "reflection points," where accuracy suddenly jumps <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a>, <a class="yt-timestamp" data-t="00:36:48">[00:36:48]</a>. This phenomenon, also observed in reinforcement learning, suggests that once a model grasps a concept, it rapidly improves <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>.

## ESMFold: Protein Folding

ESMFold is presented as Meta's answer to AlphaFold <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. ESMFold uses the pre-trained ESM2 model as a feature encoder, with a dedicated "folding head" to predict 3D structures <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>, <a class="yt-timestamp" data-t="00:51:12">[00:51:12]</a>, <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>.

### Architecture

The ESM2 encoder processes the protein sequence, and its internal states (embeddings) are passed to the folding head <a class="yt-timestamp" data-t="00:51:20">[00:51:20]</a>. The folding head consists of a series of "folding blocks" that iteratively update a sequence representation and a pairwise representation <a class="yt-timestamp" data-t="00:51:30">[00:51:30]</a>, <a class="yt-timestamp" data-t="00:57:20">[00:57:20]</a>. The output of these blocks is then passed to an equivalent Transformer structure module that outputs 3D coordinates and confidence scores <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a>, <a class="yt-timestamp" data-t="00:59:03">[00:59:03]</a>. This iterative process is referred to as "recycling" <a class="yt-timestamp" data-t="00:51:47">[00:51:47]</a>, <a class="yt-timestamp" data-t="00:57:06">[00:57:06]</a>.

### Key Innovations and Efficiency

ESMFold eliminates the need for multiple sequence alignment (MSA), a computationally intensive process often required by other models like AlphaFold <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>, <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>. AlphaFold deeply integrates MSA into its neural network architecture <a class="yt-timestamp" data-t="00:52:31">[00:52:31]</a>. By processing the entire sequence through an encoder and feeding its representation into a folding head, ESMFold simplifies the neural network used for inference <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.

This design leads to significant speed improvements:
*   AlphaFold can take over 10 minutes to predict a structure <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   ESMFold can make a prediction for a protein with 384 residues in 14.2 seconds on a single Nvidia V100 GPU <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.

### Prediction Results

ESMFold produces state-of-the-art 3D structure predictions directly from primary protein sequences <a class="yt-timestamp" data-t="00:50:15">[00:50:15]</a>.
*   **High Confidence Predictions:** The model generates 225 million high-confidence predictions, including millions whose structures are novel compared to experimentally determined structures <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>, <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>.
*   **Performance Metrics:** Predictions are evaluated using metrics like pLDDT (predicted lddt) and TM score. pLDDT is a calibrated estimate of prediction accuracy <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>. RMSD (root mean squared deviation at 95% residue coverage) measures the distance between predicted and true atomic structures <a class="yt-timestamp" data-t="01:10:35">[01:10:35]</a>.
*   **Comparison to AlphaFold:** ESMFold demonstrates comparable, and in some cases, superior performance to AlphaFold, especially for single-sequence predictions <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>, <a class="yt-timestamp" data-t="01:00:50">[01:00:50]</a>. This is particularly important for *de novo* protein design (creating new proteins from scratch) where single-sequence inputs are critical <a class="yt-timestamp" data-t="01:05:47">[01:05:47]</a>.

### Novel Discoveries

The model has found regions of protein space "distant from existing knowledge" <a class="yt-timestamp" data-t="01:15:43">[01:15:43]</a>, essentially identifying novel protein structures that are not in existing databases like UniRef90 <a class="yt-timestamp" data-t="01:15:09">[01:15:09]</a>. This opens possibilities for understanding the structure of all proteins discovered in gene sequencing experiments <a class="yt-timestamp" data-t="01:25:14">[01:25:14]</a>.

## Technical Details

### Positional Embeddings

Transformers require positional embeddings to incorporate sequence order information <a class="yt-timestamp" data-t="01:41:10">[01:41:10]</a>. ESM2 uses rotary position encoding (RoPE), which is a learned embedding <a class="yt-timestamp" data-t="01:41:34">[01:41:34]</a>. RoPE is flexible, adaptable to any sequence length, and naturally incorporates relative position dependency, which is beneficial for protein structures that don't have a clear "beginning" or "end" like human sentences do <a class="yt-timestamp" data-t="01:56:43">[01:56:43]</a>, <a class="yt-timestamp" data-t="01:42:52">[01:42:52]</a>.

### Training Infrastructure

Training these large models requires significant computational resources. Meta utilized a heterogeneous cluster of 2,000 GPUs, completing characterization in two weeks <a class="yt-timestamp" data-t="01:18:17">[01:18:17]</a>, <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>. They used large batch sizes (up to 2 million total tokens) and techniques like data parallelism to distribute the model across multiple GPUs <a class="yt-timestamp" data-t="01:44:45">[01:44:45]</a>. A key challenge in scaling is the communication bottleneck between GPUs <a class="yt-timestamp" data-t="01:45:18">[01:45:18]</a>.

### Unsupervised Learning and Data Handling

The unsupervised nature of masked language modeling allows for the use of massive protein sequence databases <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>. During training, sequences are sampled with even weighting across UniRef clusters to prevent overfitting to highly similar protein groups <a class="yt-timestamp" data-t="01:28:46">[01:28:46]</a>.

## Implications and Future Outlook

The development of ESMFold highlights the emergent capabilities of [[Large Language Models and their applications | LLMs]] when applied to protein sequences <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. While humans are adept at evaluating [[Large Language Models and their applications | LLM]] performance on text, understanding emergent intelligence in protein sequences is more challenging given our limited intuitive grasp of 3D protein structures <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>, <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>. This raises the question of whether [[Large Language Models and their applications | LLMs]] can discover patterns in protein folding that are currently unknown to human scientists <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

The ability to accurately predict protein structures has profound implications for medicine and molecular engineering, enabling the discovery of new medicines and the creation of novel molecules <a class="yt-timestamp" data-t="02:00:24">[02:00:24]</a>, <a class="yt-timestamp" data-t="02:00:32">[02:00:32]</a>. The fact that many of these research efforts and their underlying datasets are publicly funded reinforces the importance of open-source models and data <a class="yt-timestamp" data-t="01:24:22">[01:24:22]</a>.

However, challenges remain. There's a question of whether current models are reaching a limit based on the size of existing protein databases <a class="yt-timestamp" data-t="01:59:37">[01:59:37]</a>. Future improvements might depend on synthetically creating larger datasets or discovering new, more complex biological structures <a class="yt-timestamp" data-t="02:00:05">[02:00:05]</a>. Furthermore, when both Meta's models and AlphaFold show similar areas of lower accuracy, it might suggest common challenges in understanding certain "stringy" or less defined regions of proteins, or even imply that some "ground truth" experimental data could be incomplete or inaccurate <a class="yt-timestamp" data-t="01:07:44">[01:07:44]</a>, <a class="yt-timestamp" data-t="01:21:44">[01:21:44]</a>, <a class="yt-timestamp" data-t="01:22:40">[01:22:40]</a>.