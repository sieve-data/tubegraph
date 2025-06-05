---
title: Cold start problem in recommendation systems
videoId: 3k4a0PemMu4
---

From: [[aidotengineer]] <br/> 

The "cold start problem" in recommendation systems refers to the challenge of making accurate recommendations for new users or new items that have little to no interaction data <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. This issue also applies to "tail items"—products or content with very few interactions—making it difficult for systems to learn and recommend them effectively <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>. Recommendation systems often exhibit a popularity bias, struggling with new items and data sparsity <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## Challenges Posed by Cold Start <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>

When a new item is introduced, the system must "relearn" everything about it <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. This lack of initial interaction data leads to:
*   **Data Sparsity**: Many items, especially those in the "long tail," have few or no user interactions, making it insufficient for traditional models to learn from <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Popularity Bias**: Recommendation systems tend to favor popular items due to abundant interaction data, further exacerbating the visibility problem for new or niche content <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
*   **Poor User Experience**: For platforms like Indeed, bad job recommendations for new users can lead to a loss of trust and unsubscribes, which are very difficult to recover from <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Limited Discovery**: Users struggle to find new or specific items, as seen with overly broad or highly specific queries on platforms like Instacart <a class="yt-timestamp" data-t="02:47:48">[02:47:48]</a>.

## Addressing Cold Start with AI <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>

Several advanced techniques, often leveraging large language models (LLMs), are being developed and applied to mitigate the cold start problem.

### 1. Semantic IDs <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>

Unlike hash-based item IDs that do not encode an item's content <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>, semantic IDs incorporate the item's inherent content, potentially even multimodal content (e.g., visual, audio, text) <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This allows recommendations to understand content directly <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.

**Case Study: Quao (Kuaishou)**
Quao, a short video platform, faces the challenge of users uploading hundreds of millions of new short videos daily, making it hard to learn from them <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. Their solution uses trainable multimodal semantic IDs <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Process**: They encode visual content with ResNet, video descriptions with BERT, and audio with VGGish <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. These content embeddings are concatenated <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. K-means clustering is applied to learn 1,000 cluster IDs from 100 million videos, which are then mapped to an embedding table <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. A model encoder learns to map the content space to the behavioral space via these trainable cluster IDs <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
*   **Outcome**: Semantic IDs not only outperform hash-based IDs on clicks and likes but significantly increase "cold-start coverage" (new videos shared) by 3.6% and "cold-start velocity" (new videos hitting view thresholds) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

**Case Study: YouTube**
YouTube uses [[semantic_ids | semantic IDs]] to tokenize videos, representing rich multimodal features as tokens <a class="yt-timestamp" data-t="03:06:52">[03:06:52]</a>.
*   **Process**: Video features like title, description, transcript, audio, and video frame data are extracted into a multi-dimensional embedding, then quantized into tokens <a class="yt-timestamp" data-t="03:13:21">[03:13:21]</a>. This creates a "new language of YouTube videos" where billions of videos are organized by these semantically meaningful tokens <a class="yt-timestamp" data-t="03:13:48">[03:13:48]</a>.
*   **Benefit**: This approach helps address the extreme freshness requirements of YouTube, where new videos (like a Taylor Swift music video) need to be recommended within minutes or hours <a class="yt-timestamp" data-t="03:21:14">[03:21:14]</a>. The model can be continuously pre-trained on the order of days and hours to keep up with new content <a class="yt-timestamp" data-t="03:21:38">[03:21:38]</a>.

### 2. Data Augmentation <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>

LLMs are highly effective for generating synthetic data and labels, which is crucial for search and recommendation systems that require vast amounts of high-quality metadata <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>. This is far more cost-effective than human annotation <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

**Case Study: Indeed**
Indeed struggled with bad job recommendations leading to user unsubscribes <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Explicit feedback (thumbs up/down) was sparse, and implicit feedback was imprecise <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Process**: They used LLMs to generate labels for a lightweight classifier <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. Initial attempts with open LLMs (Mistral, Llama 2) were poor <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. GPT-4 performed well but was too costly and slow <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. Fine-tuning GPT-2.5 on GPT-4 generated labels allowed them to achieve desired precision at a lower cost and latency <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>. This distilled classifier achieved high performance for real-time filtering <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.
*   **Outcome**: Reducing bad recommendations by 20% led to a 4% increase in application rate and a 5% decrease in unsubscribe rate <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>. This demonstrated that quality, not just quantity, significantly impacts recommendations <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

**Case Study: Spotify**
Spotify aimed to grow new content categories like podcasts and audiobooks, facing a cold start problem not just for items but for entire categories <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
*   **Process**: They leveraged LLMs to generate natural language queries to facilitate exploratory search <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. These LLM-generated queries augmented existing query generation techniques (e.g., extracting from catalog titles, search logs) <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. The new queries were ranked and displayed to users, informing them of new categories without explicit banners <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
*   **Outcome**: This led to a 9% increase in exploratory queries, meaning one-tenth of their users were now exploring new products daily, accelerating new product category growth <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

**Case Study: Instacart**
Instacart used LLMs to improve query understanding, addressing challenges with overly broad or specific queries and enabling new item discovery <a class="yt-timestamp" data-t="02:47:41">[02:47:41]</a>.
*   **Process**: For query-to-category classification, initial LLM prompts were decent but lacked Instacart user behavior context <a class="yt-timestamp" data-t="02:52:16">[02:52:16]</a>. By augmenting prompts with Instacart domain knowledge (e.g., top converting categories, user annotations), LLMs generated much more precise results, such as identifying "Wernner soda" as ginger ale instead of generic fruit-flavored soda <a class="yt-timestamp" data-t="02:53:02">[02:53:02]</a>. For query rewrites, LLMs generated precise substitutes, broader terms, and synonyms <a class="yt-timestamp" data-t="02:54:51">[02:54:51]</a>.
*   **Outcome**: Precision for tail queries improved by 18 percentage points and recall by 70 percentage points <a class="yt-timestamp" data-t="02:53:31">[02:53:31]</a>. This significantly reduced the number of "no results" queries, benefiting the business <a class="yt-timestamp" data-t="02:55:43">[02:55:43]</a>. For discovery, LLMs generated substitute and complementary items, leading to engagement and revenue improvement <a class="yt-timestamp" data-t="02:59:53">[02:59:53]</a>.

### 3. Unified Models / Foundation Models <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>

Traditionally, companies have separate models for ads, recommendations, and search, often with multiple bespoke models even within recommendations <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. Unified models consolidate these systems, reducing duplication, maintenance costs, and allowing improvements to transfer across use cases <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

**Case Study: Netflix**
Netflix, with its diverse recommendation needs across different content types and pages, traditionally had many specialized models <a class="yt-timestamp" data-t="02:24:52">[02:24:52]</a>. This led to duplication in feature and label engineering <a class="yt-timestamp" data-t="02:25:28">[02:25:28]</a>.
*   **Solution**: Netflix adopted a "big bet" on a foundation model (Unicorn) based on transformer architecture for personalization <a class="yt-timestamp" data-t="02:23:08">[02:23:08]</a>. This model learns a centralized user representation, combining ID embedding with semantic content information to handle cold start items that the model hasn't seen during training <a class="yt-timestamp" data-t="02:31:28">[02:31:28]</a>. The model supports various tasks like search, similar item, and pre-query recommendations using a unified input schema <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.
*   **Outcome**: The unified model matched or exceeded the metrics of specialized models on multiple tasks <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. This approach is scalable and provides high leverage, accelerating innovation velocity by allowing new applications to directly fine-tune the foundation model <a class="yt-timestamp" data-t="02:39:47">[02:39:47]</a>.

**Case Study: Etsy**
Etsy sought to improve results for specific or broad queries given its constantly changing inventory <a class="yt-timestamp" data-t="02:24:32">[02:24:32]</a>.
*   **Solution**: They developed a unified embedding and retrieval system <a class="yt-timestamp" data-t="02:00:03">[02:00:03]</a>. It uses a two-tower model: a product encoder (T5 models for text embeddings, query-product logs) and a query encoder (search query encoder) <a class="yt-timestamp" data-t="02:19:50">[02:19:50]</a>. Both share encoders for text tokens, product category, and user location, allowing embeddings to match users to product locations <a class="yt-timestamp" data-t="02:42:07">[02:42:07]</a>. A "quality vector" (ratings, freshness, conversion rate) is concatenated to product embeddings to ensure good quality results <a class="yt-timestamp" data-t="02:21:18">[02:21:18]</a>.
*   **Outcome**: A 2.6% increase in conversion across the entire site and over 5% increase in search purchases <a class="yt-timestamp" data-t="02:21:52">[02:21:52]</a>. This highlights how unified models simplify systems and improve performance across various use cases <a class="yt-timestamp" data-t="02:22:12">[02:22:12]</a>.

## The LLM-Based Recommendation Recipe <a class="yt-timestamp" data-t="03:08:50">[03:08:50]</a>

A general recipe for building an LLM-based recommendation system includes three main steps:
1.  **Tokenize Content**: Develop a method to tokenize your content into atomic tokens, essentially creating a domain-specific language (e.g., [[semantic_ids | semantic IDs]] for videos) <a class="yt-timestamp" data-t="03:22:30">[03:22:30]</a>.
2.  **Adapt the LLM**: Continuously pre-train a base LLM to understand both natural language and your new domain language, creating a "bilingual" LLM <a class="yt-timestamp" data-t="03:22:57">[03:22:57]</a>. This involves linking text to content tokens and teaching the model to reason about sequences of user interactions <a class="yt-timestamp" data-t="03:14:48">[03:14:48]</a>.
3.  **Prompt with User Information**: Construct personalized prompts with user demographics, activity, and actions to train task-specific models, resulting in a generative recommendation system <a class="yt-timestamp" data-t="03:23:21">[03:23:21]</a>.

The future of LLM-based recommendations suggests a move towards user-steerable systems, where users can interact with the recommender in natural language, receive explanations for recommendations, and align results with their personal goals <a class="yt-timestamp" data-t="03:24:31">[03:24:31]</a>.