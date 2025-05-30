---
title: Innovations in posttraining and model reasoning
videoId: NLFboNNKCME
---

From: [[redpointai]] <br/> 

The field of AI is rapidly evolving, with significant advancements in areas like post-training methodologies and the development of more capable reasoning models. This article summarizes insights from a discussion with Da Kila, CEO and co-founder of Contextual AI, who previously served as Head of Research at Hugging Face and spent five years at Facebook AI Research, where he wrote the first paper on Retrieval-Augmented Generation (RAG). <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

## OpenAI's O1 Model and the Shift to Systems Thinking

Da Kila views OpenAI's O1 model as "very exciting," noting that it emphasizes thinking about "systems rather than models." <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a> The O1 model compresses Chain of Thought ideas into the model using Reinforcement Learning from Human Feedback (RLHF), turning the model into a more complex system. <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a> This approach is particularly encouraging for reasoning tasks. <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>

However, the widespread adoption of this approach depends on latency constraints, as more "thinking" during test time increases latency. <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a> While O1 shows greater power in areas like math and law, older models can still perform better on other tasks and are often faster. <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>

## Contextual AI's Approach to Enterprise AI

Contextual AI was founded to address the frustration enterprises faced with generative AI not being ready for prime time. <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a> Their approach differs from other foundation model players like OpenAI and Anthropic through two core principles:

1.  **Systems Over Models**: Contextual AI believes that a model is only "10-20% of this much bigger system that has to solve the problem." <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a> Enterprises need to buy the entire system, not just the model, to avoid the complexity of building the surrounding infrastructure themselves. <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>
2.  **Specialization Over AGI**: Unlike AGI, which is seen as a consumer product needing general intelligence, enterprises often know exactly what they need and prefer specialized AI. <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a> Generalist AI can even be problematic, as in the example of an AI system for performance reviews in the European Union, which could lead to heavy sanctions. <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a> Therefore, the right approach for enterprise AI is through specialization. <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>

Contextual AI focuses on "end-to-end specialize[ing] all the parts together" into a very integrated system, targeting high-value, knowledge-intensive use cases. <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a> This vertical slicing of the stack, controlling retrieval, reranking, generation, [[pretraining_and_finetuning_ai_models | post-training]], alignment, and fine-tuning, provides a compounding effect in problem-solving. <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>

### Challenges in Enterprise Deployment

While many "compelling demos" are built with a layered, "Frankenstein's RAG" approach, they often fail during real user testing due to issues with deployment, risk, compliance, and security. <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a> Demos often rely on small datasets (e.g., 20 PDFs) and "hill climbing directly on the test set." <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a> When scaled to 10,000 PDFs, "everything breaks down completely." <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>

Enterprises are cautioned about directly exposing AI systems to customers, especially for high-value or high-risk use cases. <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a> The focus should be on "keeping humans in the loop," solving problems within current reach, and gradually increasing complexity. <a class="yt-timestamp" data-t="00:14:39">[00:14:39]</a>

## Retrieval-Augmented Generation (RAG)

Da Kila is the co-author of the first paper on RAG. <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a> The original vision for RAG was more ambitious than what was published. <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a> The work stemmed from his career-long focus on "grounding" language in perceptual information, initially in early [[multimodal_ai_and_video_model_innovations | multimodal AI]] systems. <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>

The first prototype of RAG, which grounded language in Wikipedia, leveraged Facebook AI image similarity search (FAISS), an early vector database. <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a> The key technical challenge was figuring out "how to backpropagate into the retrieval mechanism" to train the system effectively. <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>

Da Kila notes that it wasn't immediately apparent that RAG would become such a standard paradigm, comparing its initial reception to that of the Transformer paper, which was initially "underwhelmed" at Fair. <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a> He suggests that the success of Transformers is largely due to their optimality for GPUs, rather than their inherent "amazingness." <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a> The real credit, he believes, should go to the inventors of the attention mechanism. <a class="yt-timestamp" data-t="00:13:34">[00:13:34]</a>

## Alignment and Reinforcement Learning in AI

[[the_role_of_reinforcement_and_finetuning_in_ai | Alignment]] is a crucial problem area focused on making systems maximally useful for end-users. <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a> Reinforcement Learning from Human Feedback (RLHF) was "the secret sauce" behind ChatGPT's success, allowing models to capture human preferences at the full sequence level. <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>

### Challenges with RLHF

RLHF presents two significant problems:
1.  **Reward Model Training**: It requires training a separate, often expensive, reward model that is then discarded after training. <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>
2.  **Preference Data Acquisition**: It relies on "preference data," which means human annotation (e.g., thumbs up/down feedback) is needed to correct model outputs. This process is "very slow, very expensive," and becomes even more so for specialized use cases. <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>

### Contextual AI's Innovations in Alignment

Contextual AI aims to break these dependencies:
*   **Direct Preference Optimization (DPO)**: An approach that allows optimization without a separate reward model, making it more efficient. <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>
*   **Kahneman-Tversky Optimization (KTO)**: Developed with Stanford student Kavin Singh, this method directly optimizes on feedback without needing explicit preference pairs or data annotation. <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>
*   **Contrastive Learning from Revisions (CLARE)**: Addresses the "underspecification problems" in preference datasets. Instead of just "this is better than this one," CLARE focuses on "contrasting the revisions" (the specific fix for a problem), providing a much tighter and less underspecified signal. <a class="yt-timestamp" data-t="00:18:18">[00:18:18]</a>
*   **Anchored Preference Optimization (APO)**: Accounts for the quality of the model itself in relation to the preference data. If the model is already better than the data, APO ensures that the system learns the ranking without being misled by a lower-quality "right answer." <a class="yt-timestamp" data-t="00:19:51">[00:19:51]</a>

Contextual AI's internal data annotation team and direct customer feedback mechanisms (like thumbs up/down) allow them to learn effectively using these algorithms. <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a> The speaker emphasizes that "post-training really is where a lot of the magic happens in AI," transforming a pre-trained model into one capable of specific tasks. <a class="yt-timestamp" data-t="00:20:57">[00:20:57]</a> This alignment focuses on specific business use cases rather than general capabilities like Shakespearean sonnets. <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>

## Small MoE Open-Source Model (ALOHA)

Contextual AI, in collaboration with the Allen Institute, released ALOHA, a high-quality, fully open-source Mixture of Experts (MoE) model. <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a> This work aligns with the trend of moving towards smaller models that can be deployed on edge devices. <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>

Another related innovation is GRIT (Generative Representational Instruction Tuning), which demonstrated that the same model can be used for both the retriever and the generator. <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a> This allows for significant compute caching, as the query encoding for retrieval can be reused for generation, leading to greater efficiency. <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a> The future goal is to combine ALOHA and GRIT to create powerful RAG systems deployable on mobile phones. <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>

## Academia vs. Industry in AI Research

Academia remains "super important for the progress of AI." <a class="yt-timestamp" data-t="00:24:21">[00:24:21]</a> While the scale of pre-training has shifted beyond the reach of most academic institutions compared to five years ago, there's still significant scope for research in [[pretraining_and_finetuning_ai_models | pre-training]] with smaller models. <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a> The importance of [[pretraining_and_finetuning_ai_models | post-training]] is a "real blessing," as it allows academics to take pre-trained models (like Meta's Llama) and conduct "amazing research" in [[the_role_of_reinforcement_and_finetuning_in_ai | post-training]] and alignment methods. <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>

## Overhyped vs. Underhyped in AI

*   **Overhyped/Underhyped**: Agents. They are currently "overhyped" because they don't fully work yet, but "underhyped" because they are "showing signs of life." <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>
*   **Synthetic Data**: Initially skeptical, Da Kila changed his mind, finding synthetic data to be "super powerful" when done correctly and combined with smarter algorithms like KTO and APO. <a class="yt-timestamp" data-t="00:30:45">[00:30:45]</a> He refutes the idea that society is "running out of tokens" for training, stating that huge amounts of data are produced daily, and the problem is often data quality, not quantity. <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>
*   **Multimodality**: He believes the field has "not even scratched the surface" with [[multimodal_ai_and_video_model_innovations | multimodal AI]], especially video data, which offers a much richer understanding of the world than text alone. <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>
*   **Chain of Thought**: Initially dismissed as a "cute gimmick," Chain of Thought approaches have proven to work "really, really well" when combined with other techniques like RLHF for model improvement. <a class="yt-timestamp" data-t="00:31:17">[00:31:17]</a>

## The Future of AI and Enterprise Adoption

Da Kila sees current [[trends_in_ai_model_training_and_deployment | AI model training and deployment]] as moving towards "scaling in many directions" beyond just model size. <a class="yt-timestamp" data-t="00:50:36">[00:50:36]</a> This includes sophisticated [[pretraining_and_finetuning_ai_models | post-training]], "systems thinking" distilled back into models, and improvements in practical aspects like [[challenges_and_optimizations_in_ai_model_training_and_inference | mixture of retrievers]]. <a class="yt-timestamp" data-t="00:50:14">[00:50:14]</a>

He highlights the shift in what an "AI developer" means, moving from machine learning experts to those skilled at calling APIs. <a class="yt-timestamp" data-t="00:29:31">[00:29:31]</a> This necessitates new evaluation frameworks that are accessible to developers, rather than relying on traditional machine learning metrics. <a class="yt-timestamp" data-t="00:30:12">[00:30:12]</a>

Challenges remain in [[challenges_and_advancements_in_ai_model_development | AI model development]] and [[challenges_in_ai_model_training_and_deployment | deployment]]. For instance, getting "off-the-shelf extraction systems" for documents (like PDFs) to work correctly is "very, very hard," requiring custom solutions. <a class="yt-timestamp" data-t="00:25:48">[00:25:48]</a> Similarly, robust evaluation methods for enterprise AI, especially regarding risk and accuracy, are still largely "underexplored." <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>

The long-term vision involves AI systems evolving into "multi-agent systems" where humans will also act as agents. <a class="yt-timestamp" data-t="00:45:05">[00:45:05]</a> This is already conceptually present in areas like synthetic data generation, where one agent trains another. <a class="yt-timestamp" data-t="00:43:33">[00:43:33]</a>

While it's currently akin to selling "Tesla Roadsters" (high-end, custom-tuned products with dedicated support), the goal is to build the "assembly line for the Model S" – a more accessible, turnkey solution in the future. <a class="yt-timestamp" data-t="00:49:05">[00:49:05]</a> The focus remains on delivering "amazing experiences to our customers" and proving tangible ROI from deployments. <a class="yt-timestamp" data-t="00:48:48">[00:48:48]</a>