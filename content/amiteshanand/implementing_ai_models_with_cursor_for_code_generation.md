---
title: Implementing AI models with Cursor for code generation
videoId: P_mIfIbWS8c
---

From: [[amiteshanand]] <br/> 

This article details the process of building a VS Code extension that utilizes various AI models for code generation and explanation, primarily developed using [[enhancing_vscode_extension_ui_with_cursor | Cursor]]. The extension serves as a basic tool to assist with coding tasks by interacting with Deep Seek and Quin models.

## Project Overview

A VS Code extension was developed to provide AI-assisted coding features <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. The core development was carried out using [[enhancing_vscode_extension_ui_with_cursor | Cursor]] <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. The extension integrates with Deep Seek and Quin models to help users code <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>, <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The project is open-source, with its repository available for local installation and improvements <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Development with Cursor

The majority of the extension's code was written by [[enhancing_vscode_extension_ui_with_cursor | Cursor]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>, <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. The developer initiated the process with a single prompt to [[enhancing_vscode_extension_ui_with_cursor | Cursor]]'s chat feature, then continued to prompt the AI to build, iterate, and improve the extension <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>, <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

## How to Use the Extension

1.  **Run the Extension:** After compiling, press `F5` to open the VS Code development host server for the extension <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>, <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>.
2.  **Access the Chat:** Use `Command + Shift + P` (or `Ctrl + Shift + P` on Windows) and select "deep coin coded chat" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>, <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
3.  **Enter API Key:** An API key is required from [[text_and_image_generation_using_nebius_ai_models | Nebius AI Studio]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>, <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
4.  **Select a Model:** Choose from available models in [[text_and_image_generation_using_nebius_ai_models | Nebius AI Studio]] like Deep Seek Coder V2 Light, Quin 2.5 Coder 7B, Quin 2.5 Coder 32B, and Deep Seek B3 <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>, <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
5.  **Interact:** Paste code or ask questions in the chat interface <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>, <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Supported AI Models

The extension leverages several models from [[text_and_image_generation_using_nebius_ai_models | Nebius AI Studio]]:
*   Deep Seek Coder V2 Light <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   Quin 2.5 Coder 7B Instruct <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>
*   Quin 2.5 Coder 32B Instruct <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>, <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>
*   Deep Seek B3 <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>, <a class="yt-timestamp" data-t="00:07:48">[00:07:48]</a>

> [!NOTE]
> Deep Seek R1 was not included due to longer inference times compared to Deep Seek B3 <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>, <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.

## Capabilities and Demonstrations

The extension was demonstrated through several tasks:

*   **Code Explanation:** Providing an explanation of a given JavaScript code snippet <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>, <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. The Quin 2.5 Coder model broke down constants and variables <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Code Translation:** Attempting to translate a JavaScript context into Python using Deep Seek Coder V2 Light <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>, <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>, <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. The model successfully generated equivalent Python code <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.
*   **UI/UX Improvement:** Using [[enhancing_vscode_extension_ui_with_cursor | Cursor]] chat to iterate and improve the extension's user interface and experience <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>, <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. Prompts were given to improve overall UI/UX, formatting, and color choices for code responses <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>, <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>, <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>. [[enhancing_vscode_extension_ui_with_cursor | Cursor]] made changes to the `chatPanel.ts` file for UI generation <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>, <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>, <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>, including styling enhancements, font colors, bold/italic formatting, and code formatting <a class="yt-timestamp" data-t="00:05:10">[00:05:10]</a>, <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>, <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

## Limitations and Future Improvements

Despite [[enhancing_vscode_extension_ui_with_cursor | Cursor]]'s effectiveness, some limitations were noted:
*   **Formatting Issues:** Initial output formatting was not ideal, with unformatted text and colors <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>, <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>. While [[enhancing_vscode_extension_ui_with_cursor | Cursor]] could iterate to improve this, further prompts would be needed <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>, <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
*   **UI Attractiveness:** The UI generated by [[enhancing_vscode_extension_ui_with_cursor | Cursor]] was described as "not that great" visually <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>, despite [[enhancing_vscode_extension_ui_with_cursor | Cursor]] doing a "good job" in functionality <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
*   **Model Speed:** Deep Seek B3 was observed to take longer to provide answers compared to other models <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>, <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

Custom CSS files can be incorporated for more advanced styling <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>, <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

## Power of AI Tools in Development

[[enhancing_vscode_extension_ui_with_cursor | Cursor]]'s ability to create a complex VS Code extension from scratch demonstrates its power in development <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>, <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Tools like [[enhancing_vscode_extension_ui_with_cursor | Cursor]] and Wind Surf can significantly reduce development time from days to hours <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>, <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>.

[[text_and_image_generation_using_nebius_ai_models | Nebius AI Studio]] was chosen as the inference provider for API keys and model implementation due to its affordability <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>, <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>, <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. Users signing up for [[text_and_image_generation_using_nebius_ai_models | Nebius AI Studio]] receive $1 worth of credit, with additional credits potentially available via coupon codes <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>, <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>, <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.