---
title: Creating and Using Dockerfiles
videoId: gAkwW2tuIqE
---

From: [[fireship]] <br/> 

[[Introduction to Docker | Docker]] is a tool that allows software to be packaged and run on any hardware <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. The core concepts to understand [[Introduction to Docker | Docker]] are Dockerfiles, images, and containers <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

A Dockerfile is a blueprint for building a [[Introduction to Docker | Docker image]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. A [[Introduction to Docker | Docker image]] is a template for running [[Managing Docker Containers with Commands | Docker containers]] <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. A [[Managing Docker Containers with Commands | container]] is a running process based on an image <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. The primary purpose of [[Introduction to Docker | Docker]] is to solve "it works on my machine" problems by reproducing environments reliably <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Defining the Environment with a Dockerfile

A developer can define the application's environment using a Dockerfile <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This Dockerfile allows any other developer to rebuild that environment, saving it as an immutable snapshot known as an image <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

A Dockerfile contains instructions to build your [[Introduction to Docker | Docker image]] and run your application as a [[Managing Docker Containers with Commands | container]] <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. Every instruction in a Dockerfile is considered its own step or layer, which [[Introduction to Docker | Docker]] attempts to cache for efficiency if nothing has changed <a class="yt-timestamp" data-t="00:04:03">[00:04:03]</a>.

Key instructions include:

### `FROM`
This instruction specifies the base image for your Dockerfile <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. While you can start from scratch, most Dockerfiles begin with a specific base image <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. For example, `node:12` provides everything needed to work with Node.js in the environment <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

### `WORKDIR`
The `WORKDIR` instruction sets the working directory for any subsequent instructions in the Dockerfile, similar to using the `cd` command <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

### `COPY`
The `COPY` instruction is used to add source code or other files to the image <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. It takes two arguments: the local file or directory path, and the destination path within the container <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### `.dockerignore`
Similar to a `.gitignore` file, a `.dockerignore` file can be created to tell [[Introduction to Docker | Docker]] to ignore certain local files or directories (like `node_modules`) when copying them into the image, preventing them from overriding existing files in the image <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### `RUN`
This instruction executes commands inside the image during the build process, such as `npm install` to install dependencies <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>. The results are committed to the [[Introduction to Docker | Docker image]] as a layer <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### `ENV`
The `ENV` instruction sets environment variables within the container <a class="yt-timestamp" data-t="00:05:24">[00:05:24]</a>.

### `EXPOSE`
This instruction declares that the container will listen on a specified network port at runtime <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### `CMD`
The `CMD` instruction defines the default command to execute when a [[Managing Docker Containers with Commands | container]] is launched from the image <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. There can only be one `CMD` instruction per Dockerfile <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>. It tells the [[Managing Docker Containers with Commands | container]] how to run the actual application, often in "exec form" as an array of strings, which doesn't start a shell session <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

## Building a Docker Image

To build a [[Introduction to Docker | Docker image]] from a Dockerfile, use the `docker build` command <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
The `-t` or `--tag` option allows you to give your image a memorable name tag <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. It's recommended to tag images with your Docker Hub username (e.g., `username/imagename:version`) <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>. The command typically ends with a period (`.`) to indicate the current working directory as the path to the Dockerfile <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

```bash
docker build -t fireship/demo-app:1.0 . <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>
```

During the build process, [[Introduction to Docker | Docker]] pulls the base image (if not already local) and then goes through each step in the Dockerfile <a class="yt-timestamp" data-t="00:06:38">[00:06:38]</a>. Once successfully built, the image can be used as a base for other images or to run [[Managing Docker Containers with Commands | containers]] <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>.

## Running a Docker Container from an Image

After building an image, you can run a [[Managing Docker Containers with Commands | container]] from it using the `docker run` command, specifying the image ID or tag name <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

By default, an `EXPOSE`d port in a Dockerfile is not accessible to the outside world <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>. To make it accessible, you must use the `-p` flag for port forwarding when running the [[Managing Docker Containers with Commands | container]] <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This maps a port on your local machine to a port inside the [[Managing Docker Containers with Commands | Docker container]] <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

```bash
docker run -p 5000:8080 fireship/demo-app:1.0 <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>
```
This command maps local port `5000` to the container's exposed port `8080` <a class="yt-timestamp" data-t="00:07:42">[00:07:42]</a>.

### Managing Running Containers
[[Managing Docker Containers with Commands | Docker containers]] will continue running even after closing the terminal <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>. You can use the [[Introduction to Docker | Docker desktop application]] or `docker ps` to see running containers and `docker stop` to stop them <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>, <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. Stopping a [[Managing Docker Containers with Commands | container]] results in any state or data created inside it being lost <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Debugging Containers

To inspect logs of a running [[Managing Docker Containers with Commands | container]], you can use the [[Introduction to Docker | Docker desktop application]] <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. To interact with the command line inside a [[Managing Docker Containers with Commands | container]], click the CLI button in the desktop app or use the `docker exec` command <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>, <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. This allows you to `ls` files or perform other [[basic_bash_commands_and_scripts | Linux]] commands within the container's file system <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

## [[Working with Volumes and Docker Compose | Volumes and Docker Compose]]

### Volumes
[[Working with Volumes and Docker Compose | Volumes]] are dedicated folders on the host machine where a [[Managing Docker Containers with Commands | container]] can create files that can be remounted into future [[Managing Docker Containers with Commands | containers]] or shared among multiple [[Managing Docker Containers with Commands | containers]] simultaneously <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>. Files in a [[Working with Volumes and Docker Compose | volume]] persist even after [[Managing Docker Containers with Commands | containers]] are shut down <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. Volumes are created using the `docker volume create` command <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.

### [[Working with Volumes and Docker Compose | Docker Compose]]
For applications requiring multiple processes, it's best practice to use multiple [[Managing Docker Containers with Commands | containers]] <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>. [[Working with Volumes and Docker Compose | Docker Compose]] is a tool designed to run multiple [[Managing Docker Containers with Commands | Docker containers]] simultaneously <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>. It uses a `docker-compose.yaml` file to define services (containers), their build contexts (pointing to Dockerfiles), port forwarding, and [[Working with Volumes and Docker Compose | volume]] configurations <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. This YAML file simplifies the management of complex multi-container applications compared to individual `docker` commands <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>.

To run the services defined in `docker-compose.yaml`, use `docker compose up` <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. To shut down all containers defined in the file, use `docker compose down` <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.