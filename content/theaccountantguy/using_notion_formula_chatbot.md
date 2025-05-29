---
title: Using Notion Formula Chatbot
videoId: 83EfcTk5y7g
---

From: [[theaccountantguy]] <br/> 

The Notion Formula Chatbot is designed for [[using_formulas_in_notion | Notion users]] who encounter difficulty finding the correct formula for their use case <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. This chatbot aims to help users derive the exact formula they require while [[using_formulas_in_notion | using Notion]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Getting Started

Before interacting with the chatbot, users must place their OpenAI API key in the designated field <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. After entering the API key, the desired GPT model needs to be selected <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.

### Generating an OpenAI API Key
To generate an OpenAI API key:
1.  Click the question mark icon in the chatbot interface to access the link for key generation <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
2.  This link redirects to the OpenAI platform <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
3.  Navigate to "API Keys" on the left-hand side <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
4.  Click "Create new secret key" <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
5.  Fill in the details, such as a name for the key (e.g., "test key"), and click "Create secret key" <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
6.  A new key will be generated; copy this key immediately, as it cannot be viewed again once the window is closed <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
7.  Paste the copied key into the chatbot's API key field <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. A message will confirm that the API key has been entered <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

Users typically receive a $5 free credit upon creating an OpenAI account, which can be used for testing with the GPT 3.5 Turbo model <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

### Selecting a GPT Model
The chatbot offers two GPT models:
*   **GPT 3.5 Turbo**: This is an older model and is slightly less accurate <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. It is suitable for users on the free OpenAI plan <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **GPT 4106 Preview**: This model provides better and more accurate results <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. It is recommended for users on a paid OpenAI plan <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

### Customizing User Image (Optional)
An optional feature allows users to upload an image to replace the default user icon in the chat interface <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. Uploading an image will update the display icon for the user who is generating questions <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. This can be reverted to the original image by clicking the 'X' button <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

## Interacting with the Chatbot

The chatbot interface is divided into three sections: "Info," "Chat," and "Give" <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. Users interact with the bot primarily in the "Chat" section <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

The chatbot responds instantly to questions <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> and provides explanations alongside the formulas <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Basic Arithmetic
Users can ask for basic [[using_formulas_in_notion | Notion formulas]], such as how to add two numbers.
> **Question:** What is the formula to add two numbers in Notion? <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
> **Chatbot Response:** In order to add two numbers in Notion, we can use `property A + property B`, where Property A and B can be the two numbers that we can input <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### Date and Time Differences
The chatbot can also handle more complex requests like finding [[using_formulas_to_calculate_differences_in_notion | time differences]] between dates.
> **Question:** What is the formula to find the difference between the birth date and today's date in years in Notion? <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
> **Chatbot Response:** It suggests using the `dateBetween` formula, specifying `years` to get the difference <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Conditional Logic (IF statements)
The chatbot is proficient with `if` conditions, providing formulas based on specified criteria.
> **Question:** If number one is greater than number two, I want to generate number one as the output; otherwise, I want to generate number two as the output. <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
> **Chatbot Response:** It responds that if `number one is greater than number two`, you can put in `number one` as the output, otherwise `number two`, along with a detailed explanation of the formula <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

> [!tip] Prompting Tips
> Sometimes, the chatbot may require better prompting from the user, such as providing proper examples or references, to generate the most accurate responses <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Interface Overview

The main chat window has a left panel that can be opened or closed, especially useful for smaller screens <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This panel is where the API keys and other settings are accessed <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. The interface is composed of three primary panels:

*   **Info Section**: Contains details about the chatbot, an embedded video explanation, and contact information (notionformyuse@gmail.com) for feedback or issues <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Chat Section**: The primary area for interacting with the bot <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. It includes a "Clear chat history" button to reset the conversation <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a> and a "Conversations counter" to track interactions <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Give Section**: Features a "Donate" button for users who wish to contribute to the product's improvement <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

## Additional Features and Tips

*   **Changing Theme Color**: The color theme can be changed from dark to light (or system default) by clicking the three dots on the right, selecting "Settings," then "App theme colors and font" <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>. Users can also customize active theme colors and font family <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Refresh Button**: If any error or issue occurs, clicking the "Refresh" button will typically resolve it <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.
*   **Feedback**: Users are encouraged to provide feedback or report issues by reaching out to notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>.