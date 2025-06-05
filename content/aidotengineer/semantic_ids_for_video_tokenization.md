---
title: Semantic IDs for video tokenization
videoId: 3k4a0PemMu4
---

From: [[aidotengineer]] <br/> 

Language modeling techniques have been integrated into recommendation systems since 2013, initially by learning item embeddings from co-occurrences in user interaction sequences, and later evolving with GRU4Rec for short-term prediction and Transformers for long-range dependencies <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Today, a key advancement is the use of Semantic IDs to enhance recommendation systems, particularly for video content <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

## Challenges with Hash-Based Item IDs

Traditional recommendation systems often rely on hash-based item IDs, which present several challenges <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>:
*   **Lack of Content Encoding**: Hash-based IDs do not inherently encode the content of the item itself <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
*   **Cold-Start Problem**: When a new item is introduced, the system must relearn about it entirely, leading to poor recommendations until sufficient interaction data is collected <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Sparsity**: Many items, especially those in the "long tail," have very few interactions (e.g., 1-10), making it difficult to learn effective representations <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Popularity Bias**: Recommendation systems tend to favor popular items, struggling to recommend new or niche content due to cold start and sparsity <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.

## Semantic IDs as a Solution

Semantic IDs address these issues by embedding items based on their content, often leveraging multimodal data <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. This allows recommendations to inherently "understand" the content of the items, improving cold-start coverage and enabling human-readable explanations for recommendations <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

### Quao's Trainable Multimodal Semantic IDs

Quao, a short-video platform similar to TikTok, faced the challenge of learning from hundreds of millions of daily video uploads <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>. Their solution involved trainable multimodal semantic IDs to combine static content embeddings with dynamic user behavior <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

**Model Architecture**
Quao utilized a standard two-tower network, with separate embedding layers for users and items <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. The key innovation was integrating content input through specialized encoders <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>:
*   **Visual Content**: Encoded using ResNet <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.
*   **Video Descriptions**: Encoded using BERT <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
*   **Audio Content**: Encoded using VGGish <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>.

**Encoding and Clustering**
To enable backpropagation and update these encoder model embeddings, Quao concatenated all content embeddings <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>. They then learned cluster IDs using k-means clustering; for example, 100 million short videos were grouped into 1,000 clusters <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>. These trainable cluster IDs were mapped to their own embedding tables, allowing the model encoder to learn to map the content space (via cluster IDs) to the behavioral space during training <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

**Results**
Quao's semantic IDs not only outperformed regular hash-based IDs in terms of clicks and likes but also significantly improved cold-start metrics <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>:
*   **Cold-Start Coverage**: Increased by 3.6%, meaning more new videos were shown <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   **Cold-Start Velocity**: Increased by a notable margin (specific threshold not shared), indicating new videos reached view thresholds faster <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### YouTube's Large Recommender Model (LRM)

YouTube adapted Google's Gemini LLM to create a Large Recommender Model (LRM), aimed at revolutionizing video recommendations <a class="yt-timestamp" data-t="03:10:43">[03:10:43]</a>. This model operates by treating videos as tokens, similar to how LLMs process text tokens <a class="yt-timestamp" data-t="03:12:44">[03:12:44]</a>.

**Video Tokenization with Semantic IDs**
To enable the LRM to reason over large numbers of videos, YouTube developed Semantic IDs, which were presented at Rexus <a class="yt-timestamp" data-t="03:13:14">[03:13:14]</a>.
1.  **Feature Extraction**: Videos are analyzed to extract various features, including title, description, transcript, and even [[audio_token_representation_and_codebooks | audio]] and video frame-level data <a class="yt-timestamp" data-t="03:13:25">[03:13:25]</a>.
2.  **Multidimensional Embedding**: These features are combined into a rich, multidimensional embedding <a class="yt-timestamp" data-t="03:13:33">[03:13:33]</a>.
3.  **Quantization**: The embedding is then quantized using Residual Quantized Vector Embedding (RQVE) to assign a unique, atomic token to each video <a class="yt-timestamp" data-t="03:13:36">[03:13:36]</a>. This process transforms videos into "atomic units for a new language of YouTube videos" <a class="yt-timestamp" data-t="03:13:48">[03:13:48]</a>.

This system organizes the billions of videos on YouTube into semantically meaningful tokens. For instance, topics like music, gaming, or sports would be represented by initial tokens, with further tokens specializing down to specific sub-genres or events (e.g., sports -> volleyball) <a class="yt-timestamp" data-t="03:14:04">[03:14:04]</a>. This represents a significant shift from hash-based to semantically meaningful tokenization <a class="yt-timestamp" data-t="03:14:25">[03:14:25]</a>.

**Continued Pre-training**
The LRM undergoes continuous pre-training to understand both English and this new "YouTube language" <a class="yt-timestamp" data-t="03:14:36">[03:14:36]</a>. This involves two main steps:
1.  **Linking Text and SID**: The model learns to associate text (like titles or creator names) with specific video Semantic IDs <a class="yt-timestamp" data-t="03:14:48">[03:14:48]</a>. For example, prompting "This video has title XYZ" trains the model to output the title for a given Semantic ID <a class="yt-timestamp" data-t="03:15:08">[03:15:08]</a>.
2.  **Understanding Watch Sequences**: The model is trained on sequences of user watches, predicting masked videos within a sequence to learn relationships based on user engagement <a class="yt-timestamp" data-t="03:15:26">[03:15:26]</a>. This helps the model understand which videos are watched together <a class="yt-timestamp" data-t="03:15:51">[03:15:51]</a>.

Through these tasks, the LRM develops the ability to reason across both English and YouTube videos. For example, given a series of video SIDs, it can infer the topic of a new video based solely on its Semantic ID <a class="yt-timestamp" data-t="03:16:04">[03:16:04]</a>.

**Generative Retrieval and Recommendations**
The LRM can be used for generative retrieval by constructing personalized prompts for each user, including their demographics, context videos, and watch history <a class="yt-timestamp" data-t="03:17:03">[03:17:03]</a>. The model then decodes video recommendations as SIDs <a class="yt-timestamp" data-t="03:17:37">[03:17:37]</a>. This approach yields unique and interesting recommendations, particularly for challenging recommendation tasks or users about whom less is known <a class="yt-timestamp" data-t="03:17:45">[03:17:45]</a>.

**Challenges and Optimizations**
While powerful, the LRM is expensive to serve at YouTube's scale (billions of users) <a class="yt-timestamp" data-t="03:18:36">[03:18:36]</a>. Significant effort went into reducing TPU serving costs, achieving over 95% savings <a class="yt-timestamp" data-t="03:19:01">[03:19:01]</a>.

Key challenges include:
*   **Vocabulary Size**: YouTube's corpus of 20 billion videos (with millions added daily) dwarfs the vocabulary of traditional English LLMs (around 100,000 words) <a class="yt-timestamp" data-t="03:20:24">[03:20:24]</a>.
*   **Freshness**: New content (e.g., a Taylor Swift music video) must be recommended within minutes or hours, requiring continuous pre-training on the order of days or hours, unlike the months-long pre-training cycles of classical LLMs <a class="yt-timestamp" data-t="03:20:51">[03:20:51]</a>.
*   **Scale and Efficiency**: YouTube must focus on smaller, more efficient models (like Gemini Flash) to meet latency and scale requirements for billions of daily active users <a class="yt-timestamp" data-t="03:21:52">[03:21:52]</a>.

To address serving costs, YouTube also developed an offline recommendations table. By performing offline inference on the head of the video corpus (which accounts for much watch time) using the LRM without personalized elements, a simple lookup table can serve recommendations <a class="yt-timestamp" data-t="03:19:13">[03:19:13]</a>. This "unpersonalized" model, due to its foundation on a large Gemini checkpoint, still provides differentiated recommendations <a class="yt-timestamp" data-t="03:19:40">[03:19:40]</a>.

### LLM and Rexus Recipe

The process of building an LLM-based recommendation system can be summarized in three steps <a class="yt-timestamp" data-t="03:22:25">[03:22:25]</a>:
1.  **Tokenize Content**: Create an "essence" of content into an atomic token by building a rich representation (features), forming an embedding, and then quantizing it <a class="yt-timestamp" data-t="03:22:50">[03:22:50]</a>. This effectively creates a domain-specific language.
2.  **Adapt the LLM**: Link English with the newly created domain language through training tasks that enable reasoning across both <a class="yt-timestamp" data-t="03:22:57">[03:22:57]</a>. The outcome is a bilingual LLM that understands both natural language and the domain-specific token language.
3.  **Prompt with User Information**: Construct personalized prompts using user demographics, activity, and actions <a class="yt-timestamp" data-t="03:23:21">[03:23:21]</a>. Train task-specific or surface-specific models to create a generative recommendation system on top of the LLM <a class="yt-timestamp" data-t="03:23:36">[03:23:36]</a>.

## Future Directions

[[Next token prediction in AI | Next token prediction in AI]] models, specifically LLMs, are poised to transform recommendation systems even further <a class="yt-timestamp" data-t="03:23:50">[03:23:50]</a>:
*   **Augmented but Invisible**: Currently, LLMs primarily augment recommendations, improving quality largely invisibly to users <a class="yt-timestamp" data-t="03:23:58">[03:23:58]</a>.
*   **Interactive Experiences**: In the near future, users may be able to talk to recommendation systems in natural language, steer recommendations to their goals, and receive explanations for why a candidate was recommended <a class="yt-timestamp" data-t="03:24:26">[03:24:26]</a>. This will blur the lines between search and recommendation <a class="yt-timestamp" data-t="03:24:52">[03:24:52]</a>.
*   **Generative Content**: Ultimately, recommendations may evolve to include generative content, where a personalized version of content is recommended, or even entirely new content is created for the user <a class="yt-timestamp" data-t="03:25:01">[03:25:01]</a>.

## Cold-Start for Semantic IDs

The training process for Semantic IDs is entirely unsupervised, as the system makes its own quantization of the video corpus <a class="yt-timestamp" data-t="03:27:17">[03:27:17]</a>. This enables the model to learn concepts (e.g., sports vs. movies) without explicit instruction <a class="yt-timestamp" data-t="03:27:30">[03:27:30]</a>. Semantic IDs effectively warm-start new content into a semantically meaningful space, leading to improved performance for fresh or "tail" videos uploaded recently <a class="yt-timestamp" data-t="03:27:40">[03:27:40]</a>.