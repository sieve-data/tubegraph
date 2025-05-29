---
title: Using DeepSeek and Qwen models for coding assistance
videoId: P_mIfIbWS8c
---

From: [[amiteshanand]] <br/> 

This article explores the development of a [[building_vscode_extensions_using_ai_models | VS Code extension]] designed to assist with coding, built primarily using Cursor and integrating various AI models, including [[using_deepseek_v3_and_r1_models | DeepSeek]] and [[introduction_to_qwen3_for_ai_and_job_search_functionality | Qwen models]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. The extension leverages [[using_deep_learning_models_for_content_generation | deep learning models]] to provide coding assistance.

## Building the VS Code Extension with Cursor

The entire [[building_vscode_extensions_using_ai_models | VS Code extension]] was built using Cursor, requiring only a single prompt to initiate the development process <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. The creator provided one prompt to Cursor and then used Cursor's chat feature to build, iterate, and improve the extension <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The source code for the extension is available as a repository for anyone wishing to try it out or improve it <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.

## Model Integration and Usage

The extension integrates several models from Nebius AI Studio <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Users need to provide an API key from Nebius AI Studio to use the extension's features <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. Nebius AI Studio offers various AI models for development and side projects, providing $1 worth of credit upon sign-up and additional credits via coupon codes <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

The specific models used in the extension include:
*   [[using_deepseek_v3_and_r1_models | DeepSeek]] Coder V2 Light <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>
*   [[introduction_to_qwen3_for_ai_and_job_search_functionality | Qwen]] 2.5 Coder 7B Instruct <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>
*   [[introduction_to_qwen3_for_ai_and_job_search_functionality | Qwen]] 2.5 Coder 32B Instruct <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>
*   [[using_deepseek_v3_and_r1_models | DeepSeek V3]] <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>

### Functionality Demonstration

After entering the API key, users can select a model and input code for assistance.
*   **Code Explanation**: When asked to explain a JavaScript code snippet, the [[introduction_to_qwen3_for_ai_and_job_search_functionality | Qwen]] 2.5 Coder model successfully broke down the code into components like constant variables <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Code Translation**: The [[using_deepseek_v3_and_r1_models | DeepSeek]] Coder V2 Light model was able to provide an equivalent Python code for a given JavaScript context, demonstrating its code translation capabilities <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### Model Performance Notes

While the extension allows selection between various models, some observations were made regarding their performance:
*   [[using_deepseek_v3_and_r1_models | DeepSeek V3]] was noted to take significantly longer than other models to provide an answer <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.
*   [[using_deepseek_v3_and_r1_models | DeepSeek R1]] was intentionally excluded from the extension due to its even longer processing times compared to [[using_deepseek_v3_and_r1_models | DeepSeek V3]] <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

## UI/UX Improvement with Cursor

Initially, the extension's UI/UX was basic <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. The developer used Cursor's chat feature to prompt for improvements to the overall UI/UX, asking it to enhance formatting by making sentences bold or italic and picking colors for code responses <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. Cursor made changes to the `chatPanel.ts` file, leading to styling enhancements, font color adjustments, and improved formatting <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. Although initial attempts at formatting were not perfect, further prompts with Cursor could resolve these issues <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. The extension also demonstrated the ability to generate CSS code for additional styling <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>.

## Conclusion

This project highlights the power of AI-powered tools like Cursor in rapidly building applications, such as a [[building_vscode_extensions_using_ai_models | VS Code extension]], within days or hours instead of multiple days <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. The integration of [[using_deepseek_v3_and_r1_models | DeepSeek]] and [[introduction_to_qwen3_for_ai_and_job_search_functionality | Qwen models]] via Nebius AI Studio provides a robust coding assistance tool, demonstrating the practical application of [[using_deep_learning_models_for_content_generation | deep learning models]] in a development environment <a class="yt-timestamp" data-t="00:08:13">[00:08:13]</a>.