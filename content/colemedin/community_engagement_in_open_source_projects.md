---
title: Community engagement in open source projects
videoId: 31ivQdydmGg
---

From: [[colemedin]] <br/> 

The `bolt.new any llm` project, a [[forking_open_source_platforms_for_custom_modifications | fork]] of Bolt.new, has seen rapid growth in community involvement since its inception three weeks prior to the update [00:00:00]. Initially designed to help users integrate various Large Language Models (LLMs), including local ones with Ollama, into Bolt.new [00:00:12], the project has quickly become a massive [[community_contributions_to_software_development | community-driven]] effort [00:00:21]. The project is now planned to be renamed to `autodev` [00:01:34].

## Project Evolution and Mission
The project's original aim was to facilitate LLM integration within Bolt.new [00:00:12]. Due to its rapid growth, the project is planned for renaming to `autodev` to maintain its distinct identity while potentially merging with the main Bolt.new repository in the future [00:01:34]. The ultimate mission is to create the best [[open_source_development | open-source]] AI coding assistant available [00:02:37].

## Direct [[community_contributions_to_software_development | Community Contributions]]
The project actively encourages and integrates [[community_engagement_and_contributions | community contributions]]:

### Core Contributors
Applications were opened for core contributors to `bolt.new any llm`, receiving 36 applications [00:01:08]. The project leader emphasizes the importance of these individuals in sustaining growth, as the project has become larger than what one person can manage alone [00:01:25]. Efforts are being made to involve all applicants heavily [00:01:20].

### Development and Improvements
The community has directly contributed to key developments, such as the easy Docker setup for running the application [00:07:22]. This [[community_involvement_in_bolt_diy_project | community involvement]] ensures the project continues to develop and helps users code better and faster [00:02:56].

## [[community_and_networking_through_discourse | Community and Networking]] Platforms

### Live Streams
Regular live streams are held to provide updates and engage with the community [00:00:30]. A major live stream is scheduled for Sunday, November 10th at 7:00 p.m. Central Time, replacing the usual Sunday video [00:00:48].

### Discourse Community
A dedicated Discourse community for `autodev` is set to launch on Sunday, November 10th [00:02:02]. This platform is being set up to be an awesome place for collaboration, ensuring core contributors are engaged from the start to hit the ground running [00:02:16].

## Facilitating [[community_engagement_and_contributions | Community Engagement]]: Running Autodev with Docker
To maximize [[community_engagement_and_contributions | community engagement]] and contributions, the project aims to make it as easy as possible for users to get up and running with `autodev` [00:03:20]. A comprehensive step-by-step guide is provided for non-technical users to run `autodev` using Docker [00:03:02].

### Why Docker is Recommended
Docker provides an isolated environment, ensuring all necessary components to run `autodev` are installed within the container [00:08:20]. This helps avoid common issues like access violations, missing modules, or API key errors that can arise from different system configurations when running without Docker [00:08:33]. Running with Docker guarantees the same setup as a perfectly working environment [00:08:53].

### Setup Instructions (Running with Docker)
Instructions are available in the video description and the `autodev` GitHub repository's README [00:03:31].

#### Prerequisites
1.  **Git**: Required to clone the GitHub repository [00:04:17]. Download from `git-scm.com` [00:04:25].
2.  **Node.js**: Necessary for project commands [00:04:42]. Download from `nodejs.org` [00:04:45].
3.  **Docker**: Essential for containerization [00:07:29]. Docker Desktop is recommended for its user interface and automatic Docker Compose installation [00:07:42].

#### Initial Setup
1.  **Clone the Repository**:
    ```bash
    git clone [repository_url]
    ```
    This command pulls all the `autodev` code onto the local machine [00:05:14].
2.  **Set Up API Keys**:
    *   Locate the `env.example` file at the root of the repository [00:06:01].
    *   Fill in API keys for desired LLM providers (e.g., GPT, OpenRouter) [00:06:16].
    *   Rename `env.example` to `.env` [00:06:19]. Unused API keys do not need to be set [00:06:42].

#### Running with Docker
1.  **Build the Docker Container (Development Environment)**:
    ```bash
    npm run docker:build
    ```
    This command builds the container, installing all necessary dependencies within the isolated Docker environment [00:09:06]. Building for the first time will take longer [00:09:19].
    *   *Alternative*: Direct Docker commands can be used instead of `npm` scripts if Node.js is not installed [00:10:09].
2.  **Start Autodev with Docker Compose**:
    ```bash
    docker compose --profile development up
    ```
    This command spins up the `autodev` container [00:10:25]. The terminal will display output from the backend and wait for more [00:11:03].
3.  **Access Autodev**: Visit `localhost:5173` in a web browser [00:11:17].
    *   **Browser Requirement**: Google Chrome Canary is recommended for Chrome users, as standard Google Chrome may not work with Bolt.new (not an Autodev-specific issue) [00:11:25]. Firefox also works [00:11:41].

## Future Outlook and Call to Action
The project encourages users to get involved, as together, they are building a powerful AI coding assistant accessible to everyone [00:12:39]. While currently not perfect, it is improving weekly [00:12:46]. The leader plans to create future videos detailing how to make changes, attach debuggers, and create pull requests to further facilitate [[open_source_development | community contributions]] [00:11:59]. Queries and concerns about the project are welcomed in the comments [00:12:51].