---
title: Comparison between Tailwind CSS and traditional CSS
videoId: lHZwlzOUOZ4
---

From: [[fireship]] <br/> 

The debate surrounding [[CSS Tools and Preprocessors | Tailwind CSS]] and its approach to styling user interfaces is a prominent topic in web development, with strong opinions on both sides <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The controversy escalated after a Tailwind snippet was posted on Twitter, leading to an "epic war" between its proponents and "unified [[CSS for styling and layout | CSS]] fundamentalists" <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Critics argue that [[CSS Tools and Preprocessors | Tailwind CSS]] is "not even real [[CSS for styling and layout | CSS]]" <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

Despite the criticisms, a poll revealed that while most developers haven't tried [[CSS Tools and Preprocessors | Tailwind CSS]], four out of five who have tried it love it <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The speaker personally adopted [[CSS Tools and Preprocessors | Tailwind CSS]] after initial skepticism, finding it similar to tools like TypeScript or Svelte in its ability to significantly save time and make returning to previous methods difficult <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

## Problems Solved by Tailwind CSS

[[CSS Tools and Preprocessors | Tailwind CSS]] aims to address several common issues encountered with traditional [[CSS for styling and layout | CSS]] approaches.

### 1. Co-location of Styles and Markup
Traditional [[CSS for styling and layout | CSS]] practices have historically advocated for separating styles from markup to achieve a "separation of concerns" <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. However, this approach often leads to difficulties:
*   **Naming Conventions**: Programmers must invent numerous arbitrary and often pointless names for [[CSS for styling and layout | CSS]] classes <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Maintainability**: Weeks later, it becomes challenging to recall which styles apply to which elements and what specific class names do <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
*   **Unintended Side Effects**: Changing a class name used in multiple places can inadvertently break other parts of the UI <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

[[colocation_of_styles_with_tailwind | Tailwind CSS addresses this by providing standard utility classes that are co-located directly within the HTML markup]] <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.
*   **Criticism**: This approach can result in "disgusting bloated HTML" that superficially resembles blasphemous inline styles <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. This is often the main deterrent for new users <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   **Benefits**: Developers no longer need arbitrary class names and can immediately see which styles apply to an element, reducing mental overhead <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>. Modifications can be made safely without impacting other parts of the application <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   **Pro Tip**: For Visual Studio Code users, the "inline fold" extension can automatically minimize the appearance of cluttered HTML <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

### 2. Verbosity of CSS
[[CSS for styling and layout | CSS]] can be verbose, requiring multiple lines of code for simple styling <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. [[CSS Tools and Preprocessors | Tailwind CSS]] is fundamentally built on [[CSS for styling and layout | CSS]] <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>; hovering over any [[tailwind_css_utility_class_approach | Tailwind class]] reveals the actual underlying [[CSS for styling and layout | CSS]] code <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Conciseness**: [[CSS Tools and Preprocessors | Tailwind CSS]] uses clever naming conventions, such as `inset-0`, to combine multiple [[CSS for styling and layout | CSS]] properties and values into a single line, achieving in one line what might take six lines of traditional [[CSS for styling and layout | CSS]] <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.
*   **Code Reduction**: It's estimated that [[CSS Tools and Preprocessors | Tailwind CSS]] can reduce the total amount of styling code to approximately one-third of what would be needed with vanilla [[CSS for styling and layout | CSS]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. The "best type of code is the code you never have to write" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
*   **Criticism**: A valid concern is that developers must learn an abstraction layer on top of [[CSS for styling and layout | CSS]], which is not ideal, as native platform usage is generally preferred <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>.

### 3. Control and Customization
Traditional [[CSS for styling and layout | CSS]] provides excessive control over the UI <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>, while other frameworks like Bootstrap can be difficult to customize <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a> and often result in apps that visibly resemble Bootstrap <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>.
*   **Balanced Approach**: [[customizing_the_tailwind_configuration | Tailwind CSS strikes a balance by offering a standard set of constraints]] that help ensure a good-looking UI, while also being significantly easier to customize to fit any design <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### 4. Zombie Styles (Unused CSS)
Developers often write [[CSS for styling and layout | CSS]] styles that are never actually used, leading to unnecessary bloat in the [[CSS for styling and layout | CSS]] bundle <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.
*   **Automatic Purging**: [[automatic_style_purging_with_tailwind | Tailwind CSS automatically purges all unused styles]], effectively removing this "dead code" and shrinking the final bundle size <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.

## Trade-offs and Considerations

While offering numerous [[benefits_and_drawbacks_of_tailwind_css | benefits]], [[CSS Tools and Preprocessors | Tailwind CSS]] also has drawbacks:
*   **Setup Complexity**: [[CSS Tools and Preprocessors | Tailwind CSS]] can be "heavy-handed" to set up, requiring multiple steps, including installing the Tailwind CLI, PostCSS, and a VS Code extension <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Project Suitability**: Due to its setup, [[CSS Tools and Preprocessors | Tailwind CSS]] is typically recommended for larger projects <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. For smaller demonstrations, alternatives like Pico [[CSS for styling and layout | CSS]] (which offers a classless approach for quick styling) might be more suitable <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

Ultimately, the choice to use [[CSS Tools and Preprocessors | Tailwind CSS]] or not comes down to personal preference and project needs <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. "If you like [[CSS Tools and Preprocessors | Tailwind CSS]], use it. If you don't like [[CSS Tools and Preprocessors | Tailwind CSS]], don't use it. Nobody cares" about your technology choices <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.