---
title: Introduction to Docker and its importance for developers
videoId: gAkwW2tuIqE
---

From: [[fireship]] <br/> 

Not knowing Docker can lead to "imposter syndrome" among developers, especially when discussions turn to topics like Kubernetes or Swarm [00:00:00]. Docker is a fundamental tool for developers in 2020 [00:00:14].

## What is Docker?

From a practical standpoint, Docker is a method to package software so it can run consistently on any hardware [00:00:40]. It solves the common problem of "it works on my machine" by allowing developers to define and reproduce specific software environments [00:01:09].

## Core Concepts: [[understanding_docker_files_images_and_containers | Docker Files, Images, and Containers]]

To understand how Docker works, three core concepts are essential:
*   **[[understanding_docker_files_images_and_containers | Dockerfile]]** A [[understanding_docker_files_images_and_containers | Dockerfile]] is a blueprint for building a Docker image [00:00:53]. It defines the environment and instructions for an application [00:01:20].
*   **[[understanding_docker_files_images_and_containers | Docker Image]]** A [[understanding_docker_files_images_and_containers | Docker image]] is a template for running Docker containers [00:00:56]. It's an immutable snapshot of a defined environment [00:01:27]. [[understanding_docker_files_images_and_containers | Images]] can be uploaded to public or private cloud registries [00:01:29].
*   **[[understanding_docker_files_images_and_containers | Container]]** A [[understanding_docker_files_images_and_containers | container]] is a running process of a Docker image [00:01:00], [00:01:38]. One image file can be used to spawn the same process multiple times in multiple locations [00:01:42]. This capability allows tools like Kubernetes and Swarm to scale containers for large workloads [00:01:47].

## [[stepbystep_instructions_for_docker_installation_and_setup | Docker Installation and Setup]]

The best way to learn Docker is by using it [00:01:53].
*   **Docker Desktop**: For Mac or Windows, installing Docker Desktop is highly recommended as it provides command-line tools and a graphical user interface (GUI) for inspecting containers [00:01:57].
*   **Command Line**: After installation, Docker is accessible via the command line [00:02:06]. A basic command to know is `docker ps`, which lists all running containers [00:02:11]. Each container has a unique ID and is linked to an image [00:02:14].
*   **VS Code Extension**: Installing the Docker extension for VS Code or other IDEs provides language support for [[understanding_docker_files_images_and_containers | Dockerfiles]], and can link to remote registries [00:02:22].

## [[handson_guide_to_containerizing_a_nodejs_application | Containerizing a Node.js Application]] with a Dockerfile

A [[understanding_docker_files_images_and_containers | Dockerfile]] contains the code to build a Docker image and ultimately run an application as a container [00:02:39].

### Key Dockerfile Instructions

Each instruction in a [[understanding_docker_files_images_and_containers | Dockerfile]] is considered its own step or layer, which Docker attempts to cache for efficiency if nothing has changed [00:04:03].

*   `FROM`: Specifies the base image for the build [00:03:08]. While starting from scratch is possible, most [[understanding_docker_files_images_and_containers | Dockerfiles]] begin with a base image [00:03:14]. For a Node.js application, the official Node.js image (e.g., `node:12`) provides everything needed [00:03:39].
*   `WORKDIR`: Sets the working directory for subsequent instructions [00:03:51]. It's similar to changing directories with `cd` [00:03:53].
*   `COPY`: Copies files from the local machine to the specified location in the container [00:04:27]. It takes two arguments: the source path and the destination path within the container [00:04:29].
*   `RUN`: Executes commands inside the container, similar to running commands in a terminal [00:04:41]. The results are committed to the Docker image as a layer [00:04:45]. For Node.js, `npm install` would be run to install dependencies [00:04:40].
*   `.dockerignore`: Similar to a `.gitignore` file, it specifies files or directories that Docker should ignore when copying source code, preventing local `node_modules` from overwriting installed dependencies in the image [00:05:08].
*   `ENV`: Sets environment variables within the container [00:05:24].
*   `EXPOSE`: Informs Docker that the container will be listening on a specific port (e.g., 8080 for a Node.js Express app) [00:05:30].
*   `CMD`: The final instruction, there can only be one per [[understanding_docker_files_images_and_containers | Dockerfile]], and it tells the container how to run the actual application [00:05:40]. It's preferred to use "exec form" (an array of strings) over a regular command [00:05:51].

## Building a Docker Image

A Docker image is built using the `docker build` command [00:06:07].
*   The `-t` or `--tag` flag allows you to give the image a memorable name (tag) [00:06:14], often formatted as `username/image-name` with an optional version number [00:06:21].
*   The command also requires the path to the [[understanding_docker_files_images_and_containers | Dockerfile]] (e.g., `.` for the current directory) [00:06:33].
*   During the build process, Docker pulls base images and executes each step in the [[understanding_docker_files_images_and_containers | Dockerfile]] [00:06:38].

## Running Containers

Once an image is built, it can be used to run containers in real life [00:06:54].
*   **Pushing/Pulling Images**: Images can be pushed to container registries (like Docker Hub or cloud providers) using `docker push` [00:06:56], and pulled down by other developers or servers using `docker pull` [00:07:03].
*   **`docker run`**: To run an image locally, use `docker run` with the image ID or tag name [00:07:10]. This command creates a running process, which is the container [00:07:17].
*   **[[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | Port Forwarding]]**: Even if a port is exposed in the [[understanding_docker_files_images_and_containers | Dockerfile]], it's not accessible to the outside world by default [00:07:29]. The `-p` flag (e.g., `-p 5000:8080`) is used to implement [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | port forwarding]], mapping a port on the local machine (e.g., 5000) to a port inside the Docker container (e.g., 8080) [00:07:36].
*   **Stopping Containers**: Containers continue running even after the terminal window is closed [00:07:54]. Stopping a container (e.g., via Docker Desktop) will result in the loss of any state or data created inside it [00:08:06].

## Data Persistence with Volumes

For scenarios where data needs to be shared across multiple containers or persisted beyond the life of a single container, **volumes** are used [00:08:11].
*   A volume is a dedicated folder on the host machine [00:08:18].
*   Containers can create files within this folder, and these files can be remounted into future containers or accessed by multiple containers simultaneously [00:08:21].
*   Volumes can be created using `docker volume create` [00:08:27].

## Debugging Containers

Docker Desktop provides useful tools for debugging:
*   **Logs**: Clicking on a running container in Docker Desktop shows its logs, which can be searched [00:08:55].
*   **CLI Access**: The CLI button in Docker Desktop allows executing commands directly within the container [00:09:01]. This can also be done from the command line using `docker exec` [00:09:05].

## [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | Managing Multiple Containers]] with Docker Compose

For applications composed of multiple processes (microservices), [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | Docker Compose]] is the tool of choice [00:09:21], [00:09:30]. It allows running multiple Docker containers together [00:09:34].

*   **`docker-compose.yaml`**: This YAML file defines the services (containers) that an application needs [00:09:51]. Each key in the `services` object represents a different container [00:09:54].
    *   It can specify the build context (where the [[understanding_docker_files_images_and_containers | Dockerfile]] is located) [00:10:04].
    *   It defines [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | port forwarding]] configurations [00:10:10].
    *   It can define volumes and mount them into containers, ensuring data persistence for services like databases [00:10:19].
*   **`docker compose up`**: This command reads the `docker-compose.yaml` file and starts all defined containers together [00:10:33].
*   **`docker compose down`**: This command shuts down all containers defined in the `docker-compose.yaml` file [00:10:42].