---
title: AI coding assistant development
videoId: 31ivQdydmGg
---

From: [[colemedin]] <br/> 

[[opensource_ai_coding_assistant_development | Autodev]], initially forked as `bolt.new any llm` from `bolt.new`, has rapidly grown in popularity within just three weeks of its inception <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The project began as a way to enable users to integrate various Large Language Models (LLMs), including local ones via Ollama, into `bolt.new` <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. In a short period, a large community has formed around the project, contributing to its rapid development <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.

## Project Updates and Community Engagement
The project regularly provides updates and announcements <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. A live stream was planned for November 10th at 7:00 p.m. Central Time to discuss major updates and announcements <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>.

Applications to become a core contributor to `bolt.new any llm` (now [[opensource_ai_coding_assistant_development | Autodev]]) quickly reached 36 applicants, highlighting significant community interest and involvement <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. This community support is crucial for the project's continued growth, as it has already become larger than a single individual can manage <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>.

### Renaming to Autodev
The project is being renamed from `bolt.new any llm` to [[opensource_ai_coding_assistant_development | Autodev]] <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>. While a merge with the main `bolt.new` repository might occur in the future, maintaining distinction for `Autodev` is currently important due to its unique developments <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. The new name also aligns with other related projects under development <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

### New Discourse Community
A Discourse community for [[opensource_ai_coding_assistant_development | Autodev]] is set to launch on Sunday, November 10th <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This platform is designed to facilitate collaboration and will be a key feature showcased during the live stream <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. The community was launched with core contributors already engaged to ensure a strong start <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

The overarching mission of the project is to create the best [[opensource_ai_coding_assistant_development | open-source AI coding assistant]] <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>. The project is continuously improving, especially with the launch of the Discourse community and increased contributor involvement, which is expected to help users code better and faster <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## Running [[opensource_ai_coding_assistant_development | Autodev]] with Docker
The project aims to make it as easy as possible for individuals, including non-technical users, to get `Autodev` up and running, thereby encouraging engagement and contributions <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. Instructions for running `Autodev` with Docker are available in the video description and the GitHub repository's README <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Docker is the recommended method due to its ease of use and ability to provide a consistent environment <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>.

### Initial Setup Prerequisites
Before running `Autodev` with Docker, the following prerequisites must be installed:

*   **Git:** Required to clone the GitHub repository <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. It can be downloaded from git-scm.com <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   **Node.js:** Essential for running `npm` commands <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. It can be downloaded from nodejs.org <a class="yt-timestamp" data-t="00:04:45">[00:04:45]</a>.
*   **Docker:** Recommended to install Docker Desktop, which includes Docker Compose, a tool for managing multi-container Docker applications <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>. Docker provides an isolated environment, ensuring that `Autodev` runs consistently across different systems, avoiding common issues like access violations or missing modules encountered when running without Docker <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.

### Cloning the Repository
Once Git is installed, the `Autodev` GitHub repository can be cloned using the command:
```bash
git clone <repository_url>
```
This command downloads all the `Autodev` code to the local machine <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### Setting Up API Keys
To use LLMs that require API keys (e.g., GPT, Open Router), users need to configure their API keys <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
1.  Locate the `env.example` file at the root of the repository <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>.
2.  Fill in the API keys for the desired providers (e.g., OpenAI, Open Router) <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>. Only necessary keys need to be set <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>.
3.  Rename the file to `.env` <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>.

### Building and Running the Docker Container
With prerequisites and API keys set up, `Autodev` can be built and run using Docker.

1.  **Build the Docker Container:** For a development environment, run the following `npm` command in the terminal:
    ```bash
    npm run docker:build
    ```
    This command initiates the container build process, which may take some time during the first run <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Alternatively, direct Docker commands can be used, bypassing the need for Node.js installation <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.

2.  **Run the Docker Container:** To start `Autodev` on the machine using Docker Compose profiles for the development environment, execute this command:
    ```bash
    docker compose --profile dev up
    ```
    This command will spin up the `Autodev` application within the Docker container <a class="yt-timestamp" data-t="00:10:25">[00:10:25]</a>. It will display warnings for any API keys not set in the `.env` file <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. The terminal will then show output from the `Autodev` backend, indicating it's running <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>.

    Once running, `Autodev` can be accessed in a web browser at `localhost:5173` <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.

    > [!NOTE] Browser Compatibility
    > Google Chrome does not work with `bolt.new` or `Autodev`; users should install Google Chrome Canary for web development <a class="yt-timestamp" data-t="00:11:25">[00:11:25]</a>. Firefox, especially on Linux, is also compatible <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.

## Future Development and Contributions
Future videos will cover advanced topics such as making changes to the repository, attaching debuggers, and creating pull requests to contribute to `Autodev` <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. The project actively encourages user involvement, as community contributions are vital for building a powerful and accessible [[ai_coding_assistants | AI coding assistant]] <a class="yt-timestamp" data-t="00:12:37">[00:12:37]</a>. Despite not being perfect yet, `Autodev` continues to improve weekly <a class="yt-timestamp" data-t="00:12:48">[00:12:48]</a>.