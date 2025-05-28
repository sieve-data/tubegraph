---
title: Highdimensional spaces and information storage in neural nets
videoId: yOT9WIL_2Kg
---

From: [[hu-po]] <br/> 

[[Deep Learning and Neural Networks | Neural networks]], particularly [[Deep Learning and Neural Networks | Transformers]], store and process information in complex high-dimensional spaces. This intricate mechanism allows models to effectively encode and retrieve vast amounts of knowledge.

## The Nature of Information Storage

Traditionally, within a [[Deep Learning and Neural Networks | Transformer]] block, the **Multi-Layer Perceptron (MLP)** or feed-forward network (FFN) was believed to be the primary location for storing factual knowledge <a class="yt-timestamp" data-t="00:35:36">[00:35:36]</a>. This idea stemmed from research showing that specific neurons within the MLP could be modified to change a model's factual understanding, such as the capital of a country or the location of a landmark <a class="yt-timestamp" data-t="00:35:52">[00:35:52]</a>. In contrast, the attention mechanism was thought to facilitate communication between tokens <a class="yt-timestamp" data-t="00:36:40">[00:36:40]</a>.

However, recent research challenges this strict division of labor. The "Token Former" paper suggests that the attention mechanism itself can replace all linear projections in a [[Deep Learning and Neural Networks | Transformer]] block, including those in the MLP and the Query (Q), Key (K), and Value (V) projections within the attention mechanism <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>. This implies that both attention and MLPs might be performing similar functions:

> "It seems like both of them are really kind of doing the same thing. They're using the property of high dimensional spaces to encode information." <a class="yt-timestamp" data-t="00:55:36">[00:55:36]</a>

## High-Dimensional Spaces and Orthogonality

A core concept underlying information storage in [[Deep Learning and Neural Networks | neural networks]] is the use of high-dimensional vector spaces. Each token (e.g., a word) is represented as a vector in this space, with its position and direction encoding its meaning <a class="yt-timestamp" data-t="00:42:14">[00:42:14]</a>. As a token passes through layers of a [[Deep Learning and Neural Networks | Transformer]], its vector is adjusted, continuously refining its meaning based on context <a class="yt-timestamp" data-t="00:43:19">[00:43:19]</a>.

A key property that enables vast information storage in these spaces is the **Johnson-Lindenstrauss Lemma**:
> "The number of vectors that are between 89 and 91 degrees apart, so almost orthogonal, is not just the dimensionality of the space but grows exponentially with the number of dimensions." <a class="yt-timestamp" data-t="00:49:57">[00:49:57]</a>

In simpler terms, as the dimensionality of a space increases, the number of "almost orthogonal" directions available to encode distinct pieces of information grows exponentially <a class="yt-timestamp" data-t="00:51:58">[00:51:58]</a>. This means a higher-dimensional space has significantly more "real estate" for storing different concepts without them interfering with each other <a class="yt-timestamp" data-t="00:52:51">[00:52:51]</a>.

This phenomenon is crucial for the scaling laws observed in [[Deep Learning and Neural Networks | neural networks]]:
> "This might literally be the reason that [[Deep Learning and Neural Networks | neural nets]] are capable of storing so much information... The higher the dimension of the space, the more information you can encode in there, but it's not even just proportional, it's exponential with the number of dimensions. So this is why as [[Deep Learning and Neural Networks | Transformers]] as models get bigger and bigger and bigger, they're literally the amount of information that they can store is exponentially growing with the size of that." <a class="yt-timestamp" data-t="00:52:09">[00:52:09]</a>

## Attention as a Dynamic Information Retriever

The P-attention layer in Token Former exemplifies this idea by using "learnable tokens" to represent model parameters <a class="yt-timestamp" data-t="00:48:58">[00:49:03]</a>. Input tokens act as queries, and the model parameters act as keys and values <a class="yt-timestamp" data-t="00:28:46">[00:28:46]</a>. This allows the model to "attend" to its own internal parameters, effectively querying and retrieving information dynamically from its [[Generative Latent Spaces in AI | latent space]] <a class="yt-timestamp" data-t="00:28:50">[00:28:50]</a>.

### Queries, Keys, and Values: The Mechanism of Retrieval

*   **Query (Q):** "What am I looking for?" or "What information am I interested in?" <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>
*   **Key (K):** "What do I contain?" or "What information do I have?" <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>
*   **Value (V):** The actual information or "value" associated with a key <a class="yt-timestamp" data-t="00:20:50">[00:20:50]</a>.

The attention mechanism calculates an "agreement" (dot product) between a query and all keys <a class="yt-timestamp" data-t="00:20:17">[00:20:17]</a>. High agreement means the query finds relevant information in that key. The values corresponding to highly agreeable keys are then weighted and added to the token's representation, enriching its meaning based on context <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>.

### Analogies for Understanding Information Storage

*   **Memory Palaces:** Just as humans use memory palaces (method of loci) to store information by associating it with locations in a familiar spatial environment <a class="yt-timestamp" data-t="00:45:28">[00:45:28]</a>, [[Deep Learning and Neural Networks | neural networks]] might be "filling up this very high dimensional space with information" <a class="yt-timestamp" data-t="00:56:52">[00:56:52]</a>. The "treasure map" to this information is the specific sequence of tokens <a class="yt-timestamp" data-t="01:04:04">[01:04:04]</a>.
*   **Language as an Indexing System:** Language itself can be seen as an abstract and powerful indexing system for retrieving memories <a class="yt-timestamp" data-t="01:09:56">[01:09:56]</a>. [[Deep Learning and Neural Networks | Large Language Models (LLMs)]] leverage this by using language to navigate and retrieve information from these high-dimensional spaces <a class="yt-timestamp" data-t="01:30:47">[01:30:47]</a>.
*   **Anamorphic Sculptures:** An anamorphic sculpture appears as a tangle of wires from most angles, but reveals a distinct image (e.g., an elephant or giraffes) when viewed from a specific perspective <a class="yt-timestamp" data-t="00:53:27">[00:53:27]</a>. Similarly, high-dimensional spaces can encode multiple pieces of information that become apparent when "queried" from the right "direction" <a class="yt-timestamp" data-t="00:53:57">[00:53:57]</a>.

> "What [[Deep Learning and Neural Networks | LLMs]] are doing is they're storing billions of little tiny pieces of information inside a very high dimensional space." <a class="yt-timestamp" data-t="01:32:28">[01:32:28]</a>

## Implications for [[memory optimization in neural networks | Model Scaling and Hallucinations]]

The Token Former's ability to incrementally add model parameters by adding "model tokens" allows for progressive and efficient scaling, starting with a small model and growing it during training <a class="yt-timestamp" data-t="01:27:57">[01:27:57]</a>. This approach can save compute and time compared to training a large model from scratch <a class="yt-timestamp" data-t="01:28:47">[01:28:47]</a>. This simplification of [[Deep Learning and Neural Networks | model architecture]], by making computation patterns more uniform, also makes it easier to optimize performance at scale <a class="yt-timestamp" data-t="00:39:57">[00:39:57]</a>.

While this architecture improves scaling efficiency, it may not inherently solve the problem of [[Implications of models reasoning in latent space | hallucinations]]. Hallucinations occur when a model "interpolates" in areas of the high-dimensional space where no actual data was stored during training <a class="yt-timestamp" data-t="01:12:04">[01:12:04]</a>. The model simply samples information from these "Swiss cheese" like gaps, unable to differentiate between true and interpolated facts <a class="yt-timestamp" data-t="01:12:54">[01:12:54]</a>.

> [!INFO] Entropy and Variance in Predictions
> Some theories suggest that the "variance" or "entropy" of a token's prediction can indicate the model's certainty. Low variance might mean the model has "been there before" in the high-dimensional space, indicating a factual prediction from the dataset. High variance might suggest the model is in an "unfamiliar" part of the space, leading to a hallucination <a class="yt-timestamp" data-t="01:14:17">[01:14:17]</a>.