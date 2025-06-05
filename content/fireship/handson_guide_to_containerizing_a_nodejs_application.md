---
title: Handson guide to containerizing a Nodejs application
videoId: gAkwW2tuIqE
---

From: [[fireship]] <br/> 

Docker is a powerful tool for packaging software to run on any hardware, helping developers reproduce environments and solve common deployment issues like "it works on my machine" <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a> <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. Learning Docker is crucial for developers in 2020 to avoid imposter syndrome at tech gatherings <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a> <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

This guide provides a hands-on approach to containerizing a [[nodejs_runtime_and_basic_operations | Node.js]] application, covering installation, tooling, Dockerfile instructions, and [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | advanced concepts]] like port forwarding and managing multiple containers with Docker Compose <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a> <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a> <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## Core Docker Concepts

To understand Docker, three fundamental concepts must be known: Dockerfiles, Images, and Containers <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a> <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

*   **Dockerfile**: This is a blueprint for building a Docker image <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a> <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>. It defines the environment and steps required to package software <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Docker Image**: A template for running Docker containers, saved as an immutable snapshot <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a> <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. Images can be uploaded to public or private cloud registries <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
*   **Container**: A running process of a Docker image <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a> <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. One image can spawn multiple processes in various locations <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. Tools like Kubernetes and Swarm are used to scale containers <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## Installing Docker

For Mac or Windows, it's highly recommended to install the Docker Desktop application <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. It provides command-line tools and a GUI for inspecting running containers <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

After installation, you should have access to `docker` from the command line <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>. The first command to memorize is `docker ps`, which lists all running containers, showing their unique ID and linked image <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. This information is also available in the GUI <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

Additionally, installing the Docker extension for VS Code (or your IDE) provides language support for Dockerfiles and links to remote registries <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>.

## The Dockerfile

The Dockerfile contains the instructions to build your Docker image and run your application as a container <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>. For a [[setting_up_a_nodejs_and_express_environment | Node.js Express]] application, here are the key instructions:

### 1. `FROM`

This instruction specifies the base image for your Docker build <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. While you can start from scratch, most Dockerfiles begin with a specific base image <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. For a [[nodejs_runtime_and_basic_operations | Node.js]] application, the officially supported [[installing_and_setting_up_nodejs | Node.js]] image is ideal, e.g., `node:12`, which provides everything needed for working with [[nodejs_runtime_and_basic_operations | Node.js]] <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a> <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

```dockerfile
FROM node:12
```

### 2. `WORKDIR`

Sets the working directory inside the container for any subsequent instructions <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

```dockerfile
WORKDIR /app
```

### 3. `COPY` and `RUN` (for Dependencies)

Each instruction in a Dockerfile is considered its own layer, and Docker attempts to cache layers for efficiency <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a> <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. To leverage caching, install dependencies *before* copying your application source code. This way, [[understanding_nodejs_modules_and_packages | Node.js modules]] are not reinstalled every time your source code changes <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a> <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>.

First, copy `package.json` and `package-lock.json` (or `yarn.lock`) to the working directory:

```dockerfile
COPY package*.json ./
```

Then, run `npm install` (or `yarn install`) to install dependencies. This command behaves like opening a terminal session, and its results are committed as a Docker image layer <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a> <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.

```dockerfile
RUN npm install
```

After dependencies are installed, copy over your application source code:

```dockerfile
COPY . .
```

### 4. `.dockerignore`

Similar to a `.gitignore` file, a `.dockerignore` file specifies files and directories that Docker should ignore when copying context into the image <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. This is crucial for [[nodejs_runtime_and_basic_operations | Node.js]] apps to prevent your local `node_modules` folder from overriding the installed modules in the image <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

Example `.dockerignore`:

```
node_modules
.git
.gitignore
```

### 5. `ENV`

Sets environment variables inside the container <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>. For an [[setting_up_a_nodejs_and_express_environment | Express.js]] app, you might set the port:

```dockerfile
ENV PORT 8080
```

### 6. `EXPOSE`

Informs Docker that the container will listen on the specified network ports at runtime <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>. This doesn't make the port accessible externally by default but serves as documentation and can be used by other tools.

```dockerfile
EXPOSE 8080
```

### 7. `CMD`

This is the final instruction and can only appear once per Dockerfile <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. It tells the container how to run the actual application by starting a process <a class="yt-timestamp" data-t="00:05:44">[00:05:44]</a>. It's preferred to use "exec form" (an array of strings) as it doesn't start a shell session, which is more efficient <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

```dockerfile
CMD ["node", "index.js"]
```

### Complete Dockerfile Example

```dockerfile
FROM node:12
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ENV PORT 8080
EXPOSE 8080
CMD ["node", "index.js"]
```

## Building a Docker Image

To build a Docker image from your Dockerfile, use the `docker build` command <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
The `-t` or `--tag` flag allows you to give your image an easy-to-remember name and tag <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. It's recommended to use your Docker Hub username followed by the image name and an optional version number (e.g., `fireship/demo-app:1.0.0`) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

The command also requires the path to your Dockerfile context, which is typically `.` for the current working directory <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

```bash
docker build -t your-username/demo-app:1.0.0 .
```

When you run this command, Docker will go through each step in your Dockerfile, pulling base images and building layers <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. Upon success, it will report the `image id` <a class="yt-timestamp" data-t="00:06:46">[00:06:46]</a>.

Once built, images can be pushed to a container registry (like Docker Hub or a cloud provider's registry) using `docker push` <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Other developers or servers can then pull the image down with `docker pull` <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>.

## Running a Docker Container

To run a container from your newly built image locally, use the `docker run` command, providing either the image ID or the tag name <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

```bash
docker run your-username/demo-app:1.0.0
```

By default, the container's exposed ports are not accessible to the outside world <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>. To access your application, you need to implement [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | port forwarding]] using the `-p` flag <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>.

The `-p` flag takes two arguments: `HOST_PORT:CONTAINER_PORT`. This maps a port on your local machine to a port inside the Docker container <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

```bash
docker run -p 5000:8080 your-username/demo-app:1.0.0
```

Now, your application running inside the container on port 8080 will be accessible on your local machine at `localhost:5000` <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

> [!INFO] Container Persistence
> A Docker container will continue running even after you close the terminal window where you launched it <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. You can stop containers via the Docker Desktop dashboard or with `docker stop <container_id>`. When a container is stopped, any state or data created inside it is lost <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Data Persistence with Volumes

For situations where you need to share or persist data across multiple containers, or ensure data isn't lost when a container stops, **volumes** are the preferred method <a class="yt-timestamp" data-t="00:08:11">[00:08:11]</a> <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. A volume is a dedicated folder on the host machine where a container can create files that can be remounted into future containers or shared among multiple containers simultaneously <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>.

To create a volume:

```bash
docker volume create my-app-data
```

Then, when running a container, you can mount this volume using the `-v` flag:

```bash
docker run -p 5000:8080 -v my-app-data:/app/data your-username/demo-app:1.0.0
```

Files within the `/app/data` directory inside the container will now persist to the `my-app-data` volume on the host machine <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

## Debugging Containers

When things don't go as planned, you'll need to inspect logs and interact with the container's command line <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>.

*   **Logs**: Docker Desktop allows you to easily view and search logs for any running container by clicking on it <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. From the command line, you can use `docker logs <container_id_or_name>`.
*   **CLI Access**: In Docker Desktop, click the "CLI" button for a running container to open a terminal session inside it <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. From the command line, use `docker exec -it <container_id_or_name> bash` (or `sh`) to get a shell session inside the container <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

## Managing Multiple Containers with Docker Compose

A best practice for healthy containers is to run simple, maintainable microservices, with each container running only one process <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a> <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>. If your application requires multiple processes (e.g., a [[nodejs_runtime_and_basic_operations | Node.js]] app and a database), you should use multiple containers <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>.

Docker Compose is a tool designed to run multiple Docker containers together <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. It uses a `docker-compose.yaml` file to define and manage services, networks, and volumes <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>.

### Example `docker-compose.yaml`

Consider a [[nodejs_runtime_and_basic_operations | Node.js]] app that needs to access a MySQL database, with a volume to persist database data <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>.

```yaml
version: '3.8'
services:
  web: # Our Node.js application
    build: . # Points to the current directory where the Dockerfile is located
    ports:
      - "5000:8080" # Port forwarding for the Node.js app
  db: # Our MySQL database container
    image: mysql:8.0 # Using an official MySQL image
    environment:
      MYSQL_ROOT_PASSWORD: mysecretpassword
      MYSQL_DATABASE: mydatabase
    volumes:
      - db-data:/var/lib/mysql # Mounts the named volume to persist database data
volumes:
  db-data: # Defines the named volume for the database
```

This YAML file makes it significantly easier to define complex multi-container configurations compared to individual Docker commands <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

To run all defined containers:

```bash
docker compose up
```

To shut down all containers together:

```bash
docker compose down
```

This [[advanced_docker_concepts_like_port_forwarding_and_managing_multiple_containers | approach to managing multiple containers]] with Docker Compose is highly effective for [[building_and_deploying_a_nodejs_full_stack_application | full-stack applications]] and development environments.