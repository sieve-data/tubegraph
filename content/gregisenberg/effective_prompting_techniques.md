---
title: Effective Prompting Techniques
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

Midjourney is described as an entirely new medium, a different type of canvas, and a distinct way of problem-solving [00:00:01]. Unlike traditional art, it allows users to blend and balance entire aesthetics with complex layers, finding harmony to achieve desired results [00:00:10]. Once a desired "recipe" or style is discovered, it can be infinitely prompted into [00:00:24].

## Leveraging Visuals Over Text

Initially, Midjourney primarily relied on text prompts [00:01:55]. However, the tool has evolved, enabling users to do much more by using visuals to drive visuals, as opposed to semantics (words) to drive visuals [00:01:12]. This approach allows for an "explosion" of aesthetics and style into almost infinite directions, reducing reliance on the base model's interpretation of style tokens [00:01:16].

> "Words are great, words are still great, don't get me wrong, but they're they're just the tip of the iceberg here. We can really do a lot more when we're using visuals to drive visuals as opposed to semantics to drive visuals." <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>

## Using the Midjourney Web App

For optimal use, it is recommended to transition from Discord to the Midjourney web app (`midjourney.com`) [00:06:36]. The web app offers a more streamlined and efficient workflow for creating and managing generations [00:06:46].

## Finding Inspiration

Inspiration can be found both outside and inside Midjourney:
*   **External Sources:** Platforms like Reddit, Pinterest, Google Images, or Dribbble can be used to find images like old posters [00:05:41].
*   **Midjourney Explore Tab:** The "Explore" tab in the Midjourney web app showcases all publicly available generations, serving as a vast library of inspiration [00:07:07]. Users can search for specific styles, such as "vintage poster," and if they like a particular image's style, they can use its prompt or style directly [00:07:36].

> [!TIP] Stealth Mode
> If generating content for clients or brands that requires privacy, ensure your Midjourney account is on the Pro Plan or above, and **Stealth Mode** is turned on in the settings to prevent assets from showing up in the public database [00:10:26].

## Why Use Midjourney?

Midjourney is a powerful tool with various applications [00:11:12]:
*   **Inspiration and Ideation:** It serves as a discovery engine for generating and exploring ideas, similar to building a mood board but with more control [00:11:16].
*   **Production:** With features like the new editor, existing assets can be enhanced through outpainting and adding new elements [00:11:52].
*   **Creative Control:** It offers significant creative control over the artistic outcome [00:13:38].
*   **Art Therapy/Fun:** Many users find the process enjoyable and even therapeutic [00:12:14].

## Image Prompts vs. Style References

A crucial distinction in Midjourney is between an image prompt and a style reference [00:14:24]:

*   **Image Prompt (Default):** When an image is dragged into the prompt bar, it defaults to an image prompt, indicated by a "pict" icon [00:14:20]. In this mode, Midjourney attempts to pull in the subject matter and actual pixels of the image, which can lead to "wonky" results if the goal is only to replicate style [00:20:13]. Increasing the image weight (`--iw`) parameter will make Midjourney pull more elements from the image [00:20:45].
*   **Style Reference (`--sref`):** Indicated by a "paperclip" icon [00:14:35]. This is the preferred method for applying an aesthetic. Midjourney will analyze the image to understand its inherent style (e.g., color, composition, lighting, texture, pattern) and then integrate those elements into the generation, decoupling aesthetic from subject matter [00:19:41].

> [!WARNING] Important Distinction
> Be aware that by default, an image dragged into the prompt is an image prompt. It's crucial to manually change it to a style reference (paperclip icon) if you want to influence the *style* rather than the subject matter or content of the image [00:21:17].

## Aesthetic Levers: Parameters and Personalization

Midjourney offers various "aesthetic levers" (parameters) that can be pulled to guide and push the aesthetic in different directions [00:29:03]. The goal is to learn how to balance and find harmony between them [00:18:41].

### Core Parameters

*   **Style Weight (`--sw`):** Determines how much influence a style reference image has over the generation [00:17:20]. The default is 100, but it can go up to 1000 for stronger influence [00:17:36].
    *   Example: `--sw 1000` (for high style influence) [00:17:42]
*   **Aspect Ratio (`--ar`):** Sets the desired aspect ratio of the image, useful for specific outputs like posters [00:19:03].
    *   Example: `--ar 2:3` (for a poster print layout) [00:19:14]
*   **No Parameter (`--no`):** Tells Midjourney what elements to remove from the generation [00:26:52].
    *   Example: `--no text` (to remove text) [00:27:00]
*   **Stylize (`--s`):** Controls how much of the Midjourney model's default, community-curated aesthetics are applied to the text prompt [00:31:20]. High values (e.g., 1000) will make the image look more "AI-generated" or "Midjourney-like," while lower values (default is 100) offer more creative leeway and a balanced look [00:32:00].

### Personalization

Midjourney offers a "personalization" feature that fine-tunes the model to a user's aesthetic preferences [00:31:31].
*   **How to Activate:** Go to the "Personalize" tab and start teaching the model by rating images (liking favorites) [00:29:45]. The more images rated, the more the model learns about preferences in colors, lighting, style (photographic vs. illustrative), and even specific subjects [00:30:13].
*   **Impact:** Activating personalization changes the default aesthetic of generations to align with the user's learned preferences, creating a "totally different universe" [00:32:50]. This is a highly recommended first step for new users [00:30:34].

### Blending Personalizations

It is possible to blend personalizations, either your own with others or a weighted mix, using syntax like `--s Tatiana::3 --s MyPersonalization::2` to control the influence of each [00:35:09].

## Style Reference Codes (`--sref`)

Style reference codes are a powerful feature for exploring Aesthetics [00:37:16].
*   **What they are:** These codes act like "coordinates" in a "multi-dimensional Style Space," directing Midjourney to a specific aesthetic location [00:37:31]. Anything prompted will be influenced by that location's aesthetics [00:37:44].
*   **Finding and Using:** Users can find these codes (e.g., `SRE random_number`) through tools like the Style Reference Explorer, which allows visual exploration of 40,000+ images and 15,000+ style references [00:37:01].
*   **Blending Styles:** Multiple `--sref` codes can be combined in a single prompt to blend different aesthetic influences [00:41:39]. These styles represent not just color but also composition, lighting, texture, and pattern [00:40:19]. Weighted blending (e.g., `--sref 1234::2 --sref 5678::1`) can be used to emphasize one style over another [00:44:50].

> [!QUOTE]
> "This is where you really start to get into the weeds here and do the cool that you just can't do literally anywhere else. It's just like a whole new way of blending." <a class="yt-timestamp" data-t="00:47:19">[00:47:19]</a>

## Workflow and Exploration

A basic process for exploring an aesthetic in Midjourney involves:
1.  **Start Simple:** Begin with a basic subject (e.g., "giraffe") and a style reference [00:15:46].
2.  **Interpret Results:** Observe how Midjourney interprets the style reference and identify areas for refinement (e.g., photorealism vs. illustration) [00:16:28].
3.  **Adjust Parameters:** Use parameters like `style weight` and add descriptive text to guide the aesthetic [00:17:18].
4.  **Experiment with Aspect Ratios:** Change the aspect ratio for desired layouts (e.g., poster print) [00:19:03].
5.  **Utilize Variations:** Generate subtle or strong variations of promising results [00:25:35].
6.  **Refine with Editor:** Use the in-app editor to make precise changes, like painting out unwanted elements [00:26:29].
7.  **Explore Style Space:** Experiment with blending multiple style references and personalization, playing with their weights to find the desired balance and harmony [00:29:21].
8.  **Permutation Prompts:** Use bracketed, comma-separated values in prompts (e.g., `--sw [50, 100, 500, 1000]`) to quickly test multiple parameter values at once and visually compare results [00:49:17].

## Managing Generations

*   **Liking Favorites:** Always "like" your favorite generations (using the heart icon or right-click) [00:27:22]. This makes it significantly easier to find specific images later in the "Organize" tab by filtering for "liked" items [00:27:49].

## The Future of AI Art

The intersection of AI with physical art is an emerging area. The "physically manifesting latent space" concept involves using creative AI tools with equipment like painting robots, 3D printers, and plotter printers to bring digital creations to life [00:59:51]. This includes exploring image-to-video models to make static images move and become dynamic pieces [01:00:31].

> [!QUOTE]
> "I think of Midjourney as like a new medium entirely... you have not just paint but you have like entire aesthetics that have all of these layers and this complexity and you're blending them and you're balancing them and you're finding this harmony in between to get somewhere that you really love. And once you get that, once you find that little recipe, you can infinitely prompt into it." <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>

This approach allows for a deeper exploration beyond just [[prompting_techniques_for_aigenerated_content | basic prompting techniques]], providing greater creative control and the ability to build and refine unique artistic "recipes" [00:46:46]. It is a powerful tool for [[aiassisted_writing_processes_and_frameworks | AI-assisted writing processes and frameworks]] and [[business_applications_of_ai_prompting | business applications of AI prompting]], enabling effective [[designing_with_ai_prompt_clarity | design with AI prompt clarity]] and [[tips_for_effective_aidriven_marketing_strategies | AIdriven marketing strategies]]. The process encourages [[content_engagement_and_relevance_strategies | content engagement and relevance strategies]] by allowing users to delve into [[sequential_prompting_with_ai_tools | sequential prompting with AI tools]] and explore aesthetics as if they were [[implementing_reusable_modular_prompts_in_ai_projects | reusable modular prompts in AI projects]]. This systematic exploration, rather than a "slot machine game," allows for more specific and intentional creative outcomes [00:45:24]. It also relates to [[ai_prompting_with_reasoning_models | AI prompting with reasoning models]] by allowing users to observe and react to how the AI interprets instructions.