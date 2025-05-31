---
title: PostTraining Model Optimization in AI
videoId: NLFboNNKCME
---

From: [[redpointai]] <br/> 

Post-training is a crucial phase in AI model development, where pre-trained models are further refined to enhance their performance for specific tasks and user preferences <a class="yt-timestamp" data-t="02:20:51">[02:20:51]</a>. It's often where "a lot of the magic happens in AI," turning a general pre-trained model into one that excels at what it's needed to be good at <a class="yt-timestamp" data-t="02:57:57">[02:57:57]</a>.

## Systems Over Models
Contextual AI, a company co-founded by Da Kila, focuses on a "systems over models" approach, viewing the model as only 10-20% of the larger system required to solve a problem <a class="yt-timestamp" data-t="04:43:42">[04:43:42]</a> <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. This approach emphasizes that enterprises need a complete system, not just a model, to avoid the complexity of building the surrounding infrastructure themselves <a class="yt-timestamp" data-t="05:01:03">[05:01:03]</a> <a class="yt-timestamp" data-t="05:05:03">[05:05:03]</a>. This integrated system approach allows for end-to-end specialization and is particularly effective for high-value, knowledge-intensive use cases <a class="yt-timestamp" data-t="06:20:31">[06:20:31]</a> <a class="yt-timestamp" data-t="06:29:10">[06:29:10]</a>. By controlling retrieval, reranking, generation, post-training, and alignment, companies can achieve a compounding effect that leads to better problem-solving <a class="yt-timestamp" data-t="07:16:04">[07:16:04]</a>.

## Specialization for [[Enterprise use of AI and model specialization | Enterprise Use Cases]]
Unlike Artificial General Intelligence (AGI), which is considered a consumer product due to unknown consumer needs <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>, [[Enterprise use of AI and model specialization | enterprise AI]] often requires specialized intelligence <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>. For example, a banking AI system should not be a generalist that could, for instance, perform performance reviews, as this could lead to heavy sanctions in regions like the European Union <a class="yt-timestamp" data-t="05:44:09">[05:44:09]</a> <a class="yt-timestamp" data-t="05:51:00">[05:51:00]</a>. The correct way to approach [[Enterprise use of AI and model specialization | enterprise AI]] is through specialization, focusing on what the user wants <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.

Specialization through alignment and post-training helps make systems much more convincing for production deployment <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a> <a class="yt-timestamp" data-t="02:18:20">[02:18:20]</a>. For instance, an AI for finance doesn't need knowledge of quantum mechanics or Shakespeare; it needs to be highly proficient in its specific domain <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>.

## [[Finetuning and reinforcement learning techniques for AI | Finetuning and Reinforcement Learning Techniques]] for Post-Training
[[Finetuning and reinforcement learning techniques for AI | Alignment]] is a critical problem area in post-training, aiming to make systems maximally useful for end-users <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF was the "secret sauce" behind ChatGPT's success, building upon initial instruction tuning (SFT) <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>. It captures human preferences at the full sequence level, rather than just the next word <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. However, RLHF has two main challenges:
1.  **Reward Model Training**: It requires training a separate, good reward model to propagate rewards back to the sequence, which is expensive and the model isn't used in actual generation <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a>.
2.  **Preference Data**: It relies on preference data, meaning that if a user gives a thumbs-down, additional manual annotation is needed to specify what a "thumbs-up" response would look like <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. This process is slow, expensive, and becomes even more costly for specialized use cases <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>.

### DPO (Direct Preference Optimization)
DPO aims to break the dependency on training a separate reward model, making the process more efficient <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.

### KTO (Kahneman-Tversky Optimization)
Developed by Contextual AI with Cwin (a Stanford student), KTO directly optimizes on feedback without needing explicit preference pairs, thus eliminating the need for data annotation <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a> <a class="yt-timestamp" data-t="01:47:00">[01:47:00]</a>. KTO is based on behavioral economics utility theory and prospect theory <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.

### Clare (Contrastive Language-Action REvisions)
Clare, developed with Carl, addresses the under-specification problem in alignment data <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>. Instead of just ranking options, Clare focuses on contrasting revisions: identifying a problem with an option and providing a small, specific fix, thereby making the preference signal much tighter <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

### APO (Anchored Preference Optimization)
APO considers the relationship between the data and the model, specifically how good the model being trained on the preference data is <a class="yt-timestamp" data-t="02:37:00">[02:37:00]</a>. If the model is better than the preference data, it should learn the ranking rather than the "right answer," which might be suboptimal <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>. APO provides greater control over how data quality impacts the trained model's quality <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>.

## Data for Post-Training and [[Future of AI and pretraining challenges | Future of AI]]
Concerns about running out of data tokens for training AI models are largely unfounded <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>. Society produces massive amounts of data daily, far exceeding current training rates <a class="yt-timestamp" data-t="03:33:00">[03:33:00]</a>. The real challenge lies in the quality of this data <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.

*   **Data Quality vs. Quantity**: Lower quality data requires commensurately more quantity <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. The bottleneck is high-quality data, not overall data availability <a class="yt-timestamp" data-t="03:57:00">[03:57:57]</a>.
*   **Multimodality**: Moving to multimodal data, especially video, offers a vast, largely untapped resource <a class="yt-timestamp" data-t="03:59:00">[03:59:00]</a>. Training on multimodal data can help models better understand the world, addressing a significant shortcoming of current systems <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>.
*   **Synthetic Data**: Despite some flawed research suggesting otherwise, synthetic data, when generated correctly, is "super powerful" and can reduce reliance on data annotation and heavy computation, especially when combined with algorithms like KTO and APO <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a> <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

## [[Challenges and progress in AI model alignment research | Challenges and Progress in AI Model Alignment Research]]
One of the biggest surprises for Da Kila was how well synthetic data works <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. Additionally, "agentic workflows with tool use" are much more feasible than previously expected <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>. The effectiveness of "Chain of Thought" reasoning, initially seen as a gimmick, has proven to be very powerful when combined with techniques like RLHF for model training <a class="yt-timestamp" data-t="04:08:00">[04:08:00]</a> <a class="yt-timestamp" data-t="04:18:00">[04:18:00]</a>.

### Underreported Research Areas
Practical work on retrieval, such as using a "mixture of retrievers" instead of a single dense vector database, is an area of significant, though perhaps underreported, interest <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>. The field is exploring how to make these systems actually work and finding the right product form factor for AI research <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.

## [[AI model evaluation and benchmarking | Evaluation and Deployment Challenges]] in Production
Despite many compelling demos, a lot of AI deployments, especially in enterprises, are still just "demos happening" <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. These demos often fail in real user testing due to issues beyond machine learning, including deployment, risk, compliance, and security <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. Many demos are built on small, "hacked" test sets (e.g., 20 PDFs) and break down when scaled to real-world data (e.g., 10,000 PDFs) <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>.

For enterprises, the key question is whether a system can be put in front of customers <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>. As use cases become higher value, they also become riskier to expose directly to customers <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>. The goal is to find the optimal ratio of AI to human interaction, keeping humans in the loop for problems within reach <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

### The Need for Better [[AI model evaluation and benchmarking | Evaluation Frameworks]]
There is currently no reliable standard way to [[AI model evaluation and benchmarking | evaluate AI systems]] for enterprises, especially concerning deployment risk and real accuracy <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. Many companies don't seriously evaluate their systems, relying on unprincipled spreadsheets with high variance <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.

A critical step is to clearly define what success looks like for a customer, often involving a collaborative hill-climbing process to achieve success in a prototype setting before productionizing it <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. Future [[AI model evaluation and benchmarking | evaluation frameworks]] should be accessible to AI developers, who are increasingly proficient in calling APIs rather than traditional machine learning or statistical testing <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.

### Wishlist for External Contributions
To streamline end-to-end solutions, better off-the-shelf extraction systems are needed <a class="yt-timestamp" data-t="02:45:00">[02:45:00]</a>. Properly contextualizing language models requires accurate extraction, which is surprisingly difficult for tasks like extracting information from PDFs <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.

## Academic Role in Post-Training Research
Academia remains crucial for the progress of AI <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. While pre-training at the current scale is no longer feasible for universities <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>, the importance of post-training offers a significant opportunity <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. Academics can leverage pre-trained models (e.g., those generously open-sourced by Meta/Facebook) to conduct valuable research in post-training methods and better alignment techniques <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

## Conclusion
Post-training model optimization is vital for delivering production-ready AI solutions, especially in the enterprise context. It involves complex [[Finetuning and reinforcement learning techniques for AI | techniques]] like RLHF, DPO, KTO, and APO, and requires a shift towards thinking about AI as integrated systems rather than monolithic models. While challenges in data quality and [[AI model evaluation and benchmarking | evaluation]] persist, ongoing research and pragmatic approaches are paving the way for more specialized, useful, and scalable AI deployments.

> [!NOTE] Overhyped vs. Underhyped
> Agents are both overhyped (as they don't fully work yet) and underhyped (because they are showing signs of life and potential) <a class="yt-timestamp" data-t="05:57:00">[05:57:00]</a>. The shift to smaller models deployable on edge devices is a significant trend <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.