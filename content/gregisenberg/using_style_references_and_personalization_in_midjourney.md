---
title: Using style references and personalization in Midjourney
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 
[[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] is considered a [[midjourney_as_a_new_artistic_medium | new artistic medium]], offering a different type of canvas and problem-solving approach. <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a> Instead of just paint, users can blend and balance entire aesthetics with multiple layers and complexity to achieve a desired harmony. <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a> Once a "recipe" is found, it can be infinitely prompted. <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>

## Getting Started with Midjourney
To begin, users should access the [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] web app at midjourney.com, as it is no longer recommended to work within Discord due to its "hellish" interface. <a class="yt-timestamp" data-t="06:35:32">[06:35:32]</a> <a class="yt-timestamp" data-t="06:38:00">[06:38:00]</a> The "Create" tab is where most time will be spent. <a class="yt-timestamp" data-t="06:54:57">[06:54:57]</a>

### Finding Inspiration
Inspiration can be found both externally and within [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] itself:
*   **External Sources**: Websites like Reddit, Pinterest, or even Google Images can provide inspiration. <a class="yt-timestamp" data-t="05:44:00">[05:44:00]</a>
*   **Midjourney's Explore Tab**: This tab displays all publicly available generations. <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a> Users can search for specific themes (e.g., "vintage poster") <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a> and use the search icon to find similar images based on subject matter and style. <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>
    *   **Privacy Note**: If using [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] for client work or with proprietary imagery, ensure you are on the Pro Plan or above and have "stealth mode" turned on in the settings to prevent assets from appearing in the public database. <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a> <a class="yt-timestamp" data-t="10:48:00">[10:48:00]</a>

## The Power of Midjourney
[[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] serves as a powerful [[inspiration_and_iteration_in_design | inspiration]] and ideation tool, similar to building a mood board, but with greater control over the generated content. <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a> It can be used for professional production, especially with the editor feature for outpainting or adding new elements. <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a> It can also be a form of "art therapy," allowing users to get lost in the creative process. <a class="yt-timestamp" data-t="12:16:00">[12:16:00]</a> Ultimately, it's a "discovery engine" for exploring aesthetics and turning ideas into visual assets. <a class="yt-timestamp" data-t="12:30:00">[12:30:00]</a>

## [[parameters_and_controls_for_achieving_desired_artistic_outcomes_with_midjourney | Parameters and Controls]] for [[creating_art_with_ai_and_blending_aesthetics_in_midjourney | Artistic Outcomes]]

### Image Prompt vs. Style Reference
A crucial distinction in [[parameters_and_controls_for_achieving_desired_artistic_outcomes_with_midjourney | Midjourney]] is how an image is used in a prompt:
*   **Image Prompt**: When an image is added via the image icon and left as default (little pict icon), [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] attempts to pull in the subject matter and actual pixels of that image. <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a> <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a> Increasing its weight can lead to blending the subject from the reference image with the text prompt (e.g., a "hand giraffe"). <a class="yt-timestamp" data-t="20:45:00">[20:45:00]</a>
*   **Style Reference**: By selecting the paperclip icon next to an uploaded image, it becomes a style reference. <a class="yt-timestamp" data-t="14:32:00">[14:32:00]</a> <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a> This allows [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] to decouple the aesthetic from the subject matter, applying the visual style to the new generation without bringing in the original content. <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>

### Balancing Aesthetic Levers
[[creating_art_with_ai_and_blending_aesthetics_in_midjourney | Achieving desired artistic outcomes]] involves balancing various "aesthetic levers": <a class="yt-timestamp" data-t="28:57:00">[28:57:00]</a>

1.  **Style Weight (`--sw`)**: This parameter determines how much influence a style reference has over the generation. <a class="yt-timestamp" data-t="17:18:00">[17:18:00]</a> It defaults to 100 but can go up to 1000. Higher values make the output more aligned with the style reference. <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a> <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>
2.  **Text Prompt**: Simple text prompts can be refined to guide the [[ai_tools_like_midjourney_and_chat_gpt | AI]] more precisely. For example, adding "a paper cutout illustration" to "giraffe" helps the [[ai_tools_like_midjourney_and_chat_gpt | AI]] align with the desired artistic style. <a class="yt-timestamp" data-t="18:05:00">[18:05:00]</a>
3.  **Aspect Ratio (`--ar`)**: Use this parameter to control the image dimensions, such as `--ar 2:3` for a poster-like layout. <a class="yt-timestamp" data-t="19:03:00">[19:10:00]</a>
4.  **No Parameter (`--no`)**: Use `--no [keyword]` to tell [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] what you want removed from the generation (e.g., `--no text`). <a class="yt-timestamp" data-t="26:52:00">[26:52:00]</a>
5.  **Stylize (`--s`)**: This parameter controls how much of the [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] model's default, community-curated aesthetic is applied to your prompt. <a class="yt-timestamp" data-t="31:20:00">[31:20:00]</a> Higher values (e.g., 1000, versus the default 100) will make the image look more "[[ai_tools_like_midjourney_and_chat_gpt | AI]]-screaming" or like the model's default style. <a class="yt-timestamp" data-t="31:55:00">[31:55:00]</a>

### Personalization
[[developing_and_customizing_aidriven_projects | Personalization]] allows [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] to learn a user's aesthetic preferences: <a class="yt-timestamp" data-t="29:37:00">[29:37:00]</a>
*   **Training**: By regularly rating images in the "Personalize" tab, [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] learns your preferences for colors, lighting, style (photographic vs. illustrative), and even subject matter. <a class="yt-timestamp" data-t="29:40:00">[29:40:00]</a> <a class="yt-timestamp" data-t="30:13:00">[30:13:00]</a>
*   **Impact**: With [[developing_and_customizing_aidriven_projects | personalization]] turned on, the model fine-tunes its output to your specific aesthetic, making generations more aligned with your taste. <a class="yt-timestamp" data-t="32:31:00">[32:31:00]</a> <a class="yt-timestamp" data-t="32:41:00">[32:41:00]</a> This is distinct from the default model aesthetics. <a class="yt-timestamp" data-t="32:26:00">[32:26:00]</a>
*   **Blending Personalizations**: It's possible to combine your [[developing_and_customizing_aidriven_projects | personalization]] with another user's, and even assign different weights to each, creating unique blends of styles. <a class="yt-timestamp" data-t="34:58:00">[34:58:00]</a>

### Style Reference (SRF) Codes
SRF codes are like "coordinates" in a "multi-dimensional Style Space" that direct [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]] to a specific aesthetic location. <a class="yt-timestamp" data-t="37:31:00">[37:31:00]</a> <a class="yt-timestamp" data-t="37:38:00">[37:38:00]</a>
*   **Usage**: Instead of uploading an image, users can paste an SRF code into their prompt (e.g., `--sref [code]`). <a class="yt-timestamp" data-t="38:35:00">[38:35:00]</a> <a class="yt-timestamp" data-t="39:20:00">[39:20:00]</a>
*   **Exploration**: Tools like the "Style Reference Explorer" can help users visually search and discover SRF codes based on style, vibe, or theme. <a class="yt-timestamp" data-t="36:50:00">[36:50:00]</a>
*   **Blending**: Multiple SRF codes can be combined in a single prompt to blend different aesthetic elements like color, composition, lighting, texture, and pattern. <a class="yt-timestamp" data-t="39:59:00">[39:59:00]</a> <a class="yt-timestamp" data-t="40:17:00">[40:17:00]</a> Weights can be assigned to individual SRF codes using double colons (e.g., `--sref code1::2 code2::1`) to control their influence. <a class="yt-timestamp" data-t="44:31:00">[44:31:00]</a>

## Advanced Techniques and Workflow Tips
*   **Liking Favorites**: To easily find preferred generations later, "like" them by clicking the heart icon or right-clicking on the image. This organizes them in the "Organize" tab. <a class="yt-timestamp" data-t="27:22:00">[27:22:00]</a>
*   **Permutation Prompts**: Use brackets and commas (e.g., `{100, 200, 500}`) with parameters like `--sw` to run multiple values in one go, allowing for quick visual comparison of results. <a class="yt-timestamp" data-t="49:17:00">[49:17:00]</a>
*   **The Editor**: The editor feature allows for modifying existing assets, such as outpainting, adding new elements, or painting out unwanted elements like text. <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a> <a class="yt-timestamp" data-t="50:47:00">[50:47:00]</a>

By mastering these [[parameters_and_controls_for_achieving_desired_artistic_outcomes_with_midjourney | parameters and controls]], users can move beyond a "slot machine game" approach <a class="yt-timestamp" data-t="45:37:00">[45:37:00]</a> and gain significant creative control over [[ai_tools_like_midjourney_and_chat_gpt | Midjourney]], truly "stealing like an artist" to create unique and desired visual outcomes. <a class="yt-timestamp" data-t="46:01:00">[46:01:00]</a> The emphasis shifts from semantic interpretation to visually driven aesthetic blending. <a class="yt-timestamp" data-t="46:53:00">[46:53:00]</a>