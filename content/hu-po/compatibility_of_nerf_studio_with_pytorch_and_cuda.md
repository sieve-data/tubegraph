---
title: Compatibility of Nerf Studio with PyTorch and Cuda
videoId: Ir1QMPMqPKg
---

From: [[hu-po]] <br/> 

[[introduction_to_nerf_studio_library | Nerf Studio]] is a tool designed to simplify the end-to-end process of creating Neural Radiance Fields (Nerfs) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>. It provides a simple API and is permissively licensed <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>. This article details the compatibility challenges encountered when setting up [[introduction_to_nerf_studio_library | Nerf Studio]], primarily concerning its dependencies on PyTorch and CUDA.

## Initial Setup Requirements

To set up [[introduction_to_nerf_studio_library | Nerf Studio]], an Nvidia graphics card with CUDA installed is required <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. The installation process typically begins by creating a Conda environment <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

## [[installation_process_and_issues_with_nerf_studio | Installation Process and Issues]]

### PyTorch Version Incompatibility

Initially, [[introduction_to_nerf_studio_library | Nerf Studio]] was observed to be using [[pytorch_20_and_openai_triton | PyTorch 2.0]] <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. This led to a common error: "no module named torch six" <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>. Research indicated that [[pytorch_20_and_openai_triton | PyTorch 2.0]] no longer supports `torch.six` <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

*   **Solution**: To resolve this, it was necessary to downgrade the PyTorch version to an older release, specifically less than 2.0 <a class="yt-timestamp" data-t="00:15:29">[00:15:29]</a>, such as PyTorch 1.13 with CUDA 11.6 <a class="yt-timestamp" data-t="01:04:45">[01:04:45]</a>.

### Tiny Cuda NN Dependency

Even after addressing the PyTorch version, another error emerged: "name tcnn is not defined" <a class="yt-timestamp" data-t="01:17:47">[01:17:47]</a>. This refers to Tiny Cuda NN, described as a "lighting fast C++ Cuda neural network framework" <a class="yt-timestamp" data-t="01:19:20">[01:19:20]</a>.

Installation attempts for Tiny Cuda NN faced several challenges:
*   **Compilation Issues**: Building Tiny Cuda NN from source led to "failed to detect a default Cuda architecture" errors <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>. This implied the need to specify the target compute capability for the GPU <a class="yt-timestamp" data-t="00:25:20">[00:25:20]</a>.
*   **Cuda Architecture Configuration**: For an Nvidia GeForce 1080 TI, the correct Cuda architecture value is 61 <a class="yt-timestamp" data-t="00:55:05">[00:55:05]</a>. Attempts were made to set `cmake Cuda architectures` to this value <a class="yt-timestamp" data-t="00:34:25">[00:34:25]</a>, as well as ensure the correct GCC version (GCC 11.3.0 was present, satisfying the requirement of 8 or higher) <a class="yt-timestamp" data-t="00:37:36">[00:37:36]</a>, and CMake version (3.26 was present, satisfying 3.21 or higher) <a class="yt-timestamp" data-t="00:38:14">[00:38:14]</a>.
*   **Environment Variables**: It was crucial to set `CUDA_HOME` and `CUDA_PATH` environment variables to ensure the system correctly located CUDA installations <a class="yt-timestamp" data-t="02:06:31">[02:06:31]</a>.
*   **Symbol Undefined Error**: Despite efforts, an "undefined symbol" error related to Cuda caching allocator persisted, indicating an incompatibility issue between the installed PyTorch version and the Tiny Cuda NN library version <a class="yt-timestamp" data-t="01:59:39">[01:59:39]</a>.

## [[docker_usage_for_setting_up_nerf_studio | Docker Usage for Setting Up Nerf Studio]]

Recognizing the complexity of dependency management, using a Docker image for [[introduction_to_nerf_studio_library | Nerf Studio]] was considered a potentially cleaner solution <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>.

The steps for using the Docker image included:
1.  **Pulling the image**: `docker pull dromny/nerfstudio:0.1.9` <a class="yt-timestamp" data-t="00:46:07">[00:46:07]</a>.
2.  **Running the container**: The `docker run` command involved several parameters <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>:
    *   `--gpus all`: To make all GPUs available to Docker <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>.
    *   `-v`: To mount local data and cache folders into the container <a class="yt-timestamp" data-t="00:47:48">[00:47:48]</a>.
    *   `-p 7007:7007`: To open port 7007 for the web viewer <a class="yt-timestamp" data-t="00:48:13">[00:48:13]</a>.
    *   `--rm -it`: To delete the container after use and open an interactive terminal <a class="yt-timestamp" data-t="00:48:26">[00:48:26]</a>.
    *   `--shm-size 12G`: To allocate 12GB of shared memory to the container <a class="yt-timestamp" data-t="00:48:43">[00:48:43]</a>.

### Docker Image Cuda Version Incompatibility

Even with Docker, a compatibility issue arose: the local CUDA version was 11.6, while the Docker image was built for CUDA 11.8 <a class="yt-timestamp" data-t="02:08:02">[02:08:02]</a>. This incompatibility led to `unknown compute capability` errors when trying to run [[inference and training considerations for modern GPUs | training jobs]] within the Docker container <a class="yt-timestamp" data-t="01:19:13">[01:19:13]</a>.

*   **Proposed Solution**: The path forward involved either reinstalling the local NVIDIA drivers and CUDA version to 11.8 to match the Docker image <a class="yt-timestamp" data-t="02:08:21">[02:08:21]</a>, or rebuilding the Docker image with CUDA 11.6. The former was attempted by installing CUDA Toolkit 11.8 on the host system <a class="yt-timestamp" data-t="02:09:26">[02:09:26]</a>.

## Conclusion

Despite extensive troubleshooting, including managing PyTorch versions, resolving Tiny Cuda NN compilation issues, and leveraging Docker, full compatibility was not achieved within the session due to the need for a system reboot after updating CUDA drivers <a class="yt-timestamp" data-t="02:14:14">[02:14:14]</a>. The experience highlighted the persistent challenges in managing CUDA and its dependencies for machine learning frameworks like [[introduction_to_nerf_studio_library | Nerf Studio]] on Linux systems <a class="yt-timestamp" data-t="02:17:50">[02:17:50]</a>.