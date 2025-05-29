---
title: Improving UI and UX with AI tools
videoId: P_mIfIbWS8c
---

From: [[amiteshanand]] <br/> 

AI tools, such as Cursor, can significantly streamline the process of building and enhancing the User Interface (UI) and User Experience (UX) of applications, even for complex projects like VS Code extensions <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. This approach demonstrates how simple prompts can initiate development and how iterative improvements can be made through AI-powered chat interfaces.

## Building with Cursor: An AI-Assisted Approach

A basic VS Code extension was developed almost entirely by Cursor, an AI code editor <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. The developer provided only an initial prompt, and Cursor's chat feature was then used to "build and iterate and improve this extension" <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. This extension leverages [[using_ai_models_for_coding_assistance | AI models]] such as DeepSeek and Qwen to assist with coding tasks <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Initial UI/UX Challenges

Despite Cursor's ability to generate functional code, the initial UI of the extension was not optimal <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. Key issues included:
*   **Poor Formatting**: The output was "not properly formatted" <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a> and lacked a "good layout" <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>.
*   **Subdued Colors**: The color scheme was described as "just yellow and gray" and "not Punchy" <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Visibility Issues**: Some words were not visible in the initial output <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## Iterative UI/UX Improvement with Cursor Chat

To address these issues, the developer used Cursor's chat functionality to iteratively improve the extension's UI/UX <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>, <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This process involved:
1.  **Defining Improvement Goals**: Prompts were given to the AI to "improve overall UI ux" <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a> and to "make it attactive" <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
2.  **Specifying Formatting**: Requests included "making sentence bold italic and picking colors for code responses make sure to format it properly" <a class="yt-timestamp" data-t="00:04:02">[00:04:02]</a>.
3.  **Applying Changes**: Cursor responded by modifying the `chatPanel.TS` file, which is responsible for the UI generation <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. The proposed changes were then applied and accepted <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.
4.  **Addressing Issues**: When the AI introduced new problems, like missing HTML tags, the developer could ask Cursor to "fix" them directly through the chat <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>, <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

## Results of UI/UX Enhancements

After several iterations, Cursor made notable improvements to the extension's UI/UX, including:
*   **Styling Enhancements**: General styling was improved <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Font and Color Adjustments**: Font colors were updated, and bold/italic formatting was introduced <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>.
*   **Code Formatting**: Better formatting for code responses was implemented <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>.
*   **Responsiveness and Accessibility**: Additional assistance was provided for responsive design and accessibility <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.
*   **Visibility Fixes**: Previously invisible words became visible <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

While some advanced styling challenges remained, such as consistently applying bold formatting for specific words <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>, the overall UI "improved a bit" <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. Cursor also provided example CSS code for further custom styling <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

## Underlying AI Models and Infrastructure

The VS Code extension integrates with various [[understanding_ai_agents | AI models]] provided by NVIDIA AI Studio, which acts as a "cheaper inference provider" <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>, <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Users can choose between several models, including:
*   DeepSeek Coder V2 Light <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>
*   Qwen 2.5 Coder 7B Instruct <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>, <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>
*   Qwen 2.5 Coder 32B Instruct <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>
*   DeepSeek V3 <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

Users can sign up for NVIDIA AI Studio to obtain API keys and receive credits for model usage <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>, <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

## Conclusion

This example demonstrates how [[ai_tools_for_productivity | AI tools for productivity]] like Cursor can significantly "Empower you to build things in just days or hours instead of doing in multiple days" <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. By leveraging AI chat functionalities, developers can not only generate initial code but also iteratively refine and improve the UI and UX of their applications with considerable efficiency <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.