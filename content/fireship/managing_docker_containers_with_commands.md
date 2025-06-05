---
title: Managing Docker Containers with Commands
videoId: gAkwW2tuIqE
---

From: [[fireship]] <br/> 

[[introduction_to_docker | Docker]] is a tool that allows developers to package software so it can run reliably on any hardware environment <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>. Understanding [[introduction_to_docker | Docker]] is considered essential for developers in 2020 <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

From a practical standpoint, [[introduction_to_docker | Docker]] aims to solve the problem of environment reproducibility ("it works on my machine") by enabling developers to define the environment with a [[creating_and_using_dockerfiles | Dockerfile]] <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Core Concepts

To understand how [[introduction_to_docker | Docker]] works, three key concepts are crucial <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>:

*   **[[creating_and_using_dockerfiles | Dockerfile]]**: A blueprint for building a [[introduction_to_docker | Docker]] image <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. It defines the environment and steps to create the software's snapshot <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **[[introduction_to_docker | Docker Image]]**: An immutable template for running [[introduction_to_docker | Docker Containers]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. It's a saved snapshot of the environment <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **[[introduction_to_docker | Docker Container]]**: A running process of a [[introduction_to_docker | Docker Image]] <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Multiple containers can be spawned from one image to run the same process in multiple places <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Tools like Kubernetes and Swarm can then scale these containers for large workloads <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Installation and Setup

For Mac or Windows, installing the [[introduction_to_docker | Docker]] Desktop application is recommended as it provides command-line tools and a graphical user interface (GUI) to inspect running containers <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

Additionally, installing the [[introduction_to_docker | Docker]] extension for VS Code or your preferred IDE can provide language support for [[creating_and_using_dockerfiles | Dockerfiles]] and links to remote registries <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## Basic Container Management

After installation, [[introduction_to_docker | Docker]] commands are accessible from the command line <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

### Listing Running Containers

To view all running containers on your system, use:
`docker ps` <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>

Each container has a unique ID and is linked to an image <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>. This information is also available in the [[introduction_to_docker | Docker]] Desktop GUI <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

### Running a Container

To create a running process (a container) from an image, use the `docker run` command:
`docker run [IMAGE_ID_OR_TAG]` <a class="yt-timestamp" data-t="00:07:12">[00:07:12]</a>

### Stopping Containers

While not explicitly a command, containers can be stopped using the [[introduction_to_docker | Docker]] Desktop dashboard <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>. When a container is stopped, any state or data created inside it will be lost <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Building and Distributing Images

### Building a Docker Image

A [[creating_and_using_dockerfiles | Dockerfile]] contains instructions to build a [[introduction_to_docker | Docker Image]] <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Common [[creating_and_using_dockerfiles | Dockerfile]] instructions include:
*   `FROM`: Specifies the base image (e.g., `node:12`) <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.
*   `WORKDIR`: Sets the working directory inside the image <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   `COPY`: Copies files from the local machine to the image <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.
*   `RUN`: Executes commands within the image (e.g., `npm install`) <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.
*   `ENV`: Sets environment variables <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.
*   `EXPOSE`: Declares a port the application listens on (e.g., `EXPOSE 8080`) <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   `CMD`: Defines the command to execute when the container starts, typically in "exec form" (an array of strings) <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

To build an image from a [[creating_and_using_dockerfiles | Dockerfile]], use the `docker build` command. The `-t` (tag) option is useful for naming the image:
`docker build -t [YOUR_USERNAME]/[IMAGE_NAME]:[VERSION] .` <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>

### Distributing Images

After building, images can be pushed to a container registry (like [[introduction_to_docker | Docker]] Hub or a cloud provider's registry):
`docker push [IMAGE_NAME]` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>

Other developers or servers can then pull the image down:
`docker pull [IMAGE_NAME]` <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>

## Advanced Container Management

### Port Forwarding

By default, ports exposed in a [[creating_and_using_dockerfiles | Dockerfile]] are not accessible to the outside world <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. To make a container's port accessible on the local machine, use the `-p` flag with `docker run` to implement port forwarding:
`docker run -p [LOCAL_PORT]:[CONTAINER_PORT] [IMAGE_NAME]` <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>

### [[working_with_volumes_and_docker_compose | Volumes]]

[[working_with_volumes_and_docker_compose | Volumes]] are dedicated folders on the host machine that allow containers to store and share data persistently, even after containers are shut down <a class="yt-timestamp" data-t="00:08:16">[00:08:16]</a>. Multiple containers can simultaneously mount and access the same [[working_with_volumes_and_docker_compose | volume]] <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.

To create a [[working_with_volumes_and_docker_compose | volume]]:
`docker volume create [VOLUME_NAME]` <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>

### [[debugging_and_inspecting_docker_containers | Debugging and Inspecting]]

When issues arise, [[introduction_to_docker | Docker]] offers tools for [[debugging_and_inspecting_docker_containers | inspecting]] containers:

*   **Logs**: [[introduction_to_docker | Docker]] Desktop allows viewing and searching container logs directly <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
*   **Executing Commands**: You can execute commands within a running container, effectively getting a shell session inside it <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. This can be done via the [[introduction_to_docker | Docker]] Desktop GUI's CLI button or using the command line:
    `docker exec -it [CONTAINER_ID] bash` (or `sh`) <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>

## Multi-Container Management with Docker Compose

For applications requiring multiple processes (e.g., a web app and a database), it's a best practice to run each process in its own container <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. [[working_with_volumes_and_docker_compose | Docker Compose]] is a tool designed to manage and run multiple [[introduction_to_docker | Docker Containers]] simultaneously <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

[[working_with_volumes_and_docker_compose | Docker Compose]] configurations are defined in a `docker-compose.yaml` file, typically located in the root of the project <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>. This file uses YAML syntax to define "services," where each service represents a different container <a class="yt-timestamp" data-t="00:09:54">[00:09:54]</a>. It can also define [[working_with_volumes_and_docker_compose | volumes]] for data persistence across containers <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

To run all containers defined in a `docker-compose.yaml` file:
`docker compose up` <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>

To shut down all containers together:
`docker compose down` <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>