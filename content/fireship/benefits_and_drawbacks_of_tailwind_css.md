---
title: Benefits and drawbacks of Tailwind CSS
videoId: lHZwlzOUOZ4
---

From: [[fireship]] <br/> 
This article discusses the benefits and drawbacks of [[comparison_between_tailwind_css_and_traditional_css | Tailwind CSS]], a utility-first CSS framework, as of January 16, 2023 <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Overview and Reception
Tailwind CSS has sparked significant debate, with some critics even stating it's "not even real CSS" <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Despite the controversy, a poll indicated that four out of five people who have tried Tailwind love it <a class="yt-timestamp" data-t="00:00:35">[00:00:35]</a>. The tool is open-source and free <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Its advocates, including the speaker, find it akin to tools like TypeScript or Svelte, making it hard to revert to previous methods due to significant time savings <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. However, it's acknowledged that Tailwind has trade-offs and may not be suitable for every project <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## Problems Tailwind Solves

### 1. The Co-location Problem
Traditionally, CSS is separated from markup for a "separation of concerns" <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. However, this often leads to challenges:
*   **Arbitrary Naming**: Programmers face the difficulty of creating numerous arbitrary class names <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Maintenance Difficulty**: Weeks later, it's hard to remember what class names do, making it difficult to determine which styles apply to which elements <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>.
*   **Unintended Breakage**: Changing a class name used in multiple places can inadvertently break other parts of the UI <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

[[colocation_of_styles_with_tailwind | Tailwind's Solution]] addresses this by providing [[tailwind_css_utility_class_approach | standard utility classes]] that are [[colocation_of_styles_with_tailwind | co-located directly in the HTML]] <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Benefit**: Eliminates arbitrary class names, allowing developers to immediately know which styles apply to an element <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>. This clears mental overhead and enables safe modifications without breaking other parts of the application <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   **Pro Tip**: The Inline Fold VS Code extension can minimize the appearance of "bloated HTML" <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### 2. Verbosity of CSS
CSS can be verbose, requiring multiple lines for simple styles <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.
*   [[tailwind_css_utility_class_approach | Tailwind's Solution]]: It uses clever naming conventions, such as `inset 0`, to achieve in one line what might take six lines of standard CSS <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Benefit**: This approach can reduce the total amount of code to approximately one-third compared to vanilla CSS <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.

### 3. Excessive Control and Customization Issues
While raw CSS offers too much control, leading to inconsistent UIs, frameworks like Bootstrap can be too difficult to customize, resulting in generic-looking applications <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   [[customizing_the_tailwind_configuration | Tailwind's Solution]]: Tailwind provides a standard set of constraints that ensure the UI looks good, while being much easier to customize to accommodate any design <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>. This allows for unique designs, unlike Bootstrap apps which often have a recognizable look <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### 4. Zombie Styles (Unused CSS)
Developers often write CSS that is never actually used, leading to an unnecessarily bloated CSS bundle <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>.
*   [[automatic_style_purging_with_tailwind | Tailwind's Solution]]: Tailwind automatically purges all unused styles, eliminating "dead code" <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Drawbacks

*   **Initial Appearance**: The [[colocation_of_styles_with_tailwind | co-location of styles]] in HTML can initially appear as "disgusting bloated HTML" or "blasphemous inline styles," which is often the main turn-off for new users <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.
*   **Learning Abstraction**: Users must learn an abstraction on top of CSS, which is not ideal, as it's generally best to use web platforms natively <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.
*   **Heavy Setup**: Tailwind is considered a "heavy-handed approach" requiring about five steps for setup, including installing the Tailwind CLI, PostCSS, and a VS Code extension <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

## Use Cases
Due to its setup complexity, Tailwind is generally recommended for larger projects <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. For smaller demos, classless CSS frameworks like Pico CSS can be used to achieve good aesthetics with zero effort <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Conclusion
Ultimately, the choice to use Tailwind CSS is a personal one <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. "If you like Tailwind, use it. If you don't like Tailwind, don't use it. Nobody cares, literally nobody cares about your technology choices except you" <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.