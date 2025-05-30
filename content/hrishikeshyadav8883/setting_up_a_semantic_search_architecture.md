---
title: Setting up a semantic search architecture
videoId: 7ukp3_bZHXo
---

From: [[hrishikeshyadav8883]] <br/> 

This article outlines how to set up a [[video_content_recommendation_engine | video content recommendation engine]] powered by [[semantic_similarity_in_video_recommendations | semantic similarity]] and [[Twelve Labs video embedding and retrieval | Twelve Labs video embedding and retrieval]] for an enhanced user experience <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Traditional vs. Semantic Video Recommendation

Traditionally, video recommendations rely on metadata, descriptions, keywords, transcriptions, or user interaction patterns <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Users are recommended videos based on what similar users interacted with <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

In contrast, this architecture focuses on video understanding through semantics to recommend content that aligns with what the user "feels" or "wants" <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. This is achieved by deeply understanding the video content itself <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

## Core Technologies

The system is powered by:
*   **Twelve Labs**: For embedding videos and text queries using the Marengo Retrieval 2.7 model <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   **Qdrant Cloud**: A vector database used to store video embeddings <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   **AWS S3**: For storing video files and providing public URLs for streaming <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>.
*   **Next.js**: The frontend application framework <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Flask API**: The backend service <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Architecture Breakdown

The entire application architecture can be broken down into two main parts:

### Part 1: Data Ingestion and Embedding Creation (Essential Step)

This initial step involves preparing video content by converting it into an embedding format and storing it in a vector database <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

1.  **Video Collection**: Gather your video content (e.g., 100+ videos) <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
2.  **Upload to AWS S3**: Videos are uploaded from local storage to an S3 bucket to obtain a public URL <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
    *   Dependencies include `boto3` for AWS interaction <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
    *   An `S3 client.upload_file` function handles the upload and returns the public URL <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
3.  **Generate Video Embeddings with Twelve Labs**: The videos are converted into embeddings using the [[Twelve Labs video embedding and retrieval | Twelve Labs Marengo Retrieval 2.7 model]] <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   Ensure the `embedding_scope` is set to "clip" and "video" to generate a single embedding for the whole video <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.
    *   This process takes only a few seconds per video <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
    *   The generated embeddings are stored with the public S3 URL in their metadata <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
4.  **Store in Qdrant Cloud Collection**: The embeddings, along with their metadata (e.g., video ID, S3 URL, original file name), are stored as "points" in a Qdrant Cloud collection <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   Dependencies include `qdrant-client` <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.
    *   Setting up Qdrant Cloud involves registering an account, setting up a cluster, and obtaining API keys and host <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   A `qdrant_client.upload_points` function is used for insertion <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

> [!NOTE] API Keys and Setup
> You can obtain your API key from the [[creating_and_managing_indexes_on_twelve_labs_platform | Twelve Labs playground]] <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Qdrant API keys and host credentials are provided from your Qdrant Cloud cluster <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

### Part 2: Building the Application (Core Functionality)

Once the data is embedded and stored, the application facilitates user interaction and [[video content recommendation engine | video content recommendation]] <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

1.  **User Interaction**: A user provides preferences or a search query through the frontend <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>. This input is typically text <a class="yt-timestamp" data-t="00:05:23">[00:05:23]</a>.
2.  **Text Query to Embedding**: The user's text query is converted into a text embedding using the [[Twelve Labs video embedding and retrieval | Marengo Retrieval 2.7 model]] <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
3.  **Semantic Search in Qdrant**: A semantic search is performed against the Qdrant Cloud collection using the generated text embedding <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
    *   The `query_points` function is used with the collection name, the text query vector, and a limit (e.g., 10 results) <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
    *   Results are returned with a confidence score, with higher confidence results appearing first <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
4.  **Content Recommendation**: Relevant video content is recommended to the user based on the semantic similarity search <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.
    *   The backend structures the output, including the score and video URL, and returns it to the frontend <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
    *   The frontend uses this URL to stream the recommended video <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.

### Backend API (Flask) Implementation

The Flask API handles the core search logic:
*   **Initialization**: Sets up Flask app, [[Twelve Labs video embedding and retrieval | Twelve Labs]], Qdrant client, and loads environment variables for credentials (Twelve Labs API key, Qdrant host, Qdrant API key, collection name) <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. It also initializes the Qdrant collection, creating it if it doesn't exist <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
*   **Search Endpoint (`/search`)**:
    *   Receives a JSON request from the frontend containing the query data <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
    *   Converts the incoming text query into a text embedding using `client.embed.create` with Marengo Retrieval 2.7 <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>.
    *   Performs a similarity search using `qdrant_client.query_points` with the collection name, the generated text vector, and a limit (e.g., 10 results) <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
    *   Formats the results, including score and video URL, and returns them as a JSON response to the frontend <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

### Frontend (Next.js) Implementation

The Next.js frontend interacts with the backend:
*   **Handle Search Function**: This function takes parameters like `category`, `description`, and `query` (e.g., "dark tone" for sci-fi) <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
*   **API Call**: Sends a `POST` request to the backend API's `/search` endpoint (e.g., `process.env.NEXT_PUBLIC_API_URL/search`) <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.
    *   The query is provided in JSON format within the request body <a class="yt-timestamp" data-t="00:14:53">[00:14:53]</a>.
*   **Response Handling**: Receives the data (including video URLs) from the backend <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **Video Streaming**: Processes the received data to display the video URLs for streaming in a video player <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   **Fallback Mechanism**: Includes fallback categories and general fallbacks to provide a default response if the API call fails, preventing errors for the user <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

## Overall Search Flow Diagram

The process of a user query leading to a video recommendation can be summarized as:
1.  **User Input**: User provides a search query or preferences (e.g., "funny animated clips") <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>.
2.  **Post Search Query**: The frontend sends the query to the backend's search endpoint <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
3.  **Generate Text Embedding**: The backend generates a text embedding for the query <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
4.  **Vector Similarity Search**: A vector similarity search is performed in Qdrant Cloud using the query embedding <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>.
5.  **Matching Videos and Metadata**: The search returns matching videos with their metadata and a score <a class="yt-timestamp" data-t="00:16:44">[00:16:44]</a>.
6.  **JSON Response**: A JSON response containing the matching video URLs is sent back to the frontend <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
7.  **Display Video**: The frontend displays the relevant videos to the user using the provided video URLs <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a>.