---
title: Comparison between ESM Fold and AlphaFold
videoId: I_ll4L9TpU4
---

From: [[hu-po]] <br/> 

ESM Fold, developed by Facebook (Meta) Research <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>, is Meta's entry into the field of protein structure prediction, aiming to rival DeepMind's AlphaFold <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. Its primary goal is the evolutionary scale prediction of atomic protein structure using a [[protein_structure_prediction_using_large_language_models | language model]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## ESM Fold Overview

The models developed for ESM Fold are the largest language models of proteins to date, with the largest version trained using up to 15 billion parameters <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>, <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>. The project aims to extend protein structure prediction to 200 million catalog proteins <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. It has already generated 225 million high-confidence predictions, with millions of these structures being novel compared to experimentally determined ones <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. ESM Fold is the result of a large collaboration involving New York University, Stanford University, and MIT <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

## Key Differences and Advantages

ESM Fold distinguishes itself from other models like AlphaFold through its architecture and training methodology:

### Architecture and Training Objective

ESM Fold utilizes [[protein_structure_prediction_using_large_language_models | large language models]] to directly infer structure from the primary protein sequence <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. This contrasts with what is described as DeepMind's more "one-to-one supervised learning task" where they predict 3D structure from protein components <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.

A core aspect of ESM Fold's training is the masked language modeling objective <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>. This involves masking out parts of a protein sequence and training the model to predict the missing amino acids <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>, similar to how general LLMs are trained for next token prediction <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. This approach is simple and unsupervised <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>, allowing for the "infinite" creation of training data from existing protein databases <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>. ESM Fold's base model, ESM2, uses a Bert-style encoder <a class="yt-timestamp" data-t="01:41:07">[01:41:07]</a> and a rotary position encoding <a class="yt-timestamp" data-t="01:41:34">[01:41:34]</a> for its Transformer architecture <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>.

### Inference Speed

One significant advantage of ESM Fold is its speed. It eliminates the need for multiple sequence alignment (MSA) <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>, a process that is deeply integrated into current state-of-the-art prediction models like AlphaFold <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>, <a class="yt-timestamp" data-t="00:54:12">[00:54:12]</a>. This simplification of the neural network used for inference <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a> allows ESM Fold to make a prediction on a protein with 384 residues in just 14.2 seconds on a single Nvidia V100 GPU <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>. In contrast, AlphaFold can take over 10 minutes for a single prediction <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

### Emergent Capabilities

The project also explores the concept of "emergent capabilities" in language models trained on protein sequences <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. Just as LLMs exhibit emergent intelligence on text, ESM Fold aims to uncover whether similar phenomena occur in the context of biological sequences. This raises questions about whether the models can understand patterns in proteins that humans do not <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.

### Performance and Data

ESM Fold generates state-of-the-art 3D structure predictions directly from primary protein sequences <a class="yt-timestamp" data-t="00:50:15">[00:50:15]</a>. The model's understanding of protein sequences is quantified using perplexity, with lower values indicating better performance <a class="yt-timestamp" data-t="00:32:12">[00:32:12]</a>. The 15 billion parameter model achieves a perplexity of 6.37, compared to 10 for the 8 million parameter model <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>.

Interestingly, ESM Fold was trained using a dataset of 325,000 experimentally determined structures and augmented with 12 million structures generated by AlphaFold 2 <a class="yt-timestamp" data-t="01:03:35">[01:03:35]</a>, <a class="yt-timestamp" data-t="01:04:11">[01:04:11]</a>. This blending of datasets raises questions about potential error introduction <a class="yt-timestamp" data-t="01:04:21">[01:04:21]</a>.

In terms of accuracy, ESM Fold performs particularly well on single sequences, which is crucial for *de novo* protein design (creating new proteins from scratch) <a class="yt-timestamp" data-t="01:05:45">[01:05:45]</a>. It's noted that AlphaFold and RosettaFold generally do not perform as well with single sequences <a class="yt-timestamp" data-t="01:05:19">[01:05:19]</a>. The perplexity of ESM Fold is directly linked to its prediction accuracy, indicating that improving the language model is key to improving single sequence structure prediction <a class="yt-timestamp" data-t="01:06:39">[01:06:39]</a>.

## Comparison of Capabilities

While ESM Fold offers significant speed advantages by bypassing MSA, the transcript suggests that for parts of protein structures with low prediction accuracy, there isn't a significant difference between ESM Fold and AlphaFold <a class="yt-timestamp" data-t="01:07:44">[01:07:44]</a>. This might imply that both models are learning similar underlying patterns or hitting the same limits in understanding these complex biological structures <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>. A key metric used for comparison is the root mean squared deviation (RMSD) at 95% residue coverage, which measures the distance between the predicted atomic structures and the true 3D structures <a class="yt-timestamp" data-t="01:10:35">[01:10:35]</a>.

One interesting aspect of the prediction process is the model's confidence scores. ESM Fold provides a confidence score with its predictions <a class="yt-timestamp" data-t="01:14:57">[01:14:57]</a>. A significant portion of its high-confidence predictions are novel structures not found in existing databases like UniRef90 <a class="yt-timestamp" data-t="01:15:06">[01:15:06]</a>. ESM Fold can effectively characterize regions of the protein landscape that are distant from existing knowledge <a class="yt-timestamp" data-t="01:15:43">[01:15:43]</a>.

All predicted structures from ESM Fold are publicly available through an Atlas for bulk download via a programmatic API <a class="yt-timestamp" data-t="01:23:15">[01:23:15]</a>, <a class="yt-timestamp" data-t="01:23:22">[01:23:22]</a>. This openness aligns with the fact that much of the underlying data for protein research is funded by government and non-profit organizations <a class="yt-timestamp" data-t="01:24:31">[01:24:31]</a>.