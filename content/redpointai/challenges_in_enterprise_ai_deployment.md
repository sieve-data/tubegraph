---
title: Challenges in Enterprise AI deployment
videoId: NLFboNNKCME
---

From: [[redpointai]] <br/> 

Enterprises face significant [[Enterprise AI adoption challenges | challenges]] when adopting and deploying AI solutions, particularly with generative AI (GenAI). While initial excitement around GenAI's potential is high, many companies find it isn't ready for prime time within enterprise environments <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

## Key Challenges in Enterprise AI Deployment

### System vs. Model Focus
A primary challenge is that enterprises often acquire models, not complete systems. A model, such as a large language model, might only constitute 10-20% of the entire system needed to solve a business problem <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>. Enterprises need a fully integrated system, not just a model that requires extensive surrounding infrastructure to be built, which can be complicated <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.

### Specialization vs. Generalization
While Artificial General Intelligence (AGI) aims for general capabilities, enterprises often require specialized AI tailored to specific use cases <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. A generalist AI system might generate responses outside of desired parameters, leading to issues. For example, using a generalist AI for performance reviews in the European Union could lead to heavy sanctions, necessitating significant constraints on the model <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>. The ideal approach for [[Enterprise AI adoption challenges | enterprise AI]] is through specialization <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.

### From Demos to Production
Many compelling GenAI demos, often built with layered components, fail when they reach real user testing and production deployment <a class="yt-timestamp" data-t="07:51:00">[07:51:00]</a>. Demos are frequently based on small, curated datasets (e.g., 20 PDFs), and the system breaks down when scaled to real-world volumes like 10,000 PDFs <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>.

### Non-ML Hurdles
Beyond machine learning aspects, deployment in enterprises faces significant hurdles related to risk, compliance, and security <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

### Integrating AI with Human Workflows
High-value use cases carry higher risks when directly exposed to customers <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>. Enterprises must carefully determine the optimal ratio of AI to human involvement, often by keeping humans in the loop to solve problems that are currently within the AI's capabilities, gradually expanding AI's role over time <a class="yt-timestamp" data-t="14:36:00">[14:36:00]</a>. AI systems are not yet at the stage of directly replacing people in complex roles, such as making investment decisions <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>, <a class="yt-timestamp" data-t="15:21:00">[15:21:00]</a>.

### Data and Alignment Challenges
Traditional reinforcement learning from human feedback (RLHF) methods have two main issues for enterprises:
1.  **Reward Model Training**: It requires training an expensive reward model that is then discarded <a class="yt-timestamp" data-t="16:43:00">[16:43:00]</a>.
2.  **Preference Data**: It relies on preference data (e.g., thumbs up/down feedback), which needs further annotation (e.g., by internal staff or external companies) to determine what a "good" response would look like. This process is slow, expensive, and becomes even more so for specialized use cases <a class="yt-timestamp" data-t="17:20:00">[17:20:00]</a>.

### Input Data and Extraction
A significant bottleneck is the difficulty of properly contextualizing language models, which requires correct data extraction. Extracting specific information from diverse documents, such as PDFs, is very challenging, and high-quality off-the-shelf extraction systems are not readily available <a class="yt-timestamp" data-t="25:50:00">[25:50:00]</a>.

### Evaluation and Measuring Success
There is currently no standardized, reliable way to evaluate AI systems for enterprises, making it hard to understand deployment risk and real accuracy <a class="yt-timestamp" data-t="26:40:00">[26:40:00]</a>. Many companies lack clarity on what they truly want from an AI system or what success looks like <a class="yt-timestamp" data-t="27:27:00">[27:27:00]</a>. Current evaluation methods, such as small spreadsheets with limited examples, are unprincipled and have high variance <a class="yt-timestamp" data-t="27:53:00">[27:53:00]</a>.

### Bridging the Gap for AI Developers
The role of an "AI developer" has evolved from a machine learning expert to someone skilled in calling APIs <a class="yt-timestamp" data-t="29:31:00">[29:31:00]</a>. This shift necessitates evaluation frameworks that are accessible to these new types of developers, moving away from traditional machine learning data science concepts like test set creation and statistical testing <a class="yt-timestamp" data-t="30:12:00">[30:12:00]</a>.

## Strategies to Overcome Challenges

To overcome these [[challenges_and_strategies_in_ai_deployment | challenges]], companies like Contextual AI adopt an end-to-end integrated systems approach with custom alignment and specialization <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

This approach focuses on:
*   **Vertical Slicing**: Instead of building a "Frankenstein's RAG" with layered, disparate components, they slice vertically through the AI stack, controlling retrieval, reranking, generation, post-training, and alignment <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.
*   **High-Value Use Cases**: Focusing on knowledge-intensive use cases where deep integration and specialization provide significant benefits <a class="yt-timestamp" data-t="06:27:00">[06:27:00]</a>.
*   **Direct Feedback Learning**: Utilizing thumbs up/down feedback mechanisms from customer deployments and proprietary algorithms (like KTO and APO) to directly optimize models without needing expensive data annotation <a class="yt-timestamp" data-t="20:26:00">[20:26:00]</a>.
*   **Post-Training and Alignment**: Recognizing that post-training is where the "magic happens" in AI, making models specifically good at what they are needed for, rather than being generalists <a class="yt-timestamp" data-t="20:57:00">[20:57:00]</a>, <a class="yt-timestamp" data-t="21:30:00">[21:30:00]</a>.
*   **Customer Engagement**: Spending significant time with customers to define success metrics and then incrementally building and productionizing the solution <a class="yt-timestamp" data-t="27:34:00">[27:34:00]</a>.
*   **Integrated Components**: Despite bespoke needs, the underlying system components (data extraction, retrieval mechanisms, language model contextualization, post-processing) have commonalities that can be specialized and fine-tuned <a class="yt-timestamp" data-t="28:20:00">[28:20:00]</a>.

Overall, the focus is on delivering a complete, specialized, and reliable system that can demonstrate a clear return on investment (ROI) for the enterprise <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>, <a class="yt-timestamp" data-t="21:46:00">[21:46:00]</a>.