---
title: Data augmentation techniques in AI
videoId: 3k4a0PemMu4
---

From: [[aidotengineer]] <br/> 

Data augmentation is a crucial area of focus in artificial intelligence, particularly in the realm of recommendation systems and search. The goal is to address inherent challenges related to data quality, sparsity, and the "cold-start" problem, especially for new items or infrequent queries. <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>

## The Challenge: Data Scarcity and Quality

The "lifeblood of machine learning is data" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a> – specifically, good quality data at scale. <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a> This is essential for search and recommendation systems, which require extensive metadata, query expansion, synonyms, and spell checking attached to the search index. <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a> Historically, obtaining this data has been costly and high-effort, often relying on human annotations or complex automatic methods. <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>

Recommendation systems often suffer from:
*   **Cold-start problem** <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>: When a new item is introduced, the system must relearn about it from scratch. <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
*   **Sparsity** <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>: Many "tail items" have very few interactions (e.g., one or two, up to ten), which is insufficient for effective learning. <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>
*   **Popularity bias** <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>: Systems tend to struggle with cold-start and sparsity, favoring popular items. <a class="yt-timestamp" data-t="00:04:34">[00:04:34]</a>

## Leveraging Large Language Models (LLMs) for Data Augmentation

Large Language Models (LLMs) have proven outstanding at generating synthetic data and labels, <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a> offering a solution to these data challenges. <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>

### Case Study: Indeed - Filtering Bad Job Recommendations

Indeed faced the challenge of sending bad job recommendations to users via email, leading to poor user experience and unsubscribes. <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a> While explicit negative feedback (thumbs down) was available, it was very sparse. <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a> Implicit feedback (not acting on recommendations) was often imprecise. <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>

Their solution involved using a lightweight classifier to filter out bad recommendations, with LLMs assisting in data generation and labeling:
1.  **Human Labeling**: Experts initially labeled job recommendations and user pairs based on resume and activity data. <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>
2.  **LLM Prompting (Initial Attempts)**:
    *   Open LLMs (Mistral, Llama 2) showed very poor performance, struggling to pay attention to resume and job description details, providing generic output. <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>
    *   GPT-4 performed well (90% precision and recall) but was too costly and slow (22 seconds per query). <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>
    *   GPT-3.5 had poor precision; 37% of recommendations flagged as bad were actually good. <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>
3.  **Fine-tuning and Distillation**:
    *   They then `[[Finetuning AI models for specific use cases | fine-tuned]]` GPT-2.5, which achieved the desired precision (0.3) at a quarter of GPT-4's cost and latency, but was still too slow for online filtering (6.7 seconds). <a class="yt-timestamp" data-t="00:11:30">[00:11:30]</a>
    *   The final step involved `[[Techniques for improving AI model efficiency | distilling]]` a lightweight classifier using the `[[Finetuning AI models for specific use cases | fine-tuned]]` GPT-2.5 labels. <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a> This classifier achieved high performance (0.86 AU ROC) and was fast enough for real-time filtering (less than 200 milliseconds). <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>

The outcome was a 20% reduction in bad recommendations. <a class="yt-timestamp" data-t="00:12:20">[00:12:20]</a> Surprisingly, application rates increased by 4% and unsubscribe rates dropped by 5%, demonstrating that "quantity is not everything. Quality makes a big difference." <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>

### Case Study: Spotify - Query Recommendations for New Categories

Spotify, traditionally known for songs and artists, introduced podcasts and audiobooks, facing a severe cold-start problem for these new content categories. <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a> Exploratory search became essential for expanding beyond music. <a class="yt-timestamp" data-t="00:13:40">[00:13:40]</a>

Their solution was a query recommendation system. <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>
*   **Query Generation**: Initial query ideas were extracted from catalog and playlist titles, and mined from search logs using conventional techniques. <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>
*   **LLM Augmentation**: LLMs were then used to "generate natural language queries" <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a> to augment this existing data. The strategy was to "use the LLM to augment it when you need it. Don't use the LLM for everything at the start." <a class="yt-timestamp" data-t="00:14:29">[00:14:29]</a>
*   **Ranking**: These exploratory queries were then ranked alongside immediate search results. <a class="yt-timestamp" data-t="00:14:46">[00:14:46]</a>

This `[[Enhancing existing systems with AI capabilities | enhancement to the existing system]]` led to a 9% increase in exploratory queries, meaning one-tenth of Spotify's users were now exploring new products daily. <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a> This significant engagement accelerated the growth of new product categories. <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>

## Benefits of LLM-Augmented Synthetic Data

LLM-augmented synthetic data provides significant benefits:
*   **Richer, High-Quality Data at Scale**: It allows for the creation of more comprehensive and precise data, even for "tail queries" and "tail items" where engagement data is scarce. <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a> This addresses `[[Challenges and solutions in AI driven data processing | challenges]]` in data processing.
*   **Lower Cost and Effort**: This approach is "far lower cost and effort that is even possible with human adaptation." <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>
*   **Efficiency and Scalability**: By `[[Leveraging AI Tools for Efficiency and Scalability | leveraging AI tools]]` like LLMs for data generation, systems can achieve greater efficiency and scale in data acquisition. <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>

Overall, data augmentation, particularly through the strategic use of LLMs, is a key strategy for improving AI model performance and addressing fundamental data challenges in complex systems like recommendation engines and search platforms. <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>