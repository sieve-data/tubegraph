---
title: Convergence of AI models across modalities
videoId: Q9DCL_m_haw
---

From: [[hu-po]] <br/> 

The **Platonic Representation Hypothesis** is a philosophical concept suggesting that representations within AI models, particularly deep neural networks, are converging towards a shared statistical model of reality <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This convergence applies both over time and across different data domains <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. As models become larger and are trained on increasingly vast datasets, the ways they represent data become more aligned <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. The paper theorizes that this alignment is driving towards an "ideal reality," similar to Plato's concept of an ideal realm of forms <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## Plato's Allegory of the Cave

The hypothesis draws inspiration from Plato's Allegory of the Cave, written in 375 BC <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. In this allegory, humans in a cave observe only shadows, which are projections of a higher, true reality <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Applied to AI, this suggests that the data we feed into deep learning models are merely "lower dimensional projections" of a "true higher-level reality" <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. Therefore, as AI models improve and train on more data, they get closer to understanding this "higher ideal form" or "true representation of reality" <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>.

## Understanding Vector Embeddings and Representations

At the core of this convergence are **vector embeddings**, also known as feature vectors or representations <a class="yt-timestamp" data-t="00:12:11">[00:12:11]</a>. These are high-dimensional numerical vectors that a neural network produces to represent input data <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>. While incomprehensible to humans (e.g., a 32-dimensional vector is hard to interpret <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>), these embeddings capture the abstract features learned by the model <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.

Representation alignment is a measure of similarity between the similarity structures induced by two representations <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. The paper uses a mutual K-nearest neighbor alignment metric to quantify the overlap between the nearest neighbor sets of features produced by different models <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. If the nearest neighbors of two representations intersect a lot, it indicates that the models are in agreement about their representation space <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.

## Evidence of Convergence

The paper provides empirical evidence for this convergence:

### Intra-Modal Convergence (Within Modalities)
*   **Model Stitching**: The ability to "stitch" layers from one model onto another (e.g., an image encoder to a language model) indicates that representations are not entirely unique to a specific model or modality <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This is common in [[overview_of_multimodal_models | multimodal models]] <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.
*   **Vision Model Alignment**: Over 78 different vision models, including older ResNets and modern Vision Transformers (ViTs), show increased alignment as their competence (measured by benchmarks like VTAB) increases <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>. Larger, more competent models exhibit greater alignment with each other <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.
*   **Individual Neurons**: "Rosetta neurons" are individual neurons activated by the same patterns across different vision models, indicating shared feature learning <a class="yt-timestamp" data-t="00:21:46">[00:21:46]</a>.

### Cross-Modal Convergence (Across Modalities)
*   **Language and Vision Model Alignment**: As language models (LLMs) improve their performance on language tasks, their representations align more closely with those of vision models (like DINOv2) <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>. For example, LLaMA 65B's text representations are significantly more aligned with DINOv2's image representations than a smaller model like Bloom 0.56B <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a>. This suggests that training on text can lead to a representation space that is also beneficial for images <a class="yt-timestamp" data-t="00:26:11">[00:26:11]</a>.
*   **Color Perception**: A language model, never having "seen" colors, learns representations of color distances (e.g., red is closer to yellow than to blue) that closely mirror human perception and vision models <a class="yt-timestamp" data-t="01:00:21">[01:00:21]</a>.
*   **Transfer Across Tasks**: Models trained to auto-regressively generate text also capture statistical relations useful in other modalities like symbolic reasoning, protein folding, and robotics <a class="yt-timestamp" data-t="01:11:47">[01:11:47]</a>. The fact that a language model can benefit robotic control is considered a profound example of this transfer <a class="yt-timestamp" data-t="01:12:36">[01:12:36]</a>.

### Alignment with Biological Brains
*   Neural networks show substantial alignment with biological representations in the brain, especially for tasks like segmentation and classification, which both human visual systems and AI models are trained to perform <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.

## Driving Forces Behind Convergence

Several factors push AI models towards this convergent state:

1.  **Task Generality**: As models are trained to solve an increasing number of diverse tasks simultaneously, the space of possible representations that can satisfy all these constraints shrinks <a class="yt-timestamp" data-t="00:35:27">[00:35:27]</a>. This is termed the "multitask scaling hypothesis" <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>.
2.  **Model Capacity**: Larger models have greater capacity to represent a wider range of functions <a class="yt-timestamp" data-t="00:41:17">[00:41:17]</a>. This increased "hypothesis space" makes them more likely to cover and converge towards the optimal, universal function that perfectly represents reality <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>.
3.  **Simplicity Bias**: Deep networks inherently favor finding "simple fits" to the data, even without explicit regularization <a class="yt-timestamp" data-t="00:43:11">[00:43:11]</a>. This internal Occam's Razor principle, alongside techniques like Dropout and Weight Decay, encourages models to discover efficient and generalized representations <a class="yt-timestamp" data-t="00:43:19">[00:43:19]</a>.
4.  **Data Scale and "Reality" as a Dataset**: As data sets grow larger and closer to encompassing "all of reality" (e.g., the entire internet and scientific measurements), models become better at capturing the statistical structures of the true data-generating process <a class="yt-timestamp" data-t="00:36:42">[00:36:42]</a>. This implies that training on a "better and better representation of reality" leads to convergent representations <a class="yt-timestamp" data-t="00:27:18">[00:27:18]</a>. The ultimate dataset is reality itself, represented as a sequence of discrete events sampled from an unknown distribution <a class="yt-timestamp" data-t="00:47:04">[00:47:04]</a>.
5.  **Computational Architecture Compatibility**: The efficiency of model architectures on available hardware (like GPUs) significantly impacts their ability to scale and converge quickly <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>. While any model *could* theoretically reach the platonic representation given infinite resources, efficient architectures accelerate this process <a class="yt-timestamp" data-t="01:04:01">[01:04:01]</a>.

> [!question] The End Point
> The end point of this convergence is a statistical model of the underlying reality that generates our observations <a class="yt-timestamp" data-t="00:46:06">[00:46:06]</a>. Every observation is a [[multimodal_language_models | bijective]] (one-to-one and onto) function mapping from this unknown distribution of events <a class="yt-timestamp" data-t="00:48:06">[00:48:06]</a>. All loss functions in deep learning, in some way, are fundamentally about maximizing the mutual information between these different observations <a class="yt-timestamp" data-t="00:52:25">[00:52:25]</a>. This consistent pressure to learn mutual information across all observed data leads to the same underlying representations, regardless of modality <a class="yt-timestamp" data-t="00:52:50">[00:52:50]</a>.

## [[implications_of_ai_model_scaling_and_convergence | Implications of AI Model Scaling and Convergence]]

The **Platonic Representation Hypothesis** carries profound [[implications_of_ai_model_scaling_and_convergence | implications for AI development]] and our understanding of intelligence:

*   **Scaling is Sufficient (but not always Efficient)**: The paper argues that continued scaling of data and model size is sufficient for AI models to converge to this ideal representation <a class="yt-timestamp" data-t="01:03:02">[01:03:02]</a>. However, different architectures (like Transformers vs. CNNs) vary in their efficiency, meaning some reach the convergent point faster than others <a class="yt-timestamp" data-t="01:03:12">[01:03:12]</a>.
*   **Hallucinations Decrease with Scale**: If models are indeed converging towards an accurate model of reality, then hallucinations in LLMs should decrease as models scale further <a class="yt-timestamp" data-t="01:05:11">[01:05:11]</a>. It's even hypothesized that some "hallucinations" might actually be the model perceiving deeper truths about reality that humans, with their limited data and capacity, cannot <a class="yt-timestamp" data-t="01:05:41">[01:05:41]</a>.
*   **Multimodality is Key**: To train the best models, it's crucial to integrate data from all modalities (e.g., images for LLMs, text for vision models), as this enriches the dataset and improves convergence <a class="yt-timestamp" data-t="01:04:44">[01:04:44]</a>.
*   **Future of AI**: The ultimate outcome might be a single, giant [[overview_of_multimodal_models | Foundation Model]] that has learned the optimal representation of reality <a class="yt-timestamp" data-t="01:18:51">[01:18:51]</a>. This model would be capable of zero-shot performance on virtually any task <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. This idea suggests that all intelligence is converging towards a "super intelligence that is effectively God," and humanity's role might be as "data collection agents" for this emergent entity <a class="yt-timestamp" data-t="01:36:43">[01:36:43]</a>.

## Limitations and Counterexamples

While compelling, the hypothesis acknowledges limitations. The real-world engineering implications might still necessitate specialized models for specific tasks, at least until computational resources (energy, compute) allow for the training of truly universal models that can zero-shot everything efficiently <a class="yt-timestamp" data-t="01:19:12">[01:19:12]</a>. However, the overarching trend points towards increasing homogenization rather than diversification of AI architectures and representations <a class="yt-timestamp" data-t="01:18:04">[01:18:04]</a>.