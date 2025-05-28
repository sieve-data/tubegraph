---
title: Layerwise scaling in transformer architectures
videoId: YEm4tuo2HPA
---

From: [[hu-po]] <br/> 
### Layerwise Scaling in Transformer Architectures

Layerwise scaling is an architectural strategy employed in [[Transformer architecture in image processing | Transformer]] models, notably highlighted by Apple in their OpenELM paper <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. It addresses the conventional practice in most [[Transformer architecture in image processing | Transformers]] of uniformly allocating parameters across all layers <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.

#### Concept and Purpose
Traditional [[Transformer architecture in image processing | Transformer]] models maintain a consistent configuration for each layer, meaning the number of attention heads and the dimensions of the Feed Forward Network (FFN) remain the same throughout the model <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. Layerwise scaling, however, deviates from this by adapting these parameters based on the specific layer <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.

The rationale behind this approach is that different layers within a [[Transformer architecture in image processing | Transformer]] hierarchy handle varying levels of abstraction <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. Lower layers typically operate in a more "lower-level feature space," while higher layers process "more abstract, higher-level feature space" <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. Therefore, it is logical to adjust the width and number of heads to suit the specific needs of each layer within this hierarchy <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>.

#### Implementation Details
In layerwise scaling, the dimensionality of the FFN and the number of heads in the multi-head attention mechanism are varied <a class="yt-timestamp" data-t="00:16:50">[00:16:50]</a>. This adjustment is controlled by hyperparameters:
*   `Alpha Min` and `Alpha Max` govern the scaling of attention heads <a class="yt-timestamp" data-t="00:17:51">[00:17:51]</a>.
*   `Beta Min` and `Beta Max` manage the variation in the width of the FFN layer <a class="yt-timestamp" data-t="00:17:57">[00:17:57]</a>.

Instead of a uniform structure, the model dynamically adapts its internal components as it processes information through its stacked Transformer blocks <a class="yt-timestamp" data-t="00:18:12">[00:18:12]</a>.

#### Historical Context
Despite being a highlight in recent papers like OpenELM, layerwise scaling is not a new invention <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>. The concept dates back to approximately 2019 or 2020 <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>. Its emphasis by Apple suggests its continued relevance as one of the effective [[challenges_and_insights_in_transformer_architecture_and_training | architectural tricks]] for improving model efficiency and performance.

> "for some reason they chose to kind of explain what layerwise scaling is" <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>

#### Role in OpenELM
OpenELM leverages this strategy to achieve significant improvements in accuracy while requiring fewer pre-training tokens <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. For example, a 1-billion parameter OpenELM model shows a 2.36% accuracy improvement over MMO, despite requiring two times fewer pre-training tokens <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This counter-intuitive result (smaller model, fewer tokens, yet better performance) is partly attributed to the benefits derived from [[Layerwise scaling in transformer architectures | layerwise scaling]] and other [[challenges_and_insights_in_transformer_architecture_and_training | training tricks]] <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.