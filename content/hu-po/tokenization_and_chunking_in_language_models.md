---
title: Tokenization and chunking in language models
videoId: YhrwYZ3Nsio
---

From: [[hu-po]] <br/> 

[[multimodal_models_and_tokenization | Tokenization]] is a fundamental process in [[advancements_in_language_models | language models]], involving the breaking down of a sentence of characters into smaller, manageable chunks [00:05:39]. Each of these chunks is typically referred to as a "token" [00:05:47].

## Traditional Tokenization

Traditionally, [[training_and_finetuning_of_language_models_for_code | large language models]] operate by auto-regressively predicting the next discrete token given a sequence of incoming tokens [01:41:36]. This means that the model's output is constrained to a fixed vocabulary of discrete tokens [01:31:51]. The goal of [[multimodal_models_and_tokenization | tokenization]] is to minimize the number of chunks while grouping similar elements together, as seen with words like "throne" or phrases like "Daenerys Targaryen" often remaining as single tokens [00:06:29].

## Advancements in Chunking: Byte Latent Transformer

Recent research explores new ways to chunk information, moving beyond traditional word-based tokens. One such approach is presented in the "Byte Latent Transformer: Patches Scale Better Than Tokens" paper (December 2024, Facebook AI Research) [00:03:59].

This paper introduces a new type of [[multimodal_models_and_tokenization | tokenization]] that encodes bytes into dynamically sized patches [00:05:01]. These "patches" are small segments determined by the entropy of the next byte [00:05:26]. This method aims to allocate more compute and model capacity where data complexity demands it [00:05:28]. The decision of where to break or discretize the sentence is based on a global threshold called Theta G, which is derived from entropy [00:05:52]. For instance, if certain character sequences frequently appear together (e.g., "Daenerys Targaryen"), they are more likely to be grouped into a single patch [00:07:06].

However, the perceived impact of this new method is debated, with some noting that while it shows significantly better scaling than tokenization-based models, it "doesn't feel like it's necessarily a huge breakthrough" [00:07:24]. It is viewed as "the same thing just slightly relabeled and a little bit different" [00:07:53].

## Discrete vs. Continuous Latent Spaces

The concept of [[multimodal_models_and_tokenization | tokenization]] contrasts with reasoning in a [[large_language_models_and_optimization | continuous latent space]]:
*   **Discrete Space**: In traditional [[multimodal_models_and_tokenization | tokenization]], words reside in a discrete space, meaning each token is a distinct, defined chunk [00:12:25]. This allows humans to understand the model's reasoning trace by reading the English tokens of a "Chain of Thought" [00:15:21].
*   **Continuous Latent Space**: Some [[training_and_finetuning_of_language_models_for_code | large language models]] are being trained to reason in an "unrestricted latent space" [00:08:53]. This involves using the last hidden state of the [[training_and_finetuning_of_language_models_for_code | language model]] as a representation of the reasoning state, termed "continuous thought" [00:09:05]. Instead of forcing this high-dimensional vector into a token, it remains as an embedding, which is a vector in a continuous space [00:10:52]. This "fuzziness" potentially allows for more nuance and information than discrete tokens [00:11:31].

While continuous latent spaces can significantly increase information density and allow for reasoning over more complicated concepts, they make the internal "Chain of Thought" unreadable to humans, as it would appear as a series of numbers (e.g., "0.744, 0.7, 0.0031") [00:17:17]. This lack of interpretability makes it harder to determine if there were any "bad steps" in the model's reasoning process [00:16:09].

## Conclusion

The choice of [[multimodal_models_and_tokenization | tokenization]] or chunking scheme for [[advancements_in_language_models | language models]] directly impacts their efficiency and interpretability. From granular byte-level patches to abstract continuous latent spaces, each method offers trade-offs in terms of data density, computational [[compute_efficiency_in_language_models | efficiency]], and human understanding of the model's internal processes. The move towards [[large_language_models_and_optimization | continuous latent space]] reasoning, while offering potential for deeper and faster reasoning, presents challenges in transparency and control.