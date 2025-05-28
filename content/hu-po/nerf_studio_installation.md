---
title: Nerf Studio installation
videoId: Ir1QMPMqPKg
---

From: [[hu-po]] <br/> 

Nerf Studio is a tool that provides a simplified API for the end-to-end process of creating [[applications_of_neural_network_diffusion_for_nerfs | Nerfs]] <a class="yt-timestamp" data-t="01:39:41">[01:39:41]</a>, functioning as a neural network that acts as a 3D file <a class="yt-timestamp" data-t="01:52:21">[01:52:21]</a>. It is permissively licensed <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This article details the process and common challenges encountered during the installation of Nerf Studio, primarily focusing on dependency and environment setup issues.

## Initial Setup Attempts

The installation process typically begins with setting up a conda environment <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>, requiring an Nvidia card with CUDA installed <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.

The recommended steps include:
1.  Creating a conda environment <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
2.  Activating the environment <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
3.  Upgrading pip <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
4.  Installing Nerf Studio via pip <a class="yt-timestamp" data=t="00:07:13">[00:07:13]</a>.

### Dependency Conflicts

A significant challenge during installation was resolving conflicts with core dependencies, particularly PyTorch and its interaction with `torch six` and `tiny-cuda-nn`.

*   **PyTorch Version Incompatibility**: An initial attempt to install Nerf Studio led to a `no module named torch six` error <a class="yt-timestamp" data-t="01:11:53">[01:11:53]</a>. This issue arose because PyTorch 2.0, which was installed by default, no longer supports `torch six` <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. The suggested resolution was to explicitly install an older version of PyTorch, specifically `torch==1.13.1` with `cuda-11.7` <a class="yt-timestamp" data-t="01:15:29">[01:15:29]</a>. However, even after downgrading, `tiny-cuda-nn` still presented an `undefined symbol` error related to `Cuda caching allocator` <a class="yt-timestamp" data-t="01:59:08">[01:59:08]</a>, indicating an incompatibility between PyTorch and the `tiny-cuda-nn` library <a class="yt-timestamp" data-t="01:59:45">[01:59:45]</a>.

### `tiny-cuda-nn` Compilation Issues

The `tiny-cuda-nn` dependency, a "lighting fast C++ CUDA neural network framework" <a class="yt-timestamp" data-t="01:19:20">[01:19:20]</a>, proved particularly problematic.

*   **Direct Installation Failures**: Direct `pip install` commands for `tiny-cuda-nn` did not resolve the issue <a class="yt-timestamp" data-t="01:18:59">[01:18:59]</a>.
*   **Building from Source**: Attempts were made to clone and build `tiny-cuda-nn` from its GitHub repository <a class="yt-timestamp" data-t="02:18:00">[02:18:00]</a>.
    *   **CUDA Architecture**: A common error was `failed to detect a default Cuda architecture` <a class="yt-timestamp" data-t="02:20:07">[02:20:07]</a> or `unknown compute capability` <a class="yt-timestamp" data-t="02:50:58">[02:50:58]</a>. This required explicitly setting the `CMAKE_CUDA_ARCHITECTURES` environment variable during the `cmake` command <a class="yt-timestamp" data-t="02:55:31">[02:55:31]</a>. For a GeForce 1080 TI GPU, the correct architecture was `61` <a class="yt-timestamp" data-t="02:55:01">[02:55:01]</a>.
    *   **Environment Variables**: Missing CUDA-related environment variables (`CUDA_HOME`, `CUDA_PATH`) also caused issues <a class="yt-timestamp" data-t="02:26:09">[02:26:09]</a>, which were resolved by exporting them to the session path <a class="yt-timestamp" data-t="02:39:03">[02:39:03]</a>.
    *   **GCC Version**: Conflicts arose with the GCC compiler version, with both GCC 11 and GCC 10 failing to compile `tiny-cuda-nn` <a class="yt-timestamp" data-t="03:39:37">[03:39:37]</a>.

## Docker Installation Attempt

Due to persistent environment issues, switching to a Docker-based installation was attempted <a class="yt-timestamp" data-t="04:40:06">[04:40:06]</a>, aiming to leverage containerization for dependency management <a class="yt-timestamp" data-t="04:46:17">[04:46:17]</a>.

*   **Pulling Docker Image**: The process involved pulling a pre-built Nerf Studio Docker image from Docker Hub, specifically `dromny/nerfstudio:0.1.9` <a class="yt-timestamp" data-t="04:55:55">[04:55:55]</a>.
*   **Running Docker Container**: The `docker run` command was configured to:
    *   Use all available GPUs (`--gpus all`) <a class="yt-timestamp" data-t="04:47:43">[04:47:43]</a>.
    *   Mount local data and cache folders as volumes (`-v /path/to/data:/data`, `-v /path/to/cache:/cache`) <a class="yt-timestamp" data-t="04:47:48">[04:47:48]</a>.
    *   Map port 7007 for the viewer (`-p 7007:7007`) <a class="yt-timestamp" data-t="04:48:13">[04:48:13]</a>.
    *   Allocate memory (`--memory 12g`) <a class="yt-timestamp" data-t="04:48:43">[04:48:43]</a>.
*   **Docker Image Incompatibilities**: Despite using Docker, errors persisted, including `unexpected error from Cuda device count` and `non-supported Hardware` <a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a>. The core problem identified was a mismatch between the host's CUDA version (11.6) and the Docker image's CUDA version (11.8) <a class="yt-timestamp" data-t="02:08:02">[02:08:02]</a>.
*   **Custom Docker Build**: To address this, an attempt was made to build a custom Docker image from the Nerf Studio repository, specifying the correct CUDA architecture (61) for the GPU <a class="yt-timestamp" data-t="02:56:49">[02:56:49]</a>. This lengthy process involved installing PyTorch with CUDA 11.6 <a class="yt-timestamp" data-t="01:04:45">[01:04:45]</a>.

## Preparing Data for Nerf Studio

While tackling installation issues, a practical step was taken to prepare a dataset for future Nerf creation. This involved generating images of a cat from various angles (front, profile, back, three-quarter pose) using Midjourney AI <a class="yt-timestamp" data-t="01:02:08">[01:02:08]</a>. These images were then organized into a directory structure matching Nerf Studio's requirements, including an `images` folder and copying template `colmap` and `transforms.json` files <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>.

## Conclusion

The installation of Nerf Studio, particularly the `tiny-cuda-nn` dependency, proved to be highly challenging due to intricate CUDA, PyTorch, and compiler version incompatibilities <a class="yt-timestamp" data-t="01:59:23">[01:59:23]</a>. The path forward involved upgrading the host machine's CUDA toolkit to version 11.8 to match the compatible Docker image <a class="yt-timestamp" data-t="02:09:21">[02:09:21]</a>, which necessitated a system reboot <a class="yt-timestamp" data-t="02:14:14">[02:14:14]</a>.