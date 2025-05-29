---
title: Customizing the chat interface and functionality features
videoId: 83EfcTk5y7g
---

From: [[theaccountantguy]] <br/> 

The Notion Formula Chatbot is designed to help Notion users generate formulas for their specific use cases <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This article explains how to customize its interface and utilize its various functionality features.

## Initial Setup: API Key and GPT Model Selection

Before interacting with the chatbot, users must input an OpenAI API key <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

### Generating an OpenAI API Key
To generate an API key, click the question mark icon in the chatbot interface, which redirects to the OpenAI platform <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. From there, navigate to "API Keys" on the left, then click "Create new secret key" <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. After providing details and clicking "Create secret key," a new key will be generated <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>. This key must be copied and saved immediately, as it cannot be viewed again once the window is closed <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Once pasted into the chatbot window, a confirmation message will appear <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. New OpenAI accounts typically receive a $5 free credit, usable for testing with the GPT 3.5 Turbo model <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

### Selecting a GPT Model
The chatbot offers two GPT models:
*   **GPT 3.5 Turbo:** An older model, slightly less accurate <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. It is available for free accounts <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **GPT 4-106 Preview:** A newer model that provides better and more accurate results, recommended for users with a paid OpenAI plan <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>.
The entire demonstration video utilized GPT 3.5 Turbo <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Chatbot Interaction and Capabilities

The chatbot's main interface is divided into three sections: "Info," "Chat," and "Give" <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The "Chat" section is where users interact with the bot <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Asking Formula Questions
The chatbot can instantly generate responses to Notion-related formula questions <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. It provides explanations for understanding the formula components <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

Examples of queries and responses:
*   **Adding two numbers:** When asked for the formula to add two numbers, the chatbot suggested `property A + property B` <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Time difference between dates:** For finding the difference between a birth date and today's date in years, it recommended using the `dateBetween` formula with the "years" unit <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **IF condition:** When asked for an IF condition (if number one is greater than number two, output number one, else output number two), the chatbot provided the correct formula structure and explanation <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.

> [!NOTE] Prompting
> Sometimes, the chatbot may require more specific or detailed prompts, such as proper examples or references, to generate the most accurate responses <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Interface Customization

### User Icon
The chatbot allows users to upload an image, which will then appear as their user icon next to their questions <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This is an optional feature for personalization <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Clicking the cross icon reverts the user icon to its original default <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

### Color Theme and Font
The chatbot's appearance can be customized:
1.  Click the three-dot menu on the right side of the window <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
2.  Select "Settings" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
3.  Under "App theme colors and font," use the drop-down menu <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a>.
    *   **Light:** Changes the background color to light <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   **Dark:** Reverts the background color to dark <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>.
    *   **System Settings:** Allows editing the active theme and changing individual colors to suit user requirements <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
    *   **Font Family:** Users can also change the font family <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.

## Functionality Features

### Panels
The chatbot interface features three main panels:
*   **Info Section:** Contains details about the chatbot and an embedded explanatory video <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Chat Section:** The primary area for interacting with the chatbot <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Give Section:** Contains a donation button for supporting the product's development <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Left Panel Visibility
If the left panel (where API keys and GPT models are entered) is not visible, click the arrow icon on the left side of the chat window to open it <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This is particularly useful for smartphone or other device users <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Clear Chat History
A "Clear chat history" button is available in the chat section, which will clear the conversation history and refresh the interface <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### Conversations Counter
The chatbot also displays a "conversations counter," indicating the number of interactions a user has had with the bot <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Refresh Button
If any errors or issues occur, clicking the "Refresh" button can resolve them <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

### Donations
Users can donate to support the chatbot's functionality and future features by clicking the "Donate" button <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

### Feedback and Support
For any feedback or issues, users can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.