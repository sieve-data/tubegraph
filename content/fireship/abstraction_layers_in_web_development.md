---
title: Abstraction layers in web development
videoId: lHZwlzOUOZ4
---

From: [[fireship]] <br/> 

Abstraction layers in [[introduction_to_web_development | web development]] aim to simplify complex tasks and improve developer productivity by providing higher-level interfaces over more granular code. Tailwind CSS is a prominent example of such an abstraction, generating considerable debate within the development community.

## Tailwind CSS: An Abstraction for Styling

Tailwind CSS is a utility-first CSS framework that provides a set of pre-defined classes to style HTML elements directly in the markup <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>. It's often compared to other [[frontend_ui_libraries_and_frameworks | frameworks]] like Bootstrap, but with a different approach to customization <a class="yt-timestamp" data-t="02:51:53">[02:51:53]</a>. While some critics argue it's "not even real CSS" or equates to "blasphemous inline styles," many developers find it significantly improves workflow <a class="yt-timestamp" data-t="00:20:20">[00:20:20]</a>, <a class="yt-timestamp" data-t="01:42:07">[01:42:07]</a>, <a class="yt-timestamp" data-t="00:36:00">[00:36:00]</a>.

Many consider Tailwind CSS a [[web_application_tools_for_developers | tool]] that, similar to TypeScript or Svelte, makes it difficult to revert to previous methods due to the time savings it offers <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.

### Problems Solved by Tailwind CSS

Tailwind CSS addresses several common pain points associated with traditional CSS development, primarily by offering a different abstraction over its complexities:

*   **Co-location of Styles**
    Traditionally, CSS styles are separated from HTML markup to achieve a "separation of concerns" <a class="yt-timestamp" data-t="01:06:00">[01:06:00]</a>. This practice often leads to challenges in naming CSS classes and tracking which styles apply to specific elements, especially in larger projects or after some time <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>. Tailwind addresses this by placing utility classes directly within the HTML, ensuring styles are co-located with the elements they affect. This eliminates the need for arbitrary class names and clarifies exactly which styles apply to an element, allowing for safer modifications <a class="yt-timestamp" data-t="01:36:00">[01:36:00]</a>, <a class="yt-timestamp" data-t="01:52:00">[01:52:00]</a>.
    *   **Tip**: The Inline Fold VS Code extension can help minimize the visual impact of extensive utility classes in HTML <a class="yt-timestamp" data-t="02:03:00">[02:03:00]</a>.

*   **CSS Verbosity**
    Tailwind uses clever naming conventions, such as `inset-0`, to condense multiple lines of traditional CSS into a single utility class <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a>. This approach can reduce the total amount of CSS code by approximately one-third compared to vanilla CSS <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. Despite being an abstraction that requires learning new conventions, it aims to reduce the amount of code developers need to write <a class="yt-timestamp" data-t="02:38:00">[02:38:00]</a>.

*   **Balancing UI Control**
    CSS provides immense control over UI elements, which can be overwhelming, while opinionated [[frontend_ui_libraries_and_frameworks | frameworks]] like Bootstrap can be too difficult to customize without losing their signature look <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>. Tailwind strikes a balance by offering a standard set of constraints that help maintain a good UI appearance while remaining highly customizable for unique design requirements <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. Unlike Bootstrap, which often results in apps that look distinctly "Bootstrap," Tailwind's design language is less obvious <a class="yt-timestamp" data-t="03:03:00">[03:03:00]</a>. This positions it well in a [[comparison_of_web_development_frameworks | comparison of web development frameworks]].

*   **Eliminating Zombie Styles**
    Developers often write CSS that eventually goes unused, leading to bloated CSS bundles <a class="yt-timestamp" data-t="03:10:00">[03:10:00]</a>. Tailwind includes an automatic purging mechanism that removes all unused styles from the final build, effectively eliminating "zombie styles" and optimizing the CSS bundle size <a class="yt-timestamp" data-t="03:14:00">[03:14:00]</a>.

### Trade-offs and Considerations

While Tailwind CSS offers significant advantages, it also comes with trade-offs:

*   **Initial Setup Complexity**: Setting up Tailwind CSS involves several steps, including installing the Tailwind CLI, PostCSS, and a VS Code extension <a class="yt-timestamp" data-t="03:24:00">[03:24:00]</a>. For this reason, it may be better suited for larger projects rather than small demos, where lighter alternatives like Pico CSS (a classless CSS framework) might be more appropriate <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.
*   **Learning Curve**: It requires learning a new abstraction on top of standard CSS <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>.
*   **Bloated HTML**: The co-location of many utility classes can lead to HTML that initially appears "disgusting" or "bloated" <a class="yt-timestamp" data-t="01:42:00">[01:42:00]</a>.

Ultimately, the choice to use an abstraction like Tailwind CSS depends on individual preference and project requirements <a class="yt-timestamp" data-t="03:41:00">[03:41:00]</a>.