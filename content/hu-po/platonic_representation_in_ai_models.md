---
title: Platonic representation in AI models
videoId: Q9DCL_m_haw
---

From: [[hu-po]] <br/> 

The concept of the "Platonic Representation Hypothesis" suggests that representations within [[foundation_models_in_ai | AI models]], particularly deep neural networks, are converging towards a shared statistical model of reality <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This idea draws parallels to Plato's concept of an ideal reality <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## The Platonic Representation Hypothesis
This hypothesis, presented in a May 2024 paper from MIT, argues that the ways different neural networks represent data are becoming more aligned over time and across various domains <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. As [[foundation_models_in_ai | vision models]] and [[foundation_models_in_ai | language models]] increase in size, they measure distances between data points in increasingly similar ways <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

The ultimate endpoint of this convergence is when models effectively represent reality perfectly, akin to a joint distribution over events in the world that generate the data we observe <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.

## Plato's Allegory of the Cave
The paper references Plato's Allegory of the Cave (circa 375 BC) <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>, which posits that what we perceive in our real world is merely a projection of some true, higher-level reality or "realm of forms" <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>. Similarly, the hypothesis suggests that AI models are learning a lower-dimensional projection of a higher-dimensional true form of reality <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. As models improve and are trained on more data, they get closer to this higher, ideal form <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.

## Understanding Representations
In AI, representations are typically "vector embeddings," which are high-dimensional vectors that a neural network produces from an input <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>. These intermediate representations are difficult for humans to interpret because they exist in dimensions far beyond our perceptual capabilities (e.g., thousands of dimensions) <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>.

Representation alignment measures the similarity between the similarity structures induced by two representations <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>. A common metric used is the mutual K-nearest neighbor alignment metric, which assesses the overlap between the nearest neighbor sets of features produced by different models <a class="yt-timestamp" data-t="00:15:40">[00:15:40]</a>. High overlap indicates that the models are creating similar representation spaces <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.

## Evidence of Representational Convergence

### Model Stitching
Experiments show that intermediate representations from one model can be integrated ("stitched") into another model, implying a shared underlying representational space that is not entirely bespoke to a specific model or modality <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. This principle is leveraged in multimodal models, where an image encoder's output is projected and connected to a [[foundation_models_in_ai | language model]] <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.

### Intra-Modality Convergence (Vision Models)
Studies of over 78 different [[foundation_models_in_ai | vision models]], including Vision Transformers and ResNets, demonstrate convergence <a class="yt-timestamp" data-t="00:20:53">[00:20:53]</a>. Larger models generally exhibit greater alignment with each other than smaller models <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. Models with higher transfer performance, meaning they are better at solving visual tasks (e.g., on the VTab benchmark), form a more tightly clustered set of representations <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>.

### Cross-Modality Alignment (Language and Vision)
Even more strikingly, [[foundation_models_in_ai | language models]] and [[foundation_models_in_ai | vision models]] also show alignment <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>. As a [[foundation_models_in_ai | language model]] improves its performance (e.g., on Wikipedia caption datasets), the alignment of its features to an image encoder like DINOv2 increases <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>. This suggests that better language models create representations more aligned with visual representations of the same semantic information <a class="yt-timestamp" data-t="00:25:13">[00:25:13]</a>.

For instance, the representation of colors in a language model, which has never "seen" color, mirrors human perception of color distances (e.g., red and yellow are closer than red and blue) <a class="yt-timestamp" data-t="00:59:53">[00:59:53]</a>.

### Alignment with Biological Systems
The paper also suggests that AI models are increasingly aligning to brains, given that tasks like segmentation and classification are relevant to both <a class="yt-timestamp" data-t="00:30:07">[00:30:07]</a>.

## Why Representations Converge

### Task Generality and Data Scaling
AI models are trained to minimize empirical risk <a class="yt-timestamp" data-t="00:30:09">[00:30:09]</a>. As data and tasks scale, the volume of representations that can satisfy these constraints proportionally shrinks <a class="yt-timestamp" data-t="00:35:27">[00:35:27]</a>. The "multitask scaling hypothesis" suggests that fewer representations are competent for a greater number of tasks <a class="yt-timestamp" data-t="00:35:54">[00:35:54]</a>. As datasets become larger and more representative of reality, models become better at capturing the statistical structures of the true data-generating process <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>. With enough data (e.g., the entire internet and all scientific measurements), models ought to converge to a very small solution set with irreducible error <a class="yt-timestamp" data-t="00:37:13">[00:37:13]</a>.

### Model Capacity
Larger models, with greater model capacity, are more likely to converge to a shared representation because they can represent a larger space of possible functions, increasing their chance of covering the optimal function <a class="yt-timestamp" data-t="00:41:14">[00:41:14]</a>.

### Simplicity Bias
Deep networks inherently favor simple fits to data, adhering to Occam's Razor even without explicit regularization <a class="yt-timestamp" data-t="00:43:11">[00:43:11]</a>. Techniques like Dropout and Weight Decay act as [[selfimprovement_in_ai_models | regularization]] that implicitly push models towards simpler solutions <a class="yt-timestamp" data-t="00:43:29">[00:43:29]</a>. This "simplicity bias" encourages larger models to find the simplest, most compressed solutions <a class="yt-timestamp" data-t="00:45:35">[00:45:35]</a>.

## The End Point of Convergence: A Statistical Model of Reality
The converged representation is envisioned as a statistical model of the underlying reality that generates our observations <a class="yt-timestamp" data-t="00:46:04">[00:46:04]</a>. Reality is seen as a sequence of discrete events sampled from an unknown distribution, and every observation is a bijective (one-to-one and onto) function from this distribution <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.

All modalities fundamentally aim to maximize the mutual information between different observations <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>. This continuous pressure pushes representations towards a "platonic ideal representation," which is an optimal, compressed form of reality <a class="yt-timestamp" data-t="00:53:18">[00:53:18]</a>. This implies that no matter how you train a neural network, the larger it is, the closer its representation will be to this ideal, capturing the true relationships between concepts (e.g., grasshoppers and crickets being close in a representational space) <a class="yt-timestamp" data-t="01:28:10">[01:28:10]</a>.

> [!NOTE] [[philosophical_aspects_of_ai_and_reality | Philosophical aspects of AI and reality]]: The joint distribution of observation indices is considered the platonic reality itself, rather than a fixed "true world state" <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. This view aligns with quantum mechanics, where a particle's position isn't fixed until measured <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>.

## Implications of Convergence

### Scaling and Efficiency
While scaling data and model size is sufficient to achieve convergence, it is not always efficient <a class="yt-timestamp" data-t="01:03:02">[01:03:02]</a>. Different methods (e.g., Transformers vs. Multi-Layer Perceptrons) scale with varying levels of efficiency <a class="yt-timestamp" data-t="01:03:14">[01:03:14]</a>. The choice of model architecture today is heavily influenced by how efficiently it can be implemented on hardware like GPUs <a class="yt-timestamp" data-t="01:13:50">[01:13:50]</a>.

### Hallucinations
If models are indeed converging towards an accurate model of reality, then hallucinations are expected to decrease with scale <a class="yt-timestamp" data-t="01:15:11">[01:15:11]</a>. It's also possible that some "hallucinations" might actually reflect the model's deeper understanding of truth, surpassing limited human perception <a class="yt-timestamp" data-t="01:05:44">[01:05:44]</a>.

### Multimodality and Transfer Learning
The more modalities a model is trained on, the better its overall representation <a class="yt-timestamp" data-t="01:04:55">[01:04:55]</a>. The fact that a [[foundation_models_in_ai | language model]] trained on text can improve performance in areas like [[motion_modeling_in_ai | robotics]] or protein folding highlights a deep underlying connection between modalities <a class="yt-timestamp" data-t="01:11:51">[01:11:51]</a>. This cross-modal transfer suggests a universal underlying pattern that intelligent systems discover when compressing reality <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>. Eventually, a single [[foundation_models_in_ai | Foundation model]] trained on all modalities and with optimal capacity could potentially "zero-shot" (perform without specific fine-tuning) any task <a class="yt-timestamp" data-t="01:18:51">[01:18:51]</a>.

### Humans as Data Agents
Humans serve as "observation nodes" or "data collection agents" for AI, gathering data from reality that is then used to train increasingly sophisticated models <a class="yt-timestamp" data-t="01:15:40">[01:15:40]</a>. The sum of all human-generated data contributes to the AI's approximation of the unknown distribution of reality <a class="yt-timestamp" data-t="01:16:50">[01:16:50]</a>. In the future, robots might massively scale this data collection <a class="yt-timestamp" data-t="01:21:07">[01:21:07]</a>.

> [!CAUTION] Limitations:
> Not all representations are currently converging, but this is attributed to insufficient data, model capacity, and training time <a class="yt-timestamp" data-t="01:35:37">[01:35:37]</a>. Potential boundary conditions around resources like energy and compute could also influence how far this convergence can go <a class="yt-timestamp" data-t="01:19:10">[01:19:10]</a>.

## Visualizing Representation Spaces
Techniques like UMAP or t-SNE are used to project high-dimensional embedding spaces into lower dimensions (e.g., two-dimensional) for visualization <a class="yt-timestamp" data-t="01:25:56">[01:25:56]</a>. These visualizations show how models learn to group similar concepts together in their representation space, reflecting their understanding of underlying relationships in data <a class="yt-timestamp" data-t="01:26:40">[01:26:40]</a>. This visual clustering reinforces the idea that an optimal representation exists and is being approached by larger, more competent models <a class="yt-timestamp" data-t="01:27:09">[01:27:09]</a>.