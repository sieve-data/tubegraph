---
title: Using AI models for coding assistance
videoId: P_mIfIbWS8c
---

From: [[amiteshanand]] <br/> 

AI models can be leveraged to create coding assistants and VS Code extensions, significantly speeding up development time. One such approach involves using tools like Cursor to build custom extensions that integrate various AI models for code explanation, translation, and other coding tasks <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Building an AI-Powered VS Code Extension

A VS Code extension can be entirely built using Cursor, an AI-powered coding tool. The process involves providing an initial prompt to Cursor, then iteratively asking the AI chat to build, refine, and improve the extension <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>.

The extension can integrate various AI models to provide coding assistance:
*   **Deepseek Model** <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>
    *   Deepseek Coder V2 Light <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>
    *   Deepseek B3 <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>
*   **Quan Model** <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>
    *   Quan 2.5 Coder <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a> (including 7B Instruct and 32B Instruct variants <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>)

The source code for such an extension can be made available for others to try out or improve upon <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Functionality of the Extension

Once built, the VS Code extension operates as a coding copilot. Users must first enter an API key, typically obtained from a service like [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

Key functionalities include:
*   **Model Selection** Users can choose from the integrated AI models, such as Quan 2.5 Coder or Deepseek B3, to handle their requests <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Code Explanation** Users can paste code snippets and ask the AI to explain the code, which the AI breaks down step-by-step <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
*   **Code Transformation** The AI can attempt to translate code from one language to another, such as JavaScript to Python <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Iterative Improvement with AI

Even after initial generation, the AI can be used to refine and improve the extension. For instance, if the UI/UX or response formatting is not ideal, prompts can be given to Cursor to:
*   Improve overall UI/UX <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   Enhance formatting by making sentences bold or italic, and selecting appropriate colors for code responses <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   Fix structural issues like missing HTML tags in the generated code <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

While AI tools like Cursor can rapidly generate code, some manual tweaking or further AI prompts might be needed to perfect the output's formatting and presentation <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.

## API Key Provider

The integration of various AI models for inference requires an API key provider. [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]] is noted as a source for API keys and for implementing models, offering a cheaper inference cost <a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>. Users signing up often receive credit to use the service <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

## Power of AI Tools

Tools like Cursor and platforms like [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]] empower developers to [[building_an_aipowered_app_without_coding | build AI-powered applications]] and extensions in a significantly reduced timeframe—days or even hours, as opposed to multiple days <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. This demonstrates a key [[ai_coding_copilot_use_case | AI coding copilot use case]].