---
title: Semantic IDs and multimodal embeddings
videoId: 3k4a0PemMu4
---

From: [[aidotengineer]] <br/> 

The concept of Semantic IDs and [[multimodal_models_and_omni_models_development | multimodal embeddings]] is proposed as a solution to long-standing challenges in recommendation systems, such as handling new items and sparsity issues <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Traditionally, hash-based item IDs do not encode the content of an item, leading to a "cold-start problem" for new items where systems have to relearn everything about them <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This also contributes to sparsity, especially for "tail items" with few interactions, making it difficult for recommendation systems to learn effectively and leading to popularity bias <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.

## Addressing Challenges with Semantic IDs
The proposed solution is the use of [[semantic_enrichment_and_graphbased_searches_in_architecture | semantic]] IDs, which can incorporate [[multimodal_models_and_omni_models_development | multimodal content]] <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. These IDs encode the content of the item, allowing recommendations to understand content and directly address the cold-start problem <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### Quao's Trainable Multimodal Semantic IDs
Quao, a short video platform similar to TikTok or Xiaohongshu in China, faced the challenge of learning from hundreds of millions of short videos uploaded daily <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. They developed trainable [[multimodal_models_and_omni_models_development | multimodal semantic IDs]] to combine static content embeddings with dynamic user behavior <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

The Quao model uses a standard two-tower network architecture <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
*   **Input Encoding**: Content inputs are encoded using specialized models: ResNet for visual content, BERT for video descriptions, and VGGish for audio <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Concatenation and Clustering**: These content embeddings are concatenated <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. For 100 million short videos, Quao learned 1,000 cluster IDs via k-means clustering <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **Model Encoder**: The model encoder learns to map the content space via these trainable cluster IDs to the behavioral space <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. The cluster IDs are mapped to their own embedding table <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

This approach resulted in Semantic IDs that not only outperformed regular hash-based IDs on clicks and likes but significantly increased cold-start coverage by 3.6% and cold-start velocity <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.

### YouTube's Large Recommender Model (LRM)
YouTube adapted its recommendation system using Google's Gemini model, creating what they call the Large Recommender Model (LRM) <a class="yt-timestamp" data-t="03:10:41">[03:10:41]</a>. The core innovation for this model is the development of a method to tokenize videos <a class="yt-timestamp" data-t="03:12:22">[03:12:22]</a>.

#### Semantic ID for Videos
To allow reasoning over many videos, YouTube built a [[semantic_enrichment_and_graphbased_searches_in_architecture | semantic]] ID system for video tokenization <a class="yt-timestamp" data-t="03:12:50">[03:12:50]</a>.
*   **Feature Extraction**: Features like title, description, transcript, audio, and video frame-level data are extracted from a video <a class="yt-timestamp" data-t="03:13:21">[03:13:21]</a>.
*   **Embedding and Quantization**: These features are transformed into a multi-dimensional embedding and then quantized using RQVE to assign each video a token <a class="yt-timestamp" data-t="03:13:33">[03:13:33]</a>.
*   **Domain-Specific Language**: This process creates atomic units for a new "language of YouTube videos," organizing billions of videos around [[semantic_enrichment_and_graphbased_searches_in_architecture | semantically meaningful tokens]] <a class="yt-timestamp" data-t="03:13:47">[03:13:47]</a>. These tokens can represent topics like music, gaming, or sports, with prefixes shared among related content and unique identifiers for specific videos <a class="yt-timestamp" data-t="03:14:04">[03:14:04]</a>.

#### Continued Pre-training and Reasoning
The LRM undergoes "continued pre-training" to understand both English and this new YouTube language <a class="yt-timestamp" data-t="03:14:36">[03:14:36]</a>.
1.  **Text and SID Linking**: The model learns to link text (e.g., video titles, creators, topics) with their corresponding Semantic IDs <a class="yt-timestamp" data-t="03:14:48">[03:14:48]</a>.
2.  **Sequence Understanding**: It learns from sequences of user watches, predicting masked videos within a watch history to understand relationships based on user engagement <a class="yt-timestamp" data-t="03:15:26">[03:15:26]</a>.

This training enables the model to reason across English and YouTube videos, inferring topics and connections based solely on the Semantic ID <a class="yt-timestamp" data-t="03:16:07">[03:16:07]</a>.

#### Generative Retrieval
The LRM is used for generative retrieval, where a prompt incorporating user demographics, context videos, and watch history is constructed to recommend new SIDs <a class="yt-timestamp" data-t="03:17:03">[03:17:03]</a>. This yields unique recommendations, particularly for challenging recommendation tasks or users with limited historical data <a class="yt-timestamp" data-t="03:17:41">[03:17:41]</a>. An offline recommendations table can also be built by removing personalized aspects from the prompt, which, due to the LRM's large pre-trained checkpoint, still provides differentiated recommendations <a class="yt-timestamp" data-t="03:19:12">[03:19:12]</a>.

### Etsy's Unified Embeddings
Etsy uses [[unified_models_for_recommendation_systems | unified embeddings]] and retrieval to improve search results for both specific and broad queries, especially given its constantly changing inventory <a class="yt-timestamp" data-t="03:19:13">[03:19:13]</a>.
*   **Product Encoder**: Uses T5 models for text embeddings of item descriptions and query product logs for query embeddings (what was clicked/purchased after a query) <a class="yt-timestamp" data-t="03:20:18">[03:20:18]</a>.
*   **Query Encoder**: Encodes search queries <a class="yt-timestamp" data-t="03:20:35">[03:20:35]</a>.
*   **Shared Encoders**: Both product and query encoders share encoders for text tokens, product category tokens, and user location, enabling the embedding to match users to product locations <a class="yt-timestamp" data-t="03:20:40">[03:20:40]</a>.
*   **Personalization**: User preferences are encoded via query user scale effect features, including past queries and purchase history <a class="yt-timestamp" data-t="03:20:57">[03:20:57]</a>.
*   **Quality Vector**: A "quality vector" (incorporating ratings, freshness, conversion rate) is concatenated to the product embedding to ensure retrieved items are of good quality <a class="yt-timestamp" data-t="03:21:18">[03:21:18]</a>. For the query vector, a constant vector is "slapped on" to match dimensions for dot product or cosine similarity <a class="yt-timestamp" data-t="03:21:38">[03:21:38]</a>.

This approach led to a 2.6% increase in conversion across the entire site and over 5% increase in search purchases, demonstrating that quality in recommendations makes a significant difference <a class="yt-timestamp" data-t="03:21:51">[03:21:51]</a>.

## Challenges and Future Directions
Implementing [[multimodal_models_and_omni_models_development | multimodal embedding]]-based systems presents unique challenges compared to traditional LLMs:
*   **Vocabulary Size and Freshness**: Recommendation systems deal with much larger vocabularies (e.g., billions of videos on YouTube vs. thousands of words in English) and require constant updates for new content (e.g., a new music video must be recommended within minutes or hours) <a class="yt-timestamp" data-t="03:20:24">[03:20:24]</a>. This necessitates continuous pre-training on the order of days or hours <a class="yt-timestamp" data-t="03:21:35">[03:21:35]</a>.
*   **Serving Costs**: Large [[multimodal_models_and_omni_models_development | multimodal]] models are expensive to serve, requiring significant optimization (e.g., 95%+ cost savings for YouTube's LRM) to meet the latency and scale requirements of billions of daily active users <a class="yt-timestamp" data-t="03:18:36">[03:18:36]</a>.
*   **Balancing Language Capabilities**: A key challenge is balancing the learning of [[semantic_enrichment_and_graphbased_searches_in_architecture | semantic]] ID embeddings with retaining general language capability in [[multimodal_models_and_omni_models_development | multimodal]] models <a class="yt-timestamp" data-t="03:25:50">[03:25:50]</a>. Over-training on domain-specific examples can lead to the model "forgetting" how to speak English <a class="yt-timestamp" data-t="03:26:26">[03:26:26]</a>.

The future of [[multimodal_models_and_omni_models_development | multimodal]]-powered recommendation systems is envisioned to involve more explicit user interaction, where users can steer recommendations using natural language, receive explanations for recommendations, and blur the lines between search and recommendation <a class="yt-timestamp" data-t="03:24:24">[03:24:24]</a>. Ultimately, this could lead to the recommendation of personalized and even dynamically generated content <a class="yt-timestamp" data-t="03:25:01">[03:25:01]</a>.