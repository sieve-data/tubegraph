---
title: Building in public for developers
videoId: GqLRRyCfoos
---

From: [[swarajmakesstuff]] <br/> 

Building in public is a practice where developers share their work and progress openly with the community as they build. A key feature developed by Apertures aims to automate this process, allowing developers to generate social media posts based on their GitHub commits <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Why Automate Building in Public?

This feature is designed for [[the_journey_of_building_a_startup_in_public | developers who want to build in public]] and share their ongoing work with the world <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. It functions as a personal assistant, enabling developers to focus on coding while the system automatically creates social media posts for them <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

Users can select specific projects and commits they wish to share, and Apertures will automatically generate corresponding posts <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. These posts can then be edited and customized before being published <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

## [[technical_overview_of_github_integration_for_developers | Technical Overview]]

The process of generating these automated social media posts involves several steps:

1.  **Project Connection and Context**
    *   Developers connect their GitHub project or specific repository to the Apertures platform <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   The system collects context about the project, such as its purpose, target audience, planned features, and overall vision <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Providing more detailed context helps the system generate higher-quality posts <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
2.  **Commit Segregation**
    *   As developers continue to make changes and push commits, the system monitors these <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
    *   Commits are then segregated into "important" and "non-important" categories <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. This distinction helps filter out minor changes (e.g., style or text edits) from more significant updates like feature development <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
3.  **AI Model Fine-Tuning and Generation**
    *   The important commits and project context are fed into OpenAI APIs <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   An OpenAI model is fine-tuned using specific prompts tailored for [[the_journey_of_building_a_startup_in_public | building in public]] <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>, <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
    *   This fine-tuned model then generates draft social media posts <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>.

## [[apertures_platform_features_and_functionality | Apertures Platform Features]]

The developer-focused part of the Apertures platform includes the following user interface elements:

*   **Onboarding:** Users are prompted to connect their GitHub, Twitter, and LinkedIn accounts <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Repository Connection:** Developers can connect new repositories <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.
*   **Commit Selection:** The platform displays all commits, allowing users to select which ones to use for post generation <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Context Provision:** A dedicated section presents various questions to help users provide comprehensive project context <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Post Management:**
    *   A "Post" section shows posts specific to the currently viewed repository <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   An "All Posts" section displays posts generated from all connected repositories <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
*   **Editing and Publishing:** Users can click "edit" to customize generated posts before publishing <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Analytics and Dashboard:** The platform will also include analytics and a dashboard for monitoring post performance <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

This feature is being developed with a focus on providing developers with a streamlined way to engage with their audience and share their progress efficiently.