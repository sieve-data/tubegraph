---
title: Automated social media posts from GitHub commits
videoId: GqLRRyCfoos
---

From: [[swarajmakesstuff]] <br/> 

A new feature has been developed that allows developers to connect their [[technical_overview_of_github_integration_for_developers | GitHub]] account and automatically generate social media posts based on their commits <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This tool functions as a [[personal_assistant_for_coders | personal assistant]] for developers, enabling them to focus on coding while it creates social media content <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. It is designed for developers who want to "build in public" and share their work <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Key Features & Benefits

*   **Automatic Post Generation** Users can select specific projects and commits, and the system will automatically generate posts <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>.
*   **Customization** Posts can be edited and customized before publishing <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **Focus on Coding** Acts as a [[personal_assistant_for_coders | personal assistant]], allowing developers to concentrate on their code <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## Technical Overview

The system operates by integrating with a user's GitHub repository and leveraging [[the_role_of_ai_in_content_automation_for_social_media | AI]] to craft relevant social media updates.

### Workflow

1.  **Project Connection** Users connect their GitHub project or specific repository to the system <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
2.  **Context Provision** Users provide context about their project, such as its inspiration, purpose, target audience, and features <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This context helps the system understand the project better and create more relevant posts <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. Answering more questions leads to better post quality <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
3.  **Commit Segregation** The system categorizes commits into "important" and "non-important" based on their content (e.g., distinguishing between feature developments and minor style changes) <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. This helps in selecting which commits are best suited for generating posts <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.
4.  **[[openai_api_integration_for_social_media_content | AI]] Generation**
    *   [[openai_api_integration_for_social_media_content | OpenAI APIs]] are used, fine-tuning the model based on the provided project context and segregated commits <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Specific prompts, tailored for "building in public," are given to the fine-tuned [[openai_api_integration_for_social_media_content | OpenAI]] model to generate social media posts <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Current Development Status

The feature is currently a single-feature product being developed for an Appwrite hackathon <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. The complete suite of [[social_media_management_solutions | social media automation tools]] exists on a different platform <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.

*   The frontend (UI) is ready <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.
*   The backend integration is still in progress <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

### User Interface (UI) Workflow (Frontend Demo)

*   **Onboarding Screen** Prompts users to connect their GitHub, Twitter, and LinkedIn accounts <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Post Creation** Users can either directly create posts or connect a new repository <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   **Commit Selection** Within a connected repository, users can view and select specific commits to generate posts from <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>.
*   **Context Provisioning** A dedicated section allows users to answer questions to provide detailed project context, enhancing the quality of generated posts <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Post Management**
    *   A "Posts" section displays posts specific to the current repository <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   An "All Posts" section shows all generated posts from all connected repositories <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
    *   Posts can be edited before publishing <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.

The demo also briefly showcases [[static_file_generation_during_build_time_in_react | Next.js]] features like interception routes and page navigation <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.