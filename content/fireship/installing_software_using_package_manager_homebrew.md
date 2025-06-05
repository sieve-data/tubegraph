---
title: Installing software using package manager Homebrew
videoId: r_MpUP6aKiQ
---

From: [[fireship]] <br/> 

Homebrew is a package manager used for automating software installation and management on macOS and Linux. It provides an automated way to install software, keeping track of what it has installed and helping to keep everything up to date <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. Homebrew can install various types of software, from command-line tools to full-blown applications <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

## Key Components of Homebrew <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>

*   **Taps:** These are repositories where Homebrew stores its own software and information about other software it can install <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **Brews:** These are typically command-line tools used within your shell <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Homebrew can also upgrade pre-installed software, ensuring everything is up to date <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.
*   **Casks:** These are full-blown applications that you might recognize <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

## Managing Installed Software with a Brewfile <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>

Homebrew can output a list of the software it has installed <a class="yt-timestamp" data-t="00:10:35">[00:10:35]</a>. This list can be saved to a `Brewfile`, which can then be used to reinstall all your software at a later date, such as when [[steps_to_bootstrap_a_new_computer_with_a_dotfiles_repository | bootstrapping a new computer]] <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

### Creating a Brewfile <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>
To create a `Brewfile` that lists your installed software:

1.  Navigate to your [[using_dotfiles_to_automate_development_environment_setup | dotfiles]] repository <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
2.  Run the command `brew bundle dump --describe` <a class="yt-timestamp" data-t="00:10:39">[00:10:39]</a>.
    *   This command creates a `Brewfile` in your current directory <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.
3.  Add the newly created `Brewfile` to your Git repository and commit it to save your software list and configurations <a class="yt-timestamp" data-t="00:11:22">[00:11:22]</a>.

### Reinstalling Software from a Brewfile <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>
On a new machine, after installing Homebrew, you can point it to your `Brewfile` to reinstall all your software <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>. This step is described as "very satisfying" due to its automation <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.

## Example Use Cases <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>

*   Homebrew was used to install [[programming_software | VS Code]] and other software <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   It can help keep [[programming_software | software]] like command-line tools and applications up to date <a class="yt-timestamp" data-t="00:11:10">[00:11:10]</a>.