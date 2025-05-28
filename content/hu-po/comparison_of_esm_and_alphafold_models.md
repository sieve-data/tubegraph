---
title: Comparison of ESM and AlphaFold models
videoId: I_ll4L9TpU4
---

From: [[hu-po]] <br/> 

Both ESM (Evolutionary Scale Modeling) and AlphaFold are prominent models in the field of [[protein_structure_prediction_using_language_models | protein structure prediction]], utilizing deep learning techniques. While AlphaFold, developed by DeepMind, gained significant attention, Meta's ESM model presents its own unique approach and advantages <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## ESM: Meta's Approach to Protein Modeling

ESM is a paper originating from Facebook (Meta) Research, positioning itself as a contender in the race of using deep learning for biological use cases <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The project involves a significant collaboration with New York University, Stanford University, and MIT <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.

ESM models, specifically ESM-2, are [[large_language_models_for_protein_sequences | large language models]] trained on amino acid sequences <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. The largest ESM-2 model has 15 billion parameters, making it one of the largest [[large_language_models_for_protein_sequences | language models]] of proteins to date <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The training objective for ESM-2 is a masked language modeling objective, similar to how traditional [[large_language_models_for_protein_sequences | large language models]] are trained <a class="yt-timestamp" data-t="00:31:18">[00:31:18]</a>. This means the model learns by trying to fill in missing amino acids in protein sequences <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. This unsupervised approach allows for the creation of infinite training data from existing protein databases <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>.

ESM has successfully predicted the structure of 25 million high-confidence proteins, including millions whose structures are novel compared to experimentally determined structures <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>, <a class="yt-timestamp" data-t="01:15:06">[01:15:06]</a>. This indicates that ESM can characterize regions of the protein landscape distant from existing knowledge <a class="yt-timestamp" data-t="01:15:43">[01:15:43]</a>.

## Comparison with AlphaFold

### Core Methodologies

The primary distinction between ESM's approach (specifically ESM-Fold, which is the folding head built on ESM-2) and AlphaFold lies in their handling of protein sequences:

*   **AlphaFold:** DeepMind's AlphaFold model deeply integrates [[multiple_sequence_alignment | multiple sequence alignment]] (MSA) into its neural network architecture <a class="yt-timestamp" data-t="00:52:29">[00:52:29]</a>. MSA involves comparing multiple homologous sequences to infer structure <a class="yt-timestamp" data-t="00:54:37">[00:54:37]</a>. If MSAs are ablated (removed) for AlphaFold, the model's performance degrades significantly <a class="yt-timestamp" data-t="00:59:12">[00:59:12]</a>.
*   **ESM-Fold:** ESM-Fold eliminates the need for [[multiple_sequence_alignment | multiple sequence alignment]] <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>, <a class="yt-timestamp" data-t="00:52:20">[00:52:20]</a>. It predicts structure directly from the primary protein sequence <a class="yt-timestamp" data-t="00:50:15">[00:50:15]</a>. ESM-Fold uses the pre-trained ESM-2 [[large_language_models_for_protein_sequences | language model]] as a feature encoder, feeding its embeddings into a "folding head" which performs iterative updates to sequence and pairwise representations to predict 3D coordinates <a class="yt-timestamp" data-t="00:51:01">[00:51:01]</a>, <a class="yt-timestamp" data-t="00:56:01">[00:56:01]</a>. This single-sequence prediction capability is crucial for *de novo* protein design (creating new proteins from scratch) <a class="yt-timestamp" data-t="01:05:47">[01:05:47]</a>.

### Performance and Speed

ESM boasts significant speed advantages in inference due to its single-sequence approach:

*   **Inference Speed:** AlphaFold can take over 10 minutes to predict a structure <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. In [[comparison_with_existing_models_and_algorithms | comparison]], ESM-Fold can make a prediction on a protein with 384 residues in 14.2 seconds on a single Nvidia V100 GPU <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.
*   **Accuracy:** While ESM-Fold can produce predictions with similar accuracy to RosettaFold <a class="yt-timestamp" data-t="01:00:26">[01:00:26]</a>, and often performs better than AlphaFold, particularly for single-sequence predictions <a class="yt-timestamp" data-t="00:59:20">[00:59:20]</a>, <a class="yt-timestamp" data-t="01:00:45">[01:00:45]</a>, they share some common limitations. Parts of structures where accuracy is low do not differ significantly between ESM-Fold and AlphaFold <a class="yt-timestamp" data-t="01:07:44">[01:07:44]</a>. This suggests both models might be learning similar fundamental low-dimensional representations of proteins <a class="yt-timestamp" data-t="01:08:06">[01:08:06]</a>.

### Metrics for [[comparison_with_existing_models_and_algorithms | Comparison]]

Several metrics are used to quantify performance:

*   **Perplexity:** Measures how well a model predicts a sample; a low perplexity indicates a better prediction <a class="yt-timestamp" data-t="00:32:55">[00:32:55]</a>, <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>. The largest ESM-2 model (15 billion parameters) achieved a perplexity of 6.37, significantly lower than the 8 million parameter model's perplexity of 10 <a class="yt-timestamp" data-t="00:33:27">[00:33:27]</a>.
*   **Precision at L (P@L):** Measures the accuracy of contact map prediction <a class="yt-timestamp" data-t="00:44:22">[00:44:22]</a>, where a "hit" means the correct contact is within the top L most likely predictions <a class="yt-timestamp" data-t="00:42:27">[00:42:27]</a>.
*   **TM Score and pLDDT:** These are common metrics for assessing the similarity between predicted and true 3D protein structures <a class="yt-timestamp" data-t="01:01:05">[01:01:05]</a>.
*   **RMSD (Root Mean Squared Deviation):** Measures the distance between atomic structures, indicating how well the predicted 3D structure maps to the true 3D structure <a class="yt-timestamp" data-t="01:10:35">[01:10:35]</a>.

### Emergent Capabilities

Both [[large_language_models_for_protein_sequences | large language models]] exhibit [[emergent_capabilities_in_protein_modeling | emergent capabilities]] as computation, data, and the number of parameters increase <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. While humans can readily understand emergent intelligence in text-based LLMs, it's more challenging to grasp what [[emergent_capabilities_in_protein_modeling | emergent capabilities]] in protein sequence models might mean <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. The question arises whether these models understand patterns that humans do not <a class="yt-timestamp" data-t="00:09:57">[00:09:57]</a>.

> [!info] Data Considerations
> ESM-2 was trained on a massive dataset of 65 million unique protein sequences, derived from 43 million UniRef50 training clusters and 138 million UniRef90 sequences <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>, <a class="yt-timestamp" data-t="00:32:35">[00:32:35]</a>. These datasets, like UniProt and MGnify, are often funded by government research and non-profit organizations, which supports the open-source nature of such models <a class="yt-timestamp" data-t="01:24:27">[01:24:27]</a>.
>
> ESM-Fold's training data was augmented with 12 million structures created by AlphaFold 2, a practice that could introduce errors <a class="yt-timestamp" data-t="01:04:11">[01:04:11]</a>.

## Conclusion

The development of ESM by Meta represents a significant advancement in [[protein_structure_prediction_using_language_models | protein structure prediction]], offering a faster, single-sequence-based alternative to AlphaFold. Both models demonstrate the powerful application of deep learning to complex biological problems, pushing towards an era where understanding the structure of all discovered proteins might be possible <a class="yt-timestamp" data-t="01:25:14">[01:25:14]</a>. The shared challenges in predicting certain protein regions suggest a common learning bottleneck or an area where current experimental ground truth might even be incomplete <a class="yt-timestamp" data-t="01:12:11">[01:12:11]</a>.