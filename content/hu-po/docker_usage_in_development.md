---
title: Docker usage in development
videoId: Ir1QMPMqPKg
---

From: [[hu-po]] <br/> 
## Docker Usage in Development

Docker can be a "much cleaner" solution for managing development environments, especially when dealing with complex dependencies like those found in machine learning projects <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>.

### Addressing Dependency Issues with Docker

When attempting to install Nerf Studio, numerous compatibility issues arose with different versions of Python, PyTorch, Cuda, and specific libraries like `torch.six` and Tiny Cuda NN (tcnn) <a class="yt-timestamp" data-t="00:42:21">[00:42:21]</a>. These problems included:
*   Incompatibilities with `protobuf` and `grpc` required by `tensorflow-datasets` <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>.
*   `torch.six` module not found errors due to PyTorch 2.0 no longer supporting it, necessitating a downgrade of the PyTorch version <a class="yt-timestamp" data-t="00:14:37">[00:14:37]</a>.
*   `tcnn is not defined` errors, indicating problems with the Tiny Cuda NN library installation <a class="yt-timestamp" data-t="00:17:38">[00:17:38]</a>.
*   Undefined symbol errors related to Cuda caching allocators and other Cuda incompatibilities <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>.
*   Issues detecting default Cuda architecture and requiring specific `tcnn_Cuda_architectures` environment variables <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.

Docker was considered as a solution to "not have to worry about this crap" by encapsulating all dependencies within a containerized environment <a class="yt-timestamp" data-t="00:44:26">[00:44:26]</a>.

### Key Docker Commands and Concepts

Docker commands allow developers to manage containers and their environments, often used to avoid dependency conflicts <a class="yt-timestamp" data-t="00:46:17">[00:46:17]</a>.

*   **`docker pull [image_name]:[tag]`**: This command is used to download a Docker image from a registry <a class="yt-timestamp" data-t="00:45:42">[00:45:42]</a>. For Nerf Studio, the `dromny/nerfstudio:0.1.9` image was used <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>.
*   **`docker run`**: Executes a command in a new container <a class="yt-timestamp" data-t="00:47:32">[00:47:32]</a>.
    *   **`--gpus all`**: Makes all available [[hardware_for_ai_training_and_deployment | GPUs]] accessible to the Docker container <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>.
    *   **`-v [host_path]:[container_path]`**: Mounts a volume, connecting a specific folder on the host machine to a corresponding folder inside the Docker container <a class="yt-timestamp" data-t="00:47:46">[00:47:46]</a>. This is useful for accessing data files (`--v /path/to/data:/data`) and cache folders (`--v /path/to/cache:/cache`) to avoid re-downloading models <a class="yt-timestamp" data-t="00:48:01">[00:48:01]</a>.
    *   **`-p [host_port]:[container_port]`**: Publishes a container's port to the host. For Nerf Studio, port 7007 is used for the web viewer <a class="yt-timestamp" data-t="00:48:13">[00:48:13]</a>.
    *   **`--rm`**: Automatically removes the container once it exits <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a>.
    *   **`-it`**: Runs the container in interactive mode and attaches a terminal to it, allowing direct interaction inside the container <a class="yt-timestamp" data-t="00:48:31">[00:48:31]</a>.
    *   **`--memory [amount]`**: Sets the maximum amount of memory the container can use <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>. It's important to be careful with this to avoid freezing the host machine <a class="yt-timestamp" data-t="00:48:46">[00:48:46]</a>.

### Building Custom Docker Images

Instead of pulling a pre-built image, a custom Docker image can be built from a Dockerfile. This allows for specific configurations, such as targeting a particular Cuda architecture <a class="yt-timestamp" data-t="00:56:44">[00:56:44]</a>.

*   **`docker build --build-arg CUDA_ARCHITECTURES=[value] .`**: This command builds a Docker image from a Dockerfile in the current directory (`.`) and passes a build argument (e.g., `CUDA_ARCHITECTURES=61` for a GeForce 1080 TI GPU) <a class="yt-timestamp" data-t="00:56:53">[00:56:53]</a>.

### Persistent Challenges

Despite using Docker, some compatibility issues related to Cuda persist, particularly when the host machine's Cuda version differs from the Cuda version embedded in the Docker image <a class="yt-timestamp" data-t="02:08:02">[02:08:02]</a>. For example, an 11.6 Cuda host can be incompatible with an 11.8 Cuda Docker image <a class="yt-timestamp" data-t="02:08:07">[02:08:07]</a>. This requires either:
1.  Upgrading the host machine's NVIDIA drivers and Cuda version to match the Docker image <a class="yt-timestamp" data-t="02:08:17">[02:08:17]</a>.
2.  Changing the Cuda version within the Docker image's build process to match the host's <a class="yt-timestamp" data-t="02:08:27">[02:08:27]</a>.

[!WARNING]
Attempting to upgrade or reinstall Cuda drivers on the host machine carries a non-zero chance of "nuk[ing] my computer" <a class="yt-timestamp" data-t="02:13:41">[02:13:41]</a>. Proper post-installation actions, such as setting paths, are required after Cuda installation <a class="yt-timestamp" data-t="02:21:00">[02:21:00]</a>.