---
title: Building an app with OpenAI and Cursor
videoId: 9Zmhe6_T-xU
---

From: [[everyinc]] <br/> 

The Hermes app is a personal project designed to assist with reading challenging books <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. When encountering a difficult passage, a user can take a picture of the text and send it to Hermes <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Hermes then restates the content in plain terms, offers additional insights like scientific accuracy, missing perspectives, or underlying themes, and essentially acts as an [[building_an_ai_companion | intellectual companion]] <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a><a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a><a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Development Process

The Hermes app was [[building_an_ai_app_from_scratch | built personally]] in less than an hour using Cursor and OpenAI's new O1 model <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a><a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This rapid development highlights a significant shift in [[developing_apps_and_prototypes_using_ai | building applications with AI]] <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. Just a few years ago (2-3 years prior), such a project would have been "completely impossible," requiring years of work from teams of engineers due to limitations in OCR (Optical Character Recognition) and natural language processing (NLP) technologies <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a><a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a><a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. Now, it's feasible for individuals even without extensive coding knowledge <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a><a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

The development process involved:
*   Starting in the OpenAI playground and providing an initial prompt for a coding assistant <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a><a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   Specifying the app's core functionality: a Twilio-based SMS service that analyzes text with AI <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a><a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   Defining the workflow:
    1.  User sends a text message with a picture of a book <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    2.  Twilio receives the picture <a class="yt-timestamp" data-t="00:03:16">[00:03:16]</a>.
    3.  GPT-4 transcribes the picture into text (OCR) <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a><a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. GPT-4 was chosen for OCR because it is multimodal and excels at image-to-text conversion <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a><a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
    4.  The transcription is sent to O1 Preview for analysis <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. O1 Preview is a larger, more advanced OpenAI model used for text interpretation due to its "Chain of Thought" reasoning <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a><a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a><a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
    5.  The analysis is sent back to the user via text message <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Tools and Models Used

*   **Cursor:** The integrated development environment (IDE) used for coding <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a><a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **OpenAI Models:**
    *   **O1 Mini:** A smaller, faster version of O1, used for programming tasks within the playground <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a><a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. It's better for programming but has less world knowledge <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
    *   **O1 Preview:** The larger, more advanced O1 model, used for text interpretation and analysis <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a><a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Its "Chain of Thought" processing makes it suitable for complex text interpretation <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a><a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.
    *   **GPT-4:** Used specifically for the image-to-text transcription (OCR) due to its multimodal capabilities <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a><a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Twilio:** A service for sending and receiving text messages programmatically, enabling the SMS functionality of the app <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a><a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **ngrok:** A tool used to expose the local server to the public internet, allowing Twilio to forward messages to the running application <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a><a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a><a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>.
*   **Railway:** The chosen hosting platform <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### [[challenges_in_building_ai_tools | Challenges in Building AI Tools]]

During the development, several [[challenges_in_building_ai_tools | challenges in building AI tools]] were encountered:
*   **Incorrect API Calls:** OpenAI models occasionally provided incorrect API call formats, requiring manual correction or providing the model with up-to-date documentation <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a><a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
*   **Model Misuse:** The AI initially attempted to send images to Whisper (a speech-to-text model) instead of GPT-4 for image transcription, which required correction <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a><a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.
*   **Twilio 404 Error:** The Twilio service initially could not find the correct route on the server, requiring an update to the Twilio configuration to point to the `/sms` route <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a><a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
*   **Twilio Timeout:** The image transcription and AI analysis process took too long, causing Twilio to time out while waiting for a response <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a><a class="yt-timestamp" data-t="00:23:22">[00:23:22]</a>. The solution involved immediately replying to Twilio and then sending the analysis as a separate, delayed text message <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a><a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>.
*   **Message Length Limits:** The analysis provided by O1 Preview was sometimes too long for a single text message. The app was updated to split the analysis into multiple messages <a class="yt-timestamp" data-t="00:26:44">[00:26:44]</a><a class="yt-timestamp" data-t="00:26:51">[00:26:51]</a>.

## Conclusion

The Hermes app was completed in approximately 50 minutes, demonstrating the speed and ease of [[building_apps_with_chatgpt | building apps with ChatGPT]] (or similar AI models) and AI-assisted coding environments like Cursor <a class="yt-timestamp" data-t="00:28:23">[00:28:23]</a><a class="yt-timestamp" data-t="00:28:26">[00:28:26]</a>. After the initial build, refinements were made to make the analysis more succinct and to add a proactive feature where Hermes sends follow-up messages, quotes, or author suggestions related to the passage <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a><a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a><a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>. This project exemplifies how [[building_applications_with_ai | coding with AI]] can be a "superpower," allowing individuals to quickly and easily bring ideas to life that were previously impossible <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a><a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.