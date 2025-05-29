---
title: Using MidJourney for visual inspiration and design
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

[[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] is described as an entirely new medium, a different type of canvas and a different way of problem-solving [00:00:01]. It allows users to blend and balance entire aesthetics with complex layers to find harmony in their creations [00:00:10]. Once a desired "recipe" is found, it can be infinitely prompted [00:00:24].

## Why Use MidJourney?
[[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] serves multiple purposes for designers and artists:
*   **Inspiration Tool** It's excellent for generating ideas and creating mood boards, similar to how one might use Pinterest or Google Image Search, but with more control [00:11:16].
*   **Ideation and Exploration** It helps in putting together concepts, ideating, and exploring various design possibilities [00:11:47].
*   **Production** It's a powerful tool for production, especially with features like the editor that allow outpainting and adding new elements to existing assets [00:11:52].
*   **Art Therapy** Many people find it enjoyable and use it as a form of art therapy, getting lost in the creative process [00:12:14].
*   **Discovery Engine** It acts as a discovery engine, allowing users to input an idea, see what comes of it, and then go down a rabbit hole of aesthetic exploration [00:12:27].
*   **Creative Control** It offers extensive creative control, allowing users to take an idea and turn it into a living, breathing design asset [00:13:36].

## Getting Started: The Web App and Basic Exploration

### Transition from Discord
A key tip for new users is to move from Discord to the [[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] web app at midjourney.com, as it is a more efficient and user-friendly environment [00:06:36].

### Explore Tab for Inspiration
The "Explore" tab on midjourney.com is a valuable resource for finding inspiration [00:07:05]. It displays all publicly available generations [00:07:09].
*   **Search for Styles:** Users can search for specific themes like "vintage poster" to find inspiring images [00:07:31].
*   **Image Search:** If a particular style is appealing, clicking the search icon next to an image will return similar results in terms of subject matter and style [00:07:46].
*   **Prompt Reuse:** Users can choose to "use prompt" to re-add the exact text prompt to their prompt bar [00:08:41] or "use style" to bring the image in as a style reference [00:08:50].
*   **Private Prompting:** For client work or proprietary imagery, it's crucial to be on the Pro Plan or above and activate "stealth mode" in the settings to prevent assets from appearing in the public database [00:10:26].

## Mastering Aesthetic Control

[[the_process_of_blending_aesthetics_and_styles_in_midjourney | MidJourney's] creative process involves balancing various "aesthetic levers" to guide the output [00:28:29].

### Image Prompts vs. Style References
Understanding the distinction between image prompts and style references is fundamental:
*   **Image Prompt:** When an image is added as an "image prompt" (default), [[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] attempts to pull in the subject matter and actual pixels of the image [00:20:00]. Upping the "image weight" (e.g., `--iw`) makes the image more influential, potentially leading to distorted results where the subject of the reference image mixes with the desired subject (e.g., a "hand giraffe") [00:20:45].
*   **Style Reference (Paperclip Icon):** Using an image as a "style reference" (indicated by a paperclip icon) tells [[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] to analyze the aesthetic qualities of the image, decoupling them from the subject matter [00:14:35]. This allows the AI to integrate the style elements (colors, composition, lighting, texture, pattern) into new generations [00:19:41].

### Key Parameters

*   **Style Weight (`--sw`):** This parameter determines how much influence a style reference has on the generation [00:17:18]. The default is 100, but it can go up to 1000 for stronger influence [00:17:36].
*   **Aspect Ratio (`--ar`):** This parameter allows users to set the width-to-height ratio of the image, useful for specific layouts like posters (e.g., `--ar 2:3`) [00:18:57].
*   **Stylize (`--s`):** This parameter controls how much of the default [[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] model's curated aesthetics are applied to the text prompt [00:31:20]. High stylize values (e.g., `--s 1000`) tend to produce images that "scream AI," while lower values (default is 100) offer more creative leeway [00:31:40].

### Personalization: Training MidJourney to Your Taste
[[inspiration_and_iteration_in_design | Personalization]] allows [[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] to learn a user's aesthetic preferences by having them rate images in the "Personalized" tab [00:29:37].
*   **How it Works:** Users select their favorite image from a set, and [[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] gradually learns preferences for colors, lighting, general style (photographic vs. illustrative), and even subject matter [00:30:05].
*   **Benefits:** Rating thousands of images significantly improves the aesthetic output, fine-tuning the model to the user's specific taste [00:30:30]. This can drastically change the resulting images from the community-curated default to a personalized style [00:32:41]. Personalization can also be blended with others' personalization [00:34:58].

### Style Reference (SRF) Codes: Navigating the Style Space
SRF codes are like "coordinates" in a multi-dimensional style space that direct [[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] to a specific aesthetic location [00:37:31].
*   **Usage:** Instead of using an image as a style reference, users can copy and paste an SRF code into their prompt [00:38:35].
*   **Exploration:** Tools like a "style reference explorer" allow users to visually search and find SRF codes based on style, vibe, or theme [00:39:01].
*   **Complexity:** SRF codes represent a vast array of elements including color, composition, lighting, texture, and pattern [00:40:19].

### Blending Styles: Creating Unique Amalgamations
[[the_process_of_blending_aesthetics_and_styles_in_midjourney | MidJourney]] allows for the blending of multiple style references (images or SRF codes) by including them in the prompt [00:28:47].
*   **Weighting Blends:** Users can assign different weights to individual style references within a blend using a double colon syntax (e.g., `sref1::2 sref2::1`) to indicate how much influence each style should have [00:44:35].
*   **Iterative Refinement:** The process involves visually analyzing results, deciding what works, and incrementally adding or adjusting elements and parameters to achieve a desired outcome [00:42:02]. This helps move away from the "slot machine game" of random prompting towards a more guided and intentional creative process [00:45:12].

## Refining Your Creations: The Editor
The [[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] editor allows for post-generation refinement [00:26:28].
*   **Outpainting/Inpainting:** Users can paint out unwanted elements (like text) or expand the canvas to add new elements into the image [00:26:32].
*   **No Parameter (`--no`):** Within the editor or a prompt, users can use the `--no` parameter to tell [[using_ai_design_tools_like_midjourney_and_chatgpt | MidJourney]] what elements to remove from the generation (e.g., `--no text`) [00:26:52].

## Beyond the Digital Canvas: Physical Manifestation
There's an initiative to physically manifest latent space creations by building a lab in Red Hook, in partnership with Pioneer Works [00:59:47]. This space aims to teach deep use of creative AI tools and provide equipment (robots for painting and music, 3D printers, plotter printers, editing stations) to bring digital creations to life [01:00:03].

## Practical Tips

*   **Like Your Favorites:** To easily find desired images later, consistently "like" favorite generations using the heart icon. This allows for quick filtering in the "Organize" tab [00:27:19].
*   **Up Arrow Shortcut:** After running a prompt, hitting the up arrow key on the keyboard will automatically populate the prompt bar with the last command, saving time [00:36:13].
*   **Permutation Prompts:** Use brackets and commas (e.g., `[50, 100, 200]`) with parameters like style weight to run multiple variations in one go, allowing for quick visual comparison of different values [00:49:15].
*   **Curate Style Reference Books:** Users are beginning to create and share their own curated style reference books, offering specific looks for different prompt types [00:36:39].

> "It really does bring new meaning to the expression 'steal like an artist'." <a class="yt-timestamp" data-t="00:46:01">[00:46:01]</a>
> "You have not just paint but you have like entire aesthetics that have all of these layers and this complexity and you're blending them and you're balancing them and you're finding this harmony in between to get somewhere that you really love and once you get that once you find that little recipe you can infinitely prompt into it." <a class="yt-timestamp" data-t="00:46:18">[00:46:18]</a>
> "Visuals are much more complex... A picture's worth a thousand words." <a class="yt-timestamp" data-t="00:47:08">[00:47:08]</a>