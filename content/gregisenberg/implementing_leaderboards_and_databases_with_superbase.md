---
title: Implementing leaderboards and databases with Superbase
videoId: 51Vb2_brjiA
---

From: [[gregisenberg]] <br/> 

Building interactive applications, especially [[building_viral_video_games | viral video games]], often requires a robust backend to manage data like high scores and user information. [[backend_as_a_service_solutions_like_supabase | Supabase]] is highlighted as an excellent solution for this purpose due to its ease of use and cost-effectiveness <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.

## Why Supabase for Backend?

[[backend_as_a_service_solutions_like_supabase | Supabase]] is considered "probably the easiest for beginners to use database for apps" <a class="yt-timestamp" data-t="00:21:55">[00:21:55]</a>. It is also noted as being "super cheap and easy and fast" <a class="yt-timestamp" data-t="00:47:14">[00:47:14]</a>. Even with thousands of users, a free version can be utilized, making it ideal for starting and experimenting with projects <a class="yt-timestamp" data-t="00:46:51">[00:46:51]</a>. Many new micro SaaS applications use [[backend_as_a_service_solutions_like_supabase | Supabase]] for these reasons <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>.

## Implementing a High Score Leaderboard

To integrate a high score leaderboard and collect email addresses in an AI-generated game, the following steps are taken with [[backend_as_a_service_solutions_like_supabase | Supabase]] as the backend <a class="yt-timestamp" data-t="00:43:18">[00:43:18]</a>:

1.  **Define the Goal**: The primary goal is to implement a leaderboard where users can input their email and have their score recorded when they lose <a class="yt-timestamp" data-t="00:43:57">[00:43:57]</a>.
2.  **Leverage AI for Planning**: When giving complex instructions, it's beneficial to ask the AI for a plan first, then approve it <a class="yt-timestamp" data-t="00:44:51">[00:44:51]</a>. This helps avoid "hallucinating" or going down "weird paths" <a class="yt-timestamp" data-t="00:44:32">[00:44:32]</a>. The AI's plan for [[backend_as_a_service_solutions_like_supabase | Supabase]] integration includes:
    *   Setting up [[backend_as_a_service_solutions_like_supabase | Supabase]] <a class="yt-timestamp" data-t="00:45:17">[00:45:17]</a>
    *   Game UI changes <a class="yt-timestamp" data-t="00:45:20">[00:45:20]</a>
    *   Leaderboard backend integration <a class="yt-timestamp" data-t="00:45:22">[00:45:22]</a>
    *   Visual design for the leaderboard <a class="yt-timestamp" data-t="00:45:27">[00:45:27]</a>
    *   Adding features like a "share to X" button and weekly/all-time toggles <a class="yt-timestamp" data-t="00:45:29">[00:45:29]</a>.
3.  **Setup Supabase Project**:
    *   Go to `supabase.com` and sign up <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>.
    *   Create a new project (e.g., "space game") <a class="yt-timestamp" data-t="00:47:26">[00:47:26]</a>.
    *   Set a strong password <a class="yt-timestamp" data-t="00:47:35">[00:47:35]</a>.
4.  **Create the Leaderboard Table Schema**:
    *   In the [[backend_as_a_service_solutions_like_supabase | Supabase]] SQL editor <a class="yt-timestamp" data-t="00:52:21">[00:52:21]</a>, run the following SQL commands provided by the AI:
        *   To create the `leaderboard` table where scores will be stored:
            ```sql
            CREATE TABLE leaderboard (
              id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
              email TEXT NOT NULL,
              score INT NOT NULL,
              created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
            );
            ```
            <a class="yt-timestamp" data-t="00:52:31">[00:52:31]</a>
        *   To create an index for faster queries:
            ```sql
            CREATE INDEX leaderboard_score_idx ON leaderboard (score DESC);
            ```
            <a class="yt-timestamp" data-t="00:52:47">[00:52:47]</a>
        *   To add security policies (Row Level Security):
            ```sql
            ALTER TABLE leaderboard ENABLE ROW LEVEL SECURITY;
            ```
            <a class="yt-timestamp" data-t="00:52:51">[00:52:51]</a>
        *   To allow anyone to insert scores:
            ```sql
            CREATE POLICY "Allow anon to insert scores" ON leaderboard
            FOR INSERT WITH CHECK (true);
            ```
            <a class="yt-timestamp" data-t="00:52:58">[00:52:58]</a>
        *   To allow anyone to read scores:
            ```sql
            CREATE POLICY "Allow anon to read scores" ON leaderboard
            FOR SELECT USING (true);
            ```
            <a class="yt-timestamp" data-t="00:53:04">[00:53:04]</a>
5.  **Integrate API Keys**:
    *   Go to `Project settings` then `API` in [[backend_as_a_service_solutions_like_supabase | Supabase]] to get your API credentials <a class="yt-timestamp" data-t="00:53:17">[00:53:17]</a>.
    *   Copy the project URL and anon key <a class="yt-timestamp" data-t="00:53:38">[00:53:38]</a>.
    *   Update the `supabase_config.js` file in the game code with these placeholder keys <a class="yt-timestamp" data-t="00:50:01">[00:50:01]</a>.
6.  **Update Game Code**: The AI provides the necessary code to integrate the [[backend_as_a_service_solutions_like_supabase | Supabase]] client and update the `sketch.js` file for leaderboard functionality <a class="yt-timestamp" data-t="00:48:46">[00:48:46]</a>. This includes handling the game over screen to prompt for email and score submission.
7.  **Debugging and Refinement**: Initial integration may have issues, such as the game not displaying correctly or the email input field not working <a class="yt-timestamp" data-t="00:55:09">[00:55:09]</a>. By describing the problem to the AI, it can identify and fix issues, such as `p5.js` capturing keyboard events, which prevents typing in the input field <a class="yt-timestamp" data-t="00:59:21">[00:59:21]</a>. The AI can also anticipate other edge cases, like mouse event capture, and provide fixes <a class="yt-timestamp" data-t="01:00:02">[01:00:02]</a>.

Once these steps are completed, the game successfully records scores and emails to the [[backend_as_a_service_solutions_like_supabase | Supabase]] database, and displays them on a leaderboard <a class="yt-timestamp" data-t="01:01:13">[01:01:13]</a>.

## Business Impact and Virality

Implementing a leaderboard with email collection directly contributes to a business's growth strategy <a class="yt-timestamp" data-t="00:43:18">[00:43:18]</a>. Instead of traditional methods like lengthy threads asking for newsletter sign-ups <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>, offering an engaging experience like a game allows for natural lead generation <a class="yt-timestamp" data-t="00:43:25">[00:43:25]</a>. This type of interactive content is more compelling and likely to go viral, especially on platforms like X (formerly Twitter), leading to increased clicks, followers, and newsletter subscribers <a class="yt-timestamp" data-t="00:29:56">[00:29:56]</a>. The AI's ability to integrate elements like a "share to X" button directly within the game further enhances its viral potential <a class="yt-timestamp" data-t="00:45:29">[00:45:29]</a>.

This approach demonstrates an "Arbitrage opportunity" for business owners, leveraging new AI technologies to create engaging experiences and gain attention before these strategies become commonplace <a class="yt-timestamp" data-t="01:01:56">[01:01:56]</a>.