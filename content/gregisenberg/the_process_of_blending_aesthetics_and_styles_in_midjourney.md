---
title: The process of blending aesthetics and styles in MidJourney
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

MidJourney is considered a new medium and an entirely different type of canvas for problem-solving <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. It allows users to blend and balance entire aesthetics with layers and complexity to achieve desired visual outcomes <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Utilizing the MidJourney Web App
It is highly recommended to use the MidJourney web app (`midjourney.com`) instead of Discord, as it offers a more streamlined and efficient workflow <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The web app includes a "create" tab for generating images and an "explore" tab to discover publicly available generations <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.

## Finding Inspiration
Users can find [[inspiration_and_iteration_in_design | inspiration]] within MidJourney's "explore" tab by searching for concepts like "vintage poster" <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. If a particular "vibe" or style is appealing, clicking the search icon on an image will yield similar results <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. Outside of MidJourney, platforms like Reddit and Pinterest are excellent resources for visual inspiration <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.

## Image Prompts vs. Style References
A crucial distinction in MidJourney is between an image prompt and a style reference:
*   **Image Prompt (Pict Icon)**: When an image is used as a direct image prompt, MidJourney attempts to pull in the subject matter and actual pixels from the image <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. This can lead to unwanted elements, such as a hand from a reference image appearing in the generated output if the image weight is too high <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.
*   **Style Reference (Paperclip Icon)**: When an image is used as a style reference, MidJourney focuses on understanding and integrating the aesthetic qualities of the image, decoupling them from the subject matter <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. This is the primary method for [[exploring_style_references_in_ai_design | exploring style references]] and achieving a specific aesthetic without incorporating the original image's content <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

## Key Aesthetic Levers and Parameters
Achieving desired aesthetics involves balancing various "aesthetic levers":

### Text Prompt
While words are the "tip of the iceberg," they still play a role in guiding the visual output <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Specific descriptions like "a paper cutout illustration of a giraffe" can provide support to the style reference <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>.

### Style Weight (`--sw`)
This parameter determines how much influence a style reference has over the generation <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>. The default is 100, but it can be increased up to 1000 for a stronger influence <a class="yt-timestamp" data-t="00:17:39">[00:17:39]</a>.

### Aspect Ratio (`--ar`)
Setting the aspect ratio (e.g., `--ar 2:3` for a poster print) helps guide MidJourney to fill the space effectively for the intended output format <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.

### Personalization
MidJourney's personalization feature allows the model to learn a user's aesthetic preferences <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>. By regularly rating images in the "Personalize" tab, MidJourney learns preferred colors, lighting, general style (photographic vs. illustrative), and even subject matter <a class="yt-timestamp" data-t="00:30:13">[00:30:13]</a>. This fine-tunes the model to the user's specific "vibe" <a class="yt-timestamp" data-t="00:33:00">[00:33:00]</a>.

### Stylize (`--s`)
This parameter controls how much of the MidJourney model's default aesthetics (curated by the community) are applied to the text prompt <a class="yt-timestamp" data-t="00:31:22">[00:31:22]</a>. High stylize values can make images look "AI-screaming," while lower values or personalization lead to a more balanced or customized look <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>. Increasing the stylize level can increase the influence of personalization <a class="yt-timestamp" data-t="00:48:32">[00:48:32]</a>.

### Style Reference Codes (`--sref`)
These codes act as coordinates in a "multi-dimensional Style Space," directing the AI to a specific aesthetic location <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. Using these codes (e.g., by searching for "paper cutout" vibes in a [[using_midjourney_for_visual_inspiration_and_design | style reference explorer tool]]) allows for visual exploration and application of curated aesthetics <a class="yt-timestamp" data-t="00:39:05">[00:39:05]</a>. There are billions of possible `sref` codes, representing complex combinations of color, composition, lighting, texture, and pattern <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.

### Blending Multiple Styles
Users can combine multiple style references (images or `sref` codes) in a single prompt <a class="yt-timestamp" data-t="00:28:47">[00:28:47]</a>. Weights can be assigned to individual style references (e.g., `sref::2` for two parts of one style, `sref::1` for one part of another) to control their respective influences <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>. This allows for the creation of unique "style potions" or "aesthetic recipes" <a class="yt-timestamp" data-t="00:42:42">[00:42:42]</a> <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>.

### Negative Prompting (`--no`)
The `--no` parameter allows users to specify elements they want to exclude from the generation, such as `--no text` to prevent text from appearing in the image <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>.

### Variations (Subtle/Strong)
After an initial generation, users can create variations:
*   **Subtle variations** keep most details intact but introduce minor changes <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>.
*   **Strong variations** have more dramatic effects on composition, altering elements like subject location and size while maintaining the general vibe <a class="yt-timestamp" data-t="00:25:49">[00:25:49]</a>.

### Editor Feature
The editor allows for direct manipulation of generated images, such as painting out unwanted elements or adjusting compositions, and supports integration with new prompts to fill out areas (out-painting) <a class="yt-timestamp" data-t="00:26:29">[00:26:29]</a> <a class="yt-timestamp" data-t="00:50:47">[00:50:47]</a>.

## Workflow and Mindset
The key to mastering MidJourney is to move beyond a "slot machine game" approach to a more controlled and iterative process <a class="yt-timestamp" data-t="00:45:37">[00:45:37]</a>.
*   **Start Simple**: Begin with a basic subject and a style reference to observe how MidJourney interprets the style <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
*   **Iterate and Adjust**: Based on initial results, make guided decisions to adjust parameters like style weight or add supporting text prompts <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   **Balance and Harmony**: The goal is to find balance and harmony between all the available levers (style references, text prompts, parameters, personalization) <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.
*   **Visual Analysis**: Continuously analyze results to determine if they meet the desired outcome and what further adjustments might be needed <a class="yt-timestamp" data-t="00:42:04">[00:42:04]</a>.
*   **Organize Favorites**: Liking preferred images in the MidJourney library (via the heart icon or right-click) helps in quickly finding them later amidst many generations <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>.

MidJourney functions as a powerful discovery engine, allowing users to explore and refine ideas, build mood boards, and generate production-ready assets <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>. It offers immense creative control and functions as a new medium for blending complex aesthetics <a class="yt-timestamp" data-t="00:46:09">[00:46:09]</a> <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. The ability to "steal like an artist" by leveraging existing visual styles and combining them in new ways is a core strength of [[using_ai_design_tools_like_midjourney_and_chatgpt | AI design tools]] like MidJourney <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>.

## Future Applications
Beyond digital creation, there are plans to physically manifest AI-generated art through projects like a lab with robots painting, 3D printers, and editing stations to bring creations to life <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>. The ambition is to create "Moma-level" art that transcends its AI origin <a class="yt-timestamp" data-t="00:55:50">[00:55:50]</a>.