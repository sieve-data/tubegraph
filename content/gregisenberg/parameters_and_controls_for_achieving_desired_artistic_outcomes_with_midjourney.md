---
title: Parameters and controls for achieving desired artistic outcomes with Midjourney
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

[[AI Tools like Midjourney and Chat GPT | Midjourney]] is considered a new artistic medium, offering a different type of canvas and a unique way of problem-solving in art creation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It allows for the blending and balancing of entire aesthetics to achieve a desired harmony <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Beyond Text Prompting
Initially, [[AI Tools like Midjourney and Chat GPT | Midjourney]] heavily relied on word-based prompts <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. While words are still valuable, they represent "just the tip of the iceberg" <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. The true potential lies in using visuals to drive visuals, which can "explode out Aesthetics and style space into almost infinite directions" <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This approach reduces reliance on the base model's interpretation of style tokens, allowing users to "pave their own lane" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.

## The Midjourney Web App
For optimal use, it is recommended to transition from Discord to the [[AI Tools like Midjourney and Chat GPT | Midjourney]] web app ([midjourney.com](https://midjourney.com)) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Exploring and Inspiration
The web app's "Explore" tab showcases publicly available generations, serving as a vast library of inspiration <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Users can search for specific styles (e.g., "vintage poster") <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. If a particular vibe is appealing, the search icon can be used to find similar results based on subject matter and style <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

The "Explore" tab also allows users to:
*   "Use prompt": Copy the exact text prompt from a chosen image <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   "Use style": Import an image as a style reference <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   "Use as an image": Import an image as an image prompt <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### Privacy Considerations
For client work or sensitive projects, it's crucial to use the Pro Plan or above and activate "stealth mode" in the settings <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. This prevents assets from appearing in the public database <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

## Core Concepts: Image Prompts vs. Style References
Understanding the distinction between image prompts and style references is fundamental for achieving desired outcomes <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>:

*   **Image Prompt (Pict Icon)**: When an image is used as an image prompt, [[AI Tools like Midjourney and Chat GPT | Midjourney]] attempts to pull in the actual subject matter and elements (pixels) of that image <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. Increasing the image weight (`--iw`) will make [[AI Tools like Midjourney and Chat GPT | Midjourney]] integrate more of the image's literal content, potentially leading to "wonky" results if the goal is a specific style <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>.
*   **Style Reference (Paperclip Icon)**: When an image is set as a style reference, [[AI Tools like Midjourney and Chat GPT | Midjourney]] tries to understand and decouple the aesthetic from the subject matter <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. This means it will apply the overall look, feel, colors, and composition of the reference image without necessarily incorporating its specific objects <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. This is critical for [[using_style_references_and_personalization_in_midjourney | using style references and personalization in Midjourney]] effectively.

## Key Parameters and Aesthetic Levers

Achieving specific artistic outcomes involves balancing and harmonizing various "aesthetic levers" <a class="yt-timestamp" data-t="00:29:03">[00:29:03]</a>.

1.  **Style Weight (`--sw`)**: This parameter determines how much influence a style reference has over the generation <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>. The default is 100, but it can be increased up to 1000 for stronger influence <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.

2.  **Text Prompt Refinement**: While relying less on words, text prompts can still provide "assistance" to guide the style reference <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. Adding descriptive terms like "paper cutout illustration" <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a> can help refine the aesthetic direction.

3.  **Aspect Ratio (`--ar`)**: This parameter sets the image dimensions. For example, `--ar 2:3` can be used to generate a poster-like layout <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.

4.  **No Parameter (`--no`)**: This parameter tells [[AI Tools like Midjourney and Chat GPT | Midjourney]] what to remove from the generation <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>. For example, `--no text` can be used to eliminate unwanted text elements <a class="yt-timestamp" data-t="00:26:58">[00:26:58]</a>.

5.  **Personalization (`--p`)**: This is a powerful feature that fine-tunes the [[AI Tools like Midjourney and Chat GPT | Midjourney]] model to a user's specific aesthetic preferences <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>. It's developed by rating images in the "Personalize" tab, where the model learns preferences for colors, lighting, general style (photographic vs. illustrative), and even specific subjects <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>. Turning personalization on can dramatically alter the output, making images align more with individual taste <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>. This feature makes a "huge difference" <a class="yt-timestamp" data-t="00:34:23">[00:34:23]</a>.

6.  **Stylize (`--s`)**: This parameter controls how much of the [[AI Tools like Midjourney and Chat GPT | Midjourney]] model's curated default aesthetics (V6.1) are applied to the text prompt's interpretation <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.
    *   High stylize values (e.g., `--s 1000`) make the output look more like "Midjourney" or "screams AI" <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.
    *   The default (100) balances the text prompt with [[AI Tools like Midjourney and Chat GPT | Midjourney]] aesthetics <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
    *   When personalization is active, stylize controls the *influence* of that personalization <a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>.

7.  **Style Reference Codes (SRF)**: These codes act as "coordinates in this like multi-dimensional Style Space" <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>. Each code directs generations to a specific aesthetic universe, influencing color, composition, lighting, texture, and pattern <a class="yt-timestamp" data-t="00:40:17">[00:40:17]</a>. There are billions of possible SRF codes <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>, which can be found through tools like a style reference explorer <a class="yt-timestamp" data-t="00:36:51">[00:36:51]</a>. Users can blend multiple SRF codes to create unique "aesthetic recipes" or "style potions" <a class="yt-timestamp" data-t="00:40:42">[00:40:42]</a>.

8.  **Weighting Multiple Elements**: When blending multiple style references (or other elements), specific weights can be assigned using a double colon (`::`) followed by a number <a class="yt-timestamp" data-t="00:44:35">[00:44:35]</a>. For example, `sref1::2 sref2::1` would give twice the influence to the first style reference.

9.  **Permutation Prompts**: For testing different parameter values quickly, values can be enclosed in brackets `[]` and separated by commas <a class="yt-timestamp" data-t="00:49:20">[00:49:20]</a>. This allows running multiple variations in one go to visually compare outcomes <a class="yt-timestamp" data-t="00:49:33">[00:49:33]</a>.

## Workflow for [[creating_art_with_ai_and_blending_aesthetics_in_midjourney | Creating Art with AI and Blending Aesthetics]]
The overall process is about finding balance and harmony <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>:
1.  **Start Simple**: Begin with a basic subject and a style reference, then observe how [[AI Tools like Midjourney and Chat GPT | Midjourney]] interprets it <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
2.  **Iterate and Refine**: Based on the results, make guided decisions by adjusting parameters like style weight, adding descriptive text, or changing the aspect ratio <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
3.  **Use Variations**:
    *   **Subtle variations**: Keep most details intact while changing minor aspects <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>.
    *   **Strong variations**: Introduce more dramatic changes to composition while retaining the general vibe and subject matter <a class="yt-timestamp" data-t="00:25:46">[00:25:46]</a>.
4.  **Utilize the Editor**: The editor feature allows for outpainting (adding new elements) and inpainting (removing unwanted elements like text) from existing assets <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.
5.  **Organize with Favorites**: Liking favorite generations (using the heart icon or right-click) makes it significantly easier to find them later in the "Organize" tab <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.

## Conclusion
[[AI Tools like Midjourney and Chat GPT | Midjourney]] acts as a powerful "discovery engine" <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>, allowing users to explore aesthetics in depth <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. By understanding and manipulating its parameters, users gain significant creative control, moving beyond simple text prompts to build complex and unique aesthetic worlds <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. This control enables the creation of high-quality, distinctive art that can be personally enjoyed, used for branding, or shared as social assets <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. The ultimate goal is to physically manifest these digital creations, potentially through tools like robots for painting, 3D printers, and advanced editing stations <a class="yt-timestamp" data-t="00:59:47">[00:59:47]</a>.