---
title: Leveraging personalization and parameters in AI design
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

Midjourney is considered a new medium entirely, offering a different type of canvas and a different way of problem-solving in [[Potential of AI in Product Design | AI design]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. It allows users to blend and balance entire aesthetics with multiple layers and complexity to achieve desired results <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Once a "recipe" or specific aesthetic is found, it can be infinitely prompted <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Midjourney Web App

It is recommended to use the Midjourney web app (`midjourney.com`) instead of Discord for a better workflow <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The web app is open to everyone <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Privacy Considerations
If your account is on the standard plan or below, all generations are public by default in the "Explore" tab <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. For client work or proprietary imagery, it's crucial to be on the Pro Plan or above and activate "stealth mode" to ensure assets do not appear in the public database <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. Stealth mode can be toggled in the settings of the prompt bar <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.

## Benefits of Using Midjourney

Midjourney serves as a powerful [[Potential of AI in Product Design | AI design]] tool for various purposes:
*   **Inspiration and Ideation**: It's a great way to generate and develop ideas quickly, similar to building a mood board <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. Users have more control over the discovery process <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>.
*   **Production**: With features like the editor, users can manipulate existing assets, out-paint, and add new elements <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.
*   **Discovery Engine**: It helps explore aesthetics and go down "rabbit holes" of creative exploration <a class="yt-timestamp" data-t="00:12:30">[00:12:30]</a>.
*   **Creative Control**: Midjourney offers significant creative control over the artistic direction <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.
*   **Art Therapy**: Some users find it enjoyable and therapeutic, getting lost in the creative process <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.

## Key Concepts for Aesthetic Control

Midjourney offers various "levers" or parameters to guide and push aesthetics, allowing for balance and harmony in generations <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

### Style References
Images can be used as **style references** (indicated by a paperclip icon) to influence the aesthetic of a generation <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>. Midjourney attempts to decouple the aesthetic from the subject matter of the reference image <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.

### Image Prompts vs. Style References
*   **Image Prompt (default)**: Dragging an image in defaults it to an image prompt (pict icon). This tells Midjourney to pull in more of the subject matter and actual pixels of the image <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. This can lead to "wonky" results if the goal is only aesthetic influence <a class="yt-timestamp" data-t="00:21:10">[00:21:10]</a>.
*   **Style Reference**: Using the paperclip icon, this directs Midjourney to focus solely on the aesthetic qualities of the image, like colors, composition, lighting, texture, and pattern <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a> <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>.

### Parameters for Control
*   **Style Weight (`--sw`)**: This parameter determines how much influence a style reference has over the generation. The default is 100, but it can go up to 1000 for stronger influence <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
*   **Aspect Ratio (`--ar`)**: Allows users to set the output dimensions, useful for specific formats like posters <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   **No Parameter (`--no`)**: Instructs Midjourney to remove specific elements from the generation, such as `--no text` <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>.
*   **Stylize Parameter (`--s`)**: Determines how much of the curated Midjourney model's aesthetics (community-driven default) are applied to the text prompt. Higher values make images look more "AI" or like the default Midjourney style <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.

### [[Optimizing funnels with personalization and AI | Personalization]]
[[Optimizing funnels with personalization and AI | Personalization]] in Midjourney is achieved by rating images in the "Personalize" tab <a class="yt-timestamp" data-t="00:29:36">[00:29:36]</a>. By selecting preferred images, Midjourney learns user preferences regarding colors, lighting, general style (photographic vs. illustrative), and even certain subjects <a class="yt-timestamp" data-t="00:30:13">[00:30:13]</a>. This fine-tunes the model to the user's aesthetic preferences, providing a unique look that differs from the community-curated default <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>.

### Style Reference Codes (`sref`)
These codes act as "coordinates" in a multi-dimensional Style Space, directing the [[Potential of AI in Product Design | AI]] to a specific aesthetic location <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>. There are billions of `sref` codes, representing various combinations of color, composition, lighting, texture, and pattern <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a> <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>. Users can discover and curate these codes to build "aesthetic recipes" <a class="yt-timestamp" data-t="00:38:10">[00:38:10]</a>. Multiple `sref` codes can be blended in a single prompt to combine aesthetics <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>. Specific weights can be assigned to individual `sref` codes using `::` syntax (e.g., `sref1::2 sref2::1`) to control their influence <a class="yt-timestamp" data-t="00:44:45">[00:44:45]</a>.

### Permutation Prompts
This advanced technique uses brackets and commas `{} ,` to run multiple parameter values in one go, allowing for quick visual comparison of different results <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>.

### Editor Feature
The editor allows users to adjust image composition, change aspect ratios, resize elements, and specify new elements or styles for the image <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>.

## Cultivating a Workflow
There isn't one "right way" to use Midjourney due to its deep feature set and seemingly infinite workflows <a class="yt-timestamp" data-t="00:37:41">[00:37:41]</a>. The goal is to find a personal flow that fits one's vibe <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### Workflow Example
1.  **Start with a Subject and Medium**: Begin with a general concept (e.g., "giraffe") and optionally a medium (e.g., "painting," "illustration") <a class="yt-timestamp" data-t="00:04:32">[00:04:32]</a>.
2.  **Use Style References**: Introduce an image as a style reference to guide the aesthetic <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
3.  **Iterate and Interpret**: Observe how Midjourney interprets the style and make guided decisions for the next steps <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
4.  **Adjust Parameters**: Play with parameters like `--sw` to increase the style reference's influence or `--ar` for specific layouts <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
5.  **Refine Text Prompts**: Add supporting text to further guide the [[AI design]] towards the desired look (e.g., "paper cutout illustration") <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
6.  **Experiment with Variations**: Generate subtle or strong variations of existing images <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>.
7.  **Explore Style Reference Codes**: Utilize tools like a style reference explorer to find specific `sref` codes and blend them for unique aesthetics <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>.
8.  **Incorporate [[Optimizing funnels with personalization and AI | Personalization]]**: Turn on [[Optimizing funnels with personalization and AI | personalization]] and adjust the stylize parameter (`--s`) to infuse personal aesthetic preferences <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.
9.  **Balance and Harmony**: Continuously visually analyze results and adjust parameters to find the desired balance between text prompts, style references, and [[Optimizing funnels with personalization and AI | personalization]] <a class="yt-timestamp" data-t="00:29:21">[00:29:21]</a> <a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>.

> [!tip] Quick Tip: Liking Favorites
> Always "like" your favorite generations using the heart icon or right-click to easily find them later in your organized library, especially since each generation produces four images <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.

> [!tip] Keyboard Shortcut
> After running a prompt, pressing the "up arrow" on the keyboard automatically populates the last prompt in the prompt bar, saving time <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>.

## The Future of [[Potential of AI in Product Design | AI Design]]
The ability to generate art that is indistinguishable from traditional art by top Midjourney users demonstrates its power <a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>. The goal is to move beyond mere digital existence and physically manifest [[Potential of AI in Product Design | AI]]-generated art through labs equipped with robots for painting and music, 3D printers, and editing stations for image-to-video models <a class="yt-timestamp" data-t="00:59:47">[00:59:47]</a>. This represents a new way of blending and creating <a class="yt-timestamp" data-t="01:00:29">[01:00:29]</a>.