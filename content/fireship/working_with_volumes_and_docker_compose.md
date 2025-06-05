---
title: Working with Volumes and Docker Compose
videoId: gAkwW2tuIqE
---

From: [[fireship]] <br/> 

When working with [[introduction_to_docker | Docker containers]], managing data persistence and coordinating multiple services can be complex. Volumes provide a solution for data persistence, while Docker Compose simplifies the orchestration of multi-container applications <a class="yt-timestamp" data-t="09:34:10">[09:34:10]</a>.

## Docker Volumes

A volume is a dedicated folder on the host machine that allows [[introduction_to_docker | Docker containers]] to create and store files persistently <a class="yt-timestamp" data-t="08:18:14">[08:18:14]</a>.

### Why Use Volumes?
When a [[introduction_to_docker | Docker container]] is stopped, any state or data created inside it will be lost <a class="yt-timestamp" data-t="08:06:11">[08:06:11]</a>. Volumes address this by:
*   **Persisting Data** <a class="yt-timestamp" data-t="08:40:07">[08:40:07]</a>: Files created within a volume will stick around even after all the containers are shut down <a class="yt-timestamp" data-t="08:40:07">[08:40:07]</a>.
*   **Sharing Data** <a class="yt-timestamp" data-t="08:11:43">[08:11:43]</a>: Data can be shared across multiple containers simultaneously <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. For example, a [[mysql_database | MySQL database]] container might need a volume to persist its data across multiple containers <a class="yt-timestamp" data-t="09:43:10">[09:43:10]</a>.

### Creating and Mounting Volumes
Volumes can be created using the `docker volume create` [[managing_docker_containers_with_commands | command]] <a class="yt-timestamp" data-t="08:27:14">[08:27:14]</a>. Once created, a volume can be mounted into a [[introduction_to_docker | Docker container]] when it's run <a class="yt-timestamp" data-t="08:32:14">[08:32:14]</a>.

## Docker Compose

Docker Compose is a tool designed to run multiple [[introduction_to_docker | Docker containers]] at the same time <a class="yt-timestamp" data-t="09:34:10">[09:34:10]</a>. It's ideal for applications that require multiple processes, such as a web application and a database <a class="yt-timestamp" data-t="09:26:00">[09:26:00]</a>.

### Defining Services with `docker-compose.yaml`

Docker Compose uses a `docker-compose.yaml` file located in the root of your project to define and configure services <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>.

The file contains a `services` object, where each key represents a different [[introduction_to_docker | Docker container]] you want to run <a class="yt-timestamp" data-t="09:54:10">[09:54:10]</a>.

#### Example Configuration
Consider a scenario where a [[building_and_deploying_a_full_stack_application_with_nodejs_and_express | Node.js application]] needs to access a [[mysql_database | MySQL database]] <a class="yt-timestamp" data-t="09:38:00">[09:38:00]</a>.

```yaml
version: '3.8'
services:
  web:
    build: . # Points to the current working directory where the [[creating_and_using_dockerfiles | Dockerfile]] is located
    ports:
      - "5000:8080" # [[debugging_and_inspecting_docker_containers | Port forwarding]] configuration
  db:
    image: mysql:latest # Uses a pre-built MySQL image
    volumes:
      - db_data:/var/lib/mysql # Mounts a volume for database persistence
    environment:
      MYSQL_ROOT_PASSWORD: mysecretpassword # Example environment variable
volumes:
  db_data: # Defines the volume to store database data
```
<a class="yt-timestamp" data-t="09:54:10">[09:54:10]</a>, <a class="yt-timestamp" data-t="10:04:00">[10:04:00]</a>, <a class="yt-timestamp" data-t="10:10:10">[10:10:10]</a>, <a class="yt-timestamp" data-t="10:13:10">[10:13:10]</a>, <a class="yt-timestamp" data-t="10:18:14">[10:18:14]</a>, <a class="yt-timestamp" data-t="10:23:07">[10:23:07]</a>

Using YAML for configuration makes it easier to define complex multi-container setups compared to writing individual [[managing_docker_containers_with_commands | commands]] <a class="yt-timestamp" data-t="10:27:14">[10:27:14]</a>.

### Running and Stopping Services

*   To run all containers defined in `docker-compose.yaml`, use the [[managing_docker_containers_with_commands | command]]: `docker compose up` <a class="yt-timestamp" data-t="10:34:07">[10:34:07]</a>.
*   To shut down all containers together, use: `docker compose down` <a class="yt-timestamp" data-t="10:42:07">[10:42:07]</a>.

These tools are crucial for deploying and managing applications in a containerized environment, especially for [[debugging_and_inspecting_docker_containers | debugging]] and maintaining healthy, isolated microservices <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.