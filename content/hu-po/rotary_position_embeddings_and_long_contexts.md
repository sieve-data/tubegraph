---
title: Rotary Position Embeddings and Long Contexts
videoId: Y0gYsq7tOnM
---

From: [[hu-po]] <br/> 

Rotary Position Embeddings (RoPE) are a type of [[positional_embeddings_in_transformers | positional embedding]] used in Transformer models to encode the position of tokens within a sequence <a class="yt-timestamp" data-t="02:50:02">[02:50:02]</a>. They provide the model with additional information for each token, indicating its relative position within the overall text sequence <a class="yt-timestamp" data-t="02:50:12">[02:50:12]</a>. RoPE is currently a popular choice for positional embeddings <a class="yt-timestamp" data-t="02:50:39">[02:50:39]</a>.

## How RoPE Works

RoPE functions by rotating the vectors that represent tokens in a high-dimensional space <a class="yt-timestamp" data-t="02:51:01">[02:51:01]</a>. When dot products are performed between query and key vectors in a Transformer's self-attention mechanism, RoPE ensures that the relative angle between these vectors remains consistent, regardless of their absolute position in the sequence <a class="yt-timestamp" data-t="02:51:48">[02:51:48]</a>. This is achieved by rotating both the query and key vectors <a class="yt-timestamp" data-t="02:51:49">[02:51:49]</a>.

An intuitive way to visualize RoPE is to imagine it creating a spiral where each token's position embedding corresponds to a point along this spiral <a class="yt-timestamp" data-t="02:51:27">[02:51:27]</a>.

## RoPE and Long Contexts in Code Llama

A significant challenge in Transformer-based language modeling is effectively handling [[the_significance_of_longcontext_processing_in_ai_models | long input sequences]] <a class="yt-timestamp" data-t="03:04:16">[03:04:16]</a>. Key challenges include:
*   **Extrapolation**: Operating on sequence lengths beyond those seen during training <a class="yt-timestamp" data-t="03:04:32">[03:04:32]</a>.
*   **Quadratic Complexity**: The attention mechanism in Transformers has a quadratic complexity, meaning memory requirements increase quadratically with sequence length <a class="yt-timestamp" data-t="03:05:03">[03:05:03]</a>.

Code Llama addressed these challenges by modifying the parameters of the RoPE [[positional_embeddings_in_transformers | positional embeddings]] <a class="yt-timestamp" data-t="02:59:01">[02:59:01]</a>. Specifically, they extended the maximum context length from 4,000 tokens (used in Llama 2) to 100,000 tokens <a class="yt-timestamp" data-t="02:58:59">[02:58:59]</a>. This was done by increasing the base period of the `theta` parameter in the RoPE calculations from 10,000 to 1 million <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

### Training Strategy for Long Contexts

Code Llama's approach involved a specialized "long context fine-tuning" stage <a class="yt-timestamp" data-t="02:57:14">[02:57:14]</a>. By limiting the training time spent on processing long sequences to this fine-tuning stage, they were able to gain long-range capabilities without significantly increasing the overall training cost <a class="yt-timestamp" data-t="02:57:30">[02:57:30]</a>. This strategy is similar to position interpolation methods <a class="yt-timestamp" data-t="02:57:55">[02:57:55]</a>. The modification of the `theta` parameter allowed for processing much longer sequences and reduced bias towards short-distance attention <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

Experiments showed that Code Llama models were not only effective with the increased sequence length during fine-tuning but also exhibited extrapolation capabilities and stable behavior on very long sequences, up to 100,000 tokens <a class="yt-timestamp" data-t="03:01:10">[03:01:10]</a>. While long context fine-tuning could potentially hurt short context results, Code Llama demonstrated that it did not significantly degrade performance on standard, shorter code generation benchmarks <a class="yt-timestamp" data-t="03:02:45">[03:02:45]</a>.

## Limitations of Positional Encoding

While effective, the current positional encodings are largely based on the sequential order of words in a text <a class="yt-timestamp" data-t="03:53:46">[03:53:46]</a>. However, for code, the order of functions within a file often doesn't affect functionality <a class="yt-timestamp" data-t="03:54:06">[03:54:06]</a>. Future improvements in [[positional_embeddings_in_transformers | positional embeddings]] could incorporate more nuanced information, such as Abstract Syntax Trees (ASTs), to better reflect the non-linear structure of code <a class="yt-timestamp" data-t="03:53:34">[03:53:34]</a>.