---
title: Semantic similarity in video recommendations
videoId: 7ukp3_bZHXo
---

From: [[hrishikeshyadav8883]] <br/> 

A [[video_content_recommendation_engine | video content recommendation engine]] aims to provide users with videos they genuinely want to watch <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Traditionally, video recommendations have been based on metadata, descriptions, keywords, transcription, or user interaction with videos <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. This means if similar users interacted with a particular video, it might be recommended to you <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.

However, a more advanced approach focuses on [[use_cases_for_video_understanding | video understanding]] through semantic similarity <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. This method recommends content based on what the user "feels" or "wants" by understanding the semantic meaning of the video content itself <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Core Technology

This semantic recommendation system is powered by [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] and relies on a few key components:
*   **Video Embedding:** Videos are embedded using the Marengo Retrieval 2.7 model <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
*   **Vector Database:** These embeddings are stored in a Qdrant Cloud collection <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
*   **Fast Search:** Qdrant search provides quick results <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

## System Architecture

The application's architecture is broken down into two main parts:

### Step 1: Data Ingestion and Embedding Generation

This initial step is crucial for transforming raw video content into a format suitable for semantic search <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

1.  **Video Collection:** A large number of videos (e.g., 100+) are collected <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
2.  **Upload to Cloud Storage:** Videos are uploaded from local storage to an AWS S3 bucket to obtain public URLs for streaming <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. This process involves using the Boto3 library for AWS interaction <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The `S3 client.upload file` function is used for this <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.
3.  **Video Embedding Creation:** Each video is converted into a numerical embedding using the [[twelve_labs_video_embedding_and_retrieval | Twelve Labs]] Marengo Retrieval 2.7 model <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. It's important to specify an `embedding scope` of `clip` and `video` to generate a single embedding for the entire video <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. This is done via `client.ed.task` <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
4.  **Embedding Storage:** The generated video embeddings, along with their corresponding public S3 URLs and other metadata (like original filename), are stored as "points" in a Qdrant Cloud collection <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. Each point structure includes the vector (embedding), video ID, S3 URL, and original file name <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>. Setting up Qdrant Cloud involves registering an account, setting up a cluster, and obtaining API keys and host information <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Step 2: Recommendation Application and Semantic Search

Once the data is embedded and stored, the application can serve recommendations. This part is typically handled by a [[building_a_flask_api_for_video_recommendation | Flask API]] backend <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

1.  **User Input:** A user provides preferences or a search query, often in text format (e.g., "Comedy," "Fantasy and Musical," "Sci-Fi and dark tone") <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>, <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a>.
2.  **Text Embedding Generation:** The user's text query is converted into a text embedding using the same Marengo Retrieval 2.7 model used for videos <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>, <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>. This is done via `client.ed.create` <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
3.  **Semantic Search:** A semantic search is performed in the Qdrant Cloud collection using the generated text embedding <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>, <a class="yt-timestamp" data-t="00:11:56">[00:11:56]</a>. The `query_points` function is used, specifying the collection name, the vector (text embedding), and a limit (e.g., 10 results) <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>. Results are ordered by confidence score <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>.
4.  **Content Recommendation:** The system returns relevant video recommendations based on the semantic similarity between the query embedding and the stored video embeddings <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. The backend then structures the output to provide video URLs and scores <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
5.  **Front-end Display:** The front-end (built with Next.js) receives the video URLs and metadata, allowing the user to stream the recommended content <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>, <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>.

This approach ensures that recommendations are highly relevant to the user's inferred intent, moving beyond simple keyword matching to deeper content understanding <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.