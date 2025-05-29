---
title: Midjourney AI Design Overview
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

Midjourney is described as an entirely new medium, a different type of canvas, and a distinct way of problem-solving in the design world <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>. It offers the ability to blend and balance entire aesthetics with multiple layers and complexities, aiming for a harmonious result that can be infinitely iterated upon once a "recipe" is found <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Why Use Midjourney?

Professionally, Midjourney serves as a significant inspiration tool, ideal for jamming out ideas and building mood boards, similar to platforms like Pinterest or Dribbble <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. However, it provides greater control over the creative process <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. It's beneficial for:
*   Coming up with ideas <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>
*   Putting together concepts <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>
*   Ideating and exploring <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>

The tool can also be used in production, especially with the newer editor feature, which allows users to out-paint or add new elements to existing assets <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. Beyond professional use, Midjourney is simply enjoyable, likened to "art therapy" where users can get lost in the creative flow <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>. It functions as a powerful discovery engine, enabling users to put an idea in and explore the aesthetic rabbit hole it creates <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

For skilled users, Midjourney can produce art that is indistinguishable from traditional art, capable of being featured in galleries or used as valuable [[ai_product_designer_reviews | design assets]] for websites or social media <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. It provides the most creative control, embodying a new medium for artistic expression <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

## Moving to the Midjourney Web App

Users are strongly encouraged to use the Midjourney web application at `midjourney.com` instead of Discord, which is described as a "hellish place to be" for working <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The web app is open to everyone <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Key Sections of the Web App
*   **Create Tab:** Where most of the prompting and creation takes place <a class="yt-timestamp" data-t="00:06:54">[00:06:54]</a>.
*   **Explore Tab:** Displays all publicly available generations, serving as a source of inspiration <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Users can search for specific styles (e.g., "vintage poster") and find similar results using an image search icon <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
    *   From the explore tab, users can "Use Prompt" to copy the text prompt or "Use Style" to bring an image in as a style reference <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
    *   All images in the Explore tab are created on Midjourney <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
*   **Stealth Mode:** For Pro Plan subscribers, enabling stealth mode in settings (via the gear icon in the prompt bar) prevents generated assets from appearing in the public database, which is important for client work or proprietary imagery <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

## Core Midjourney Features and Workflow

The core of Midjourney involves balancing various "levers" to guide the aesthetics of the generated images <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

### Prompting with Visuals
Initially, Midjourney relied heavily on words and parameters. However, recent advancements have introduced:
*   **Style Space:** A system that expands aesthetics into an infinite universe <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Style References:** Using images to drive visuals, allowing for an explosion of aesthetics and style space beyond semantic interpretation <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.
*   **Character References:** Not explicitly covered in detail, but mentioned as distinct from style references <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

#### Image Prompt vs. Style Reference
This is a critical distinction:
*   **Image Prompt (pict icon):** When an image is used as an image prompt, Midjourney tries to pull in the subject matter and actual pixels of that image <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Increasing the image weight (`--iw`) will make Midjourney prioritize incorporating elements from the source image, potentially leading to distorted results (e.g., a "hand giraffe") if the subject matter clashes with the text prompt <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>.
*   **Style Reference (paperclip icon):** When an image is used as a style reference, Midjourney analyzes the image to understand its core aesthetic qualities (e.g., color, composition, lighting, texture, pattern) and integrates those into the generation, decoupling aesthetics from subject matter <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. This is the preferred method for guiding stylistic direction.

#### Key Parameters and Concepts
*   **Style Weight (`--sw`):** Determines how much influence a style reference has over the generation. The default is 100, but it can go up to 1000 for stronger influence <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
*   **Aspect Ratio (`--ar`):** Changes the output image's proportions, useful for specific formats like posters (e.g., `--ar 2:3`) <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   **Variations (Subtle/Strong):** Available when refining a generated image.
    *   **Subtle:** Keeps most details intact while making minor changes <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>.
    *   **Strong:** Introduces more dramatic changes to composition, subject location, or size while maintaining the general vibe <a class="yt-timestamp" data-t="00:25:48">[00:25:48]</a>.
*   **Editor:** Allows users to modify parts of an image by painting out elements. Midjourney is often good at removing desired elements, but the `--no` parameter can be used in the prompt to explicitly tell Midjourney what to exclude (e.g., `--no text`) <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>.
*   **Organizing Favorites:** Users should "like" their favorite generations by clicking the heart icon or right-clicking. This makes them easily discoverable in the "Organize" tab by filtering for "liked" items, preventing loss amidst hundreds of generations <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.

### Personalization and Stylize
*   **Personalization:** Midjourney can be fine-tuned to a user's aesthetic preferences by rating images in the "Personalize" tab <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>. By selecting preferred images, Midjourney learns about desired colors, lighting, general style (photographic vs. illustrative), and even subject matter preferences. Rating about a thousand images significantly improves results <a class="yt-timestamp" data-t="00:30:05">[00:30:05]</a>.
*   **Stylize (`--s`):** This parameter controls how much of Midjourney's default, community-curated aesthetic is applied to the text prompt.
    *   Default is 100, balancing text prompt and Midjourney aesthetics <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.
    *   Higher values (e.g., 1000) make the image "scream AI" or look heavily like the default Midjourney style <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.
    *   Lower values or using `style raw` (which leans more photorealistic) can pull away from the heavy AI look <a class="yt-timestamp" data-t="00:52:08">[00:52:08]</a>.
    *   When personalization is active, the `stylize` parameter amplifies the user's *fine-tuned* aesthetic preferences, rather than the general community default <a class="yt-timestamp" data-t="00:33:12">[00:33:12]</a>.

### Style Reference Codes (`sref`)
These are unique codes (e.g., `sref XXXXXXXXX`) that act as "coordinates" in a multi-dimensional style space <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>. When an `sref` code is added to a prompt, anything generated will be influenced by the aesthetics of that specific "universe" <a class="yt-timestamp" data-t="00:37:52">[00:37:52]</a>. There are billions of possible `sref` codes <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.

*   **Blending Styles:** Multiple `sref` codes can be combined in a single prompt to blend different styles like "paints on a palette" <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a>. Each `sref` represents a complex combination of color, composition, lighting, texture, and pattern <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>.
*   **Weighted Blending:** Users can assign weights to individual `sref` codes using double colons (e.g., `::2`) to control their relative influence in a blend <a class="yt-timestamp" data-t="00:44:37">[00:44:37]</a>.
*   **Permutation Prompts:** Using brackets `[]` and commas allows users to test multiple parameter values or style combinations in a single go, quickly seeing visual variations (e.g., `--sw [50, 100, 500]`) <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>.

## Beyond Digital: Physical Manifestation
There's a growing movement to physically manifest AI-generated art. A lab is being built in Red Hook, in partnership with Pioneer Works, to provide tools and equipment (robots for painting, 3D printers, plotter printers, editing stations) for users to bring their digital creations to life, including translating images into video models <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>. This initiative aims to get AI-generated art, such as a "funky giraffe" image, into galleries like MoMA <a class="yt-timestamp" data-t="01:00:59">[01:00:59]</a>. This highlights the [[leveraging_ai_for_startup_product_design_and_development | potential of AI for creative endeavors]] and the ongoing efforts in [[improving_ai_designs_and_interfaces | improving AI designs and interfaces]].

## Resources
*   **Midjourney Web App:** `midjourney.com` <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>
*   **Style Reference Explorer:** A tool with over 40,000 images and 15,000 style reference codes (`sref`) for visual exploration of aesthetics <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>.
*   **Maven Course:** A deeper course on Midjourney and creative AI tools <a class="yt-timestamp" data-t="01:01:55">[01:01:55]</a>.
*   **Twitter:** Nick St. Pierre's profile is a source of information and updates <a class="yt-timestamp" data-t="01:01:49">[01:01:49]</a>.

Midjourney is constantly [[improving_ai_designs_and_interfaces | evolving]], offering a new way of problem-solving and exploring aesthetics by blending and balancing various controls <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. This shift from relying solely on text prompts to [[designing_with_ai_prompt_clarity | leveraging visuals]] allows for far greater creative control and exploration within the "Style Space" <a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a>.