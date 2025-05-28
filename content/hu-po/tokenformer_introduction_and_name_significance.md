---
title: Tokenformer introduction and name significance
videoId: yOT9WIL_2Kg
---

From: [[hu-po]] <br/> 

Tokenformer is a novel model architecture that challenges conventional approaches to [[Transformer scaling with tokenized model parameters | Transformer scaling]]. It proposes replacing traditional linear projections within a Transformer block with a new attention mechanism where model weights are treated as tokens themselves <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This approach suggests that "attention is all you need" to an extreme extent <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

## Origin and Naming Significance

The Tokenformer paper, "TokenFormer: Rethinking Transformer Scaling with Tokenized Model Parameters," was released on October 30th <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. It is a collaborative effort from the Max Planck Institute for Informatics, Google, and Peking University <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

The name "Tokenformer" itself is considered "kind of a cool name" <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>. Notably, the researchers "resisted" naming it a variant of "Attention Is All You Need," despite their findings suggesting that attention mechanisms can replace every part of a Transformer block <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This highlights the paper's core assertion: that attention alone seems sufficient for Transformer operations <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Technical Innovations

### Replacing Linear Projections with P-attention

In traditional Transformers, linear projections use a fixed number of parameters (a matrix of weights multiplied by an input vector) <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>. These dimensions are "hardcoded" when the neural network is initialized and do not change during training or inference <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>. Changing these dimensions typically requires retraining the entire model <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>.

Tokenformer introduces "P-attention" (parameter attention) <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a>. This mechanism replaces all linear projections in a Transformer, including those for queries (Q), keys (K), values (V) in the attention mechanism, and within the Multi-Layer Perceptron (MLP) or Feed-Forward Network (FFN) <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>, <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>. In P-attention, model parameters are represented as "learnable tokens" or "trainable tokens" <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>.

### How P-attention Works

P-attention employs cross-attention between input tokens and these special "model parameter tokens" <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. The input tokens act as queries, while the model parameter tokens act as keys and values <a class="yt-timestamp" data-t="00:29:10">[00:29:10]</a>.

*   **Queries**: Represent "what am I looking for?" <a class="yt-timestamp" data-t="00:19:12">[00:19:12]</a>.
*   **Keys**: Represent "what do I contain?" <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.
*   **Values**: The information to be extracted when there's high agreement between a query and a key <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.

This reformulation allows for "progressive and efficient scaling" <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>. As the model scales, new learnable tokens can be added to expand the existing key and value parameter sets <a class="yt-timestamp" data-t="00:27:27">[00:27:27]</a>, effectively reusing pre-trained weights <a class="yt-timestamp" data-t="00:30:58">[00:30:58]</a>. This means a smaller model can be trained initially, and then more tokens can be incrementally added to grow the model over time <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. This incremental growth saves training compute and time, as it allows for faster training initial stages <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

### Implications for Understanding [[Foundation models in AI | Transformer Models]]

Tokenformer's success in replacing MLPs with attention mechanisms challenges the long-held belief that MLPs primarily store factual knowledge, while attention handles communication between tokens <a class="yt-timestamp" data-t="00:36:30">[00:36:30]</a>. If Tokenformer can perform well without MLPs, it suggests that both components might be performing similar roles in storing and retrieving information <a class="yt-timestamp" data-t="00:55:16">[00:55:16]</a>.

In Transformers, approximately two-thirds of the total parameters are dedicated to the FFN/MLP <a class="yt-timestamp" data-t="00:37:48">[00:37:48]</a>. Replacing these with attention mechanisms could lead to "smaller models, more simpler models" <a class="yt-timestamp" data-t="00:38:06">[00:38:06]</a>. Furthermore, if all operations use the same attention kernel, it simplifies optimization efforts for the entire architecture <a class="yt-timestamp" data-t="00:38:28">[00:38:28]</a>.

### The Role of High-Dimensional Spaces

The effectiveness of neural networks, and attention specifically, in storing vast amounts of information can be intuited through the Johnson-Lindenstrauss Lemma <a class="yt-timestamp" data-t="00:49:37">[00:49:37]</a>. This lemma suggests that in an n-dimensional space, the number of almost-orthogonal vectors (vectors between 89 and 91 degrees apart) grows exponentially with the number of dimensions <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>. This means that high-dimensional spaces offer significantly more "real estate" to store distinct concepts or meanings as directions <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a>.

Each layer of a Transformer block continuously adjusts the meaning of a token by adding vectors based on context, effectively moving it around in this high-dimensional semantic space <a class="yt-timestamp" data-t="00:43:05">[00:43:05]</a>. The deeper the model, the more adjustments are made, allowing for more nuanced representations <a class="yt-timestamp" data-t="01:03:15">[01:03:15]</a>.

This principle extends to different data modalities:
*   **Language**: Language acts as a powerful indexing and retrieval system for memories and ideas in the brain <a class="yt-timestamp" data-t="00:41:17">[00:41:17]</a>. In [[Tokenization and synthetic data generation in language models | LLMs]], tokens effectively serve as "treasure maps" to specific pieces of information stored in this high-dimensional space <a class="yt-timestamp" data-t="01:04:04">[01:04:04]</a>.
*   **Vision**: In [[Challenges and Advances in Image Tokenization | image tokenization]], the order of patches (tokens) in an image might not matter as much as for text, due to visual data's redundancy and spatial properties <a class="yt-timestamp" data-t="01:08:11">[01:08:11]</a>, <a class="yt-timestamp" data-t="01:09:01">[01:09:01]</a>. Models can learn to extract meaning even with randomized token orders, demonstrating the flexibility of high-dimensional space storage <a class="yt-timestamp" data-t="01:09:07">[01:09:07]</a>.

The ability of attention to encode questions, answers, and values allows for a flexible and powerful way to navigate and retrieve information within these vast high-dimensional spaces, suggesting that its structure is particularly well-suited for information storage beyond simple linear projections <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>.

> "The more you have more real estate to store information so if language is a is a way of retrieving information that's stored then a very high dimensional space and a very with the with the kind of language on top of that what Transformers and what attention is really doing is it's basically encoding information it's storing information in these very very high-dimensional space spaces..." <a class="yt-timestamp" data-t="00:52:49">[00:52:49]</a>

## Related Concepts & Papers

### Differential Transformer
The Differential Transformer, another attention-focused paper, highlights how subtracting two softmax attention maps can cancel noise and promote a sparse attention pattern <a class="yt-timestamp" data-t="01:19:21">[01:19:21]</a>. This suggests that often only the "dominant directions" or significant additions of value vectors matter, and smaller adjustments can be effectively ignored without losing critical information <a class="yt-timestamp" data-t="01:21:36">[01:21:36]</a>.

### Hallucinations
The concept of storing information in high-dimensional spaces also sheds light on hallucinations. While a model stores "truths" from its training data at specific points in this space, it can "interpolate" or "extrapolate" to areas where no real data exists, leading to fabricated facts <a class="yt-timestamp" data-t="01:12:04">[01:12:04]</a>. The "variance" or "entropy" in a model's predictions can indicate its certainty about a token's truthfulness, differentiating between known data points and potential hallucinations <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>, <a class="yt-timestamp" data-t="01:16:25">[01:16:25]</a>.

> [!Note] GAT (Graph Attention Mechanism)
> A user asked about GAT (Graph Attention Mechanism) and its utility in smart cities <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. This is distinct from the Tokenformer's focus on general Transformer blocks <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.

## Conclusion

Tokenformer offers a paradigm shift by demonstrating that attention mechanisms might be "all you need" to construct highly effective Transformer architectures, streamlining operations and enabling more efficient scaling. This work challenges our fundamental understanding of how [[Transformer scaling with tokenized model parameters | Transformer models]] store and process information, pointing to the underlying power of high-dimensional spaces for knowledge representation.