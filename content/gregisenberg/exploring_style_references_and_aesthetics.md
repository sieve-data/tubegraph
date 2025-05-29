---
title: Exploring Style References and Aesthetics
videoId: h5nxat56wKI
---

From: [[gregisenberg]] <br/> 

Midjourney is considered a new medium entirely, acting as a different type of canvas and a different way of problem-solving in art creation <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. It offers not just paint, but [[aesthetics_in_software_design | entire aesthetics]] with layers and complexity that can be blended and balanced to find harmony <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Once a desired "recipe" or look is achieved, it can be infinitely prompted into <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Beyond Text Prompts
While words are useful, they only scratch the surface in Midjourney <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>. Using visuals to drive visuals, instead of semantics, allows for the explosion of [[aesthetics_in_software_design | aesthetics]] and style space into almost infinite directions <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>. This approach reduces reliance on the base model's interpretation of style tokens, enabling users to "pave their own lane" <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.

Previously, Midjourney primarily relied on structuring text prompts and describing every detail <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Recent developments have introduced:
*   **Style Space** <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>
*   **Style References** <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>
*   **Character References** <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>

These features expand [[aesthetics_in_software_design | aesthetics]] into an infinite universe, offering a more visual and engaging canvas than mere keyword blending <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.

### Why Use Midjourney?
Midjourney serves multiple purposes <a class="yt-timestamp" data-t="00:11:09">[00:11:09]</a>:
*   **Inspiration Tool**: It's excellent for generating ideas and creating mood boards, similar to Pinterest or Dribbble, but with more control <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. This makes it a great [[design_inspiration_and_workflow_organization | design inspiration and workflow organization]] tool.
*   **Production**: With features like the new editor, users can modify existing assets, outpaint, and add elements <a class="yt-timestamp" data-t="00:11:52">[00:11:52]</a>.
*   **Art Therapy/Fun**: Users can get lost in the creative process <a class="yt-timestamp" data-t="00:12:14">[00:12:14]</a>.
*   **Discovery Engine**: It helps explore new [[aesthetics_in_software_design | aesthetics]] and go down "rabbit holes" of discovery <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>.
*   **Creative Control**: It offers significant control over the creative output <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>.
*   **Asset Creation**: Ideas can be transformed into living, breathing design assets for websites, landing pages, or social media <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.

## Midjourney Web App vs. Discord
For optimal workflow, users should switch from Discord to the Midjourney web app (`midjourney.com`) <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. The web app is open to everyone <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.

## Finding Inspiration within Midjourney
The "Explore" tab on `midjourney.com` displays all publicly available generations <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **Public vs. Private**: Standard plans show public generations by default. Pro Plan users can enable "stealth mode" to prompt privately, which is important for client work or proprietary imagery <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. Stealth mode can be turned on in the settings panel of the prompt bar <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>.
*   **Searching**: Users can search for terms like "vintage poster" to find inspiration <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.
*   **Image Search**: Clicking the search icon on a liked image performs an image search, yielding similar subject matter and styles <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
*   **Using Prompts/Styles**: From the explore tab, users can choose to "use prompt" (copies the text prompt), "use style" (uses the image as a style reference), or "use as an image" (uses the image as an image prompt) <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

## Image Prompts vs. Style References
Understanding the distinction between image prompts and style references is crucial:
*   **Image Prompt**: When an image is dragged in as an "image prompt" (indicated by a "pict" icon), Midjourney tries to pull in the subject matter and actual pixels of that image <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>. Increasing its weight will integrate more elements from the image into the generation, potentially leading to "wonky" results if the goal is only style transfer <a class="yt-timestamp" data-t="00:20:45">[00:20:45]</a>.
*   **Style Reference (`--sref`)**: When an image is selected as a "style reference" (indicated by a paperclip icon), Midjourney attempts to understand and integrate the [[aesthetics_in_software_design | aesthetic]] qualities (like color, composition, lighting, texture, pattern) while decoupling them from the subject matter <a class="yt-timestamp" data-t="00:19:41">[00:19:41]</a>. This is the preferred method for transferring a visual style without pulling in literal elements from the reference image <a class="yt-timestamp" data-t="00:20:00">[00:20:00]</a>.

## Key Aesthetic Levers and Parameters
The "name of the game" in Midjourney is balance and harmony among various levers <a class="yt-timestamp" data-t="00:18:29">[00:18:29]</a>.

### 1. Style Weight (`--sw`)
This parameter determines how much influence a [[understanding_and_utilizing_style_weight | style reference]] has over the generation <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
*   Default: 100 <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>
*   Range: Up to 1000 <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>
*   Increasing `sw` makes the generation more likely to resemble the style reference <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. Lowering it gives more room for the text prompt and personalization <a class="yt-timestamp" data-t="00:48:55">[00:48:55]</a>.

### 2. Text Prompts
Even with style references, a well-crafted text prompt can provide assistance and guidance to the AI <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. For example, adding "a paper cutout illustration" to "giraffe" pushes the image generation towards the desired [[aesthetics_in_software_design | aesthetic]] <a class="yt-timestamp" data-t="00:18:10">[00:18:10]</a>.

### 3. Aspect Ratio (`--ar`)
This parameter controls the image layout, useful for specific formats like posters <a class="yt-timestamp" data-t="00:19:03">[00:19:03]</a>. For example, `--ar 2:3` is suitable for poster prints <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.

### 4. Editor Feature
The in-app editor allows users to paint out unwanted elements, like text <a class="yt-timestamp" data-t="00:26:28">[00:26:28]</a>. Midjourney is often good at understanding the intent to remove, but an explicit `--no` parameter can also be used <a class="yt-timestamp" data-t="00:26:38">[00:26:38]</a>.

### 5. Personalization (`--p`)
[[Personalization and Stylizing in AI Art | Personalization]] allows Midjourney to fine-tune its model to a user's specific [[aesthetics_in_software_design | aesthetic]] preferences <a class="yt-timestamp" data-t="00:30:27">[00:30:27]</a>.
*   **How to Activate**: Users can rate images in the "Personalize" tab by selecting their favorite image from a given set <a class="yt-timestamp" data-t="00:29:36">[00:29:36]</a>. The more images rated, the more Midjourney learns about preferences in color, lighting, general style (photographic vs. illustrative), and even subject matter <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.
*   **Effect**: Personalization significantly changes the output's [[aesthetics_in_software_design | aesthetic]] <a class="yt-timestamp" data-t="00:30:34">[00:30:34]</a>. It's highly recommended to rate at least a thousand images <a class="yt-timestamp" data-t="00:30:37">[00:30:37]</a>. It functions as an additional [[aesthetics_in_software_design | aesthetic]] lever that can be turned up or down <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.

### 6. Stylize (`--s`)
This parameter controls how much of the Midjourney model's default, community-curated [[aesthetics_in_software_design | aesthetics]] are applied to the text prompt <a class="yt-timestamp" data-t="00:31:17">[00:31:17]</a>.
*   Default: 100 <a class="yt-timestamp" data-t="00:31:58">[00:31:58]</a>
*   Range: Up to 1000 <a class="yt-timestamp" data-t="00:31:57">[00:31:57]</a>
*   High stylize values tend to produce images that "scream AI" or look distinctly "Midjourney" <a class="yt-timestamp" data-t="00:32:15">[00:32:15]</a>.
*   When [[personalization_and_stylizing_in_ai_art | personalization]] is active, the stylize parameter increases the influence of the user's personalized aesthetic preferences instead of the default Midjourney aesthetic <a class="yt-timestamp" data-t="00:32:41">[00:32:41]</a>.

### 7. Style Reference Codes (`--sref`)
These are unique codes that act as coordinates in a multi-dimensional "Style Space" <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>.
*   **Function**: They direct the AI to a specific [[aesthetics_in_software_design | aesthetic]] location, influencing anything prompted with that code <a class="yt-timestamp" data-t="00:37:42">[00:37:42]</a>.
*   **Vastness**: There are approximately 4.6 billion possible `sref` codes <a class="yt-timestamp" data-t="00:38:01">[00:38:01]</a>.
*   **Discovery**: Users can "mine" these codes, finding and curating the best ones into lists or "style reference books" <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>. Tools like a "style reference explorer" can help visually search for these codes based on style, vibe, or theme <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a>.
*   **Impact**: `sref` codes represent complex [[aesthetics_in_software_design | aesthetics]] including color, composition, lighting, texture, and pattern, which are balanced with text prompts and other parameters <a class="yt-timestamp" data-t="00:40:19">[00:40:19]</a>.

### 8. Blending Styles
Multiple `sref` codes can be combined in a prompt, acting like "paint on a palette" to blend different [[aesthetics_in_software_design | aesthetics]] <a class="yt-timestamp" data-t="00:39:59">[00:39:59]</a>. Users can adjust the weight of each style within the blend using `::` syntax (e.g., `sref1::2 sref2::1`) to prioritize one over the other <a class="yt-timestamp" data-t="00:44:35">[00:44:35]</a>.

### 9. Permutation Prompts
This feature allows users to test multiple parameter values in one go by placing them in brackets separated by commas (e.g., `--sw {50, 100, 200}`) <a class="yt-timestamp" data-t="00:49:17">[00:49:17]</a>. This helps quickly identify which level of a parameter produces the desired visual outcome <a class="yt-timestamp" data-t="00:49:30">[00:49:30]</a>.

## Workflow Tips
*   **Start Basic**: Begin with a simple subject and a style reference to understand Midjourney's interpretation <a class="yt-timestamp" data-t="00:16:12">[00:16:12]</a>.
*   **Iterate**: After initial results, make guided decisions: adjust style weight, refine text prompts, and experiment with aspect ratios <a class="yt-timestamp" data-t="00:16:36">[00:16:36]</a>.
*   **"Use Prompt" Shortcut**: Hover over a generated image and click "Use" to re-add its prompt to the prompt bar <a class="yt-timestamp" data-t="00:17:05">[00:17:05]</a>.
*   **Variations**: Explore "Variation Subtle" (keeps most details, subtle changes) and "Variation Strong" (more dramatic compositional changes) from a generated image <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>.
*   **Favorite Images**: Use the heart icon to "like" favorite images. This organizes them in the "Organize" tab, making them easy to find later among hundreds of generations <a class="yt-timestamp" data-t="00:27:19">[00:27:19]</a>.
*   **Keyboard Shortcut**: After running a prompt, hit the up arrow key to instantly populate the last prompt, saving time <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>.

## Future of AI Art and Midjourney
Midjourney, with its robust [[personalization_and_stylizing_in_ai_art | personalization and stylizing]] options, offers significant [[content_engagement_and_relevance_strategies | content engagement]] and relevance <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. The ability to control the [[aesthetics_in_software_design | aesthetic direction]] deeply contrasts with playing a "slot machine game" by just trying random prompts <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>. The current developments are pushing towards physically manifesting latent space, with plans for a lab in Red Hook for deep learning of creative AI tools and equipment to bring digital creations to life (e.g., robots painting, 3D printers) <a class="yt-timestamp" data-t="00:59:47">[00:59:47]</a>.