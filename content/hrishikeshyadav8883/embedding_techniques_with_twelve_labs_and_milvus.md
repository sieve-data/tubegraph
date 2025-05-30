---
title: Embedding Techniques with Twelve Labs and Milvus
videoId: X16N0fvZtt8
---

From: [[hrishikeshyadav8883]] <br/> 

This article explores the use of embedding techniques, specifically leveraging the [[twelvelabs_platform_and_capabilities | Twelve Labs platform]] and [[Milvus]] vector database, to build a fashion assistant application. The tutorial demonstrates how to develop a platform that retrieves information in a multimodal format, including text, video segments, and styling suggestions <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Fashion Assistant Platform Capabilities

The platform allows users to query for fashion items and receive detailed responses. For instance, a query for "men's black T-shirt" yields an LLM-generated answer detailing product features, style suggestions (e.g., with dark denim jeans or as a Halloween costume), and additional style advice <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Alongside the text, the platform retrieves product descriptions and relevant video segments that showcase the product, complete with similarity scores and links to view items on a store <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Similar functionality applies to queries like "Indian bridal wear," providing product details and styling advice <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Visual Search Feature

The visual search component enables users to upload a photo and receive video segments where similar items appear <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Users can specify the number of results, and the platform returns cards sorted by similarity score, decreasing from highest to lowest <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>.

## Data Ingestion and Embedding Creation

The foundation of the platform relies on converting product catalog data into embeddings. The data inserted includes product ID, product link, title, description, and video URL <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

*   **Text Embedding**: The product title and description are converted into text embeddings using the [[integration_of_the_twelve_labs_api | Twelve Labs API]] embed API, specifically with the `Maringo retrieval 2.7` model <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Video Embedding**: The video URL is converted into video embeddings using the same `Maringo retrieval 2.7` model. Video clips are segmented, with a default length of 6 seconds, though this can be adjusted <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

Once generated, both text and video embeddings are inserted into a [[Milvus]] vector database, with Zilliz Cloud being used for this demo <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>. The collection in the database thus contains both text and video modalities <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>. Metadata structures are used to maintain authenticity and provide additional information about the original source <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.

## Architecture and Development Environment

The application is built on Streamlit for the UI, using CSS and Markdown for styling <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>. The backend logic is primarily in Python. The project structure includes three main pages: the chat page, an add product page, and a visual search page <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>. The core functions are centralized in `utils.py`, allowing for modular reuse <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

Key libraries and services used include:
*   [[use_of_twelve_labs_sdk | Twelve Labs SDK client]] <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>
*   `pymilvus` for connection with the [[Milvus]] database <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>
*   Streamlit <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>
*   OpenAI for LLM interactions <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>

The development environment is designed for ease of use, with a Replit setup allowing direct development without complex environment configuration <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.

## Retrieving Similar Videos (Visual Search Logic)

The process for retrieving similar videos via visual search involves several steps <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>:
1.  **Input**: An image file and a `topk` value (number of results to retrieve) are provided <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
2.  **Client Initialization**: The [[use_of_twelve_labs_sdk | Twelve Labs client]] is initialized <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
3.  **Image Embedding**: The query image is converted into an image embedding <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
4.  **Semantic Search**: The `collection.search` method (part of [[using_twelvelabs_sdk_and_marango_engine | the Milvus SDK]]) is used to find semantically similar embeddings. Search parameters include cosine similarity for distance, `EF` for accuracy-time tradeoff, and `topk` with `video` type <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
5.  **Result Processing**: The retrieved results are processed by extracting metadata, converting similarity scores (originally -1 to 1 for cosine similarity) into a 0-100 percentage scale for better judgment, and formatting timestamps <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.

## RAG Response (Chat Interface Logic)

The Retrieval Augmented Generation (RAG) response combines LLM capabilities with the retrieved embeddings <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>:
1.  **User Query**: The user sends a text query via the chat interface <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.
2.  **Query Embedding**: The text query is converted into a text embedding using the `Maringo retrieval 2.7` model <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.
3.  **Semantic Search**: Semantic similar text and video embeddings are retrieved from the vector database. The system extracts top matches (e.g., top two text embeddings, top three video embeddings) <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.
4.  **Context Generation**: The retrieved product information and video segments form the context for the LLM <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
5.  **LLM Prompting**: The LLM is given a system role as a "professional fashion advisor and shopping assistant" and instructed to format its response with specific sections like product name, key features, why the product matches the need, and style suggestions <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.
6.  **LLM Response**: OpenAI's `gpt-3.5-turbo` model processes the query and the provided text context, generating a comprehensive response. Parameters like `temperature` (0.7 for creativity) and `max_tokens` are set <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
7.  **Output**: The final output includes the LLM's response, along with retrieved product metadata and video segments, offering a full multimodal retrieval experience <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.

## Potential Use Cases

The embedding techniques demonstrated have broad applicability beyond fashion assistance <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>:
*   **E-commerce**: Enhancing product search and recommendations with multimodal data (text, image, video) <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
*   **Music Discovery**: Powering intelligent search engines for music based on various attributes <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   **Intelligent Video Search Engine**: For diverse fields ranging from journalism to research <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
*   **Personalized Travel Planner**: Suggesting destinations and experiences based on user preferences and multimedia content <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>.
*   **Educational Resource Management**: Organizing and retrieving educational content efficiently <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>.
*   **Sports Analytics**: Analyzing sports videos and data for insights <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.