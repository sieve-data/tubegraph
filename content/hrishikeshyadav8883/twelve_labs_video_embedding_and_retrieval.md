---
title: Twelve Labs video embedding and retrieval
videoId: 7ukp3_bZHXo
---

From: [[hrishikeshyadav8883]] <br/> 

This article explores the use of [[twelvelabs_platform_and_capabilities | Twelve Labs]] for building a [[video_content_recommendation_engine | video content recommendation engine]] based on semantic similarity of videos <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Traditionally, video recommendations rely on metadata, descriptions, keywords, transcriptions, or user interaction data <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. However, this approach focuses on understanding the video content through semantics to provide more relevant recommendations <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Core Components and Workflow

The system leverages [[twelvelabs_platform_and_capabilities | Twelve Labs]] for video embeddings, storing these embeddings in Qdrant Cloud, and using Qdrant's search capabilities for quick results <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. The application is built with Next.js for the frontend and a Flask API for the backend <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Video Ingestion and Embedding

This first essential step involves converting video content into an embedding format and storing it in a vector database <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

The process includes:
1.  **Video Collection:** Gathering numerous video files <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  **Embedding Generation:** Videos are converted into embeddings using the [[twelvelabs_platform_and_capabilities | Twelve Labs]] Maringo Retrieval 2.7 model <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.
    *   The `embedding_scope` is set to 'clip' and 'video' to ensure a complete video is treated as a single embedding <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.
    *   The [[use_of_twelve_labs_sdk | Twelve Labs SDK]] client's `ed.task` function is used for this <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
3.  **S3 Upload for Public URLs:** If a public URL for streaming is not available, videos are stored locally, then uploaded to an S3 bucket to obtain a public URL <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. This public URL is then stored as metadata alongside the embedding <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
    *   Boto 3 is used for AWS S3 interactions <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
4.  **Quadrant Cloud Insertion:** The generated embedding and its associated metadata (including the S3 public URL) are stored as "points" in a Qdrant Cloud collection <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
    *   The Qdrant client is initialized with credentials (host and API key) from the Qdrant Cloud cluster <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>.
    *   The `vector` (embedding), `video ID`, `S3_URL`, and `original_file_name` are included in the payload for insertion <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

```python
# Example pseudo-code for embedding creation and insertion
# (based on transcript description)
# client.ed.task(video_path, embedding_scope=['clip', 'video'])
# s3_url = upload_to_s3(video_path)
# quadrant_client.upsert(
#     collection_name='content_collection',
#     points=[
#         {
#             "vector": embedding_vector,
#             "payload": {
#                 "video_id": video_id,
#                 "s3_url": s3_url,
#                 "original_file_name": original_name
#             }
#         }
#     ]
# )
```
<a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a> <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>

### Querying and Retrieval

After the video data is embedded and stored, the application becomes functional:
1.  **User Query:** A user provides preferences, typically as text input (e.g., "Fantasy and musical" or "sci-fi" with a "dark tone") <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>.
2.  **Text Embedding Generation:** The text query is converted into a text embedding using the same Maringo Retrieval 2.7 model <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>.
    *   This is done via `client.ed.create` with the text input <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
3.  **Semantic Search:** A semantic search is performed against the Qdrant Cloud collection using the generated text embedding <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
    *   The `query_points` function of the Qdrant client is used <a class="yt-timestamp" data-t="00:12:01">[00:12:01]</a>.
    *   The search specifies the collection name, the query vector, and a limit (e.g., 10 results) <a class="yt-timestamp" data-t="00:12:07">[00:12:07]</a>.
4.  **Content Recommendation:** Relevant video content recommendations are returned based on the semantic similarity score <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. The results include the video URL and a confidence score <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>.

## [[integration_of_the_twelve_labs_api | Integration and Implementation Details]]

The backend Flask API handles the [[integration_of_the_twelve_labs_api | integration of the Twelve Labs API]] and Qdrant client <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. Key dependencies include `flask`, `twelvelabs`, `qdrant-client`, `boto3`, and `python-dotenv` <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>. API keys and host information for [[twelvelabs_platform_and_capabilities | Twelve Labs]] and Qdrant are loaded from environment variables for security <a class="yt-timestamp" data-t="00:09:55">[00:09:55]</a>.

The `search` endpoint in the Flask API receives text queries from the frontend, generates text embeddings using [[twelvelabs_platform_and_capabilities | Twelve Labs]], performs a vector similarity search in Qdrant, and returns the top relevant videos <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>.

The frontend (Next.js) sends queries to the backend API via a `POST` method with the query data in JSON format <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. Upon receiving the backend response, it processes the data to display the video URLs for streaming <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. Fallback methods are also implemented to provide a default response if the API call fails <a class="yt-timestamp" data-t="00:15:21">[00:15:21]</a>.

This architecture enables a robust [[video_content_recommendation_engine | video content recommendation engine]] by deeply understanding video content through embeddings rather than just metadata, facilitating an efficient [[video indexing and processing | video indexing and processing]] and retrieval system <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.