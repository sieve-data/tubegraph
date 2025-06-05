---
title: Personalization strategies using LLMs
videoId: 3k4a0PemMu4
---

From: [[aidotengineer]] <br/> 

The intersection of recommendation systems and large language models (LLMs) is a significant area of development, promising to revolutionize how users discover content and products <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This integration builds upon a long history of language modeling techniques in recommendation systems, which date back to 2013 with item embeddings and later evolved with GRU4Rec and transformers for handling longer interaction sequences <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

## Challenges in Conventional Recommendation Systems

Traditional recommendation systems face several inherent challenges:
*   **Hash-based Item IDs**: These do not inherently encode content, leading to the "cold-start problem" for new items where systems must relearn everything about them <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.
*   **Sparsity**: Many "tail" items have very few interactions, making it difficult for models to learn effectively <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Popularity Bias**: Systems often favor popular items, struggling to recommend new or niche content <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
*   **Data Quality and Scale**: Machine learning models, especially for search and recommendations, require vast amounts of high-quality, metadata-rich data, which is costly and labor-intensive to acquire through traditional means <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **System Silos**: Historically, systems for ads, recommendations, and search operate separately, leading to duplicated engineering efforts, high maintenance costs, and limited knowledge transfer between models <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>.

## Personalization Strategies Leveraging LLMs

Three key strategies are emerging to address these challenges and enhance personalization:

### 1. [[semantic_ids | Semantic IDs]]
[[semantic_ids | Semantic IDs]] encode the content of an item, including multimodal information, allowing recommendations to understand content <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This approach directly tackles the cold-start problem for new items <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

#### Example: Kwai's Trainable Multimodal Semantic IDs
Kwai, a short-video platform, faced the challenge of learning from hundreds of millions of daily video uploads <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Their solution involved combining static content embeddings with dynamic user behavior using trainable multimodal semantic IDs <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **Architecture**: They used a standard two-tower network. Content inputs (visual via ResNet, video descriptions via BERT, audio via VGGish) were concatenated <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
*   **Clustering**: Non-trainable content embeddings were used to learn 1,000 cluster IDs via K-means clustering from 100 million short videos <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. These cluster IDs were mapped to their own embedding table <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.
*   **Learning**: The model encoder learned to map the content space via these cluster IDs to the behavioral space <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Outcome**: These semantic IDs not only outperformed hash-based IDs on clicks and likes but significantly increased cold-start coverage (3.6%) and cold-start velocity, enabling new videos to reach view thresholds faster <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

Future integrations may involve blending LLMs with [[semantic_ids | semantic IDs]] to explain why a user might like a recommendation, providing human-readable explanations <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>. YouTube has also built [[semantic_ids | semantic IDs]] by distilling multimodal features into tokens, organizing billions of videos into semantically meaningful tokens <a class="yt-timestamp" data-t="03:06:52">[03:06:52]</a>.

### 2. [[data_handling_and_preparing_training_datasets_for_LLMs | LLM-Augmented Synthetic Data / Data Augmentation]]
LLMs excel at generating synthetic data and labels, providing richer, high-quality data at scale, especially for tail queries and items, at a significantly lower cost and effort than human annotation <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.

#### Example: Indeed's Job Recommendation Filtering
Indeed faced the challenge of bad job recommendations leading to poor user experience and unsubscriptions <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Explicit feedback (thumbs up/down) was sparse, and implicit feedback was imprecise <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Solution**: They developed a lightweight classifier to filter bad recommendations <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Process**:
    1.  Human experts labeled job recommendations and user pairs based on resume and activity data <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
    2.  Open LLMs (Mistral, Llama 2) showed poor performance due to generic output <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.
    3.  GPT-4 performed well (90% precision and recall) but was too costly and slow (22 seconds per prediction) <a class="yt-timestamp" data-t="00:10:38">[00:10:38]</a>.
    4.  GPT-3.5 had poor precision, incorrectly filtering out 37% of good recommendations <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
    5.  Fine-tuning GPT-2.5 achieved the desired precision but was still too slow (6.7 seconds) for online filtering <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>.
    6.  Finally, they distilled a lightweight classifier using labels from the fine-tuned GPT-2.5, achieving high performance (0.86 AU ROC) and real-time latency <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
*   **Outcome**: This reduced bad recommendations by 20%, increased application rates by 4%, and decreased unsubscribe rates by 5%, demonstrating that quality over quantity significantly improves recommendation impact <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>.

#### Example: Spotify's Query Recommendation System
Spotify aimed to expand beyond music into podcasts and audiobooks, facing a cold-start problem for new content categories <a class="yt-timestamp" data-t="00:13:04">[00:13:04]</a>.
*   **Solution**: They used an LLM to generate natural language queries for an exploratory search system <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>. Existing techniques generated queries from catalog titles, playlists, and search logs <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>. The LLM augmented this by generating more natural language queries <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>.
*   **Outcome**: This led to a 9% increase in exploratory queries, meaning one-tenth of their users were now exploring new products daily, significantly accelerating category growth <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.

#### Example: Instacart's Search and Discovery
Instacart used LLMs to improve query understanding and product discovery, tackling challenges like overly broad or specific queries, and enabling new item discovery <a class="yt-timestamp" data-t="02:47:32">[02:47:32]</a>.
*   **Query to Product Category Classifier**: Traditional models struggled with tail queries due to lack of engagement data <a class="yt-timestamp" data-t="02:50:46">[02:50:46]</a>. Initial LLM prompting was decent but failed in A/B tests due to a mismatch with Instacart user behavior (e.g., "protein" meaning supplements vs. chicken) <a class="yt-timestamp" data-t="02:51:36">[02:51:36]</a>. The solution was to augment the prompt with Instacart's domain knowledge, such as top converting categories for each query, significantly improving precision and recall for tail queries <a class="yt-timestamp" data-t="02:52:30">[02:52:30]</a>.
*   **Query Rewrites**: LLMs generated precise rewrites (substitute, broad, synonymous) for queries, which was crucial for retailers with varying catalog sizes <a class="yt-timestamp" data-t="02:54:08">[02:54:08]</a>. This drastically reduced queries with no results, boosting business <a class="yt-timestamp" data-t="02:55:41">[02:55:41]</a>.
*   **Discovery-Oriented Content**: LLMs generated substitute and complementary product suggestions for search results pages (e.g., seafood alternatives for swordfish, Asian cooking ingredients for sushi) <a class="yt-timestamp" data-t="02:58:43">[02:58:43]</a>. Again, augmenting LLM prompts with Instacart domain knowledge (top converting categories, query annotations, subsequent user queries) was key to aligning generated content with user behavior and business metrics <a class="yt-timestamp" data-t="03:01:39">[03:01:39]</a>.
*   **Serving**: Instacart precomputed LLM outputs for head and torso queries offline, caching them for low-latency online serving, and falling back to existing models for the long tail, with plans to replace those with distilled LLMs <a class="yt-timestamp" data-t="02:56:02">[02:56:02]</a>.

### 3. [[augmented_llm_architectures | Unified Models]]
Unified models aim to consolidate multiple specialized models for different recommendation tasks (e.g., homepage, item, cart recommendations) into a single, cohesive system <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. This approach leverages shared learning and reduces engineering overhead <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

#### Example: Netflix's Unified Contextual Ranker (Unicorn)
Netflix sought to address the proliferation of bespoke models for various recommendation and search tasks <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>.
*   **Solution**: They developed Unicorn, a unified contextual ranker built on a user foundation model and a context/relevance model <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
*   **Unified Input**: The model uses a single data schema for all use cases, incorporating user ID, item ID, search query (if applicable), country, and task <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. Smart imputation fills missing data, like using the current item's title as a search query if none exists <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   **Outcome**: Unicorn matched or exceeded the metrics of specialized models across multiple tasks <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>, reducing technical debt and accelerating future iterations <a class="yt-timestamp" data-t="00:19:04">[00:19:04]</a>.

#### Scaling Foundation Models for Recommendations
Netflix observed that scaling laws, similar to those in LLMs, apply to recommendation systems; continuous scaling up of models and data yielded performance gains <a class="yt-timestamp" data-t="02:34:31">[02:34:31]</a>. However, stringent latency and cost requirements for real-time recommendations necessitate distillation of larger models for production <a class="yt-timestamp" data-t="02:35:08">[02:35:08]</a>.

#### Learnings from LLM Development Applied to Recommendation Models
*   **Multi-Token Prediction**: Forces the model to be less myopic, more robust to serving time shifts, and targets long-term user satisfaction <a class="yt-timestamp" data-t="02:35:36">[02:35:36]</a>.
*   **Multi-Layer Representation**: Improves the stability and quality of user representations <a class="yt-timestamp" data-t="02:36:12">[02:36:12]</a>.
*   **Long Context Window Handling**: Techniques from LLMs, such as truncated sliding windows and sparse attention, maximize learning and training efficiency <a class="yt-timestamp" data-t="02:36:34">[02:36:34]</a>.

#### Integration and Application of Foundation Models
Netflix's foundation model (FM) integrates with downstream models in three ways:
1.  **Subgraph Integration**: The FM can be used as a pre-trained subgraph within downstream neural networks <a class="yt-timestamp" data-t="02:37:48">[02:37:48]</a>.
2.  **Embedding Push-out**: Content and user embeddings from the FM are pushed to a centralized embedding store for wider use cases, including analytics <a class="yt-timestamp" data-t="02:38:15">[02:38:15]</a>.
3.  **Model Extraction and Fine-tuning/Distillation**: Specific applications can fine-tune or distill the FM to meet online serving requirements <a class="yt-timestamp" data-t="02:38:51">[02:38:51]</a>.

This approach yielded significant "wins" in both A/B test improvements and infrastructure consolidation <a class="yt-timestamp" data-t="02:39:12">[02:39:12]</a>.

#### Example: Etsy's Unified Embeddings
Etsy used unified embeddings for search and retrieval to address challenges with specific or broad queries and constantly changing inventory <a class="yt-timestamp" data-t="01:59:30">[01:59:30]</a>.
*   **Architecture**: Similar to a two-tower model, with a product encoder (using T5 for text embeddings and query-product logs) and a query encoder. Both share encoders for text tokens, product categories, and user location <a class="yt-timestamp" data-t="02:00:03">[02:00:03]</a>. User preferences are personalized via query-user scale effect features <a class="yt-timestamp" data-t="02:05:40">[02:05:40]</a>.
*   **Quality Vector**: A "quality vector" (ratings, freshness, conversion rate) was concatenated to the product embedding vector, with a constant vector slapped onto the query embedding to match dimensions for similarity calculation <a class="yt-timestamp" data-t="02:11:18">[02:11:18]</a>.
*   **Outcome**: This resulted in a 2.6% increase in conversion across the entire site and over 5% increase in search purchases <a class="yt-timestamp" data-t="02:18:50">[02:18:50]</a>, demonstrating the strong impact of unified models on core business metrics.

## Future Directions
The application of LLMs in personalization is rapidly evolving:
*   **Invisible Augmentation**: Currently, LLMs largely augment recommendation quality invisibly to users <a class="yt-timestamp" data-t="02:39:56">[02:39:56]</a>.
*   **Interactive Experiences**: Future developments aim for users to directly interact with recommendation systems using natural language, allowing them to steer recommendations, receive explanations, and align recommendations with their specific goals <a class="yt-timestamp" data-t="02:40:07">[02:40:07]</a>. This will blur the lines between search and recommendation <a class="yt-timestamp" data-t="02:40:52">[02:40:52]</a>.
*   **Generative Content**: Ultimately, recommendation systems may not just recommend content but also generate personalized versions of content, leading to "end-of-one" content created specifically for individual users <a class="yt-timestamp" data-t="02:41:01">[02:41:01]</a>.

The recipe for building an LLM-based recommendation system involves three major steps <a class="yt-timestamp" data-t="02:42:25">[02:42:25]</a>:
1.  **Content Tokenization**: Creating a domain-specific language by tokenizing content (e.g., video frames, audio, text) into atomic units (like [[semantic_ids | semantic IDs]]) <a class="yt-timestamp" data-t="02:42:30">[02:42:30]</a>.
2.  **LLM Adaptation**: Teaching an LLM to understand both natural language and this new domain-specific language, creating a bilingual LLM through targeted training tasks <a class="yt-timestamp" data-t="02:42:57">[02:42:57]</a>.
3.  **Personalized Prompting**: Using user information (demographics, activity) to construct personalized prompts, leading to a generative recommendation system <a class="yt-timestamp" data-t="02:43:21">[02:43:21]</a>.

This approach represents a significant advancement in personalization, promising more relevant, dynamic, and interactive user experiences <a class="yt-timestamp" data-t="02:43:36">[02:43:36]</a>.