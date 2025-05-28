---
title: comparison of image and textbased retrieval methods
videoId: YLdK-683lCY
---

From: [[hu-po]] <br/> 

Retrieval Augmented Generation (RAG) systems aim to reduce hallucinations and provide more accurate responses by fetching relevant information from external knowledge bases [00:05:00]. This article explores different approaches to integrating image and text information within RAG, highlighting their trade-offs and effectiveness.

## The Challenge of Multimodal Information Retrieval
Large Language Models (LLMs) often lack domain-specific knowledge and are prone to hallucinations, especially when dealing with complex or real-world visual information [00:48:20]. For instance, GPT-4o, despite its browsing capabilities, hallucinated when asked to identify a specific robot arm from an image, incorrectly identifying it as a [[feature_matching_in_computer_vision | Boston Dynamics Spot arm]] [00:03:00, 00:04:30]. This demonstrates the difficulty in retrieving accurate information based on visual inputs alone.

Updating Vision Language Models (VLMs) is computationally burdensome due to the large size of images, making frequent retraining impractical [00:10:42]. This makes it challenging for VLMs to stay current with recent visual information, as demonstrated by several VLMs failing to identify the "Black Myth Wukong" game from an image, mistaking it for older or different titles [00:14:51].

## Approaches to Multimodal RAG

Several methods are explored to integrate multimodal inputs, particularly images, into RAG systems effectively.

### 1. Vision Search Assistant: Image-to-Text Conversion
The **Vision Search Assistant (VSA)** proposes a collaboration between Vision Language Models (VLMs) and web agents (LLMs that scrape the internet) to perform open-world retrieval augmented generation [00:11:41]. Its key idea is **visual content formulation** through regional captioning [00:18:19].

*   **Process**:
    1.  An open vocabulary detector identifies regions of interest within an image [00:18:19].
    2.  Each region receives a specialized caption [00:18:46].
    3.  These regional captions, along with the user's query, are expanded into more detailed text for a web knowledge search [00:19:56].
    4.  A planning agent breaks down the query into components (event name, time, place, effect) to guide the search [00:20:00].
    5.  The retrieved web pages are analyzed, selected, and summarized by an LLM [00:20:25].
    6.  The original image, user prompt, correlated formulation, and obtained web knowledge are used to generate the final answer [00:20:30].
*   **Advantages**: This method effectively turns visual information into text, which can then be processed by text-based search and retrieval mechanisms [00:23:43]. It demonstrated success in identifying recent visual content that traditional VLMs failed on [00:15:50]. Human expert [[evaluation_of_retrieval_models | evaluation]] suggested VSA significantly outperformed Perplexity AI Pro and GPT-4o web in accuracy [00:21:24].
*   **Disadvantages**: This process involves multiple steps of text generation and expansion, which could potentially introduce latency [00:24:00].

### 2. "Beyond Text": Multimodal Embeddings vs. Image Summaries
This paper conducts experiments on integrating multimodal models into RAG systems, focusing on image processing and retrieval [00:48:48]. It compares two main approaches:

*   **Multimodal Embeddings with Separate Vector Stores**:
    *   Images are encoded into image embeddings and stored in a dedicated image vector database.
    *   Text is encoded into text embeddings and stored in a separate text vector database [00:49:11].
    *   Retrieval involves searching both databases separately and then combining the results [00:51:08].
*   **Image Summaries in a Combined Vector Store**:
    *   Images are extracted and converted into text summaries (or captions) [00:51:21].
    *   These image summaries are then turned into text embeddings.
    *   Both the image-derived text embeddings and original text embeddings are stored in a single, combined vector database [00:51:34].
    *   Retrieval is performed using text embeddings across this unified store [00:51:46].
*   **Findings**: The study found that using **image summaries (turning images into text) performs better** in terms of answer correctness compared to approaches that solely rely on image embeddings or separate stores [00:52:13, 00:56:18]. This suggests that converting visual information into a textual format for retrieval is often more effective for current RAG systems.

### 3. Call P: Direct Image Embedding for Document Retrieval
Call P explores efficient document retrieval with vision language models [01:04:04]. In contrast to methods that extract and summarize text content from PDFs (e.g., OCR, document layout detection) and then embed that text, Call P proposes a simpler approach:

*   **Process**:
    1.  Chunk the entire PDF (or document) into images [01:05:36].
    2.  Feed each image chunk directly into a large image encoder to obtain image embeddings [01:05:40].
    3.  Use these image embeddings for similarity search in a vector database [01:05:45].
*   **Comparison with Standard Retrieval**:
    *   **Standard Retrieval (Text-based)**: Takes a PDF, performs OCR to extract text, embeds the text, and searches for text embeddings. It also extracts images and possibly embeds them separately [01:05:16].
    *   **Call P (Image-based)**: Chunks the PDF into images and embeds those image chunks directly [01:05:36].
*   **Advantages**: This approach is simpler and potentially faster for document retrieval, showing competitive performance on benchmarks [01:07:39]. The creation of these embeddings can be done offline, reducing inference latency [01:06:26].
*   **Trade-off**: While simpler and efficient for document retrieval, this method focuses on finding similar *pages* rather than specific textual content within them, potentially requiring further processing by an LLM to extract precise answers.

## General Observations and Future Outlook

*   **Flow Engineering**: Many current RAG papers emphasize "flow engineering" or "agent loops," where human-designed processes orchestrate the flow of information between different models (e.g., VLM, LLM, retrieval model) [01:12:40].
*   **Cost vs. Latency**: There's a constant trade-off between retrieval speed (latency) and accuracy [00:30:30]. Generating full hypothetical documents for search is slower than simply producing a single token to determine relevance [00:35:30, 00:37:04].
*   **Context Length vs. Fine-tuning**: The future of RAG might involve either:
    1.  LLMs with extremely long context windows, allowing all relevant information to be included in the prompt, simplifying the pipeline but increasing inference cost [01:10:06].
    2.  More frequent fine-tuning (continual learning) of models with new data, reducing the need for large contexts during inference but increasing training costs [01:10:34]. The optimal path depends on hardware advancements and query patterns [01:11:58].
*   **Embedding Dimensions**: Increasing the dimensions of embeddings can cram more information into the embedding space, leading to better information retrieval accuracy, but it also increases computation time and memory requirements [01:14:13]. As computing power advances, embedding sizes are expected to grow [01:15:05].

The field of RAG is still actively exploring different ideas, with no clear single "winner" approach yet [01:31:19]. The effectiveness of image and text-based retrieval methods heavily depends on the specific application, data characteristics, and desired trade-offs between speed, accuracy, and computational resources.