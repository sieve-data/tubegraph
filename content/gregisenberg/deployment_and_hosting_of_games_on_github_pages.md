---
title: Deployment and hosting of games on GitHub Pages
videoId: 51Vb2_brjiA
---

From: [[gregisenberg]] <br/> 

This article outlines how to create, deploy, and host simple AI-generated video games using tools like Grok, Cursor, and Superbase, specifically focusing on [[setting_up_a_github_repository_for_use_with_codex | GitHub]] Pages for live deployment. This method is presented as a powerful strategy for growth hacking, driving newsletter sign-ups, and increasing product attention <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Overview of the Process

The process involves using AI models to design and code a game, integrating a database for features like leaderboards, and then deploying the game to a live web server <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>. This approach is accessible even for those without extensive coding experience <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.

### Key Tools

*   **Grock**: An AI model used for planning and generating code.
    *   **Deep Search**: Scans the web for research and creates a game plan <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>.
    *   **Think**: Executes the plan and builds the actual code <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.
    *   It's noted for its speed and detailed chain of thought <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>. Grok 3 is available for free with limited use, or higher usage for premium X subscribers <a class="yt-timestamp" data-t="00:13:50">[00:13:50]</a>.
*   **p5.js**: A free and easy-to-use JavaScript gaming framework, ideal for quick prototyping due to its instant testing capability on its website (p5js.org) <a class="yt-timestamp" data-t="00:07:47">[00:07:47]</a>.
*   **Cursor**: An AI agent (IDE) that allows users to build and modify code, integrating with models like Claude Sonet 3.7 <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Superbase**: An easy-to-use, often free, database for beginners to store data like high scores and email addresses <a class="yt-timestamp" data-t="00:21:52">[00:21:52]</a>.

## Game Development with AI

The process begins by using Grok's Deep Search to create a game plan, specifying elements like game type (e.g., space shooter), visual style, and asset generation (telling the AI to build all sprites itself) <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. This plan is then fed into Grok's Think mode to generate the actual p5.js code <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>.

Once the initial code is generated, it's moved to Cursor for further refinement, debugging, and feature additions, such as shooting mechanics or collision detection <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>. AI can also act as a product manager, offering design suggestions to make the game more viral or appealing <a class="yt-timestamp" data-t="00:25:56">[00:25:56]</a>. For instance, suggesting power-ups or different enemy types to enhance engagement <a class="yt-timestamp" data-t="01:00:57">[01:00:57]</a>.

### Integrating Superbase for Leaderboards

To add a leaderboard and collect emails, Superbase is used as the backend database <a class="yt-timestamp" data-t="00:44:14">[00:44:14]</a>.
1.  **Set up Superbase**: Create a new project on superb.com <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>.
2.  **Create Table Schema**: Use Superbase's SQL editor to run commands provided by the AI (e.g., in a generated README file) to create a `leaderboard` table with fields for score and email <a class="yt-timestamp" data-t="00:51:57">[00:51:57]</a>.
3.  **Configure API Keys**: Copy the Project URL and Anon Key from Superbase settings and paste them into a `superbase_config.js` file in your project <a class="yt-timestamp" data-t="00:53:17">[00:53:17]</a>.
4.  **Implement in Game**: The AI updates the game's JavaScript file (`sketch.js`) to handle submitting scores and emails to Superbase <a class="yt-timestamp" data-t="00:48:40">[00:48:40]</a>.

## Deployment to GitHub Pages

GitHub Pages is highlighted as one of the easiest ways to move a prototype to a live internet presence <a class="yt-timestamp" data-t="01:00:17">[01:00:17]</a>.

### Steps for Deployment

1.  **Initialize Git**: In your project directory within Cursor's terminal, initialize a Git repository <a class="yt-timestamp" data-t="01:04:58">[01:04:58]</a>.
    ```bash
    git init
    ```
2.  **Create `.gitignore`**: Exclude unnecessary files <a class="yt-timestamp" data-t="01:05:03">[01:05:03]</a>.
    ```bash
    git ignore
    ```
3.  **Add Files**: Add all project files to the Git repository <a class="yt-timestamp" data-t="01:05:10">[01:05:10]</a>.
    ```bash
    git add .
    git commit -m "Initial game commit"
    ```
4.  **Create GitHub Repository**: Go to GitHub.com, create a new *public* repository (e.g., `space-shooter-email`), and **do not** initialize it with a README <a class="yt-timestamp" data-t="01:05:41">[01:05:41]</a>.
5.  **Push Code to GitHub**: GitHub will provide commands to push your existing local repository to the newly created remote repository <a class="yt-timestamp" data-t="01:06:25">[01:06:25]</a>.
    ```bash
    git remote add origin https://github.com/your-username/your-repo-name.git
    git branch -M main
    git push -u origin main
    ```
6.  **Enable GitHub Pages**:
    *   On your GitHub repository page, navigate to `Settings` <a class="yt-timestamp" data-t="01:07:47">[01:07:47]</a>.
    *   Scroll down to the `Pages` section <a class="yt-timestamp" data-t="01:07:50">[01:07:50]</a>.
    *   Under "Source," select the `main` branch (or whichever branch contains your game's `index.html`) <a class="yt-timestamp" data-t="01:08:26">[01:08:26]</a>.
    *   Click `Save` <a class="yt-timestamp" data-t="01:08:38">[01:08:38]</a>.
7.  **Verify Deployment**: After a few minutes, your game will be live at the URL provided by [[setting_up_a_github_repository_for_use_with_codex | GitHub]] Pages <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>.

> [!NOTE] Other deployment options include [[prototyping_and_deployment_with_replit | Replit]] and Netlify <a class="yt-timestamp" data-t="01:00:24">[01:00:24]</a>.

## Leveraging for Virality and Lead Generation

Once deployed, the game becomes a powerful marketing tool:
*   **Share on X (formerly Twitter)**: Instead of a text-based thread, share a video of the game with a compelling hook, then include the live game link in a follow-up tweet <a class="yt-timestamp" data-t="01:11:01">[01:11:01]</a>.
*   **Encourage Engagement**: Incentivize plays by offering a prize for the highest score, encouraging users to share screenshots of their scores in the replies, boosting visibility <a class="yt-timestamp" data-t="01:10:01">[01:10:01]</a>.
*   **Email Collection**: The integrated leaderboard automatically collects email addresses from players, serving as a lead generation mechanism for newsletters or other products <a class="yt-timestamp" data-t="00:43:33">[00:43:33]</a>.

### Advanced Tips

*   **Turn Memes into Games**: Leverage trending memes and jokes by uploading images of them to AI and prompting it to create a game experience around them. This taps into current viral trends for maximum attention <a class="yt-timestamp" data-t="01:14:05">[01:14:05]</a>.

This approach offers an "arbitrage opportunity" for early adopters to gain significant returns before this strategy becomes commonplace <a class="yt-timestamp" data-t="01:02:53">[01:02:53]</a>.