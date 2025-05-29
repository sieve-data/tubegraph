---
title: Exploring aesthetics with style space in MidJourney
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

[[midjourney_as_a_new_design_canvas | MidJourney]] is described as an entirely new medium, a different type of canvas and a different way of problem-solving [00:00:01]. It allows users to blend and balance entire aesthetics with layers and complexity to achieve a desired visual outcome [00:00:10]. Once a "recipe" is found, it can be infinitely prompted into [00:00:24].

## Visual vs. Text Prompts in MidJourney

Initially, [[ai_design_tools_like_runway_and_midjourney | MidJourney]] primarily relied on words and parameters for prompting [00:01:55]. While words are still useful, they represent "just the tip of the iceberg" [00:01:07]. Much more can be achieved by using visuals to drive visuals, rather than semantics, which allows for the explosion of aesthetics and style space into "almost infinite directions" [00:01:12]. This approach reduces reliance on the base model's interpretation of style tokens, enabling users to "pave our own lane" [000:01:23].

Recent months have seen the release of features like Style Space, style references, and character references, which collectively "explodes Aesthetics out into this infinite universe" [00:02:29]. This makes playing on a visual canvas more enjoyable than simply blending keywords [00:02:45].

## Navigating MidJourney

For optimal use, it is recommended to transition from Discord to the [[ai_design_tools_like_runway_and_midjourney | MidJourney]] web app at midjourney.com, which is open to everyone [00:06:36].

### Finding Inspiration

Inspiration can be found both externally and within [[midjourney_for_inspiration_and_creative_exploration | MidJourney]] itself:
*   **External Sources**: Websites like Reddit, Pinterest, and Google image search are good starting points [00:05:41]. For example, old Tokyo Trade Fair posters from 1995 provided inspiration with their simple, minimalist paper cutout graphics, bold colors, and simple shapes [00:05:59].
*   **MidJourney Explore Tab**: The "Explore" tab in the [[ai_design_tools_like_runway_and_midjourney | MidJourney]] web app showcases publicly available generations [00:07:07]. Users can search for styles (e.g., "vintage poster") [00:07:31]. If a particular style is appealing, clicking the search icon next to an image will provide similar results in terms of subject matter and style [00:07:46]. Users can also "Like" images and utilize their prompts or styles directly [00:08:33].

### Privacy Considerations

Users with standard plans or below have publicly visible generations by default [00:07:15]. For client work or branded content using proprietary imagery, it is crucial to be on the Pro Plan or above and enable "stealth mode" in the settings to prevent assets from appearing in the public database [00:10:26].

## Leveraging Style References

[[midjourney_for_inspiration_and_creative_exploration | MidJourney]] is a powerful tool for ideation, concept development, and exploration, akin to building a mood board but with more control [00:11:16]. It can also be used in production, especially with the new editor feature for out-painting and adding new elements [00:11:52]. It also serves as a form of "art therapy" due to its immersive nature [00:12:16]. Its most exciting aspect is its function as a "discovery engine," allowing users to explore aesthetics down a "Rabbit Hole" [00:12:27].

### Image Prompt vs. Style Reference

When adding an image to a prompt, it can function in two key ways:
*   **Image Prompt (Pict Icon)**: By default, images are added as image prompts. In this mode, [[ai_design_tools_like_runway_and_midjourney | MidJourney]] attempts to pull in the subject matter and actual pixels of the input image [00:20:00]. Increasing the image weight will make MidJourney try to incorporate more elements from the image directly into the generation [00:20:48]. For instance, a hand image used as an image prompt might result in a "hand giraffe" [00:21:10].
*   **Style Reference (Paperclip Icon)**: When selected as a style reference, [[ai_design_tools_like_runway_and_midjourney | MidJourney]] analyzes the image to understand its aesthetic qualities by "decoupling aesthetic from subject matter" [00:19:49]. It then integrates these stylistic elements into the new generation [00:16:01]. This is crucial for maintaining a desired aesthetic without pulling in unwanted subject matter [00:21:17].

### Style Weight (`--sw`)

The `--sw` parameter allows users to control the influence of a style reference on the generation [00:17:18]. The default style weight is 100, but it can be increased up to 1000 for a stronger stylistic resemblance [00:17:36]. This helps guide the aesthetics, especially when initial results are too photorealistic for an illustrative style [00:17:56].

### Combining Elements

To refine results, users can combine a style reference with a supporting text prompt and aspect ratio parameters. For example, using a paper cutout illustration style reference, specifying "a paper cutout illustration of a giraffe," and setting an aspect ratio like `--ar 2:3` for a poster print, helps guide the generation towards the desired look [00:18:13]. The process involves continuous balancing and finding harmony between these "levers" [00:18:29].

## Style Reference Codes (SRF Codes)

In addition to using images as style references, [[personalization_and_style_reference_codes_in_midjourney | MidJourney]] introduced Style Reference Codes (SRF codes) [00:37:16]. These codes are like "coordinates" in a multi-dimensional Style Space, directing [[ai_design_tools_like_runway_and_midjourney | MidJourney]] to a specific aesthetic location that influences anything prompted [00:37:34]. There are billions of possible SRF codes, and users are "mining these out of Mid Journey," curating them, and mixing them with their own personalization and text prompt flavorings to build "aesthetic recipes" [00:38:08].

SRF codes allow for visual exploration of styles, where users can search by "style, vibe, [or] theme" [00:39:01]. Multiple SRF codes can be combined in a single prompt, allowing for the blending of different styles like "paint on a palette" [00:40:02]. Unlike simple paint colors, SRF codes represent complex aesthetic elements including color, composition, lighting, texture, and pattern [00:40:19].

## Personalization and Stylize (`--s`)

[[personalization_and_style_reference_codes_in_midjourney | Personalization and style reference codes in MidJourney]] is a feature that fine-tunes the model to a user's aesthetic preferences [00:31:31]. This is achieved by rating images in the "Personalize" tab on the [[ai_design_tools_like_runway_and_midjourney | MidJourney]] web app [00:29:45]. The more images rated, the more [[ai_design_tools_like_runway_and_midjourney | MidJourney]] learns preferences for colors, lighting, general style (photographic vs. illustrative), and even subject matter [00:30:15]. This significantly impacts the aesthetics of generated images and is highly recommended as a first step for new users [00:30:34].

The `--stylize` (`--s`) parameter controls "how much of the Mid Journey model" aesthetics (curated by the community) are applied to a text prompt versus just the interpretation of the text prompt [00:31:22].
*   High stylize values (e.g., 1000) tend to produce images that "scream AI" or strongly reflect the default MidJourney aesthetic [00:32:15].
*   The default stylize value (100) balances the text prompt with MidJourney aesthetics, offering more creative leeway [00:32:00].
*   When personalization is turned on, [[ai_design_tools_like_runway_and_midjourney | MidJourney]] applies the user's fine-tuned aesthetic preferences instead of the community-curated default [00:32:45].

Personalization can even be blended with other users' personalizations for unique stylistic combinations [00:34:58].

## Advanced Techniques and Control

[[ai_design_tools_like_runway_and_midjourney | MidJourney]] offers numerous levers for aesthetic control, enabling users to move beyond a "slot machine game" of random prompting [00:45:37].

*   **Balancing Aesthetic Levers**: The key is to balance style references, text prompts, parameters (like style weight `--sw` and stylize `--s`), and personalization [00:29:03]. Understanding how each influences the output helps make more guided decisions [00:16:36].
*   **Parameter Weights**: Within multiple style references, the `::` syntax can be used to assign different weights to each style, influencing their relative contribution to the blend [00:44:37].
*   **Permutation Prompts**: For experimenting with different parameter values, permutation prompts using curly brackets and commas (e.g., `{100, 500, 1000}`) allow running multiple variations in one go to quickly visualize and choose the best level [00:49:17].
*   **Editor Feature**: The built-in editor allows for "out-painting" and removing elements like unwanted text by masking them [00:26:29]. The `--no` parameter can also be used in the prompt to explicitly tell [[ai_design_tools_like_runway_and_midjourney | MidJourney]] what to remove [00:26:52].
*   **Organizing Favorites**: To easily find past creations, users should "Like" their favorite images using the heart icon [00:27:22]. This allows filtering by "liked" in the organize tab, preventing getting lost among hundreds of generations [00:27:50].

This deep level of control over aesthetic direction is what distinguishes [[ai_design_tools_like_runway_and_my_ai_design_tools_like_runway_and_midjourney | MidJourney]] from other AI tools, as it allows users to "build up that world" and create unique, living, breathing design assets [00:46:44]. The visual nature of style references and SRF codes allows for greater complexity than text-only prompting, as "a picture's worth a thousand words" [00:47:11].

Future developments include efforts to "physically manifest latent space" by building a lab with equipment like robots for painting and music, 3D printers, and editing stations to bring digital creations to life [00:59:47].