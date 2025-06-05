---
title: Using extensions and snippets in VS Code
videoId: u21W_tfPVrY
---

From: [[fireship]] <br/> 

[[modern_code_editors_like_visual_studio_code_and_jetbrains | Visual Studio Code]] (VS Code) has become the most popular code editor among developers since its inception, as indicated by the Stack Overflow 2018 survey <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. It is known for being minimal, powerful, free, and open-source <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. A significant part of its power comes from its extensibility and ability to use code snippets.

## Enhancing Productivity with Extensions

[[vs_code_extensions_for_productivity | VS Code extensions]] allow users to customize their coding experience and integrate additional functionalities.

### Navigation and Bookmarking
For quickly navigating specific lines of code, a bookmark plugin can be used to highlight a block of code, set a bookmark number, and then easily navigate to it later via the [[command_palette_usage_in_vs_code | Command Palette]] <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

### Code Generation with Snippets
[[custom_snippets_and_boilerplate_code_in_vs_code | Custom Snippets and Boilerplate Code in VS Code]] are highly effective for generating repetitive code.
*   **Installation**: Snippets can be installed to automatically generate boilerplate code <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.
*   **Angular Snippets**: For Angular projects, popular snippet libraries are available from Mike Moreland and John Papa, which can be used together <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   **[[vs_codes_integrated_terminal_and_intellisense | IntelliSense]] Integration**: Once installed, snippets are automatically added to [[vs_codes_integrated_terminal_and_intellisense | VS Code's IntelliSense]] <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. For example, typing a prefix from a snippet library can generate tedious code like an `NG switch` statement <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   **Library Support**: Snippets are also available for specific libraries like Angular Material and ng XS <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

### Type Definition Generation
An extension called "Paste JSON as Code" simplifies working with APIs that return JSON <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>. Users can copy a JSON example response, paste it into a file, and then use the [[command_palette_usage_in_vs_code | Command Palette]] to trigger the "paste JSON as code" command. This will magically generate a full set of interfaces to model the API response, providing strong typing and developer tooling for any API <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.

### Debugging Capabilities
[[debugging_with_vs_code | Debugging with VS Code]] can be extended with specific extensions. For instance, the Chrome extension allows users to [[debugging_with_vs_code | debug]] Angular applications within the context of the Chrome browser <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

### Version Control Enhancement
For [[git_version_control_and_collaboration_tools_in_vs_code | Git version control and collaboration tools in VS Code]], an extension like GitLens significantly enhances the integrated [[git_version_control_and_collaboration_tools_in_vs_code | Git]] experience <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>. GitLens provides additional panels in the [[git_version_control_and_collaboration_tools_in_vs_code | Git]] tab for traversing the [[git_version_control_and_collaboration_tools_in_vs_code | Git]] tree, dealing with stashes, tags, and remote repositories <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>. It also annotates code directly, allowing users to hover over a piece of code to see who wrote it, when, and its commit ID <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

### Real-time Collaboration
VS Code Live Share is a feature that allows users to connect their GitHub or Azure account to VS Code and collaborate with multiple team members on a single document in real-time <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. It functions like Google Docs for coding <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. After installing the extension and connecting an account, users can click "share" to generate a link to pass to other team members <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.

### Other Utilities
For a more focused coding experience, "Zen mode" (activated by Ctrl + K Z) removes all distractions from the viewport <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>. Additionally, a Spotify extension can be installed to control music directly from VS Code <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>.