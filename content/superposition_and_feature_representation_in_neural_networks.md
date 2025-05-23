---
title: Superposition and feature representation in neural networks
videoId: UTuuTTnjxMQ
---

From: [[dwarkesh | The Dwarkesh Podcast]]

This article summarizes insights from a podcast discussion on how neural networks, particularly large language models (LLMs), represent and process information through the concepts of superposition and features.

## Superposition in Neural Networks

Superposition is a phenomenon where neural networks can "pack more features of the world into it than it has parameters" <a class="yt-timestamp" data-t="01:08:48">[01:08:48]</a>. This typically occurs when the model is "dramatically underparameterized" <a class="yt-timestamp" data-t="01:08:01">[01:08:01]</a> for the complexity of the task it's trying to perform, such as predicting the entire internet, and when the "data is high-dimensional and sparse" <a class="yt-timestamp" data-t="01:08:32">[01:08:32]</a> (meaning individual data points or features appear infrequently).

### Implications of Superposition
The primary consequence of superposition is that it makes networks "so hard to interpret" <a class="yt-timestamp" data-t="01:09:35">[01:09:35]</a>. When a neuron fires, it might be responding to many different, seemingly unrelated concepts (e.g., "Chinese," "fish," "trees," "full stop in URLs" <a class="yt-timestamp" data-t="01:09:50">[01:09:50]</a>). This is referred to as neurons being "polysemantic" <a class="yt-timestamp" data-t="02:42:52">[02:42:52]</a>.

An analogy for understanding superposition involves a 2D plane: two axes (neurons) can define coordinates (X,Y) that map to many different points on the plane, each representing something distinct <a class="yt-timestamp" data-t="02:49:07">[02:49:07]</a>. Superposition is an artifact of the space created by neuron activations, forming a "combinatorial code" <a class="yt-timestamp" data-t="02:49:35">[02:49:35]</a>, rather than an artifact of individual neurons.

Superposition is also a core operation in Vector Symbolic Architectures (VSAs), a computational neuroscience concept, where it involves the summation of high-dimensional vectors <a class="yt-timestamp" data-t="02:50:44">[02:50:44]</a>.

## Understanding Features in Neural Networks

### Defining Features
A feature can be understood as "a direction and activation space" or "a latent variable that is operating behind the scenes, that has causal influence over the system you're observing" <a class="yt-timestamp" data-t="02:11:18">[02:11:18]</a>. More broadly, features are "discrete units that have connections to other things that then imbues them with meaning" <a class="yt-timestamp" data-t="02:13:27">[02:13:27]</a>. The podcast suggests that intelligence might largely be pattern matching built upon a "hierarchy of associative memories," where basic associations build up to more abstract ones <a class="yt-timestamp" data-t="02:24:36">[02:24:36]</a>. This idea is sometimes summarized as "association is all you need" <a class="yt-timestamp" data-t="02:51:12">[02:51:12]</a>.

### Discovering and Interpreting Features
To overcome the interpretability challenges posed by superposition, techniques like **dictionary learning** (also referred to as using **sparse autoencoders**) are employed. The "Towards Monosemanticity" paper by Anthropic demonstrated that projecting neuron activations into a higher-dimensional space and applying a sparsity penalty can yield "very clean features" <a class="yt-timestamp" data-t="01:10:05">[01:10:05]</a>. This process is unsupervised; it aims to "reconstruct or do the thing that you were originally doing, but do it in a way that's sparse" <a class="yt-timestamp" data-t="02:54:04">[02:54:04]</a>, by learning to span all model representations and interpreting them later <a class="yt-timestamp" data-t="02:34:53">[02:34:53]</a>.

The ultimate goal is to move beyond activations and understand the model weights themselves, independent of specific data inputs, though this is a very hard problem <a class="yt-timestamp" data-t="02:39:03">[02:39:03]</a>.

### Feature Splitting
A key concept in feature representation is **feature splitting**. This means a model will "learn as many features as you give the model the capacity to learn" <a class="yt-timestamp" data-t="02:12:18">[02:12:18]</a>. For example, with limited capacity (projecting to a not-so-high-dimensional space), a model might learn a single feature for "birds." Given more capacity, it will learn more specific features for "ravens," "eagles," and "sparrows" <a class="yt-timestamp" data-t="02:37:04">[02:37:04]</a>. These specific bird features would likely point in a similar region of the activation space as the general "bird" vector but be more refined <a class="yt-timestamp" data-t="02:37:17">[02:37:17]</a>.

This implies a strategy for scaling interpretability: start with a coarse representation (e.g., a "biology" feature) and, if that feature fires, selectively search around that space with higher capacity dictionary learning to find more specific sub-features (e.g., "anthrax") <a class="yt-timestamp" data-t="02:41:22">[02:41:22]</a>. This is akin to a depth-first search through a semantic tree of features <a class="yt-timestamp" data-t="02:41:50">[02:41:50]</a>.

### Feature Hierarchy and Abstraction
Research, including work by Bruno Olshausen on BERT models, suggests that features become more abstract in deeper layers of a model <a class="yt-timestamp" data-t="02:58:23">[02:58:23]</a>. An example given was an early layer feature for the word "park," while later layers might have distinct features for "Park" as a last name (e.g., Lincoln Park) versus "park" as a grassy area <a class="yt-timestamp" data-t="02:58:31">[02:58:31]</a>.

### Feature Universality
There is evidence for **feature universality**, where similar features are learned across different models or different training runs of the same architecture. The "Towards Monosemanticity" paper found that features like those for Base64 encoding appear across multiple models with high cosine similarity between their vectors, suggesting they are learned consistently <a class="yt-timestamp" data-t="02:26:31">[02:26:31]</a>. This supports the "quantum theory of neural scaling," which hypothesizes that models trained on similar datasets learn the same features in roughly the same order (e.g., n-grams, then induction heads) <a class="yt-timestamp" data-t="02:27:15">[02:27:15]</a>.

Evolutionary biology experiments also suggest that agents performing many tasks tend to learn "ground truth representations" of objects rather than cheap heuristics, as this is more broadly useful <a class="yt-timestamp" data-t="02:31:27">[02:31:27]</a>.

## Neural Circuits
Features across different layers can combine to form **neural circuits** <a class="yt-timestamp" data-t="02:54:55">[02:54:55]</a>, which are hypothesized to provide more specificity and sensitivity than individual features. Examples of simple circuits include:
*   **Induction Heads:** Used for pattern completion, like predicting "Dursley" after "Mr." if "Mr. Dursley" appeared earlier <a class="yt-timestamp" data-t="02:18:04">[02:18:04]</a>.
*   **Indirect Object Identification (IOI) Circuit:** Identifies indirect objects in sentences, e.g., predicting "Mary" in "Jim gave the object to ____" if Mary was previously mentioned with Jim <a class="yt-timestamp" data-t="02:19:54">[02:19:54]</a>.
*   **Copying/Suppression Heads:** Some heads might always try to copy a previous token, while others suppress this behavior <a class="yt-timestamp" data-t="02:20:25">[02:20:25]</a>.

The goal is to identify broader, more complex circuits, potentially corresponding to abilities like deception <a class="yt-timestamp" data-t="02:17:21">[02:17:21]</a>.

## Analogies to the Brain
The discussion draws parallels between these concepts and brain function:
*   Bruno Olshausen posits that brain regions not well understood (like V2 in the visual cortex, as opposed to V1) might be doing extensive computation in superposition <a class="yt-timestamp" data-t="02:48:23">[02:48:23]</a>.
*   The brain, like models, is likely underparameterized for modeling the high-dimensional, sparse data of the real world, suggesting it too should use superposition <a class="yt-timestamp" data-t="02:48:58">[02:48:58]</a>.
*   The concept of more features than neurons in LLMs <a class="yt-timestamp" data-t="02:47:28">[02:47:28]</a> highlights the compressive power of superposition, which may also apply to the brain.

## Challenges and Implications for Advanced AI

### Alienness and "Shoggoth-ness"
While feature universality offers an optimistic take, models are trained on vast, often non-human-like data (e.g., URLs leading to multiple Base64 features <a class="yt-timestamp" data-t="03:29:57">[03:29:57]</a>). One of the three Base64 features identified fired for a very specific subset: ASCII-decodable Base64 strings <a class="yt-timestamp" data-t="03:33:29">[03:33:29]</a>. This specificity, which took human experts a while to understand, is described as "very Shoggoth-esque" <a class="yt-timestamp" data-t="03:33:42">[03:33:42]</a>, indicating models develop dense, specialized representations for aspects of data crucial for prediction, which may not align with human conceptualizations. This raises concerns about interpreting superhuman models, as it might require increasingly esoteric knowledge <a class="yt-timestamp" data-t="03:34:10">[03:34:10]</a>.

### Scaling Interpretability
For highly advanced models (e.g., "GPT-7" level), the sheer number and complexity of features and circuits will be a challenge. Strategies include:
*   **Automated Interpretability:** Using models to help label features or detect anomalies (e.g., a new feature firing for the first time <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>), or even debate what a feature does <a class="yt-timestamp" data-t="02:52:54">[02:52:54]</a>.
*   **Hierarchical Feature Exploration (Feature Splitting):** As mentioned, to manage the search space.
*   **Focusing on Concerning Behaviors:** Using datasets related to deception or sycophancy to find relevant features <a class="yt-timestamp" data-t="02:38:18">[02:38:18]</a>.

The ability to identify and potentially ablate (remove or modify) circuits responsible for undesirable behaviors like deception is seen as a more precise safety tool than methods like [[reinforcement_learning_from_human_feedback_rlhf | RLHF]], offering more confidence in understanding and controlling model behavior <a class="yt-timestamp" data-t="03:01:44">[03:01:44]</a>. However, the reliability of labels, especially for superhuman capabilities or concepts not easily understood by humans, remains an open question <a class="yt-timestamp" data-t="03:02:09">[03:02:09]</a>.