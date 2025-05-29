---
title: Visual vs textbased prompts in AI design
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

Midjourney is described as an entirely new medium, offering a different type of canvas and a unique approach to problem-solving in design <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. It allows users to blend and balance entire aesthetics with layers and complexity to achieve desired visual harmony <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Once a successful "recipe" is found, it can be infinitely prompted into <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Evolution of Prompting in Midjourney

Initially, Midjourney primarily relied on text-based prompts, using words and parameters to describe every detail <a class="yt-timestamp" data-t="01:55:00">[01:55:00]</a>. This approach, while still valid, is considered just the "tip of the iceberg" <a class="yt-timestamp" data-t="01:07:00">[01:07:00]</a>. The base model's interpretation of "style tokens" through semantics can be limiting <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>, confining visuals to a "semantic box" <a class="yt-timestamp" data-t="01:23:00">[01:23:00]</a>.

In recent months, Midjourney has introduced new features that "explode aesthetics" and style into seemingly infinite directions, offering more creative control than relying solely on text <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>.

### Visual Prompting

The key to unlocking greater creative control in Midjourney is [[using_modular_and_reusable_prompts_in_ai_coding | using visuals to drive visuals]] <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This allows users to move beyond the limitations of purely semantic descriptions <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>.

#### Style References

Style references are images used to inform the aesthetic of the generated output <a class="yt-timestamp" data-t="02:22:00">[02:22:00]</a>. When an image is used as a style reference (indicated by a paperclip icon), Midjourney attempts to understand and integrate the core aesthetic elements of that image into the new generation, largely decoupling the aesthetic from the original subject matter <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>.

*   **Style Weight (`--sw`)**: This parameter controls how much influence the style reference has over the generation <a class="yt-timestamp" data-t="01:17:18">[01:17:18]</a>. The default is 100, but it can go up to 1000 for stronger influence <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>.
*   **Blending Styles**: Multiple style references can be used in a single prompt, allowing Midjourney to blend their unique flares <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. Users can specify the weight of each style reference using a double colon (e.g., `srf_code1::2 srf_code2::1`) to dictate the proportional influence <a class="yt-timestamp" data-t="04:47:00">[04:47:00]</a>.
*   **Style Reference (SRF) Codes**: These are unique codes (e.g., `SRE` followed by numbers) that act as coordinates in a multi-dimensional "Style Space" <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. They direct the AI to a specific aesthetic location, influencing anything prompted thereafter <a class="yt-timestamp" data-t="03:37:00">[03:37:00]</a>. There are billions of these codes, and users can find, curate, and mix them to build "aesthetic recipes" <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. Tools like the "Style Reference Explorer" help visually explore these codes <a class="yt-timestamp" data-t="03:57:00">[03:57:00]</a>.

#### Image Prompts

When an image is used as an image prompt (indicated by a pict icon), Midjourney attempts to pull in the actual subject matter and elements, or "pixels," of the source image <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>. This is distinct from a style reference, which focuses on the aesthetic <a class="yt-timestamp" data-t="02:08:00">[02:08:00]</a>. If an image weight is too high in an image prompt, it can lead to distorted results (e.g., a "hand giraffe") <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

### Personalization

Midjourney offers a "Personalize" feature that fine-tunes the model to a user's aesthetic preferences <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. This is achieved by rating images in the "Personalized" tab <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>. The more images rated, the more the model learns about preferences such as color, lighting, general style (photographic vs. illustrative), and even preferred subjects <a class="yt-timestamp" data-t="03:13:00">[03:13:00]</a>. This significantly alters the aesthetic of generated images <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>.

*   **Stylize (`--s`)**: This parameter controls how much of Midjourney's community-curated aesthetic is applied to the text prompt's interpretation <a class="yt-timestamp" data-t="03:17:00">[03:17:00]</a>. High stylize values (e.g., 1000) result in a very "AI" look <a class="yt-timestamp" data-t="03:19:00">[03:19:00]</a>, while a default of 100 offers a more balanced look <a class="yt-timestamp" data-t="03:20:00">[03:20:00]</a>. Personalization essentially replaces this default aesthetic with the user's fine-tuned preferences <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>. Increasing the stylize parameter when personalization is active will amplify the user's unique aesthetic <a class="yt-timestamp" data-t="04:31:00">[04:31:00]</a>.

## Midjourney Workflow and Tips

### Using the Web App

*   **Midjourney.com**: Users should migrate from Discord to the Midjourney web app for a more efficient workflow <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.
*   **Create Tab**: This is the primary area for generating images <a class="yt-timestamp" data-t="06:54:00">[06:54:00]</a>.
*   **Explore Tab**: A source of inspiration where all publicly available generations are displayed <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>. Users can search for specific styles (e.g., "vintage poster") <a class="yt-timestamp" data-t="07:31:00">[07:31:00]</a>.
    *   **Image Search**: Clicking the search icon on an image in the explore tab finds similar results <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>.
    *   **Use Prompt/Style/Image**: These options allow users to quickly import elements from existing generations into their own prompts <a class="yt-timestamp" data-t="08:44:00">[08:44:00]</a>.
*   **Stealth Mode**: For professional or client work, users on a Pro Plan or higher should enable stealth mode in settings to prevent their generations from appearing publicly <a class="yt-timestamp" data-t="10:26:00">[10:26:00]</a>.

### Iterative Design Process

The "name of the game" in Midjourney is balance and harmony among various "aesthetic levers" <a class="yt-timestamp" data-t="01:28:29">[01:28:29]</a>.

1.  **Start Simple**: Begin with a basic subject and a style reference, without specifying medium or lighting <a class="yt-timestamp" data-t="01:12:00">[01:12:00]</a>. This helps interpret how Midjourney handles the style reference <a class="yt-timestamp" data-t="01:14:00">[01:14:00]</a>.
2.  **Refine with Parameters**:
    *   Adjust `style weight` to control the influence of the style reference <a class="yt-timestamp" data-t="01:17:00">[01:17:00]</a>.
    *   Use `aspect ratio` (`--ar`) to specify desired dimensions, like for a poster print <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>.
    *   The `no` parameter can be used to explicitly tell Midjourney what to remove from the generation (e.g., `--no text`) <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
3.  **Enhance with Text Prompts**: Add descriptive text to assist the visual style, guiding the aesthetic <a class="yt-timestamp" data-t="01:25:00">[01:25:00]</a>.
4.  **Variations**:
    *   **Subtle Variations**: Keep most details intact, making minor changes <a class="yt-timestamp" data-t="02:35:00">[02:35:00]</a>.
    *   **Strong Variations**: Introduce more dramatic changes to composition while retaining the general vibe and subject matter <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>.
5.  **Editor Feature**: Allows for outpainting (adding new elements) and masking out unwanted elements like text <a class="yt-timestamp" data-t="02:58:00">[02:58:00]</a>.
6.  **Organize Favorites**: Liking preferred generations helps locate them easily in the library later <a class="yt-timestamp" data-t="02:51:00">[02:51:00]</a>.
7.  **Permutation Prompts**: Use brackets and commas to test multiple parameter values at once (e.g., `--sw 50,100,200`) to quickly assess which level works best <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a>.

## Benefits of Midjourney for Design

Midjourney serves as a powerful [[planning_and_visualizing_with_ai_tools | discovery engine]] and [[using_ai_in_graphic_design | inspiration tool]] <a class="yt-timestamp" data-t="11:16:00">[11:16:00]</a>. It's excellent for:
*   Generating ideas and concepts <a class="yt-timestamp" data-t="11:47:00">[11:47:00]</a>.
*   Building mood boards with greater control than traditional methods <a class="yt-timestamp" data-t="11:26:00">[11:26:00]</a>.
*   Production, especially with features like the editor for manipulating existing assets <a class="yt-timestamp" data-t="11:52:00">[11:52:00]</a>.
*   A form of "art therapy," allowing users to get lost in the creative process <a class="yt-timestamp" data-t="12:14:00">[12:14:00]</a>.
*   Enabling users to create "Moma-level" art and transform ideas into tangible design assets <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>.

The ability to blend and balance various aesthetic levers—including style references, text prompts, parameters, and personalization—offers a unique level of creative control and allows for the exploration of complex, multi-layered aesthetics <a class="yt-timestamp" data-t="04:16:00">[04:16:00]</a>. This approach moves beyond the "slot machine game" of random text prompting, enabling more guided and intentional creative exploration <a class="yt-timestamp" data-t="04:36:00">[04:36:00]</a>.