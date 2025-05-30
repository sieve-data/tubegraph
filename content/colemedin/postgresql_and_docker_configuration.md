---
title: PostgreSQL and Docker configuration
videoId: V_0dNE-H2gw
---

From: [[colemedin]] <br/> 

The n8n team has developed a self-hosted AI starter kit that includes PostgreSQL as a core component for local AI infrastructure <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. This package aims to provide everything needed for local AI, featuring Olama for LLMs, Qdrant for the vector database, PostgreSQL for the SQL database, and n8n for workflow automations <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>.

## Setting Up the Environment

To get started with the self-hosted AI starter kit, you will need Git and Docker installed on your system <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. Docker Desktop is recommended as it includes Docker Compose, which is necessary to orchestrate all the services together <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

The project is hosted on GitHub <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a> and can be downloaded by copying the `git clone` command from the repository <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. After cloning, navigate into the new repository directory <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

The repository primarily contains two important files:
*   `.env` file: Used to set credentials for services like PostgreSQL <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.
*   `docker-compose.yaml` file: Brings together all services, including PostgreSQL, Qdrant, and Olama, into a single package for local AI <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Editing Environment Variables

Before running the Docker Compose setup, you need to configure the `.env` file. You will set your PostgreSQL username, password, and database name in this file <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>. Additionally, n8n secrets should be defined as long alphanumeric strings <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>.

### Docker Compose Adjustments for PostgreSQL

The default `docker-compose.yaml` file for the self-hosted AI starter kit does not expose the PostgreSQL container's port by default <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>. This prevents external services, such as n8n workflows, from directly accessing PostgreSQL as a database, for example, for chat memory <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

To rectify this, add the following lines under the `postgres` service in your `docker-compose.yaml` file:

```yaml
ports:
  - "5432:5432"
```
This maps port 5432 inside the container to port 5432 on your local machine, allowing you to access PostgreSQL via `localhost:5432` <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>.

## Running the Docker Compose Services

Once the configuration is complete, you can start the services using a Docker Compose command tailored to your system's architecture <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>:
*   **Nvidia GPU users**: Follow specific instructions for a GPU Nvidia profile <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Mac users**: Use a specific command for Mac <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Everyone else (including CPU-only on Nvidia)**: Use `docker compose --profile CPU up` <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

On the first run, Docker will pull the necessary images for Olama, PostgreSQL, n8n, and Qdrant, and then start them up <a class="yt-timestamp" data-t="00:06:00">[00:06:00]</a>. This process will take some time as it includes downloading large models like Llama 3.1 for Olama <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Verifying Services in Docker Desktop

After running the command, you can open Docker Desktop to verify that all four containers for the local AI services are running under the "self-hosted AI starter kit" <a class="yt-timestamp" data-t="00:06:41">[00:06:41]</a>. You can click into each container to view its output logs or use the "Exec" tab to run Linux commands directly within the container <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. For instance, you can run commands in the PostgreSQL container to query tables <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

## Using PostgreSQL for n8n Chat Memory

The self-hosted n8n instance can be accessed at `localhost:5678` <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>. In n8n workflows, PostgreSQL can be configured as the chat memory for AI agents <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>.

When setting up PostgreSQL credentials in n8n for chat memory:
*   **Host**: Use `host.docker.internal`. This is crucial for n8n within the Docker container to communicate with other services like PostgreSQL running on the host machine <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Database Name, User, and Password**: These should match the values defined in your `.env` file <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.
*   **Port**: The standard PostgreSQL port is `5432` <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

n8n will automatically create the necessary table in your PostgreSQL database based on the table name you provide <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Future Expansions

While the current setup provides a robust starting point, future enhancements could include integrating services like Redis for caching or using a [[selfhosting_supabase_with_docker | self-hosted Supabase]] instance instead of vanilla PostgreSQL <a class="yt-timestamp" data-t="00:19:43">[00:19:43]</a>. [[selfhosting_supabase_with_docker | Supabase]] could offer additional functionalities like authentication handling <a class="yt-timestamp" data-t="00:19:47">[00:19:47]</a>. The goal is to evolve this into a comprehensive local AI tech stack, potentially incorporating a front-end and baking in best practices for RAG (Retrieval Augmented Generation) and LLMs <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.