---
title: Creating and using symbolic links symlinks
videoId: r_MpUP6aKiQ
---

From: [[fireship]] <br/> 

## What is a Symbolic Link?

A symbolic link, or "symlink" for short, is a way for a file to appear to be in two places at the same time on a computer system <a class="yt-timestamp" data-t="06:47:38">[06:47:38]</a>. Symlinks are typically represented visually with an arrow icon in file explorers, signifying that they are not the original file but rather a link to it <a class="yt-timestamp" data-t="07:20:46">[07:20:46]</a>.

## Why Use Symlinks?

Developers often maintain a repository of text-based configuration files, known as [[using_dotfiles_to_automate_development_environment_setup | dot files]], to set up and restore customized development environments <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. These [[using_dotfiles_to_automate_development_environment_setup | dot files]] (which are hidden files starting with a period, like `.bashprofile` or `.git config`) store critical system preferences and software configurations <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>.

When these configuration files are moved from their original location (e.g., the home directory) to a [[using_dotfiles_to_automate_development_environment_setup | dot files]] repository, software that expects them in the original location can break <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>. For instance, moving the `.git config` file will cause `git` to use automatically configured committer information instead of the user's defined name and email <a class="yt-timestamp" data-t="05:16:03">[05:16:03]</a>. Similarly, moving the `zshrc` file will cause the Z shell to lose custom configurations like the command prompt <a class="yt-timestamp" data-t="06:21:09">[06:21:09]</a>.

Instead of duplicating these files and manually keeping them synchronized, symlinks allow the original location to point to the file within the [[using_dotfiles_to_automate_development_environment_setup | dot files]] repository, resolving the broken configurations <a class="yt-timestamp" data-t="06:37:38">[06:37:38]</a>.

## How to Create a Symlink

To create a symbolic link, the `ln` (link) command is used with the `-s` (symbolic link) option <a class="yt-timestamp" data-t="06:55:04">[06:55:04]</a>:

```bash
ln -s /path/to/real/file /path/to/original/location
```
*   `/path/to/real/file`: The full path to the actual configuration file stored in your [[using_dotfiles_to_automate_development_environment_setup | dot files]] repository <a class="yt-timestamp" data-t="07:03:00">[07:03:00]</a>.
*   `/path/to/original/location`: The path where the software expects the configuration file to reside <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>.

### Example Symlink Creation

To fix the broken `zshrc` configuration, a symlink can be created:
```bash
ln -s ~/.dotfiles/zshrc ~/.zshrc
```
This command links the `zshrc` file inside the hidden `.dotfiles` directory to the home directory, where the Z shell expects it <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a>. A similar process can be used for the `.git config` file <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.

## Verifying and Using Symlinks

Once a symlink is created, it will appear in the target directory (e.g., your home directory) with an arrow icon indicating it's a link <a class="yt-timestamp" data-t="07:14:00">[07:14:00]</a>.

Any changes made to the real file in the [[using_dotfiles_to_automate_development_environment_setup | dot files]] repository will be reflected in the symlinked version, and vice-versa <a class="yt-timestamp" data-t="07:40:00">[07:40:00]</a>. This ensures that when software (like `zsh` or `git`) reads the symlink in the expected location, it is actually reading the updated configuration from the [[using_dotfiles_to_automate_development_environment_setup | dot files]] repository <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>.

By using symlinks, configurations can be centrally managed in a [[using_dotfiles_to_automate_development_environment_setup | dot files]] repository, tracked with `git`, and automatically applied to new systems without breaking software that relies on specific file locations <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>.