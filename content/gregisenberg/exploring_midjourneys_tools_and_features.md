---
title: Exploring Midjourneys tools and features
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

[[midjourney_as_a_new_artistic_medium | Midjourney]] is considered a new artistic medium, a different type of canvas, and a unique way of problem-solving [00:00:00]. It allows users to blend and balance entire aesthetics with layers and complexity to achieve desired results [00:00:10]. Once a "recipe" is found, it can be infinitely prompted into [00:00:24].

## Getting Started with Midjourney

Historically, Midjourney focused on text prompts and parameters, with image prompts pulling in subject matter rather than style [00:01:50]. However, recent months have seen the release of new features like Style Space, style references, and character references, which [[using_style_references_and_personalization_in_midjourney | explode aesthetics into an infinite universe]] [00:02:19]. The emphasis has shifted from semantics to visuals for driving visual output, allowing for infinite directions in aesthetics and style [00:01:09].

### Midjourney Web App

It is recommended to use the Midjourney web app at midjourney.com instead of Discord, as it offers a more efficient workspace [00:06:36].

### Core Tabs

*   **Explore Tab**: This tab displays all publicly available generations, serving as a vast library for inspiration [00:07:05]. Users can search for specific themes like "vintage poster" [00:07:31]. If a particular style is appealing, an image search can be performed to find similar results [00:07:46].
    *   **"Use Prompt"**: Copies the entire prompt from a public generation for reuse [00:08:44].
    *   **"Use Style"**: Brings the image in as a style reference (indicated by a paperclip icon) [00:08:50].
    *   **"Use Image"**: Incorporates the image as an image prompt [00:09:00].
*   **Create Tab**: This is where most of the creative work takes place [00:06:54].

### Privacy Considerations

For client work or proprietary imagery, it's crucial to subscribe to the Pro Plan or above and activate "stealth mode" in the settings. This prevents generated assets from appearing in the public database [00:10:26].

### Why Use Midjourney?

[[practical_applications_and_workflows_in_midjourney | Midjourney]] serves as a powerful inspiration and discovery tool, allowing users to quickly develop ideas, assemble concepts, and explore aesthetics [00:11:16]. It offers greater control over visual outcomes compared to traditional mood board creation [00:11:36]. It can also be used in production, especially with the editor feature for outpainting and adding new elements [00:11:52]. Beyond professional uses, it can be a form of "art therapy," where users can get lost in the creative process [00:12:14]. The ability to transform an idea into a "living breathing asset" that can be used on websites, landing pages, or social media, demonstrates its value in [[ai_tools_for_business_and_content_creation | business and content creation]] [00:13:23].

## Key Features and Parameters

### Image Prompt vs. Style Reference

*   **Image Prompt**: When an image is added as an image prompt (default, indicated by a "pict" icon), Midjourney attempts to pull in the subject matter and actual pixels of the source image [00:20:00]. Increasing the image weight (`--iw`) makes the original image's elements more prominent, potentially leading to "wonky" results if the goal is only style transfer [00:20:48].
*   **Style Reference (`--sref`)**: When an image is added as a style reference (indicated by a paperclip icon), Midjourney analyzes the image to understand its aesthetic qualities, decoupling them from the subject matter [00:19:41]. This allows the generated images to adopt the visual style (colors, composition, lighting, texture, pattern) without directly copying the original content [00:40:19].

### Parameters for Control

Midjourney offers various parameters to balance and guide aesthetic outcomes:

*   **Style Weight (`--sw`)**: Determines how much influence a style reference has over the generation [00:17:20]. The default is 100, but it can be increased up to 1000 for stronger influence [00:17:36].
*   **Aspect Ratio (`--ar`)**: Controls the width-to-height ratio of the generated image, useful for specific formats like posters [00:19:03].
*   **No Parameter (`--no`)**: Instructs Midjourney to remove specified elements from the generation, e.g., `--no text` [00:26:52].
*   **Stylize (`--s`)**: Controls how much of the Midjourney model's default aesthetic (curated by the community) is applied to the text prompt [00:31:20]. High stylize values (e.g., 1000) result in images that "scream AI," while lower values (default 100) offer more creative leeway and a balanced look [00:32:00].

### Personalization

Midjourney offers a "personalization" feature that allows the model to learn a user's aesthetic preferences [00:29:37]. By rating images in the "Personalize" tab, users teach Midjourney about their preferred colors, lighting, general style (photographic vs. illustrative), and even subject matter [00:30:13]. This fine-tunes the model to the user's specific tastes, leading to more desired results and significantly changing the aesthetics of generations [00:30:29]. Turning up the stylize parameter when personalization is active increases the influence of these learned preferences [00:32:41].

### Style Reference Codes (`sref`)

Style reference codes are "coordinates" in a "multi-dimensional Style Space" that direct Midjourney to a specific aesthetic location [00:37:31]. There are billions of these codes, which users can "mine" or discover to find desired styles [00:38:01]. These codes can be used in prompts to influence generations [00:38:45]. Multiple `sref` codes can be combined, similar to blending paints on a palette, to create unique "aesthetic recipes" [00:39:59]. Weights can be assigned to `sref` codes (e.g., `sref::2` for two parts) to control their influence when blending [00:44:49].

### Editor Feature

The editor allows users to manipulate existing assets, such as outpainting or adding new elements [00:50:47].

### Organization Tips

*   **Favorites**: Liking favorite generations (using the heart icon or right-clicking) makes it much easier to find specific images later in the organized library [00:27:19].

## Workflow and Exploration

A basic process for exploring aesthetics involves:
1.  Starting with a simple subject (e.g., "giraffe") and a style reference [00:15:19].
2.  Observing how Midjourney interprets the style reference and noting any unwanted elements (e.g., photorealism when an illustrative style is desired) [00:16:31].
3.  Adjusting parameters like `--sw` to increase the style's influence [00:17:18].
4.  Adding supporting text to the prompt (e.g., "paper cutout illustration") to guide Midjourney towards the desired medium [00:18:13].
5.  Experimenting with aspect ratios (`--ar`) to fit specific layouts like posters [00:19:03].
6.  Generating variations (subtle or strong) to explore different compositions while maintaining the core style [00:25:35].
7.  Using the editor to refine images, such as removing unwanted text [00:26:29].
8.  Incorporating personalization to infuse personal aesthetic preferences into the generations [00:32:31].
9.  Experimenting with `sref` codes from external tools or the explore tab to discover and blend new aesthetics [00:38:35].
10. Using permutation prompts (e.g., `[50, 100, 500, 1000]`) to quickly test multiple parameter values at once and visually compare results [00:49:17].

The goal is to analyze results, understand how parameters and inputs influence the output, and iteratively refine the "aesthetic mix" [00:42:04]. This process is about finding balance and harmony between different "aesthetic levers" rather than relying on a "slot machine" approach [00:28:29].

## Future Possibilities

[[integration_of_ai_tools_like_runway_and_midjourney | A lab in Red Hook]] is being built to teach deep-level use of creative AI tools like Midjourney, and to provide equipment (robots for painting, 3D printers, plotter printers, editing stations) for physically manifesting digital creations [00:59:51]. This aims to bring AI-generated art to life beyond the digital realm, enabling printed canvases, animated videos, and more [01:00:13].