---
title: Git version control and collaboration tools in VS Code
videoId: u21W_tfPVrY
---

From: [[fireship]] <br/> 

[[modern_code_editors_like_visual_studio_code_and_jetbrains | Visual Studio Code]] significantly aids in [[developer_productivity_tools | developer productivity]] by streamlining Git version control and offering advanced collaboration features. Dealing with Git in large projects can be challenging from the command line, but VS Code provides an integrated and intuitive interface for these tasks <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>.

## Git Integration

VS Code automatically highlights files based on their Git status:
*   Untracked or new files appear green <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
*   Modified files are yellow <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>.
*   Files with linter errors are red <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Committing Changes
To commit changes, navigate to the Git tab, add your commit message, and you're done <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. This process eliminates the need to manually type `git add` or `git commit -m` commands in the command line <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.

### Managing Commits and Files
*   **Rollback Commit**: If a commit was made unintentionally, it can be rolled back from the options menu within the Git tab <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>.
*   **Other Git Commands**: Most other Git commands are accessible from this menu <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **Reverting File Changes**: To discard all changes made to a specific file, simply click the revert button <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
*   **Staging Individual Files**: For selective commits, click the plus button next to individual files to stage only those for the next commit <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

## GitLens Extension

For enhanced Git insights, the GitLens [[vs_code_extensions_for_productivity | extension]] is highly recommended <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **Additional Panel**: After installation, GitLens adds an extra panel to the Git tab, providing detailed Git data <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Navigation**: It simplifies traversing the Git tree and managing aspects like stashes, tags, and remote repositories <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   **Code Annotations**: GitLens annotates your code directly, allowing you to hover over a piece of code to see who wrote it, when it was written, and its commit ID <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

## VS Code Live Share

[[vs_code_extensions_for_productivity | VS Code Live Share]] is a significant collaboration feature that enables real-time collaborative coding <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>. It functions much like Google Docs for writing code <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.
*   **Account Connection**: To use Live Share, connect your GitHub or Microsoft account <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Real-time Collaboration**: It allows multiple team members to collaborate on a single document simultaneously <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
*   **Sharing**: Simply click "share," and VS Code will generate a link to share with other team members <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

Live Share has proven highly useful for collaborating on issues and working on app development strategies <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.