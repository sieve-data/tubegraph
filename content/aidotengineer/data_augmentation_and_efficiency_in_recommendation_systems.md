---
title: Data augmentation and efficiency in recommendation systems
videoId: 3k4a0PemMu4
---

From: [[aidotengineer]] <br/> 
The integration of large language models (LLMs) and advanced techniques has significantly impacted the efficiency and data quality within recommendation systems. These advancements address long-standing challenges such as cold-start problems, data sparsity, and operational costs.

## Data Augmentation with LLMs
[[Data Collection and Training Techniques for AI Models | Data collection and training techniques for AI Models]] are crucial for machine learning, especially for search and recommendation systems which require high-quality data at scale [00:08:08]. LLMs have proven exceptional at generating synthetic data and labels, offering a cost-effective and high-effort alternative to traditional human annotation or automated methods [00:08:35].

### Indeed: Filtering Bad Job Recommendations
Indeed faced the challenge of users losing trust due to irrelevant job recommendations delivered via email, leading to unsubscribes [00:09:03]. Explicit negative feedback was sparse, and implicit feedback was imprecise [00:09:25].

To address this, Indeed developed a lightweight classifier to filter out poor recommendations [00:09:50]. Their journey involved several steps:
*   **Human Annotation:** Experts initially labeled job recommendations and user pairs based on resume and activity data [00:10:07].
*   **LLM Experimentation:**
    *   Prompting open LLMs (Mistral, Llama 2) yielded poor performance, as they struggled to focus on resume/job description details [00:10:20].
    *   GPT-4 achieved high precision and recall (90%) but was too costly and slow (22 seconds) [00:10:40].
    *   GPT-3.5 showed very poor precision, discarding 37% of good recommendations [00:10:56].
    *   Fine-tuning GPT-2.5 improved precision, was cheaper and faster than GPT-4, but still too slow (6.7 seconds) for online filtering [00:11:30].
*   **Distillation:** They distilled a lightweight classifier using labels from the fine-tuned GPT-2.5 [00:11:53]. This classifier achieved high performance (0.86 AU ROC) and was fast enough for real-time filtering [00:11:58].

This approach reduced bad recommendations by 20%, leading to a 4% increase in application rates and a 5% decrease in unsubscribe rates [00:12:20]. This demonstrated that quality, not just quantity, significantly impacts recommendations [00:12:55].

### Spotify: Growing New Categories
Spotify, traditionally known for music, faced a cold-start problem when introducing new content like podcasts and audiobooks [00:13:24]. They needed to help users discover these new categories and expand beyond music [00:13:34].

Their solution was a query recommendation system [00:13:53]. While conventional techniques generated queries from catalog titles, playlists, and search logs, LLMs were specifically used to generate natural language queries to *augment* these existing methods [00:14:01].

This strategy led to a 9% increase in exploratory queries, meaning one-tenth of Spotify's users began exploring their new products daily, significantly accelerating new product category growth [00:15:13]. The benefits of [[Data Collection and Training Techniques for AI Models | LLM-augmented synthetic data]] include richer, high-quality data at scale, especially for tail queries and items, at a significantly lower cost and effort than human adaptation [00:15:35].

## Efficiency and Scalability in Recommendation Systems
Traditional recommendation systems often suffer from duplicated engineering pipelines, high maintenance costs, and limited knowledge transfer between specialized models for different tasks (e.g., ads, homepage recommendations, search) [00:16:03].

### Unified Models
A solution to these challenges is the adoption of [[unified_models_for_recommendation_systems | unified models]], which consolidate multiple tasks or data streams into a single architecture [00:16:47].

#### Netflix: Unified Contextual Ranker (Unicorn)
Netflix developed a "Unified Contextual Ranker" (Unicorn) to replace bespoke models for search, similar item recommendations, and pre-query recommendations [00:17:14].
*   **Unified Input:** Unicorn accepts unified input data, including user ID, item ID, search query (if applicable), country, and task type [00:17:53]. Missing items (e.g., search query for item-to-item recommendation) are smartly imputed (e.g., using the title of the current item) [00:18:27].
*   **Outcome:** This [[unified_models_for_recommendation_systems | unified model]] was able to match or exceed the metrics of their specialized models across multiple tasks [00:18:48]. This unification reduces technical debt and provides a better foundation for future iterations, enabling faster development [00:19:02].

#### Etsy: Unified Embeddings
Etsy aimed to improve search results for both specific and broad queries while accounting for its constantly changing inventory [00:19:24].
*   **Approach:** They use a two-tower model with a product encoder and a query encoder [00:20:09].
    *   The **product encoder** uses T5 models for text embeddings (item descriptions) and query product logs for query embeddings (queries linked to clicked/purchased products) [00:20:19].
    *   The **query encoder** processes search queries [00:20:35].
    *   Both share encoders for text tokens, product category, and user location, allowing embeddings to match users to product locations [00:20:40].
    *   User preferences are personalized via query user scale effect features [00:20:57].
*   **Quality Integration:** A "quality vector" (ratings, freshness, conversion rate) is concatenated to the product embedding. For the query vector, a constant vector expands its dimension for dot product or cosine similarity [00:21:18].
*   **Results:** This led to a 2.6% increase in conversion across the entire site and over 5% increase in search purchases, demonstrating significant impact for e-commerce [00:21:52].

### LLM Efficiency at Pinterest
Pinterest leveraged LLMs to improve search relevance by creating a classification model that predicts pin relevance to a search query [03:00:18].
*   **Architecture:** They use a cross-encoder structure, concatenating query and pin text into an LLM to get an embedding, which then feeds into an MLP for relevance prediction [03:11:11].
*   **Performance:** LLMs substantially improved relevance prediction compared to in-house baselines. Larger LLMs showed continuous improvement (e.g., 8B L3 model provided 20% improvement over the search stage embedding model) [03:12:10].
*   **Addressing Latency:** To make LLMs efficient for real-time applications (sub-500ms latency), Pinterest employs three levers:
    1.  **Smaller Models (Distillation):** They follow a "go big, then go small" strategy. Starting with a large model (e.g., 150B parameters) to capture complex reasoning, then distilling it into smaller models (e.g., 8B, 3B, 1B) step-by-step [03:33:50]. This gradual distillation is more effective than direct distillation [03:34:16].
    2.  **Pruning:** Reducing the number of heads or MLPs in transformers. Aggressive pruning early on can suffer performance, so gradual pruning (interleaving pruning and distillation) is used to minimize information loss [03:34:45].
    3.  **Quantization:** Leveraging FP8 for activation model parameters. Mixed precision is crucial, with the LLM head (prediction output) remaining in FP32 to maintain precision and calibration [03:36:03].
    4.  **Specification:** Optimizing attention scores, the most expensive part of transformers, by specifying which items attend to others, especially in recommendation scenarios [03:36:53].

These optimizations resulted in a 7x reduction in latency and a 30x increase in throughput (queries per GPU) for Pinterest's search relevance models [03:37:39].

### YouTube: Adapting Gemini for Recommendations
YouTube embarked on building a Large Recommender Model (LRM) by adapting Google's Gemini LLM for video recommendations [03:10:41].
*   **Semantic IDs:** A core innovation is the creation of [[robustness_and_coverage_in_ai_models | semantic IDs]] for videos, moving away from hash-based item IDs which lack content encoding and suffer from cold-start and sparsity issues [00:04:00].
    *   Semantic IDs are generated by extracting multimodal features (title, description, transcript, audio, video frames) from videos, converting them into multi-dimensional embeddings, and then quantizing them into unique tokens [03:13:21].
    *   This organizes billions of YouTube videos into a semantically meaningful "language," allowing the model to understand topics and relationships [03:13:57].
*   **Continued Pre-training:** The Gemini base model is continuously pre-trained to understand both English and this new "YouTube language" [03:14:36]. This involves:
    *   **Linking Text and SIDs:** Training tasks like predicting video titles or creators from SIDs [03:14:48].
    *   **Understanding Watch Sequences:** Masking videos in user watch histories and training the model to predict them, learning relationships between videos based on user engagement [03:15:26].
*   **Generative Retrieval:** The LRM can generate video recommendations by constructing personalized prompts with user demographics, context videos, and watch history [03:17:03]. This yields unique recommendations, particularly for difficult cold-start scenarios [03:17:45].
*   **Challenges:** Training an LLM-based recommendation system presents unique challenges:
    *   **Vocabulary Size:** Billions of videos (compared to ~100k words for English LLMs) with millions added daily [03:20:24].
    *   **Freshness:** New content (e.g., a Taylor Swift music video) must be recommended within minutes/hours, requiring continuous pre-training (daily/hourly) [03:20:51].
    *   **Scale:** Serving to billions of daily active users necessitates focusing on smaller, more efficient LLM checkpoints (like Flash) to meet latency and scale requirements [03:21:52].
*   **Offline Inference:** To manage serving costs, YouTube also leverages LRM for offline inference, creating unpersonalized recommendation tables based on video-to-video relationships. This table can then be quickly looked up for serving, complementing real-time personalization [03:19:13].

## Key Takeaways for LLM-based Recommendation Systems
*   **Tokenize Content:** Create a domain-specific language by tokenizing your content into atomic units with semantic meaning [03:22:28].
*   **Adapt LLM:** Teach the LLM to understand both natural language and your domain-specific language through linking tasks and sequence understanding [03:22:54].
*   **Prompt with User Information:** Construct personalized prompts with user data to build a generative recommendation system [03:23:21].
*   **Domain Knowledge is Key:** Combine LLM world knowledge with specific domain knowledge (e.g., Instacart's user behavior data) for optimal results [03:01:41].
*   **Evaluation:** Robust [[improving_ai_evaluation_methods | evaluation methods]] are critical to ensure LLM outputs are accurate, align with business metrics, and enhance user experience [03:03:13]. The use of LLMs as judges can be part of this process [03:04:30].
*   **Cost and Latency:** LLMs can be expensive and slow. Strategies like distillation, pruning, quantization, and careful serving architectures (e.g., offline pre-computation, caching) are essential for deployment at scale [03:18:48].
*   **Future Directions:** The future of recommendations with LLMs includes:
    *   Universal representation for heterogeneous entities [[robustness_and_coverage_in_ai_models | Robustness and coverage in AI models]] [02:40:23].
    *   Generative retrieval for collections [02:40:40].
    *   Faster adaptation through prompt tuning [02:40:57].
    *   User-steerable recommendations, with explanations and goal alignment [03:24:35].
    *   Blurring lines between search and recommendations [03:24:52].
    *   The potential for LLMs to generate personalized content directly [03:25:01].