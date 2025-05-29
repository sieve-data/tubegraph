---
title: Interacting with a GPT Model
videoId: 83EfcTk5y7g
---

From: [[theaccountantguy]] <br/> 

## Introduction
The [[using_notion_formula_chatbot | Notion Formula Chatbot]] is designed to assist [[notion | Notion]] users in generating formulas for specific use cases <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. Its purpose is to help users derive the exact formulas needed for their Notion tasks <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Initial Setup
Before interacting with the chatbot, users must complete a few initial setup steps:

### [[generating_and_using_openai_api_keys | Generating and Using OpenAI API Keys]]
To begin interacting with the chatbot, users need to input their OpenAI API key <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

To generate an API key:
1.  Click the question mark icon in the chatbot interface to access a link that redirects to the OpenAI platform <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
2.  On the OpenAI platform, navigate to "Open API Keys" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
3.  Click "Create new secret key" <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
4.  Fill in the required details (e.g., "test key") and click "Create secret key" <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
5.  A new key will be generated <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Copy this key immediately, as it cannot be viewed again once the window is closed <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
6.  Paste the copied key into the designated field in the chatbot window <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. A confirmation message "AP key has been entered" will appear <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

OpenAI accounts typically receive a $5 free credit for testing, which is limited to the GPT 3.5 Turbo model <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

### [[selecting_and_configuring_ai_engines_such_as_gemini_and_gpt | Selecting a GPT Model]]
After entering the API key, users must select their preferred GPT model from a dropdown menu <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
The available models include <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>:
*   **GPT 3.5 Turbo**: An older model that is less accurate <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This model can be used with the free $5 credit for new accounts <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **GPT 4-106 Preview**: A newer model that provides more accurate results with prompts <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. This model is recommended for users on a paid OpenAI plan <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

The demonstration of the chatbot functionality in the video was performed using the GPT 3.5 Turbo model <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Chatbot Interface and Interaction
The chatbot interface is divided into three main sections <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>:
*   **Info Section**: Provides details related to the chatbot and includes an embedded video explanation <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Chat Section**: Where users interact with the bot by typing messages <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.
*   **Give Section**: Contains a "Donate" button for users to support the product's development <a class="yt-timestamp" data-t="00:09:07">[00:09:07]</a>.

### Interacting with the Chatbot
Users can start by typing an initial message like "Hi" <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. The bot then generates a response <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

Examples of Notion formula questions asked and responses:
*   **Adding two numbers**:
    *   **Question**: "What is the formula to add two numbers in Notion?" <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>
    *   **Answer**: The chatbot instantly responds that `property A + property B` can be used, where Property A and B are the two numbers to be input <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>.
*   **Time difference between two dates**:
    *   **Question**: "What is the formula to find the difference between the birth date and today's date in years in Notion?" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>
    *   **Answer**: The chatbot suggested using the `dateBetween` formula, specifying "years" as the unit <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
*   **IF condition**:
    *   **Question**: "If number one is greater than number two, I want to generate number one as the output, otherwise I want to generate number two as the output." <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>
    *   **Answer**: The chatbot demonstrated its fluency with IF conditions by explaining that if number one is greater than number two, number one should be used, otherwise number two <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>. It provided a detailed explanation of the formula <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

The chatbot responds instantly and provides explanations along with the formulas <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Sometimes, better prompting with proper examples or references may be needed to achieve the desired response <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Customization and Features

### User Image
Users can upload an image to customize the user icon (display picture) that appears when they generate a question <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This feature is optional <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. Uploading an image updates the user icon immediately <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>. Clicking the cross icon reverts to the original user image <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

### Theme and Font Settings
To change the color theme or font:
1.  Click the three dots on the right side of the window <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
2.  Click "Settings" <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
3.  Under "App theme colors and font," select "Light" for a light background, "Dark" to return to dark settings, or "System settings" to customize colors and font family <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

### Panel Visibility
If the left panel (for API keys and other settings) is not visible, users can click the arrow on the left side of the window to open it <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This is particularly useful for smartphone or other device users <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

### Additional Chat Features
*   **Clear Chat History**: A "Clear chat history" button is available to reset the conversation <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **Conversations Counter**: Displays the number of conversations had with the chatbot <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Refresh**: In case of errors or issues, clicking the "Refresh" button can resolve them <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

## Support and Feedback
Users can contact the developer for feedback or issues at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. Donations for product improvement are accepted via the "Donate" button in the "Give" section <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.