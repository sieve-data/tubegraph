---
title: Setting up and installing MMDetection environment
videoId: SWB2pTY3UDM
---

From: [[hu-po]] <br/> 

[[mmdetection_open_source_object_detection_toolkit|MMDetection]] is an open-source object detection toolbox built on PyTorch, and it is a component of the OpenMMLab project, an open-source community that contributes to object detection [00:01:01]. The project operates under the permissive Apache 2 license, which is a variant of the MIT license [00:01:52].

## Environment Setup and Prerequisites

The setup discussed takes place on a Linux system [00:00:47].

### Python Virtual Environment
To manage dependencies, a Python virtual environment is created using `pyenv` [00:03:39].
```bash
pyenv virtualenv mmdet
pyenv activate mmdet
```
A second environment, `mmdet2`, was later created for a fresh start during troubleshooting [00:29:53].

### Development Environment
VS Code is used as the development environment, with the Python interpreter configured to use the created virtual environment [00:03:15].

### CUDA and PyTorch Compatibility
It's important to check your system's CUDA version. The discussed system uses CUDA 11.6 [00:05:18]. The master branch of [[mmdetection_open_source_object_detection_toolkit|MMDetection]] works with PyTorch 1.5 and newer [00:05:30]. The system was running PyTorch 1.13, which is compatible [00:29:15].

## Installation Process

### Initial Pip Installation
The initial attempt involves installing [[mmdetection_open_source_object_detection_toolkit|MMDetection]] via pip [00:02:21]:
```bash
pip install mmdet
```
This command installs several generic dependencies, including `scipy`, `pycocotools` (Python tools for the COCO dataset), `numpy`, `matplotlib`, and `Pillow` (Python Imaging Library) [00:04:41]. Notably, this command does *not* install PyTorch or CUDA [00:04:58].

### Installing PyTorch with CUDA
As PyTorch is not automatically installed with `pip install mmdet`, it must be installed separately, ensuring compatibility with your CUDA version [00:05:36]. The command used for Linux, Pip, and CUDA 11.6 was [00:05:43]:
```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
```

### Cloning the MMDetection Repository
Due to dependency issues and the need for specific configuration files (like `yolo_mobilenet_coco.py`), it became necessary to clone the [[mmdetection_open_source_object_detection_toolkit|MMDetection]] GitHub repository [00:21:11]:
```bash
git clone https://github.com/open-mmlab/mmdetection.git
```
Then, navigate into the cloned directory:
```bash
cd mmdetection
```

### Installing MMCV-Full and MMDetection from Source
[[mmdetection_open_source_object_detection_toolkit|MMDetection]] requires `mmcv-full` for comprehensive features including CPU and CUDA operations [00:13:16].
The recommended installation order is [00:30:12]:
1.  Install `openmim` (a command-line tool for OpenMMLab projects):
    ```bash
    pip install openmim
    ```
2.  Install `mmcv-full` using `mim`:
    ```bash
    mim install mmcv-full
    ```
    This command also installs `addict` (a dictionary subclass for attribute-style access) and `opencv-python` [00:14:13].
3.  Install [[mmdetection_open_source_object_detection_toolkit|MMDetection]] itself in editable mode from the cloned repository [00:23:41]:
    ```bash
    pip install -v -e .
    ```

### Troubleshooting `distutils` and `setuptools`
During installation, a `No module named setuptools.distutils` error was encountered [00:21:51]. This issue was resolved by downgrading `setuptools` to an older version [00:34:37]:
```bash
pip install setuptools==59.5.0 # Example version, actual version found was 59.5.0 [00:34:37]
```

## Verifying the Installation and Inference

### Basic Import
After installation, `import mmdet` should work without errors [00:15:39].

### Running an Inference Demo
[[mmdetection_open_source_object_detection_toolkit|MMDetection]] provides an API for initializing detectors and running inference [00:16:32].
To run an inference, you typically need a model configuration file (`.py`) and a checkpoint file (`.pth`) [00:32:51]. These can be downloaded using `mim download` [00:28:28]:
```python
from mim.apis import download

# Example of downloading a specific model
download(config='yolo/yolov3_mobilenetv2_320_coco.py', dest_root='./')
download(checkpoint='yolo/yolov3_mobilenetv2_320_coco.pth', dest_root='./')
```
*Note: An outdated API argument `destination_dur` was found in the documentation, which was actually `dest_root`. This discrepancy led to a pull request to fix the documentation [00:38:42].*

A Python script can then be used to load the detector and perform inference:
```python
from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import os

# Define config and checkpoint paths
config_file = './yolov3_mobilenetv2_320_coco.py'
checkpoint_file = './yolov3_mobilenetv2_320_coco.pth'

# Initialize the detector
detector = init_detector(config_file, checkpoint_file, device='cuda:0') # Or 'cpu'
# Path to image
img = '/tmp/AI_astronaut.png' # Example image path

# Perform inference
result = inference_detector(detector, img)

# Visualize the results
show_result_pyplot(detector, img, result, score_thr=0.3)
```

### Model Performance and Comparison
The speaker tested [[mmdetection_open_source_object_detection_toolkit|MMDetection]] with different images and models:

*   **YOLO MobileNetV2**: This is a smaller, faster model [00:56:07].
    *   On an AI-generated image of an astronaut at a table, it showed low confidence for objects like "bottle" and "dog" [00:36:50].
    *   On an AI-generated image of a cowboy on a horse, it detected "person" and "horse" with high confidence [01:10:34].
    *   On a real photo of people in a stadium, it detected only a handful of people with varying confidence [01:11:02].

*   **Faster R-CNN ResNet-101**: A larger, more complex model [00:58:34].
    *   On the AI-generated astronaut image, it still produced peculiar results like "teddy bear" and "toothbrush," suggesting issues with the AI-generated texture [01:09:48].
    *   On the AI-generated cowboy image, it also detected "person" and "horse" with high confidence, similar to YOLO but with possibly higher scores [01:10:34].
    *   On the real photo of people in a stadium, this model performed significantly better, detecting almost everyone in the crowd with high confidence (e.g., 0.99, 1.0, 0.96) and even finding "cell phones" [01:10:58].

This demonstrates that larger models generally provide higher confidence and better detection in crowded scenes, but AI-generated images with unusual textures can still pose challenges [01:10:07]. Attempting to "crispen" an AI-generated image using a face restoration service like Replicate actually worsened the detection results [01:14:51].

## [[exploring_mmdetection_model_zoo|MMDetection Model Zoo]]

[[mmdetection_open_source_object_detection_toolkit|MMDetection]] offers a [[exploring_mmdetection_model_zoo|model zoo]] with a wide array of pre-trained models. These models are categorized by paper name (e.g., Faster R-CNN, YOLO) and architecture (e.g., ResNet, MobileNet) [01:05:06]. The official model links and benchmarks can be found on the OpenMMLab website [00:56:47].

## Project Health and Community

[[mmdetection_open_source_object_detection_toolkit|MMDetection]] is part of the OpenMMLab project, an open-source community [00:01:07].

*   **License**: Apache 2 [00:01:52].
*   **Documentation**: Available [00:01:59].
*   **Continuous Integration (CI)**: The project uses CI, and a "build failing" badge indicates issues with the latest pushed code, which can affect stability [00:08:17].
*   **Code Coverage**: The project has about 60% code coverage, which is considered acceptable for an open-source project [00:09:24].
*   **Contributors**: Contributions started around 2018, showing consistent linear growth. Initial contributors have moved on, with new maintainers taking over. This suggests a healthy, evolving project [01:15:55].
*   **Releases**: The project has a good amount of releases (45 total), with frequent updates (e.g., two and three weeks ago), indicating active maintenance [01:18:18].
*   **Issues**: The project shows many closed issues, which indicates active support and bug resolution [01:18:06].

Overall, [[mmdetection_open_source_object_detection_toolkit|MMDetection]] appears to be a healthy and actively maintained open-source project providing a robust object detection framework [01:18:42].