---
title: Understanding and Utilizing Style Weight
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

Midjourney treats image generation as a new medium, offering a canvas with layers of aesthetics and complexity that can be blended and balanced to achieve harmony <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This approach allows users to [[personalization_and_stylizing_in_ai_art | personalize and stylize AI art]] far beyond simple text prompts <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. One of the key "levers" for guiding the aesthetic direction is **Style Weight**.

## What is Style Weight?

Style Weight, accessed via the parameter `--sw` (or `-sw`), is a crucial parameter that determines how much influence a [[exploring_style_references_and_aesthetics | style reference image]] has over the generated image <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. It allows users to balance the aesthetic impact of a visual input against the textual prompt.

### Default Value and Range
By default, the style weight is set to `100` <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. However, it can be adjusted from `0` all the way up to `1000` <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

## How Style Weight Influences Generations

When a style reference image is provided, Midjourney attempts to understand its core aesthetic qualities, decoupling them from the subject matter <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

-   **Higher Style Weight**: Increasing the style weight (e.g., to `1000`) makes the generated image much more likely to adopt the look and feel of the [[exploring_style_references_and_aesthetics | style reference]] <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. This is useful when you want to strongly adhere to a specific visual aesthetic.
-   **Lower Style Weight**: Conversely, decreasing the style weight (e.g., to `50` or below the default `100`) reduces the impact of the [[exploring_style_references_and_aesthetics | style reference]], giving more room for the text prompt and other settings (like [[personalization_and_stylizing_in_ai_art | personalization]]) to influence the final output <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a><a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>.

It's important to understand the difference between a **style reference** (indicated by a paperclip icon) and an **image prompt** (indicated by a pict icon). An image prompt tends to pull in the subject matter and actual pixels of the input image, while a style reference focuses purely on the aesthetic <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a><a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a><a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.

## Balancing Aesthetics with Text Prompts

The entire process of effective prompting in Midjourney revolves around finding balance and harmony between different "aesthetic levers" <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a><a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a><a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>. Style weight is one of these crucial levers.

-   Initially, you might start with a basic subject and a [[exploring_style_references_and_aesthetics | style reference]] to see how Midjourney interprets the style <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a><a class="yt-timestamp" data-t="00:16:18">[00:16:18]</a>.
-   If the results are too photorealistic or deviate from the desired aesthetic, increasing the style weight can push the generation closer to the reference <a class="yt-timestamp" data-t="00:16:51">[00:16:51]</a><a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
-   Adding descriptive text to the prompt (e.g., "paper cutout illustration") can provide additional assistance to Midjourney, supporting the aesthetic direction hinted at by the style reference <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a><a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a><a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

The goal is to analyze the results and make guided decisions about where to take the image next, adjusting parameters like style weight and text prompts iteratively <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a><a class="yt-timestamp" data-t="00:42:06">[00:42:06]</a>.

## Experimenting with Style Weight

To effectively utilize style weight, experimentation is key. Midjourney allows for "permutation prompts" using brackets `[]` and commas to run multiple values for a parameter at once <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a><a class="yt-timestamp" data-t="00:49:20">[00:49:20]</a>.

For example, to test different style weight values:
`[your prompt here] --sw [50, 100, 200, 500, 1000]`

This allows for quick visual comparison of how different style weight levels affect the output, helping you identify the optimal range for your desired aesthetic <a class="yt-timestamp" data-t="00:49:30">[00:49:30]</a><a class="yt-timestamp" data-t="00:49:39">[00:49:39]</a><a class="yt-timestamp" data-t="00:49:41">[00:49:41]</a>.

## Combining Style Weight with Other Features

Style weight can be combined with other powerful Midjourney features to further refine the aesthetic:

-   **Multiple Style References**: You can include multiple [[exploring_style_references_and_aesthetics | style references]] in a single prompt. Midjourney will blend these styles together, and you can even assign different weights to each reference (e.g., `--sref <url1>::2 --sref <url2>::1`) to control their individual influence <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a><a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a><a class="yt-timestamp" data-t="00:44:52">[00:44:52]</a>.
-   **[[personalization_and_stylizing_in_ai_art | Personalization]]**: Your own personal aesthetic preferences, learned by Midjourney through your image ratings in the "Personalize" tab, act as another aesthetic lever <a class="yt-timestamp" data-t="00:29:36">[00:29:36]</a><a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a><a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>. This [[personalization_and_stylizing_in_ai_art | personalization]] can be balanced with the style reference and text prompt <a class="yt-timestamp" data-t="00:35:15">[00:35:15]</a><a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.
-   **Stylize Parameter (`--s`)**: This parameter controls how much of Midjourney's default, community-curated aesthetic is applied to your prompt. Higher stylize values make the image look more "AI-generated" in the traditional Midjourney sense, while lower values give more creative leeway <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a><a class="yt-timestamp" data-t="00:31:23">[00:31:23]</a><a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. When combined with [[personalization_and_stylizing_in_ai_art | personalization]], stylize dictates the influence of *your* fine-tuned aesthetic <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a><a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>.

By understanding and strategically utilizing style weight alongside these other parameters, users gain significant creative control over their AI art, moving beyond "slot machine" prompting to intentionally shape their aesthetic direction <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a><a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a><a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a>.