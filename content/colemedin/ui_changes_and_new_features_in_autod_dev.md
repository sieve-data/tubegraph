---
title: UI changes and new features in Autod Dev
videoId: nkqQfABopyc
---

From: [[colemedin]] <br/> 

Autod Dev, formerly known as [[renaming_of_bolt_new_any_llm_to_autod_dev | Bolt.new]], has seen significant community development over the past month and a half, with a strong focus on becoming the leading open-source AI coding assistant <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This rapid progress includes numerous UI enhancements and the implementation of highly requested features <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Core New Features

### [[introduction_of_local_project_load_feature_in_autod_dev | Local Project Load Feature]]

A highly anticipated feature, the ability to load existing local projects into Autod Dev, is now available <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This allows users to continue working on their projects within the platform <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>.
*   **Credit**: This feature was developed by Edward, one of the core maintainers of Autod Dev <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>.
*   **Usage**: Users can import folders, whether they were built in Autod Dev, Bolt.new, or custom-coded <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. Once imported, Autod Dev understands all the files and can continue conversations from where the project left off <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Limitations**: It is recommended to keep project imports under 100 files to avoid crashing the site <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Users should also avoid importing large folders like `node_modules`, even with ignore settings, as files are still brought into the front end before filtering <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
*   **Functionality**: After importing, users may need to explicitly tell Autod Dev to run installation and execution commands (e.g., `npm install`, `npm run dev`) for the project to spin up correctly <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### Loading GitHub Projects

The ability to load Git repositories into Autod Dev, similar to local projects, is currently in progress <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>. This work is being done by The Codus <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

### Attaching Images to Prompts

This feature is nearing completion and will allow users to upload images to prompts <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a> <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>.
*   **Demonstration**: Users can test this feature by switching to its specific pull request branch using GitHub Desktop and running the development environment <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>.
*   **Model Requirements**: This feature will only work with models that support image comprehension, such as Claude or GPT-4o <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>. Models like Llama or Quen Coder will not understand images <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.
*   **Current State**: While the feature allows for image uploading and the AI models can comprehend them, further UI improvements are needed, such as displaying the uploaded image in the chat history <a class="yt-timestamp" data-t="00:12:03">[00:12:03]</a>.

## UI Enhancements and Other Additions

Many other significant UI changes and feature additions have been made to Autod Dev <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>:

*   **Chat Management**:
    *   Importing and exporting chats <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
    *   Searching through chat history <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
    *   Reverting code to earlier versions within a conversation, allowing users to scrap unwanted changes <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   Forking chats from a specific message <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Interface Improvements**:
    *   Many UI changes to make the interface more similar to the commercial Bolt.new platform <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.
    *   Ability to collapse model settings for more UI room <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a> <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
    *   Mobile-friendly updates <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   **Model and Prompt Enhancements**:
    *   Enhancements to the "Prompt enhance" feature <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
    *   Cohere integration by Hassan <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
    *   Dynamic model max token limits, crucial because different models have varying token requirements <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   Prompt caching, added by Sujal <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **Project Maintenance and Documentation**:
    *   Stable additions and cleanup efforts, significantly contributed by Dustin Loring <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.
    *   Improvements to linting and testing, contributed by Sujal and Oliver, which are vital for project maturity <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a> <a class="yt-timestamp" data-t="00:08:30">[00:08:30]</a>.
    *   A dedicated documentation page for Autod Dev, added by The Codakiss <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This page auto-compiles from Readme and Markdown files in the repository, making documentation more accessible <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.

## Connecting to the [[roadmap_and_development_progress_of_autod_dev | Autod Dev Roadmap]]

These new features directly align with the [[roadmap_and_development_progress_of_autod_dev | Autod Dev roadmap]], which was recently established to outline the project's vision <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Many high-priority features, such as [[introduction_of_local_project_load_feature_in_autod_dev | loading local projects]], are already completed or in progress <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

### [[upcoming_strategic_partnership_for_autod_dev | Upcoming Strategic Partnership]]

An [[upcoming_strategic_partnership_for_autod_dev | upcoming strategic partnership]] is set to further enhance Autod Dev by bringing in open-source experts to improve organization, testing, CI/CD, issue templates, and community management <a class="yt-timestamp" data-t="00:13:06">[00:13:06]</a>. This partnership will also provide financial incentives to reward contributors and support the core team (excluding the speaker), and will significantly boost the project's visibility and credibility, moving it beyond a hobbyist project to a mature and leading open-source AI coding assistant <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.

## Get Involved

The progress on Autod Dev has been phenomenal and encouraging <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. Users are encouraged to download and try out the new features <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. The Autod Dev community, or "think tank," welcomes new members to be part of its ongoing development <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.