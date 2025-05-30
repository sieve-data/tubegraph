---
title: Retrieval augmented generation and contextual AI
videoId: NLFboNNKCME
---

From: [[redpointai]] <br/> 

Da Kila, CEO and co-founder of Contextual AI, is known for authoring the first paper on Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Contextual AI has raised nearly $100 million to help enterprises build customized, contextual language models for their specific use cases <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. Previously, Kila was the head of research at Hugging Face, spent five years at Facebook AI Research (Fair), and is an adjunct professor at Stanford <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Contextual AI's Vision and Approach

Contextual AI was founded to address the frustration enterprises faced with [[generative_ai_for_business_applications | generative AI]] – while exciting, it wasn't production-ready for their specific needs <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Da Kila and his team knew RAG would be a solution, but aimed to go "much better" than the existing RAG concept <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.

Contextual AI operates on two core principles:

1.  **Systems over Models**: While new models like OpenAI's 01 are compressing "Chain of Thought" ideas into the model, Contextual AI believes a model is only 10-20% of the much larger system needed to solve enterprise problems <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Enterprises need to buy the entire system, not just a model they then have to build around <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
2.  **Specialization over AGI**: General Artificial General Intelligence (AGI) is fundamentally a consumer product because consumer needs are unknown <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. In contrast, enterprises often know exactly what they want and do not want a generalist AI <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>. For example, a bank in the European Union would face severe sanctions for using a generalist AI system for performance reviews <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. The right approach for enterprise AI is through specialization, not generalization <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

Contextual AI builds integrated systems, end-to-end specializing all parts, and focuses on high-value, knowledge-intensive use cases where deep integration and specialization pay off <a class="yt-timestamp" data-t="00:06:20">[00:06:20]</a>. Unlike the "layered cake" approach of combining many specific infrastructure parts (which can lead to a "Frankenstein's RAG"), Contextual AI slices vertically through the stack, controlling retrieval, reranking, generation, post-training, alignment, and fine-tuning to deliver a unified solution <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.

### Challenges in Enterprise AI Deployments

While many "compelling demos" are built with a layered approach, they often fail completely during real user testing or when scaled to larger datasets (e.g., 10,000 PDFs instead of 20) <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Beyond machine learning, challenges include risk, compliance, security, and operations <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>. Contextual AI exclusively focuses on production deployment <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.

Enterprises must be cautious about directly exposing AI to customers, especially for high-value use cases <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>. The focus should be on finding the optimal ratio of AI to human, keeping humans in the loop, and solving problems that are currently within reach <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. For example, instead of an AI making investment decisions, it should provide great tools to help investors make better decisions <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

## The Origin of Retrieval Augmented Generation (RAG)

Da Kila's work on RAG stemmed from a long-standing interest in "grounding" language models <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. His PhD focused on grounding language in perceptual information, like understanding the word "cat" by integrating pictures of cats into NLP systems <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

At Fair (Facebook AI Research), working with PhD student Ethan Perez, the idea emerged to ground models in Wikipedia <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. They built an early RAG prototype, made possible by Facebook AI Image Similarity Search (FAISS), which served as the archetype for vector databases <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. A key challenge was figuring out how to backpropagate into the retrieval mechanism to train the system, which many future implementations would avoid by using off-the-shelf components <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>. The collaboration with Patrick Lewis and Sebastian Riedel in London on open domain question answering solidified RAG's application <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

At the time of publication, it wasn't apparent that RAG would become such a standard paradigm; breakthroughs often involve much simultaneous work, similar to the Transformer paper, whose historical narrative has been "rewritten" to inflate its initial impact <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. The success of Transformers, for instance, was largely due to their optimality for GPUs, not solely their inherent architectural superiority <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## [[Advancements in AI for Creative Tools | Alignment and Reinforcement Learning]]

Alignment is a critical area for making AI systems maximally useful for end-users <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. Reinforcement Learning from Human Feedback (RLHF) was the "secret sauce" behind ChatGPT's success, allowing models to capture human preferences at the full sequence level <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.

However, RLHF has two major problems:
1.  **Expensive Reward Model**: Training a reward model (to propagate rewards back to the sequence) is costly and the model is then discarded <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
2.  **Preference Data Requirement**: Obtaining preference data (e.g., thumbs up/down feedback requiring internal or external annotation) is slow, expensive, and becomes even more so for specialized use cases <a class="yt-timestamp" data-t="00:17:03">[00:17:03]</a>.

Contextual AI's research, often in collaboration with Stanford students, aims to break these dependencies:
*   **DPO (Direct Preference Optimization)**: Achieves alignment without needing to train a separate reward model, making it more efficient <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>.
*   **KTO (Kahneman-Tversky Optimization)**: Allows direct optimization on feedback without requiring explicit data annotation <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>. This is based on behavioral economist utility theory and prospect theory <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   **Clare (Contrastive Revisions)**: Addresses "underspecification problems" in preference data. Instead of vague rankings, Clare uses "revisions" where a small difference between two options clearly highlights the desired fix, making the preference signal much tighter <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.
*   **APO (Anchored Preference Optimization)**: Recognizes the relationship between data and model quality. If the model is better than the preference data (which is possible now), APO ensures the system learns only the ranking preference, not that the "good" answer is the absolute right one <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>.

Contextual AI uses its own data annotation team and gathers direct feedback (e.g., thumbs up/down) from customer deployments, which their algorithms can learn from without standard RLHF <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This alignment work is crucial for the core model during post-training, which is where "a lot of the magic happens" in AI <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. By aligning models to specific business use cases (e.g., finance) rather than general knowledge (e.g., quantum mechanics or Shakespeare), specialization and customization are achieved, making models production-ready and delivering real ROI <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.

## ALLOAI and the Trend Towards Smaller Models

Contextual AI, in collaboration with the Allen Institute, released ALLOAI, a powerful small Mixture of Experts (MoE) open-source model <a class="yt-timestamp" data-t="00:22:15">[00:22:15]</a>. This work was inspired by the trend towards smaller models that can be deployed on edge devices <a class="yt-timestamp" data-t="00:22:47">[00:22:47]</a>.

ALLOAI builds on previous work called GRIT (Generative Representational Instruction Tuning), which demonstrated that the same model could be used for both retriever and generator, allowing for significant compute caching <a class="yt-timestamp" data-t="00:22:58">[00:22:58]</a>. The vision is to combine ALLOAI with GRIT to create "super powerful RAG systems" deployable on phones <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.

## Academia's Role in AI Research

Academia continues to play a vital role in AI progress <a class="yt-timestamp" data-t="00:24:22">[00:24:22]</a>. While the scale of pre-training has shifted beyond what most universities can do, there's still significant and interesting research in pre-training with smaller models <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>. The importance of post-training and alignment methods means that academics can take generously donated pre-trained models (like Meta's Llama) and conduct amazing research on top of them <a class="yt-timestamp" data-t="00:24:55">[00:24:55]</a>.

## Challenges and Future of Evaluation

One major challenge in enterprise AI is the lack of good off-the-shelf extraction systems, especially for complex documents like PDFs. This crucial "boring stuff" at the beginning of the pipeline is necessary for proper retrieval and contextualization <a class="yt-timestamp" data-t="00:25:47">[00:25:47]</a>.

Another underdeveloped area is evaluation, particularly for enterprises needing to understand deployment risk and real system accuracy <a class="yt-timestamp" data-t="00:26:40">[00:26:40]</a>. Currently, many evaluations are informal, often based on small spreadsheets with high variance, lacking principle <a class="yt-timestamp" data-t="00:27:51">[00:27:51]</a>. A key problem is that many people don't understand what they truly want from an AI system <a class="yt-timestamp" data-t="00:27:29">[00:27:29]</a>. Contextual AI spends significant time with customers to define success and productionize prototypes <a class="yt-timestamp" data-t="00:27:34">[00:27:34]</a>.

The future of evaluation should move towards accessible frameworks for API-focused AI developers, rather than relying on traditional machine learning or data science knowledge around test set creation and statistical testing <a class="yt-timestamp" data-t="00:29:46">[00:29:46]</a>.

## Shifting AI Research Beliefs

Da Kila has observed several changes in his AI research beliefs:
*   **Synthetic data working well**: This was initially unexpected <a class="yt-timestamp" data-t="00:30:49">[00:30:49]</a>.
*   **[[the_role_of_simulation_and_generative_agents_in_ai | Agentic workflows with tool use]]**: Considered much more possible now than a year ago, despite agents still being ill-defined <a class="yt-timestamp" data-t="00:30:56">[00:30:56]</a>.
*   **Test-time compute and Chain of Thought**: Initially viewed as a "cute gimmick" or flawed from an evaluation perspective, Chain of Thought has proven to work "really, really well" <a class="yt-timestamp" data-t="00:31:17">[00:31:17]</a>. The power often comes from combining these ideas <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>.

## Data Scarcity, Multimodality, and Reasoning

The notion that AI is "running out of tokens" for training data is misguided <a class="yt-timestamp" data-t="00:32:53">[00:32:53]</a>. Society produces massive amounts of data daily; the real challenge is the lack of high-quality data <a class="yt-timestamp" data-t="00:33:07">[00:33:07]</a>.

Beyond text, [[the_role_of_generative_ai_in_preserving_memories | multimodal data]] (especially video) is largely untapped <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>. Models currently understand the world indirectly through linguistic behaviors (text), which is a "poor proxy" <a class="yt-timestamp" data-t="00:34:20">[00:34:20]</a>. Training on vast amounts of video data, for instance, could help models understand concepts like "cat" in a more human-like way <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>.

Furthermore, synthetic data, if done correctly and combined with smarter algorithms like KTO and APO, can be "super powerful," reducing the need for expensive data annotation or heavy compute <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>.

Models already possess reasoning capabilities, and these can be improved with more high-quality, specialized data (e.g., from mathematics PhD students for complex reasoning tasks) <a class="yt-timestamp" data-t="00:35:48">[00:35:48]</a>. Kila points to "metalinguistic tests" involving self-reference (like his paper "I am a strange data set," inspired by Douglas Hofstadter's "I Am a Strange Loop") as a milestone he'd be impressed to see models master <a class="yt-timestamp" data-t="00:36:47">[00:36:47]</a>. This tests the ability to reason about language itself, going beyond simple mathematics <a class="yt-timestamp" data-t="00:37:54">[00:37:54]</a>.

## Underreported Research Areas

Much of the exciting, underreported work in AI is practical, focusing on how to make things actually work, like sophisticated retrieval mechanisms (e.g., "mixture of retrievers" instead of a single dense vector database) <a class="yt-timestamp" data-t="00:38:26">[00:38:26]</a>. The industry is navigating a new product paradigm where the product is the model's behavior, reflecting its training data, which is a complex shift from traditional SaaS development <a class="yt-timestamp" data-t="00:38:48">[00:38:48]</a>.

## Reflections on Former Employers

### Facebook AI Research (Fair)
When Da Kila joined Fair in 2016, it was an incredibly free and academic environment <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>. While he worked on multi-agent systems and emergent communication protocols (which he believes will become relevant again soon), Fair's major contribution that "really changed the world" was PyTorch <a class="yt-timestamp" data-t="00:41:03">[00:41:03]</a>. Da Kila believes Mark Zuckerberg deserves significant credit for visionary leadership in open-sourcing projects like PyTorch, React, and Llama, which has significantly improved Meta's public perception and aided hiring <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>. Open-sourcing Llama, in particular, is a pragmatic move to avoid being dependent on other platforms if language models become the new dominant platform <a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>.

### Hugging Face
Hugging Face is an "amazing company" that has become the central place for publishing AI models <a class="yt-timestamp" data-t="00:45:37">[00:45:37]</a>. While they benefit from others' open-source efforts, they've built a "very special place for themselves" <a class="yt-timestamp" data-t="00:46:41">[00:46:41]</a>. Their future role could involve expanding into model deployment and [[experimenting_and_testing_ai_use_cases | experiments]] around that <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>.

## Funding Strategy for Contextual AI

Contextual AI adopts a pragmatic funding strategy, avoiding raising more money than needed at unsustainable valuations <a class="yt-timestamp" data-t="00:47:30">[00:47:30]</a>. This is crucial given the potential for the AI hype cycle to "die off a little bit in the next year or two" <a class="yt-timestamp" data-t="00:47:50">[00:47:50]</a>.

By not training their own large base models (leveraging open-source alternatives like Llama), Contextual AI can be more capital-efficient and allocate resources to essential areas like hiring top talent and working closely with customers to solve problems <a class="yt-timestamp" data-t="00:48:08">[00:48:08]</a>. The current stage of AI products often requires "white glove" or dedicated support (like selling a "Tesla Roadster" with engineers), as it's not yet a "turnkey thing" <a class="yt-timestamp" data-t="00:48:40">[00:48:40]</a>. The goal is to build towards an "assembly line for the Model S" that will eventually be a standard, easy-to-use product <a class="yt-timestamp" data-t="00:49:22">[00:49:22]</a>.

## Future of AI

Da Kila believes we are "only just getting started" with AI <a class="yt-timestamp" data-t="00:49:54">[00:49:54]</a>. The "cars coming off the assembly line" will be systems, not just models <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>. While scaling laws are important, there's significant room for improvement through post-training, alignment, and distilling system thinking back into models, leading to "scaling in many directions" <a class="yt-timestamp" data-t="00:50:11">[00:50:11]</a>.

### Overhyped vs. Underhyped
[[the_role_of_simulation_and_generative_agents_in_ai | Agents]] are simultaneously overhyped (because they don't fully work yet) and underhyped (because they are showing signs of life) <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>.

### Biggest Surprise in Building Contextual AI
The difficulty of building and maintaining a high-end research cluster that actually works was a major surprise <a class="yt-timestamp" data-t="00:51:21">[00:51:21]</a>. Hardware failures (GPUs, entire nodes) are frequent, highlighting the fragility of the infrastructure underpinning AI <a class="yt-timestamp" data-t="00:51:44">[00:51:44]</a>.

### Closed Source vs. Open Source Models
Da Kila sees a mix dominating in the long term, with a "triangle" metaphor:
*   **Top**: High-end, expensive, closed-source frontier models.
*   **Bottom**: Accessible open-source models.
*   **Middle**: The most interesting part, where companies achieve the right tradeoffs between capital efficiency, customer usefulness, and price point <a class="yt-timestamp" data-t="00:52:19">[00:52:19]</a>. Starting from open-source models and building strong post-training capabilities can lead to this "sweet spot" <a class="yt-timestamp" data-t="00:52:55">[00:52:55]</a>.

### Exciting AI Startups (Outside Contextual AI's Space)
Da Kila is most impressed by AI-based entertainment companies like Suno and video generation companies, noting that progress in this space is happening "way quicker" than expected <a class="yt-timestamp" data-t="00:53:11">[00:53:11]</a>. This could lead to personalized movies and infinite episodes of shows in the future <a class="yt-timestamp" data-t="00:53:56">[00:53:56]</a>.

### Company Most Interesting to Run AI At (Outside Contextual AI)
Beyond obvious tech giants, Da Kila finds traditional enterprises like JP Morgan interesting, where the head of AI gets to solve massive problems by integrating new AI technology before competitors <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>.

### Preferred AI Application to Build (If Not Contextual AI)
He would likely still work on something related to work, as he believes it's the "most obvious place" where AI will change everything and has a "very noble mission" to improve how the world works through AI <a class="yt-timestamp" data-t="00:55:42">[00:55:42]</a>. Otherwise, applications in the entertainment space are very interesting <a class="yt-timestamp" data-t="00:55:33">[00:55:33]</a>.

Da Kila views this as an "amazing point in history" where the world is changing rapidly due to AI <a class="yt-timestamp" data-t="00:56:51">[00:56:51]</a>.