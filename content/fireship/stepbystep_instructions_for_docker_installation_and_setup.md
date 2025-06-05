---
title: Stepbystep instructions for Docker installation and setup
videoId: gAkwW2tuIqE
---

From: [[fireship]] <br/> 

One of the leading causes of imposter syndrome among developers is not knowing [[introduction_to_docker_and_its_importance_for_developers | Docker]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This guide will help you understand and set up Docker to survive as a developer <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>. It takes a hands-on approach by [[handson_guide_to_containerizing_a_nodejs_application | containerizing a Node.js application]] <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## What is Docker?

From a practical standpoint, [[introduction_to_docker_and_its_importance_for_developers | Docker]] is a way to package software so it can run on any hardware <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. The whole point of Docker is to solve problems where an application works on one machine but breaks on another due to different environments <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Docker achieves this by reproducing environments <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.

### Core Concepts: Dockerfiles, Images, and Containers

To understand how Docker works, three things are essential to know: [[understanding_docker_files_images_and_containers | Dockerfiles]], [[understanding_docker_files_images_and_containers | images]], and [[understanding_docker_files_images_and_containers | containers]] <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

*   **Dockerfile:** A blueprint for building a Docker image <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. The developer defines the environment for the software using a Dockerfile <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
*   **Image:** A template for running Docker containers <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It's an immutable snapshot of the environment built from a Dockerfile <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Images can be uploaded to public or private registries in the cloud <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Container:** A running process of a Docker image <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Any developer or server can pull an image down to create a container <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>. One image file can spawn the same process multiple times in multiple places <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Tools like Kubernetes and Swarm can scale containers to an infinite workload <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Docker Installation

The best way to learn Docker is by using it, and that requires installation <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Docker Desktop Application

For Mac or Windows users, it is highly recommended to install the Docker Desktop application <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.
*   It installs everything needed for the command line <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
*   It provides a GUI to inspect running containers <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

Once installed, Docker should be accessible from the command line <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.
The first command to memorize is `docker ps`, which lists all running containers on the system <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. Each container has a unique ID and is linked to an image <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This information is also available in the GUI <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### VS Code Docker Extension

It's also advisable to install the Docker extension for VS Code or your preferred IDE <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. This provides language support when writing [[understanding_docker_files_images_and_containers | Dockerfiles]] and can link to remote registries <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Building a Dockerfile for a Node.js Application

A Dockerfile contains the code to build a Docker image and ultimately run an app as a container <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. For this example, we'll containerize a simple Node.js application with an `index.js` file that exposes an API endpoint <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

Create a `Dockerfile` in the root of your project <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Key Dockerfile Instructions

1.  **`FROM`**:
    *   This is the first instruction in a Dockerfile <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
    *   While you could start from scratch, most [[understanding_docker_files_images_and_containers | Dockerfiles]] begin with a specific base image <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>.
    *   For a Node.js application, it's best to use the officially supported [[installing_and_setting_up_nodejs | Node.js]] image (e.g., `node:12`) which provides everything needed for Node.js <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

2.  **`WORKDIR`**:
    *   Sets the working directory for any subsequent instructions <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. It's similar to `cd` into a directory <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
    *   Example: `WORKDIR /app` <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

3.  **Layer Caching and `COPY`/`RUN` Order**:
    *   Every instruction in a Dockerfile is considered its own step or layer, and Docker attempts to cache layers if nothing has changed <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.
    *   To keep things efficient, install dependencies *before* copying the entire application source code <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This prevents reinstalling `node_modules` every time the app's source code changes <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

    *   **`COPY package.json .`**: Copies the local `package.json` file to the current working directory in the container <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
    *   **`RUN npm install`**: Executes the `npm install` command inside the container, just like in a terminal session <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. The results are committed to the Docker image as a layer <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

    *   **`COPY . .`**: Copies all local files to the current working directory in the container <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
        *   **`.dockerignore`**: To prevent local `node_modules` from being copied over and overriding the installed dependencies in the image, create a `.dockerignore` file and add `node_modules` to it <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. It works like a `.gitignore` file <a class="yt-timestamp" data-t="00:05:16">[00:05:16]</a>.

4.  **`ENV`**:
    *   Sets environment variables within the container <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
    *   Example: `ENV PORT=8080` to set the port for the Node.js application <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.

5.  **`EXPOSE`**:
    *   Informs Docker that the container will be listening on the specified network ports at runtime <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
    *   Example: `EXPOSE 8080` <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

6.  **`CMD`**:
    *   The final instruction, only one allowed per Dockerfile <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.
    *   Tells the container how to run the actual application by starting a process <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>.
    *   Use "exec form" (array of strings) as it's the preferred way and doesn't start a shell session <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.
    *   Example: `CMD ["node", "index.js"]` <a class="yt-timestamp" data-t="00:05:46">[00:05:46]</a>.

## Building a Docker Image

Once the Dockerfile is complete, the next step is to build the Docker image <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### `docker build` Command

*   Use `docker build` to create an image <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **`-t` (tag)**: Gives the image a memorable name and tag <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>.
    *   It's recommended to set up a username on Docker Hub and use the format `username/imagename` (e.g., `fireship/demoapp`) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. A version number can also be added with a colon (e.g., `fireship/demoapp:1.0`) <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.
*   **Path to Dockerfile**: Specify the path to the Dockerfile, often `.` for the current working directory <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

**Example:**
`docker build -t fireship/demoapp:1.0 .` <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>

When executed, Docker will pull the base image, go through each step in the Dockerfile, and confirm a successful build with an image ID <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. This image can then be pushed to a container registry (like Docker Hub or a cloud provider) using `docker push` <a class="yt-timestamp" data-t="00:06:55">[00:06:55]</a>, or pulled down by others using `docker pull` <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>.

## Running a Docker Container

To run the image locally as a container <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>:

### `docker run` Command

*   Use `docker run` followed by the image ID or tag name <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>.
*   This creates a running process called a container <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.

**Initial Problem: Local Access**
Even if the application is listening on a port (e.g., 8080) inside the container, it's not accessible to the outside world by default <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Port Forwarding with `-p`

To access the container locally, use the `-p` (port forwarding) flag <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>:
*   Map a port on your local machine to a port on the Docker container.
*   Format: `-p <local_port>:<container_port>`

**Example:**
`docker run -p 5000:8080 fireship/demoapp:1.0` <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>
Now, the app should be accessible at `localhost:5000` in the browser <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

### Stopping Containers

*   Containers continue running even after the terminal window is closed <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   Use the Docker Desktop dashboard to stop containers <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   Be aware that any state or data created inside the container will be lost when it's stopped <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Managing Data with Volumes

To share data across multiple containers or persist data after a container stops, use [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | Docker volumes]] <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a>.
*   A volume is a dedicated folder on the host machine <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.
*   Containers can create files in this folder that can be remounted into future or multiple containers simultaneously <a class="yt-timestamp" data-t="00:08:20">[00:08:20]</a>.
*   Files in a volume stick around even after all containers are shut down <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

### Creating and Mounting Volumes

*   **Create**: `docker volume create <volume_name>` <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Mount**: During `docker run`, use the `-v` flag: `-v <volume_name>:<container_path>` <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>.

## Debugging Containers

When things don't go as planned, you might need to inspect logs or access the container's command line <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

*   **Docker Desktop**: Click on a running container to view its logs and search through them <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   **CLI Access**: Use the "CLI" button in Docker Desktop, or the `docker exec` command from your own command line, to get a shell session inside the container <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This allows you to `ls` files or run other Linux commands <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## Managing Multiple Containers with Docker Compose

For applications requiring multiple processes, like a Node.js app needing a database, it's best to use multiple containers <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | Docker Compose]] is designed for this <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. It's a tool for running multiple Docker containers simultaneously <a class="yt-timestamp" data-t="00:09:34">[00:09:34]</a>.

### `docker-compose.yaml`

Define your multi-container application in a `docker-compose.yaml` file at the root of your project <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

*   **`services` object**: Each key in this object represents a different container to run <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>.
    *   **`web` service (Node.js app)**:
        *   `build: .`: Points to the current working directory where the Dockerfile is located <a class="yt-timestamp" data-t="00:10:04">[00:10:04]</a>.
        *   `ports: "5000:8080"`: Defines the [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | port forwarding]] configuration <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>.
    *   **`db` service (e.g., MySQL database)**:
        *   `image: mysql:latest`: Specifies the image to use for the database container <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.
*   **`volumes` object**: Defines volumes to store persistent data, like database data across multiple containers <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
    *   Volumes can then be mounted into containers (e.g., `db` container) <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>.

Defining configurations in YAML is much easier than writing individual commands <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

### Running Docker Compose

*   **`docker compose up`**: Finds the `docker-compose.yaml` file and runs all defined containers together <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **`docker compose down`**: Shuts down all containers defined in the Compose file together <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.