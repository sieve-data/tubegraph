---
title: Challenges and advancements in LLMbased recommendation models
videoId: 3k4a0PemMu4
---

From: [[aidotengineer]] <br/> 
## Challenges and Advancements in LLM-Based Recommendation Models

The integration of Large Language Models (LLMs) with recommendation systems (Rex) marks a significant shift in how personalized experiences are delivered. This evolving field addresses long-standing challenges in Rex through novel applications of LLM capabilities <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Key areas of focus include semantic IDs, data augmentation, and [[unified_models_for_recommendation_systems | unified models]] <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Semantic IDs: Understanding Content Beyond Hashes

Traditionally, recommendation systems rely on hash-based item IDs, which do not inherently encode content information <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>. This leads to several problems:
*   **Cold-start problem**: New items require relearning their properties <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Sparsity**: Long-tail items with few interactions are difficult to learn from <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Popularity bias**: Systems struggle with cold-start items and sparsity, favoring popular items <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

**Advancement**: [[semantic_ids_in_llm_based_recommendation_systems | Semantic IDs]] offer a solution by encoding item content, potentially involving multimodal data <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

#### Kuaishou's Multimodal Semantic IDs
Kuaishou, a short video platform, faced the challenge of learning from hundreds of millions of daily video uploads <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. Their approach involved trainable multimodal semantic IDs:
*   They combine static content embeddings (visual from ResNet, video descriptions from BERT, audio from VGGish) with dynamic user behavior <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   Content embeddings are concatenated <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   Cluster IDs are learned via k-means clustering (e.g., 1,000 clusters from 100 million videos) <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   A "motor encoder" learns to map the content space, via cluster IDs and an embedding table, to the behavioral space <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

**Outcome**: These semantic IDs not only outperform hash-based IDs on clicks and likes but significantly increase cold-start coverage (3.6%) and cold-start velocity <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. This means recommendations can understand content and even provide human-readable explanations <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

### Data Augmentation and Efficiency: Leveraging LLMs for Quality Data

High-quality data at scale is crucial for search and recommendation systems <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   Traditional methods like human annotations are costly and high-effort <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   Implicit feedback is often imprecise <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>.

**Advancement**: LLMs excel at generating synthetic data and labels, offering a solution to these data challenges <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

#### Indeed's Lightweight Classifier for Job Recommendations
Indeed faced the issue of poor job recommendations leading to user dissatisfaction and unsubscribes <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Challenge**: Explicit negative feedback was sparse <a class="yt-timestamp" data-t="00:09:28">[00:09:28]</a>.
*   **Solution**: A lightweight classifier to filter bad recommendations <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>.
*   **Process**:
    *   Experts labeled job recommendations and user pairs <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
    *   Prompting open LLMs (Mistral, LLaMA 2) yielded poor performance <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
    *   GPT-4 performed well (90% precision and recall) but was costly and too slow (22 seconds) <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   GPT-3.5 had very poor precision (63%) <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
    *   Fine-tuning GPT-2.5 achieved desired precision but was still too slow for online filtering (6.7 seconds) <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
    *   Finally, they distilled a lightweight classifier using fine-tuned GPT-2.5 labels, achieving high performance (0.86 AU ROC) and real-time suitability <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
*   **Outcome**: Reduced bad recommendations by 20%, increased application rate by 4%, and decreased unsubscribe rate by 5% <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a>. This highlighted that quality over quantity in recommendations makes a significant difference <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>.

#### Spotify's Query Recommendation System
Spotify aimed to grow new content categories like podcasts and audiobooks, facing a cold-start problem not just on items but on categories <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>.
*   **Solution**: A query recommendation system <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.
*   **Process**:
    *   Traditional techniques extracted ideas from catalog/playlist titles and search logs <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
    *   LLMs were used to generate natural language queries, augmenting existing methods <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
*   **Outcome**: +9% in exploratory queries, meaning one-tenth of users were exploring new products daily, significantly accelerating new product category growth <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>.

**Benefit**: LLM-augmented synthetic data provides richer, high-quality data at scale, even for tail queries and items, at a much lower cost than human annotation <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

### Unified Models: Streamlining Recommendation Systems

Traditional companies often have separate, bespoke systems for ads, recommendations, and search, with different models even within recommendations for various surfaces (e.g., homepage, item page) <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>.
*   **Challenge**: Duplicative engineering pipelines, high maintenance costs, and improvements in one model not transferring to others <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.

**Advancement**: [[unified_models_for_recommendation_systems | Unified models]], inspired by vision and language domains, address these inefficiencies <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

#### Netflix's Unified Contextual Ranker (Unicorn)
Netflix faced high operational costs due to bespoke models for search, similar item recommendations, and pre-query recommendations <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
*   **Solution**: A unified contextual ranker (Unicorn) <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
*   **Process**: It uses a user foundation model and a context and relevance model with unified input (user ID, item ID, search query, country, task) <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>. Smart imputation handles missing items, for instance, by using the current item's title as a search query <a class="yt-timestamp" data-t="00:18:27">[00:18:27]</a>.
*   **Outcome**: The unified model matched or exceeded the metrics of specialized models on multiple tasks, leading to infrastructure consolidation and faster iteration <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.

#### Etsy's Unified Embeddings
Etsy aimed to provide better results for both specific and broad queries despite its constantly changing inventory <a class="yt-timestamp" data-t="00:19:24">[00:19:24]</a>.
*   **Challenge**: Lexical embeddings didn't account for user preferences <a class="yt-timestamp" data-t="00:19:53">[00:19:53]</a>.
*   **Solution**: Unified embedding and retrieval <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>.
*   **Process**: A product encoder (using T5 for text embeddings and query-product logs) and a query encoder share token, product category, and user location encoders <a class="yt-timestamp" data-t="00:20:18">[00:20:18]</a>. User preferences are encoded via query-user scale effect features <a class="yt-timestamp" data-t="00:20:59">[00:20:59]</a>. A "quality vector" (ratings, freshness, conversion rate) is concatenated to the product embedding <a class="yt-timestamp" data-t="00:21:22">[00:21:22]</a>.
*   **Outcome**: 2.6% increase in conversion across the entire site and over 5% increase in search purchases <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.

**Benefits**: Unified models simplify systems, and improvements in one part of the model transfer to other use cases <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>. However, misalignment can occur, potentially requiring multiple unified models <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.

### LLM-Based Search Relevance and Efficiency: Pinterest's Approach

Pinterest, handling over six billion searches monthly across billions of pins and 45+ languages, uses LLMs for semantic relevance modeling in the reranking stage <a class="yt-timestamp" data-t="00:29:04">[00:29:04]</a>.

**Advancements**:
*   **Relevance Prediction**: A cross-encoder structure concatenates query and pin text, passing them to an LLM to get an embedding. This embedding is then fed into an MLP layer for five relevance levels <a class="yt-timestamp" data-t="00:31:11">[00:31:11]</a>. Fine-tuning open-source LLMs with Pinterest data substantially improves performance, with larger models yielding greater gains (e.g., 12% improvement over multilingual BERT) <a class="yt-timestamp" data-t="00:32:17">[00:32:17]</a>.
*   **Content Annotations**: Vision-language model-generated captions and user actions provide useful content annotations for text representation of pins <a class="yt-timestamp" data-t="00:32:54">[00:32:54]</a>.
*   **Efficiency**: To address latency (e.g., 500-400 ms) and throughput requirements <a class="yt-timestamp" data-t="00:33:26">[00:33:26]</a>, Pinterest employs:
    *   **Distillation**: Start with a larger model (e.g., 150 billion parameters) and gradually distill it into smaller models (e.g., 8B, 3B, 1B) <a class="yt-timestamp" data-t="00:34:08">[00:34:08]</a>. This step-by-step approach is more effective than direct distillation <a class="yt-timestamp" data-t="00:34:17">[00:34:17]</a>.
    *   **Pruning**: Gradually reduce redundancy in transformer models (e.g., number of heads, MLPs) <a class="yt-timestamp" data-t="00:34:55">[00:34:55]</a>. Aggressive pruning can lead to significant quality reduction <a class="yt-timestamp" data-t="00:35:20">[00:35:20]</a>.
    *   **Quantization**: Use lower precision (e.g., FP8) for activations and parameters, but maintain FP32 for the LM head to preserve prediction precision and calibration <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
    *   **Sparsification**: Specify attention scores, preventing every item from attending to every other item, especially for recommended items in a sequence <a class="yt-timestamp" data-t="00:37:03">[00:37:03]</a>.

**Outcome**: These optimizations resulted in a 7x reduction in latency and a 30x increase in throughput (queries per GPU) <a class="yt-timestamp" data-t="00:37:51">[00:37:51]</a>.

### Netflix's Foundational Model for Personalization

Netflix has made a "big bet" on using one foundational model to cover all recommendation use cases <a class="yt-timestamp" data-t="02:23:26">[02:23:26]</a>.

**Challenges of Traditional Systems**:
*   **Diverse Needs**: Netflix has varied recommendation requirements across rows (genres, new/trending, Netflix originals), items (movies, TV shows, games, live streaming), and pages (homepage, search, kids' homepage, mobile feed) <a class="yt-timestamp" data-t="02:23:48">[02:23:48]</a>.
*   **Many Specialized Models**: Historically, this led to numerous independently built models, each with different objectives and significant overlap, resulting in duplications in feature/label engineering <a class="yt-timestamp" data-t="02:24:52">[02:24:52]</a>.
*   **Scalability**: Spinning up new models for each use case is unsustainable and hinders innovation velocity <a class="yt-timestamp" data-t="02:26:32">[02:26:32]</a>.

**Advancement**: Centralizing user representation learning through a transformer-based foundation model <a class="yt-timestamp" data-t="02:27:19">[02:27:19]</a>.

**Hypotheses**:
1.  **Scaling Law**: Scaling up semi-supervised learning can improve personalization, akin to LLM scaling laws <a class="yt-timestamp" data-t="02:27:36">[02:27:36]</a>.
2.  **High Leverage**: Integrating the foundation model into all systems can simultaneously improve downstream, canvas-facing models <a class="yt-timestamp" data-t="02:27:49">[02:27:49]</a>.

**Data and Training Considerations**:
*   **Tokenization**: Crucial decision for model quality <a class="yt-timestamp" data-t="02:28:44">[02:28:44]</a>. Unlike language tokens, each "token" in a recommendation context is an interaction event with many facets (when, where, what) <a class="yt-timestamp" data-t="02:29:21">[02:29:21]</a>.
*   **Event Representation**: Break down events by time, location, device, canvas, target entity, and interaction details <a class="yt-timestamp" data-t="02:30:31">[02:30:31]</a>.
*   **Embedding Feature Transformation**: Combine ID embedding learning with semantic content information to address the cold-start problem (not an issue for LLMs but critical for Rex) <a class="yt-timestamp" data-t="02:31:28">[02:31:28]</a>.
*   **Transformer Layer**: Hidden state output serves as a long-term user representation. Stability and aggregation methods (across time/layers) are key <a class="yt-timestamp" data-t="02:32:10">[02:32:10]</a>.
*   **Objective/Loss Function**: Richer than LLMs, as multiple sequences can represent output (entity IDs, action types, metadata, duration, next play time) <a class="yt-timestamp" data-t="02:33:06">[02:33:06]</a>. This allows for multitask learning or using targets as weights/rewards <a class="yt-timestamp" data-t="02:34:01">[02:34:01]</a>.

**Scaling Results**: The foundation model demonstrated continuous gains over two-and-a-half years, scaling from millions of profiles to billions of parameters <a class="yt-timestamp" data-t="02:34:38">[02:34:38]</a>. Latency/cost requirements necessitate distillation for larger models <a class="yt-timestamp" data-t="02:35:08">[02:35:08]</a>.

**Learnings from LLMs**:
*   **Multi-token prediction**: Forces the model to be less myopic, more robust to serving time shifts, and targets long-term user satisfaction <a class="yt-timestamp" data-t="02:35:36">[02:35:36]</a>.
*   **Multi-layer representation**: Techniques like layer-wise supervision and self-distillation lead to better, more stable user representations <a class="yt-timestamp" data-t="02:36:12">[02:36:12]</a>.
*   **Long context window handling**: Utilizes techniques like truncated sliding windows, sparse attention, and progressive training <a class="yt-timestamp" data-t="02:36:34">[02:36:34]</a>.

**Application and Serving**:
*   The foundation model (FM) consolidates data and representation layers (user and content) <a class="yt-timestamp" data-t="02:37:15">[02:37:15]</a>.
*   Application models become thinner layers built on top of FM <a class="yt-timestamp" data-t="02:37:30">[02:37:30]</a>.
*   **Consumption Patterns**:
    1.  FM integrated as a subgraph within downstream models <a class="yt-timestamp" data-t="02:37:48">[02:37:48]</a>.
    2.  Push out embeddings (content and member) to a centralized store for wider use <a class="yt-timestamp" data-t="02:38:17">[02:38:17]</a>.
    3.  Extract and fine-tune/distill models for specific applications to meet online serving requirements <a class="yt-timestamp" data-t="02:38:55">[02:38:55]</a>.

**Wins**: High leverage of FM leads to AB test gains and infrastructure consolidation, validating the big bet. It provides a scalable solution, higher leverage, and faster innovation velocity <a class="yt-timestamp" data-t="02:39:12">[02:39:12]</a>.

**Current Directions**:
*   Universal representation for heterogeneous entities ([[semantic_ids_in_llm_based_recommendation_systems | semantic ID]]) <a class="yt-timestamp" data-t="02:40:23">[02:40:23]</a>.
*   Generative retrieval for collection recommendation (multi-step decoding) <a class="yt-timestamp" data-t="02:40:40">[02:40:40]</a>.
*   Faster adaptation through prompt tuning (training soft tokens) <a class="yt-timestamp" data-t="02:40:59">[02:40:59]</a>.

### Instacart's LLM-Powered Search and Discovery

Instacart uses LLMs to transform search and discovery for grocery e-commerce, where customers have long shopping lists and seek both restocking and new product discovery <a class="yt-timestamp" data-t="02:46:17">[02:46:17]</a>.

**Challenges of Conventional Search Engines**:
*   **Overly Broad Queries**: E.g., "snacks," where engagement data is hard to collect for long-tail products <a class="yt-timestamp" data-t="02:47:48">[02:47:48]</a>.
*   **Very Specific Queries**: E.g., "unsweetened plant-based yogurt," where sparse data limits model training <a class="yt-timestamp" data-t="02:48:12">[02:48:12]</a>.
*   **New Item Discovery**: Difficulty in surfacing related products or enabling exploratory browsing, leading to dead ends <a class="yt-timestamp" data-t="02:48:43">[02:48:43]</a>.

**Advancements**: LLMs enhance query understanding and enable discovery-oriented content.

#### Query Understanding: Enhancing Accuracy
Instacart's query understanding module includes models for normalization, tagging, and classification <a class="yt-timestamp" data-t="02:49:59">[02:49:59]</a>.
*   **Query-to-Category Classifier**: Maps a query to relevant categories (multilabel problem, 10,000 labels) <a class="yt-timestamp" data-t="02:50:16">[02:50:16]</a>.
    *   **Traditional Challenge**: FastText and NPMI models struggled with low coverage for tail queries due to lack of engagement data <a class="yt-timestamp" data-t="02:51:15">[02:51:15]</a>.
    *   **LLM Approach**: Initially, raw LLM predictions were decent but mismatched Instacart user behavior (e.g., "protein" for chicken vs. protein shakes) <a class="yt-timestamp" data-t="02:51:38">[02:51:38]</a>.
    *   **Hybrid Approach**: Augmented the prompt with Instacart's domain knowledge (e.g., top converting categories, query annotations like brands/dietary attributes) <a class="yt-timestamp" data-t="02:52:34">[02:52:34]</a>.
    *   **Outcome**: Significant improvements for tail queries: 18 percentage points increase in precision, 70 percentage points increase in recall <a class="yt-timestamp" data-t="02:53:29">[02:53:29]</a>.
*   **Query Rewrites Model**: Generates broader or synonymous queries to ensure results even with small retailer catalogs <a class="yt-timestamp" data-t="02:54:10">[02:54:10]</a>.
    *   **LLM Approach**: Similar to category classification, LLMs generate precise rewrites (substitute, broad, synonymous) <a class="yt-timestamp" data-t="02:54:51">[02:54:51]</a>.
    *   **Outcome**: Offline improvements in human evaluation and a significant drop in queries without any results online <a class="yt-timestamp" data-t="02:55:19">[02:55:19]</a>.

**Serving Strategy**: Precompute outputs for head and torso queries offline in batch mode and cache them for low-latency serving. Fallback to existing models (or distilled LLMs) for the long tail <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.

**Future Direction**: Consolidate multiple query understanding models into a single LLM for consistency and pass extra context (e.g., user mission like recipe ingredients) <a class="yt-timestamp" data-t="02:57:30">[02:57:30]</a>.

#### Discovery-Oriented Content: Enhancing User Experience
Instacart aimed to make search results pages more useful after an item is added to the cart, by showing complementary or substitute items <a class="yt-timestamp" data-t="02:58:43">[02:58:43]</a>.
*   **Traditional Challenge**: Required extensive feature engineering or manual work <a class="yt-timestamp" data-t="02:59:08">[02:59:08]</a>.
*   **LLM Approach**: Instruct LLM to act as an AI assistant generating complementary and substitute shopping lists <a class="yt-timestamp" data-t="03:00:40">[03:00:40]</a>.
    *   Initial LLM common-sense answers didn't align with user behavior (e.g., "protein" for chicken vs. protein bars) <a class="yt-timestamp" data-t="03:01:17">[03:01:17]</a>.
    *   **Improved Approach**: Augmented prompts with Instacart domain knowledge (top converting categories, query annotations, subsequent user queries) <a class="yt-timestamp" data-t="03:01:41">[03:01:41]</a>.
*   **Outcome**: Significantly improved engagement and revenue per search <a class="yt-timestamp" data-t="02:59:53">[02:59:53]</a>.

**Serving Strategy**: Precompute LLM-generated content for historical search logs in batch mode and store it for quick lookup <a class="yt-timestamp" data-t="03:02:29">[03:02:29]</a>.

**Key Challenges in Implementation**:
1.  Aligning generation with business metrics like revenue <a class="yt-timestamp" data-t="03:03:16">[03:03:16]</a>.
2.  Improving ranking of generated content, often requiring diversity-based reranking <a class="yt-timestamp" data-t="03:03:28">[03:03:28]</a>.
3.  [[LM_evaluation_challenges | Evaluating LLM-generated content]] for correctness (no hallucination) and adherence to product needs (using LLM as a judge) <a class="yt-timestamp" data-t="03:03:45">[03:03:45]</a>.

**Overall Takeaways**: LLM world knowledge improves query understanding for tail queries. Success comes from combining domain knowledge with LLMs. Robust evaluation is crucial <a class="yt-timestamp" data-t="03:04:02">[03:04:02]</a>.

### YouTube's Large Recommender Model (LRM)

YouTube aims to transform its recommendation system by adapting Gemini, a large language model, to recommend videos. Over 70% of YouTube's watch time is driven by its recommendation system <a class="yt-timestamp" data-t="03:09:08">[03:09:08]</a>.

**Problem**: Learning a function that takes user and context as input to provide recommendations <a class="yt-timestamp" data-t="03:09:44">[03:09:44]</a>.

**Advancement**: The Large Recommender Model (LRM) adapts Gemini for YouTube recommendations <a class="yt-timestamp" data-t="03:11:43">[03:11:43]</a>.

**Recipe for LLM-Based Rex**:
1.  **Tokenize Content (Semantic ID)**:
    *   **Goal**: Create atomic units for a new "language" of YouTube videos <a class="yt-timestamp" data-t="03:13:48">[03:13:48]</a>.
    *   **Process**: Extract features (title, description, transcript, audio, video frames) from a video, combine into a multi-dimensional embedding, then quantize using RQVA to assign each video a [[semantic_ids_in_llm_based_recommendation_systems | semantic ID]] (SID) <a class="yt-timestamp" data-t="03:13:21">[03:13:21]</a>.
    *   **Outcome**: A semantically meaningful tokenization where related videos share common prefixes (e.g., sports -> volleyball) <a class="yt-timestamp" data-t="03:14:04">[03:14:04]</a>.
2.  **Adapt the LLM (Continued Pre-training)**:
    *   **Goal**: Teach the LLM to understand both English and this new YouTube language <a class="yt-timestamp" data-t="03:14:39">[03:14:39]</a>.
    *   **Tasks**:
        *   **Linking Text and SID**: Prompt the model with a video's SID and ask it to output its title, creator, or topics <a class="yt-timestamp" data-t="03:14:48">[03:14:48]</a>.
        *   **Understanding Watch Sequences**: Prompt with user watch history (video SIDs), mask some, and train the model to predict them, learning relationships based on user engagement <a class="yt-timestamp" data-t="03:15:26">[03:15:26]</a>.
    *   **Outcome**: A "bilingual" LLM that can reason across English and YouTube videos <a class="yt-timestamp" data-t="03:16:00">[03:16:00]</a>.
3.  **Prompt with User Information (Generative Retrieval)**:
    *   **Goal**: Generate personalized recommendations <a class="yt-timestamp" data-t="03:17:03">[03:17:03]</a>.
    *   **Process**: Construct a prompt with user demographics, context video, and watch history <a class="yt-timestamp" data-t="03:17:12">[03:17:12]</a>.
    *   **Outcome**: Yields unique and interesting recommendations, especially for hard cases (e.g., finding women's track races related to men's Olympic highlights) <a class="yt-timestamp" data-t="03:17:45">[03:17:45]</a>.

**Challenges in LLM-Based Rex (YouTube's Perspective)**:
*   **Vocabulary and Corpus Size**: Billions of YouTube videos compared to 100,000 words in English vocabulary <a class="yt-timestamp" data-t="03:20:44">[03:20:44]</a>.
*   **Freshness**: Millions of videos added daily require continuous pre-training (on the order of days/hours) to recommend new, relevant content immediately (e.g., Taylor Swift's new music video) <a class="yt-timestamp" data-t="03:20:51">[03:20:51]</a>, unlike classical LLM pre-training which is less frequent <a class="yt-timestamp" data-t="03:21:40">[03:21:40]</a>.
*   **Scale and Serving Cost**: Large LLMs like Gemini Pro are too expensive for billions of daily active users; smaller, efficient models (e.g., Flash) are needed to meet latency and scale requirements, often after significant cost reduction efforts (e.g., 95%+ savings) <a class="yt-timestamp" data-t="03:21:52">[03:21:52]</a>.
*   **Balancing Language Capability**: Training on semantic IDs can cause the model to "forget" English, requiring strategies like Mixture of Experts <a class="yt-timestamp" data-t="03:25:50">[03:25:50]</a>.

**Solution for Serving Costs**: Turn it into an offline problem by removing personalized aspects from the prompt, building an offline recommendations table for popular videos. This allows simple lookup for serving <a class="yt-timestamp" data-t="03:19:10">[03:19:10]</a>.

### Future Directions for LLM and Rexus

*   **Augmentation to Interaction**: LLMs currently augment recommendations invisibly, enhancing quality <a class="yt-timestamp" data-t="03:23:58">[03:23:58]</a>. The future involves interactive experiences where users can steer recommendations using natural language, receive explanations for recommendations, and align them with their goals <a class="yt-timestamp" data-t="03:24:28">[03:24:28]</a>.
*   **Blurring Search and Recommendation**: The lines between these two domains will blur <a class="yt-timestamp" data-t="03:24:52">[03:24:52]</a>.
*   **Generative Content**: Recommendations may evolve to personalized versions of content, and eventually, the system might even create content tailored for the user (end-of-one content) <a class="yt-timestamp" data-t="03:25:01">[03:25:01]</a>.

These advancements highlight a dynamic field where LLMs are not just improving existing recommendation paradigms but enabling entirely new capabilities and experiences.