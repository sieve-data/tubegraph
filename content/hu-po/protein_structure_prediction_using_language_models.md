---
title: Protein structure prediction using language models
videoId: I_ll4L9TpU4
---

From: [[hu-po]] <br/> 

Meta (formerly Facebook) Research has developed an approach to protein structure prediction using [[large_language_models_for_protein_sequences | language models]], positioning itself as a contender in the race to use deep learning for biological applications <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. This effort aims to extend protein structure prediction to a catalog of 200 million proteins <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

## Evolutionary Scale Language Models (ESM2)

The core of Meta's approach is a new family of [[large_language_models_for_protein_sequences | Transformer protein language models]] called ESM2 <a class="yt-timestamp" data-t="00:30:51">[00:30:51]</a>. These are the largest [[LLM Large Language Models development | language models]] of proteins to date, with versions trained up to 15 billion parameters <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Smaller models with 8 million parameters are also available <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

### Training and Architecture
ESM2 models are trained with a masked language modeling objective, an unsupervised method <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>. This involves masking out parts of a protein sequence and training the model to predict the missing amino acids <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>. This training method allows for infinite creation of training data from existing protein databases <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>. The models utilize Transformer architectures, which have become prevalent in [[LLM Large Language Models development | language models]] <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.

The training dataset includes 650 million unique sequences, sampled evenly across 43 million UniRef50 training clusters and 138 million UniRef90 sequences <a class="yt-timestamp" data-t="00:32:35">[00:32:35]</a>.
The training employed a heterogeneous cluster of 2,000 GPUs and took two weeks to characterize <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>. Training efficiency is improved by sharding model weights and optimization parameters across multiple GPUs <a class="yt-timestamp" data-t="01:44:45">[01:44:45]</a>.

### Positional Embeddings
ESM2 uses rotary position encoding, which differs from the absolute sinusoidal positional encoding used in the original Transformer paper <a class="yt-timestamp" data-t="01:41:34">[01:41:34]</a>. Rotary position embedding (RoPE) encodes absolute positional information with a rotation matrix and naturally incorporates explicit relative position dependency <a class="yt-timestamp" data-t="01:56:30">[01:56:30]</a>. This method is flexible for varying sequence lengths and introduces decaying inter-token dependency with increasing relative distances <a class="yt-timestamp" data-t="01:56:45">[01:56:45]</a>. This approach makes sense for proteins, where the linear sequence doesn't directly map to 3D spatial relationships in the same way human language has a temporal progression <a class="yt-timestamp" data-t="01:42:45">[01:42:45]</a>.

## Protein Structure Prediction (ESMfold)

ESMfold is the structure prediction model that leverages the pre-trained ESM2 [[large_language_models_for_protein_sequences | language model]] <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. ESM2 acts as a feature encoder, processing the protein sequence and passing its internal states (embeddings) to a "folding head" <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>. This folding head contains "folding blocks" that iteratively update sequence and pairwise representations before passing them to a structure module that outputs 3D coordinates and confidences <a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>.

### Key Innovations Compared to AlphaFold
ESMfold eliminates the need for multiple sequence alignment (MSA) <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>, a computationally intensive process often required by other state-of-the-art models like AlphaFold <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>. By processing structures directly from the primary sequence, ESMfold simplifies the neural network used for inference <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. This change significantly speeds up prediction times; for a protein with 384 residues, ESMfold can make a prediction in 14.2 seconds on a single Nvidia V100 GPU <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>, whereas AlphaFold can take over 10 minutes <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.

## Performance and Results

### Perplexity and Contact Prediction
Perplexity is a measure of how well a probability model predicts a sample; a lower perplexity indicates a better model <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>. ESM2 models show large improvements in modeling protein structures as parameters increase <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>. The 8 million parameter model has a perplexity of 10, while the 15 billion parameter model achieves 6.37 <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>. Perplexity and contact map prediction accuracy are linked, with proteins undergoing large changes in one also showing large changes in the other <a class="yt-timestamp" data-t="00:38:05">[00:38:05]</a>.

[[Advancements in language models | Larger models]] exhibit "emergent capabilities," where greater capabilities emerge as computation, data, and the number of parameters increase <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. This raises the possibility that a similar form of emergence might be exhibited by [[large_language_models_for_protein_sequences | language models]] trained on protein sequences <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### 3D Structure Prediction
ESMfold generates state-of-the-art three-dimensional structure predictions directly from the primary protein sequence <a class="yt-timestamp" data-t="00:50:15">[00:50:15]</a>. The models were validated against holdout sets like CAMEO and CASP14 proteins, where the actual atomic structure is known <a class="yt-timestamp" data-t="00:39:03">[00:39:03]</a>. Accuracy is measured using metrics like pLDDT (predicted local distance difference test), a well-calibrated estimate of prediction accuracy <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>, and RMSD95 (root mean squared deviation at 95% residue coverage) <a class="yt-timestamp" data-t="01:10:35">[01:10:35]</a>.

One notable finding is that regions of a protein structure that are difficult for ESMfold to predict accurately also pose challenges for AlphaFold, suggesting both models are learning similar underlying patterns <a class="yt-timestamp" data-t="01:07:44">[01:07:44]</a>.

### Novel Structures and Metagenomic Atlas
ESMfold has made 25 million high-confidence predictions, including millions whose structures are novel compared to experimentally determined structures <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. In a comprehensive characterization of the MGnify90 dataset (over 617 million proteins) <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>, 225 million high-confidence predictions were made <a class="yt-timestamp" data-t="00:18:30">[00:18:30]</a>. A vast majority of these high-confidence predictions were distinct from existing UniRef90 entries, indicating discovery in metagenomic space distant from existing knowledge <a class="yt-timestamp" data-t="01:15:06">[01:15:06]</a>. All predicted structures are accessible via the ESM Metagenomic Atlas <a class="yt-timestamp" data-t="02:27:19">[02:27:19]</a>.

## Data Sources and Challenges
The protein sequence databases like UniProt and MGnify are largely funded by government research and non-profits, including the National Human Genome Research Institute and NIH <a class="yt-timestamp" data-t="01:24:31">[01:24:31]</a>. This public funding influences the open-source availability of some [[large_language_models_in_machine_learning_research | large-scale models]] <a class="yt-timestamp" data-t="01:24:22">[01:24:22]</a>.

A potential challenge identified is the quality of existing ground truth data. When models like ESMfold and AlphaFold predict a structure different from the "ground truth," it raises the question of whether the experimental ground truth might sometimes be inaccurate or represent only one possible conformation <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a>. Humans have less intuitive understanding of protein sequences compared to human language, making it difficult to "fact-check" AI predictions or fully understand emergent intelligence in this domain <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

The task of protein structure prediction is at a point where the size of existing protein databases might become a limiting factor for further "step-function improvements" in model performance <a class="yt-timestamp" data-t="01:59:37">[01:59:37]</a>. However, there's potential for models to synthetically create new datasets to train even larger models <a class="yt-timestamp" data-t="02:00:05">[02:00:05]</a>.

## Conclusion
The development of ESMfold represents significant [[advancements_in_language_models | advancements in language models]] for biological applications, specifically in protein structure prediction. By training [[large_language_models_for_protein_sequences | language models]] on amino acid sequences and developing efficient folding architectures, Meta has demonstrated competitive performance and the ability to discover novel protein structures, contributing to a future where the structure of all proteins discovered through gene sequencing experiments might be understood <a class="yt-timestamp" data-t="01:25:14">[01:25:14]</a>.