---
title: Roadmap and development progress of Autod Dev
videoId: nkqQfABopyc
---

From: [[colemedin]] <br/> 

Autod Dev is an open-source AI coding assistant that aims to be the best in its category <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Over the past month and a half, the community has significantly contributed to its development <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. A roadmap for Autod Dev was initiated to outline its vision and prioritize high-impact features <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

## Key Developments and Features

### [[introduction_of_local_project_load_feature_in_autod_dev | Local Project Loading]]
One of the most requested features for Autod Dev was the ability to load existing local projects into the platform, allowing users to continue working on them within the assistant <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This highly anticipated feature is now available, thanks to Edward, a core maintainer of Autod Dev <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

*   **Functionality**: Users can import folders, and Autod Dev understands the files, maintaining context for continued work <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a> <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. This allows for improvements to existing projects as if they were coded directly within the platform <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Limitations**: It's advised to keep project imports nimble, ideally less than 100 files, and avoid bringing in large folders like `node_modules` to prevent crashes <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a> <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a> <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Users may need to explicitly tell the AI to run installation and execution commands for imported projects <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### [[ui_changes_and_new_features_in_autod_dev | UI Changes and New Features]]
Significant work has been done on Autod Dev's UI and overall functionality, making it more similar to the commercial Bolt.new platform <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a> <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

Key UI and feature updates include:
*   Importing and exporting chats <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   Searching through chat history <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   Collapsing model settings for more UI room <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   Ability to revert to a specific message in the conversation <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   Forking a chat from a specific message <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   Enhancements to the "Prompt Enhance" feature <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.
*   Dynamic model max token limits for different model requirements <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   Prompt caching <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   Mobile-friendly updates <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.
*   A dedicated documentation page that recompiles based on repo readmes and markdown files <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

### Roadmap Progress
The Autod Dev roadmap outlines high-priority features essential for the project's maturity <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a> <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

*   **Completed**:
    *   [[introduction_of_local_project_load_feature_in_autod_dev | Loading local projects]] <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   **In Progress (High Priority)**:
    *   **Loading GitHub projects**: This feature, being developed by 'the codus', will allow loading Git repositories into Autod Dev, complementing the local project loading capability <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a> <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
    *   **Attaching images to prompts**: This feature is nearing completion <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a> <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. It enables users to upload images and prompt the AI (e.g., Claude, GPT-4o) to describe or even code a website based on the image <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a> <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

### Community Contributions and Recent Changes
Numerous contributors have made valuable additions to Autod Dev:
*   **Edward**: Implemented [[introduction_of_local_project_load_feature_in_autod_dev | local project loading]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a> <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a> and the ability to revert code to earlier versions <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
*   **Hassan**: Added Cohere integration <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.
*   **Hanan**: Contributed dynamic model max token limits <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
*   **Sujal**: Implemented prompt caching <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a> and contributed to linting and testing <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Dustin Loring**: Made significant stable additions to clean up the project and worked on UI and prompt caching <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a> <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **Oliver**: Contributed to linting and testing efforts, which are crucial for project maturity <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.
*   **The codus**: Made significant additions including streaming code output <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, and added the dedicated documentation page <a class="yt-timestamp" data-t="00:08:49">[00:08:49]</a>.

## [[upcoming_strategic_partnership_for_autod_dev | Upcoming Strategic Partnership]]
Autod Dev is set to announce a strategic partnership that is expected to significantly enhance the project <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a> <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. While timing and logistics are still being finalized, the partnership is anticipated to bring:

*   **Open-source expertise**: Experts will help organize the repository, improve tests and CI/CD, create issue templates, and enhance management of pull requests and the community <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   **Financial incentives**: This includes rewarding contributors, supporting the core contributor team (excluding the speaker), and providing necessary funding to advance Autod Dev <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.
*   **Visibility and credibility**: The partnership is expected to transition Autod Dev from a hobbyist project into a professional, "real deal" endeavor, boosting its recognition as a leading open-source AI coding assistant <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>.

Autod Dev continues to make phenomenal progress towards its goal of becoming the best open-source AI coding assistant <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. Users are encouraged to download and try the new features and join the Autod Dev community and "think tank" <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.