---
title: evaluation of retrieval models
videoId: YLdK-683lCY
---

From: [[hu-po]] <br/> 

[[retrieval_augmented_generation | Retrieval augmented generation]] (RAG) is a broad term describing any generation process that retrieves information from a static source to improve the output <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a>. This concept dates back to the Von Neumann architecture, where an arithmetic logic unit (generator) retrieves information from a memory unit to produce output from an input <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a>. In modern AI, RAG aims to reduce hallucinations in language models by fetching relevant information and adding context <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. However, even advanced RAG systems can still exhibit hallucinatory behavior <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>.

## Challenges in Evaluating RAG Systems

A primary challenge in [[evaluation metrics for language models | evaluating language models]], especially those incorporating RAG, is the propensity for hallucinations, where models "make stuff up" if a direct answer isn't available <a class="yt-timestamp" data-t="04:45:00">[04:45:00]</a>.

For instance, when asked to identify a robot arm from a Chinese startup (Rec Camera) and inquire where to buy it, GPT-4o (a type of [[retrieval_augmented_generation | retrieval augmented generation]] system with browsing capabilities <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>) incorrectly identified it as a Boston Dynamics Spot Arm <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>. Even when prompted with "Rec camera arm," it continued to hallucinate, confusing it with an HTC Rec camera <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. This highlights a critical flaw, as RAG is designed to *reduce* hallucinations <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.

## Benchmarking Approaches

### Vision Search Assistant (VSA)

A paper titled "Vision Search Assistant: Empower Vision Language Models as Multimodal Search Engines" proposes a collaboration between [[vision_language_models | vision language models]] (VLMs) and web agents to perform open-world [[retrieval_augmented_generation | retrieval augmented generation]] <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>. VLMs are computationally expensive to update frequently due to their larger token requirements for images <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a>. VSA leverages the VLM's visual understanding and the web agent's real-time information access <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>.

The VSA system's flow involves:
1.  **Understanding the query**: Deciding which objects in an image to focus on <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>.
2.  **Visual Content Formulation**: Using an open vocabulary detector (like Grounding DINO) to detect regions of interest and generate regional captions for each <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>. This approach enriches the visual description for search <a class="yt-timestamp" data-t="18:56:00">[18:56:00]</a>.
3.  **Generating text for search**: Using the regional captions to create search queries <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.
4.  **Analyzing search results**: A planning agent breaks down information into event, time, place, and effect <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>.
5.  **Judging sufficiency**: Determining if the obtained visual and textual information is enough <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.

In a human expert evaluation, VSA (a 7B model) significantly outperformed larger [[vision_language_models | vision language models]] (like LLaVA 1.6, Qwen 2 VL, Intern VL2) in identifying an image from "Black Myth Wukong," a relatively recent game that pre-trained VLMs failed to recognize <a class="yt-timestamp" data-t="15:09:00">[15:09:00]</a>. Surprisingly, GPT-4o *without* web search capabilities also correctly identified "Black Myth Wukong," suggesting its VLM might be more recently trained or adept at grounded captioning <a class="yt-timestamp" data-t="54:03:00">[54:03:00]</a>.

### AutoMIR for Medical Information Retrieval

"AutoMIR: Effective Zero-Shot Medical Information Retrieval Without Relevance Labels" proposes a self-learning framework to refine pseudo-document generation and retrieval using unlabeled medical corpora <a class="yt-timestamp" data-t="24:55:00">[24:55:00]</a>. A retrieval model's training has two stages:
1.  **Unsupervised pre-training**: Learning domain knowledge from large volumes of unlabeled text <a class="yt-timestamp" data-t="26:33:00">[26:33:00]</a> (e.g., 800 million text pairs for general medical terminology <a class="yt-timestamp" data-t="28:49:00">[28:49:00]</a>).
2.  **Supervised fine-tuning**: Using a high-quality labeled dataset and hard negative mining to differentiate similar texts <a class="yt-timestamp" data-t="27:52:00">[27:52:00]</a> (e.g., 3 million pairs for specific tasks <a class="yt-timestamp" data-t="28:54:00">[28:54:00]</a>).

AutoMIR's training pipeline is automated:
1.  Select a random document from an unlabeled database <a class="yt-timestamp" data-t="31:11:00">[31:11:00]</a>.
2.  Generate a hypothetical question from that document <a class="yt-timestamp" data-t="31:12:00">[31:12:00]</a>.
3.  Use the question to generate hypothetical documents <a class="yt-timestamp" data-t="31:17:00">[31:37:00]</a>.
4.  A retriever ranks database documents based on similarity to hypothetical documents <a class="yt-timestamp" data-t="31:26:00">[31:26:00]</a>.
5.  This creates a labeled dataset (query, generated doc, correct doc, negative examples) to fine-tune both the generator and retriever <a class="yt-timestamp" data-t="32:39:00">[32:39:00]</a>. This self-supervised approach allows continuous improvement specific to a given knowledge domain <a class="yt-timestamp" data-t="31:15:00">[31:15:00]</a>.

### Zero-Shot Dense Retrieval with Relevance Feedback

A limitation of hypothetical document generation for retrieval is latency: the system must wait for the generator to produce all tokens before retrieval can begin <a class="yt-timestamp" data-t="35:38:00">[35:38:00]</a>. To address this, "Zero-Shot Dense Retrieval with Embeddings from Relevance Feedback" proposes using an LLM to select documents for nearest neighbor search by outputting only a single token to indicate relevance (e.g., 0 for irrelevant, 1 for relevant) <a class="yt-timestamp" data-t="36:04:00">[36:04:00]</a>. This "minimum viable action" framing as a relevance estimation task dramatically reduces retrieval latency by 7.5 to 11x <a class="yt-timestamp" data-t="38:08:00">[38:08:00]</a>.

### Coral: Benchmarking Multi-Turn Conversational RAG

[[Benchmarking vision models | Benchmarking]] for RAG typically focuses on single-turn interactions <a class="yt-timestamp" data-t="39:58:00">[39:58:00]</a>. The "Coral" paper introduces a large-scale benchmark for multi-turn information-seeking conversations, automatically derived from Wikipedia <a class="yt-timestamp" data-t="39:53:00">[39:53:00]</a>.

Multi-turn settings require systems to:
*   Deal with redundant or irrelevant information from prior turns <a class="yt-timestamp" data-t="40:34:00">[40:34:00]</a>.
*   Cope with abrupt topic shifts, ignoring previous context if irrelevant <a class="yt-timestamp" data-t="40:39:00">[40:39:00]</a>.
*   Handle open-domain questions <a class="yt-timestamp" data-t="41:28:00">[41:28:00]</a>.
*   Provide knowledge-intensive and free-form responses <a class="yt-timestamp" data-t="41:32:00">[41:32:00]</a>.
*   Include citation labeling (though the utility of this is debated) <a class="yt-timestamp" data-t="41:46:00">[41:46:00]</a>.

The Coral dataset is constructed by traversing Wikipedia's knowledge graph (using methods like breadth-first, depth-first, or random walks) to generate synthetic multi-turn conversations (11-20 turns per conversation, 8,000 conversations total) <a class="yt-timestamp" data-t="44:47:00">[44:47:00]</a>. This allows for [[benchmarking_vision_models | benchmarking]] RAG systems in more realistic, dynamic conversational scenarios <a class="yt-timestamp" data-t="45:49:00">[45:49:00]</a>.

### Beyond Text: Multimodal Input Optimization

"Beyond Text: Optimizing RAG with Multimodal Inputs for Industrial Applications" explores how to best integrate [[overview_of_multimodal_models | multimodal models]] into RAG, focusing on image processing and retrieval <a class="yt-timestamp" data-t="48:48:00">[48:48:00]</a>. The paper compares two main approaches for [[comparison_of_image_and_textbased_retrieval_methods | retrieval augmented generation]] involving images:

1.  **Multimodal Embeddings with Separate Vector Stores**: Images are encoded into image embeddings and texts into text embeddings, stored in separate vector databases. Retrieval then occurs by searching each specialized database <a class="yt-timestamp" data-t="50:52:00">[50:52:00]</a>.
2.  **Image Summaries in a Combined Vector Store**: Images are first converted into text (e.g., through detailed captions or summaries), then encoded into text embeddings. Both image-derived text embeddings and original text embeddings are stored in a single vector database <a class="yt-timestamp" data-t="51:15:00">[51:15:00]</a>.

The study indicates that converting images into text summaries and then using these text embeddings for search generally yields better answer correctness than using raw image embeddings in separate stores <a class="yt-timestamp" data-t="52:15:00">[52:15:00]</a>. This suggests that processing images into textual representations can enhance retrieval effectiveness, especially when combined with a baseline RAG setup <a class="yt-timestamp" data-t="54:57:00">[54:57:00]</a>.

### Rare: Retrieval Augmented Retrieval with In-Context Examples

"Rare: Retrieval Augmented Retrieval with In-Context Examples" investigates whether adding in-context examples can improve embedding model performance in retrieval <a class="yt-timestamp" data-t="56:58:00">[56:58:00]</a>. In-context examples involve providing previous query-document pairs within the prompt to guide the model <a class="yt-timestamp" data-t="57:57:00">[57:57:00]</a>.

The findings suggest that simply adding in-context examples without updating the embedding model's parameters (i.e., fine-tuning) can *decrease* performance <a class="yt-timestamp" data-t="57:17:00">[57:17:00]</a>. This is because a retrieval model, once trained on a wide distribution, can suffer from "catastrophic forgetting" when exposed to a narrower, fine-tuning distribution without proper adaptation <a class="yt-timestamp" data-t="59:01:00">[59:01:00]</a>.

Rare's approach involves fine-tuning retrieval models specifically to leverage semantically similar in-context examples <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>. However, the results were mixed: while a 10-point improvement was observed on a science fact-based benchmark (CACT), performance remained largely unchanged or even worsened on other benchmarks <a class="yt-timestamp" data-t="01:01:45">[01:01:45]</a>. This suggests that the benefit of in-context examples in retrieval models is not universally consistent and may increase latency due to more tokens needing to be processed <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a>. This is considered a "negative result paper," valuable for informing future research directions <a class="yt-timestamp" data-t="01:01:12">[01:01:12]</a>.

## Factors Influencing Evaluation

### Context Length vs. Training Cadence
The effectiveness of RAG models often depends on the trade-off between increasing context length and frequent model re-training (continual learning) <a class="yt-timestamp" data-t="01:09:04">[01:09:04]</a>.
*   **Large Context Length**: If context windows become vast, models might rarely need retraining, with all relevant information simply passed in the prompt <a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>. This increases inference cost but reduces training frequency.
*   **Frequent Re-training**: Alternatively, models could be continually fine-tuned (e.g., daily or weekly) with new data via gradient pushes <a class="yt-timestamp" data-t="01:10:55">[01:10:55]</a>. This leads to faster inference (less context needed) but higher training costs and a more rapid "foundation model" release cadence <a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a>. The optimal balance depends on query types, architectural advancements for long context, and hardware capabilities <a class="yt-timestamp" data-t="01:11:38">[01:11:38]</a>.

### Embedding Dimension
The "quality" of an embedding model can be linked to the dimensionality of its output embeddings <a class="yt-timestamp" data-t="01:13:51">[01:13:51]</a>. Higher-dimensional embeddings offer greater "information representation capacity," leading to potentially better performance in similarity-based retrieval tasks <a class="yt-timestamp" data-t="01:14:13">[01:14:13]</a>. However, this comes at the cost of increased computational time for similarity calculations and higher memory requirements in vector databases <a class="yt-timestamp" data-t="01:14:41">[01:14:41]</a>. As computing power and memory capacities grow, embedding dimensions are expected to increase <a class="yt-timestamp" data-t="01:15:05">[01:15:05]</a>.

## Conclusion

The field of RAG is still highly experimental, with diverse approaches and no single clear winner <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>. Current research explores various methods, from breaking down images into regional captions to automating data generation for domain-specific retrieval, optimizing for speed, and [[benchmarking_vision_models | benchmarking]] complex multi-turn conversations <a class="yt-timestamp" data-t="01:23:43">[01:23:43]</a>. While the concept of RAG mirrors fundamental computer science ideas like memory and processing <a class="yt-timestamp" data-t="01:19:02">[01:19:02]</a>, its modern applications continue to evolve, with ongoing efforts to balance accuracy, efficiency, and generalization across diverse data types and user interactions <a class="yt-timestamp" data-t="01:31:16">[01:31:16]</a>.