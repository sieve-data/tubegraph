---
title: Improvements in project organization and contribution management
videoId: nkqQfABopyc
---

From: [[colemedin]] <br/> 

AutodDev, a fork of Bolt.new, is being developed by the community to be the "best [[Open Source Development | open-source]] AI coding assistant" <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Over the past month and a half, the community has made significant strides, particularly in improving project organization and managing contributions <a class="yt-timestamp" data-t="00:00:01">[00:00:01]</a>.

## Key Developments and Features

### Local Project Loading
A highly requested feature, the ability to load existing local projects into AutodDev, is now available <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This feature was implemented by Edward, one of AutodDev's [[Core contributor opportunities for the Bolt new fork project | core maintainers]] <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. Users can now import folders containing their projects, enabling them to continue working on them within AutodDev <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. The system intelligently understands imported files, retaining context for continued development <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

There are some limitations to be aware of:
*   Avoid loading "massive massive projects" to prevent site crashes; keep projects under approximately 100 files <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   Though an ignore setup exists for folders like `node_modules`, these files are still brought to the front end before filtering, so users should keep imports "nimble" <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.
*   When importing projects, users often need to explicitly command the AI to run installation and execution commands (e.g., `npm install`, `npm run dev`) <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.

### User Interface and Experience Enhancements
Numerous UI changes have been implemented to make AutodDev more similar to the commercial Bolt.new platform <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. These include:
*   **Importing/Exporting Chats**: Chats can now be imported and exported <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   **Chat History Features**: Users can search through past chats <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   **Collapsible Model Settings**: Model settings can be collapsed to provide more UI space <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
*   **Conversation Reversion**: The ability to revert to a specific message in the conversation, which is useful for correcting AI mistakes <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Chat Forking**: Users can fork a chat from a specific message point <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
*   **Prompt Enhance Enhancements**: Improvements have been made to the "Prompt enhance" feature <a class="yt-timestamp" data-t="00:04:29">[00:04:29]</a>.

### Roadmap and Future Developments
A roadmap for AutodDev has been established to outline its vision, starting with high-priority features <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>.

Current high-priority features include:
*   **Loading Local Projects**: Completed <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   **Loading GitHub Projects**: In progress, allowing users to load Git repositories similar to local projects <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a> <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.
*   **Attaching Images to Prompts**: Nearing completion, this feature will allow users to upload images for AI comprehension, though it requires models that support image input (e.g., Claude, GPT-4o) <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a> <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

The roadmap will continue to be extended as the vision for AutodDev evolves <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.

## Community Contributions and Organizational Improvements

[[Community Contributions to Software Development | Incredible contributions]] are being made by various individuals to AutodDev <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. These efforts are making the project more mature and stable <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

Notable contributors and their contributions include:
*   **Edward**: Implemented the ability to revert code to earlier versions <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>, and the high-priority task of loading local projects <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Hassan**: Added Coher integration <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a> and dynamic model max token links, which are crucial due to varying model requirements <a class="yt-timestamp" data-t="00:06:59">[00:06:59]</a>.
*   **Sujal**: Contributed prompt caching <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, and, along with Oliver, has been instrumental in linting and testing efforts, which are vital for project maturity <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a> <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.
*   **Dustin Luring**: Made significant stable additions to clean up and tidy the project, including UI work and assisting with prompt caching integration <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a> <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.
*   **The Codus**: Made phenomenal additions such as code streaming output <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>, and developed a dedicated documentation page for AutodDev <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. This page automatically recompiles based on `README` and Markdown files, improving project presentation and maturity <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. The Codus is also working on Git repository integration <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.
*   **Oliver**: Contributed to linting and testing, essential for the project's maturity <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

Other notable improvements include mobile-friendly updates <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a> and enhanced `FAQ`s <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.

## Strategic Partnership for Project Maturity

A strategic partnership is soon to be announced that will "supercharge" AutodDev <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This partnership aims to elevate AutodDev to a mature project by addressing key areas:

*   **Organizational Expertise**: The partnership will bring in [[Open Source Development | open-source]] experts to improve tests, CI/CD, issue templates, pull request management, and overall [[Community engagement and contributions | community management]] <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. This expertise is expected to make the project "shine" as an [[Open Source Development | open-source]] endeavor <a class="yt-timestamp" data-t="00:13:58">[00:13:58]</a>.
*   **Financial Incentives**: This partnership will provide financial incentives, enabling rewards for contributors and support for the core contributor team (excluding the speaker) <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a>.
*   **Increased Visibility and Credibility**: The partnership will bring significant visibility and credibility, transitioning AutodDev from a hobbyist project to "the real deal" <a class="yt-timestamp" data-t="00:14:25">[00:14:25]</a>. This is expected to be a major factor in making AutodDev the best [[Open Source Development | open-source]] AI coding assistant <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.

The project is making phenomenal progress towards becoming the leading [[Open Source Development | open-source]] AI coding assistant <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>. The community is encouraged to download and try the new features <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a> and join the AutodDev "think tank" community <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.