---
title: Personalization and style reference codes in MidJourney
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

[[AI design tools like Runway and Midjourney | MidJourney]] is considered a new medium entirely, offering a different type of canvas and a different way of problem-solving for creative exploration <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. It allows users to blend and balance aesthetics to achieve desired results <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Once a "recipe" is found, it can be infinitely prompted <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## MidJourney's Evolution
Initially, [[visual_versus_text_prompts_in_midjourney | MidJourney]] primarily relied on word prompts and parameters <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. Image prompts existed but mainly pulled subject matter and elements, often not the desired outcome <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. In recent months, significant features like Style Space, style references, and character references have been introduced <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>, allowing for more visual-driven creation <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

### Why Use MidJourney?
[[midjourney_for_inspiration_and_creative_exploration | MidJourney]] serves as a powerful inspiration tool, similar to building a mood board through Pinterest or Google image searches, but with more control <a class="yt-timestamp" data-t="00:11:36">[00:11:36]</a>. It's excellent for ideating, putting together concepts, and exploring designs <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. It's also a fun "art therapy" that users can get lost in <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. The goal is to gain enough understanding to be "dangerous" and effectively explore aesthetics <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

## Navigating MidJourney
The primary place for working in [[midjourney_as_a_new_design_canvas | MidJourney]] is the web app at Midjourney.com, rather than Discord <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   **Create Tab**: This is where most of the generation work happens <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Explore Tab**: Displays publicly available generations, serving as a source of inspiration <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Users can search for specific styles (e.g., "vintage poster") <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   **Image Search**: Clicking the search icon on an image in the Explore tab finds similar results based on subject matter and style <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
    *   **Use Prompt/Style/Image**: Options available when viewing an image in the Explore tab:
        *   `Use prompt`: Copies the text prompt <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
        *   `Use style`: Imports the image as a style reference (paperclip icon) <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
        *   `Use image`: Imports the image as an image prompt (pict icon), which differs from a style reference <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.
*   **Stealth Mode**: For professional or client work, enable stealth mode in settings (Pro Plan or above) to prevent assets from appearing in the public database <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.
*   **Liking Favorites**: Users should "heart" or "like" their favorite generations to easily find them later in the "organize" tab <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.

## Understanding Aesthetic Levers

### Style References (Images)
When an image is dragged into the prompt bar, it defaults to an image prompt (pict icon) <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.
*   **Style Reference (Paperclip icon)**: This is used to inform MidJourney of the aesthetic style of an image without incorporating its subject matter <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. MidJourney attempts to decouple the aesthetic from the subject <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
*   **Image Prompt (Pict icon)**: This tells MidJourney to pull in more of the actual subject matter or pixels from the image <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. Increasing its weight (e.g., `--iw` parameter implicitly discussed) can lead to elements from the reference image appearing in the generation (e.g., a hand in a giraffe image) <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>. This is an important distinction to avoid "wonky" results <a class="yt-timestamp" data-t="00:21:15">[00:21:15]</a>.
*   **Style Weight (`--sw`)**: This parameter determines how much influence a style reference image has over the generation <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>. Default is 100, but can go up to 1000 <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>. A higher value means the generation will lean more towards the style reference <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>.
*   **Blending Styles**: Multiple style references can be added to blend their aesthetics <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.

### Style Reference Codes (SRF Codes)
SRF codes are like "coordinates in a multi-dimensional Style Space" that direct the generation to a specific aesthetic location <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. There are billions of possible SRF codes <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.
*   **Discovery**: Users can find and curate SRF codes into lists to build "aesthetic recipes" <a class="yt-timestamp" data-t="00:38:15">[00:38:15]</a>. Tools exist to visually explore these codes <a class="yt-timestamp" data-t="00:39:01">[00:39:01]</a>.
*   **Usage**: Instead of an image, an SRF code (e.g., `srf <code_number>`) is added to the prompt <a class="yt-timestamp" data-t="00:38:45">[00:38:45]</a>.
*   **Blending SRF Codes**: Multiple SRF codes can be combined to blend different styles <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>. These styles represent color, composition, lighting, texture, pattern, and more <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>.
*   **Weighting Multiple SRF Codes**: Use `::` after an SRF code to assign a relative weight (e.g., `srf <code>::2 srf <other_code>::1`) <a class="yt-timestamp" data-t="00:44:34">[00:44:34]</a>. This allows control over how much each style contributes to the blend <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>.

### Personalization
Personalization fine-tunes the MidJourney model to a user's specific aesthetic preferences <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>.
*   **How it Works**: Users activate personalization by rating images in the "Personalize" tab. By selecting favorite images, MidJourney learns preferences like preferred colors, lighting, general style (photographic vs. illustrative), and even subject matter <a class="yt-timestamp" data-t="00:29:40">[00:29:40]</a>. Rating many images (e.g., a thousand) is highly recommended <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>.
*   **Stylize (`--s`)**: This parameter controls how much of the MidJourney model's curated aesthetics (or, with personalization, the user's fine-tuned aesthetics) are applied to the text prompt <a class="yt-timestamp" data-t="00:31:23">[00:31:23]</a>.
    *   High stylize values (e.g., `s 1000`) with *no personalization* tend to produce results that "scream AI" or look like the default MidJourney aesthetic <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.
    *   With *personalization turned on*, a high stylize value will lean heavily into the user's learned preferences, creating a "totally different universe" of style <a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>.
    *   The default stylize value (100) balances the text prompt with MidJourney's aesthetics <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
*   **Layering**: Personalization can be layered with style references (images and SRF codes) and text prompts, creating a complex interplay of aesthetic influences <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

## Practical Techniques

### Text Prompting
While visuals drive much of the style, text prompts still play a vital role, especially for specifying subject matter or supporting visual style (e.g., "paper cutout illustration of a giraffe") <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
*   **No Parameter (`--no`)**: Can be used to explicitly tell MidJourney what elements to remove from a generation (e.g., `--no text`) <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>.

### Image Manipulation
*   **Editor**: Allows users to paint out unwanted elements in an image to remove them <a class="yt-timestamp" data-t="00:26:29">[00:26:29]</a>. It can also be used to adjust aspect ratios and reposition elements before generating new parts of an image <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>.

### Prompt Parameters & Workflow
*   **Aspect Ratio (`--ar`)**: Used to set the desired aspect ratio of the image, important for specific outputs like posters (e.g., `--ar 2:3`) <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   **Variations**:
    *   `Subtle`: Keeps most details intact but changes minor aspects <a class="yt-timestamp" data-t="00:25:38">[00:25:38]</a>.
    *   `Strong`: Leads to more dramatic changes in composition while retaining the general vibe and subject matter <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>.
*   **Permutation Prompts**: Using brackets `[]` and commas `,` allows running multiple values for a parameter in a single prompt (e.g., `[value1, value2]`), enabling quick experimentation and comparison <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>.
*   **Re-running Prompts**: After hitting Enter, pressing the up arrow on the keyboard automatically populates the prompt bar with the last command <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>.

## The Philosophy of "Balance and Harmony"
The core of using [[exploring_aesthetics_with_style_space_in_midjourney | MidJourney]] effectively is finding balance and harmony among its various "levers" <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>. By visually analyzing results and making guided decisions, users can push aesthetics in desired directions <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>. The goal is to move beyond "playing the slot machine game" of random prompting and gain a deeper understanding of why results appear as they do <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>. This approach turns MidJourney into a creative canvas where users have significant control over the aesthetic direction <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>.