---
title: Unified models for recommendation systems
videoId: 3k4a0PemMu4
---

From: [[aidotengineer]] <br/> 

Recommendation systems, search, and advertising platforms traditionally operate with separate and specialized models for various use cases, leading to significant engineering and maintenance overhead. For instance, a single company might have distinct models for homepage recommendations, item recommendations, and even thank you page suggestions [00:16:15]. This fragmented approach results in duplicative engineering pipelines, high maintenance costs, and limited transfer of improvements between models [00:16:27]. The solution gaining traction in the industry is the adoption of unified models, which centralize learning and improve efficiency across diverse applications [00:16:47]. This approach leverages principles successfully applied in vision and language models, enabling a more scalable and interconnected AI system [00:16:47].

## Benefits of Unified Models

Unified models offer several compelling advantages:
*   **Simplified Systems** They streamline the overall system architecture by consolidating multiple specialized models into a single, comprehensive framework [00:22:11].
*   **Increased Leverage** Improvements made to one part of the unified model can automatically benefit other use cases and downstream applications [00:22:16]. This fosters faster innovation and reduces technical debt [02:27:02].
*   **Cost and Effort Reduction** By replacing numerous bespoke models, unified models significantly lower maintenance costs and engineering effort [00:16:38].
*   **Improved Consistency** Consolidating various prediction tasks into one model, such as query understanding components, can lead to more consistent and accurate results across different scenarios [02:57:30].

However, it's important to note that while unified models offer significant advantages, they may also face "alignment issues" where optimizing for one task negatively impacts another, potentially necessitating a split into a few, rather than a single, unified model [00:22:24].

## Examples of Unified Models

### Stripe: Payments Fraud Model

Stripe has developed a transformer-based payments fraud model that exemplifies a foundational model built on a sequence of payments [00:16:57]. This demonstrates that unified models can be applied beyond traditional recommendation contexts, even to financial transactions, by treating payment sequences as a form of "behavioral data."

### Netflix: Unified Contextual Ranker (Unicorn)

Netflix faced challenges with numerous bespoke models for various personalization needs, including search, similar item recommendations, and pre-query suggestions [00:17:16]. These models, developed independently over years, led to high operational costs and missed opportunities for shared learning [00:17:26].

Netflix's solution, the [[multimodal_models_and_omni_models_development | Unified Contextual Ranker (Unicorn)]], serves as a single model for both search and recommendation ranking [00:17:32].
*   **Architecture** It employs a user foundation model (incorporating user watch history) and a context and relevance model (for video context) [00:17:39].
*   **Unified Input** A key aspect is its ability to take unified input across different use cases, adopting a multi-task learning approach [00:17:53]. Inputs include user ID, item ID, search query (if available), country, and the specific task (e.g., search, pre-query, "more like this") [00:18:08].
*   **Smart Imputation** For tasks like item-to-item recommendations where a search query might be absent, the model intelligently imputes it by using the title of the current item to find similar ones [00:18:27].
*   **Results** The Unicorn model successfully matched or exceeded the metrics of Netflix's specialized models across multiple tasks, while also unifying tech debt and establishing a stronger foundation for future iterations [00:18:48].

Netflix's "big bet" on a foundation model for personalization aims to centralize the learning of user representation [02:27:19]. They hypothesize that scaling up semi-supervised learning can improve personalization, and that this scaling law applies to recommendation systems much like it does to LLMs [02:27:36]. This unified approach allows them to simultaneously improve all downstream, user-facing models [02:27:52].

Netflix's foundation model journey has seen continuous performance gains over two and a half years by scaling up data and model parameters, reaching billions of parameters [02:34:36]. While latency and cost requirements are stringent, they believe the scaling law is not yet exhausted [02:35:08].

Key learnings from LLMs applied to Netflix's foundation model include:
*   **Multi-Token Prediction** Forces the model to be less myopic, more robust to serving time shifts, and focused on long-term user satisfaction rather than just the next action [02:35:36].
*   **Multi-Layer Representation** Improves the quality and stability of user representations [02:36:12].
*   **Long Context Window Handling** Utilizes techniques from LLMs for efficient training and maximizing learning from long user sequences [02:36:34].

The foundation model (FM) consolidates the data and representation layers, particularly for user and content representations, making application-specific models thinner layers built on top of the FM [02:37:15]. FM is consumed through three main patterns: as a subgraph within downstream models, by pushing out embeddings (content and member embeddings) to a centralized store for wider use, and by allowing users to extract and fine-tune models for specific applications [02:37:42]. The incorporation of FM has led to significant AB test wins and infrastructure consolidation, validating Netflix's strategy [02:39:12]. Future directions include universal representation for heterogeneous entities (semantic IDs), generative retrieval for collection recommendations, and faster adaptation through prompt tuning [02:40:23].

### Etsy: Unified Embeddings

Etsy addressed the challenge of providing relevant results for both very specific and very broad queries, especially with its constantly changing inventory [00:19:24]. Traditional lexical embeddings struggled with user preferences and dynamic content [00:19:53].

Their solution involved [[multimodal_models_and_omni_models_development | unified embedding and retrieval]] using a two-tower model architecture [00:20:01]:
*   **Product Encoder** Uses T5 models for text embeddings (item descriptions) and query product logs for query embeddings (mapping queries to clicked/purchased products) [00:20:18].
*   **Query Encoder** Processes search queries [00:20:35].
*   **Shared Encoders** Both towers share encoders for text tokens, product category tokens, and user location, allowing embeddings to match users to product locations [00:20:40].
*   **Personalization** User preferences (past queries, purchases) are encoded via "query user scale effect features" [00:20:57].
*   **Quality Vector** A unique addition is a quality vector (ratings, freshness, conversion rate) concatenated to the product embedding to ensure retrieved items are of good quality [00:21:17]. A constant vector is added to the query embedding to match dimensions for similarity calculations [00:21:38].
*   **Results** This unified embedding approach led to a 2.6% increase in conversion across the entire site and over 5% increase in search purchases [00:21:52], demonstrating that quality, not just quantity, drives significant business impact [00:12:55].

### Pinterest: LLM-Enhanced Search Relevance

Pinterest, a visual discovery platform handling billions of searches across over 45 languages, focused on improving semantic relevance modeling within its search re-ranking stage [00:29:02].
*   **Cross-Encoder Structure** They used a cross-encoder structure where query and pin text are concatenated and passed into an LLM to generate an embedding. This captures interaction between query and pin, which is then fed into an MLP layer to predict relevance on a five-point scale [00:31:09].
*   **Performance** Fine-tuning open-source LLMs with Pinterest's internal data substantially improved relevance prediction performance, with an 8 billion parameter model showing a 20% improvement over a baseline embedding model [00:32:02].
*   **Useful Annotations** Vision-language model generated captions and user actions proved useful for content annotations, enriching the text representation of pins [00:32:50].
*   **Efficiency** To make models more efficient, they employed techniques like distillation (going from larger to smaller models step-by-step), gradual pruning of model layers, and mixed-precision quantization (e.g., using FP32 for the LLM head to maintain prediction precision) [00:33:31]. These efforts resulted in a 7x reduction in latency and a 30x increase in throughput (queries per GPU) [00:37:40].
*   **Benchmarking** Extensive benchmarking (50-60 sets) helps ensure models retain generalization power even after optimization [00:39:03].
*   **Automation** Pinterest emphasizes automation in their system setup, allowing developers to efficiently run experiments by simply changing parameters and leveraging open-source tools integrated for an optimized flow [00:43:26].

### Instacart: LLMs for Search and Discovery

Instacart addressed challenges in grocery e-commerce search, particularly with overly broad or highly specific "tail queries" that lacked sufficient engagement data for traditional models [02:47:41]. They also aimed to improve new item discovery beyond direct search results [02:48:42].

Instacart leveraged LLMs to uplevel their query understanding module, which includes models for normalization, tagging, and classification [02:49:37].
*   **Query-to-Category Classifier** Traditionally, this involved fastText-based neural networks and NPMI co-occurrence models, which struggled with tail queries due to data sparsity [02:50:46]. Initial LLM attempts, though semantically plausible, failed in online AB tests due to a mismatch with Instacart user behavior (e.g., "protein" meaning shakes vs. chicken) [02:51:36]. The solution was to augment the LLM prompt with Instacart's domain knowledge, such as top converting categories for a query or annotations from other query understanding models [02:52:30]. This hybrid approach significantly improved precision (18 percentage points) and recall (70 percentage points) for tail queries [02:53:26].
*   **Query Rewrites Model** This model is crucial for e-commerce, especially for smaller retailers where original queries might yield no results [02:54:10]. LLMs generated precise rewrites (substitute, broad, synonymous), which reduced queries with no results and boosted purchase rates [02:54:49].
*   **Discovery-Oriented Content** LLMs were used to generate substitute items for queries with no exact matches (e.g., "swordfish" suggesting other seafood) and complementary items for highly relevant queries (e.g., "sushi" suggesting Asian cooking ingredients) [02:58:43]. This led to improved engagement and revenue [02:59:51].
*   **Domain Alignment** Crucially, LLMs were augmented with Instacart's domain knowledge (e.g., historical user behavior, top converting categories, query annotations) to align recommendations with user intent and business metrics [03:01:41].
*   **Serving Strategy** To manage latency, Instacart precomputed LLM outputs for head and torso queries offline in batch mode, serving them from a cache. For the long tail, they plan to use a distilled LLM model for online inference [02:56:00].
*   **Challenges** Key challenges included aligning LLM generation with business metrics (revenue), improving the ranking of generated content for user engagement (e.g., diversity-based re-ranking), and rigorously evaluating content for correctness and adherence to product needs (even using LLMs as judges) [03:03:06].
*   **Future** Instacart aims to consolidate multiple query understanding models into a single LLM to improve consistency and leverage user context (e.g., recipe intent) [02:57:30].

## YouTube: Large Recommender Model (LRM)

YouTube, one of the world's largest consumer apps, relies heavily on its recommendation system for watch time across home feeds, watch next, shorts, and personalized search results [03:09:08]. Seeing the transformative potential of Gemini, YouTube developed the [[challenges_and_advancements_in_llmbased_recommendation_models | Large Recommender Model (LRM)]] to adapt Gemini for recommendations [03:10:41].

The recipe for building an LLM-based recommendation system involves three main steps:

1.  **Tokenizing Content:**
    *   Unlike traditional LLMs that tokenize text, YouTube had to develop a way to "tokenize" videos to enable reasoning over many videos [03:12:24].
    *   This led to the creation of [[aigenerated_recommendations_and_user_experience | Semantic ID]] (SID) [03:13:14]. SID works by extracting multimodal features (title, description, transcript, audio, video frames) from a video, embedding them into a multi-dimensional space, and then quantizing them into a unique token using RQVE [03:13:21].
    *   This process organizes the billions of YouTube videos into semantically meaningful tokens, forming a "new language of YouTube videos" [03:13:48]. SIDs allow cold-starting into a semantically meaningful space, improving performance for fresh and tail content [03:27:40].

2.  **Adapting the LLM:**
    *   YouTube continued pre-training the base Gemini checkpoint to understand both English and this new "YouTube language" [03:14:36].
    *   This involves two steps: linking text and SIDs (e.g., training the model to output a video's title given its SID) and training it on sequences of user watches to understand relationships between videos based on engagement [03:14:48].
    *   The outcome is a "bilingual LLM" that can reason across English and YouTube videos, inferring characteristics from SIDs alone [03:16:00].

3.  **Prompting with User Information:**
    *   This bilingual LRM is then used for generative retrieval [03:17:03]. Personalized prompts are constructed with user demographics, context video, and watch history, allowing the model to decode recommended SIDs [03:17:12].
    *   LRM provides unique and interesting recommendations, especially for challenging cases or users with limited data, uncovering connections not found by traditional systems [03:17:45].
    *   To address high serving costs for billions of users, YouTube made LRM more efficient (achieving 95%+ cost savings) and also explored turning it into an offline recommendation problem where unpersonalized recommendations can still be differentiated due to the large pre-trained checkpoint [03:18:36].

**Challenges Unique to LLM-based Recommendation Systems:**
*   **Vocabulary and Corpus Size:** Unlike LLMs with limited vocabularies (e.g., 100,000 words), YouTube has billions of videos with millions added daily, requiring continuous learning [03:20:24].
*   **Freshness:** The immediate relevance of new content (e.g., a new music video) is paramount, necessitating continuous pre-training on the order of days or hours, unlike classical LLM pre-training that occurs less frequently [03:20:51].
*   **Scale:** Serving models to billions of daily active users requires highly efficient, smaller models (e.g., Gemini Flash) to meet latency and scale requirements [03:21:52].

**Future Directions:**
*   LLMs are currently augmenting recommendations invisibly, enhancing quality [03:23:56].
*   Future developments could enable users to steer recommendations through natural language, allow recommenders to explain their suggestions, and blur the lines between search and recommendation [03:24:24].
*   Ultimately, recommendation and generative content might converge, leading to personalized content versions or even AI-created content tailored for individual users [03:25:01].