---
title: challenges with hallucinations in language models
videoId: YLdK-683lCY
---

From: [[hu-po]] <br/> 

## What are Hallucinations?
[[large_language_models_and_their_applications | Large Language Models]] (LLMs) are prone to "hallucinations," which occur when they generate incorrect or made-up information as if it were factual <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. These models tend to fabricate answers when they encounter questions for which they lack a definitive response <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.

## Real-world Examples and Observations

### GPT-4o's Browsing Capabilities
Sam Altman, CEO of OpenAI, has promoted [[Multimodal large language models | GPT-4o]]'s browsing capabilities, suggesting they are a powerful form of [[retrieval_augmented_generation | Retrieval Augmented Generation]] (RAG) <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. However, real-world tests have shown instances of hallucination <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

One example involved a user uploading a picture of a robot arm with a camera and asking where to buy it <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>. This specific robot arm was from a very early-stage Chinese startup called Rec Camera, which primarily sells only the camera, not the arm itself <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. It's likely a prototype or demo machine not commercially available <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>.

Despite this, [[Multimodal large language models | GPT-4o]] incorrectly identified the arm as the "Spot arm" from Boston Dynamics, a completely different robot arm and end effector <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. Even when prompted with "Rec camera arm," [[Multimodal large language models | GPT-4o]] hallucinated again, mistaking it for the "HTC Rec camera," a periscope-shaped camera, which is entirely unrelated <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. This indicates that while RAG is intended to reduce hallucinations by providing relevant information, it doesn't always succeed <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

### Inconsistent Performance
Interestingly, when presented with an image from the popular Chinese game "Black Myth Wukong" and asked for information about it, [[Multimodal large language models | GPT-4o]] correctly identified the game <a class="yt-timestamp" data-t="16:03:00">[16:03:00]</a>. This suggests that [[Multimodal large language models | GPT-4o]] either has sufficient recent training data to be aware of the game or is adept at providing grounded captions that allow its web search agent to find the correct information <a class="yt-timestamp" data-t="16:52:00">[16:52:00]</a>. This positive result contrasts with its performance on the robot arm example <a class="yt-timestamp" data-t="17:15:00">[17:15:00]</a>.

### Political Bias and "Truth"
A notable observation concerns how different models handle controversial or political images. American model providers like [[Multimodal large language models | GPT-4o]], Gemini, and Cloud 3.5 Sonet, when prompted with a political picture of Donald Trump, tend to either refuse to comment or provide responses that could be seen as biased or "propaganda" <a class="yt-timestamp" data-t="22:25:00">[22:25:00]</a>. This highlights the challenge of defining and delivering "truth" or factual information when models are subjected to ethical or political alignment considerations <a class="yt-timestamp" data-t="22:16:00">[22:16:00]</a>.

## Causes of Hallucinations

### Lack of Domain-Specific Knowledge
LLMs often lack domain-specific knowledge, making them prone to hallucinations when asked about niche topics <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. For example, [[Multimodal large language models | GPT-4o]]'s inability to correctly identify the Rec Camera robot arm stems from its lack of specialized knowledge in robotics beyond common examples like Boston Dynamics <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.

### Making Up Information
When an LLM doesn't have an answer to a question, it might simply "make stuff up," leading to hallucinations <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a>.

### Fragile Models and Catastrophic Forgetting
Fine-tuning a pre-trained model, especially an embedding or retrieval model, on a very narrow or low-variance dataset can lead to "catastrophic forgetting" <a class="yt-timestamp" data-t="58:50:00">[58:50:00]</a>. This means the model loses its generalization capability, which can decrease performance when, for example, [[evaluation_metrics_for_language_models | in-context examples]] are added without proper fine-tuning for that specific use case <a class="yt-timestamp" data-t="59:03:00">[59:03:00]</a>.

## Approaches to Mitigate Hallucinations

### [[retrieval_augmented_generation | Retrieval Augmented Generation]] (RAG)
RAG is fundamentally designed to reduce hallucinations by allowing LLMs to fetch and use relevant external information as context for their generations <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. It's a broad term encompassing various approaches to integrate information retrieval with text generation <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

### Vision Search Assistant
This approach, presented in a Chinese paper, aims to empower [[Multimodal Language Models | Vision Language Models]] (VLMs) as multimodal search engines <a class="yt-timestamp" data-t="10:33:00">[10:33:00]</a>. It proposes a collaboration between VLMs and web agents to perform "open world retrieval augmented generation" <a class="yt-timestamp" data-t="12:04:00">[12:04:00]</a>.

Key aspects include:
*   **Regional Captioning**: Breaking down an image into regions of interest and creating specific captions for each region <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>. This provides a more detailed visual description for searching <a class="yt-timestamp" data-t="18:56:00">[18:56:00]</a>.
*   **Flow Engineering**: The system uses a human-designed "agent loop" or "flow engineering" where information is processed through various steps, including query understanding, object inference, text generation for search, content analysis, and judgment of sufficiency <a class="yt-timestamp" data-t="12:29:00">[12:29:00]</a>.
*   **Automated Data Generation**: The system dynamically expands user input (image + short text) into a rich set of information for effective searching <a class="yt-timestamp" data-t="20:44:00">[20:44:00]</a>.

This approach claims to significantly outperform competitors like Perplexity AI Pro and [[Multimodal large language models | GPT-4o]] web in human evaluations <a class="yt-timestamp" data-t="22:20:00">[22:20:00]</a>.

### AutoMIR (Automated Medical Information Retrieval)
This paper proposes a self-learning framework that refines pseudo-document generation and retrieval using unlabeled medical corpora <a class="yt-timestamp" data-t="24:55:00">[24:55:00]</a>. The goal is to automatically create high-quality, labeled training data for a retrieval model without human intervention <a class="yt-timestamp" data-t="31:07:00">[31:07:00]</a>.

The process involves:
1.  **Hypothetical Question Generation**: A document from the database is used to generate a hypothetical question <a class="yt-timestamp" data-t="31:12:00">[31:12:00]</a>.
2.  **Pseudo Document Generation**: The hypothetical question is used to generate pseudo-documents that are expected to answer it <a class="yt-timestamp" data-t="31:19:00">[31:19:00]</a>.
3.  **Retrieval and Ranking**: A retrieval model ranks documents in the database based on their similarity to the pseudo-documents <a class="yt-timestamp" data-t="31:26:00">[31:26:00]</a>.
4.  **Data Point Creation**: By knowing the original document, this process creates a labeled data point (query, generated document, correct document, negative examples) to train and improve both the generator and the retriever <a class="yt-timestamp" data-t="32:56:00">[32:56:00]</a>.

This automated pipeline can create a highly specialized retrieval model for esoteric databases (e.g., medical data), which may not be covered by general LLM pre-training corpora <a class="yt-timestamp" data-t="33:55:00">[33:55:00]</a>.

### Zero-Shot Dense Retrieval with Embeddings from Relevance Feedback
This method aims to speed up dense retrieval systems that use hypothetical document generation <a class="yt-timestamp" data-t="35:03:00">[35:03:00]</a>. Instead of an LLM generating a large number of tokens for a hypothetical document, this approach focuses on the LLM outputting a single token (e.g., 0 or 1) to quickly determine if a document is relevant to a query <a class="yt-timestamp" data-t="36:04:00">[36:04:00]</a>. This "minimum viable action" significantly reduces retrieval latency by 7.5 to 11 times <a class="yt-timestamp" data-t="38:00:00">[38:00:00]</a>.

### Multimodal RAG with Image Summaries
When integrating multimodal inputs like images into RAG systems, one effective strategy is to convert images into text summaries or captions <a class="yt-timestamp" data-t="51:15:00">[51:15:00]</a>. These "image summaries" are then turned into text embeddings and stored in a combined vector database along with traditional text embeddings <a class="yt-timestamp" data-t="51:30:00">[51:30:00]</a>. This allows for a unified text-based search across all modalities, which has been shown to perform better than maintaining separate vector stores for images and text <a class="yt-timestamp" data-t="52:09:00">[52:09:00]</a>.

### Challenges with [[adversarial_attacks_on_language_models | In-Context Examples]]
A paper exploring "Retrieval Augmented Retrieval with [[adversarial_attacks_on_language_models | In-Context Examples]]" found that simply adding [[adversarial_attacks_on_language_models | in-context examples]] to a query *without* updating the model parameters of the embedding model can actually *decrease* performance <a class="yt-timestamp" data-t="57:17:00">[57:17:00]</a>. While fine-tuning the retrieval models with semantically similar [[adversarial_attacks_on_language_models | in-context examples]] can equip them with the ability to leverage such inputs, the overall performance improvement is often marginal and inconsistent across different benchmarks <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>. This suggests that adding more data to the context can increase latency without guaranteeing better performance <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>.

## The Future of RAG and Context Length
A key question is whether RAG will become less relevant as context lengths for LLMs grow indefinitely <a class="yt-timestamp" data-t="00:46:44">[00:46:44]</a>. If LLMs can handle massive contexts (e.g., hundreds of documents), the need for complex "flow engineering" and intermediate steps might diminish <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a>.

Two potential futures exist:
1.  **Large Context, Infrequent Training**: Models are rarely trained (e.g., once or twice a year), and all relevant new information is simply put into the context <a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>. This shifts the cost to inference, as more data needs to be processed per query <a class="yt-timestamp" data-t="01:11:18">[01:11:18]</a>.
2.  **Smaller Context, Continual Learning**: Models are frequently retrained (e.g., weekly or daily) with the latest news and data, pushing new information directly into the model's parameters via gradients <a class="yt-timestamp" data-t="01:10:31">[01:10:31]</a>. This makes inference faster but incurs high, continuous training costs <a class="yt-timestamp" data-t="01:11:25">[01:11:25]</a>.

The optimal approach depends on various factors, including the type of queries, architectural advancements for long contexts, and the cost-efficiency of training clusters <a class="yt-timestamp" data-t="01:11:38">[01:11:38]</a>. [[evaluation_metrics_for_language_models | Prompt caching]] could also influence this by making larger contexts more viable <a class="yt-timestamp" data-t="01:12:37">[01:12:37]</a>.

## Conclusion
As of November 2024, the field of RAG is still highly experimental, with various ideas being explored to combat hallucinations and improve performance <a class="yt-timestamp" data-t="01:59:58">[01:59:58]</a>. The fact that seemingly "random" open-source Chinese papers can claim to outperform commercial systems like [[Multimodal large language models | GPT-4o]] and Perplexity suggests that there isn't a clear "winner" or established best practice yet <a class="yt-timestamp" data-t="01:30:41">[01:30:41]</a>. The pursuit of robust and reliable RAG systems remains an active area of research, with an ongoing debate about whether to prioritize expanding context windows or engaging in continuous model fine-tuning.