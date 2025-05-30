---
title: Building a Flask API for video recommendation
videoId: 7ukp3_bZHXo
---

From: [[hrishikeshyadav8883]] <br/> 

This article discusses the process of building a Flask API specifically for a [[video_content_recommendation_engine | video content recommendation engine]] that leverages [[semantic_similarity_in_video_recommendations | semantic similarity in video recommendations]] <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Traditionally, video recommendations have been based on metadata, descriptions, keywords, transcriptions, or user interaction data <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. However, this system focuses on "video understanding" through semantics <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The system is powered by [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] and Qdrant Cloud <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

## Architecture Overview

The application's architecture is divided into two main parts <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>:

1.  **Data Ingestion:** Converting video content into an embedding format and storing it in a vector database <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>. This is an essential prerequisite step <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
2.  **Application Building (Flask API):** After data is embedded, the Flask API handles user queries, performs semantic search, and recommends content <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.

The entire application is built on Next.js for the frontend and a Flask API for the backend <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## 1. Data Ingestion: Video Embedding and Storage

This first step involves processing videos to generate embeddings and store them for efficient retrieval <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

### Process Flow
*   Numerous videos (e.g., 100+) are collected <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
*   Videos are converted into embeddings using the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs Marengo Retrieval 2.7 model]] <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
*   If a public URL isn't available for streaming, videos are stored from local to an S3 bucket to generate a public URL <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   The generated embeddings and the public URL (as metadata) are combined into a "point struct" and stored in Qdrant Cloud <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.

### Key Components & Steps
*   **Dependencies:** `qdrant-client`, `boto3` (for AWS S3), and `twelvelabs` <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   **AWS S3 Setup:** Configuration requires AWS access key, secret key, and bucket name <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>.
    *   `upload_to_s3_bucket`: A function that takes a file path and uploads the video to an S3 bucket, returning its public URL <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.
*   **[[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] Embedding Generation:**
    *   `create_video_embedding`: Uses `client.embed.task` from [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] to generate embeddings from a video path <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   **Crucial:** The `embedding_scope` must be set to `clip` and `video` to get a complete video embedding <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. This process takes only a few seconds <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Qdrant Cloud Insertion:**
    *   The `store_in_qdrant` function takes the embedding (vector), video ID, S3 URL, and original file name, structuring them as a payload <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   This payload is then inserted as a point into the Qdrant Cloud collection <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
    *   Setting up Qdrant Cloud involves registering an account, setting up a cluster, and obtaining API keys and host URL <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## 2. Flask API Backend: Core Functionality

The Flask API handles the main recommendation logic after the video data has been ingested and embedded <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Technology Stack & Dependencies
*   **Framework:** Flask API <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   **Libraries:** `twelvelabs`, `qdrant-client`, `python-dotenv` (for environment variables), `logging`, and `Flask-CORS` (to allow interaction with other origins) <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Scheduler:** `app_scheduler` is used to prevent the API server from sleeping after hosting <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

### Configuration & Initialization
*   **Environment Variables:** Crucial for security, loading `API_KEY` from [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]], `QDRANT_HOST`, `QDRANT_API_KEY` from Qdrant Cloud, and defining `COLLECTION_NAME` (e.g., "content\_collection") and `VECTOR_SIZE` (1024) <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.
*   **Client Initialization:** Both [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] and Qdrant clients are initialized with their respective credentials <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.
*   **Qdrant Collection Check:** The API initializes the Qdrant collection, creating it if it doesn't already exist <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

### The Search Function (`/search` Endpoint)

This is the core of the recommendation engine <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.

1.  **Request Handling:** The API receives a JSON request from the frontend containing the user's query or preferences (e.g., "Sci-Fi," "dark tone") <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.
2.  **Text Embedding Generation:** The incoming text query is converted into a [[semantic_similarity_in_video_recommendations | text embedding]] using `client.embed.create` with the [[twelve_labs_video_embedding_and_retrieval | Marengo Retrieval 2.7 model]] <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. This embedding is stored as a vector <a class="yt-timestamp" data-t="00:11:54">[00:11:54]</a>.
3.  **[[semantic_similarity_in_video_recommendations | Semantic Search]] (Qdrant):**
    *   The `query_points` function of the Qdrant client performs a search using the generated text embedding (vector) against the stored video embeddings in the specified collection <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
    *   A `limit` of 10 is set to retrieve the top 10 most similar videos <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
    *   The search returns results with confidence scores, ordered by highest confidence <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
4.  **Response Generation:** The API structures the received data (including score and video URL) into a JSON object and returns it to the frontend <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

## Frontend Interaction (Next.js)

The frontend, built with Next.js, interacts with the Flask API to provide the user interface for recommendations <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a>.

*   **Calling the API:** The frontend's `handleSearch` function takes the category and query (e.g., "Sci-Fi," "dark tone") <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. It then sends a POST request with the query in JSON format to the backend's `/search` endpoint <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
*   **API URL:** The backend URL (e.g., `Local Host 5000` or a deployed API URL) is typically defined as an environment variable (`process.env.NEXT_PUBLIC_API_URL`) for easier management across development and production environments <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
*   **Response Processing:** Upon receiving data from the backend, the frontend processes it to extract video URLs for streaming <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **Fallback Mechanism:** A fallback method is implemented to handle API failures, providing predefined content to the user instead of an error <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>. This also aids in debugging <a class="yt-timestamp" data-t="00:15:43">[00:15:43]</a>.

## Development and Deployment Notes

*   The code for this application is available on GitHub, with step-by-step instructions for setting up both frontend and backend <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   API keys for [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] can be generated from the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] playground <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   Setting up a Qdrant Cloud cluster is described as straightforward, involving registration and a few clicks to get host and API keys <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

```mermaid
graph TD
    A[User] -->|Provides Preferences / Search Query| B[Frontend (Next.js)]
    B -->|POST Request to /search endpoint| C[Flask API Backend]
    C -->|Convert Text Query to Embedding (Twelve Labs Marengo Retrieval 2.7)| D[Text Embedding]
    D -->|Vector Similarity Search (Qdrant Cloud - query_points)| E[Matching Videos with Metadata & Score]
    E -->|JSON Response| C
    C -->|JSON Response to Frontend| B
    B -->|Display Video with Metadata (Video URL)| F[User Sees Relevant Videos]

    subgraph Data Ingestion (Prerequisite)
        G[Video Content (e.g., 100+ videos)] -->|Upload to AWS S3 (Get Public URL)| H[Public Video URL]
        G -->|Generate Embeddings (Twelve Labs Marengo Retrieval 2.7, scope: clip & video)| I[Video Embedding]
        H & I -->|Combine into Point Struct (Embedding + Metadata)| J[Store in Qdrant Cloud Collection]
    end

    J --|> C
```