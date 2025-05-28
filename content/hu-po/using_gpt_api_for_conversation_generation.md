---
title: Using GPT API for conversation generation
videoId: Kvjd-V8zLtM
---

From: [[hu-po]] <br/> 

The "speech to speech" project is an application designed to facilitate [[developments_in_multiturn_conversational_AI | multi-turn AI conversations]] between multiple characters <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It allows users to initiate conversations, input their own speech, and generate AI-driven responses from virtual personalities <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Core Functionality

The application enables users to:
*   **Initiate Conversations** The process begins by selecting desired participants, such as Joe Biden, Donald Trump, and Elon Musk <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.
*   **User Input** Users record their speech, which is then automatically converted into text <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.
*   **Generate AI Responses** After the user's input, additional conversation bubbles are generated <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. These responses are created by GPT via its API, tailored to the persona of each selected character <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
*   **Playback** The entire conversation, including both user input and AI-generated dialogue, can be played back through the computer's speakers <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.
*   **Export Audio** Conversations can be exported as an audio file, allowing users to share them or upload them to other platforms <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.

## Technology Stack

The project leverages two primary API services:
*   **OpenAI API** The OpenAI API is utilized for generating the conversational responses from the AI characters <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **Eleven Labs API** The Eleven Labs API is used for the speech synthesis, converting the generated text responses into natural-sounding speech <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

A key advantage is that the application does not require local GPUs, as all processing is handled via APIs, making it runnable on less powerful machines <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>.

## Character Customization

The "speech to speech" project allows for extensive customization of characters, moving beyond just [[creating_ai_conversations_with_famous_personalities | famous personalities]] <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>:
*   **Any Individual** Users can define virtually any character <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Character Definition** To create a new character, users need to:
    *   Choose a name <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
    *   Provide a description of the character's personality and communication style <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
    *   Supply a list of audio references, typically 60 seconds to two minutes of audio from any YouTube video <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Even a 30-second clip can be sufficient <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.

## Requirements and Availability

*   **API Keys** Users need an OpenAI API key (estimated at $20 to get started) and an Eleven Labs API key (estimated at $5 to get started) <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. The total initial cost is approximately $25 <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
*   **GitHub Repository** The project's code is available on GitHub under an MIT license, allowing for community use and development <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.