---
title: Technical overview of GitHub integration for developers
videoId: GqLRRyCfoos
---

From: [[swarajmakesstuff]] <br/> 

This document provides a technical overview of a feature developed by [[apertures_platform_features_and_functionality | Apertures]] that enables developers to automatically generate social media posts based on their GitHub commits. This feature is designed to assist developers who want to [[building_in_public_for_developers | build in public]] and share their work with the world without constantly focusing on social media content creation <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## Core Functionality

The primary purpose of this integration is to serve as a personal assistant, automatically creating social media posts while developers focus on coding <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Users can select specific projects and commits they wish to share, and the system will automatically generate posts <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. Generated posts can also be edited and customized before publishing <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

## Technical Workflow

The process involves several steps to transform GitHub commits into social media posts:

1.  **Project Connection & Commit Monitoring**:
    *   Developers connect their GitHub account and specific repositories <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>.
    *   The system monitors changes and commits pushed to the connected repository <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

2.  **Context Provisioning**:
    *   Users provide context about their project <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This includes details like the project's purpose, target audience, planned [[features_and_functionalities_of_the_new_application | features]], and inspiration <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>.
    *   Providing more context helps the system understand the project better and generate higher-quality posts <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

3.  **Commit Segregation**:
    *   Commits are segregated into "important" and "non-important" categories <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.
    *   This distinction is crucial because not every commit represents a significant development; some might just be minor style or text changes <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This segregation helps identify which commits are best suited for generating effective social media posts <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

4.  **AI Model Fine-tuning and Generation**:
    *   The project context and segregated commits are fed into OpenAI APIs <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
    *   An OpenAI model is fine-tuned using this data <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
    *   Specific prompts, tailored for [[building_in_public_for_developers | building in public]], are then applied to the fine-tuned model <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
    *   The model generates social media posts based on the provided input and prompts <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.

## User Interface and Features

The application's [[features_and_functionalities_of_the_new_application | features]] are demonstrated through a demo project built for an Appwrite hackathon <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. While the backend was still in progress during the demonstration, the [[frontend_and_backend_frameworks | front-end]] UI was ready <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

Key user interface elements include:

*   **Onboarding**: Users connect their GitHub, Twitter, and LinkedIn accounts <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.
*   **Post Creation**: Options to create posts directly or connect a new repository <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Commit Selection**: Users can view and select specific commits from which to generate posts <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>.
*   **Context Input**: A dedicated section with questions prompts users to provide detailed project context, ensuring better post generation <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>.
*   **Post Management**:
    *   A "Posts" section displays posts specific to the current repository <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
    *   An "All Posts" section shows all generated posts across all connected repositories <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
    *   Users can edit generated posts before publishing <a class="yt-timestamp" data-t="00:05:58">[00:05:58]</a>.
*   **Analytics and Dashboard**: The platform is planned to include analytics and dashboard functionalities <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

### Technologies Mentioned

The demo project's [[frontend_and_backend_frameworks | frontend]] is built using Next.js, specifically utilizing its interception routes feature for UI navigation <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.