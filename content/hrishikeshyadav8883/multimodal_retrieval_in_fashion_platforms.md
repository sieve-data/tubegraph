---
title: Multimodal Retrieval in Fashion Platforms
videoId: X16N0fvZtt8
---

From: [[hrishikeshyadav8883]] <br/> 

This article discusses the development of a [[fashion_ai_assistant_development | fashion assistant]] platform that utilizes multimodal retrieval to provide comprehensive product information and styling advice <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The platform aims to integrate text and video content for a richer user experience <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Platform Overview

The platform allows users to search for fashion items and receive detailed responses including:
*   Textual product descriptions <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>
*   Key features <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>
*   Style suggestions <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>
*   Relevant video segments showcasing the product <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a> <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>

### Demo Examples

*   **Men's Black T-shirt Query:** When asked for a "men's black T-shirt," the system provides an LLM-generated answer with product details (e.g., "all black daily V t-shirt"), key features, and styling advice such as pairing it with dark denim jeans or light sneakers <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a> <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. It also retrieves product descriptions and specific video segments where the T-shirt is featured <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a> <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Video segments can be as short as 6 seconds <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Indian Bridal Wear Query:** A query for "Indian bridal wear" yields results like a "crafted Lea or Brides made collection" with styling advice and relevant video segments <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a> <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

## [[Integration of Visual Search in Ecommerce | Visual Search]] Capability

The platform also includes a [[integration_of_visual_search_in_ecommerce | visual search]] feature where users can upload an image to find relevant video segments <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a> <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This allows for product similarity exploration based on visual input <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Technical Architecture

The platform is primarily built using Streamlit for the UI, with CSS and Markdown for styling, and all logic implemented in Python <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a> <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a> <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.

### Core Components
*   **Pages:** The application is structured with three main pages: the chat interface, an add product page, and the [[integration_of_visual_search_in_ecommerce | visual search]] page <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a> <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>.
*   **`utils.py`:** This file contains all the core functions and logic, designed to be modular and reusable <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a> <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>.
*   **Vector Database:** Milvus is used as the vector database for storing and retrieving embeddings <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a> <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>. For the demo, Zilliz Cloud (Milvus vector database) is utilized <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **[[Twelve Labs video embedding and retrieval | Embedding]] Generation:**
    *   [[Twelve Labs video embedding and retrieval | Twelve Labs]] Embed API, specifically the Meringo Retrieval 2.7 model, is used to convert text (product title, description) and video URLs into embeddings <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a> <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a> <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
    *   The platform can segment videos into specified clip lengths (e.g., 6 seconds) for more granular [[twelve_labs_video_embedding_and_retrieval | video embedding]] <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **LLM Integration:** OpenAI's GPT-3.5 Turbo model is used for generating responses and styling advice <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a> <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a> <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.

### Data Ingestion Process
Product data, including product ID, link, title, description, and video URL, is inserted into the system <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This data is then converted into embeddings:
1.  Text data (title, description) becomes text embeddings <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
2.  Video URLs become [[twelve_labs_video_embedding_and_retrieval | video embeddings]] <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.
Both types of embeddings are then inserted into the Milvus vector database, creating a collection with two modalities <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a> <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### Multimodal Retrieval Flow (Text Query)

1.  **User Query:** A user sends a text query (e.g., "suggest me a black T-shirt") through the chat interface <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a> <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.
2.  **Query [[Twelve Labs video embedding and retrieval | Embedding]]:** The text query is converted into a text embedding using Meringo Retrieval 2.7 <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a> <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.
3.  **Semantic Search:** This embedding is used to find [[semantic_similarity_in_video_recommendations | semantically similar]] embeddings (both text and video) in the vector database <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a> <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. The search uses parameters like cosine similarity and `ef` for accuracy-time tradeoff <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a> <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
4.  **Context Generation:** The retrieved relevant product descriptions (text) and video metadata are compiled <a class="yt-timestamp" data-t="00:12:26">[00:12:26]</a> <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
5.  **LLM Response Generation:** This retrieved context is then sent to an LLM (OpenAI) along with a defined system role ("professional fashion advisor and shopping assistant organizer") and a specific output format request <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a> <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a> <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>. The LLM generates a comprehensive response, including product name, key features, why it matches the need, and style suggestions <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>.
6.  **Presentation:** The system presents the LLM's response, relevant product metadata, and video segments to the user, offering a complete multimodal retrieval experience <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a> <a class="yt-timestamp" data-t="00:15:02">[00:15:02]</a>.

### Visual Search Flow

1.  **Image Upload:** User uploads an image <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
2.  **Image [[Twelve Labs video embedding and retrieval | Embedding]]:** The image is converted into an image embedding by the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] client <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.
3.  **Vector Search:** This image embedding is used to search the vector database for [[semantic_similarity_in_video_recommendations | semantically similar]] video embeddings <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.
4.  **Result Processing:** The results are processed to extract metadata, convert similarity scores to percentages, and format timestamps before being displayed to the user <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

## Broader [[Use cases for video understanding | Use Cases]]

The principles demonstrated in this [[fashion_ai_assistant_development | fashion AI assistant]] can be applied to various other domains and [[Use cases for video understanding | use cases for video understanding]], leveraging the [[twelve_labs_video_embedding_and_retrieval | embedding API]] for multimodal data:
*   **E-commerce:** Particularly for portals integrating multiple modalities like text, image, and short-form videos <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a> <a class="yt-timestamp" data-t="00:16:21">[00:16:21]</a>.
*   **Music Discovery** <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>
*   **Intelligent [[video_content_recommendation_engine | Video Search Engine]]** <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>
*   **Personalized Travel Planner** <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>
*   **Educational Resource Management** <a class="yt-timestamp" data-t="00:16:46">[00:16:46]</a>
*   **Sports Analytics** <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>

The development environment is designed for ease of use, with a pre-configured Replit environment allowing developers to directly build and experiment without extensive setup <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a> <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.