---
title: Fashion AI Assistant Development
videoId: X16N0fvZtt8
---

From: [[hrishikeshyadav8883]] <br/> 

This article outlines the development of a fashion assistant platform that leverages [[multimodal_retrieval_in_fashion_platforms | multimodal retrieval]] to provide users with comprehensive fashion advice and product information, including relevant video segments. <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>

## Platform Purpose and Features

The platform's core purpose is to develop a fashion assistant that retrieves information in a [[multimodal_retrieval_in_fashion_platforms | multimodality]] format, offering not only text descriptions but also [[video_segment_generation_and_processing | video segments]] showcasing the product and suggesting styling options. <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a> The platform offers two primary functionalities:

1.  **Text Search (Chat Interface):** Users can ask natural language queries (e.g., "I'm looking for a men's black T-shirt" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a> or "suggest me some Indian bridal wear" <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>) and receive detailed responses.
2.  **Visual Search:** Users can upload an image to find similar products and their corresponding [[video_segment_generation_and_processing | video segments]]. <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>

## Demo Walkthrough

### Text-Based Fashion Assistant
When a user queries the platform, an LLM provides a rapid response. For example, a query for "men's black T-shirt" yields:
*   Product name (e.g., "All Black Daily V T-Shirt"). <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Key features. <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Style suggestions (e.g., "with dark denim jeans, light sneakers for classic"). <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>
*   Additional style advice. <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>
*   Retrieved product descriptions with similarity scores. <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   Relevant [[video_segment_generation_and_processing | video segments]] (e.g., 0-6 seconds, 6-12 seconds, 12-18 seconds), showcasing the product. <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>
The [[video_segment_generation_and_processing | video segments]] are typically 6 seconds long, though this can be adjusted. <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>

### Visual Search for Similar Videos
The visual search feature allows users to upload an image, and the platform returns [[video_segment_generation_and_processing | video segments]] where similar products appear. <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a> Users can specify the number of results to retrieve, and the results are presented with their similarity scores, ordered from highest to lowest. <a class="yt-timestamp" data-t="00:03:13">[00:03:13]</a>

## Data Ingestion and Architecture

### Data Insertion
The platform processes product data, which includes:
*   Product ID <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>
*   Product link <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>
*   Product title <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>
*   Product description <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>
*   Video URL <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>

This product data is converted into embeddings using Twelve Labs APIs:
*   **Text Embeddings:** Product title and description are converted into text embeddings using the Twelve Labs embed API with the Maringo Retrieval 2.7 model. <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>
*   **Video Embeddings:** The video URL is converted into video embeddings using the same model. <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>
These embeddings are then inserted into a vector database, with Milvus being used for this demo. <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>

### System Architecture
The application is built entirely on Streamlit for the UI, with UI components using CSS and Markdown. <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a> The entire logic is implemented in Python. <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>

The project structure includes three main pages:
*   **Main Chat Page:** Handles user queries and displays responses. <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>
*   **Add Product Page:** For inserting new product data into the database. <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
*   **Visual Search Page:** Manages the visual search functionality. <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>

The core logic and utility functions are housed in `utils.py`, making them modular and reusable. <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>

Key technologies and libraries used:
*   **Streamlit:** For building the web application UI. <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>
*   **Twelve Labs SDK:** For generating text and video embeddings. <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>
*   **Milvus:** As the vector database for storing and searching embeddings. <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>
*   **OpenAI:** For Large Language Model (LLM) capabilities (e.g., GPT-3.5 Turbo). <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>

## Core Functionalities

### Similar Videos
The `similar_videos` function takes an image file and a `top_k` parameter (number of results) as input. <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>
1.  The image file is converted into an image embedding using the Twelve Labs client. <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>
2.  This image embedding is used to search for semantically similar video embeddings in the Milvus collection using a cosine similarity search. <a class="yt-timestamp" data-t="00:09:43">[00:09:43]</a>
3.  Results are processed to extract metadata, convert similarity scores to percentages (from -1 to 1 to 0-100%), and format timestamps. <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>

### [[building_fashion_assistance_using_rag | RAG Response]] (Retrieval-Augmented Generation)
The core of the chat interface is the [[building_fashion_assistance_using_rag | RAG response]] mechanism:
1.  **User Query:** The user's text query is sent to be converted into a text embedding using the Maringo Retrieval 2.7 model. <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>
2.  **Semantic Search:** This text embedding is used to find semantically similar text and video embeddings (relevant product information) from the vector database. <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>
3.  **Context Generation:** The retrieved relevant information (text context from products) is used as context for the LLM. <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>
4.  **LLM Interaction:** An OpenAI LLM (e.g., GPT-3.5 Turbo) is prompted with a defined system role (e.g., "professional fashion advisor and shopping assistant") and the user's query augmented with the retrieved context. <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>
5.  **Response Generation:** The LLM generates a comprehensive response that includes product name, key features, reasons why the product matches the need, and style suggestions. <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>
6.  **Multimodal Output:** The final response includes the LLM-generated text, retrieved product metadata, and relevant [[video_segment_generation_and_processing | video segments]], providing a complete [[multimodal_retrieval_in_fashion_platforms | multimodal retrieval]] experience. <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>

## Potential Use Cases

This architecture and approach can be extended to various other domains:
*   **E-commerce:** Enhancing product search and recommendations by incorporating text, image, and video modalities. <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>
*   **Music Discovery:** Building intelligent systems for music search and recommendations. <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>
*   **Intelligent Video Search Engines:** For journalism, research, or content creation. <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>
*   **Personalized Travel Planners:** Leveraging visual and textual data for itinerary suggestions. <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>
*   **Educational Resource Management:** Organizing and retrieving learning materials based on multimodal content. <a class="yt-timestamp" data-t="00:16:45">[00:16:45]</a>
*   **Sports Analytics:** Analyzing video footage and text data for performance insights. <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>