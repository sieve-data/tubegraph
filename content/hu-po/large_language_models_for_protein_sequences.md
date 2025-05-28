---
title: Large language models for protein sequences
videoId: I_ll4L9TpU4
---

From: [[hu-po]] <br/> 

This article explores the application of [[large_language_models_in_machine_learning_research | large language models]] (LLMs) to predict atomic protein structures, focusing on a paper from Facebook AI Research that positions itself as a contender in the field of using deep learning for biological use cases <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. The research aims to extend [[protein_structure_prediction_using_language_models | protein structure prediction]] to a catalog of 200 million proteins <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Background and Approach
Meta's research serves as an answer to DeepMind's work in protein folding <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. The core idea is the direct inference of structure from primary protein sequences using a [[llm_large_language_models_development | large language model]] <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

A key challenge lies in adapting LLMs, which are typically trained on one-dimensional text sequences (like sentences), to the three-dimensional nature of amino acids and proteins <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a>. The method involves tokenizing proteins into a sequence of "letters" representing amino acids <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.

### Model Scale and Training
The models developed, named ESM2, include versions with up to 15 billion parameters, making them the largest [[large_language_models_llms_and_scaling | language models of proteins]] to date <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. ESM2 models are trained with a masked language modeling objective, an unsupervised approach where parts of the protein sequence are masked out, and the model is trained to predict the missing parts <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>, <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>. This allows for infinite creation of training data from existing protein databases <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.

The training process utilized a diverse dataset:
*   43 million UniRef50 training clusters <a class="yt-timestamp" data-t="00:32:25">[00:32:25]</a>
*   138 million UniRef90 sequences <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>
*   A total of 65 million unique sequences <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>

The training process also involves:
*   Even sampling across clusters to prevent overfitting to specific protein types <a class="yt-timestamp" data-t="01:28:48">[01:28:48]</a>.
*   Large effective batch sizes of up to 2 million tokens <a class="yt-timestamp" data-t="01:43:43">[01:43:43]</a>.
*   [[large_language_models_and_optimization | Adam optimization]] with weight decay and learning rate scheduling (warm-up followed by linear decay) <a class="yt-timestamp" data-t="01:43:48">[01:43:48]</a>.
*   Sharded data parallelism to distribute model weights and parameters across multiple GPUs <a class="yt-timestamp" data-t="01:44:48">[01:44:48]</a>.

## ESM-Fold Architecture and Performance
ESM-Fold is the system that uses the pre-trained ESM2 model as a feature encoder for structure prediction <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. The architecture involves a "folding head" or "folding trunk" that processes the sequence embeddings from ESM2 <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>. This folding head updates sequence and pairwise representations iteratively <a class="yt-timestamp" data-t="00:51:36">[00:51:36]</a>.

A key distinction from other models like AlphaFold is that ESM-Fold eliminates the need for multiple sequence alignment (MSA) during inference <a class="yt-timestamp" data-t="01:32:23">[01:32:23]</a>, <a class="yt-timestamp" data-t="01:32:27">[01:32:27]</a>. While state-of-the-art models deeply integrate MSA, ESM-Fold processes the entire sequence through the encoder and then feeds the representation into the folding head, simplifying the neural network used for inference <a class="yt-timestamp" data-t="01:04:04">[01:04:04]</a>, <a class="yt-timestamp" data-t="01:04:11">[01:04:11]</a>. This leads to significant speed improvements; for example, it can make a prediction for a protein with 384 residues in 14.2 seconds on a single Nvidia V100 GPU <a class="yt-timestamp" data-t="01:05:38">[01:05:38]</a>.

### Evaluation Metrics and Results
*   **Perplexity**: A measure of how well a probability model predicts a sample; a lower perplexity indicates better prediction <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>. The 15 billion parameter model achieved a perplexity of 6.37 <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>.
*   **TM Score / pLDDT / RMSD**: Metrics to quantify the accuracy of the predicted 3D structure compared to the ground truth <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>. pLDDT is a well-calibrated estimate of prediction accuracy <a class="yt-timestamp" data-t="01:01:08">[01:01:08]</a>. Root Mean Squared Deviation (RMSD) measures the distance between atomic structures <a class="yt-timestamp" data-t="01:11:06">[01:11:06]</a>.

ESM-Fold generates state-of-the-art three-dimensional structure predictions directly from the primary protein sequence <a class="yt-timestamp" data-t="00:50:15">[00:50:15]</a>. It performs comparably to or better than AlphaFold2 and RosettaFold on single-sequence predictions <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>, <a class="yt-timestamp" data-t="01:00:28">[01:00:28]</a>. The model's predictions often show high confidence, with many novel structures found that are not present in existing databases like UniRef90 <a class="yt-timestamp" data-t="01:15:07">[01:15:07]</a>.

## Emergent Capabilities and Novelty
As [[large_language_models_llms_and_scaling | models scale up]] in computation, data, and parameters, greater capabilities emerge <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. For protein sequences, this means that these models may understand patterns that humans do not <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>. The relationship between perplexity and structure prediction indicates that improving the underlying language model is key to enhancing single-sequence structure prediction accuracy <a class="yt-timestamp" data-t="01:06:39">[01:06:39]</a>.

The project produced 25 million high-confidence predictions, including millions of structures considered novel compared to experimentally determined structures <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. ESM-Fold effectively characterizes regions of the protein landscape distant from existing knowledge <a class="yt-timestamp" data-t="01:15:45">[01:15:45]</a>.

## Technical Considerations
*   **Positional Encoding**: ESM2 uses rotary positional encoding, which encodes absolute positional information with a rotation matrix and naturally incorporates explicit relative position dependency <a class="yt-timestamp" data-t="01:41:34">[01:41:34]</a>, <a class="yt-timestamp" data-t="01:56:32">[01:56:32]</a>. This differs from absolute sinusoidal positional encoding often used in general [[large_language_models_in_machine_learning_research | Transformer architectures]], and might be more suitable for proteins where sequential "beginning" and "end" may not have the same meaning as in human language <a class="yt-timestamp" data-t="01:42:22">[01:42:22]</a>.
*   **Inference Efficiency**: The model is designed for [[large_language_models_and_inference_efficiency | efficient inference]], simplifying the neural network and eliminating complex multi-step processes for prediction <a class="yt-timestamp" data-t="01:13:28">[01:13:28]</a>.

## Public Availability and Future Impact
All predicted structures are available through the ESM Metagenomic Atlas <a class="yt-timestamp" data-t="02:08:02">[02:08:02]</a>, including bulk download via a programmatic API <a class="yt-timestamp" data-t="01:23:22">[01:23:22]</a>. The availability of these models as open-source projects is partly due to the government and non-profit funding of the underlying genomic databases <a class="yt-timestamp" data-t="01:24:31">[01:24:31]</a>.

This research marks an era where it is possible to understand the structure of all proteins discovered in gene sequencing experiments <a class="yt-timestamp" data-t="01:25:16">[01:25:16]</a>. High-confidence predictions are expected to be reliable enough for insights similar to experimentally determined structures <a class="yt-timestamp" data-t="01:25:51">[01:25:51]</a>. While the models may be approaching the limits of current data set sizes, the ability to synthetically create data with these models could potentially lead to even larger models and further breakthroughs <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a>. The application of deep learning to biological problems like [[protein_structure_prediction_using_language_models | protein structure prediction]] holds immense promise for discovering new medicines and molecules <a class="yt-timestamp" data-t="02:00:24">[02:00:24]</a>.