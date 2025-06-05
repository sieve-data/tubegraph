---
title: Understanding Docker files images and containers
videoId: gAkwW2tuIqE
---

From: [[fireship]] <br/> 

[[introduction_to_docker_and_its_importance_for_developers | Docker]] is a fundamental technology for developers in 2020, addressing challenges like "it works on my machine" syndrome [00:01:14]. Not understanding [[introduction_to_docker_and_its_importance_for_developers | Docker]] can lead to imposter syndrome among developers [00:00:00].

From a practical standpoint, [[introduction_to_docker_and_its_importance_for_developers | Docker]] is a method to package software, enabling it to run consistently on any hardware [00:00:40]. It ensures that the software environment is reproducible [00:01:16].

## Core Concepts: Dockerfiles, Images, and Containers

To grasp how [[introduction_to_docker_and_its_importance_for_developers | Docker]] works, three essential concepts are: Dockerfiles, Images, and Containers [00:00:47].

### Dockerfile
A Dockerfile serves as a blueprint for building a [[introduction_to_docker_and_its_importance_for_developers | Docker]] image [00:00:53]. It defines the environment and steps required to set up an application [00:01:19].

### Docker Image
A [[introduction_to_docker_and_its_importance_for_developers | Docker]] image is a template used for running [[introduction_to_docker_and_its_importance_for_developers | Docker]] containers [00:00:56]. It is an immutable snapshot of the environment and application code [00:01:27]. Images can be uploaded to public or private cloud registries for sharing [00:01:29].

### Docker Container
A container is a running process of a [[introduction_to_docker_and_its_importance_for_developers | Docker]] image [00:01:00]. One image can be used to spawn identical processes multiple times in various locations [00:01:42]. Tools like Kubernetes and Swarm can then be used to scale these containers to handle infinite workloads [00:01:47].

## Hands-On: Containerizing a Node.js Application

This section provides a [[handson_guide_to_containerizing_a_nodejs_application | hands-on guide to containerizing a Node.js application]] using [[introduction_to_docker_and_its_importance_for_developers | Docker]] [00:00:17].

### [[stepbystep_instructions_for_docker_installation_and_setup | Docker Installation and Setup]]
To use [[introduction_to_docker_and_its_importance_for_developers | Docker]], it must first be installed [00:01:54].
*   **Docker Desktop**: Recommended for Mac or Windows, as it installs necessary command-line tools and provides a GUI for inspecting running containers [00:01:57].
*   **Command Line**: After installation, [[Shell Commands and Bash Scripting | `docker ps`]] is a key command to memorize, listing all running containers, their unique IDs, and linked images [00:02:06].
*   **VS Code Extension**: The [[introduction_to_docker_and_its_importance_for_developers | Docker]] extension for VS Code or other IDEs provides language support for Dockerfiles and links to remote registries [00:02:22].

### The Dockerfile
The Dockerfile contains the instructions to build a [[introduction_to_docker_and_its_importance_for_developers | Docker]] image and run the application as a container [00:02:39]. Every instruction in a Dockerfile is considered a separate layer, and [[introduction_to_docker_and_its_importance_for_developers | Docker]] attempts to cache these layers for efficiency if nothing has changed [00:04:03].

Here are key instructions within a Dockerfile:

*   **`FROM`**: Specifies the base image for your Dockerfile [00:03:09]. While you can start from scratch, most Dockerfiles begin with a specific base image like Ubuntu or an officially supported Node.js image [00:03:14]. For a Node.js application, using the `node:12` base image provides the necessary Node.js environment [00:03:39].
*   **`WORKDIR`**: Sets the working directory for any subsequent instructions, similar to [[Shell Commands and Bash Scripting | `cd`]] [00:03:51].
*   **`COPY`**: Copies files from the local machine into the [[introduction_to_docker_and_its_importance_for_developers | Docker]] image [00:04:27]. It takes two arguments: the source path on the local machine and the destination path within the container [00:04:28].
*   **`RUN`**: Executes a command inside the image during the build process [00:04:40]. For Node.js, `npm install` is typically run after copying `package.json` to install dependencies [00:04:40]. Installing dependencies first allows them to be cached as a layer, preventing reinstallation every time the application source code changes [00:04:18].
*   **`.dockerignore`**: Similar to a `.gitignore` file, this file specifies files and directories to ignore when copying content to the [[introduction_to_docker_and_its_importance_for_developers | Docker]] image [00:05:08]. This prevents local `node_modules` from overwriting the dependencies installed within the image [00:04:57].
*   **`ENV`**: Sets environment variables within the container [00:05:27].
*   **`EXPOSE`**: Informs [[introduction_to_docker_and_its_importance_for_developers | Docker]] that the container will listen on a specific port at runtime, like port 8080 for a Node.js Express app [00:05:30].
*   **`CMD`**: The final instruction that tells the container how to run the actual application [00:05:40]. There can only be one `CMD` instruction per Dockerfile [00:05:41]. It's preferred to use "exec form" (an array of strings) which doesn't start a shell session [00:05:51].

## Building and Running Docker Components

### Building a Docker Image
An image is built using the [[Shell Commands and Bash Scripting | `docker build`]] command [00:06:07].
*   The [[Shell Commands and Bash Scripting | `-t`]] or [[Shell Commands and Bash Scripting | `--tag`]] flag is used to give the image a memorable name tag [00:06:14]. It's recommended to tag with a Docker Hub username (e.g., `fireship/demo-app`) and optionally a version number [00:06:21].
*   The command also requires the path to the Dockerfile, often specified as `.` for the current working directory [00:06:33].
*   When built, [[introduction_to_docker_and_its_importance_for_developers | Docker]] pulls the base image and goes through each step in the Dockerfile [00:06:38].

### Image Management
*   **`docker push`**: Used to upload an image to a container registry like Docker Hub or a cloud provider's registry [00:06:56].
*   **`docker pull`**: Used by other developers or servers to download an image from a registry [00:07:05].

### Running a Docker Container
A container is run using the [[Shell Commands and Bash Scripting | `docker run`]] command, specifying the image ID or tag name [00:07:12].
*   **Port Forwarding**: By default, an exposed port in a Dockerfile is not accessible to the outside world [00:07:31]. The [[Shell Commands and Bash Scripting | `-p`]] flag with [[Shell Commands and Bash Scripting | `docker run`]] implements port forwarding, mapping a port on the local machine to a port on the container (e.g., [[Shell Commands and Bash Scripting | `-p 5000:8080`]] maps local port 5000 to container port 8080) [00:07:36].
*   Containers continue running even after the terminal window is closed [00:07:54]. They can be stopped from the Docker Desktop dashboard or command line [00:08:01].

## Data Persistence: Volumes
When a container is stopped, any state or data created inside it is lost [00:08:06]. [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | Volumes]] are the preferred way to share and persist data across multiple containers [00:08:15].
*   A [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | volume]] is a dedicated folder on the host machine [00:08:18].
*   Containers can create files in this folder, and these files can be remounted into future containers or accessed simultaneously by multiple containers [00:08:22].
*   [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | Volumes]] are created using the [[Shell Commands and Bash Scripting | `docker volume create`]] command [00:08:27].

## Debugging and Inspection
*   **Docker Desktop**: Provides an easy way to inspect container logs and execute commands within a running container via a CLI button [00:08:53].
*   [[Shell Commands and Bash Scripting | `docker logs`]]: Views logs from the command line.
*   [[Shell Commands and Bash Scripting | `docker exec`]]: Allows executing commands inside a running container from the command line, enabling interaction with the [[File System and Permissions in Linux | file system]] and Linux environment [00:09:06].

## Managing Multiple Containers: Docker Compose
[[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | Docker Compose]] is a tool designed for running multiple [[introduction_to_docker_and_its_importance_for_developers | Docker]] containers simultaneously [00:09:30]. It encourages the practice of writing simple, maintainable microservices where each container runs only one process [00:09:21].

*   **`docker-compose.yaml`**: This YAML file defines the services (containers) that make up your application, including their build context, port forwarding configurations, and [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | volumes]] [00:09:49]. For example, it can define a Node.js web app and a MySQL database, along with a [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | volume]] to persist database data [00:09:37].
*   [[Shell Commands and Bash Scripting | `docker compose up`]]: Reads the `docker-compose.yaml` file and starts all defined containers together [00:10:34].
*   [[Shell Commands and Bash Scripting | `docker compose down`]]: Shuts down all containers defined in the `docker-compose.yaml` file [00:10:42].