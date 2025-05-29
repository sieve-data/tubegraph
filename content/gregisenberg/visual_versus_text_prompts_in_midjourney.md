---
title: Visual versus text prompts in MidJourney
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

MidJourney is considered a new medium entirely, offering a different type of canvas and a distinct approach to problem-solving in design <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>. It allows users to blend and balance entire aesthetics with layers and complexity to achieve desired artistic outcomes <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Limitations of Text-Based Prompting
Many users begin their [[ai_design_tools_like_runway_and_midjourney | MidJourney]] journey by using words and prompts found on platforms like Twitter <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>. While words are still valuable, they are merely "the tip of the iceberg" <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a> <a class="yt-timestamp" data-t="01:09:09">[01:09:09]</a>. Historically, MidJourney primarily relied on structuring text prompts and parameters, with image prompts only pulling subject matter rather than style <a class="yt-timestamp" data-t="01:12:14">[01:12:14]</a> <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. This approach can be limiting, as the model's interpretation of a word often yields a consistent but narrow aesthetic <a class="yt-timestamp" data-t="01:56:58">[01:56:58]</a>.

## Embracing Visual Prompting for Broader Exploration
In recent months, MidJourney has introduced features like Style Space, Style References, and Character References, which "explodes aesthetics out into this infinite universe" <a class="yt-timestamp" data-t="02:19:22">[02:19:22]</a>. This allows for a more visual approach to creation, moving beyond semantic interpretations <a class="yt-timestamp" data-t="02:36:38">[02:36:38]</a>. The core principle of [[exploring_aesthetics_with_style_space_in_midjourney | visual prompting]] is to use visuals to drive visuals, enabling exploration of "aesthetics and style space into almost infinite directions" <a class="yt-timestamp" data-t="01:12:12">[01:12:12]</a> <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

### Key Visual Prompting Techniques

1.  **Image Prompts vs. Style References**
    *   **Image Prompt**: When an image is used as an image prompt (default behavior), MidJourney attempts to pull in the subject matter and actual pixels from the image, often leading to "wonky" results if the goal is purely stylistic <a class="yt-timestamp" data-t="02:00:00">[02:00:00]</a> <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.
    *   **Style Reference**: By selecting the "paperclip" icon, an image is used as a style reference. This instructs MidJourney to analyze the image's aesthetic (color, composition, lighting, texture, pattern) and apply that style to the generated image, while decoupling it from the original subject matter <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a> <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>. This is crucial for guiding the aesthetic direction without pulling specific elements <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.

2.  **Balancing Levers: Parameters and Text Prompts**
    *   **Style Weight (`--sw`)**: This parameter controls how much influence the style reference has over the generation. The default is 100, but it can be increased up to 1000 for a stronger stylistic adherence <a class="yt-timestamp" data-t="01:17:18">[01:17:18]</a> <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
    *   **Aspect Ratio (`--ar`)**: Helps shape the output, such as using `2:3` for a poster print <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
    *   **Text Prompt Refinement**: Even with style references, adding descriptive text (e.g., "a paper cutout illustration") can provide "assistance" and guide MidJourney towards the desired medium or look <a class="yt-timestamp" data-t="01:18:05">[01:18:05]</a> <a class="yt-timestamp" data-t="01:18:07">[01:18:07]</a>. The goal is to find a balance and harmony between all inputs <a class="yt-timestamp" data-t="01:28:29">[01:28:29]</a>.

3.  [[personalization_and_style_reference_codes_in_midjourney | Personalization]]
    *   MidJourney can learn a user's aesthetic preferences by rating images in the "Personalize" tab. This fine-tunes the model to align with individual tastes, influencing colors, lighting, general style (photographic vs. illustrative), and even preferred subjects <a class="yt-timestamp" data-t="02:59:00">[02:59:00]</a>. This can significantly change the aesthetics of generations, moving away from the default "MidJourney look" <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
    *   The `stylize` parameter (`--s`) controls how much of the model's curated aesthetics (including personalizations) are applied to the text prompt. A high `stylize` value makes the image "scream AI" <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>.

4.  **Style Reference Codes (SRF)**
    *   SRF codes (e.g., `sref random_number`) are like coordinates in a "multi-dimensional Style Space" <a class="yt-timestamp" data-t="03:37:01">[03:37:01]</a>. They direct the model to a specific location in this space, influencing anything prompted thereafter <a class="yt-timestamp" data-t="03:37:01">[03:37:01]</a>.
    *   These codes represent deep aesthetic properties beyond simple color, including composition, lighting, texture, and pattern <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.
    *   Users can combine multiple SRF codes (e.g., `sref code1::2 code2::1`) to blend different styles, akin to mixing "paint on a palette" <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a> <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. The weights (`::2`, `::1`) control the influence of each style <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.

## Workflow and Iteration
[[sequential_prompting_for_ai_workflows | Exploring aesthetics]] in MidJourney is an iterative process. It involves:
*   Starting with basic ideas and style references to see how MidJourney interprets them <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.
*   Making "guided decisions" based on initial results, refining text prompts and adjusting parameters like style weight and aspect ratio <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
*   Experimenting with variations (subtle or strong) to explore different compositions while maintaining the general vibe <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
*   Using permutation prompts (e.g., `--sw 50,100,500`) to test multiple parameter values at once for rapid visual comparison <a class="yt-timestamp" data-t="04:19:00">[04:19:00]</a>.
*   Actively liking favorite generations for easier organization and future reference in the library <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.
*   Leveraging the MidJourney web app (`midjourney.com`) for a better user experience than Discord <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

This process moves beyond a "slot machine game" of random prompting, enabling users to build "aesthetic recipes" and gain control over the artistic direction <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a> <a class="yt-timestamp" data-t="04:29:00">[04:29:00]</a>. The goal is to find "harmony" and "balance" between all the aesthetic levers <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>.

Ultimately, this advanced approach to prompting allows users to take their ideas and transform them into "living breathing design assets" <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a>, providing significant creative control and leading to results that are indistinguishable from traditional art <a class="yt-timestamp" data-t="05:50:00">[05:50:00]</a>. [[midjourney_for_inspiration_and_creative_exploration | MidJourney functions as a discovery engine]] and inspiration tool, helping users ideate, explore, and even engage in what can be considered "art therapy" <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a> <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.