---
title: Building Fashion Assistance using RAG
videoId: X16N0fvZtt8
---

From: [[hrishikeshyadav8883]] <br/> 

A tutorial demonstrates the development of a [[fashion_ai_assistant_development | fashion assistant platform]] that utilizes [[multimodal_retrieval_in_fashion_platforms | multimodality retrieval]] to provide users with comprehensive fashion advice and product information <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This platform not only retrieves text-based information but also video segments and reels showcasing specific products, alongside styling suggestions <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Platform Features

The fashion assistant offers two primary search functionalities:

### Text-Based Search
Users can query the assistant with text, such as "men's black T-shirt" or "Indian bridal wear" <a class="yt-timestamp" data-t="01:00:23">[01:00:23]</a>. The system's Large Language Model (LLM) provides a rapid response, including:
*   Product name and key features <a class="yt-timestamp" data-t="01:10:52">[01:10:52]</a>
*   Style suggestions on how to wear the product <a class="yt-timestamp" data-t="01:12:30">[01:12:30]</a>
*   Additional style advice <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>
*   Links to product descriptions <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>
*   Video segments showcasing the product, often with similarity scores <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>

For example, a query for a men's black T-shirt might retrieve an "all black daily V t-shirt," suggesting styling it with dark denim jeans and light sneakers <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.

### Visual Search
The platform also supports visual search, allowing users to upload an image to find similar products or video segments where that product appears <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>. Users can specify the number of results to retrieve, and the system displays cards showing products with decreasing similarity scores <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>.

## Architecture and Development

The application is built primarily on [[streamlit_application_development | Streamlit]] for the UI components, using CSS and Markdown for styling <a class="yt-timestamp" data-t="05:17:00">[05:17:00]</a>. All logic is implemented in Python <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>.

### Data Ingestion and Embeddings
To enable the system's functionality, product data is inserted into a vector database <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>. This data includes:
*   Product ID <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>
*   Product link <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>
*   Title <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>
*   Description <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>
*   Video URL <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>

This product catalog data is converted into embeddings <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>:
*   **Text Embeddings:** Title and description are converted using the 12 Labs Embed API with the `meringo retrial 2.7` model <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>.
*   **Video Embeddings:** Video URLs are also converted into video embeddings using the same `meringo retrial 2.7` model, with options to segment video clips (e.g., into 6-second segments) <a class="yt-timestamp" data-t="04:14:00">[04:14:00]</a>.
*   **Image Embeddings:** For visual search, uploaded images are converted into image embeddings <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

These multimodal embeddings are then inserted into a vector database, with Milvus used for this demo <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.

### Retrieval Augmented Generation (RAG) Process
The core of the fashion assistant's response generation is a RAG pipeline <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>:

1.  **User Query:** A user sends a query via the chat interface <a class="yt-timestamp" data-t="11:51:00">[11:51:00]</a>.
2.  **Query Embedding:** The text query is converted into a text embedding using the `meringo retrial 2.7` model <a class="yt-timestamp" data-t="11:59:00">[11:59:00]</a>.
3.  **Semantic Search:** This query embedding is used to find semantically similar embeddings in the vector database <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>. This step retrieves relevant text and video segments (context) <a class="yt-timestamp" data-t="12:23:00">[12:23:00]</a>. The search uses parameters like cosine similarity for distance and `EF` for accuracy/time tradeoff <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.
4.  **Context Generation:** The retrieved relevant information forms the context for the LLM <a class="yt-timestamp" data-t="13:46:00">[13:46:00]</a>.
5.  **LLM Response:** An LLM (OpenAI's GPT-3.5 Turbo is used in this demo) generates a response based on the user's query and the retrieved context <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>. The system defines a "professional fashion advisor and shopping assistant" system role and specifies a desired output format including product name, key features, reasons for matching, and styling advice <a class="yt-timestamp" data-t="14:03:00">[14:03:00]</a>.
6.  **Formatted Output:** The final response includes the LLM's advice, product metadata, and links to relevant video segments, providing a comprehensive [[multimodal_retrieval_in_fashion_platforms | multimodal retrieval]] result <a class="yt-timestamp" data-t="12:48:00">[12:48:00]</a>.

### Development Environment
The project is set up on Replit, allowing for easy experimentation and development without complex environment configurations <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>. The `utils.py` file contains all the core functions for generating embeddings, searching, and handling the RAG pipeline <a class="yt-timestamp" data-t="05:41:00">[05:41:00]</a>.

## Use Cases

The underlying technology, particularly the ability to generate and retrieve multimodal embeddings, has applications beyond fashion assistance <a class="yt-timestamp" data-t="16:12:00">[16:12:00]</a>. Potential use cases include:
*   **E-commerce:** Enhancing product discovery with text, image, and video modalities <a class="yt-timestamp" data-t="16:14:00">[16:14:00]</a>.
*   **Music Discovery:** Identifying music based on various inputs.
*   **Intelligent Video Search Engines:** Improving search capabilities for video content, from journalism to research <a class="yt-timestamp" data-t="16:38:00">[16:38:00]</a>.
*   **Personalized Travel Planners:** Suggesting destinations and activities based on diverse criteria.
*   **Educational Resource Management:** Organizing and retrieving educational content more effectively <a class="yt-timestamp" data-t="16:45:00">[16:45:00]</a>.
*   **Sport Analytics:** Analyzing sports videos and data <a class="yt-timestamp" data-t="16:49:00">[16:49:00]</a>.