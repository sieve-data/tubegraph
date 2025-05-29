---
title: Balancing aesthetics with text prompts and style references
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

Midjourney is described as an entirely new medium, a different type of canvas for problem-solving. It offers a way to blend and balance entire aesthetics with layers and complexity to achieve desired artistic outcomes <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Beyond Text Prompts: The Power of Visuals

While words are still valuable in Midjourney prompts, they are "the tip of the iceberg" <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Using visuals to drive visuals, as opposed to semantics, allows for an explosion of aesthetics and style space in infinite directions <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This approach reduces reliance on the base model's interpretation of style tokens, enabling users to "pave their own lane" <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Newer features like Style Space, style references, and character references have transformed the process from merely structuring text prompts to a more visual, playful canvas <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

## Midjourney Web App and Workflow Tips

It is highly recommended to use the Midjourney web app (`midjourney.com`) instead of Discord for generating images <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Privacy and Stealth Mode
By default, generations on Midjourney are public if an account is on the Standard Plan or below <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. For client work or proprietary imagery, it is crucial to be on the Pro Plan or above and enable "stealth mode" in the settings to prevent assets from appearing in the public database <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>.

### Finding Inspiration
Inspiration can be found on platforms like Reddit, Pinterest, or through Google image searches <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. The Midjourney explore tab also serves as a vast library of publicly available generations <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. Users can search for specific themes (e.g., "vintage poster") <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>. If a particular image's style is appealing, a search icon can be used to find similar results based on subject matter and style <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. Options like "use prompt," "use style," or "use image" allow direct application of existing generations <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Benefits of Midjourney
Midjourney functions as a powerful inspiration tool, excellent for quickly jamming out ideas, building mood boards, and developing concepts <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. It offers more control over the generated visuals compared to traditional image searches <a class="yt-timestamp" data-t="00:11:38">[00:11:38]</a>. It can be used in production, especially with the editor feature which allows out-painting and adding new elements to existing assets <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>. For many, it's also a form of art therapy <a class="yt-timestamp" data-t="00:12:16">[00:12:16]</a>. The platform excels as a "discovery engine" for exploring aesthetics <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.

### Workflow Enhancements
*   **Liking Favorites**: Users should "like" their favorite generations by clicking the heart icon or right-clicking. This helps organize the library and easily find preferred images later, as hundreds of generations can accumulate quickly <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.
*   **Keyboard Shortcut**: After hitting enter, pressing the up arrow on the keyboard automatically populates the prompt bar with the last run prompt, saving time <a class="yt-timestamp" data-t="00:36:11">[00:36:11]</a>.

## Incorporating Visuals for Aesthetic Control

### Style References vs. Image Prompts
When uploading an image to a prompt, there's a crucial distinction between an "image prompt" (pict icon) and a "style reference" (paperclip icon) <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.
*   **Image Prompt**: When an image is used as an image prompt, Midjourney attempts to pull in the subject matter and actual pixels from the original image <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>. Increasing the image weight (`--iw`) will make Midjourney try to include more elements from the image, potentially leading to "wonky" results if the goal is only aesthetic transfer <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>.
*   **Style Reference**: As a style reference, Midjourney analyzes the image to understand its aesthetic qualities (e.g., colors, composition, lighting, texture, pattern) and then integrates those elements into new generations, decoupling aesthetic from subject matter <a class="yt-timestamp" data-t="00:15:55">[00:15:55]</a>.

### Aesthetic Levers and Parameters
The core of using Midjourney involves balancing various "aesthetic levers":

*   **Style Weight (`--sw`)**: This parameter determines how much influence a style reference has over the generation. The default is 100, but it can go up to 1000, making the generation more likely to resemble the style reference <a class="yt-timestamp" data-t="00:17:18">[00:17:18]</a>.
*   **Text Prompt Refinement**: Providing a clear text prompt, such as "a paper cutout illustration of a giraffe," helps guide Midjourney when combined with a style reference, leading to more consistent results <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.
*   **Aspect Ratio (`--ar`)**: Adjusting the aspect ratio (e.g., `--ar 2:3` for a poster print) helps guide the composition and how the image fills the space <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>.
*   **Negative Prompting (`--no`)**: Using `--no` followed by a keyword (e.g., `--no text`) can tell Midjourney what elements to remove from the generation <a class="yt-timestamp" data-t="00:26:52">[00:26:52]</a>.
*   [[using_style_references_and_personalization_in_midjourney | Personalization]]**: Users can fine-tune the Midjourney model to their aesthetic preferences by rating images in the "personalize" tab (found under "start teaching") <a class="yt-timestamp" data-t="00:29:37">[00:29:37]</a>. The more images rated, the more Midjourney learns about preferred colors, lighting, style (photographic vs. illustrative), and even subject matter <a class="yt-timestamp" data-t="00:30:21">[00:30:21]</a>. This drastically changes the aesthetics of generations, often making "everything better" <a class="yt-timestamp" data-t="00:30:44">[00:30:44]</a>.
*   **Stylize (`--s`)**: This parameter controls how much of Midjourney's default, community-curated aesthetic is applied to a text prompt <a class="yt-timestamp" data-t="00:31:20">[00:31:20]</a>. A high stylize value (e.g., `--s 1000`) can make images look "super in-your-face AI," while lower values (default 100) offer more creative leeway <a class="yt-timestamp" data-t="00:32:10">[00:32:10]</a>. When [[using_style_references_and_personalization_in_midjourney | personalization]] is turned on, the `stylize` parameter increases the influence of the user's fine-tuned aesthetic <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.

## Advanced Aesthetic Exploration: SRF Codes

Style reference codes (SRF codes) are like coordinates in a multi-dimensional "Style Space" that direct generations to a specific aesthetic location <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>. There are billions of possible SRF codes <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>. People are "mining" these codes, curating them into lists, and building "aesthetic recipes" by mixing them with personalization and text prompts <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.

SRF codes can be found and explored visually using tools like a style reference explorer <a class="yt-timestamp" data-t="00:36:53">[00:36:53]</a>.

### Blending Styles Like Paint
SRF codes and style references can be thought of as "paint on a palette" <a class="yt-timestamp" data-t="00:40:05">[00:40:05]</a>. Unlike simple paint colors, these styles represent complex attributes like color, composition, lighting, texture, and pattern <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>. They can be blended together by including multiple SRF codes or style references in a single prompt <a class="yt-timestamp" data-t="00:41:39">[00:41:39]</a>.

### Weighting Styles
The influence of individual SRF codes within a blend can be controlled using the `::` syntax (e.g., `srf_code_1::2 srf_code_2::1`) to indicate relative importance, allowing for experiments with different balances <a class="yt-timestamp" data-t="00:44:36">[00:44:36]</a>.

### Using Permutation Prompts
To quickly test different parameter values (like style weights or stylize values), a permutation prompt can be used by putting values in brackets separated by commas (e.g., `--sw {50,100,200}`) <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>. This runs multiple generations at once, allowing for rapid visual comparison of outcomes <a class="yt-timestamp" data-t="00:49:36">[00:49:36]</a>.

## Conclusion

The "name of the game" in Midjourney is balance and harmony <a class="yt-timestamp" data-t="00:28:29">[00:28:29]</a>. By understanding and manipulating the various "aesthetic levers"—style references, text prompts, parameters, and [[using_style_references_and_personalization_in_midjourney | personalization]]—users can guide and push aesthetics in desired directions <a class="yt-timestamp" data-t="00:31:31">[00:31:31]</a>. This allows for a creative process beyond simply playing a "slot machine game" of random prompts, enabling a more controlled exploration of unique aesthetic recipes <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.

The Midjourney editor can be used to refine generated images by, for example, adjusting aspect ratios or removing elements <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.

Ultimately, Midjourney provides a new way of problem-solving where entire aesthetics can be blended, balanced, and infinitely re-prompted to create unique, high-quality art <a class="yt-timestamp" data-t="00:46:09">[00:46:09]</a>. This moves beyond the limitations of text-only prompting, as visuals offer a far more complex and rich input <a class="yt-timestamp" data-t="00:46:56">[00:46:56]</a>.

There is a lab being built in Red Hook in partnership with Pioneer Works to physically manifest latent space, allowing creators to learn and use creative AI tools and equipment (robots, 3D printers, editing stations) to bring their digital art to life <a class="yt-timestamp" data-t="00:59:47">[00:59:47]</a>.