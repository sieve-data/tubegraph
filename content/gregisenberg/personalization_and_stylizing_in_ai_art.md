---
title: Personalization and Stylizing in AI Art
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

Midjourney is considered a new medium entirely, offering a different canvas and approach to problem-solving [00:00:00]. It involves blending and balancing aesthetics to find harmony in creations, allowing for infinite prompting once a "recipe" is discovered [00:00:10].

## Beyond Text Prompts
Initially, Midjourney primarily relied on words and parameters [00:01:55]. While words remain valuable, they are merely "the tip of the iceberg" [00:01:07]. The true potential lies in using visuals to drive visuals, which can "explode aesthetics and style space into almost infinite directions" [00:01:12]. This approach reduces reliance on the base model's interpretation of style tokens, allowing users to "pave our own lane" [00:01:29].

New features like Style Space, style references, and character references have transformed the tool, making it more about visual exploration than intricate prompt structuring [00:02:19].

### Midjourney Web App
Users are advised to migrate from Discord to the Midjourney web app (midjourney.com) for a better experience [00:06:36].

The "Explore" tab in the web app showcases publicly available generations, serving as a significant source of inspiration [00:07:07]. Users can search for specific styles (e.g., "vintage poster") [00:07:31]. If a particular style is appealing, the "search icon" allows for finding similar results, including subject matter and styles [00:07:46].

### Uses of Midjourney
Midjourney serves as a powerful inspiration tool, similar to mood boarding, but with greater control over the generated content [00:11:16]. It's excellent for ideation, concept development, and exploration [00:11:47]. The tool can also be integrated into production workflows, especially with features like the new editor that allow for outpainting and adding elements to existing assets [00:11:52]. Beyond professional use, many find it enjoyable as a form of "art therapy" [00:12:14].

## Image Prompts vs. Style References
A crucial distinction in Midjourney involves how images are used in prompts:

*   **Image Prompt**: When an image is dragged into the prompt bar, it defaults to an image prompt (represented by a "pict" icon) [00:14:24]. In this mode, Midjourney attempts to pull in the actual subject matter and pixels of the image, leading to mixed results if only the style is desired (e.g., a "hand giraffe") [00:20:00].
*   **Style Reference**: By clicking the "paperclip" icon, an image is used as a style reference [00:15:03]. This tells Midjourney to analyze the image's aesthetic (colors, composition, lighting, texture, pattern) and apply that style to the new generation, decoupling it from the subject matter [00:19:41].

## Key Parameters for Stylizing
Midjourney offers various "levers" to control and balance the aesthetic output:

*   **`--sw` (Style Weight)**: This parameter determines how much influence a style reference has over the generation. The default is 100, but it can be increased up to 1000 for stronger influence [00:17:18].
*   **`--ar` (Aspect Ratio)**: Used to define the output image's aspect ratio (e.g., `--ar 2:3` for a poster print) [00:19:03].
*   **`--no` (No Parameter)**: Allows users to specify elements they want excluded from the generation (e.g., `--no text` to remove text) [00:26:52].
*   **`--s` (Stylize)**: Controls how much of Midjourney's default, community-curated aesthetic is applied to the text prompt [00:31:20]. A high stylize value (e.g., `--s 1000`) results in images that "scream AI" [00:32:15], while lower values offer more creative leeway [00:32:10].

## Personalization
Midjourney's "Personalize" tab allows users to "teach" the model their aesthetic preferences [00:29:37]. By rating images (selecting favorites or skipping ones you don't like), Midjourney learns preferences for colors, lighting, general style (photographic vs. illustrative), and even preferred subjects or ethnicities [00:29:51]. This process fine-tunes the model to the user's specific "vibe," making "everything better" and yielding unique results that don't look like "classic Midjourney" [00:30:34].

> [!NOTE] Stealth Mode
> For client work or proprietary imagery, it is crucial to activate "stealth mode" on a Pro Plan or above to prevent assets from appearing in the public "Explore" database [00:10:26]. This setting is found in the little "settings" gear icon on the right side of the prompt bar [00:10:48].

## Style Reference (SRF) Codes
SRF codes are "coordinates in this multi-dimensional Style Space" that direct the AI to a specific aesthetic location [00:37:34]. Anything prompted is then influenced by that location [00:37:44]. Users can find these codes in tools like the Style Reference Explorer, which contains thousands of visually searchable references [00:36:59].

### Blending Styles
Multiple SRF codes can be combined in a single prompt to blend aesthetics, akin to mixing "paint on a palette" [00:39:59]. Unlike simple colors, these styles represent complex attributes like color, composition, lighting, texture, and pattern, which are then balanced with text prompts and other parameters [00:40:17].

Weights can be assigned to individual style references within a prompt using the `::` syntax (e.g., `srf code_A::2 srf code_B::1`) to control their relative influence [00:44:37]. This allows for controlled experimentation and understanding how different aesthetic elements contribute to the final output [00:45:10].

## Midjourney Editor
The editor feature allows for direct manipulation of generated images, such as adjusting aspect ratios, moving subjects, and using inpainting to remove unwanted elements (e.g., text) [00:26:28].

## Future Possibilities
The concept of "physically manifesting latent space" involves bringing AI-generated art to life using physical tools like robots for painting, 3D printers, and plotter printers [00:59:47]. This aims to create a space where users can learn deep AI tools and produce tangible art [01:00:03].