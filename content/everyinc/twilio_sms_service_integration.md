---
title: Twilio SMS service integration
videoId: 9Zmhe6_T-xU
---

From: [[everyinc]] <br/> 

Hermes is a custom application designed to act as an "intellectual companion" for reading challenging books <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>. It simplifies complex text passages and provides additional context and analysis via SMS <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. The application was built in under an hour using Cursor and OpenAI's new o1 model <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Hermes Functionality

When a user encounters a difficult passage in a book, they can take a picture of it and send it to Hermes via text message <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Hermes then performs the following actions:
1.  **Transcribes the image into text**: It uses GPT-4's multimodal capabilities for Optical Character Recognition (OCR) to convert the image of the book page into readable text <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
2.  **Analyzes the transcription**: The transcribed text is sent to o1 preview for analysis <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. o1 preview is chosen for text interpretation due to its advanced chain-of-thought processing, which allows it to reflect before responding, leading to better text interpretation <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
3.  **Sends back the analysis**: The analysis is returned to the user as a text message <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. The analysis includes a restatement of the text in plain terms, insights into whether the science is up-to-date, missing perspectives, or underlying themes <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

Beyond initial analysis, Hermes can also proactively send follow-up messages throughout the day, "riffing" on the passage and introducing related quotes, ideas, or authors <a class="yt-timestamp" data-t="00:28:38">[00:28:38]</a>.

## Building the Twilio SMS Service

The development of Hermes involved integrating Twilio for SMS communication with OpenAI's models for AI processing.

### Initial Setup and Prompting

The development began in the OpenAI playground, pasting a prompt to define the application. The prompt specified the desire to build a Twilio-based SMS service that analyzes text with AI <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. Twilio is a service that enables programmatic sending and receiving of text messages <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

The initial prompt also included desired technologies like React, TypeScript, and Tailwind, though these were later found to be unnecessary for an SMS app <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### Key AI Models Used

*   **o1 mini**: Used for the programming and code generation in Cursor. It is a smaller, faster version of o1 preview, better suited for programming tasks <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **o1 preview**: Utilized for the deeper text interpretation and analysis of the book passages, requiring more extensive world knowledge <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
*   **GPT-4**: Employed specifically for image-to-text conversion (OCR) from the book pictures due to its multimodal capabilities <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

### Development Workflow and Challenges

The process demonstrated the rapid development possible with AI-assisted coding:

*   **Code Generation**: o1 generated the initial code, prompting for details like hosting (Railway) and other configurations <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.
*   **Dependency Management**: Red underlines in Cursor indicated missing installations, which were resolved using `npm install` <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.
*   **API Documentation Issues**: A significant challenge was the AI's occasional incorrect formatting of API calls (e.g., `Configuration` and `OpenAIApi` syntax for the OpenAI API, and initially trying to send images to Whisper, a speech-to-text model, instead of GPT-4 for image-to-text) <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. The developer manually provided the correct OpenAI API documentation to the AI <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. This highlights the need for precise input even with advanced models.
*   **Local Server Exposure (ngrok/enro)**: To allow Twilio to send incoming text messages to the local server running on the developer's machine, `enro` (a tool similar to ngrok) was used to expose the local server to the public internet <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
*   **Twilio Route Configuration**: Initially, Twilio attempted to hit the root index route, causing a 404 error <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>. This was resolved by configuring Twilio to correctly hit the `/sms` route <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>.
*   **Timeout Issues**: A critical challenge was Twilio timing out while waiting for a response because the image transcription and AI analysis process took too long <a class="yt-timestamp" data-t="00:21:06">[00:21:06]</a>. The solution involved separating the calls: an immediate reply is sent to Twilio upon receiving the message, and the analysis is sent as a separate text message later once completed <a class="yt-timestamp" data-t="00:23:37">[00:23:37]</a>.
*   **Long Response Handling**: Text messages have character limits. The AI was instructed to split long analysis responses into multiple messages to ensure full delivery <a class="yt-timestamp" data-t="00:26:44">[00:26:44]</a>.

## Conclusion

The project demonstrates the power of [[building_apps_with_chatgpt | building apps with ChatGPT]] and other AI models, especially when integrated with tools like Cursor and services like Twilio. What would have taken teams of engineers years to accomplish just a few years ago due to [[challenges_with_old_voicetotext_technology | challenges with old voicetotext technology]] and natural language processing limitations <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>, was achieved by one person in less than an hour, even with minimal coding experience <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. This highlights the "superpower" of [[integrating_agents_into_existing_development_workflows | integrating agents into existing development workflows]] for rapid prototyping and development <a class="yt-timestamp" data-t="00:28:54">[00:28:54]</a>.