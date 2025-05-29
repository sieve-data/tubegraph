---
title: Features and Functionalities of the New Application
videoId: h9ifgquMh7s
---

From: [[swarajmakesstuff]] <br/> 

The developer has significantly revamped their side project, now a completely new application, after a period of limited work between October and December, resuming active development from February and March onwards <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The focus of the update is to detail the current state of the application and the changes that have been implemented <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## [[technical_platform_and_tools_migration | Technical Evolution]]

The application has undergone extensive [[technical_platform_and_tools_migration | technical platform and tools migration]] <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>:
*   Transitioned from Pages router to App router, and then to Turbo router <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   Migrated databases from MySQL to Postgres, then PlanetScale to Supabase, and finally Supabase to Neon DB <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   Completely changed the UI, migrating from Material Tailwind to Shadcn <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>.
*   Migrated ORM from Prisma to Drizzle <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   The backend, utilizing tRPC, did not require changes, but tRPC routes were moved to a separate package with the adoption of Turbo repo <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Personal Profile Features

The application now allows users to connect their social media accounts on a personal profile <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Supported Platforms**: Currently supports Twitter and LinkedIn <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. Instagram integration is being considered but requires official business registration in India, which entails costs <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Twitter API Keys**: Users are required to provide their own Twitter API keys due to the high cost of Twitter API access (starting from $100 up to $48,000) <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. All keys are safely stored for security <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.
*   **Content Creation**: Users can select multiple social media accounts for a single post <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. The application allows for minor tweaks to the content for each selected platform (e.g., "Hi Twitter" for Twitter, "Hi LinkedIn" for LinkedIn, while the default is "Hi") <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Drafts and Publishing**: Content can be saved to drafts and later published from the dashboard <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

These features contribute to [[apertures_platform_features_and_functionality | the application's overall functionality]] and aim at [[enhancing_web_app_interactivity | enhancing web app interactivity]] for social media management.

## Organization Features

A significant new feature is the ability to create organizations, which requires a subscription plan <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The billing process is handled with tax considerations based on the user's country (e.g., 18% GST for India) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Team Collaboration
*   **Organization Creation**: Users with a subscription can create new organizations <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
*   **Team Member Invitation**: The platform supports inviting new team members who can then accept the invitation <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **Role-Based Access Control**:
    *   **Owners/Admins**: Have full control, including editing roles, inviting members, and publishing content to social media <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
    *   **Editors**: Can create and edit content (e.g., upload videos), but cannot publish to social media or change roles/invite members <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. They can save content to draft <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>.
    *   **Viewers**: Can only view content, acting as a preview function, and cannot edit posts or add members <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

### YouTube Integration

Within an organization, users can integrate and manage YouTube content <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Video Uploads**: Users can upload video content and add thumbnails <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
*   **Background Processing**: Videos are first uploaded to the backend. From the database, a container is spun up to publish the video, meaning the user's internet is not consumed for streaming to YouTube <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. The process starts quickly and uploads in the background <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **Visibility**: Uploaded videos initially have private visibility and show as "pending" until processed by YouTube <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Future Enhancements**: The developer plans to add features for setting videos public or scheduling posts, as the scheduling function is not yet working <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>. Future plans also include adding review processes, live documentation reviews, and more comprehensive team management <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.