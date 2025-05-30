---
title: Challenges in realtime text analysis
videoId: 9Zmhe6_T-xU
---

From: [[everyinc]] <br/> 

Developing applications that perform real-time text analysis, such as the Hermes app for understanding complex books, presents several challenges, particularly when integrating with external services and dealing with the inherent processing times of advanced AI models <a class="yt-timestamp" data-t="00:21:03">[00:21:03]</a>.

## Limitations of Older Technology
Historically, tasks like transcribing images into readable text and performing advanced natural language processing were significantly more difficult.
*   **Optical Character Recognition (OCR)**: Just a few years ago, OCR technology was not robust enough to reliably convert arbitrary pictures into text <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This made it "completely impossible" to build applications like Hermes that relied on image-to-text conversion <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Natural Language Processing (NLP)**: Older NLP models were not capable of extracting "interesting things" or providing insightful analysis from text <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. The advent of models like OpenAI's 01 and GPT-4 has made such in-depth analysis feasible <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

## AI Model Integration and Configuration
While modern AI greatly simplifies development, [[challenges_in_building_ai_tools | building AI tools]] still involves specific challenges:
*   **Incorrect API Calls**: Even with advanced coding assistants, models like 01 can sometimes generate incorrect API call formats, requiring the developer to consult documentation or manually correct the code <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. This was observed when the model got the `Configuration` and `OpenAI API` calls wrong <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>, and later with the `create chat completion` call <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
*   **Misapplication of Models**: An AI might attempt to use a model for the wrong task, such as sending an image to Whisper (a speech-to-text model) instead of GPT-4 (an image-to-text model) for transcription <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Model Knowledge Gaps**: Newer models might not have information about themselves or their own API, requiring the developer to provide their documentation <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## Real-time Processing and External Service Timeouts
A significant hurdle in real-time text analysis, especially when interacting with services like [[twilio_api_timeout | Twilio]], is managing processing time:
*   **API Timeouts**: The process of transcribing an image and then performing an analysis can be time-consuming <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. Services like [[twilio_api_timeout | Twilio]] expect a quick response <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. If the server takes too long to reply, the API may time out, leading to communication failures <a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>.
    *   **Solution**: To overcome this, the application can be designed to send an immediate reply to [[twilio_api_timeout | Twilio]] upon receiving a message, and then send the analysis back as a separate message once processing is complete <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a>. This separates the immediate communication expectation from the longer analysis process.
*   **Output Length Constraints**: Text messages have a limited number of characters <a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>. If the AI's analysis is too long, it must be split into multiple messages for proper delivery <a class="yt-timestamp" data-t="00:26:46">[00:26:46]</a>.

Despite these [[challenges_in_building_ai_tools | challenges in building AI tools]], modern AI capabilities have made the creation of complex applications like Hermes, which performs real-time text analysis of book passages, incredibly fast and accessible <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.