---
title: Integration of LLMs with recommendation systems
videoId: 3k4a0PemMu4
---

From: [[aidotengineer]] <br/> 

The future of recommendation systems involves a significant merger with Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This integration builds on a history of language modeling techniques in recommendation systems, which began around 2013 with learning item embeddings from user interaction sequences <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Early methods, like GRU4, predicted the next item from short sequences <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The advent of transformers and attention mechanisms improved handling of long-range dependencies, allowing processing of hundreds or thousands of item IDs in user sequences <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Three key ideas are emerging for the future of this integration: [[semantic_ids | semantic IDs]], [[data_handling_and_preparing_training_datasets_for_llms | data augmentation]], and [[augmented_llm_architectures | unified models]] <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Semantic IDs

Traditional hash-based item IDs do not encode the content of an item, leading to cold-start problems for new items and sparsity issues for tail items with limited interactions <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This often results in recommendation systems being popularity-biased <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

The solution proposed is the use of [[semantic_ids | semantic IDs]], which can incorporate multimodal content <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### Kwai's Trainable Multimodal Semantic IDs
Kwai, a short-video platform, faced challenges learning from hundreds of millions of daily user-uploaded videos <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. They sought to combine static content embeddings with dynamic user behavior <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

Kwai's approach involves a standard two-tower network, with embedding layers for user and item IDs <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. What's new is the incorporation of content input:
*   Visual content is encoded using ResNet <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   Video descriptions use BERT <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   Audio is encoded with VGGish <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

These content embeddings are concatenated <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. The system then learns 1,000 cluster IDs (from 100 million videos) using K-means clustering <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. These trainable cluster IDs are mapped to their own embedding table <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. The model encoder learns to map the content space via these cluster IDs to the behavioral space <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

The outcomes were significant:
*   [[semantic_ids | Semantic IDs]] outperformed regular hash-based IDs on clicks and likes <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   Cold-start coverage (new videos shared) increased by 3.6% <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   Cold-start velocity (new videos reaching a view threshold) also increased substantially <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

The benefits of [[semantic_ids | semantic IDs]] include addressing cold-start issues and enabling recommendations that understand content <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. This allows for human-readable explanations of why a user might like a particular item, by blending LLMs with [[semantic_ids | semantic IDs]] <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.

## Data Augmentation
Machine learning relies on high-quality data at scale, especially for search and recommendation systems, which require extensive metadata for query expansion, synonyms, and spell checking <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>. This data collection is costly and high-effort, traditionally relying on human annotations or automatic methods <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. LLMs have proven outstanding at generating synthetic data and labels <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

### Indeed's Lightweight Classifier
Indeed faced the challenge of sending poor job recommendations via email, leading to user distrust and unsubscribes <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. Explicit feedback (thumbs up/down) was sparse, and implicit feedback was often imprecise <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

Their solution was a lightweight classifier to filter out bad recommendations <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>. Their journey to this solution was iterative:
1.  **Human Labeling**: Experts labeled job recommendations and user pairs based on resume and activity data <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
2.  **Open LLMs**: Prompting open LLMs like Mistral and Llama 2 yielded very poor performance due to their inability to focus on resume/job description details and generic outputs <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
3.  **GPT-4**: GPT-4 worked well with 90% precision and recall, but was too costly and slow (22 seconds) for practical use <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
4.  **GPT-3.5**: GPT-3.5 had very poor precision (63%), meaning 37% of "bad" recommendations it flagged were actually good, which was unacceptable <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
5.  **Fine-tuned GPT-2.5**: Fine-tuning GPT-2.5 achieved the desired precision (0.83) at a quarter of GPT-4's cost and latency, but was still too slow (6.7 seconds) for online filtering <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
6.  **Distilled Lightweight Classifier**: Finally, they distilled a lightweight classifier using the fine-tuned GPT-2.5 labels <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This classifier achieved high performance (0.86 AU ROC) and was fast enough for real-time filtering <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>.

The outcome was a 20% reduction in bad recommendations <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. Contrary to initial fears, this led to a 4% increase in application rate and a 5% decrease in unsubscribe rate, demonstrating that quality in recommendations makes a significant difference over mere quantity <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

### Spotify's Query Recommendation System
Spotify, known for music, introduced podcasts and audiobooks, facing a cold-start problem for these new content categories <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>. Exploratory search was crucial for expanding beyond music <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>.

The solution was a query recommendation system <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>. New queries were generated from catalog/playlist titles and search logs, and augmented with LLMs to generate natural language queries <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. This approach leverages conventional techniques and augments them with LLMs only where needed <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. These exploratory queries are then ranked alongside immediate search results <a class="yt-timestamp" data-t="00:14:34">[00:14:34]</a>.

This strategy led to a 9% increase in exploratory queries, meaning one-tenth of Spotify's users were exploring new products daily, significantly accelerating new product category growth <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

The benefits of [[data_handling_and_preparing_training_datasets_for_llms | LLM-augmented synthetic data]] include richer, high-quality data at scale, even for tail queries and items, at a significantly lower cost and effort compared to human adaptation <a class="yt-timestamp" data-t="00:15:34">[00:15:34]</a>.

## Unified Models
Traditional company setups often involve separate systems and bespoke models for ads, recommendations (homepage, item, cart, thank you page, etc.), and search <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This results in duplicative engineering pipelines, high maintenance costs, and limited knowledge transfer between models <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

The solution is [[augmented_llm_architectures | unified models]] (or foundation models), similar to how they've worked for vision and language tasks <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

### Netflix's Unified Contextual Ranker (Unicorn)
Netflix faced high operational costs and missed learning opportunities due to teams building bespoke models for search, similar item recommendations, and pre-query recommendations <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.

Their solution, Unicorn, is a [[augmented_llm_architectures | unified ranker]] <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. It uses a user foundation model and a context/relevance model <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. Unicorn takes unified input, allowing different use cases and features to use the same data schema <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. Input includes user ID, item ID, search query (if present), country, and task (e.g., search, pre-query, more like this) <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. Missing items are smartly imputed; for example, in item-to-item recommendations, the current item's title can be used as a search query <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.

This [[augmented_llm_architectures | unified model]] was able to match or exceed the metrics of specialized models across multiple tasks <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. This unification removes technical debt and builds a better foundation for future iterations, leading to faster development <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.

### Etsy's Unified Embeddings
Etsy aimed to help users find better results for both very specific and very broad queries, especially with its constantly changing inventory <a class="yt-timestamp" data-t="00:19:22">[00:19:22]</a>. Lexical embedding retrieval did not account for user preferences <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

Their solution was [[augmented_llm_architectures | unified embedding]] and retrieval <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>. Similar to the Kwai model, they use a product tower and a query encoder <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>. Product encoding uses T5 models for text embeddings (from item descriptions and query-product logs) <a class="yt-timestamp" data-t="00:20:21">[00:20:21]</a>. Both towers share encoders for text tokens, product category tokens, and user location, enabling embeddings to match users to product locations <a class="yt-timestamp" data-t="00:20:34">[00:20:34]</a>. User preferences (via query user scale effect features) are encoded for [[personalization_strategies_using_llms | personalization]] <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.

Their system architecture also included a "quality vector" (ratings, freshness, conversion rate) concatenated to the product embedding <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>. This quality vector was then mapped to the query vector to maintain dimension for dot product or cosine similarity <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>.

The results were impressive: a 2.6% increase in conversion across the entire site and over 5% increase in search purchases <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

### Netflix's Foundation Model for Personalization
Netflix has diverse recommendation needs across various content types (movies, TV shows, games, live streaming) and pages (homepage, search page, kids homepage, mobile feed) <a class="yt-timestamp" data-t="02:23:32">[02:23:32]</a>. Traditionally, this led to many specialized models developed independently, with duplicated efforts in feature and label engineering <a class="yt-timestamp" data-t="02:24:52">[02:24:52]</a>. This system was not scalable, offered little leverage, and hindered innovation velocity <a class="yt-timestamp" data-t="02:26:29">[02:26:29]</a>.

Netflix's "big bet" is to centralize user representation learning in one foundation model based on transformer architecture <a class="yt-timestamp" data-t="02:27:10">[02:27:10]</a>. Their hypotheses are:
1.  **Scalability**: Scaling up semi-supervised learning can improve [[personalization_strategies_using_llms | personalization]], similar to how scaling laws apply to LLMs <a class="yt-timestamp" data-t="02:27:36">[02:27:36]</a>.
2.  **High Leverage**: Integrating the foundation model into all systems can simultaneously improve all downstream models <a class="yt-timestamp" data-t="02:27:49">[02:27:49]</a>.

**Data and Training:**
*   **Data Cleaning and Tokenization**: Critical initial steps. Unlike LLMs with single language tokens, recommendation systems deal with rich "event interaction" tokens, each having multiple facets (when, where, what) <a class="yt-timestamp" data-t="02:28:38">[02:28:38]</a>. The granularity of tokenization and its trade-off with context window size are carefully considered <a class="yt-timestamp" data-t="02:29:42">[02:29:42]</a>.
*   **Model Layers**:
    *   **Event Representation**: Captures information about when, where (physical location, device, page), and what (target entity, interaction type, duration) an event happened <a class="yt-timestamp" data-t="02:30:31">[02:30:31]</a>.
    *   **Embedding Feature Transformation**: Combines ID embedding learning with [[semantic_ids | semantic content information]] to address cold-start problems, which are common in recommendations but not LLMs <a class="yt-timestamp" data-t="02:31:21">[02:31:21]</a>.
    *   **Transformer Layer**: Hidden state output is used as user representation <a class="yt-timestamp" data-t="02:32:07">[02:32:07]</a>. Considerations include representation stability, aggregation methods (across time or layers), and explicit adaptation for downstream objectives <a class="yt-timestamp" data-t="02:32:24">[02:32:24]</a>.
    *   **Objective/Loss Function**: Richer than LLMs, with multiple sequences to represent output. Targets can include entity IDs, action type, entity metadata (type, genre, language), or action details (duration, device, next play time) <a class="yt-timestamp" data-t="02:33:04">[02:33:04]</a>. These can be used for multi-task learning, or as weights/rewards/masks for loss functions <a class="yt-timestamp" data-t="02:34:01">[02:34:01]</a>.

Netflix observed that scaling laws apply to their foundation model, showing continuous gains over two and a half years, scaling up to a billion model parameters <a class="yt-timestamp" data-t="02:34:27">[02:34:27]</a>.

Learnings borrowed from LLMs include:
*   **Multi-token prediction**: Forces the model to be less myopic, more robust to serving time shifts, and targets long-term user satisfaction <a class="yt-timestamp" data-t="02:35:36">[02:35:36]</a>.
*   **Multi-layer representation**: Techniques like layer-wise supervision and multi-layer output aggregation lead to better and more stable user representations <a class="yt-timestamp" data-t="02:36:12">[02:36:12]</a>.
*   **Long context window handling**: Using truncated sliding windows, sparse attention, and progressively training longer sequences for efficient training <a class="yt-timestamp" data-t="02:36:34">[02:36:34]</a>.

**Serving and Applications:**
The foundation model consolidates the data and representation layers, particularly for user and content representations <a class="yt-timestamp" data-t="02:37:12">[02:37:12]</a>. Application models become thinner layers built on top of the foundation model <a class="yt-timestamp" data-t="02:37:28">[02:37:28]</a>.
The foundation model can be integrated in three ways:
1.  **Subgraph**: Integrated as a subgraph within the downstream model, replacing existing sequence transformer towers <a class="yt-timestamp" data-t="02:37:47">[02:37:47]</a>.
2.  **Pushed-out Embeddings**: Content and member embeddings can be pushed to a centralized store, allowing wider use cases beyond [[personalization_strategies_using_llms | personalization]] <a class="yt-timestamp" data-t="02:38:15">[02:38:15]</a>.
3.  **Fine-tuning/Distillation**: Models can be extracted and fine-tuned or distilled for specific applications to meet online serving requirements <a class="yt-timestamp" data-t="02:38:53">[02:38:53]</a>.

Netflix has seen high leverage, with many applications incorporating the foundation model and showing AB test wins, alongside infrastructure consolidation <a class="yt-timestamp" data-t="02:39:12">[02:39:12]</a>. This has validated their big bets, proving the solution is scalable and provides high leverage and faster innovation velocity <a class="yt-timestamp" data-t="02:39:46">[02:39:46]</a>.

Future directions include:
*   **Universal representation for heterogeneous entities**: Further developing [[semantic_ids | semantic IDs]] as Netflix expands content types <a class="yt-timestamp" data-t="02:40:23">[02:40:23]</a>.
*   **Generative retrieval for collection recommendation**: Generating collections of recommendations, where business rules or diversity can be handled during multi-step decoding <a class="yt-timestamp" data-t="02:40:40">[02:40:40]</a>.
*   **Faster adaptation through prompt tuning**: Training soft tokens to prompt the foundation model to behave differently at inference time <a class="yt-timestamp" data-t="02:40:59">[02:40:59]</a>.

### Pinterest's LLM Integration for Search Relevance
Pinterest handles over six billion searches per month across billions of pins, supporting over 45 languages <a class="yt-timestamp" data-t="02:29:02">[02:29:02]</a>. Their search backend involves query understanding, retrieval, re-ranking, and blending <a class="yt-timestamp" data-t="02:29:42">[02:29:42]</a>. They focused on semantic relevance modeling in the re-ranking stage <a class="yt-timestamp" data-t="02:30:02">[02:30:02]</a>.

Their search relevance model is a classification model predicting the relevance of a pin to a search query on a five-point scale <a class="yt-timestamp" data-t="02:30:18">[02:30:18]</a>.
*   **Model Architecture**: Query and pin text are concatenated and passed into an LLM using a cross-encoder structure to capture interaction <a class="yt-timestamp" data-t="02:31:11">[02:31:11]</a>. The LLM embedding feeds into an MLP layer to produce a five-dimensional vector for relevance levels <a class="yt-timestamp" data-t="02:31:30">[02:31:30]</a>. Open-source LLMs are fine-tuned with Pinterest internal data <a class="yt-timestamp" data-t="02:31:42">[02:31:42]</a>.
*   **LLM Effectiveness**: LLMs substantially improved relevance prediction compared to Pinterest's in-house content and query embedding baseline <a class="yt-timestamp" data-t="02:31:58">[02:31:58]</a>. Using more advanced LLMs and increasing model size continued to improve performance, with an 8-billion parameter LLM showing 20% improvement over the search stage embedding model <a class="yt-timestamp" data-t="02:32:20">[02:32:20]</a>.
*   **Useful Annotations**: Vision-language model generated captions and user actions (e.g., user-curated boards, queries leading to pins) are useful content annotations <a class="yt-timestamp" data-t="02:32:50">[02:32:50]</a>.
*   **Efficiency for Serving**: Achieving low latency (e.g., 500-400ms) for serving LLMs requires efficiency <a class="yt-timestamp" data-t="02:33:23">[02:33:23]</a>. Three levers:
    1.  **Smaller Models**: Going "big and then small" by distilling larger models (e.g., 150B parameters) step-by-step into smaller ones (8B, 3B, 1B) maintains reasoning power and improves throughput <a class="yt-timestamp" data-t="02:33:55">[02:33:55]</a>.
    2.  **Pruning**: Gradual pruning of redundant layers or reducing precision in transformers is more effective than aggressive pruning, which can significantly reduce model quality <a class="yt-timestamp" data-t="02:34:45">[02:34:45]</a>.
    3.  **Quantization**: Using lower precision (e.g., FP8) for activations and parameters. Mixed precision is important, with the LLM head (prediction output) needing FP32 to maintain precision and calibration <a class="yt-timestamp" data-t="02:36:03">[02:36:03]</a>.
    4.  **Sparsification**: Specifying attention scores so not every item attends to every other item, especially when recommending multiple items simultaneously <a class="yt-timestamp" data-t="02:36:53">[02:36:53]</a>.

By combining these techniques, Pinterest achieved a 7x reduction in latency and a 30x increase in throughput (queries per GPU) <a class="yt-timestamp" data-t="02:37:37">[02:37:37]</a>.

### Instacart's LLMs for Search and Discovery
Instacart focuses on online grocery, where customers have long shopping lists, mostly restocking purchases <a class="yt-timestamp" data-t="02:46:40">[02:46:40]</a>. Search plays a dual role: enabling quick, efficient finding of known products and facilitating new product discovery <a class="yt-timestamp" data-t="02:47:07">[02:47:07]</a>. New product discovery benefits customers (new items), advertisers (showcasing products), and the platform (larger basket sizes) <a class="yt-timestamp" data-t="02:47:17">[02:47:17]</a>.

**Challenges with Conventional Search Engines:**
1.  **Overly Broad Queries**: E.g., "snacks" results in tons of products <a class="yt-timestamp" data-t="02:47:48">[02:47:48]</a>. Engagement data is hard to collect for unexposed items, leading to a cold-start problem <a class="yt-timestamp" data-t="02:47:57">[02:47:57]</a>.
2.  **Very Specific Queries**: E.g., "unsweetened plant-based yogurt" are infrequent, lacking sufficient engagement data <a class="yt-timestamp" data-t="02:48:12">[02:48:12]</a>.
3.  **New Item Discovery**: Users desire an experience similar to physical stores (seeing related items) <a class="yt-timestamp" data-t="02:48:43">[02:48:43]</a>. Conventional methods struggled with precision due to lack of engagement data <a class="yt-timestamp" data-t="02:49:25">[02:49:25]</a>.

**Leveraging LLMs:**
Instacart used LLMs to uplevel their query understanding module, which is the most upstream part of the search stack <a class="yt-timestamp" data-t="02:49:37">[02:49:37]</a>.

1.  **Query to Product Category Classifier**: Maps a query to categories in their 10,000-label taxonomy <a class="yt-timestamp" data-t="02:50:16">[02:50:16]</a>.
    *   **Previous Approach**: FastText-based neural network for semantic relationships, with NPMI for statistical co-occurrence. Low coverage for tail queries due to lack of engagement data <a class="yt-timestamp" data-t="02:50:46">[02:50:46]</a>. BERT-based models showed limited improvement for increased latency <a class="yt-timestamp" data-t="02:51:22">[02:51:22]</a>.
    *   **LLM Approach**: Initially, LLMs were prompted with queries and taxonomy to predict relevant categories. While output seemed decent, online AB tests showed poor results. LLMs lacked Instacart's domain understanding (e.g., "protein" meaning supplements to users, but chicken/tofu to LLM) <a class="yt-timestamp" data-t="02:51:36">[02:51:36]</a>.
    *   **Augmented LLM Prompt**: The problem was rephrased by providing the LLM with top-converting categories for each query as additional context <a class="yt-timestamp" data-t="02:52:30">[02:52:30]</a>. This greatly simplified the problem for the LLM, leading to precise results (e.g., "Wernner soda" as "ginger ale") <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.
    *   **Results**: For tail queries, precision improved by 18 percentage points and recall by 70 percentage points <a class="yt-timestamp" data-t="02:53:26">[02:53:26]</a>. The prompt is very simple, passing converted categories and guidelines <a class="yt-timestamp" data-t="02:53:42">[02:53:42]</a>.

2.  **Query Rewrites Model**: Important for e-commerce where catalog variations mean queries may not always return results <a class="yt-timestamp" data-t="02:54:08">[02:54:08]</a>. Rewrites like "1% milk" to "milk" ensure results <a class="yt-timestamp" data-t="02:54:27">[02:54:27]</a>.
    *   **Previous Approach**: Engagement data-trained models performed poorly on tail queries <a class="yt-timestamp" data-t="02:54:37">[02:54:37]</a>.
    *   **LLM Approach**: Similar to category classification, LLMs generated precise rewrites (substitute, broad, synonymous) <a class="yt-timestamp" data-t="02:54:49">[02:54:49]</a>.
    *   **Results**: Offline improvements based on human evaluation, and online, a large drop in queries with no results, which was significant for the business <a class="yt-timestamp" data-t="02:55:16">[02:55:16]</a>.

**Scoring and Serving:**
Instacart's query pattern has a fat head/torso and a long tail <a class="yt-timestamp" data-t="02:56:06">[02:56:06]</a>. They precomputed outputs for head/torso queries offline in batch mode and cached them <a class="yt-timestamp" data-t="02:56:18">[02:56:18]</a>. Online queries are served from the cache with low latency. For the long tail, they fall back to existing models, planning to replace them with a distilled LLM <a class="yt-timestamp" data-t="02:56:37">[02:56:37]</a>.

**Discovery-Oriented Content:**
LLMs were used to show more discovery content in search results:
*   For queries with no exact results, LLMs generated substitute results (e.g., other seafood for "swordfish") <a class="yt-timestamp" data-t="02:59:17">[02:59:17]</a>.
*   For queries with many exact results, complementary items were shown (e.g., Asian cooking ingredients for "sushi") <a class="yt-timestamp" data-t="02:59:31">[02:59:31]</a>.
Both led to improved engagement and revenue <a class="yt-timestamp" data-t="02:59:51">[02:59:51]</a>.

**Requirements for Content Generation:**
1.  **Incremental Content**: Avoid duplicates of already shown results <a class="yt-timestamp" data-t="03:00:07">[03:00:07]</a>.
2.  **Domain Alignment**: LLM answers must align with Instacart's domain knowledge (e.g., "dishes" meaning cookware, not food, unless "Thanksgiving dishes" is queried) <a class="yt-timestamp" data-t="03:00:12">[03:00:12]</a>.

**Addressing Challenges:**
*   **Initial LLM Generation**: Basic prompts produced common-sense answers but didn't align with user behavior on Instacart (e.g., "protein" again) <a class="yt-timestamp" data-t="03:00:36">[03:00:36]</a>.
*   **Augmented Prompt**: Instacart's domain knowledge (top converting categories, query annotations like brand/dietary attributes, subsequent user queries) was added to the prompt <a class="yt-timestamp" data-t="03:01:40">[03:01:40]</a>. This yielded much better results, leading to significant engagement and revenue improvements <a class="yt-timestamp" data-t="03:02:16">[03:02:16]</a>.
*   **Serving**: Similar to query understanding, LLMs were called in batch mode on historical search logs, storing query content and potential products <a class="yt-timestamp" data-t="03:02:29">[03:02:29]</a>. Online serving is a quick lookup from a feature store <a class="yt-timestamp" data-t="03:02:51">[03:02:51]</a>.
*   **Key Challenges Solved**:
    1.  **Aligning generation with business metrics**: Iterating prompts and metadata to achieve topline wins <a class="yt-timestamp" data-t="03:03:12">[03:03:12]</a>.
    2.  **Improving ranking**: Traditional PCTR/PCBR models didn't work, requiring strategies like diversity-based re-ranking <a class="yt-timestamp" data-t="03:03:28">[03:03:28]</a>.
    3.  [[evaluation_of_llms_using_realworld_scenarios | **Evaluating content**]]: Ensuring LLM outputs are accurate, not hallucinating, and adhere to product needs, often using LLM as a judge <a class="yt-timestamp" data-t="03:04:19">[03:04:19]</a>.

**Key Takeaways**:
*   LLM's world knowledge improved query understanding predictions for tail queries <a class="yt-timestamp" data-t="03:04:02">[03:04:02]</a>.
*   Success came from combining Instacart's domain knowledge with LLMs <a class="yt-timestamp" data-t="03:04:11">[03:04:11]</a>.
*   [[evaluation_of_llms_using_realworld_scenarios | Evaluating content]] and query predictions was critical and more difficult than anticipated <a class="yt-timestamp" data-t="03:04:21">[03:04:21]</a>.
*   Consolidating multiple query understanding models into a single LLM could improve consistency <a class="yt-timestamp" data-t="02:57:21">[02:57:21]</a>.
*   LLMs for query understanding allow passing extra context to understand customer intent (e.g., recipe ingredients) <a class="yt-timestamp" data-t="02:58:13">[02:58:13]</a>.

### YouTube's Large Recommender Model (LRM) with Gemini
YouTube, one of the largest consumer apps, has most of its watch time driven by its recommendation system across home, watch next, shorts, and personalized search results <a class="yt-timestamp" data-t="03:09:01">[03:09:01]</a>. The recommendation problem involves learning a function to provide recommendations based on user and context input (demographics, watch history, engagement, subscriptions) <a class="yt-timestamp" data-t="03:09:44">[03:09:44]</a>.

YouTube aimed to rethink its recommendation system on top of Gemini, leading to the Large Recommender Model (LRM) <a class="yt-timestamp" data-t="03:10:26">[03:10:26]</a>.
*   **Adaptation**: LRM starts with a base Gemini checkpoint, adapted for YouTube recommendations by teaching it YouTube-specific information <a class="yt-timestamp" data-t="03:11:32">[03:11:32]</a>. This unified, YouTube-specific Gemini checkpoint (LRM) is then aligned for tasks like retrieval and ranking, creating custom versions for major recommendation surfaces <a class="yt-timestamp" data-t="03:11:46">[03:11:46]</a>.
*   **Tokenizing Videos (Semantic IDs)**: The first step was to tokenize videos so the LLM could take video tokens as input and output video tokens as recommendations <a class="yt-timestamp" data-t="03:12:24">[03:12:24]</a>. Given the need to reason over many videos with up to a million tokens of context, video representation had to be compressed <a class="yt-timestamp" data-t="03:12:52">[03:12:52]</a>.
    *   They built [[semantic_ids | semantic ID]] by extracting features (title, description, transcript, audio, video frames) into a multi-dimensional embedding <a class="yt-timestamp" data-t="03:13:14">[03:13:14]</a>. This embedding is quantized using RQVE to give each video a token <a class="yt-timestamp" data-t="03:13:36">[03:13:36]</a>.
    *   This creates an atomic unit for a new language of YouTube videos, organizing billions of videos around semantically meaningful tokens (e.g., music, gaming, sports, specific sports) <a class="yt-timestamp" data-t="03:13:47">[03:13:47]</a>. This was a milestone in moving from hash-based to semantically meaningful tokenization <a class="yt-timestamp" data-t="03:14:23">[03:14:23]</a>.
*   **Continued Pre-training**: LRM is trained to understand both English and this new YouTube language in two steps:
    1.  **Linking Text and SID**: Teaching the model to connect text (e.g., video title, creator, topics) with video tokens (SID) <a class="yt-timestamp" data-t="03:14:48">[03:14:48]</a>.
    2.  **Understanding Watch Sequences**: Using YouTube engagement data (user watch paths), the model learns to predict masked videos in a sequence, understanding relationships between videos based on user engagement <a class="yt-timestamp" data-t="03:15:26">[03:15:26]</a>.

After pre-training, the model can reason across English and YouTube videos. For example, given a sequence of videos, it can infer shared topics like sports or technology based on their [[semantic_ids | semantic ID]] <a class="yt-timestamp" data-t="03:16:07">[03:16:07]</a>.

*   **Generative Retrieval**: LRM is used for generative retrieval by constructing personalized prompts for each user, including demographics, context video, and watch history <a class="yt-timestamp" data-t="03:17:03">[03:17:03]</a>. The model then decodes video recommendations as SIDs <a class="yt-timestamp" data-t="03:17:37">[03:17:37]</a>. This yields unique recommendations, especially for hard recommendation tasks (e.g., finding related women's track races based on a user's Olympic highlight watch history) <a class="yt-timestamp" data-t="03:17:41">[03:17:41]</a>.
*   **Serving Costs**: LRM is powerful and learns quickly but is expensive to serve. YouTube achieved over 95% cost savings to launch it in production <a class="yt-timestamp" data-t="03:18:36">[03:18:36]</a>.
*   **Offline Recommendation Table**: They also created an offline recommendation table by removing personalized aspects from the prompt, allowing for simple lookup serving for "watch next" type recommendations <a class="yt-timestamp" data-t="03:19:10">[03:19:10]</a>.
*   **Challenges for YouTube Recommendations**:
    1.  **Vocabulary and Corpus Size**: YouTube's billions of videos (millions added daily) dwarf LLM text vocabularies <a class="yt-timestamp" data-t="03:20:23">[03:20:23]</a>.
    2.  **Freshness**: New videos (e.g., Taylor Swift music video) must be recommended within minutes or hours, requiring continuous pre-training on the order of days/hours, unlike classical LLM pre-training (months) <a class="yt-timestamp" data-t="03:20:51">[03:20:51]</a>.
    3.  **Scale**: Serving models to billions of daily active users necessitates focusing on smaller, more efficient models (like Gemini Flash or smaller checkpoints) to meet latency and scale requirements <a class="yt-timestamp" data-t="03:21:52">[03:21:52]</a>.

The benefits of [[augmented_llm_architectures | unified models]] include system simplification, where improvements to one part of the model transfer to other use cases, leading to faster iteration <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>. However, there can be "alignment types" where improving one task might worsen another, potentially requiring splitting into multiple unified models <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

## Recipe for LLM-Based Recommendation Systems

A general recipe for building LLM-based recommendation systems involves three major steps <a class="yt-timestamp" data-t="03:22:28">[03:22:28]</a>:
1.  **Tokenize Your Content**:
    *   **Goal**: Create an atomic token representation of your content.
    *   **Method**: Build rich representations from features, create embeddings, and then tokenize or quantize them.
    *   **Outcome**: A domain-specific language for your content <a class="yt-timestamp" data-t="03:22:50">[03:22:50]</a>.

2.  **Adapt the LLM**:
    *   **Goal**: Link the LLM's natural language understanding with your new domain language.
    *   **Method**: Find training tasks that enable the LLM to reason across both English and your domain-specific tokens.
    *   **Outcome**: A bilingual LLM that understands both natural language and your domain language <a class="yt-timestamp" data-t="03:22:56">[03:22:56]</a>.

3.  **Prompt with User Information**:
    *   **Goal**: Create a generative recommendation system.
    *   **Method**: Construct personalized prompts using user demographics, activity, and actions. Train task-specific or surface-specific models.
    *   **Outcome**: An LLM-powered system capable of generating recommendations <a class="yt-timestamp" data-t="03:23:21">[03:23:21]</a>.

## Future Directions
Currently, LLMs primarily augment recommendation systems, enhancing quality invisibly to users <a class="yt-timestamp" data-t="03:23:56">[03:23:56]</a>. However, the future holds more interactive experiences:
*   Users will be able to communicate with the recommender in natural language to steer recommendations towards their goals <a class="yt-timestamp" data-t="03:24:28">[03:24:28]</a>.
*   The recommender will be able to explain *why* a candidate was recommended <a class="yt-timestamp" data-t="03:24:42">[03:24:42]</a>.
*   The lines between search and recommendation will blur <a class="yt-timestamp" data-t="03:24:52">[03:24:52]</a>.
*   Eventually, recommendations may evolve into generative content, creating personalized versions of content or even entirely new content tailored for the user <a class="yt-timestamp" data-t="03:25:01">[03:25:01]</a>.