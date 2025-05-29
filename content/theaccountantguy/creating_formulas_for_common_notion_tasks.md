---
title: Creating formulas for common Notion tasks
videoId: 83EfcTk5y7g
---

From: [[theaccountantguy]] <br/> 

The [[using_the_notion_formula_chatbot | Notion Formula Chatbot]] is a tool designed to help Notion users create formulas for specific use cases <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It assists in deriving the exact formula needed when [[using_formulas_in_notion | using formulas in Notion]] <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Getting Started with the Chatbot

Before interacting with the chatbot, users must input an OpenAI API key and select a GPT model <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

### Obtaining an OpenAI API Key
To use the chatbot, an OpenAI API key is required <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.
1.  Click the question mark icon within the chatbot interface to find the link for generating the OpenAI key <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
2.  This link redirects to the OpenAI platform <a class="yt-timestamp" data-t="00:04:11">[00:04:11]</a>.
3.  Navigate to "API Keys" on the left-hand side <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
4.  Click "Create new secret key" <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
5.  Enter a name for the key (e.g., "test key") <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
6.  Click "Create secret key" <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>.
7.  **Important**: Copy the generated key immediately, as it will not be visible again once the window is closed <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>.
8.  Paste the copied key into the designated field in the chatbot interface <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>. A confirmation message will appear, indicating the API key has been entered <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

> [!INFO] OpenAI Free Credit
> Creating an OpenAI account typically provides a $5 free credit, which can be used for testing with the GPT 3.5 Turbo model <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

### Selecting a GPT Model
After entering the API key, choose a GPT model from the dropdown menu <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **GPT 3.5 Turbo**: This is an older model and is slightly less accurate <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. It is suitable for users on the free OpenAI plan <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>.
*   **GPT 4106 Preview**: This model offers better and more accurate results <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. It is recommended for users with a paid OpenAI plan <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>. The demonstration in the video utilized the GPT 3.5 Turbo model <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

## Interacting with the Chatbot for Formulas

The chatbot interface is divided into three main sections: **Info**, **Chat**, and **Give** <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>. The "Chat" section is where users interact with the bot to generate formulas <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

### Asking Basic Questions
The chatbot can provide formulas for simple operations.
*   **Adding Two Numbers**: To add two numbers in Notion, the chatbot suggests `property A + property B`, where 'property A' and 'property B' represent the input numbers <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### Asking Complex Questions
The chatbot is also capable of handling more complex formula requests.
*   **Time Difference Between Dates**: To find the difference in years between a birth date and today's date in Notion, the chatbot recommends [[using_excellike_formulas_in_notion | using the `dateBetween` formula]] with the 'years' unit <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Conditional Logic (IF Statements)**: The chatbot can generate formulas involving IF conditions. For example, to output 'number one' if it's greater than 'number two', otherwise output 'number two', the chatbot provides the correct IF statement syntax <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.

The chatbot typically responds instantly, providing both the formula and an explanation of what needs to be identified for the formula to work <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

### Tips for Better Prompting
For more accurate responses, it may be necessary to provide better prompting, including examples or references to what you are trying to achieve <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

## Customization and Features

### User Image
Users can upload an image, which will update the user icon displayed during chat interactions <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>. This feature is optional <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. Clicking the 'X' icon will revert the image to the original user icon <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

### Color Theme and Font
The chatbot's color theme can be changed from dark to light <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
1.  Click the three dots on the right side of the window <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
2.  Go to "Settings" <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.
3.  Under "App theme colors and font," click the dropdown menu <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.
4.  Select "Light" to change the background to light <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
5.  Users can revert to "Dark" or select "System settings" to customize active themes and font family <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.

### Chat Window Panels
If the left panel (for API key and GPT model selection) is not visible, click the arrow icon on the left side of the chat window to open it <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This is especially useful on smaller devices like smartphones <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>.

The chatbot has three main panels:
*   **Info Section**: Provides details related to the chatbot and may include an embedded video explanation <a class="yt-timestamp" data-t="00:08:35">[00:08:35]</a>.
*   **Chat Section**: The primary interface for interacting with the chatbot <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>. It includes:
    *   **Clear Chat History Button**: Allows users to clear past conversations <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
    *   **Conversations Counter**: Displays the number of conversations had with the chatbot <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Give Section**: Contains a "Donate" button for users who wish to support the product's development <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

If any error or issue occurs, clicking the "Refresh" button will restart the chatbot <a class="yt-timestamp" data-t="00:09:16">[00:09:16]</a>.

## Support and Feedback

For any feedback or issues, users can reach out via email at notionformyuse@gmail.com <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.