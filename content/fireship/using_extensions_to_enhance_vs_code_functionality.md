---
title: Using extensions to enhance VS Code functionality
videoId: ifTF3ags0XI
---

From: [[fireship]] <br/> 

Visual Studio Code (VS Code) is a powerful tool for developers, offering a wide array of [[Productivity tips for Visual Studio Code | productivity boosting features]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a> that allow users to [[Efficient navigation and code editing in VS Code | write and analyze code faster]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. Beyond its core capabilities, VS Code's functionality can be significantly enhanced through the use of extensions.

## Leveraging Extensions for Enhanced Productivity

The less reliance on the mouse, the more efficient one becomes in VS Code <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. While the mouse makes the tool approachable, it's not the most efficient way to work <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. Everything done with the mouse can likely be done quicker with the keyboard <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. The [[VS Code keyboard shortcuts and commands | Command Palette]] <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a> (Ctrl+P) is key to accessing VS Code's power from the keyboard, including commands for extensions, without memorizing numerous keybindings <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

## Key Extensions for Developers

Several extensions are highlighted as significantly enhancing VS Code's capabilities:

### Quokka

Quokka is an extension that automatically runs JavaScript code in the background and appends the output directly in your editor <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This feature facilitates rapid prototyping when the goal is to write plain JavaScript code <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Auto Rename Tag

The Auto Rename Tag extension automatically renames the closing HTML tag when you edit the opening tag, and it can work in other languages beyond just HTML <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>.

### Add JSDoc Comments

The Add JSDoc Comments extension allows users to highlight a function and then use the [[VS Code keyboard shortcuts and commands | Command Palette]] <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a> to automatically add a JSDoc comment to it <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>. This helps in adhering to the JSDoc standard for comments <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>. JSDoc comments can also include `link` tags to symbols in source code, allowing hovering for comments and clicking to navigate to that part of the code <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

### Better Comments

The Better Comments extension provides automatic highlighting for comment text <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. For example, lines starting with "bang" are red, and "to-do's" are highlighted orange <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.

### GitLens

For projects involving multiple developers and complex Git operations, the GitLens extension is highly recommended <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. It offers additional ways to visualize and explore your code, including showing who made specific changes <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>. This complements [[Using VS Code with Git | VS Code's built-in source control tab]] <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>, which provides a breakdown of changes, allows staging files by pointing and clicking, and lists possible Git commands from a drop-down menu <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### Remote Development Extensions

Microsoft provides a suite of remote development extensions that transform VS Code into a full-blown integrated development environment <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>:

*   **Remote Repositories**: This extension allows you to work with Git repositories hosted on GitHub without needing to clone them to your local system <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. You can log in with your GitHub account and contribute to any repo directly from VS Code, including creating new branches, editing code, and submitting pull requests <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>. This is part of [[Version control and remote development in VS Code | version control and remote development features]] <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Remote SSH**: This extension enables connecting to a remote server <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Remote Containers**: This allows you to use a Docker container as your development environment instead of your local system <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Paste JSON as Code

The Paste JSON as Code extension is particularly useful for TypeScript developers <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. It takes a JSON object and automatically infers TypeScript types using a tool called QuickType, potentially saving hours of work <a class="yt-timestamp" data-t="00:10:41">[00:10:41]</a>.

## Code Snippets and Refactoring

While you can create custom snippets within VS Code <a class="yt-timestamp" data-t="00:09:39">[00:09:39]</a>, the extensions panel is a good place to look for pre-built snippets for popular frameworks that can meet your needs without needing to create your own <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

For safely renaming code, instead of a dangerous find-and-replace across a whole project, VS Code allows you to find all references or implementations of a symbol by right-clicking it <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>. From there, you can use the "Rename Symbol" option to safely rename it across all your files <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.