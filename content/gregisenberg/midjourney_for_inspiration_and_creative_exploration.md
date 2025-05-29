---
title: MidJourney for inspiration and creative exploration
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

[[ai_design_tools_like_runway_and_midjourney | MidJourney]] is considered a new medium entirely, offering a different type of canvas and a different way of problem-solving [00:00:00]. Instead of just paint, users have entire aesthetics with layers and complexity that can be blended and balanced to find harmony [00:00:10]. Once a preferred "recipe" is found, it can be infinitely prompted into [00:00:24].

## Why Use MidJourney for Inspiration?

[[ai_design_tools_like_runway_and_midjourney | MidJourney]] serves as a powerful inspiration tool, allowing users to jam out ideas quickly [00:11:16]. It functions similarly to exploring platforms like Pinterest or Google Image Search for mood boards, but with more control over the results [00:11:24]. It is excellent for ideating, exploring concepts, and putting together designs [00:11:47].

Beyond ideation, [[ai_design_tools_like_runway_and_midjourney | MidJourney]] can be used in production, especially with features like the editor that allow out-painting and adding new elements to existing assets [00:11:52]. Many users also find it a form of "art therapy," where they can get lost in the creative process [00:12:14]. Ultimately, it's described as a "discovery engine" to explore aesthetics and go down creative rabbit holes [00:12:27].

The ability to turn an idea into a "living, breathing design asset" is highly valuable [00:13:23]. Users can create art for personal enjoyment, websites, landing pages, or social media [00:13:06]. [[ai_design_tools_like_runway_and_midjourney | MidJourney]] offers significant creative control, making it a new medium for artistic expression [00:13:36].

## Navigating MidJourney for Creative Exploration

### Essential Tips for Getting Started
*   **Use the Web App**: It's highly recommended to use the [[ai_design_tools_like_runway_and_midjourney | MidJourney]] web app (`midjourney.com`) instead of Discord, as it offers a superior working environment [00:06:36].
*   **Explore Tab**: The explore tab on the web app displays all publicly available generations, serving as a vast library of inspiration [00:07:05]. Users can search for specific themes like "vintage poster" [00:07:31].
*   **Image Search**: Clicking the search icon on an image in the explore tab will find similar results based on subject matter and style [00:07:46].
*   **Prompt and Style Reuse**: Users can easily apply a prompt from an existing image using "Use Prompt" or "Use Style" [00:08:44].
*   **Stealth Mode**: For client work or proprietary imagery, it's crucial to use the Pro Plan or above and turn on stealth mode in the settings to prevent assets from appearing in the public database [00:10:26].
*   **Favorite Your Creations**: Liking favorite images using the heart icon or right-clicking significantly helps organize and find specific generations later in the library [00:27:19].

## Core Concepts for Creative Exploration in MidJourney

[[midjourney_as_a_new_design_canvas | MidJourney]] operates using various "aesthetic levers" that can be pulled and balanced to guide the direction of image generations [00:29:03].

### Visual vs. Text Prompts
Traditional text prompts are powerful, but [[visual_versus_text_prompts_in_midjourney | visual prompts]] offer a different dimension of control.
*   **Image Prompt**: When an image is used as an image prompt (represented by a "pict icon"), [[ai_design_tools_like_runway_and_midjourney | MidJourney]] attempts to pull in the subject matter and actual pixels of that image [00:20:00]. Increasing the image weight will make the generated image resemble the input image more closely, potentially mixing subjects (e.g., a hand giraffe if a hand image is used with a giraffe prompt) [00:20:45].
*   **Style Reference**: Using an image as a style reference (represented by a "paperclip icon" or `--sref` parameter) is crucial for aesthetic exploration [00:14:32]. [[ai_design_tools_like_runway_and_midjourney | MidJourney]] analyzes the style reference to understand its aesthetic qualities (color, composition, lighting, texture, pattern) and decouple them from the subject matter, applying these qualities to new generations [00:19:41].

### Aesthetic Levers and Parameters
*   **Style Weight (`--sw`)**: This parameter determines how much influence a style reference has over the generation [00:17:20]. The default is 100, but it can be increased up to 1000 for more stylistic adherence [00:17:36].
*   **Text Prompts**: While [[visual_versus_text_prompts_in_midjourney | visual prompts]] are emphasized, text prompts still assist in guiding the desired output, especially when combined with style references (e.g., "a paper cutout illustration of a giraffe") [00:18:05].
*   **Aspect Ratio (`--ar`)**: Adjusting the aspect ratio (e.g., `2:3` for a poster print) helps guide the composition and layout [00:19:03].
*   **Negative Prompt (`--no`)**: The `--no` parameter tells [[ai_design_tools_like_runway_and_midjourney | MidJourney]] what to exclude from the generation (e.g., `no text`) [00:26:52].
*   **Stylize (`--s`)**: This parameter controls how much of the [[ai_design_tools_like_runway_and_midjourney | MidJourney]] model's default, community-curated aesthetic is applied to the text prompt [00:31:20]. High stylize values (e.g., `--s 1000`) tend to produce images that "scream AI," while lower values (default 100) offer more creative leeway [00:32:00]. This is a key lever for avoiding the "classic MidJourney" look [00:34:01].

### [[personalization_and_style_reference_codes_in_midjourney | Personalization and Style Reference Codes]]

Personalization in [[ai_design_tools_like_runway_and_midjourney | MidJourney]] allows the model to fine-tune to a user's specific aesthetic preferences [00:31:31].
*   **Rating Images**: By consistently rating images in the "Personalized" tab, [[ai_design_tools_like_runway_and_midjourney | MidJourney]] learns preferences regarding colors, lighting, general style (photographic vs. illustrative), and even subject matter [00:29:37]. Rating thousands of images is highly recommended as a first step to improve all future generations [00:30:37].
*   **Blending Personalizations**: Users can even blend their personalization with others' or adjust its influence [00:34:57].

[[personalization_and_style_reference_codes_in_midjourney | Style reference codes]] (`--sref` followed by a number) are like coordinates in a multi-dimensional style space [00:37:31]. These codes, of which there are billions, direct [[ai_design_tools_like_runway_and_midjourney | MidJourney]] to a specific aesthetic location [00:38:01].
*   **Mining and Curating**: Users often "mine" these codes, find effective ones, and curate them into lists or "style reference books" [00:38:08].
*   **Aesthetic Recipes**: By combining `sref` codes, personalization, and text prompts, users can build "aesthetic recipes" [00:38:19].
*   **Blending Styles**: Multiple `sref` codes can be combined (e.g., `--sref <code1> <code2>`) to blend different aesthetics like "paint on a palette" [00:39:59]. Each code represents a complex set of attributes, including color, composition, lighting, texture, and pattern [00:40:19].
*   **Weighted Blending**: Specific weights can be applied to individual `sref` codes within a prompt (e.g., `--sref <code1>::2 <code2>::1`) to control their relative influence [00:44:45]. This allows for precise [[exploring_aesthetics_with_style_space_in_midjourney | exploration of aesthetics with style space]] and understanding *why* certain visual outcomes occur [00:45:12].

By understanding and manipulating these levers, users move beyond "playing the slot machine game" of random prompts and gain greater control over the aesthetic direction [00:45:24]. This approach brings new meaning to "steal like an artist" within the digital realm [00:46:01].

## The Future of AI Design

[[ai_design_tools_like_runway_and_midjourney | MidJourney]] provides a new way of blending aesthetics, allowing for complex and unique creations [00:47:28]. The speaker is actively working on physically manifesting latent space by building a lab to teach people how to use creative [[ai_design_tools_like_runway_and_midjourney | AI tools]] and bring digital creations to life through robots, printers, and editing stations [00:59:47]. The goal is to move digital art into physical manifestations, like painting a generated giraffe on a large canvas and exhibiting it [01:00:12].