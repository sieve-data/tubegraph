---
title: Application of OCR and GPT4 in app development
videoId: 9Zmhe6_T-xU
---

From: [[everyinc]] <br/> 

This article explores the development of "Hermes," a custom application designed to analyze text from images using [[The role of ChatGPT in learning and research | AI]]. The app demonstrates how modern AI models, specifically [[Building custom GPTs with OpenAI | OpenAI]]'s GPT-4 and o1, can be leveraged for rapid [[Building Apps with ChatGPT | app development]] and practical personal use, including [[ChatGPT in writing and content creation | content creation]] and comprehension.

## Introducing Hermes: An Intellectual Companion

Hermes is a small application built to help users understand challenging books by analyzing text from images <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. When a user encounters a difficult passage, they can take a picture of it and send it to Hermes <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. Hermes then rephrases the content in plain terms and provides additional insights, such as whether the science is up-to-date, missing perspectives, or underlying themes <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This process enriches the reading experience, turning the app into an "intellectual companion" <a class="yt-timestamp" data-t="00:01:03">[00:01:03]</a>.

## Technology Behind Hermes

The core functionality of Hermes relies on a combination of technologies:

*   **Twilio:** A service that enables programmatic sending and receiving of text messages <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Hermes uses Twilio to receive image texts from users and send back analysis.
*   **GPT-4 for Optical Character Recognition (OCR):** When Hermes receives a picture of a book, it uses GPT-4 to transcribe the image into text <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. GPT-4 is chosen for this task because of its multimodal capabilities, making it very effective at image-to-text conversion <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **OpenAI's o1 Preview for Text Analysis:** Once the text is transcribed, it's sent to o1 preview for analysis <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. O1 preview is a larger, more advanced version of [[Building custom GPTs with OpenAI | OpenAI]]'s new model o1, designed for "thinking" and "Chain of Thought" processing, which makes it better for text interpretation as it can reflect before responding <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
*   **OpenAI's o1 Mini for Coding:** For the actual coding assistance during development, o1 mini is used <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. O1 mini is a smaller, faster version of o1, better suited for programming tasks, though it has less general world knowledge <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
*   **Cursor:** A coding environment that integrates deeply with [[The role of ChatGPT in learning and research | AI]] models for assistance <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.

## Rapid Application Development with AI

The developer built Hermes in less than an hour using Cursor and [[Building custom GPTs with OpenAI | OpenAI]]'s o1 model <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. This speed was previously impossible, with tasks like reliable OCR and natural language processing requiring years of work from teams of engineers <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The process demonstrates how [[ChatGPTs impact on programming and data visualization | AI impacts programming]] by enabling rapid prototyping even for those with limited coding experience <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.

### Development Workflow

The development process involved interacting with [[The role of ChatGPT in learning and research | AI]] to generate code and troubleshoot issues:

1.  **Prompting the AI:** The process began in the [[Building custom GPTs with OpenAI | OpenAI]] playground, pasting a prompt to define the application's requirements, including the desired workflow (sending a picture, transcribing with GPT-4, analyzing with o1 preview, and sending back analysis) <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.
2.  **Iterative Coding:** The [[ChatGPT as a problemsolving tool for coding | AI]] generated initial code, which was then refined. The developer copied the generated code into a `server.ts` file within a new project directory <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
3.  **Dependency Management:** The [[ChatGPT as a problemsolving tool for coding | AI]] helped identify and install necessary packages (e.g., Twilio, TypeScript) using `npm install` <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
4.  **API Integration Challenges:**
    *   **Incorrect API Calls:** The [[Overcoming the limitations of ChatGPT for effective usage | AI initially]] made errors in the exact format of [[Building custom GPTs with OpenAI | OpenAI]] API calls, sometimes confusing Python documentation for Node.js <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. The developer manually corrected these by supplying the correct documentation to the [[ChatGPT as a problemsolving tool for coding | AI]] <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.
    *   **Model Misuse:** The [[Overcoming the limitations of ChatGPT for effective usage | AI initially]] attempted to use Whisper (a speech-to-text model) for image transcription instead of GPT-4, which can handle image-to-text <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. This required explicit instruction to use GPT-4 Vision <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.
5.  **Local Server Exposure:** `ngrok` was used to expose the local server to the public internet, allowing Twilio to send incoming text messages to it <a class="yt-timestamp" data-t="00:17:30">[00:17:30]</a>.
6.  **Troubleshooting and Refinement:**
    *   **Routing Issues:** An initial 404 error indicated Twilio was hitting the wrong server route. The Twilio configuration was updated to target the correct `/sms` endpoint <a class="yt-timestamp" data-t="00:19:11">[00:19:11]</a>.
    *   **Timeout Handling:** [[The role of ChatGPT in learning and research | AI]] was used to implement a mechanism to avoid Twilio timeouts. The server was modified to send an immediate reply to Twilio upon receiving a message, and then send the analysis as a separate, later message once completed <a class="yt-timestamp" data-t="00:23:18">[00:23:18]</a>.
    *   **Message Length Limits:** To handle long analysis results, the [[The role of ChatGPT in learning and research | AI]] was instructed to split the analysis into multiple text messages to conform to SMS character limits <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>.

### Post-Development Enhancements

After the initial build, the developer spent additional time cleaning up the prompt to make the analysis more succinct <a class="yt-timestamp" data-t="00:28:28">[00:28:28]</a>. An additional feature was added where, after receiving a passage, Hermes proactively sends follow-up messages throughout the day, riffing on the passage and introducing related quotes, ideas, or authors <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.

The development of Hermes highlights the "superpower" of [[Developing custom GPTs for programming and personal use | coding with AI]], allowing for rapid creation of applications that were previously impossible to build quickly <a class="yt-timestamp" data-t="00:29:00">[00:29:00]</a>.