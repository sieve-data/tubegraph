---
title: The process and benefits of using AI in programming
videoId: 9Zmhe6_T-xU
---

From: [[everyinc]] <br/> 

This article details the development of "Hermes," an application designed to assist in understanding complex texts, highlighting [[the_role_of_ai_in_programming_assistance | the role of AI in programming assistance]] and demonstrating [[challenges_and_benefits_of_integrating_ai_into_product_development | the challenges and benefits of integrating AI into product development]]. The entire process of building Hermes from scratch took less than an hour, showcasing the significant advancements and accessibility offered by modern [[generative_ai_in_programming | generative AI in programming]] tools <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>.

## What is Hermes?

Hermes is a small application built to help users understand challenging books <a class="yt-timestamp" data-t="00:57:00">[00:57:00]</a>. When a user encounters a difficult passage, they can take a picture of it and send it to Hermes <a class="yt-timestamp" data-t="00:43:00">[00:43:00]</a>. Hermes then performs the following functions:
*   Restates the passage in plain terms <a class="yt-timestamp" data-t="00:46:00">[00:46:00]</a>.
*   Provides information about the passage, such as the recency of the science, missing perspectives, or underlying themes <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
This functionality transforms reading into a richer experience, akin to having an "intellectual companion" <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.

## [[the_evolution_of_ai_in_software_engineering | The Evolution of AI in Software Engineering]]: Building Hermes with AI

The development of Hermes was made possible by advanced AI tools, specifically Cursor and OpenAI's new model O1 <a class="yt-timestamp" data-t="01:09:00">[01:09:00]</a>. Just a few years ago, building such an application would have been impossible, even for teams of engineers working for years, due to limitations in OCR technology and natural language processing <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.

### AI Models and Their Roles

*   **O1 as a Coding Assistant**: In the OpenAI playground, O1 (specifically O1 Mini) acts as a coding assistant. It takes high-level prompts detailing the desired application and workflow, then generates the necessary code <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a> <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. O1 Mini is preferred for programming due to its speed and efficiency, though it "knows less about the world" than its larger counterpart <a class="yt-timestamp" data-t="04:20:00">[04:20:00]</a>.
*   **GPT-4 for Optical Character Recognition (OCR)**: When an image of a book is sent to Hermes, GPT-4 is used to transcribe the picture into text <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. GPT-4's multimodal capabilities make it highly effective at image-to-text conversion <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.
*   **O1 Preview for Text Analysis**: Once the text is extracted, it is sent to O1 Preview for analysis <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. O1 Preview, being the larger and more advanced version of O1, performs a "Chain of Thought" process, allowing it time to reflect before responding, which is beneficial for complex text interpretation as it requires extensive world knowledge <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a> <a class="yt-timestamp" data-t="04:33:00">[04:33:00]</a>.
*   **Twilio for SMS Functionality**: Twilio is a service used to send and receive text messages programmatically, forming the communication backbone of Hermes <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### The Development Process

The development process, guided by AI, involved several key steps:

1.  **Initial Prompting**: The process began by pasting a prompt into the OpenAI playground, instructing the AI to act as a coding assistant and define the desired app (a Twilio-based SMS service that analyzes text with AI) and its workflow <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a> <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
2.  **Code Generation and Setup**: O1 generated the initial code, which was then copied into a new TypeScript file (`server.ts`) in a Cursor project <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a> <a class="yt-timestamp" data-t="07:38:00">[07:38:00]</a>.
3.  **Dependency Installation**: The AI indicated necessary libraries, which were installed using `npm install` <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.
4.  **Iterative Debugging and Correction**:
    *   **API Call Correction**: The AI initially struggled with the exact format of OpenAI API calls, necessitating manual input of correct documentation <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a> <a class="yt-timestamp" data-t="13:58:00">[13:58:00]</a>.
    *   **Model Misidentification**: A significant correction involved changing the image processing from Whisper (a speech-to-text model) to GPT-4o (an image-to-text model), as the AI initially tried to use the wrong model for image transcription <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
    *   **External Service Integration (Twilio & ngrok)**: The developer used `ngrok` (enro) to expose the local server to the internet, allowing Twilio to forward text messages to the server <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>. This required configuring Twilio's webhook to hit the correct server route (`/sms`) <a class="yt-timestamp" data-t="19:30:00">[19:30:00]</a>.
    *   **Timeout Handling**: To prevent Twilio's timeout issues during image processing and analysis, a mechanism was implemented to send an immediate reply to Twilio upon message receipt, with the actual analysis sent as a separate message later <a class="yt-timestamp" data-t="23:20:00">[23:20:00]</a>.
    *   **Message Length Splitting**: Since SMS messages have character limits, the analysis was split into multiple messages to ensure it could be sent back to the user <a class="yt-timestamp" data-t="26:40:00">[26:40:00]</a>.

### Post-Development Enhancements

After the initial build, the prompt was refined to make the analysis more succinct <a class="yt-timestamp" data-t="28:31:00">[28:31:00]</a>. An additional feature was added where Hermes proactively sends follow-up messages throughout the day, riffing on the passage and introducing related ideas, quotes, or authors <a class="yt-timestamp" data-t="28:36:00">[28:36:00]</a>.

## [[benefits_of_using_ai_for_creative_work | Benefits of Using AI in Programming]]

The development of Hermes exemplifies several key [[applications_of_ai_in_automating_tasks | applications of AI in automating tasks]] and the broader benefits of [[generative_ai_in_programming | generative AI in programming]]:

*   **Rapid Prototyping**: A functional application was built in approximately 50 minutes <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a> <a class="yt-timestamp" data-t="28:23:00">[28:23:00]</a>. This speed was previously unimaginable for complex projects involving OCR, NLP, and external APIs <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
*   **Increased Accessibility**: The process is highly accessible even for individuals with limited or no prior coding experience <a class="yt-timestamp" data-t="01:43:00">[01:43:00]</a> <a class="yt-timestamp" data-t="05:42:00">[05:42:00]</a>. AI tools can guide users through installation and setup steps <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.
*   **Automation of Tedious Tasks**: AI handles much of the boilerplate code generation and initial API integration, allowing the developer to focus on higher-level logic and problem-solving <a class="yt-timestamp" data-t="17:12:00">[17:12:00]</a>.
*   **Problem-Solving Assistance**: AI helps identify and suggest solutions for common programming issues like dependency management, API formatting, and logical flow <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>.
*   **Empowerment**: AI-assisted coding provides a "superpower," enabling individuals to quickly bring ideas to life in a way that was never before possible <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. This significantly lowers the barrier to entry for building and deploying applications.

The experience demonstrates that AI-assisted programming makes previously impossible projects feasible within short timeframes, even with minor human errors during live development <a class="yt-timestamp" data-t="09:54:00">[09:54:00]</a>.