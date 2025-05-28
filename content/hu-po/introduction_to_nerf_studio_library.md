---
title: Introduction to Nerf Studio library
videoId: Ir1QMPMqPKg
---

From: [[hu-po]] <br/> 

[[Introduction to Nerf Studio library | Nerf Studio]] is a tool designed to simplify the end-to-end process of creating [[3D Gaussian splatting and Nerfs | NeRFs]] (Neural Radiance Fields) <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. It features a very permissive license <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a> and is actively developed with many contributors <a class="yt-timestamp" data-t="08:04:00">[08:04:00]</a>.

## Core Functionality
[[Introduction to Nerf Studio library | Nerf Studio]] provides a simple API that streamlines the creation of [[3D Gaussian splatting and Nerfs | NeRFs]] <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>. A [[3D Gaussian splatting and Nerfs | NeRF]] itself is fundamentally a neural network that functions as a 3D file <a class="yt-timestamp" data-t="01:52:16">[01:52:16]</a>.

### Model Training and Output
The `nerfacto` model is recommended for real-world scenes <a class="yt-timestamp" data-t="06:37:00">[06:37:00]</a>. After a [[3D Gaussian splatting and Nerfs | NeRF]] model is generated, users have the option to render a video or export a point cloud <a class="yt-timestamp" data-t="07:05:00">[07:05:00]</a>.

## Viewer
[[Introduction to Nerf Studio library | Nerf Studio]] includes a built-in viewer <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>. This viewer connects to a websocket server while the training job is running <a class="yt-timestamp" data-t="05:25:00">[05:25:00]</a>. For remote access, SSH can be used to port into a Linux machine running [[Introduction to Nerf Studio library | Nerf Studio]] <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a>.

## Data Handling
[[Introduction to Nerf Studio library | Nerf Studio]] handles image datasets for [[3D Gaussian splatting and Nerfs | NeRF]] creation. Test data, such as a "poster.zip" containing images of a chair, includes `colmap` data for camera position and `transforms.json` for camera rotation matrices <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>, <a class="yt-timestamp" data-t="11:08:00">[11:08:00]</a>. For custom data, users may need to create a `transforms.json` file to define camera poses <a class="yt-timestamp" data-t="01:49:35">[01:49:35]</a>.

## [[Installation process and issues with Nerf Studio | Installation and Compatibility]]
[[Installation process and issues with Nerf Studio | Nerf Studio]] requires an Nvidia graphics card with [[compatibility_of_nerf_studio_with_pytorch_and_cuda | CUDA]] installed <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>. It uses Conda environments for setup <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>. A key dependency is TinyCUDA-NN <a class="yt-timestamp" data-t="23:52:00">[23:52:00]</a>, which can be challenging to install due to [[compatibility_of_nerf_studio_with_pytorch_and_cuda | PyTorch]] and [[compatibility_of_nerf_studio_with_pytorch_and_cuda | CUDA]] version incompatibilities <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>, <a class="yt-timestamp" data-t="01:59:39">[01:59:39]</a>.

### [[Docker usage for setting up Nerf Studio | Docker Support]]
To alleviate [[installation_process_and_issues_with_nerf_studio | dependency issues]], [[Introduction to Nerf Studio library | Nerf Studio]] provides [[docker_usage_for_setting_up_nerf_studio | Docker]] images <a class="yt-timestamp" data-t="43:56:00">[43:56:00]</a>, with the latest stable version being 0.1.9 <a class="yt-timestamp" data-t="45:55:00">[45:55:00]</a>. The [[docker_usage_for_setting_up_nerf_studio | Docker]] image is designed to work with [[compatibility_of_nerf_studio_with_pytorch_and_cuda | CUDA]] 11.8 <a class="yt-timestamp" data-t="45:24:00">[45:24:00]</a> and requires specifying the target [[compatibility_of_nerf_studio_with_pytorch_and_cuda | CUDA]] architecture (e.g., `61` for a GeForce 1080 TI) <a class="yt-timestamp" data-t="55:01:00">[55:01:00]</a>. Running the [[docker_usage_for_setting_up_nerf_studio | Docker]] container allows for GPU access, volume mounting for data and cache, and port forwarding for the viewer <a class="yt-timestamp" data-t="47:40:00">[47:40:00]</a>.