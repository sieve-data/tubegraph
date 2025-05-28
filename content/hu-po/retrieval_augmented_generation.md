---
title: retrieval augmented generation
videoId: YLdK-683lCY
---

From: [[hu-po]] <br/> 
## Retrieval Augmented Generation (RAG)

Retrieval Augmented Generation (RAG) is a broad, generic term encompassing various approaches where information is retrieved from a static source to enhance the generation process of a model <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a> <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a> <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a> <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. It functions by fetching relevant information to add context, aiming to reduce hallucinations in AI models <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a> <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

### The Current Landscape of RAG

RAG systems have seen significant recent developments, with powerful systems being released to the public <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. Sam Altman has notably promoted GPT-4o, highlighting its new browsing capabilities as a type of RAG <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a> <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. This category has traditionally been dominated by companies like Google and startups like Perplexity <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a> <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. OpenAI's push into RAG is seen as an attempt to challenge Google's dominance in the search space <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a> <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a> <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

#### Challenges: Hallucinations

Despite the goal of reducing hallucinations, current RAG systems can still exhibit them. For example, when presented with an image of a robot arm from a Chinese startup (Rec Camera), GPT-4o mistakenly identified it as the Boston Dynamics Spot Arm, a well-known robot arm accessory <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a> <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a> <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. Even when given a specific hint like "Rec camera arm," the model hallucinated again, mistaking it for an HTC RE Camera, a periscope-shaped device <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a> <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a> <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a> <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>. This demonstrates that LLMs can still generate incorrect information if asked a question for which there isn't a direct answer in their knowledge base <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a> <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>.

> "The whole point of retrieval augmented generation is that it's a way of kind of reducing hallucinations because you can uh fetch relevant information and then use that information to kind of add context to prevent hallucinations but here it's literally hallucinating..." <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a> <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>

### General Principles of RAG Systems

Many RAG systems involve an "[[agent_loops_and_retrieval_augmented_generation | agent loop]]" or "flow engineering," where a human designs a process for information flow <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a> <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a> <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a> <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>. This process typically includes:
1.  **Understanding the query:** Deciphering what the user is asking <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>.
2.  **Object/Information Identification:** Deciding which objects or pieces of information are relevant and inferring correlations <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a> <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>.
3.  **Text Generation for Search:** Creating appropriate text queries for a search engine <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.
4.  **Content Analysis:** Analyzing information returned from the search engine <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.
5.  **Sufficiency Judgment:** Determining if the retrieved visual and textual information is adequate <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.
6.  **Summarization/Generation:** Summarizing the retrieved information to form a final answer <a class="yt-timestamp" data-t="14:15:00">[14:15:00]</a> <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a> <a class="yt-timestamp" data-t="20:59:00">[20:59:00]</a>.

### Specific RAG Approaches and Papers

#### Vision Search Assistant

This approach focuses on enhancing Vision Language Models (VLMs), which are computationally expensive to update due to the large token size of images <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a> <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a> <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>. The Vision Search Assistant proposes a collaboration between VLMs and web agents to perform open-world retrieval augmented generation <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a> <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.

VLMs often struggle with generalization to recent or specific information, as demonstrated by several VLMs incorrectly identifying the game "Black Myth Wukong" from an image <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a> <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a> <a class="yt-timestamp" data-t="14:54:00">[14:54:00]</a>. The Vision Search Assistant tackles this by:
*   Using an open vocabulary detector to identify regions of interest within an image <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a> <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.
*   Creating a regional caption for each identified region <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a> <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>.
*   Feeding these detailed visual descriptions to a web scraping agent (web knowledge search) and a planning agent, which generates sub-questions and analyzes web pages <a class="yt-timestamp" data-t="19:53:00">[19:53:00]</a> <a class="yt-timestamp" data-t="19:55:00">[19:55:00]</a> <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>.
*   The final answer is generated by combining the original image, user prompt, correlated formulation, and retrieved web knowledge <a class="yt-timestamp" data-t="20:30:00">[20:30:00]</a>.

This approach claims to significantly outperform systems like Perplexity AI Pro and GPT-4o web in human expert evaluations <a class="yt-timestamp" data-t="21:15:00">[21:15:00]</a> <a class="yt-timestamp" data-t="21:24:00">[21:24:00]</a>.

#### AutoMir: Zero-Shot Medical Information Retrieval

AutoMir addresses the challenge of information retrieval from unlabeled and unstructured medical corpora <a class="yt-timestamp" data-t="24:45:00">[24:45:00]</a> <a class="yt-timestamp" data-t="25:08:00">[25:08:00]</a>. It uses a "self-learning hypothetical document embeddings" (SHADE) framework <a class="yt-timestamp" data-t="24:57:00">[24:57:00]</a> <a class="yt-timestamp" data-t="24:59:00">[24:59:00]</a>.

The core idea is an automated, self-supervised training pipeline to create a specialized retrieval model:
*   It starts with a random document from the large, unlabeled database <a class="yt-timestamp" data-t="30:48:00">[30:48:00]</a> <a class="yt-timestamp" data-t="31:12:00">[31:12:00]</a>.
*   A hypothetical question is generated from this document <a class="yt-timestamp" data-t="31:14:00">[31:14:00]</a>.
*   This question is used by a generator to create hypothetical documents (fake answers) <a class="yt-timestamp" data-t="31:17:00">[31:17:00]</a> <a class="yt-timestamp" data-t="31:19:00">[31:19:00]</a>.## Retrieval Augmented Generation (RAG)

Retrieval Augmented Generation (RAG) is a broad, generic term encompassing various approaches where information is retrieved from a static source to enhance the generation process of a model <a class="yt-timestamp" data-t="01:45:00">[01:45:00]</a> <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a> <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a> <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. It functions by fetching relevant information to add context, aiming to reduce hallucinations in AI models <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a> <a class="yt-timestamp" data-t="05:03:00">[05:03:00]</a>.

### The Current Landscape of RAG

RAG systems have seen significant recent developments, with powerful systems being released to the public <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. Sam Altman has notably promoted GPT-4o, highlighting its new browsing capabilities as a type of RAG <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a> <a class="yt-timestamp" data-t="02:39:00">[02:39:00]</a>. This category has traditionally been dominated by companies like Google and startups like Perplexity <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a> <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. OpenAI's push into RAG is seen as an attempt to challenge Google's dominance in the search space <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a> <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a> <a class="yt-timestamp" data-t="06:11:00">[06:11:00]</a>.

#### Challenges: Hallucinations

Despite the goal of reducing hallucinations, current RAG systems can still exhibit them. For example, when presented with an image of a robot arm from a Chinese startup (Rec Camera), GPT-4o mistakenly identified it as the Boston Dynamics Spot Arm, a well-known robot arm accessory <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a> <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a> <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>. Even when given a specific hint like "Rec camera arm," the model hallucinated again, mistaking it for an HTC RE Camera, a periscope-shaped device <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a> <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a> <a class="yt-timestamp" data-t="05:37:00">[05:37:00]</a> <a class="yt-timestamp" data-t="05:39:00">[05:39:00]</a>. This demonstrates that LLMs can still generate incorrect information if asked a question for which there isn't a direct answer in their knowledge base <a class="yt-timestamp" data-t="06:48:00">[06:48:00]</a> <a class="yt-timestamp" data-t="06:50:00">[06:50:00]</a>.

> "The whole point of retrieval augmented generation is that it's a way of kind of reducing hallucinations because you can uh fetch relevant information and then use that information to kind of add context to prevent hallucinations but here it's literally hallucinating..." <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a> <a class="yt-timestamp" data-t="05:16:00">[05:16:00]</a>

### General Principles of RAG Systems

Many RAG systems involve an "[[agent_loops_and_retrieval_augmented_generation | agent loop]]" or "flow engineering," where a human designs a process for information flow <a class="yt-timestamp" data-t="02:30:00">[02:30:00]</a> <a class="yt-timestamp" data-t="12:35:00">[12:35:00]</a> <a class="yt-timestamp" data-t="12:38:00">[12:38:00]</a> <a class="yt-timestamp" data-t="12:40:00">[12:40:00]</a>. This process typically includes:
1.  **Understanding the query:** Deciphering what the user is asking <a class="yt-timestamp" data-t="13:33:00">[13:33:00]</a>.
2.  **Object/Information Identification:** Deciding which objects or pieces of information are relevant and inferring correlations <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a> <a class="yt-timestamp" data-t="13:38:00">[13:38:00]</a>.
3.  **Text Generation for Search:** Creating appropriate text queries for a search engine <a class="yt-timestamp" data-t="13:51:00">[13:51:00]</a>.
4.  **Content Analysis:** Analyzing information returned from the search engine <a class="yt-timestamp" data-t="13:57:00">[13:57:00]</a>.
5.  **Sufficiency Judgment:** Determining if the retrieved visual and textual information is adequate <a class="yt-timestamp" data-t="13:59:00">[13:59:00]</a>.
6.  **Summarization/Generation:** Summarizing the retrieved information to form a final answer <a class="yt-timestamp" data-t="14:15:00">[14:15:00]</a> <a class="yt-timestamp" data-t="20:09:00">[20:09:00]</a> <a class="yt-timestamp" data-t="20:59:00">[20:59:00]</a>.

### Specific RAG Approaches and Papers

#### Vision Search Assistant

This approach focuses on enhancing Vision Language Models (VLMs), which are computationally expensive to update due to the large token size of images <a class="yt-timestamp" data-t="10:44:00">[10:44:00]</a> <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a> <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>. The Vision Search Assistant proposes a collaboration between VLMs and web agents to perform open-world retrieval augmented generation <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a> <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.

VLMs often struggle with generalization to recent or specific information, as demonstrated by several VLMs incorrectly identifying the game "Black Myth Wukong" from an image <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a> <a class="yt-timestamp" data-t="14:45:00">[14:45:00]</a> <a class="yt-timestamp" data-t="14:54:00">[14:54:00]</a>. The Vision Search Assistant tackles this by:
*   Using an open vocabulary detector to identify regions of interest within an image <a class="yt-timestamp" data-t="18:19:00">[18:19:00]</a> <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.
*   Creating a regional caption for each identified region <a class="yt-timestamp" data-t="18:22:00">[18:22:00]</a> <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>.
*   Feeding these detailed visual descriptions to a web scraping agent (web knowledge search) and a planning agent, which generates sub-questions and analyzes web pages <a class="yt-timestamp" data-t="19:53:00">[19:53:00]</a> <a class="yt-timestamp" data-t="19:55:00">[19:55:00]</a> <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>.
*   The final answer is generated by combining the original image, user prompt, correlated formulation, and retrieved web knowledge <a class="yt-timestamp" data-t="20:30:00">[20:30:00]</a>.

This approach claims to significantly outperform systems like Perplexity AI Pro and GPT-4o web in human expert evaluations <a class="yt-timestamp" data-t="21:15:00">[21:15:00]</a> <a class="yt-timestamp" data-t="21:24:00">[21:24:00]</a>.

#### AutoMir: Zero-Shot Medical Information Retrieval

AutoMir addresses the challenge of information retrieval from unlabeled and unstructured medical corpora <a class="yt-timestamp" data-t="24:45:00">[24:45:00]</a> <a class="yt-timestamp" data-t="25:08:00">[25:08:00]</a>. It uses a "self-learning hypothetical document embeddings" (SHADE) framework <a class="yt-timestamp" data-t="24:57:00">[24:57:00]</a> <a class="yt-timestamp" data-t="24:59:00">[24:59:00]</a>.

The core idea is an automated, self-supervised training pipeline to create a specialized retrieval model:
*   It starts with a random document from the large, unlabeled database <a class="yt-timestamp" data-t="30:48:00">[30:48:00]</a> <a class="yt-timestamp" data-t="31:12:00">[31:12:00]</a>.
*   A hypothetical question is generated from this document <a class="yt-timestamp" data-t="31:14:00">[31:14:00]</a>.
*   This question is used by a generator to create hypothetical documents (fake answers) <a class="yt-timestamp" data-t="31:17:00">[31:17:00]</a> <a class="yt-timestamp" data-t="31:19:00">[31:19:00]</a>.
*   A retriever model then ranks documents in the database based on these hypothetical documents to find the most relevant ones <a class="yt-timestamp" data-t="32:26:00">[32:26:00]</a> <a class="yt-timestamp" data-t="32:29:00">[32:29:00]</a>.
*   This process automatically constructs a labeled fine-tuning dataset, including "hard negative mining" to differentiate between very similar texts <a class="yt-timestamp" data-t="27:54:00">[27:54:00]</a> <a class="yt-timestamp" data-t="30:21:00">[30:21:00]</a> <a class="yt-timestamp" data-t="30:35:00">[30:35:00]</a>.

This automated pipeline iteratively refines both the pseudo document generation and the retrieval process, creating highly specialized models for domain-specific, unlabeled corpora <a class="yt-timestamp" data-t="25:04:00">[25:04:00]</a> <a class="yt-timestamp" data-t="31:09:00">[31:09:00]</a>.

A retrieval model's training generally has two stages <a class="yt-timestamp" data-t="26:30:00">[26:30:00]</a>:
1.  **Unsupervised pre-training:** Uses large volumes of unlabeled text to learn domain knowledge, e.g., medical terminology <a class="yt-timestamp" data-t="26:33:00">[26:33:00]</a> <a class="yt-timestamp" data-t="26:35:00">[26:35:00]</a>.
2.  **Supervised fine-tuning:** Uses a high-quality labeled dataset, often alongside hard negative mining, to enable the model to differentiate between similar texts <a class="yt-timestamp" data-t="27:50:00">[27:50:00]</a> <a class="yt-timestamp" data-t="27:52:00">[27:52:00]</a>.

#### Zero-Shot Dense Retrieval with Embeddings from Relevance Feedback

This paper addresses the latency issue in previous hypothetical document generation methods, where an LLM generates many tokens before retrieval can begin <a class="yt-timestamp" data-t="35:22:00">[35:22:00]</a> <a class="yt-timestamp" data-t="35:25:00">[35:25:00]</a>.
The proposed "real document embeddings from relevance feedback" (RDFR) method uses an LLM to select documents for nearest neighbor search <a class="yt-timestamp" data-t="36:04:00">[36:04:00]</a> <a class="yt-timestamp" data-t="36:05:00">[36:05:00]</a>. The key innovation is that the relevance estimation only requires the LLM to output a single token (e.g., 0 for irrelevant, 1 for relevant) <a class="yt-timestamp" data-t="36:12:00">[36:12:00]</a> <a class="yt-timestamp" data-t="36:15:00">[36:15:00]</a>. This minimum viable action significantly reduces retrieval latency, offering a 7.5 to 11x speed improvement <a class="yt-timestamp" data-t="38:05:00">[38:05:00]</a> <a class="yt-timestamp" data-t="38:08:00">[38:08:00]</a>.

#### Coral: Benchmarking Multi-Turn Conversational Retrieval Augmented Generation

Coral introduces a large-scale benchmark for multi-turn information-seeking conversations in RAG systems <a class="yt-timestamp" data-t="39:51:00">[39:51:00]</a> <a class="yt-timestamp" data-t="39:53:00">[39:53:00]</a>. Traditional RAG benchmarks are often single-turn, but real-world interactions are multi-turn <a class="yt-timestamp" data-t="40:01:00">[40:01:00]</a> <a class="yt-timestamp" data-t="40:26:00">[40:26:00]</a>.

Multi-turn settings require systems to:
*   Deal with redundant or irrelevant information from prior interactions <a class="yt-timestamp" data-t="39:58:00">[39:58:00]</a>.
*   Cope with abrupt topic shifts <a class="yt-timestamp" data-t="40:39:00">[40:39:00]</a>.
*   Provide [[using_gpt_api_for_conversation_generation | free-form responses]] with detailed, contextually rich answers <a class="yt-timestamp" data-t="41:37:00">[41:37:00]</a>.
*   Handle open-domain questions and retrieve deep contextual knowledge <a class="yt-timestamp" data-t="41:28:00">[41:28:00]</a> <a class="yt-timestamp" data-t="41:32:00">[41:32:00]</a>.
*   Include citation labeling (though the speaker notes the challenges in verifying cited sources) <a class="yt-timestamp" data-t="41:46:00">[41:46:00]</a>.

The Coral dataset is automatically derived from Wikipedia, using its structured knowledge graph to create synthetic multi-turn conversations through various graph traversal techniques (e.g., breadth-first search, depth-first search, linear descent sampling, dual tree random walk) <a class="yt-timestamp" data-t="42:22:00">[42:22:00]</a> <a class="yt-timestamp" data-t="42:26:00">[42:26:00]</a> <a class="yt-timestamp" data-t="43:35:00">[43:35:00]</a> <a class="yt-timestamp" data-t="44:43:00">[44:43:00]</a>.

#### Beyond Text: Optimizing RAG with Multimodal Inputs

This paper explores how to integrate multimodal models into RAG systems, specifically focusing on image processing and retrieval <a class="yt-timestamp" data-t="48:16:00">[48:16:00]</a> <a class="yt-timestamp" data-t="48:48:00">[48:48:00]</a>. It addresses LLMs' lack of domain-specific knowledge and their propensity for hallucinations <a class="yt-timestamp" data-t="48:20:00">[48:20:00]</a> <a class="yt-timestamp" data-t="48:23:00">[48:23:00]</a>.

Two main strategies are explored:
1.  **Multimodal embeddings and separate vector stores:** Images are encoded into image embeddings and text into text embeddings, stored in separate databases. Search is performed separately, and results are combined <a class="yt-timestamp" data-t="49:11:00">[49:11:00]</a> <a class="yt-timestamp" data-t="49:13:00">[49:13:00]</a>.
2.  **Image summaries in a combined vector store:** Images are first processed to extract text (e.g., image captions or "image summaries"), then these texts are converted into text embeddings. Both original text and image-derived text are stored in a single vector database, allowing a unified text-based search <a class="yt-timestamp" data-t="51:15:00">[51:15:00]</a> <a class="yt-timestamp" data-t="51:17:00">[51:17:00]</a>.

The findings suggest that using image summaries (converting images to text for embedding) in a combined vector store performs better than separate multimodal stores <a class="yt-timestamp" data-t="51:17:00">[51:17:00]</a> <a class="yt-timestamp" data-t="51:21:00">[51:21:00]</a> <a class="yt-timestamp" data-t="52:16:00">[52:16:00]</a>. This implies that using text-based embeddings for all modalities can be more effective for RAG.

#### Rare: Retrieval Augmented Retrieval with In-Context Examples

This paper investigates whether adding in-context examples can improve embedding model performance in retrieval <a class="yt-timestamp" data-t="56:56:00">[56:56:00]</a>. In-context examples involve providing a few examples of query-document pairs alongside the target query to guide the model <a class="yt-timestamp" data-t="57:57:00">[57:57:00]</a> <a class="yt-timestamp" data-t="57:59:00">[57:59:00]</a>.

A key finding is that simply adding in-context examples to the query *without* fine-tuning the embedding model generally *decreases* performance <a class="yt-timestamp" data-t="57:17:00">[57:17:00]</a> <a class="yt-timestamp" data-t="57:24:00">[57:24:00]</a>. This is attributed to the "fragile" nature of retrieval models, which can suffer from catastrophic forgetting if fine-tuned on a narrow distribution <a class="yt-timestamp" data-t="58:32:00">[58:32:00]</a> <a class="yt-timestamp" data-t="58:50:00">[58:50:00]</a>.

The paper fine-tunes retrieval models specifically to leverage in-context examples <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a> <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a>. However, the results show that while there can be significant improvements for specific benchmarks (e.g., a 10-point improvement on Cact, a science fact-based benchmark), for many others, it does not significantly improve performance and can even make it worse <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a> <a class="yt-timestamp" data-t="01:01:12">[01:01:12]</a> <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a> <a class="yt-timestamp" data-t="01:02:10">[01:02:10]</a> <a class="yt-timestamp" data-t="01:02:16">[01:02:16]</a>. This suggests that adding in-context examples might not be universally beneficial and can introduce latency without proportional performance gains <a class="yt-timestamp" data-t="01:03:06">[01:03:06]</a> <a class="yt-timestamp" data-t="01:03:10">[01:03:10]</a>.

### The Future of RAG

The current state of RAG indicates a lot of exploration and varied ideas without a clear "winner" <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a> <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a> <a class="yt-timestamp" data-t="01:31:16">[01:31:16]</a> <a class="yt-timestamp" data-t="01:31:21">[01:31:21]</a>. The future of RAG systems and LLMs might follow two paths:
*   **Longer context windows:** As context lengths increase, it might become feasible to simply feed all relevant information directly into the model's context, reducing the need for complex multi-step RAG pipelines <a class="yt-timestamp" data-t="00:46:47">[00:46:47]</a> <a class="yt-timestamp" data-t="00:47:01">[00:47:01]</a> <a class="yt-timestamp" data-t="01:10:06">[01:10:06]</a>. This would shift the cost to inference.
*   **Continuous learning/fine-tuning:** Alternatively, models could be continuously fine-tuned with new information (e.g., daily news) by pushing gradients <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a> <a class="yt-timestamp" data-t="01:10:48">[01:10:48]</a>. This would reduce the need for large context windows during inference but increase training costs.

The optimal path depends on factors like query types, architectural advancements for long contexts, and the capabilities of future training hardware <a class="yt-timestamp" data-t="01:11:38">[01:11:38]</a>. Regardless, RAG represents a modern re-framing of fundamental computer science concepts involving memory (space) and processing inputs over time <a class="yt-timestamp" data-t="01:17:10">[01:17:10]</a> <a class="yt-timestamp" data-t="01:17:40">[01:17:40]</a>.