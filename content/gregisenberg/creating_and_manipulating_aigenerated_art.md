---
title: Creating and manipulating AIgenerated art
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

Midjourney is described as an entirely new medium, a different type of canvas and a different way of problem-solving in art creation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It allows users to blend and balance entire aesthetics with multiple layers and complexities to achieve desired results <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Once a "recipe" or harmonious combination is found, it can be infinitely prompted <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Key Principles of Midjourney

The core principle behind effective use of Midjourney is to leverage visuals to generate other visuals, rather than solely relying on semantics (words) <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This approach allows for the expansion of aesthetics and style into "infinite directions," reducing reliance on the base model's interpretation of style tokens <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. The goal is to find balance and harmony among the various levers and parameters available <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

## Evolution of Midjourney Features

Initially, Midjourney primarily relied on words and parameters for prompting <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>. Image prompts existed but mainly pulled subject matter and elements, often not the desired outcome <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. In recent months, Midjourney has introduced "Style Space," style references, and character references, which allow for a more visual and expansive exploration of aesthetics <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Getting Started with Midjourney

### Using the Web Application

It is recommended to use the Midjourney web app (midjourney.com) instead of Discord for a better workflow <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The web app is open to everyone <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.

### Finding Inspiration

*   **External Sources:** Websites like Reddit and Pinterest, or even Google Image Search, are good places to find existing art for inspiration <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Midjourney Explore Tab:** The explore tab within Midjourney (midjourney.com/explore) showcases publicly available generations <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Users can search for styles (e.g., "vintage poster") and find similar results using the search icon on an image <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Prompt Reuse:** From the explore tab, users can:
    *   "Use Prompt": This will copy the text prompt into the creation bar <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
    *   "Use Style": This will bring the image in as a style reference (indicated by a paperclip icon) <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
    *   "Use Image": This functions differently from a style reference, pulling in subject matter and pixels rather than just the aesthetic <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>.

### Stealth Mode

For client work or when using private imagery, it is crucial to use the "Pro Plan" or above and enable "stealth mode" in the settings <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>. This prevents assets from appearing in the public database <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.

## Why Use Midjourney?

Midjourney serves multiple purposes:
*   **Inspiration and Ideation:** It's a powerful tool for generating ideas, putting together concepts, and exploring different possibilities, similar to building a mood board <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Production:** It can be used directly in production workflows, especially with its editor feature for outpainting and adding new elements to existing assets <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.
*   **Art Therapy:** Many find it enjoyable and therapeutic, allowing them to get lost in the creative process <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Discovery Engine:** It allows users to quickly explore aesthetics and go down "rabbit holes" of creative discovery <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
*   **Creative Control:** Midjourney offers significant creative control over the final output, enabling users to transform ideas into living design assets <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.

## Core Elements of Prompting

When creating images in Midjourney's "create" tab, users can combine various elements:

### Image Prompts

*   **Uploading Images:** Images can be uploaded by clicking the image icon in the prompt bar <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.
*   **Image Prompt vs. Style Reference:**
    *   **Image Prompt (pict icon):** When an image is used as an image prompt, Midjourney attempts to pull in the subject matter and actual pixels of the image <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. Increasing the image weight (`--iw`) will make Midjourney prioritize incorporating the visual elements of the input image, potentially leading to "wonky" results if the subject matter is too strong (e.g., a hand-giraffe when a hand image is used with a giraffe prompt) <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>.
    *   **Style Reference (paperclip icon):** Midjourney attempts to understand the aesthetic qualities of the image and integrate those elements without necessarily pulling in the subject matter <a class="yt-timestamp" data-t="00:15:58">[00:15:58]</a>. This is crucial for matching a desired style <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. Multiple style references can be combined to blend styles <a class="yt-timestamp" data-t="00:28:42">[00:28:42]</a>.

### Text Prompts

Text prompts guide the subject matter and desired medium (e.g., "a paper cutout illustration of a giraffe") <a class="yt-timestamp" data-t="00:18:13">[00:18:13]</a>. Even with style references, text prompts can provide "assistance" to guide the direction of the generation <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.

### Parameters

Parameters are "levers" that allow users to balance and guide the aesthetics <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>:
*   **Style Weight (`--sw`):** Determines how much influence a style reference has on the generation <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>. The default is 100, but it can go up to 1000 for stronger influence <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Aspect Ratio (`--ar`):** Changes the output image's proportions (e.g., `--ar 2:3` for a poster print) <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   **No Parameter (`--no`):** Used to exclude specific elements from the generation (e.g., `--no text`) <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>.
*   **Stylize (`--s`):** Controls how much of Midjourney's default aesthetic (curated by the community) is applied <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>. A high stylize value (e.g., 1000) makes the image look "very AI," while a lower value (e.g., default 100) balances the text prompt with Midjourney's aesthetics, allowing more creative leeway <a class="yt-timestamp" data-t="00:31:50">[00:31:50]</a>.
*   **Style Raw (`--style raw`):** Leans toward a more photorealistic output <a class="yt-timestamp" data-t="00:52:06">[00:52:06]</a>.
*   **Weighting Multiple Styles:** When combining multiple style references or elements, a double colon (`::`) followed by a number can be used to assign relative weights (e.g., `srf1::2 srf2::1` means two parts of style 1 and one part of style 2) <a class="yt-timestamp" data-t="00:44:35">[00:44:35]</a>.

### Personalization

Midjourney offers a personalization feature that fine-tunes the model to a user's aesthetic preferences <a class="yt-timestamp" data-t="00:31:00">[00:31:00]</a>. This is achieved by rating images in the "Personalize" tab, where users select their favorite images from presented pairs <a class="yt-timestamp" data-t="00:29:45">[00:29:45]</a>. The more images rated (e.g., a thousand), the more Midjourney learns about preferred colors, lighting, general style (photographic vs. illustrative), and even subject matter <a class="yt-timestamp" data-t="00:30:27">[00:30:27]</a>. Turning on personalization significantly alters the aesthetics compared to the community-curated default <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>. Users can also blend their personalization with others' or adjust its influence using the `--s` parameter <a class="yt-timestamp" data-t="00:34:58">[00:34:58]</a>.

### Style Reference Codes (SRF Codes)

These codes are like "coordinates" in a multi-dimensional style space that direct the AI to a specific aesthetic location <a class="yt-timestamp" data-t="00:37:34">[00:37:34]</a>. Anything prompted will be influenced by that location <a class="yt-timestamp" data-t="00:37:44">[00:37:44]</a>. There are billions of SRF codes, representing various combinations of color, composition, lighting, texture, and pattern <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>. Users can find and use these codes to define or blend specific aesthetics <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>. Users are exploring and curating these codes, combining them with personalization and text prompts to create "aesthetic recipes" <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.

### Helpful Tips

*   **Save Favorites:** Users should "like" their favorite generations by clicking the heart icon or right-clicking on the image <a class="yt-timestamp" data-t="00:27:22">[00:27:22]</a>. This makes it easier to find them later in the "Organize" tab by filtering for "liked" items <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>.
*   **Re-running Prompts:** After hitting enter, pressing the up arrow on the keyboard automatically repopulates the last prompt <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>.
*   **Permutation Prompts:** Using brackets and commas allows users to run multiple parameter values in one go, quickly comparing visual results <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>.

## Beyond the Digital

There are efforts to physically manifest latent space, such as a lab in Red Hook, NYC, in partnership with Pioneer Works <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>. This lab aims to teach deep usage of creative AI tools and provide equipment (robots learning to paint or play music, 3D printers, plotter printers, editing stations) to bring digital creations to life <a class="yt-timestamp" data-t="01:00:03">[01:00:03]</a>. This includes moving from image to video models to create more dynamic pieces <a class="yt-timestamp" data-t="01:00:31">[01:00:31]</a>.

## Related Topics

*   [[innovations_in_ai_image_generation_and_design | Innovations in AI Image Generation and Design]]
*   [[generating_app_assets_using_ai_tools | Generating app assets using AI tools]]
*   [[creating_aigenerated_commercials | Creating AI-generated commercials]]
*   [[creating_video_games_with_ai | Creating video games with AI]]
*   [[generating_brand_assets_with_ai | Generating brand assets with AI]]
*   [[automating_content_creation_with_ai | Automating content creation with AI]]
*   [[building_a_business_around_aigenerated_content | Building a business around AI-generated content]]
*   [[business_ideas_using_aigenerated_content | Business ideas using AI-generated content]]
*   [[opportunities_in_aigenerated_music | Opportunities in AI-generated music]]