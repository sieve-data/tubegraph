---
title: Innovations in computational biology by Meta formerly Facebook
videoId: I_ll4L9TpU4
---

From: [[hu-po]] <br/> 

[[meta_ai_research | Meta AI research]] has entered the field of [[challenges_and_advancements_in_protein_folding_and_prediction | protein folding and prediction]], positioning itself as a contender against DeepMind's AlphaFold [00:01:11]. This effort focuses on using deep learning for biological use cases [00:01:27].

## Evolutionary Scale Modeling (ESM)

Meta's approach involves "evolutionary scale prediction of atomic protein structure with a language model" [00:00:49]. This is based on a paper from [[meta_ai_research | Facebook research]] [00:01:05].

### ESM2 Language Models
ESM2 is a new family of Transformer protein language models [00:30:49]. Improvements in ESM2 over its previous generation (ESM1) include advancements in architecture, training parameters, and computational resources [00:31:05].

*   **Model Sizes**: ESM2 models range in size, with the smallest being 8 million parameters and the largest being 15 billion parameters, making them the largest language models of proteins to date [00:03:46], [00:11:40].
*   **Training Objective**: The models are trained using a masked language modeling objective [00:31:18]. This involves masking out parts of a protein sequence and training the model to predict the missing amino acids [00:31:29]. This method is simple and unsupervised, allowing for the creation of infinite training data from existing protein databases [00:31:38].
*   **Data Sets**: The models are trained on large protein sequence databases.
    *   The total training data set size for ESM2 included 65 million unique sequences [00:32:35].
    *   Specifically, sequences were sampled from 43 million UniRef50 training clusters and 138 million UniRef90 sequences [00:32:23].
    *   Training data used from UniRef50 was from September 2021 [01:27:19].
    *   Validation data sets were approximately 0.5% of the training data [01:27:32].
    *   The models also leveraged [[role_of_largescale_genomic_databases_in_training_ai_models | large-scale gene sequencing experiments]] and metagenomic proteins, which contributed to an exponential growth in the size of protein sequence databases [00:13:10], [00:15:43]. The MGnify database (a microbiome analysis resource funded by European governments and cancer/Alzheimer's research) was also utilized [01:03:22], [01:19:16], [01:48:48].
*   **Computational Resources**: Training the models involved significant computational power, utilizing a heterogeneous cluster of 2,000 GPUs over two weeks for characterization [01:18:17].
*   **Performance Metrics**:
    *   **Perplexity**: A measurement of how well a probability distribution or model predicts a sample [00:33:43]. Lower perplexity indicates better understanding [00:33:50]. The 8 million parameter model had a perplexity of 10, while the 15 billion parameter model achieved 6.37 [00:33:27]. This reflects significant improvements in modeling protein structures [00:32:50].
    *   **Precision at L**: Used to quantify prediction accuracy, where a contact is a positive prediction if it's within the top L most likely contacts for a sequence of length L [00:41:24].
    *   **TM score / pLDDT / RMSD**: Metrics used to compare predicted 3D structures to ground truth. pLDDT is a well-calibrated estimate of prediction accuracy [01:01:05]. RMSD (root mean squared deviation) measures the distance between atomic structures [01:10:35].

## ESMFold: Protein Structure Prediction

ESMFold is Meta's dedicated protein folding model, serving as their "answer to AlphaFold" [00:50:50]. It generates state-of-the-art three-dimensional structure predictions directly from the primary protein sequence [00:50:15].

### Architecture
ESMFold's architecture uses ESM2 as a feature encoder [00:51:06]. The sequence is processed through ESM2's feed-forward layers, and the model's internal states (embeddings/representations) are passed to a "folding head" [00:51:20].

*   **Folding Head**: This component consists of a series of "folding blocks" that alternate between updating a sequence representation and a pairwise representation [00:51:30]. The output then goes to an equivariant Transformer structure module which predicts 3D coordinates and confidences [00:58:55].
*   **Elimination of MSA**: A key innovation is that ESMFold eliminates the need for multiple sequence alignment (MSA) [01:31:20], [01:32:20]. Traditional state-of-the-art models like AlphaFold deeply integrate MSA into their neural network architecture [00:52:29]. ESMFold's approach is faster, making a prediction on a protein with 384 residues in 14.2 seconds on a single Nvidia V100 GPU [00:53:38], whereas AlphaFold can take over 10 minutes [01:42:26].
*   **Single Sequence Prediction**: ESMFold excels at single sequence prediction, which is crucial for *de novo* protein design (creating new proteins from scratch) [01:05:45]. AlphaFold and RosettaFold reportedly do not perform as well with single sequences [01:05:19].

### Emergent Capabilities in Protein Language Models
Just as large language models (LLMs) exhibit [[collective_intelligence_in_biology_and_ai | emergent intelligence]] on text, there's a possibility of parallel forms of emergence in language models trained on protein sequences [00:09:02]. As computation, data, and the number of parameters increase, greater capabilities emerge [00:08:43].

*   **Human Understanding vs. AI**: Humans are proficient at understanding text, making it easy to evaluate LLM performance [00:09:21]. However, humans are less adept at understanding protein sequences [00:09:41]. This raises questions: "What does that even mean? Do they understand patterns that we don't understand, and how do we even how do we know that they've understood something that we ourselves do not know?" [00:09:56].
*   **Novel Discoveries**: [[meta_ai_research | Meta AI research]]'s models have made high-confidence predictions for over 225 million structures [00:04:41], including millions whose structures are novel compared to experimentally determined structures [00:04:46]. This suggests the model characterizes regions of the protein landscape "distant from existing knowledge" [01:15:45]. For example, the model can find similar structures for "lone wolf" proteins that previously had no close matches in existing databases [01:16:17].

## Challenges and Future Directions
Despite the advancements, [[challenges_and_advancements_in_ai_research | challenges]] remain.

*   **3D vs. 1D Data**: A fundamental challenge is that biological entities like amino acids and proteins are three-dimensional, while large language models are traditionally trained on one-dimensional sequences [00:07:40].
*   **Ground Truth Accuracy**: There's a question about the accuracy of existing experimentally determined protein structures (ground truth data) [01:11:21]. If both AlphaFold and ESMFold models predict a structure different from the ground truth, it's possible the ground truth itself could be incorrect, highlighting the difficulty in "fact-checking" advanced AI biological predictions [01:12:11].
*   **Common Error Modes**: Parts of protein structures that have low prediction accuracy do not differ significantly between ESMFold and AlphaFold [01:07:44]. This suggests that both models might be learning the same "low-hanging fruit" or a basic understanding of proteins, implying further breakthroughs require overcoming common limitations [01:08:03]. These consistently challenging areas often correspond to "stringy parts" of proteins, which might be flexible or have variable conformations in nature [01:22:20]. These "active sites" are crucial for protein function [01:26:04].
*   **Scaling Data Sets**: The current models may be hitting the limit of available protein databases [01:59:37]. Future improvements might require 100x increases in dataset size or model size, or synthetically creating data sets with these models themselves to train even larger models [02:00:00].

## Public Availability
All predicted structures from ESMFold are available on the ESM Metagenomic Atlas [02:27:19], which can be explored and accessed for bulk download via a programmatic API [02:27:25], [01:23:17]. This open-source approach aligns with the funding sources of many protein databases (e.g., government and non-profit research) [01:24:31].