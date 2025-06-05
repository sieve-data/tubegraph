---
title: Version control and remote development in VS Code
videoId: ifTF3ags0XI
---

From: [[fireship]] <br/> 

Visual Studio Code (VS Code) is a powerful editor that can be transformed into a full-blown Integrated Development Environment (IDE) with its advanced features and [[Using extensions to enhance VS Code functionality | extensions]] <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. While VS Code functions as a simple text editor, it contains numerous [[productivity_tips_for_visual_studio_code | productivity-boosting features]] that can help users write and analyze code faster <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

<br>

## Opening VS Code Projects

To open a directory or edit a file quickly from the terminal, users can leverage the VS Code Command Line Interface (CLI) using the `code` command <a class="yt-timestamp" data-t="00:00:55">[00:00:55]</a>. For Mac or Linux users, it's necessary to first add the binary to the system's path <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.

<br>

## Version Control with Git

[[Version Control Basics with Git | Git]] commands can be complex and potentially dangerous if misused <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>. However, VS Code provides a more intuitive, mouse-friendly interface for Git operations in its Source Control tab <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

Within the Source Control tab, users can see a breakdown of all changes in their current working directory <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. Files can be easily staged by pointing and clicking <a class="yt-timestamp" data-t="00:08:08">[00:08:08]</a>. Icons next to each file indicate whether it has been modified, added, or removed <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

A dropdown menu offers a list of all possible Git commands, simplifying common tasks like committing files without needing to consult documentation <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### GitLens Extension

For complex projects involving multiple developers, the GitLens extension is highly recommended <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. This extension provides additional ways to visualize and explore code history, including identifying who made specific changes <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.

<br>

## Remote Development Capabilities

VS Code offers powerful remote development features through dedicated [[Using extensions to enhance VS Code functionality | extensions]]:

### Remote Repositories Extension

Traditionally, working with a Git repository on GitHub required cloning it to a local system <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. The Remote Repositories extension streamlines this process <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

Once installed, users can click an icon in the bottom-left corner of VS Code to open a remote repository <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>. After logging in with a GitHub account, developers can contribute to any GitHub repository without dealing with complex [[version_control_basics_with_git | Git commands]] <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This includes creating new branches, editing code, and submitting pull requests, all within VS Code <a class="yt-timestamp" data-t="00:09:08">[00:09:08]</a>.

### Other Remote Extensions

Beyond remote repositories, other extensions enhance remote development:

*   **Remote SSH**: Allows connecting to a remote server <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Remote Containers**: Enables using a Docker container as the development environment instead of the local system <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

These Microsoft-managed [[using_extensions_to_enhance_vs_code_functionality | extensions]] elevate VS Code from a basic text editor to a comprehensive integrated development environment <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.