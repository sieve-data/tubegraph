---
title: Installation process and issues with Nerf Studio
videoId: Ir1QMPMqPKg
---

From: [[hu-po]] <br/> 

The video details attempts to install and configure [[introduction_to_nerf_studio_library | Nerf Studio]], a tool designed to simplify the end-to-end process of creating NeRFs (Neural Radiance Fields) <a class="yt-timestamp" data-t="01:39">[00:01:39]</a>. The tool has a permissive license <a class="yt-timestamp" data-t="01:26">[00:01:26]</a>.

## Initial Setup and Environment Requirements

Nerf Studio requires an Nvidia graphics card with CUDA installed <a class="yt-timestamp" data-t="01:50">[00:01:50]</a>. The installation process typically involves creating a Conda environment <a class="yt-timestamp" data-t="01:58">[01:58]</a> and updating `pip` <a class="yt-timestamp" data-t="02:35">[02:35]</a>. The project uses PyTorch, with a version of 2.0 initially noted as "interesting" <a class="yt-timestamp" data-t="03:27">[00:03:27]</a>, but expected to be backwards compatible <a class="yt-timestamp" data-t="03:35">[00:03:35]</a>.

The process encountered initial incompatibilities with `tensorflow-datasets`, `protobuf`, and `grpc` <a class="yt-timestamp" data-t="04:17">[00:04:17]</a>.

## Nerf Studio Viewer and Remote Access

Nerf Studio includes a viewer that connects to a websocket server when a training job is running <a class="yt-timestamp" data-t="05:08">[00:05:08]</a>. This viewer can be accessed remotely if SSH is set up on the machine running Nerf Studio, using SSH local port forwarding (e.g., `ssh -L` command) <a class="yt-timestamp" data-t="05:25">[00:05:25]</a>. This method is also applicable for [[challenges_of_robotics_integration | GradIO frontends]] <a class="yt-timestamp" data-t="05:57">[00:05:57]</a>.

## Core Installation Challenges

The installation repeatedly ran into significant issues, primarily related to CUDA compatibility and a dependency called `tiny-cuda-nn`.

### Issue 1: `no module named torch six`

After initial `pip` installation attempts, the first major error encountered was `no module named torch six` <a class="yt-timestamp" data-t="11:53">[01:11:53]</a>.
*   **Cause:** This error stemmed from PyTorch 2.0 no longer supporting `torch.six` <a class="yt-timestamp" data-t="14:37">[01:14:37]</a>.
*   **Attempted Solution:** Downgrading PyTorch to a version less than 2.0 (specifically, PyTorch 1.13 with CUDA 11.6 was attempted) <a class="yt-timestamp" data-t="15:29">[01:15:29]</a>.

### Issue 2: `tcnn is not defined` (Tiny CUDA NN)

Even after addressing the `torch six` issue, the installation failed with `tcnn is not defined` <a class="yt-timestamp" data-t="17:38">[01:17:38]</a>. This indicates a problem with the `tiny-cuda-nn` dependency.

*   **Problem:** Direct `pip install git` for `tiny-cuda-nn` did not resolve the issue <a class="yt-timestamp" data-t="18:28">[01:18:28]</a>.
*   **Attempt to Build from Source:** To overcome this, building `tiny-cuda-nn` from source was attempted <a class="yt-timestamp" data-t="24:02">[00:24:02]</a>.
    *   **Sub-Issue: `failed to detect a default Cuda architecture` / `cmake Cuda architectures must be non-empty if set`**:
        *   This required manually setting the `CMAKE_CUDA_ARCHITECTURES` variable (e.g., to `86` or `61` for a GeForce 1080 TI <a class="yt-timestamp" data-t="55:05">[00:55:05]</a>) during the `cmake` command <a class="yt-timestamp" data-t="34:25">[00:34:25]</a>.
        *   Verification of GCC version (11.3.0, meeting the requirement of 8 or higher) <a class="yt-timestamp" data-t="37:36">[00:37:36]</a> and CMake version (3.26, meeting the requirement of 3.21 or higher) <a class="yt-timestamp" data-t="38:14">[00:38:14]</a> was performed.
        *   The `LD_LIBRARY_PATH` and `PATH` environment variables were adjusted to include CUDA 11.6 directories <a class="yt-timestamp" data-t="39:26">[00:39:26]</a>.
        *   Eventually, a `cmake` build was successful after specific environment variable adjustments and library path modifications <a class="yt-timestamp" data-t="01:32:31">[01:32:31]</a>.
    *   **Persistent Error: `undefined symbol: cudaCachingAllocator`**: Despite successful `tiny-cuda-nn` builds, this error persisted upon attempting to import the module or run Nerf Studio <a class="yt-timestamp" data-t="01:59:33">[01:59:33]</a>. This indicated an incompatibility between installed PyTorch and `tiny-cuda-nn` <a class="yt-timestamp" data-t="01:59:45">[01:59:45]</a>. Reinstalling PyTorch, TorchVision, and FunTorch with specific CUDA versions (11.6 again) was attempted <a class="yt-timestamp" data-t="02:03:26">[02:03:26]</a>.

## Attempting [[docker_usage_for_setting_up_nerf_studio | Docker Usage for Setting Up Nerf Studio]]

Recognizing the persistent dependency issues, a [[docker_usage_for_setting_up_nerf_studio | Docker usage for setting up Nerf Studio]] approach was pursued, hoping containerization would abstract away dependency conflicts <a class="yt-timestamp" data-t="00:44:02">[00:44:02]</a>.
*   The official Docker image (`dromny/nerfstudio:0.1.9`) was pulled <a class="yt-timestamp" data-t="00:45:55">[00:45:55]</a>.
*   The Docker run command involved mounting volumes for data and cache, exposing port 7007 (for the viewer), assigning memory (12 GB), and enabling interactive mode <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>.
*   **Docker Issues:** Running the pre-built Docker image resulted in `unexpected error from Cuda device count` and `non-supported Hardware` errors <a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a>, still trying to import `tcnn` <a class="yt-timestamp" data-t="00:53:40">[00:53:40]</a>.
*   **Cause:** The Docker image used CUDA 11.8, while the host system had CUDA 11.6, leading to incompatibility <a class="yt-timestamp" data-t="02:08:02">[02:08:02]</a>.
*   **Attempted Solution:** Rebuilding the Docker image from source within the Nerf Studio repository, specifying the `CUDA_ARCHITECTURES` (61) for the local GPU <a class="yt-timestamp" data-t="00:56:53">[00:56:53]</a>. This process took a significant amount of time <a class="yt-timestamp" data-t="00:58:54">[00:58:54]</a>.

## Dataset Creation with Midjourney AI

While troubleshooting installation, a side project involved generating a custom dataset for NeRF creation using Midjourney AI. Images of a white Bengal cat were generated from various angles (front, profile, behind, three-quarter pose) <a class="yt-timestamp" data-t="01:03:35">[01:03:35]</a>. The goal was to create a dataset that includes different camera positions and a consistent background <a class="yt-timestamp" data-t="01:16:48">[01:16:48]</a>. The dataset was structured to match Nerf Studio's requirements, with images placed in a dedicated `images` folder alongside placeholder `colmap`, `output`, and `transforms.json` files <a class="yt-timestamp" data-t="01:07:05">[01:07:05]</a>. It was acknowledged that the number of images might be insufficient for a high-quality NeRF <a class="yt-timestamp" data-t="01:47:47">[01:47:47]</a>.

## Conclusion of Installation Attempts

The primary obstacle remained the [[compatibility_of_nerf_studio_with_pytorch_and_cuda | compatibility of Nerf Studio with PyTorch and CUDA]], specifically the persistent `undefined symbol: cudaCachingAllocator` error linked to `tiny-cuda-nn` <a class="yt-timestamp" data-t="01:59:33">[01:59:33]</a>. The core problem was identified as a mismatch between the host's CUDA version (11.6) and the CUDA version expected or used by the Docker image/`tiny-cuda-nn` (11.8) <a class="yt-timestamp" data-t="02:08:02">[02:08:02]</a>. The final attempt involved upgrading the host machine's CUDA toolkit to 11.8 to match the Docker image <a class="yt-timestamp" data-t="02:09:26">[02:09:26]</a>. This required updating system packages and removing older CUDA versions <a class="yt-timestamp" data-t="02:13:08">[02:13:08]</a>. The installation process ended with a necessary computer reboot to apply driver changes <a class="yt-timestamp" data-t="02:16:06">[02:16:06]</a>, leaving the final outcome of the Nerf Studio installation unresolved in this session <a class="yt-timestamp" data-t="02:21:41">[02:21:41]</a>.