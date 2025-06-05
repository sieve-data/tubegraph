---
title: Debugging and Inspecting Docker Containers
videoId: gAkwW2tuIqE
---

From: [[fireship]] <br/> 

When working with Docker, understanding how to debug and inspect your containers is crucial for troubleshooting and maintaining healthy applications <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

## Tools for Debugging

Several tools and techniques can assist in [[developer_productivity_tools | debugging]] and inspecting Docker containers:

*   **Docker Desktop Application** The Docker Desktop application (available for Mac and Windows) provides a graphical user interface (GUI) to inspect running containers <a class="yt-timestamp" data-t="02:03">[00:02:03]</a>. This dashboard allows you to:
    *   View all logs directly from a running container <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
    *   Search through logs <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
    *   Execute commands inside your container by clicking the "CLI" button <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Docker Extension for VS Code/IDE** Installing the Docker extension for your Integrated Development Environment (IDE), such as [[Debugging with VS Code | VS Code]], provides language support for Dockerfiles and can link to remote registries <a class="yt-timestamp" data-t="02:22">[00:02:22]</a>.
*   **Command Line Interface (CLI)**
    *   The `docker ps` command lists all running containers on your system, showing their unique IDs and linked images <a class="yt-timestamp" data-t="02:09">[00:02:09]</a>.
    *   The `docker exec` command allows you to execute commands directly within a running container from your own command line <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This puts you in the root of the container's file system, enabling you to `ls` files or interact with the Linux environment <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Inspecting Container Logs

When an application inside a container doesn't behave as expected, one of the first steps is to inspect its logs <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>. Using Docker Desktop, you can click on a running container to see all its logs <a class="yt-timestamp" data-t="00:08:56">[00:08:56]</a>.

## Best Practices for Healthy Containers

To maintain healthy and debuggable containers, it is recommended to:

*   **Write Simple, Maintainable Microservices**: Each container should ideally run only one process <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>.
*   **Use Multiple Containers for Multiple Processes**: If your application requires multiple processes, it should be structured to use multiple containers, which can then be orchestrated using tools like [[Working with Volumes and Docker Compose | Docker Compose]] <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. This approach aligns with [[DevOps practices | DevOps practices]] by promoting isolation and easier troubleshooting.