---
title: Startup Evolution and Progress
videoId: h9ifgquMh7s
---

From: [[swarajmakesstuff]] <br/> 

This article details the recent evolution and progress of a startup, focusing on significant technical migrations, new features, and the journey of building a comprehensive social media management tool.

## Development Timeline and Technical Overhaul

The developer shared that a significant period of inactivity on the startup occurred from October to December, with work resuming mostly in February and March <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. The project underwent a complete overhaul, involving numerous [[Technical Platform and Tools Migration|migrations]] <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

Key technical changes include:
*   **Routers**: Transitioned from Pages router to App router, then to Turbo router <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   **Databases**: Migrated from MySQL to PostgreSQL, and then between hosting providers: PlanetScale, Supabase, and finally Neon DB <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   **UI Frameworks**: Switched from Material Tailwind to Shadcn <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.
*   **ORMs**: Moved from Prisma to Drizzle <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   **Backend**: The TRPC backend remained unchanged, but its routes were moved to a separate package within a Turbo repo setup <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

The migration process was described as "fun" despite being more complicated than starting a new project <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Current Application State and Features

The application now allows users to connect various social media accounts to their personal profile <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Social Media Integration
Currently, users can connect Twitter and LinkedIn <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Instagram**: The developer is considering adding Instagram, but it requires official business registration in India, which incurs costs <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
*   **Twitter API**: Users must provide their own Twitter API keys due to the high cost of Twitter's API, which ranges from $100 to $48,000 <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The developer, a small developer from India, does not have the funds to cover these costs <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>. User security for API keys is assured <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This highlights [[challenges_and_solutions_in_startup_development|challenges related to external API costs]].

### Posting Capabilities
Users can select multiple social media accounts for a single post and make specific tweaks for each platform (e.g., "Hi Twitter" for Twitter, "Hi L" for LinkedIn) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. Posts can be saved as drafts and published directly from the dashboard <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

## Organizations and Team Management

A significant new feature is the ability to create organizations, which requires a subscription <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. The billing process was demonstrated in test mode, showing how taxes are applied based on the user's country (e.g., 18% GST in India) <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.

### Organization Features
*   **Creation**: Users can create an organization, give it a name, and upload an image <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>.
*   **Team Invitation**: New team members can be invited to an organization <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### YouTube Integration
Organizations can connect YouTube channels <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Video Upload**: Users can upload videos and add thumbnails, titles, and descriptions <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Background Processing**: Videos are first uploaded to the backend, then a container is started from the database to publish them directly to YouTube in the background. This means team members do not need to consume their own internet bandwidth for uploads <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>.
*   **Privacy**: Uploaded YouTube videos are initially set to private <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

### Team Roles and Permissions
The application implements different roles within an organization:
*   **Owner/Admin**: Can edit roles, invite members, and publish posts to social media <a class="yt-timestamp" data-t="00:09:17">[00:09:17]</a>.
*   **Editor**: Can create and edit content, upload videos, and save to draft, but cannot publish to social media <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. They can add social accounts but not publish to them <a class="yt-timestamp" data-t="00:09:56">[00:09:56]</a>.
*   **Viewer**: Can only view content and cannot edit posts or add members <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.

## Future Plans

The developer plans to add further enhancements, including:
*   **Scheduling**: Implementing a feature to schedule posts <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>. This relates to [[dynamic_onetime_event_schedulers|dynamic onetime event schedulers]].
*   **Team Management**: Expanding team management features to include reviews and live documentation <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.