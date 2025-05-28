---
title: Role of largescale genomic databases in training AI models
videoId: I_ll4L9TpU4
---

From: [[hu-po]] <br/> 

Large-scale genomic databases play a crucial role in the development and training of artificial intelligence (AI) models, particularly in the field of protein structure prediction. These extensive datasets enable the training of models with billions of parameters, leading to emergent capabilities in understanding complex biological structures.

## Overview of Databases and Their Scale

Genomic databases have experienced exponential growth due to large-scale gene sequencing experiments, revealing billions of protein sequences <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>. These repositories include:

*   **UniProt** A comprehensive resource providing protein sequence and annotation data, containing approximately 200 million proteins <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>. It is funded by various government and research institutes, including the National Institutes of Health (NIH) and the National Human Genome Research Institute <a class="yt-timestamp" data-t="00:19:35">[00:19:35]</a>.
*   **MGnify90** A microbiome analysis resource that includes over 617 million protein structures <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>. This database is funded by European governments and supports research in areas like cancer and Alzheimer's <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Metagenomic Proteins** Sequences derived from large-scale sequencing of environmental samples, such as pond water, which contain DNA from diverse organisms like bacteria, tadpoles, and plants <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>. These efforts contribute significantly to the rapid growth of protein sequence databases <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

For context, the human genome contains about 20,000 proteins <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. The sheer volume of data in these databases allows for the training of extremely large AI models.

## Role in Training AI Models

Large-scale genomic databases are fundamental to the training of AI models, particularly for tasks like protein structure prediction.

### ESM2 and ESM-Fold Training

Meta's (formerly Facebook) [[Large Language Models and their applications | language model]] for proteins, ESM2, and its related folding model, ESM-Fold, were trained on massive datasets:

*   **Training Data** The ESM2 models were trained using a total of 650 million unique sequences from the UniRef50 (43 million clusters) and UniRef90 (138 million sequences) datasets <a class="yt-timestamp" data-t="00:32:35">[00:32:35]</a>. The training data utilized was current as of September 2021 <a class="yt-timestamp" data-t="01:27:25">[01:27:25]</a>.
*   **Unsupervised Learning** ESM2 is trained with a masked language modeling objective, which is an unsupervised approach <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>. This method allows for the infinite creation of training data from existing protein databases by masking out parts of the protein sequence and training the model to predict the missing portions <a class="yt-timestamp" data-t="00:31:38">[00:31:38]</a>.
*   **Data Sampling** During training, sequences are sampled with even weighting across UniRef50 clusters to prevent the model from overfitting to specific, overrepresented clusters <a class="yt-timestamp" data-t="01:28:48">[01:28:48]</a>.
*   **Scale of Models** ESM2 models range in size from 8 million to 15 billion parameters, making them the largest [[Large Language Models and their applications | language models]] of proteins to date <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>.
*   **Computational Resources** The characterization of 617 million structures was completed in two weeks using a heterogeneous cluster of 2,000 GPUs <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>, <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>.
*   **Synthetic Data for Training** The folding head of ESM-Fold was initially trained on 325,000 experimentally determined structures <a class="yt-timestamp" data-t="01:03:39">[01:03:39]</a>. However, this dataset was later augmented with 12 million additional structures created by AlphaFold2 <a class="yt-timestamp" data-t="01:04:14">[01:04:14]</a>. This highlights a potential strategy for [[Data Generation for AI Models | data generation for AI models]], where models can [[synthetic_data_sets_for_training_ai | synthetically create data sets]] to train even larger subsequent models <a class="yt-timestamp" data-t="02:00:05">[02:00:05]</a>.

### Impact of Data Scale on Model Performance

The size and quality of the training data significantly impact model performance. As demonstrated by ESM2:

*   **Emergent Capabilities** Larger models, trained on more data and for longer durations, exhibit "emergent capabilities" <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>, <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. This means greater capabilities emerge as computation, data, and the number of parameters increase <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>.
*   **Perplexity Improvement** As models scale from 8 million to 15 billion parameters, their perplexity (a measure of uncertainty) decreases from 10 to 6.37, indicating improved understanding of protein sequences <a class="yt-timestamp" data-t="00:33:32">[00:33:32]</a>, <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>.
*   **Non-linear Improvements** The accuracy of predictions shows non-linear improvements as model scale increases, often appearing as "reflection points" or "emergence points" where performance suddenly jumps <a class="yt-timestamp" data-t="00:36:43">[00:36:43]</a>, <a class="yt-timestamp" data-t="00:36:48">[00:36:48]</a>. This aligns with findings in other large AI models regarding [[Implications of AI model scaling and convergence | AI model scaling and convergence]].
*   **Data Saturation** While larger models generally perform better, there may be a point where the data set size becomes the limiting factor. The perplexity gap between the 150 million and 15 billion parameter models of ESM2 is relatively small, suggesting the data set size might be reaching its limit for current models <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>, <a class="yt-timestamp" data-t="00:47:47">[00:47:47]</a>. This highlights [[the_role_of_data_quality_and_training_scale_in_ai_models | the role of data quality and training scale in AI models]].

## Challenges and Future Directions

Despite the advancements, challenges remain:

*   **Data Quality** The accuracy of experimentally determined protein structures in these large databases is crucial, as mislabeled or inaccurate data could impact model training <a class="yt-timestamp" data-t="01:11:27">[01:11:27]</a>. The models may even uncover inaccuracies in existing ground truths <a class="yt-timestamp" data-t="01:12:18">[01:12:18]</a>.
*   **Novel Structures** ESM-Fold has predicted 225 million high-confidence structures, with millions of these being novel compared to experimentally determined structures in existing databases <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>, <a class="yt-timestamp" data-t="01:15:26">[01:15:26]</a>. This demonstrates the model's ability to characterize regions of the protein landscape distant from existing knowledge <a class="yt-timestamp" data-t="01:15:47">[01:15:47]</a>.
*   **Open Access** Many of these large-scale genomic databases and the resulting AI models (like ESM-Fold) are being made [[Open source AI models and accessibility | open source and publicly accessible]] <a class="yt-timestamp" data-t="01:16:17">[01:16:17]</a>, <a class="yt-timestamp" data-t="01:24:24">[01:24:24]</a>. This is largely due to the public funding of the underlying research and data collection efforts <a class="yt-timestamp" data-t="01:24:31">[01:24:31]</a>.

The ability of AI models to infer protein structure directly from primary sequence using large language models is a significant step forward <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The continuous growth and accessibility of large-scale genomic databases are vital for pushing the boundaries of AI in biological applications, with potential for discovering new medicines and molecules <a class="yt-timestamp" data-t="02:00:24">[02:00:24]</a>.