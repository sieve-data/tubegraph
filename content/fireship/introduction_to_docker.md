---
title: Introduction to Docker
videoId: gAkwW2tuIqE
---

From: [[fireship]] <br/> 

Docker is a method for packaging software so it can run on any hardware <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. It addresses the common problem of software working on one machine but not another due to environmental differences <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>, aiming to reproduce environments consistently <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Core Concepts

Understanding Docker involves three fundamental concepts:
*   **Dockerfiles** <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>: A blueprint that defines the steps to build a Docker image <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a> <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Developers can define the software environment using a Dockerfile <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Docker Images** <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>: An immutable snapshot and template for running Docker containers <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a> <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Images can be uploaded to public or private cloud registries <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Docker Containers** <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>: A running process of a Docker image <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a> <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. One image can be used to spawn multiple containers in multiple locations <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>.

## Installation and Tooling

To use Docker, it needs to be installed. For Mac or Windows, the Docker Desktop application is recommended <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. This application includes everything needed for the command line and provides a graphical user interface (GUI) to inspect running containers <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

After installation, Docker commands are accessible from the command line <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. A useful first command is `docker ps`, which lists all running containers on the system <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Each container has a unique ID and is linked to an image <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This information is also available in the GUI <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

Installing the Docker extension for VS Code or other IDEs is also recommended. It provides language support for writing Dockerfiles and can link to remote registries <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## [[creating_and_using_dockerfiles | Creating and Using Dockerfiles]]

A Dockerfile contains instructions to build a Docker image and ultimately run an application as a container <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

### Example: Dockerizing a [[introduction_to_nodejs | Node.js]] Application

For a [[introduction_to_nodejs | Node.js]] application, the process involves defining the environment and copying the source code. An example application might have an `index.js` file exposing an API endpoint <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a> and listening on a `PORT` environment variable <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

A Dockerfile is typically created in the project's root directory <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Dockerfile Instructions

Each instruction in a Dockerfile is considered a separate step or layer. Docker attempts to cache layers if nothing has changed, improving efficiency <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

Key instructions include:

*   **`FROM`**: Specifies the base image for the Dockerfile <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   Instead of starting from scratch or a general [[introduction_to_linux | Linux]] distribution like Ubuntu which would require manual [[introduction_to_nodejs | Node.js]] installation <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>, it's better to use an officially supported image like `node:12` for [[introduction_to_nodejs | Node.js]] applications <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>. Tags can be used to specify different variations of a base image <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **`WORKDIR`**: Sets the working directory inside the image for subsequent instructions, similar to `cd` in a terminal <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **`COPY`**: Copies files from the local machine into the image <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   It's generally more efficient to copy `package.json` and install dependencies (e.g., `npm install`) *before* copying the full source code. This allows the dependency layer to be cached unless `package.json` changes <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
    *   After dependencies are installed, the application source code can be copied <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **`.dockerignore`**: Similar to `.gitignore`, this file specifies patterns for files and directories that should be ignored and not copied into the Docker image (e.g., `node_modules`) <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **`ENV`**: Sets environment variables within the container <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **`EXPOSE`**: Informs Docker that the container will listen on a specified network port at runtime <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This does not automatically make the port accessible to the outside world <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   **`CMD`**: The final instruction in a Dockerfile, it tells the container how to run the application by starting a process <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. There can only be one `CMD` instruction per Dockerfile <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. Using "exec form" (an array of strings) is the preferred way, as it doesn't start a shell session <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

## Building and Managing Images

Once a Dockerfile is created, a Docker image can be built using the `docker build` command <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>.
*   The `-t` or `--tag` flag allows assigning a memorable name tag to the image (e.g., `username/imagename:version`) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
*   The command also requires the path to the Dockerfile, often `.` for the current working directory <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   The build process pulls the base image, then executes each step defined in the Dockerfile <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>.

Images can be managed by:
*   `docker push`: Uploads an image to a container registry (like Docker Hub or a cloud provider's registry) <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   `docker pull`: Downloads an image from a registry <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

## [[managing_docker_containers_with_commands | Running and Managing Containers]]

To run a Docker image as a container, use the `docker run` command, specifying the image ID or tag name <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. This creates a running process <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

### Port Forwarding

By default, an `EXPOSE`d port in a container is not accessible to the outside world <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. To make it accessible, use the `-p` flag with `docker run` to implement port forwarding <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This maps a port on the local machine (host) to a port on the Docker container (e.g., `-p 5000:8080` maps local port 5000 to container port 8080) <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

Stopping a container will cause any state or data created inside it to be lost <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## [[debugging_and_inspecting_docker_containers | Debugging and Inspecting Docker Containers]]

For debugging and inspecting containers:
*   **Docker Desktop Dashboard**: Provides a GUI to view container logs and search through them <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **`docker logs`**: Command-line equivalent for viewing container logs.
*   **`docker exec`**: Allows executing commands inside a running container, providing command-line access to its [[introduction_to_linux | Linux]] environment <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This can also be done via the Docker Desktop CLI button <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

For container health, it's recommended to write simple, maintainable microservices where each container runs only one process <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>. If an application requires multiple processes, multiple containers should be used <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

## [[working_with_volumes_and_docker_compose | Volumes and Docker Compose]]

### Volumes

Volumes are the preferred way to share data across multiple containers and persist data after containers are shut down <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>. A volume is a dedicated folder on the host machine where a container can create files <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. This folder can be remounted into future containers or shared by multiple containers simultaneously <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.

To create a volume, use the `docker volume create` command <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### Docker Compose

[[working_with_volumes_and_docker_compose | Docker Compose]] is a tool designed to run multiple Docker containers together <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. It uses a `docker-compose.yaml` file (placed in the project root) to define and configure multiple services (containers) and volumes <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

Example `docker-compose.yaml` structure:
*   **`services` object**: Each key in this object represents a different container to run <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
    *   A "web" service might define the [[introduction_to_nodejs | Node.js]] app, pointing to its Dockerfile with `build: .` and setting port forwarding <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>.
    *   A "db" service could define a database container, such as MySQL <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.
*   **`volumes` definition**: Defines volumes to store persistent data, like database data <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. These volumes can then be mounted into the respective service containers <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

With this configuration, `docker compose up` will find the `docker-compose.yaml` file and run all defined containers together <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. `docker compose down` can then be used to shut down all containers together <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.