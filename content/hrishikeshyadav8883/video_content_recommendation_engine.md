---
title: Video content recommendation engine
videoId: 7ukp3_bZHXo
---

From: [[hrishikeshyadav8883]] <br/> 

A video content recommendation engine is discussed, focusing on a method that leverages [[semantic_similarity_in_video_recommendations | semantic similarity]] among videos <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This approach aims to provide recommendations based on understanding the video's content, rather than solely relying on traditional metadata <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Traditional Video Recommendation
Traditionally, video recommendations are based on metadata, descriptions, keywords, transcription, or user interaction with the video <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This means if you interact with certain videos, and other similar users interact with those same videos, you might be recommended similar content <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.

## Semantic Similarity for Recommendations
The discussed system utilizes [[semantic_similarity_in_video_recommendations | semantic similarity]] to understand the video and recommend content based on the user's perceived wants or needs <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This is powered by [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.

### Core Technologies
*   **Video Embedding and Retrieval:** [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]]'s Marengo Retrieval 2.7 model is used to embed videos <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Vector Database:** The embeddings are stored in Qdrant Cloud collection <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. Qdrant search provides quick results <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.
*   **Application Frameworks:** The application is built with Next.js for the frontend and a [[building_a_flask_api_for_video_recommendation | Flask API]] for the backend <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

## System Architecture and Workflow
The entire architecture can be broken down into two main parts <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>:

### Part 1: Data Ingestion and Embedding
This crucial first step involves converting video content into an embedding format and storing it in a vector database <a class="yt-timestamp" data-t="00:03:59">[00:04:06]</a>.

1.  **Video Collection:** A large number of videos (e.g., 100+) are collected <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>.
2.  **Video Upload to S3:** Videos are uploaded to an AWS S3 bucket to obtain public URLs <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. This is necessary if local videos need to be streamed <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
3.  **Embedding Generation:** The Marengo Retrieval 2.7 model from [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] converts the videos into embeddings <a class="yt-timestamp" data-t="00:04:19">[00:04:22]</a>. The embedding scope is set to "clip and video" to get a complete video embedding <a class="yt-timestamp" data-t="00:07:25">[00:07:28]</a>.
4.  **Storage in Qdrant:** The generated embeddings, along with the public S3 URL and other metadata (like original file name and video ID), are stored as "points" in a Qdrant Cloud collection <a class="yt-timestamp" data-t="00:04:53">[00:05:03]</a> <a class="yt-timestamp" data-t="00:07:49">[00:07:57]</a>.

> "client.ed.task with maringo retrieval 2.7 model" <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>
> "embedding scope is clip and video" <a class="yt-timestamp" data-t="00:07:25">[00:07:28]</a>

### Part 2: Application and Search
Once the video data is in the Qdrant Cloud collection in an embedded format, the application can be built <a class="yt-timestamp" data-t="00:05:07">[00:05:10]</a>.

1.  **User Query:** A user provides preferences or a search query (e.g., "Comedy," "Sci-fi," "dark tone") <a class="yt-timestamp" data-t="00:05:15">[00:05:19]</a>. This query is typically text-based <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
2.  **Text Embedding Generation:** The text query is converted into a text embedding using the Marengo Retrieval 2.7 model <a class="yt-timestamp" data-t="00:05:26">[00:05:31]</a>.
3.  **Semantic Search:** A [[semantic_similarity_in_video_recommendations | semantic search]] is performed using the text embedding against the video embeddings stored in Qdrant Cloud <a class="yt-timestamp" data-t="00:05:33">[00:05:34]</a>. The `query_points` function is used for this search <a class="yt-timestamp" data-t="00:12:01">[00:12:04]</a>.
4.  **Recommendation Retrieval:** The system retrieves relevant video content recommendations, typically a limit of 10 videos, ordered by confidence score <a class="yt-timestamp" data-t="00:12:12">[00:12:16]</a>.
5.  **Display:** The application displays the recommended videos to the user, providing the video URL for streaming <a class="yt-timestamp" data-t="00:12:32">[00:12:33]</a>. If the API fails, a fallback method provides alternative content to avoid user errors <a class="yt-timestamp" data-t="00:15:21">[00:15:27]</a>.

The entire process, from user query to displaying relevant videos, involves posting the search query to an endpoint, generating a text embedding, performing a vector similarity search, and then receiving a JSON response with matching videos and their metadata <a class="yt-timestamp" data-t="00:16:29">[00:16:55]</a>.

## Demo Walkthrough
In a demonstration, selecting categories like "Comedy," "Fantasy," "Musical," or "Sci-fi" with a "dark tone" dynamically changes the video recommendations, showcasing the system's ability to understand preferences and provide relevant content quickly <a class="yt-timestamp" data-t="00:01:21">[00:02:30]</a>. For example, a "Sci-fi" and "dark tone" search might yield videos about robots <a class="yt-timestamp" data-t="00:02:13">[00:02:18]</a>.

The application's ease of use and quick streaming of recommended videos highlight its efficiency <a class="yt-timestamp" data-t="00:02:30">[00:02:33]</a>.