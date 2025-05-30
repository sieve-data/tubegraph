---
title: Installation and setup of autod Dev with Docker
videoId: 31ivQdydmGg
---

From: [[colemedin]] <br/> 

[[upcoming_strategic_partnership_for_autod_dev | Autod Dev]], initially forked from bolt.new as `bolt.new-any-llm`, has rapidly grown, fostering a large community since its inception just three weeks ago [00:00:00]. The project was created to enable users to integrate various Large Language Models (LLMs), including [[using_local_large_language_models_with_autod_dev | local LLMs with Ollama]], into bolt.new [00:00:14]. The project has since been renamed to Autod Dev to keep it distinct while still allowing for a potential future merge with the main bolt.new repository [00:01:33]. The primary mission of [[roadmap_and_development_progress_of_autod_dev | Autod Dev]] is to become the leading open-source AI coding assistant [00:02:37].

This guide provides a step-by-step process for installing and running Autod Dev using Docker, which is the recommended method for ease of setup and consistent operation [00:03:02].

## Initial Setup Prerequisites

Regardless of whether you choose to run Autod Dev with or without Docker, certain prerequisites are necessary.

### 1. Git

You must install Git to clone the [[roadmap_and_development_of_autod_dev | Autod Dev]] GitHub repository [00:04:14].
*   Download Git from `git-scm.com` [00:04:25]. The website typically recommends the correct version for your operating system [00:04:34].

### 2. Node.js

Node.js is required for running certain `npm` commands used in the setup process [00:04:42].
*   Download Node.js from `nodejs.org` [00:04:45]. Installation is generally straightforward [00:04:50].
*   You can verify Node.js is in your system path by checking if Node commands work [00:04:52].

### 3. Clone the Autod Dev Repository

Once Git is installed, you can clone the [[roadmap_and_development_progress_of_autod_dev | Autod Dev]] GitHub repository to your local machine:
*   Open a terminal and use the `git clone` command found in the project's README or video description [00:05:14].
*   Example command: `git clone https://github.com/autod-dev/autod-dev.git` [00:05:16].

### 4. Configure API Keys

If you plan to use any Large Language Models that require API keys (e.g., GPT, OpenRouter), you need to set these up [00:05:47].
*   Locate the `env.example` file at the root of the cloned repository [00:06:09].
*   Fill in the API keys for the providers you intend to use [00:06:16]. For example, if using GPT, input your OpenAI API key; for OpenRouter, input its API key [00:06:25]. You do not need to set keys for providers you won't use [00:06:42].
*   After filling in the necessary keys, rename the file from `env.example` to `.env` [00:06:22].

## Running Autod Dev with Docker

Docker is highly recommended for running Autod Dev because it provides an isolated environment, ensuring a consistent setup across different systems and avoiding common issues like missing modules or access violations [00:08:20].

### 1. Docker Installation

*   Install Docker on your machine [00:07:35]. The recommended way is to install Docker Desktop from `docker.com` [00:07:37].
*   Docker Desktop provides a user-friendly interface and typically installs Docker Compose, which is used to run multiple containers together [00:07:56].

### 2. Build the Docker Container

Once Docker is installed, navigate to the cloned Autod Dev repository in your terminal.
*   **For Development Environment**: Run the `npm run docker:build` command [00:09:06].
    *   `npm run docker:build` [00:09:10]
    *   This command will build the Docker container. The first time you run it, it will take some time; subsequent builds will be faster due to caching [00:09:18].
*   **Alternative (without Node.js/npm)**: If you prefer not to install Node.js, you can run the Docker commands directly as an alternative to the `npm` helper scripts [00:10:05].

### 3. Run the Docker Container

After building the container, you can run Autod Dev using Docker Compose with profiles.
*   **For Development Environment**: Execute the `npm run docker:dev` command [00:10:37].
    *   `npm run docker:dev` [00:10:39]
    *   This command will start Autod Dev, and your terminal will display output from the backend, similar to running it without Docker [00:11:03].
    *   You might see warnings for any API keys not set in your `.env` file [00:10:52].

## Accessing Autod Dev

Once the Docker container is running, you can access the Autod Dev user interface:
*   Open your web browser and navigate to `localhost:5173` [00:11:17].
*   **Browser Compatibility**:
    *   If you are using Google Chrome, you may need to install Google Chrome Canary, a web development browser, as standard Chrome might not work with bolt.new (which Autod Dev is based on) [00:11:25].
    *   Firefox users, especially on Linux, should not encounter issues and can use their standard browser [00:11:41].

## Next Steps and Contribution

This guide aims to make it as easy as possible for everyone to get Autod Dev up and running, encouraging more engagement and contributions [00:12:20]. The project is continuously improving [00:12:48].

Future videos will cover more advanced topics such as:
*   Making changes and contributing to the repository [00:11:59].
*   Attaching a debugger for feature development [00:12:08].
*   Creating pull requests [00:12:13].

The project strongly encourages community involvement to build a powerful and accessible AI coding assistant [00:12:39].

### Community and Engagement

*   A Discourse Community for Autod Dev is launching on Sunday, November 10th, and will be a platform for collaboration [00:02:03].
*   Applications to become [[core_contributor_applications_for_autod_dev | a core contributor]] to Autod Dev are open, with significant interest already [00:01:08]. The project is seeking ways to involve all interested individuals [00:01:20].
*   A live stream event is planned for Sunday, November 10th, at 7:00 p.m. Central Time to discuss updates and announcements [00:00:48].