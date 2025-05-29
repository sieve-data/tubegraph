---
title: Exploring aesthetics and style references in Midjourney
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

[[Midjourney as a new medium for art creation | Midjourney]] is considered a new medium entirely, acting as a different type of canvas and a different way of problem-solving for artists and designers <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It allows users to blend and balance entire aesthetics with multiple layers and complexities to achieve desired harmony <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Once a "recipe" is found, it can be infinitely prompted <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Beyond Text Prompts: Visual-Driven Design

Initially, [[Midjourney as a new medium for art creation | Midjourney]] primarily relied on word-based prompts <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. However, the true power lies in using visuals to drive visuals, rather than semantics <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This approach allows for the exploration of aesthetics and style space in almost infinite directions, reducing reliance on the base model's interpretation of style tokens <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Recent updates have introduced "Style Space," [[personalization_and_style_referencing_in_midjourney | style references]], and character references, enabling a more visual approach to creation <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## The Midjourney Web App

For optimal use, it is recommended to transition from Discord to the [[Midjourney as a new medium for art creation | Midjourney]] web app ([midjourney.com](https://www.midjourney.com)) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The web app offers a more user-friendly interface <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

### Finding Inspiration
The "Explore" tab in the [[Midjourney as a new medium for art creation | Midjourney]] web app showcases publicly available generations, serving as a vast library of inspiration <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Users can search for specific themes (e.g., "vintage poster") <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. If a particular style is appealing, an image search feature (magnifying glass icon) can find similar results based on subject matter and style <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

From any explored image, users have several options:
*   **Use Prompt:** Copies the original text prompt for modification <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.
*   **Use Style:** Imports the image as a [[personalization_and_style_referencing_in_midjourney | style reference]] (indicated by a paperclip icon) <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.
*   **Use Image:** Imports the image as an image prompt (indicated by a picture icon) <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

### Stealth Mode for Client Work
For client work or private projects, the Pro Plan allows users to activate "stealth mode" in the settings, ensuring assets do not appear in the public database <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.

## The Power of Style References (`--sref`)

When incorporating external images (or internal ones from the "Explore" tab), [[Midjourney as a new medium for art creation | Midjourney]] offers two primary ways to use them:

1.  **Image Prompt (Picture icon):**
    *   This function attempts to pull in the subject matter and actual pixels of the source image <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.
    *   Increasing the image weight (`--iw`) will make Midjourney prioritize these elements, potentially leading to distorted results if the goal is purely style transfer (e.g., a "hand giraffe") <a class="yt-timestamp" data-t="00:20:48">[00:20:48]</a>.

2.  **Style Reference (Paperclip icon):**
    *   This is crucial for aesthetic exploration <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.
    *   [[Midjourney as a new medium for art creation | Midjourney]] attempts to understand the *aesthetic* of the image by decoupling it from the subject matter <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>.
    *   **Style Weight (`--sw`):** This parameter controls how much influence the [[personalization_and_style_referencing_in_midjourney | style reference]] has over the generation <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>. The default is 100, but it can go up to 1000, allowing for stronger adherence to the reference's style <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
    *   **Assisting with Text Prompts:** Combining a [[personalization_and_style_referencing_in_midjourney | style reference]] with a descriptive text prompt (e.g., "a paper cutout illustration of a giraffe") can provide the necessary guidance to achieve a specific look <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
    *   **Aspect Ratio (`--ar`):** Another parameter that can be adjusted to fit desired layouts, such as posters (e.g., `--ar 2:3`) <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.

### Managing Generations
To prevent losing desired outputs, users should "like" their favorite generations using the heart icon <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>. This allows for easy filtering in the "Organize" tab <a class="yt-timestamp" data-t="00:27:50">[00:27:50]</a>.

## Why Use Midjourney?

[[Midjourney as a new medium for art creation | Midjourney]] is invaluable for:
*   **Inspiration and Ideation:** It acts as a powerful discovery engine, similar to mood boarding tools like Pinterest or Tumblr, but with more creative control <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **Production:** With features like the new editor, it can be used to out-paint or add new elements to existing assets <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.
*   **Art Therapy and Engagement:** Many find the process fun and can get lost in the creative exploration <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Creating High-Quality Art:** Highly skilled users can produce art that is indistinguishable from traditional art forms, suitable for personal use, websites, or social media <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>.

## Personalization and Stylization

### Fine-tuning the Model to Your Aesthetic
[[personalization_and_style_referencing_in_midjourney | Personalization]] is a key feature that allows [[Midjourney as a new medium for art creation | Midjourney]] to learn a user's aesthetic preferences <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>. By regularly rating images in the "Personalize" tab, the model learns preferred colors, lighting, general style (photographic vs. illustrative), and even specific subjects <a class="yt-timestamp" data-t="00:29:48">[00:29:48]</a>. This process fine-tunes the model to the user's taste, significantly influencing future generations <a class="yt-timestamp" data-t="00:30:30">[00:30:30]</a>. It is highly recommended to rate at least a thousand images to leverage this feature <a class="yt-timestamp" data-t="00:30:41">[00:30:41]</a>.

### Stylize Parameter (`--s`)
The `--s` (stylize) parameter controls how much of [[Midjourney as a new medium for art creation | Midjourney]]'s default or community-curated aesthetic is applied to a text prompt <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>.
*   **High Stylize Values (e.g., `--s 1000`):** Tend to make images look more "AI-generated" or like the default style of [[Midjourney as a new medium for art creation | Midjourney]] <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.
*   **Lower Stylize Values (e.g., default `--s 100`):** Offer a more balanced look, allowing more creative leeway and integrating better with [[personalization_and_style_referencing_in_midjourney | personalization]] <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>.

When [[personalization_and_style_referencing_in_midjourney | personalization]] is turned on, the model adapts its default aesthetics to the user's learned preferences <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.

## Style Reference Codes (`--srf`)

Beyond using images as [[personalization_and_style_referencing_in_midjourney | style references]], [[Midjourney as a new medium for art creation | Midjourney]] introduces "style reference codes" (`--srf`) <a class="yt-timestamp" data-t="00:37:16">[00:37:16]</a>.
*   These codes are like multi-dimensional coordinates in "Style Space" that direct the model to a specific aesthetic location <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>.
*   Anything prompted will be influenced by the aesthetic attributes associated with that code, which can include color, composition, lighting, texture, and pattern <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>.
*   Users can blend multiple SRF codes by including them in a single prompt, optionally assigning relative weights using `::` (e.g., `srf <code1>::2 srf <code2>::1`) <a class="yt-timestamp" data-t="00:44:49">[00:44:49]</a>. This allows for complex aesthetic combinations, akin to mixing paints on a palette <a class="yt-timestamp" data-t="00:39:59">[00:39:59]</a>.
*   Tools like the Style Reference Explorer can help visually discover and curate SRF codes <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>.

## Balancing and Harmony

The core of [[Midjourney as a new medium for art creation | Midjourney]] use lies in [[balancing_and_blending_aesthetic_elements_using_ai | balancing and finding harmony]] between various "aesthetic levers" <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>:
*   [[personalization_and_style_referencing_in_midjourney | Style references]] (images or SRF codes)
*   Text prompts (including medium, lighting, subject details)
*   Parameters (e.g., `--sw`, `--ar`, `--s`, `--no`)
*   [[personalization_and_style_referencing_in_midjourney | Personalization]] settings

By experimenting with these elements and observing the visual results, users can guide the AI to create unique and desired aesthetics <a class="yt-timestamp" data-t="00:42:02">[00:42:02]</a>. This systematic approach helps move beyond merely playing a "slot machine game" and enables more intentional creative control <a class="yt-timestamp" data-t="00:45:22">[00:45:22]</a>.

## From Digital to Physical
The goal is to not only create stunning digital art but also to bring it to life physically <a class="yt-timestamp" data-t="00:59:47">[00:59:47]</a>. This involves using equipment like robots for painting, 3D printers, and editing stations to transition [[creating_animated_visuals_with_ai_tools_like_runway | AI-generated images into videos]] and other tangible forms <a class="yt-timestamp" data-t="01:00:10">[01:00:10]</a>.