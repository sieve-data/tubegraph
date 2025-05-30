---
title: Integration of Visual Search in Ecommerce
videoId: X16N0fvZtt8
---

From: [[hrishikeshyadav8883]] <br/> 

This article explores the integration of visual search capabilities within an e-commerce platform, specifically demonstrated through a fashion assistant. The platform aims to provide a [[multimodal_retrieval_in_fashion_platforms | multimodal retrieval]] experience, offering not only text-based information but also relevant video segments and styling suggestions <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Fashion Assistant Platform Overview

The fashion assistant platform allows users to query for fashion items and receive comprehensive results. The underlying data for the demo primarily consists of bridal wear, black T-shirts, and black dresses <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Text-Based Search
Users can input text queries, such as "men's black T-shirt" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The system utilizes a Large Language Model (LLM) to provide a fast response <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. For a black T-shirt query, the response includes:
*   Product name (e.g., "all black daily V t-shirt") <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Key features <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Style suggestions (e.g., with dark denim jeans and sneakers) <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Additional style advice <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>

Accompanying the text response, the platform retrieves relevant product descriptions and [[video_content_recommendation_engine | video segments]] that showcase the product <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Each retrieved item displays a [[semantic_similarity_in_video_recommendations | similarity score]] <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Users can also view the product on the store directly <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Video segments are shown with specific timestamps (e.g., 0-6 seconds, 6-12 seconds) highlighting where the product appears <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

### Visual Search
The platform also incorporates a visual search feature, allowing users to upload a photo to find corresponding video segments <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. When an image is provided, the system returns [[video_content_recommendation_engine | video segments]] where similar items occur <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. The number of results can be adjusted by the user (e.g., from two to six) <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>. Results are presented with a [[semantic_similarity_in_video_recommendations | similarity score]], ordered from highest to lowest <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## Technical Architecture

The fashion assistant demo is built using Streamlit for the user interface, with Python for the backend logic <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. Key components and processes include:

### Data Ingestion and Embedding Generation
Product data, including product ID, link, title, description, and video URL, is ingested into the system <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This data is then converted into embeddings:
*   **Text Embedding**: Product title and description are converted into text embeddings using the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs embed API]] with the Meringo Retrieval 2.7 model <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Video Embedding**: The video URL is converted into a video embedding using the same [[twelve_labs_video_embedding_and_retrieval | Twelve Labs embed API]] model <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>. Video clips can be segmented (e.g., every 6 seconds) for more granular retrieval <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

These [[embedding_techniques_with_twelve_labs_and_milvus | embeddings]] (both text and video) are then inserted into a [[setting_up_a_semantic_search_architecture | vector database]], with Milvus being the chosen database for this demo <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. Metadata is also structured and stored alongside the embeddings to provide context and authenticity <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

### Visual Search Implementation Details
When a user uploads an image for visual search:
1.  The image file is provided to a function `s_similar_videos` <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
2.  The [[twelve_labs_video_embedding_and_retrieval | Twelve Labs client]] is initialized <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
3.  The query image is converted into an image embedding <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
4.  This image embedding is then used to search the Milvus [[setting_up_a_semantic_search_architecture | collection]] for semantically similar video embeddings <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>.
5.  Search parameters include cosine similarity for distance measurement and `ef` for balancing accuracy and time <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>.
6.  The `top_k` parameter determines the number of segments to retrieve <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
7.  Results are processed by extracting metadata, converting similarity scores to a percentage scale (from -1 to 1 to 0-100%), and formatting timestamps <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Retrieval-Augmented Generation (RAG) for Text Queries
For text-based queries, the system employs a RAG approach to generate comprehensive responses:
1.  The user's text query is converted into a text embedding using [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] Meringo Retrieval 2.7 <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
2.  This text embedding is used to find [[semantic_similarity_in_video_recommendations | semantically similar embeddings]] (both text and video) from the [[setting_up_a_semantic_search_architecture | vector database]] <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
3.  The retrieved relevant segments (text and video) serve as context for the LLM <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a>.
4.  An OpenAI LLM (GPT-3.5 Turbo) generates a response based on the retrieved context, with a defined system role (e.g., "professional fashion advisor and shopping assistant") and a specific output format <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
5.  The response includes product name, key features, reasons the product matches the need, and styling suggestions <a class="yt-timestamp" data-t="00:14:18">[00:14:18]</a>.
6.  The final output to the user includes the LLM response, product metadata, and retrieved [[video_content_recommendation_engine | video segments]], completing the [[multimodal_retrieval_in_fashion_platforms | multimodal retrieval]] <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

## Broader Use Cases for Video Understanding

The [[embedding_techniques_with_twelve_labs_and_milvus | embedding techniques]] and multimodal retrieval demonstrated in this fashion assistant have wide-ranging [[use_cases_for_video_understanding | applications]] beyond e-commerce, including:
*   **E-commerce**: Particularly for platforms adding more modalities like images and short-form videos <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
*   **Music Discovery**: Identifying music based on various inputs <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   **Intelligent [[video_content_recommendation_engine | Video Search Engine]]**: For journalists, researchers, or general content discovery <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **Personalized Travel Planner**: Recommending destinations or experiences based on visual or textual preferences <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
*   **Educational Resource Management**: Finding relevant educational content, potentially across different media types <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
*   **Sport Analytics**: Analyzing sports videos for specific events or player actions <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

This technology makes it easier for developers to build applications without extensive environment configuration <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.