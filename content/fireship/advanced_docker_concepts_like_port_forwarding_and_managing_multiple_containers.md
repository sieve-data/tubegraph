---
title: Advanced Docker concepts like port forwarding and managing multiple containers
videoId: gAkwW2tuIqE
---

From: [[fireship]] <br/> 

[[introduction_to_docker_and_its_importance_for_developers | Docker]] is a tool for packaging software so it can run on any hardware, addressing issues like "it works on my machine" by reproducing environments <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Developers define the environment with a [[understanding_docker_files_images_and_containers | Dockerfile]], which is then used to build an [[understanding_docker_files_images_and_containers | image]] (an immutable snapshot) <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. [[understanding_docker_files_images_and_containers | Images]] can be uploaded to public or private registries <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>, and any developer or server can pull the [[understanding_docker_files_images_and_containers | image]] to create a [[understanding_docker_files_images_and_containers | container]] <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Docker Installation and Setup
For Mac or Windows, installing the Docker Desktop application is highly recommended as it provides command-line tools and a GUI <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. After [[stepbystep_instructions_for_docker_installation_and_setup | Docker installation and setup]], the `docker ps` command can list all running [[understanding_docker_files_images_and_containers | containers]] <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. Each [[understanding_docker_files_images_and_containers | container]] has a unique ID and is linked to an [[understanding_docker_files_images_and_containers | image]] <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. Installing the Docker extension for VS Code or your IDE provides language support for [[understanding_docker_files_images_and_containers | Dockerfiles]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Containerizing a Node.js Application
A [[handson_guide_to_containerizing_a_nodejs_application | Node.js application]] is used as an example, consisting of a single `index.js` file that exposes an API endpoint and uses a `PORT` environment variable <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

### Dockerfile Instructions
A [[understanding_docker_files_images_and_containers | Dockerfile]] specifies instructions for building a Docker [[understanding_docker_files_images_and_containers | image]] <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

*   **`FROM`**: Specifies the base [[understanding_docker_files_images_and_containers | image]]. While starting from scratch is possible, most [[understanding_docker_files_images_and_containers | Dockerfiles]] begin with a base [[understanding_docker_files_images_and_containers | image]], such as the official Node.js version 12 [[understanding_docker_files_images_and_containers | image]] <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
*   **`WORKDIR`**: Sets the working directory for subsequent instructions, similar to `cd` <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   **Layer Caching**: Each instruction in a [[understanding_docker_files_images_and_containers | Dockerfile]] is a separate layer, and Docker attempts to cache layers if nothing has changed, making builds more efficient <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.
*   **Dependency Management**: To optimize caching, dependencies (e.g., `package.json`) are copied and installed *before* the application source code <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>.
    *   **`COPY`**: Copies files from the local machine to the [[understanding_docker_files_images_and_containers | container]]. For example, `COPY package.json .` copies the `package.json` file to the current working directory in the [[understanding_docker_files_images_and_containers | container]] <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   **`RUN`**: Executes a command inside the [[understanding_docker_files_images_and_containers | container]], such as `npm install` <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   **`.dockerignore`**: Similar to `.gitignore`, this file specifies files or directories (like `node_modules`) that should be ignored when copying files into the [[understanding_docker_files_images_and_containers | image]] <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.
*   **`ENV`**: Sets environment variables within the [[understanding_docker_files_images_and_containers | container]] <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   **`EXPOSE`**: Declares that the [[understanding_docker_files_images_and_containers | container]] will listen on specified network ports at runtime. This does not automatically publish the port <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **`CMD`**: The final instruction in a [[understanding_docker_files_images_and_containers | Dockerfile]], it tells the [[understanding_docker_files_images_and_containers | container]] how to run the application (e.g., `node index.js`) <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. It's preferred to use "exec form" (an array of strings) which doesn't start a shell session <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Building and Running Docker Images
*   **`docker build`**: Used to build a Docker [[understanding_docker_files_images_and_containers | image]] <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
    *   The `-t` or `--tag` flag assigns a name tag (e.g., `fireship/demo-app:1.0.0`) for easy identification <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>.
    *   The command `docker build -t fireship/demo-app:1.0.0 .` builds the [[understanding_docker_files_images_and_containers | image]] from the current directory <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
*   **`docker push`**: Used to upload an [[understanding_docker_files_images_and_containers | image]] to a container registry (e.g., Docker Hub) <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
*   **`docker pull`**: Used by other developers or servers to download an [[understanding_docker_files_images_and_containers | image]] from a registry <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.
*   **`docker run`**: Creates a running process (a [[understanding_docker_files_images_and_containers | container]]) from a Docker [[understanding_docker_files_images_and_containers | image]] <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.

## Port Forwarding
Even if a port is `EXPOSE`d in the [[understanding_docker_files_images_and_containers | Dockerfile]], it's not automatically accessible to the outside world <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.

*   The `-p` flag in `docker run` implements port forwarding.
*   It maps a port on the local machine to a port on the Docker [[understanding_docker_files_images_and_containers | container]] <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   Example: `docker run -p 5000:8080 fireship/demo-app` maps local port `5000` to [[understanding_docker_files_images_and_containers | container]] port `8080` <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

## Managing Data with Volumes
When a [[understanding_docker_files_images_and_containers | container]] is stopped, any state or data created inside it is lost <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

*   **Volumes** are the preferred way to share and persist data across multiple [[understanding_docker_files_images_and_containers | containers]] <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   A volume is a dedicated folder on the host machine where a [[understanding_docker_files_images_and_links | container]] can create files <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.
*   Files in a volume persist even after [[understanding_docker_files_images_and_links | containers]] are shut down, and multiple [[understanding_docker_files_images_and_links | containers]] can mount and access the same volume simultaneously <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **`docker volume create`**: Used to create a new volume <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

## Debugging Containers
*   **Docker Desktop Dashboard**: Provides access to [[understanding_docker_files_images_and_links | container]] logs and allows executing commands within a running [[understanding_docker_files_images_and_links | container]] <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **`docker exec`**: Allows executing commands inside a running [[understanding_docker_files_images_and_links | container]] from the command line <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.

## Managing Multiple Containers with Docker Compose
For applications requiring multiple processes, it's best practice to use multiple [[understanding_docker_files_images_and_links | containers]], each running a single process <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. [[introduction_to_docker_and_its_importance_for_developers | Docker]] Compose is a tool designed to manage and run multiple Docker [[understanding_docker_files_images_and_links | containers]] simultaneously <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

*   **`docker-compose.yaml`**: A YAML file used to define the services (containers), networks, and volumes for a multi-[[understanding_docker_files_images_and_links | container]] application <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.
    *   The `services` object defines each [[understanding_docker_files_images_and_links | container]] to be run, such as a `web` service for the Node.js app and a `db` service for a MySQL database <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
    *   The `build` key points to the [[understanding_docker_files_images_and_links | Dockerfile]]'s location <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
    *   Port forwarding (`ports`) and volume mounting (`volumes`) can be configured directly within the `docker-compose.yaml` file <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
*   **`docker compose up`**: Reads the `docker-compose.yaml` file and starts all defined [[understanding_docker_files_images_and_links | containers]] together <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **`docker compose down`**: Shuts down all [[understanding_docker_files_images_and_links | containers]] defined in the `docker-compose.yaml` file <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.