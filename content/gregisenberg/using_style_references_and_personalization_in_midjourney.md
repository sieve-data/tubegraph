---
title: Using style references and personalization in Midjourney
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

Midjourney is considered a new artistic medium, offering a different type of canvas and problem-solving approach <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It allows users to blend and balance entire aesthetics, finding harmony to achieve desired results <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>. Once a "recipe" is discovered, it can be infinitely prompted <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Moving Beyond Text Prompts

While words are still valuable, they are merely the tip of the iceberg in Midjourney <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. Using visuals to drive visuals, as opposed to semantics, allows for the exploration of aesthetics and style space in almost infinite directions <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This means less reliance on the base model's interpretation of style tokens <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.

Historically, Midjourney primarily relied on structuring text prompts and detailing every aspect <a class="yt-timestamp" data-t="02:14:00">[02:14:00]</a>. Images could be used as prompts, but they often pulled subject matter and elements, not just style <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>. However, in recent months, Midjourney has introduced concepts like [[exploring_midjourneys_tools_and_features | Style Space]], [[exploring_midjourneys_tools_and_features | style references]], and [[exploring_midjourneys_tools_and_features | character references]], which "explodes aesthetics out into this infinite universe" <a class="yt-timestamp" data-t="02:19:00">[02:19:00]</a>. This shift makes it more enjoyable to play on a visual canvas <a class="yt-timestamp" data-t="02:36:00">[02:36:00]</a>.

There is no single "right way" to use Midjourney; its deep feature set allows for seemingly infinite workflows <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

## Midjourney Web App and Inspiration

For an optimized experience, it is highly recommended to use the Midjourney web app at midjourney.com instead of Discord <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>. The "Create" tab is where most prompting takes place <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>.

The "Explore" tab in the web app showcases publicly available generations, serving as a vast library of inspiration <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>. Users can search for terms like "vintage poster" to find styles <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>. If a particular vibe is appealing, clicking the search icon next to an image performs an image search, providing similar results in terms of subject matter and style <a class="yt-timestamp" data-t="07:46:00">[07:46:49]</a>.

Within the "Explore" tab, users can:
*   "Like" images for easier organization later <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.
*   Use the exact prompt ("Use Prompt") <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.
*   Use the image as a [[exploring_midjourneys_tools_and_features | style reference]] ("Use Style") <a class="yt-timestamp" data-t="08:48:00">[08:48:00]</a>.
*   Use the image as an image prompt ("Use Image") <a class="yt-timestamp" data-t="09:00:00">[09:00:00]</a>.

### Stealth Mode
For client work or when using proprietary imagery, it's crucial to use the Pro Plan or above and enable "stealth mode" in the settings <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>. This prevents creations from appearing in the public database <a class="yt-timestamp" data-t="10:36:00">[10:36:00]</a>.

## Why Use Midjourney?

Midjourney is a powerful tool for:
*   **Inspiration**: It acts as a discovery engine, allowing users to jam out ideas and build mood boards with more control than traditional image searches <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>.
*   **Ideation and Exploration**: Great for coming up with concepts and ideating <a class="yt-timestamp" data-t="11:47:00">[11:47:00]</a>.
*   **Production**: It can be used in production, especially with the new editor feature that allows outpainting and adding elements to existing assets <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.
*   **Art Therapy/Fun**: Many users find it enjoyable and a form of art therapy <a class="yt-timestamp" data-t="12:14:00">[12:14:00]</a>.

The ability to create high-quality art that is indistinguishable from human-made work allows for the transformation of ideas into living, breathing design assets for personal use, websites, or social media <a class="yt-timestamp" data-t="12:51:00">[12:51:00]</a>. It offers immense creative control <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>.

## Image Prompts vs. Style References

It's critical to understand the distinction between an image prompt and a style reference:
*   **Image Prompt**: When an image is dragged into the prompt bar, it defaults to an image prompt (pictogram icon) <a class="yt-timestamp" data-t="14:20:00">[14:20:00]</a>. This attempts to pull in the subject matter and actual pixels of the image <a class="yt-timestamp" data-t="20:00:00">[20:00:00]</a>. Increasing the image weight (`--iw`) will lead to Midjourney trying to pull more literal elements from the image <a class="yt-timestamp" data-t="20:45:00">[20:45:00]</a>.
*   **Style Reference**: To use an image as a style reference, select the paperclip icon <a class="yt-timestamp" data-t="14:35:00">[14:35:00]</a>. Midjourney will analyze the image to understand its aesthetic qualities (colors, composition, lighting, texture, pattern) while decoupling it from the subject matter <a class="yt-timestamp" data-t="19:41:00">[19:41:00]</a>. These aesthetic elements are then integrated into the new generation <a class="yt-timestamp" data-t="16:00:00">[16:00:00]</a>.

### Style Weight Parameter (`--sw`)
The `--sw` parameter determines how much influence a style reference has on the generation <a class="yt-timestamp" data-t="17:18:00">[17:18:00]</a>. The default is 100, but it can go up to 1000. A higher style weight makes the output more likely to resemble the style reference <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>.

## Personalization

Midjourney offers a "personalization" feature that fine-tunes the model to your aesthetic preferences <a class="yt-timestamp" data-t="29:36:00">[29:36:00]</a>.
*   **How to Enable**: Go to the "Personalize" tab and click "Start Teaching" <a class="yt-timestamp" data-t="29:45:00">[29:45:00]</a>. Simply select your favorite image from pairs presented, or skip if neither is liked <a class="yt-timestamp" data-t="29:51:00">[29:51:00]</a>. The more images rated, the more Midjourney learns about your preferred colors, lighting, general style (photographic vs. illustrative), and even subject matter <a class="yt-timestamp" data-t="30:10:00">[30:10:00]</a>. Rating a thousand images can significantly improve results <a class="yt-timestamp" data-t="30:41:00">[30:41:00]</a>.
*   **Impact**: When personalization is turned on, the model generates images based on your fine-tuned aesthetic rather than the community-curated Midjourney default <a class="yt-timestamp" data-t="32:41:00">[32:41:00]</a>. This can lead to a "totally different universe" of output <a class="yt-timestamp" data-t="33:32:00">[33:32:00]</a>. It helps to avoid the "classic Midjourney" look <a class="yt-timestamp" data-t="34:01:00">[34:01:00]</a>.

### Stylize Parameter (`--s`)
The `--s` parameter controls how much of the Midjourney model's curated aesthetics are applied to your text prompt <a class="yt-timestamp" data-t="31:20:00">[31:20:00]</a>.
*   **High stylize values** (e.g., `--s 1000`) will make images look more like the default Midjourney style, often described as "screams AI" <a class="yt-timestamp" data-t="32:12:00">[32:12:00]</a>.
*   **Lower stylize values** (default is 100) balance the text prompt with Midjourney aesthetics, offering more creative leeway <a class="yt-timestamp" data-t="32:00:00">[32:00:00]</a>.
*   With personalization, the `--s` parameter increases the influence of *your* aesthetic preferences <a class="yt-timestamp" data-t="48:34:00">[48:34:00]</a>.

## Style Reference Codes (SRF)

SRF codes are coordinates in a multi-dimensional [[exploring_midjourneys_tools_and_features | Style Space]] that direct the generation to a specific aesthetic location <a class="yt-timestamp" data-t="37:31:00">[37:31:00]</a>.
*   They are like a "seed" that fixes a point in style space <a class="yt-timestamp" data-t="37:51:00">[37:51:00]</a>.
*   There are billions of possible SRF codes, and users are actively "mining" and curating the best ones into lists <a class="yt-timestamp" data-t="38:01:00">[38:01:00]</a>.
*   SRF codes represent complex aesthetic qualities like color, composition, lighting, texture, and pattern <a class="yt-timestamp" data-t="40:19:00">[40:19:00]</a>.
*   Users can blend multiple SRF codes, similar to mixing paints on a palette, to create "style potions" <a class="yt-timestamp" data-t="40:02:00">[40:02:00]</a>. This is where "aesthetic recipes" are built <a class="yt-timestamp" data-t="38:19:00">[38:19:00]</a>.
*   SRF codes are added to a prompt using the syntax `sref random_number` <a class="yt-timestamp" data-t="37:28:00">[37:28:00]</a>. Multiple SRF codes can be used, separated by a space, and their relative influence can be weighted using `::` (e.g., `sref code1::2 sref code2::1` for two parts of code1 and one part of code2) <a class="yt-timestamp" data-t="44:35:00">[44:35:00]</a>.

## Balancing Aesthetic Levers

The core of effective Midjourney use lies in balancing and finding harmony between various "aesthetic levers" <a class="yt-timestamp" data-t="28:29:00">[28:29:00]</a>:
1.  **Style References (Images or SRF Codes)**: Guide the overall visual style <a class="yt-timestamp" data-t="29:06:00">[29:06:00]</a>.
2.  **Text Prompt**: Defines the subject matter and specific details (e.g., "paper cutout illustration") <a class="yt-timestamp" data-t="29:11:00">[29:11:00]</a>.
3.  **Parameters**:
    *   `--sw` (Style Weight): Controls the influence of style references <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>.
    *   `--s` (Stylize): Controls the influence of the model's default aesthetics or your personalization <a class="yt-timestamp" data-t="31:17:00">[31:17:17]</a>.
    *   `--ar` (Aspect Ratio): Defines the output image dimensions <a class="yt-timestamp" data-t="18:57:00">[18:57:00]</a>.
    *   `--no`: Excludes elements (e.g., `--no text`) <a class="yt-timestamp" data-t="26:52:00">[26:52:00]</a>.
4.  **Personalization**: Fine-tunes the model to your unique preferences <a class="yt-timestamp" data-t="29:36:00">[29:36:00]</a>.

The goal is to visually analyze results and make guided decisions on how to adjust these levers to push the aesthetics in desired directions <a class="yt-timestamp" data-t="16:36:00">[16:36:00]</a>. This process moves beyond a "slot machine game" to a more controlled artistic creation <a class="yt-timestamp" data-t="45:24:00">[45:24:00]</a>.

## Practical Workflow Example: Creating a Stylized Giraffe

Starting with an image (e.g., a 1995 Tokyo Trade Fair poster) as a style reference, the process unfolds:

1.  **Initial Prompt**: Start with a simple subject (e.g., "a giraffe") and the chosen style reference <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>. This helps interpret how Midjourney applies the style <a class="yt-timestamp" data-t="16:12:00">[16:12:00]</a>.
2.  **Adjust Style Weight**: If the results are too photorealistic, increase the style weight (`--sw 1000`) to emphasize the style reference's influence <a class="yt-timestamp" data-t="17:18:00">[17:18:00]</a>.
3.  **Refine Text Prompt**: Add descriptive terms to the text prompt for assistance (e.g., "a paper cutout illustration of a giraffe") <a class="yt-timestamp" data-t="18:10:00">[18:10:00]</a>. This aids in achieving the desired medium <a class="yt-timestamp" data-t="18:43:00">[18:43:00]</a>.
4.  **Aspect Ratio**: Adjust the aspect ratio (`--ar`) for the intended output (e.g., `--ar 2:3` for a poster) <a class="yt-timestamp" data-t="18:57:00">[18:57:00]</a>.
5.  **Explore SRF Codes**: Replace or combine image style references with SRF codes, searching for specific aesthetics like "paper cutout" or "glazed ceramic" in tools like a style reference explorer <a class="yt-timestamp" data-t="38:50:00">[38:50:00]</a>. This allows for visually exploring and blending unique aesthetic universes <a class="yt-timestamp" data-t="39:05:00">[39:05:00]</a>.
6.  **Incorporate Personalization**: Add your personalized aesthetic by enabling the feature <a class="yt-timestamp" data-t="48:00:00">[48:00:00]</a>.
7.  **Iterate with Parameters**: Use permutation prompts (e.g., `{100,200,500}`) to test different parameter values (like `--sw`) simultaneously, quickly seeing how different levels affect the output <a class="yt-timestamp" data-t="49:17:00">[49:17:00]</a>.
8.  **Refine and Post-Process**: Utilize the editor feature to remove unwanted elements (e.g., text) or adjust composition <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>.

This iterative process, constantly balancing the various levers, helps achieve unique and high-quality artistic outcomes that can be considered museum-worthy <a class="yt-timestamp" data-t="55:56:00">[55:56:00]</a>.

## Benefits and Future of Midjourney

Midjourney enables users to "steal like an artist" by blending existing aesthetics into new creations <a class="yt-timestamp" data-t="46:01:00">[46:01:00]</a>. It's a new medium where entire aesthetics, with their layers and complexity, can be blended and balanced <a class="yt-timestamp" data-t="46:09:00">[46:09:00]</a>. This level of control over aesthetic direction goes beyond the limitations of text interpretation alone <a class="yt-timestamp" data-t="46:46:00">[46:46:00]</a>.

The future of AI art involves not just digital creation but also [[practical_applications_and_workflows_in_midjourney | physically manifesting latent space]] <a class="yt-timestamp" data-t="59:47:00">[59:47:00]</a>. This includes using robots to paint, play music, and employing 3D printers, plotter printers, and editing stations to bring digital creations to life <a class="yt-timestamp" data-t="01:00:13">[01:00:13]</a>.