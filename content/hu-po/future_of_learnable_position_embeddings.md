---
title: Future of learnable position embeddings
videoId: PFxi6SmozZ4
---

From: [[hu-po]] <br/> 

The ongoing development of [[positional_embeddings_in_transformers | positional embeddings]] for Transformer models raises a fundamental question within deep learning: should these critical components be hand-engineered or learned by the model itself? This debate aligns with "[[The Bitter Lesson]]" principle, suggesting that methods leveraging computation and scale ultimately prove most effective <a class="yt-timestamp" data-t="01:23:30">[01:23:30]</a>.

## Current State: Hand-Engineered Complexity

Current approaches to [[Rotary Position Embeddings and Long Contexts | Rotary Position Embeddings]] (RoPE) and its derivatives, such as Long Rope, involve intricate human-designed formulas. These methods modify how Transformer models understand the relative position of tokens in a sequence <a class="yt-timestamp" data-t="01:13:11">[01:13:11]</a>.

For instance, the original RoPE concept involves rotating vectors based on complex, hand-defined angles determined by trigonometric functions <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>. Innovations like Long Rope further complicate this by introducing evolutionary search to find optimal scaling factors for these rotations and arbitrary "non-uniformities" in interpolation, such as holding the first `n` tokens unchanged <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>.

> [!INFO] A "Remix on a Remix"
> Long Rope is described as a "remix on a remix on a remix" <a class="yt-timestamp" data-t="02:02:02">[02:02:04]</a>, starting from original [[positional_embeddings_in_transformers | position embeddings]], moving to [[Rotary Position Embeddings and Long Contexts | rotary position embeddings]], then to position interpolation (like in the Meta paper) and Yarn, and finally to Long Rope <a class="yt-timestamp" data-t="03:36:38">[03:36:38]</a>. This progression shows increasing human-designed complexity.

The values for elements like the base of 10,000 in the `Theta J` formula are arbitrary, "just some random dude came up with this 10,000" <a class="yt-timestamp" data-t="01:45:18">[01:45:18]</a>. Similarly, the "non-uniformities" in Long Rope, like the `n hat` parameter (the number of initial tokens without interpolation) and the arbitrary frequency binning in Yarn, are human heuristics <a class="yt-timestamp" data-t="01:20:00">[01:20:00]</a>. While Long Rope uses [[evolutionary_search_for_optimizing_embeddings | evolutionary search]] to find optimal values for these hand-designed parameters <a class="yt-timestamp" data-t="00:58:14">[00:58:14]</a>, the underlying structure of the position embedding itself remains a human construct.

## The Bitter Lesson: Learning Over Engineering

Rich Sutton's "[[The Bitter Lesson]]" posits that attempts to "build knowledge into agents" (i.e., hand-engineer features or rules) eventually plateau and hinder progress. True breakthroughs come from "scaling computation by search and learning" <a class="yt-timestamp" data-t="01:24:07">[01:24:08]</a>. The speaker argues that the current state of [[positional_embeddings_in_transformers | position embeddings]] is "20 steps inside a rabbit hole that we don't need to get into" <a class="yt-timestamp" data-t="01:27:13">[01:27:13]</a>.

### Historical Precedent: Computer Vision

A parallel can be drawn from the history of computer vision:
*   **Past**: Early computer vision relied on "Gabber filters" – hand-designed convolutional filters used to detect features like vertical or horizontal edges in images <a class="yt-timestamp" data-t="01:24:37">[01:24:37]</a>. These filters were meticulously crafted by human engineers <a class="yt-timestamp" data-t="01:25:17">[01:25:17]</a>.
*   **Present**: With the advent of Convolutional Neural Networks (CNNs), these filters became "learned" <a class="yt-timestamp" data-t="01:25:30">[01:25:30]</a>. Instead of human design, the network itself, through backpropagation and large-scale computation, discovered the optimal filters for tasks like image classification <a class="yt-timestamp" data-t="01:25:45">[01:25:45]</a>. Ironically, some of these learned filters resembled the original Gabber filters, validating the human intuition but demonstrating the power of learning <a class="yt-timestamp" data-t="01:25:56">[01:25:56]</a>.

## The Prediction: Learnable Position Embeddings Will Prevail

The speaker predicts a similar evolution for [[positional_embeddings_in_transformers | position embeddings]]. While token embeddings are already learned <a class="yt-timestamp" data-t="01:27:35">[01:27:35]</a>, [[positional_embeddings_in_transformers | position embeddings]] remain largely hand-engineered. The expectation is that "eventually we're going to basically just learn these" <a class="yt-timestamp" data-t="01:35:40">[01:35:40]</a>, similar to how convolutional filters are learned in CNNs <a class="yt-timestamp" data-t="01:26:19">[01:26:19]</a>.

> [!NOTE] "Learned PEs are better" <a class="yt-timestamp" data-t="01:29:35">[01:29:35]</a>
> "The reason we're still using rope and long rope and all these things is because all these papers failed and learned position and codings just don't work quite as well as hand-designed position and coding but I think that's just a matter of scale" <a class="yt-timestamp" data-t="01:30:33">[01:30:33]</a>.

Previous attempts to learn [[positional_embeddings_in_transformers | position embeddings]] have been made (citing papers from 2017-2020) <a class="yt-timestamp" data-t="01:30:08">[01:30:08]</a>, but they haven't yet outperformed hand-designed methods. This is attributed to a current limitation in "scale" <a class="yt-timestamp" data-t="01:30:46">[01:30:46]</a>.

The ultimate goal is to move away from "this giant mess of [heuristics]" <a class="yt-timestamp" data-t="01:47:11">[01:47:11]</a> and instead allow models to discover the optimal position representations through compute and scale. This aligns with the principle that architectures with fewer inductive biases, like the Transformer itself, tend to be the most powerful <a class="yt-timestamp" data-t="01:55:27">[01:55:27]</a>.

## Implications and Speculation

The speaker speculates that Google's Gemini 1.5, known for its state-of-the-art context length <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>, might secretly be using such "learned [[positional_embeddings_in_transformers | position embeddings]]" <a class="yt-timestamp" data-t="01:48:16">[01:48:16]</a>. If so, it would validate the "bitter lesson" by demonstrating the power of learning over complex human engineering. Conversely, if Gemini's secret sauce is an "even more convoluted complicated version of Long Rope," it would be "kind of lame" <a class="yt-timestamp" data-t="01:48:20">[01:48:20]</a>, perpetuating the cycle of increasing heuristic complexity.

The development of increasingly longer context windows in models like Long Rope (up to 2048K tokens) <a class="yt-timestamp" data-t="01:13:15">[01:13:15]</a> also has implications for other areas, such as the relevance of Retrieval Augmented Generation (RAG). As context lengths increase, the need for external memory retrieval systems might diminish, as "we're just going to be capable of putting everything in the context" <a class="yt-timestamp" data-t="01:17:14">[01:17:16]</a>. However, the use of embedding vectors for database search would likely persist <a class="yt-timestamp" data-t="01:18:44">[01:18:44]</a>.

Ultimately, the speaker envisions a future where the complexities of hand-designed [[positional_embeddings_in_transformers | position embeddings]] are replaced by a simpler, learned approach, similar to how learned filters transformed computer vision <a class="yt-timestamp" data-t="01:28:13">[01:28:13]</a>.