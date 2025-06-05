---
title: AIgenerated recommendations and user experience
videoId: 3k4a0PemMu4
---

From: [[aidotengineer]] <br/> 

The integration of artificial intelligence (AI) and recommendation systems is evolving, with a focus on enhancing the [[the_role_of_user_experience_in_ai | user experience]] and addressing long-standing challenges in personalized content delivery <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This field has seen significant advancements, particularly with the advent of large language models (LLMs) and transformer-based architectures <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## Evolution of AI in Recommendation Systems
Language modeling techniques have been applied to recommendation systems since 2013, initially focusing on learning item embeddings from co-occurrences in user interaction sequences <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Early methods, like GRU4 (Gated Recurrent Units), predicted the next item from short sequences <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The introduction of transformers and attention mechanisms improved handling of long-range dependencies, allowing models to process hundreds to thousands of items in a user sequence <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

Current trends in improving recommendation systems with AI focus on three key ideas:
1.  **Semantic IDs** <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>
2.  **[[data_augmentation_and_efficiency_in_recommendation_systems | Data Augmentation]]** <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>
3.  **[[unified_models_for_recommendation_systems | Unified Models]]** <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>

## Addressing Challenges in Recommendation Systems

### Semantic IDs
Traditional hash-based item IDs do not encode the content of the item, leading to the "cold-start problem" for new items and sparsity issues for long-tail items with few interactions <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This causes recommendation systems to be popularity-biased <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

**Solution: Multimodal Semantic IDs**
Semantic IDs, potentially involving multimodal content, offer a solution by encoding the item's content <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

**Example: Kuaishou (Kuaishou)**
Kuaishou, a short video platform in China, faced challenges learning from hundreds of millions of daily video uploads <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. They developed a trainable multimodal semantic ID system <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Architecture**: A two-tower network where content input is integrated <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **Content Encoding**: ResNet for visual <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>, BERT for video descriptions <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>, and VGGish for audio <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.
*   **Trainable Embeddings**: Content embeddings are concatenated, and K-means clustering is used to learn a fixed number of cluster IDs (e.g., 1,000 for 100 million videos) <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. These cluster IDs are trainable and map the content space to the behavioral space <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.
*   **Results**: Semantic IDs not only outperformed hash-based IDs on clicks and likes <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>, but also increased cold-start coverage by 3.6% and cold-start velocity significantly <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

**Benefits of Semantic IDs**:
*   Addresses the cold-start problem <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
*   Recommendations understand content <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
*   Enables human-readable explanations for recommendations when combined with language models <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

### [[data_augmentation_and_efficiency_in_recommendation_systems | Data Augmentation]] with LLMs
High-quality, scaled data is crucial for search and recommendation systems <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. Generating metadata, query expansions, and synonyms is costly and labor-intensive <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. LLMs excel at generating synthetic data and labels <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

**Example: Indeed**
Indeed faced challenges with poor job recommendation quality, leading to users losing trust and unsubscribing from emails <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>. Explicit negative feedback (thumbs down) was sparse, and implicit feedback was imprecise <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.

**Solution: LLM-distilled Lightweight Classifier**
Indeed developed a lightweight classifier to filter bad recommendations <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Initial Approach**: Human experts labeled job recommendations and user pairs <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
*   **LLM Experimentation**:
    *   Open LLMs (Mistral, Llama 2) performed poorly, producing generic output <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
    *   GPT-4 achieved 90% precision and recall but was too costly and slow (22 seconds) <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
    *   GPT-3.5 had very poor precision (63%), leading to discarding good recommendations <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
    *   Fine-tuning GPT-2.5 yielded desired precision but was still too slow for online filtering (6.7 seconds) <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
*   **Final Solution**: A lightweight classifier was distilled from the fine-tuned GPT-2.5 labels, achieving high performance (0.86 AU ROC) and real-time latency <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.

**Outcome**: Bad recommendations were reduced by 20% <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. Application rate increased by 4%, and unsubscribe rate decreased by 5% <a class="yt-timestamp" data-t="00:12:45">[00:12:45]</a>. This demonstrated that quality, not just quantity, significantly impacts recommendation performance <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

**Example: Spotify**
Spotify aimed to grow its podcast and audiobook categories beyond music, facing a cold-start problem for new content types <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.

**Solution: LLM-Generated Query Recommendations**
Spotify used LLMs to generate natural language queries for exploratory search <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Query Generation**: Combined conventional techniques (catalog titles, search logs, artist covers) with LLM-generated queries <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   **User Experience**: When a user searches, the system presents query recommendations at the top, informing users about new categories like audiobooks or podcasts without obtrusive banners <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

**Outcome**: A 9% increase in exploratory queries, meaning one-tenth of users explored new products daily, rapidly growing new content categories <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

**Benefits of LLM-augmented Synthetic Data**:
*   Richer, high-quality data at scale, especially for tail queries and items <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.
*   Lower cost and effort compared to human annotation <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

### [[unified_models_for_recommendation_systems | Unified Models]]
Traditional companies often have separate systems and models for ads, recommendations (e.g., homepage, item-to-item, cart), and search <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. This leads to duplicative engineering, high maintenance costs, and limited knowledge transfer between models <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

**Solution: Unified Models**
Inspired by successes in vision and language, unified models consolidate multiple tasks into a single architecture <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

**Example: Netflix (Unicorn Ranker)**
Netflix faced high operational costs and missed learning opportunities due to bespoke models for search, similar item recommendations, and pre-query recommendations <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

**Solution: Unified Contextual Ranker (Unicorn)**
Netflix developed a unified contextual ranker, Unicorn, to consolidate these tasks <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
*   **Architecture**: Takes unified input (user ID, item ID, search query, country, task) and uses a user foundation model with a context and relevance model <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.
*   **Missing Item Imputation**: For tasks like item-to-item recommendations where a search query might be absent, the model imputes it using the current item's title <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   **Outcome**: The unified model matched or exceeded the metrics of specialized models across multiple tasks <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. This reduced technical debt and built a better foundation for future iterations, enabling faster innovation <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.

**Example: Etsy (Unified Embeddings)**
Etsy needed to provide better results for both specific and broad queries while dealing with a constantly changing inventory <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>. Lexical embeddings didn't account for user preferences <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

**Solution: Unified Embedding and Retrieval**
Etsy implemented a unified embedding approach based on a two-tower model <a class="yt-timestamp" data-t="00:20:01">[00:20:01]</a>.
*   **Product Encoder**: Uses T5 models for text embeddings (item descriptions) and query-product logs for query embeddings <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>.
*   **Query Encoder**: Incorporates search query, product category, and user location <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.
*   **Personalization**: User preferences (past queries, purchases) are encoded <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a>.
*   **Quality Vector**: A quality vector (ratings, freshness, conversion rate) is concatenated to the product embedding to ensure relevant and high-quality results <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.
*   **Outcome**: A 2.6% increase in conversion across the entire site and over 5% increase in search purchases <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>.

**Benefits of [[unified_models_for_recommendation_systems | Unified Models]]**:
*   Simplifies the system <a class="yt-timestamp" data-t="00:22:10">[00:22:10]</a>.
*   Improvements to one part of the model automatically benefit other use cases <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>.
*   **Challenge**: Potential for "alignment types" where improving one task degrades another, requiring careful model design <a class="yt-timestamp" data-t="00:22:24">[00:22:24]</a>.

## Pinterest's Approach to Search Relevance
Pinterest, a visual discovery platform handling over six billion searches monthly across billions of pins and 45+ languages <a class="yt-timestamp" data-t="00:29:02">[00:29:02]</a>, focuses on semantic relevance modeling in the re-ranking stage <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>.

**LLMs for Relevance Prediction**
*   **Model**: A cross-encoder structure concatenates query and pin text, passing them to an LLM to get an embedding <a class="yt-timestamp" data-t="00:31:09">[00:31:09]</a>. This embedding then feeds into an MLP layer to predict relevance on a five-point scale <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>.
*   **Fine-tuning**: Open-source LLMs are fine-tuned using Pinterest's internal data <a class="yt-timestamp" data-t="00:31:42">[00:31:42]</a>.
*   **Results**: LLMs substantially improved relevance prediction performance <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>. Larger, more advanced LLMs (e.g., 8 billion parameters) showed significant improvements (12% over multilingual BERT, 20% over in-house embedding model) <a class="yt-timestamp" data-t="00:32:21">[00:32:21]</a>.

**Leveraging Multimodal Content**
Vision-language models (VLMs) generate captions from images and videos <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>. User actions (saves, clicks, searches) also provide valuable content annotations <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>. This diverse data helps create text representations of pins for LLM-based relevance prediction <a class="yt-timestamp" data-t="00:33:06">[00:33:06]</a>.

**Efficiency in LLM Serving**
To achieve low latency (under 500ms) for LLM serving, Pinterest employs three levers:
1.  **Specification**: Optimizing attention scores for specific tasks <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>.
2.  **Smaller Models**: Distilling larger models (e.g., 150 billion parameters) into smaller ones (8B, 3B, 1B) step-by-step to retain reasoning power <a class="yt-timestamp" data-t="00:33:50">[00:33:50]</a>. Aggressive pruning can significantly reduce model quality <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>.
3.  **Quantization**: Using lower precision (FP8) for activations and parameters, with mixed precision where the LLM head remains in FP32 for better calibration <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.

These optimizations resulted in a 7x reduction in latency and a 30x increase in throughput (queries per GPU) <a class="yt-timestamp" data-t="00:37:37">[00:37:37]</a>.

## Netflix's Foundational Model for Personalization
Netflix aims to use one foundational model to cover all recommendation use cases, addressing diverse recommendation needs across various content types and pages <a class="yt-timestamp" data-t="02:23:24">[02:23:24]</a>. Traditionally, this led to many specialized, independently built models with duplicative engineering and feature engineering <a class="yt-timestamp" data-t="02:24:52">[02:24:52]</a>.

**Hypothesis**:
1.  **Scalability**: Through scale-up semi-supervised learning, personalization can be improved, similar to LLMs <a class="yt-timestamp" data-t="02:27:36">[02:27:36]</a>.
2.  **High Leverage**: Integrating the foundation model into all systems can simultaneously improve downstream models <a class="yt-timestamp" data-t="02:27:49">[02:27:49]</a>.

**Data and Training**:
*   **Tokenization**: Crucial decision for model quality <a class="yt-timestamp" data-t="02:28:38">[02:28:38]</a>. Unlike LLMs, each event token in recommendations has multiple facets (when, where, what) <a class="yt-timestamp" data-t="02:29:11">[02:29:11]</a>.
*   **Event Representation**: Deciding what information (time, location, device, canvas, entity, interaction type/duration) to keep or drop <a class="yt-timestamp" data-t="02:30:31">[02:30:31]</a>.
*   **Embedding Layer**: Combines ID embedding learning with semantic content information to address the cold-start problem <a class="yt-timestamp" data-t="02:31:21">[02:31:21]</a>.
*   **Transformer Layer**: Hidden state output is used as user representation <a class="yt-timestamp" data-t="02:32:07">[02:32:07]</a>. Stability and aggregation methods are key considerations <a class="yt-timestamp" data-t="02:32:26">[02:32:26]</a>.
*   **Objective/Loss Function**: Richer than LLMs, using multiple sequences and facets of events (action type, metadata, future action prediction) as targets <a class="yt-timestamp" data-t="02:33:04">[02:33:04]</a>. This can be a multitask learning problem or used for weighting/masking <a class="yt-timestamp" data-t="02:34:01">[02:34:01]</a>.

**Scaling Results**: Netflix observed continuous gains in model quality over two and a half years by scaling data and model parameters (up to 1 billion parameters) <a class="yt-timestamp" data-t="02:34:27">[02:34:27]</a>. While scaling can continue, stringent latency and cost requirements necessitate distillation back to smaller models <a class="yt-timestamp" data-t="02:35:08">[02:35:08]</a>.

**Learnings from LLMs**:
*   **Multi-token prediction**: Forces the model to be less myopic, more robust to serving time shifts, and targets long-term user satisfaction <a class="yt-timestamp" data-t="02:35:36">[02:35:36]</a>.
*   **Multi-layer representation**: Techniques like layer-wise supervision and self-distillation create better and more stable user representations <a class="yt-timestamp" data-t="02:36:12">[02:36:12]</a>.
*   **Long context window handling**: Using truncated sliding windows, sparse attention, and progressive training for longer sequences improves efficiency <a class="yt-timestamp" data-t="02:36:34">[02:36:34]</a>.

**Serving and Applications**:
The foundation model consolidates the data and representation layers (user and content representation), making application models thinner <a class="yt-timestamp" data-t="02:37:12">[02:37:12]</a>.
*   **Integration as Subgraph**: FM can be integrated as a pre-trained subgraph within downstream neural network models <a class="yt-timestamp" data-t="02:37:48">[02:37:48]</a>.
*   **Embedding Push-out**: Content and member embeddings can be pushed to a centralized store, allowing wider use cases beyond personalization (e.g., analytics) <a class="yt-timestamp" data-t="02:38:15">[02:38:15]</a>.
*   **Fine-tuning/Distillation**: Users can extract and fine-tune models for specific applications or distill them to meet online serving requirements <a class="yt-timestamp" data-t="02:38:51">[02:38:51]</a>.

**Outcome**: The foundational model has been incorporated into many applications, leading to significant AB test wins and infrastructure consolidation <a class="yt-timestamp" data-t="02:39:12">[02:39:12]</a>. It's a scalable solution that improves quality and accelerates innovation velocity <a class="yt-timestamp" data-t="02:40:03">[02:40:03]</a>.

## Instacart's Search and Discovery Enhancement with LLMs
Instacart, a leader in online grocery, focuses on search to help customers find both restocking items and discover new products <a class="yt-timestamp" data-t="02:46:01">[02:46:01]</a>. New product discovery benefits customers, advertisers, and increases basket sizes <a class="yt-timestamp" data-t="02:47:17">[02:47:17]</a>.

**Challenges with Conventional Search Engines**:
*   **Broad Queries**: Overly broad queries (e.g., "snacks") map to many products but lack engagement data for proper ranking <a class="yt-timestamp" data-t="02:47:48">[02:47:48]</a>.
*   **Specific Queries**: Very specific queries (e.g., "unsweetened plant-based yogurt") occur infrequently, leading to insufficient engagement data <a class="yt-timestamp" data-t="02:48:12">[02:48:12]</a>.
*   **Precision vs. Recall**: Traditional models improved recall but struggled with precision <a class="yt-timestamp" data-t="02:48:37">[02:48:37]</a>.
*   **Limited Discovery**: Users found it difficult to discover related products after finding an initial item, requiring multiple searches <a class="yt-timestamp" data-t="02:49:03">[02:49:03]</a>.

**Upleveling Query Understanding with LLMs**:
Instacart used LLMs to enhance its query understanding module, which includes query normalization, tagging, and classification <a class="yt-timestamp" data-t="02:49:37">[02:49:37]</a>.

**Query-to-Category Classifier**:
*   **Task**: Map a query (e.g., "watermelon") to relevant categories (e.g., "fruits") within a taxonomy of ~10,000 labels <a class="yt-timestamp" data-t="02:50:16">[02:50:16]</a>. This is a multi-label classification problem <a class="yt-timestamp" data-t="02:50:40">[02:50:40]</a>.
*   **Previous Models**: FastText neural networks and NPMI (statistical co-occurrence) models worked for head/torso queries but had low coverage for tail queries due to lack of engagement data <a class="yt-timestamp" data-t="02:50:46">[02:50:46]</a>. BERT-based models offered some improvement but insufficient for increased latency <a class="yt-timestamp" data-t="02:51:22">[02:51:22]</a>.
*   **LLM Approach**: Initially, LLMs alone produced decent but not optimal results in A/B tests because they didn't understand Instacart-specific user behavior (e.g., "protein" meaning shakes/bars, not chicken/tofu) <a class="yt-timestamp" data-t="02:51:36">[02:51:36]</a>.
*   **Hybrid Approach**: The prompt was augmented with Instacart domain knowledge, such as top-converting categories for each query and annotations from query understanding models (brands, dietary attributes) <a class="yt-timestamp" data-t="02:52:30">[02:52:30]</a>.
*   **Outcome**: For tail queries, precision improved by 18 percentage points and recall by 70 percentage points <a class="yt-timestamp" data-t="02:53:29">[02:53:29]</a>. A simple prompt with contextual information was highly effective <a class="yt-timestamp" data-t="02:53:42">[02:53:42]</a>.

**Query Rewrites Model**:
*   **Purpose**: Essential for e-commerce, especially with varied retailer catalogs, to ensure results are returned even for specific queries <a class="yt-timestamp" data-t="02:54:10">[02:54:10]</a> (e.g., "1% milk" to "milk") <a class="yt-timestamp" data-t="02:54:27">[02:54:27]</a>.
*   **Previous Approach**: Engagement data-trained models struggled with tail queries <a class="yt-timestamp" data-t="02:54:37">[02:54:37]</a>.
*   **LLM Approach**: LLMs generated precise rewrites (substitute, broad, synonymous) <a class="yt-timestamp" data-t="02:54:48">[02:54:48]</a>.
*   **Outcome**: Significant offline improvements through human evaluation and a large drop in "no results" queries online <a class="yt-timestamp" data-t="02:55:16">[02:55:16]</a>, benefiting the business by showing results where none existed before <a class="yt-timestamp" data-t="02:55:47">[02:55:47]</a>.

**Scoring and Serving**:
Instacart precomputes outputs for head and torso queries offline in batch mode and caches them for low-latency online serving <a class="yt-timestamp" data-t="02:56:06">[02:56:06]</a>. For the long tail, existing models are currently used as a fallback, with plans to replace them with distilled LLM models <a class="yt-timestamp" data-t="02:56:49">[02:56:49]</a>.

**Future Directions for Query Understanding**:
*   **Consolidation**: Consolidating multiple query understanding models into a single LLM to improve consistency and simplify management <a class="yt-timestamp" data-t="02:57:21">[02:57:21]</a> (e.g., fixing "hum" vs. "hummus" error) <a class="yt-timestamp" data-t="02:57:41">[02:57:41]</a>.
*   **Contextual Understanding**: Using LLMs to understand the customer's broader mission (e.g., buying ingredients for a recipe) <a class="yt-timestamp" data-t="02:58:13">[02:58:13]</a>.

**Discovery-Oriented Content in Search Results**:
Users often found search results pages to be "dead ends" after adding an item to the cart <a class="yt-timestamp" data-t="02:58:43">[02:58:43]</a>. LLMs were used to generate substitute and complementary results directly on the page <a class="yt-timestamp" data-t="02:59:17">[02:59:17]</a>.
*   **Substitute Results**: For queries with no exact matches (e.g., "swordfish"), LLMs generate alternatives (e.g., "other seafood alternatives") <a class="yt-timestamp" data-t="02:59:21">[02:59:21]</a>.
*   **Complementary Results**: For queries with many exact matches (e.g., "sushi"), LLMs suggest related items (e.g., "Asian cooking ingredients") at the bottom of the page <a class="yt-timestamp" data-t="02:59:31">[02:59:31]</a>.
*   **Outcome**: Both led to improvements in engagement and revenue per search <a class="yt-timestamp" data-t="02:59:51">[02:59:51]</a>.

**Generation Requirements and Techniques**:
*   **Incrementality**: Generate content incremental to existing solutions <a class="yt-timestamp" data-t="03:00:08">[03:00:08]</a>.
*   **Domain Alignment**: LLM answers must align with Instacart's domain knowledge (e.g., "dishes" meaning cookware, not food, unless specified) <a class="yt-timestamp" data-t="03:00:14">[03:00:14]</a>.
*   **Prompt Augmentation**: Initially, LLM-generated common sense answers didn't align with user behavior <a class="yt-timestamp" data-t="03:01:11">[03:01:11]</a>. Augmenting prompts with Instacart domain knowledge (top converting categories, query annotations, subsequent user queries) significantly improved results <a class="yt-timestamp" data-t="03:01:41">[03:01:41]</a>.

**Serving Discovery Content**:
Similar to query understanding, Instacart precomputes LLM outputs for historical search logs in batch mode, storing query content metadata and potential products <a class="yt-timestamp" data-t="03:02:30">[03:02:30]</a>. Online serving is a quick lookup from a feature store, maintaining low latency <a class="yt-timestamp" data-t="03:02:52">[03:02:52]</a>.

**Key Challenges Faced**:
1.  **Aligning with Business Metrics**: Iterating on prompts and metadata to ensure LLM generations drive top-line wins like revenue <a class="yt-timestamp" data-t="03:03:13">[03:03:13]</a>.
2.  **Ranking Improvement**: Traditional models failed; strategies like diversity-based re-ranking were needed for user engagement <a class="yt-timestamp" data-t="03:03:28">[03:03:28]</a>.
3.  **Content Evaluation**: Ensuring LLM outputs are accurate (not hallucinating) and adhere to product needs, often using an LLM as a judge <a class="yt-timestamp" data-t="03:04:21">[03:04:21]</a>.

## YouTube's Large Recommender Model (LRM)
YouTube, one of the largest consumer apps globally, relies heavily on recommendation systems for watch time across various surfaces (home, watch next, shorts, search) <a class="yt-timestamp" data-t="03:09:01">[03:09:01]</a>. Google has built a new [[building_user_experiences_with_ai | recommendation system]] using Gemini to recommend YouTube videos <a class="yt-timestamp" data-t="03:07:08">[03:07:08]</a>.

**Adapting Gemini for YouTube Recommendations (LRM)**:
*   **Foundation**: Starts with a base Gemini checkpoint <a class="yt-timestamp" data-t="03:11:36">[03:11:36]</a>.
*   **Continued Pre-training**: Teaches the model information about YouTube to create a unified, YouTube-specific checkpoint called LRM <a class="yt-timestamp" data-t="03:11:39">[03:11:39]</a>.
*   **Alignment**: Aligns LRM for specific recommendation tasks like retrieval and ranking, creating custom versions for major surfaces <a class="yt-timestamp" data-t="03:11:51">[03:11:51]</a>. LRM is in production for retrieval and being experimented with for ranking <a class="yt-timestamp" data-t="03:12:06">[03:12:06]</a>.

**Semantic ID for Videos**:
*   **Challenge**: Need to tokenize videos to allow LLMs to reason over many videos <a class="yt-timestamp" data-t="03:12:24">[03:12:24]</a>.
*   **Process**:
    1.  Extract features (title, description, transcript, audio/video frame data) from a video <a class="yt-timestamp" data-t="03:13:21">[03:13:21]</a>.
    2.  Create a multi-dimensional embedding <a class="yt-timestamp" data-t="03:13:33">[03:13:33]</a>.
    3.  Quantize using RQVE to assign a unique semantic ID (SID) token to each video <a class="yt-timestamp" data-t="03:13:36">[03:13:36]</a>.
*   **Outcome**: The entire corpus of billions of YouTube videos is organized around semantically meaningful tokens, creating a "new language of YouTube videos" <a class="yt-timestamp" data-t="03:13:55">[03:13:55]</a>. This is a move away from hash-based tokenization <a class="yt-timestamp" data-t="03:14:25">[03:14:25]</a>.

**Continued Pre-training of LRM**:
1.  **Linking Text and SID**: Training tasks connect English text with video tokens (SIDs) <a class="yt-timestamp" data-t="03:14:45">[03:14:45]</a> (e.g., "This video has title XYZ" followed by the model outputting the title) <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.
2.  **Understanding Watch Sequences**: Using YouTube engagement data (user paths through videos), the model is prompted with sequences of watched videos (e.g., ABCD) and learns to predict masked videos <a class="yt-timestamp" data-t="03:15:26">[03:15:26]</a>. This teaches it relationships between videos based on user engagement <a class="yt-timestamp" data-t="03:15:46">[03:15:46]</a>.

**Generative Retrieval with LRM**:
*   **Process**: A prompt is constructed for each user including demographic information, context video, and watch history <a class="yt-timestamp" data-t="03:17:05">[03:17:05]</a>. The model then decodes video recommendations as SIDs <a class="yt-timestamp" data-t="03:17:37">[03:17:37]</a>.
*   **Outcome**: Generates unique and interesting recommendations, particularly for difficult recommendation tasks or users with limited data <a class="yt-timestamp" data-t="03:17:41">[03:17:41]</a>.

**Challenges for YouTube LRM**:
*   **Cost**: LRM is powerful but expensive to serve <a class="yt-timestamp" data-t="03:18:36">[03:18:36]</a>. YouTube achieved over 95% cost savings to enable production launch <a class="yt-timestamp" data-t="03:19:01">[03:19:01]</a>.
*   **Vocabulary Size**: Billions of videos (20 billion, millions added daily) vs. 100,000 words in LLM English vocabulary <a class="yt-timestamp" data-t="03:20:24">[03:20:24]</a>.
*   **Freshness**: Unlike LLMs, recommendation systems demand real-time freshness (minutes/hours) for new content <a class="yt-timestamp" data-t="03:20:51">[03:20:51]</a>. LRM requires continuous pre-training on a daily/hourly basis <a class="yt-timestamp" data-t="03:21:35">[03:21:35]</a>.
*   **Scale**: Must use smaller, more efficient models (Flash and smaller checkpoints) to meet latency and scale requirements for billions of daily active users <a class="yt-timestamp" data-t="03:21:52">[03:21:52]</a>.

**Recipe for LLM-based Recommendation System**:
1.  **Tokenize Content**: Create a domain-specific language by building rich embeddings from features and quantizing them into atomic tokens <a class="yt-timestamp" data-t="03:22:28">[03:22:28]</a>.
2.  **Adapt LLM**: Link English and the new domain language through training tasks that enable reasoning across both <a class="yt-timestamp" data-t="03:22:56">[03:22:56]</a>, resulting in a bilingual LLM <a class="yt-timestamp" data-t="03:23:10">[03:23:10]</a>.
3.  **Prompt with User Information**: Construct personalized prompts with user demographics, activity, and actions, then train task-specific models to create a generative recommendation system <a class="yt-timestamp" data-t="03:23:21">[03:23:21]</a>.

## [[future_of_ai_in_improving_user_experience_and_integrations | Future of AI in Recommendations]]
Currently, LLMs primarily augment recommendations, enhancing quality invisibly to users <a class="yt-timestamp" data-t="03:23:56">[03:23:56]</a>. The [[ai_trust_gap_in_user_experiences | AI trust gap in user experiences]] for recommendations is "underhyped" because users don't directly know what's happening <a class="yt-timestamp" data-t="03:24:16">[03:24:16]</a>.

**Upcoming Developments**:
*   **Interactive Experiences**: Users will be able to talk to bilingual LLMs in natural language to steer recommendations towards their goals <a class="yt-timestamp" data-t="03:24:26">[03:24:26]</a>.
*   **Explainable Recommendations**: Recommenders will explain why a candidate was recommended <a class="yt-timestamp" data-t="03:24:42">[03:24:42]</a>.
*   **Blurring Search and Recommendations**: The lines between search and recommendation will increasingly blur <a class="yt-timestamp" data-t="03:24:52">[03:24:52]</a>.
*   **Generative Content**: Recommendations may evolve to include personalized versions of content, or even content creation itself, leading to "end-of-one" content generated for individual users <a class="yt-timestamp" data-t="03:25:01">[03:25:01]</a>. This represents a significant shift in [[the_evolution_of_ai_interfaces_and_user_interaction | the evolution of AI interfaces and user interaction]] and [[design_process_improvements_with_ai | design process improvements with AI]].

> [!NOTE] Learnings:
> *   **Semantic IDs**: Solve cold-start and sparsity by encoding content.
> *   **[[data_augmentation_and_efficiency_in_recommendation_systems | Data Augmentation]]**: LLMs generate rich, high-quality synthetic data for tail queries and items at lower cost.
> *   **[[unified_models_for_recommendation_systems | Unified Models]]**: Simplify systems, reduce maintenance, and accelerate innovation across multiple recommendation tasks.