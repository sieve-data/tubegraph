---
title: Deep learning in biological research
videoId: I_ll4L9TpU4
---

From: [[hu-po]] <br/> 

This article explores the application of deep learning, particularly [[large_language_models_in_machine_learning_research | large language models]], to biological research, focusing on protein structure prediction. The primary subject is a paper from Facebook (Meta) Research, which presents an approach competing with [[google_deepmind_mirasol_paper | DeepMind's]] protein folding efforts <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Evolutionary Scale Modeling (ESM)

The paper, titled "Evolutionary Scale Prediction of Atomic Protein Structure with a Language Model," aims to use [[Deep Learning Approaches in Image Correspondence | deep learning]] for biological use cases, specifically predicting atomic protein structures <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>, <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Key contributors include Tom Sercu and Joe Shim <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

The research seeks to extend protein structure prediction to a catalog of 200 million proteins <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>, inferring structure directly from the primary sequence using a [[large_language_models_in_machine_learning_research | large language model]] <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. The trained models are up to 15 billion parameters, making them the largest [[large_language_models_in_machine_learning_research | language models]] for proteins to date <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. This collaborative effort involves institutions such as New York University, Stanford University, and MIT <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>.

### ESM2 Model and Training
ESM2 is a new family of Transformer protein [[large_language_models_in_machine_learning_research | language models]] developed by Meta, building upon the previous generation ESM1 <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>. Improvements in ESM2 come from architecture, training parameters, and computational resources <a class="yt-timestamp" data-t="00:31:05">[00:31:05]</a>.

The model is trained using a masked language modeling objective, an unsupervised approach <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>. This involves masking out parts of a protein sequence and training the model to predict the missing amino acids <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>. This method allows for infinite creation of training data from existing protein databases <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.

The training data set, sourced from UniRef50 (September 2021), comprises 65 million unique sequences <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>, <a class="yt-timestamp" data-t="01:27:19">[01:27:19]</a>. During training, sequences are sampled with even weighting across 43 million UniRef50 training clusters, ensuring balanced learning across diverse protein types and preventing overfitting to specific clusters <a class="yt-timestamp" data-t="01:28:46">[01:28:46]</a>. The smallest ESM2 model has 8 million parameters, while the largest has 15 billion <a class="yt-timestamp" data-t="00:30:57">[00:30:57]</a>.

### Performance Metrics
Perplexity is used to quantify the model's understanding of protein sequences <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>. A low perplexity indicates a high ability to predict the sample <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>. For protein sequences, perplexity describes the number of amino acids the model chooses between for each prediction <a class="yt-timestamp" data-t="00:33:06">[00:33:06]</a>.
*   The 8 million parameter model achieved a perplexity of 10 <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>.
*   The 15 billion parameter model reached a perplexity of 6.37 <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>.
The speaker observes that the perplexity drop is quite fast, with the 150 million parameter model and the 15 billion parameter model showing closer performance, suggesting the data set size might be a limiting factor <a class="yt-timestamp" data-t="00:47:29">[00:47:29]</a>.

Transformer models trained with masked language modeling develop attention patterns that correspond to the residue-residue contact map of proteins <a class="yt-timestamp" data-t="00:34:59">[00:34:59]</a>. ESM2 exhibits non-linear improvements in accuracy, akin to "emergence points" seen in other [[large_language_models_in_machine_learning_research | LLMs]] or reinforcement learning, where performance jumps significantly after a period of stability <a class="yt-timestamp" data-t="00:36:41">[00:36:41]</a>.

## ESM-Fold for 3D Structure Prediction

ESM-Fold is Meta's answer to [[google_deepmind_mirasol_paper | AlphaFold]] for predicting 3D protein structures <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. ESM-Fold uses ESM2 as a feature encoder, with a separate "folding head" that takes the encoded representations (embeddings) to predict protein folds <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>, <a class="yt-timestamp" data-t="00:56:05">[00:56:05]</a>. The folding head incorporates a series of "folding blocks" that update sequence and pairwise representations iteratively <a class="yt-timestamp" data-t="00:51:30">[00:51:30]</a>, <a class="yt-timestamp" data-t="00:57:06">[00:57:06]</a>.

### Key Innovations and Comparisons to AlphaFold
ESM-Fold offers significant speed advantages by eliminating the need for multiple sequence alignment (MSA) <a class="yt-timestamp" data-t="01:32:20">[01:32:20]</a>, which is deeply integrated into other state-of-the-art models like [[google_deepmind_mirasol_paper | AlphaFold]] <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>. While [[google_deepmind_mirasol_paper | AlphaFold]]'s performance degrades when MSAs are ablated <a class="yt-timestamp" data-t="00:59:12">[00:59:12]</a>, ESM-Fold can predict structure directly from a single primary sequence <a class="yt-timestamp" data-t="00:50:15">[00:50:15]</a>.

> "Current state-of-the-art prediction models deeply integrate the multiple sequence alignment into the neural network architecture... ESM-Fold eliminates the need for a multiple sequence alignment" <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>, <a class="yt-timestamp" data-t="01:32:20">[01:32:20]</a>

This simplification of the neural network used for inference makes ESM-Fold considerably faster <a class="yt-timestamp" data-t="01:40:58">[01:40:58]</a>. While [[google_deepmind_mirasol_paper | AlphaFold]] can take over 10 minutes to predict a protein structure <a class="yt-timestamp" data-t="01:40:58">[01:40:58]</a>, ESM-Fold can make a prediction on a protein with 384 residues in 14.2 seconds on a single Nvidia V100 GPU <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.

ESM-Fold shows comparable or better performance than [[google_deepmind_mirasol_paper | AlphaFold]] and RosettaFold, especially for single sequences <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>. Single sequence performance is critical for *de novo* protein design (creating new proteins from scratch) <a class="yt-timestamp" data-t="01:05:47">[01:05:47]</a>.

### Novel Discoveries
ESM-Fold made 225 million high-confidence predictions, characterizing regions of metagenomic space distant from existing knowledge <a class="yt-timestamp" data-t="01:30:08">[01:30:08]</a>. The model successfully found many novel protein structures that are not present in the UniRef90 database <a class="yt-timestamp" data-t="01:15:06">[01:15:06]</a>.

> "ESM-Fold effectively characterizes regions of the protein landscape that are distant from existing knowledge." <a class="yt-timestamp" data-t="01:15:43">[01:15:43]</a>

This capability allows the model to identify patterns and structures previously unknown to humans, potentially understanding protein behaviors beyond current scientific comprehension <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>, <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a>.

## Metagenomics and Data Sources
The exponential growth in protein sequence databases is largely due to metagenomics, which involves sequencing DNA from diverse, often unknown, environmental samples <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a>, <a class="yt-timestamp" data-t="01:50:01">[01:50:01]</a>.
*   The human genome contains about 20,000 proteins <a class="yt-timestamp" data-t="01:06:09">[01:06:09]</a>.
*   UniProt, a comprehensive resource for protein sequence and annotation data, contains around 200 million proteins <a class="yt-timestamp" data-t="01:06:13">[01:06:13]</a>, <a class="yt-timestamp" data-t="01:19:27">[01:19:27]</a>.
*   The MgNify90 dataset contains over 617 million structures <a class="yt-timestamp" data-t="01:19:16">[01:19:16]</a>. This open database is funded by European governments and initiatives like cancer and Alzheimer's research <a class="yt-timestamp" data-t="01:17:51">[01:17:51]</a>.

The predictions from ESM-Fold are made available through the ESM Metagenomic Atlas Explorer <a class="yt-timestamp" data-t="01:27:19">[01:27:19]</a>, <a class="yt-timestamp" data-t="02:13:15">[02:13:15]</a>.

## Challenges and Future Directions
A significant challenge noted by the speaker is the potential for "mislabeled training data" in the ground truth protein structures <a class="yt-timestamp" data-t="01:11:26">[01:11:26]</a>. Since humans have a less intuitive understanding of protein sequences compared to natural language, it is difficult to verify if the AI's divergent predictions are errors or a deeper, more accurate understanding of protein structures that humans might not yet grasp <a class="yt-timestamp" data-t="01:12:03">[01:12:03]</a>.

There is a suggestion that the models might be hitting the limit of available data, potentially requiring "100x the data set size or 100x the model size" for "step function improvements" <a class="yt-timestamp" data-t="01:59:37">[01:59:37]</a>. However, the possibility remains that these models could synthetically create new datasets to train even larger models <a class="yt-timestamp" data-t="02:00:05">[02:00:05]</a>.

Despite these challenges, the application of [[Deep Learning Approaches in Image Correspondence | deep learning]] to biological problems like protein structure prediction holds immense promise for discovering new medicines and molecules in the future <a class="yt-timestamp" data-t="02:00:24">[02:00:24]</a>.

<hr>
_This article was created using information from the video at <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>._