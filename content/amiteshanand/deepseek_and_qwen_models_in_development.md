---
title: DeepSeek and Qwen models in development
videoId: P_mIfIbWS8c
---

From: [[amiteshanand]] <br/> 

This article details the development of a basic [[building_a_chrome_extension_with_deepseek_and_flux | VS Code extension]] that leverages [[deepseek_r10528_model_capabilities | DeepSeek]] and [[qwen_3235b_a22b_model_comparison | Qwen]] models to assist with coding <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The extension was built primarily using Cursor, an AI-powered coding environment <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Development Process with Cursor

The entire codebase for the extension was generated by Cursor through a series of prompts <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. The developer provided an initial prompt and then used Cursor's chat feature to iterate and improve the extension <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>.

To run the extension:
1.  Compile the project (Cursor handles this) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
2.  Click `F5` to open the VS Code development host server <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
3.  Use `Command + Shift + P` and select "Deep Coin Coded Chat" <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## Model Integration and Usage

The extension integrates various AI models, primarily accessed through [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]], which serves as an inference provider <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Users need to enter an API key from [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]] to utilize the models <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]] offers various AI models, including:
*   [[deepseek_r10528_model_capabilities | DC Coder V2 Light]] <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>
*   [[qwen_3235b_a22b_model_comparison | Qwen 2.5 Coders]] (7B and 32B Instruct) <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
*   [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek V3]] <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>

### Demonstration of Capabilities

During a demonstration, the extension was used to:
*   **Explain Code**: Using [[qwen_3235b_a22b_model_comparison | Qwen 2.5 Coder 32B Instruct]], the extension successfully explained a copied code segment, breaking it down into constant variables <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Translate Code**: Using [[deepseek_r10528_model_capabilities | DPC Coder V2 Light]], the extension attempted to translate a JavaScript code snippet into Python, generating an "equivalent Python code" <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## UI/UX Improvement Attempts

The initial UI of the extension was described as "not that great" <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>, with issues like poor formatting and un-punchy colors <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. The developer used Cursor's chat feature to prompt for improvements to the overall UI/UX, including formatting sentences with bold/italic text and picking colors for code responses <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Cursor made changes to the `chatPanel.ts` file for these enhancements <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

Despite these efforts, some formatting challenges persisted, such as proper styling of output and making specific words bold <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. The extension also demonstrated the ability to suggest creating a CSS file for custom styling <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>.

### Model Performance Notes
*   [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek V3]] was noted to take "a lot of time" compared to other models to provide answers <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek R1]] was not included in the extension due to expected longer thinking times compared to [[deepseek_v3_and_r1_for_technical_content_evaluation | DeepSeek V3]] <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## Key Takeaways

The project highlights the power of AI tools like Cursor in rapidly building applications within days or hours, rather than multiple days <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. The use of [[leveraging_nebas_ai_studio_for_open_source_model_access | Nebas AI Studio]] was beneficial for its cheaper inference provision and initial credit offerings <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>. The GitHub repository for this VS Code extension is publicly available for those interested in trying or improving it <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.