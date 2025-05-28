---
title: Using MMDetection in Python
videoId: SWB2pTY3UDM
---

From: [[hu-po]] <br/> 

[[mmdetection_overview | MM detection]] is an open-source [[object_detection_with_pytorch | object detection]] toolbox built on PyTorch, and it is a component of the [[openmmlab_project | OpenMMLab project]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. It is designed to be a comprehensive and customizable framework for various [[object_detection_with_pytorch | object detection]] tasks <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

## Key Features

*   **Open Source and Permissive License:** [[mmdetection_overview | MM detection]] operates under the Apache 2 license, a permissive license that allows for broad use <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
*   **PyTorch-Based:** It is built on PyTorch, leveraging its capabilities for deep learning model development <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.
*   **Modular Design:** The framework decomposes the [[object_detection_with_pytorch | detection]] process into different components, allowing users to easily construct customized [[object_detection_with_pytorch | object detection]] frameworks by combining various modules <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
*   **Extensive Framework Support:** It directly supports popular and contemporary [[object_detection_with_pytorch | detection]] frameworks such as Faster R-CNN, Mask R-CNN (used for segmentation), and RetinaNet <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.
*   **GPU Acceleration:** All basic bounding box and mask operations run on GPUs, leading to training speeds that are faster than or comparable to other [[object_detection_with_pytorch | detection]] codebases, including Detectron2 <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
*   **State-of-the-Art Performance:** The toolbox stems from a codebase developed by the [[mmdetection_overview | MM detection]] team, which won the COCO [[object_detection_with_pytorch | detection]] challenge in 2018 <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. It continues to push for state-of-the-art performance in areas like [[object_detection_with_pytorch | object detection]] in aerial images and real-time segmentation for MS COCO <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Model Zoo:** [[mmdetection_overview | MM detection]] includes a wide range of pre-trained models available in its Model Zoo, offering various architectures and performance characteristics <a class="yt-timestamp" data-t="00:56:04">[00:56:04]</a>.

## Installation Guide

### Prerequisites

Before installing, ensure you have:
*   A Python virtual environment activated (e.g., created with `pienv virtualenv mmdet`) <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
*   NVIDIA CUDA installed. The master branch typically works with PyTorch 1.5+, and a CUDA version like 11.6 or newer is compatible <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Initial Installation Steps

1.  **Install `mmdet` via pip:**
    ```bash
    pip install mmdet
    ```
    This command installs `SciPy`, `pycocotools` (Python tools for the COCO dataset), `numpy`, `matplotlib`, and `Pillow` (Python Image Library) <a class="yt-timestamp" data-t="00:04:41">[00:04:41]</a>. Note that `pip install mmdet` does *not* install PyTorch or CUDA dependencies automatically <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

2.  **Install `openmim`:** This is a tool provided by [[openmmlab_project | OpenMMLab]] to simplify the installation of its components and models.
    ```bash
    pip install openmim
    ```
    <a class="yt-timestamp" data-t="00:30:23">[00:30:23]</a>

3.  **Install `mmcv-full` using `mim`:**
    ```bash
    mim install mmcv-full
    ```
    This command ensures `mmcv-full`, which includes comprehensive features and various CPU and CUDA operations, is installed <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>.

4.  **Install PyTorch (if not already present):** Choose the appropriate PyTorch version based on your CUDA version from the PyTorch website. For example, for Linux with Pip and CUDA 11.6:
    ```bash
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu116
    ```
    <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>

5.  **Install from Source (Recommended):** Clone the [[mmdetection_overview | MM detection]] repository and install it in editable mode for full functionality:
    ```bash
    git clone https://github.com/open-mmlab/mmdetection.git
    cd mmdetection
    pip install -v -e .
    ```
    <a class="yt-timestamp" data-t="00:23:28">[00:23:28]</a>

### Troubleshooting Dependencies

A common issue encountered during installation is with `setuptools` and `distutils`. If you face `no module named distutils` or similar errors, downgrading `setuptools` can resolve it:
```bash
pip install setuptools==59.5.0
```
<a class="yt-timestamp" data-t="00:34:37">[00:34:37]</a>

## Performing Inference

### Setting up the Inference Script

A basic Python script to perform inference with [[mmdetection_overview | MM detection]] might look like this:

```python
import os
from mmdet.apis import init_detector, inference_detector, show_result_pyplot

# Define model configuration and checkpoint files
# These files need to be downloaded or present locally
# Example: model_config_path = 'path/to/your/model_config.py'
# Example: model_checkpoint_path = 'path/to/your/model_checkpoint.pth'

# Initialize the detector
# detector = init_detector(model_config_path, model_checkpoint_path, device='cuda:0')

# Perform inference on an image
# image_path = 'path/to/your/image.jpg'
# result = inference_detector(detector, image_path)

# Visualize the results
# show_result_pyplot(detector, image_path, result)
```
<a class="yt-timestamp" data-t="01:17:12">[01:17:12]</a>, <a class="yt-timestamp" data-t="01:17:31">[01:17:31]</a>

### Acquiring Models and Configs

Models and [[configuring_object_detection_models | config file]]s are necessary for inference. These can be downloaded using the `mim` tool. For example, to download a YOLOv3 MobileNetV2 model:
```bash
mim download mmdet --config yolov3_mobilenetv2_320_300e_coco --dest .
```
<a class="yt-timestamp" data-t="00:20:28">[00:20:28]</a>, <a class="yt-timestamp" data-t="00:37:33">[00:37:33]</a>

Alternatively, you can manually download models from the [[openmmlab_project | OpenMMLab]] [[mmdetection_overview | MM detection]] Model Zoo <a class="yt-timestamp" data-t="00:56:47">[00:56:47]</a>.

### Running Detection

After setting up the detector with a [[configuring_object_detection_models | config file]] and checkpoint, you can run inference on an image. The `inference_detector` function returns the detection results, and `show_result_pyplot` can visualize them directly <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>.

It's important to note that the API for downloading models (`mim download`) might change. For instance, the `destination_dir` argument was changed to `dest_root` <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>. Checking the latest documentation is always recommended.

## Model Performance and Zoo

[[mmdetection_overview | MM detection]] offers a diverse Model Zoo, which includes various [[object_detection_with_pytorch | object detection]] models with different architectures and complexities. Examples include:
*   **YOLOv3 Tiny MobileNetV2:** A smaller, faster model suitable for quick inference, though it may have lower confidence scores and miss some objects in crowded scenes <a class="yt-timestamp" data-t="01:00:05">[01:00:05]</a>.
*   **Faster R-CNN ResNet-101:** A larger, more powerful model that generally yields higher confidence scores and better detection in complex scenarios, like identifying multiple people in a crowded image <a class="yt-timestamp" data-t="01:06:13">[01:06:13]</a>, <a class="yt-timestamp" data-t="01:10:58">[01:10:58]</a>.

Models can perform differently based on the input image's characteristics. For instance, AI-generated images with unusual textures might lead to unexpected detections (e.g., "teddy bear" or "toothbrush" in an astronaut image) <a class="yt-timestamp" data-t="01:09:48">[01:09:48]</a>. Pre-processing or enhancing images (like "crisping" them using a face restoration model) does not always improve [[object_detection_with_pytorch | detection]] performance <a class="yt-timestamp" data-t="01:14:49">[01:14:49]</a>.

## Project Health and Community Contribution

The [[mmdetection_overview | MM detection]] repository shows signs of a healthy open-source project <a class="yt-timestamp" data-t="01:18:42">[01:18:42]</a>:
*   **Consistent Contributions:** The project has seen steady contributions since around 2018, indicating continuous development <a class="yt-timestamp" data-t="01:15:55">[01:15:55]</a>.
*   **Active Maintainership:** While initial contributors may shift away, new maintainers take over, ensuring the project's longevity <a class="yt-timestamp" data-t="01:16:32">[01:16:32]</a>.
*   **Regular Releases:** With 45 total releases and recent updates within weeks, the project is actively maintained and improved <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>.
*   **Issue Resolution:** A high number of closed issues indicates responsiveness to community questions and bug reports <a class="yt-timestamp" data-t="01:18:06">[01:18:06]</a>.
*   **Community Contribution:** Users can contribute by forking the repository, making changes (e.g., fixing documentation typos), and submitting pull requests <a class="yt-timestamp" data-t="00:40:59">[00:40:59]</a>. This collaborative model helps improve the project for everyone <a class="yt-timestamp" data-t="00:44:53">[00:44:53]</a>.

---
**Disclaimer:** This article is based solely on the provided transcript and may not cover all aspects of [[mmdetection_overview | MM detection]]. For the most up-to-date information, refer to the official [[mmdetection_overview | MM detection]] documentation and repository.