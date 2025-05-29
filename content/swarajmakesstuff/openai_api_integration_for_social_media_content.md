---
title: OpenAI API integration for social media content
videoId: GqLRRyCfoos
---

From: [[swarajmakesstuff]] <br/> 

A feature has been developed by [[Apertures platform features and functionality | Apertures]] that allows users to connect their GitHub account and automatically generate social media posts based on their commits <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This capability is specifically designed for developers who engage in "building in public" and wish to share their work with the world <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. It functions as a personal assistant, creating social media posts while developers focus on coding <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## How It Works

The system integrates with GitHub repositories and leverages [[the_role_of_ai_in_content_automation_for_social_media | AI]], specifically [[the_role_of_ai_in_content_automation_for_social_media | OpenAI API]], to generate content.

### Connecting Projects and Providing Context

Users first connect their GitHub project or specific repository <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. As changes are made and commits are pushed, the system captures this information <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

A crucial step involves providing "context" about the project <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This context includes details such as:
*   What the project is about <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a>
*   Its purpose <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
*   Planned features <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>
*   The target audience <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>
*   Inspiration behind starting the project <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>

Providing as much detail as possible in the context section helps the system understand the project better and generate more relevant and effective posts <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Commit Segregation and AI Processing

The system processes the commits by segregating them into "important" and "non-important" categories <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. This distinction is made because not every commit may be a significant feature development; some might be minor style or text changes <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. This segregation helps in identifying which commits are best suited for generating social media posts <a class="yt-timestamp" data-t="00:02:18">[00:02:18]</a>.

The context and the segregated commits are then used to fine-tune [[the_role_of_ai_in_content_automation_for_social_media | OpenAI API]] models <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. Specific prompts, designed for "building in public," are given to the fine-tuned model to ensure the generated posts are appropriate for public sharing <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

## User Workflow and Features

The process for a user involves several steps within the platform:

### Onboarding and Connection
Upon onboarding, users are prompted to connect their GitHub, Twitter, and LinkedIn accounts <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Once connected, they can either create posts directly or connect a new repository <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.

### Post Generation and Customization
Users can view all their commits for a connected repository <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. They can select specific commits from which to generate posts <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. The system then automatically generates posts based on the selected commits and changes <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

Users retain control over the generated content, having the option to edit and customize posts before publishing them <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.

### Post Management and Analytics
The platform organizes posts by repository, allowing users to view posts specific to a particular project <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. There is also an "all posts" section where users can see all content created from all connected repositories <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>. The system is also designed to provide analytics and a dashboard <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## Development Status
As of the video, the feature is still under development by [[Apertures platform features and functionality | Apertures]] <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. The front-end user interface is ready, while the back-end integration is currently in progress <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. This specific feature is being developed for an Appwrite hackathon, distinct from Apertures' complete social media automation tools <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.