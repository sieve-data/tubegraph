---
title: Technical Platform and Tools Migration
videoId: h9ifgquMh7s
---

From: [[swarajmakesstuff]] <br/> 

After a period of reduced development between October and December, significant work resumed on the startup project in February and March, leading to a complete overhaul of the technical stack <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This extensive [[startup_evolution_and_progress | evolution]] involved numerous migrations across various components of the application, transforming it into a completely new project <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

## Frontend Framework and Routing

The application underwent multiple changes in its routing and UI frameworks:
*   Initial migration from a normal Pages router to an App router <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   Further transition from the App router to a Turbo router <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
*   The UI framework was migrated from Material Tailwind to ShadCN, which is now regularly used <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

The developer noted that these changes were enjoyable <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Database and ORM Migrations

The database and object-relational mapping (ORM) layers also saw significant changes:
*   Transitioned from MySQL to Postgres <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
*   Database hosting moved from PlanetScale to Superbase, and then to Neon DB <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
*   The ORM was migrated from Prisma to Drizzle <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.
*   The developer highlighted that migrating these components was more complicated than starting a new project, but it was a "fun and good thing" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Backend and Monorepo Integration

Despite the extensive [[frontend_and_backend_frameworks | frontend]] and database changes, the backend, utilizing TRPC, did not require a complete rewrite <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. Instead, the project transitioned to a Turbo repo setup, and the TRPC routes were moved to a separate package <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. This process was also described as fun <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

These [[technical_aspects_and_ideation_process_in_startups | technical migrations]] have culminated in the current state of the application, which includes features like [[features_and_functionalities_of_the_new_application | social media integration]] and organization management <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.