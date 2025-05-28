---
title: MMDetection overview
videoId: SWB2pTY3UDM
---

From: [[hu-po]] <br/> 

[[using_mmdetection_in_python | MMDetection]] is an open-source object detection toolbox built on PyTorch [00:01:01]. It is a component of the larger [[openmmlab_project | OpenMMLab project]] [00:01:07].

## What is MMDetection?
[[using_mmdetection_in_python | MMDetection]] serves as an object detection toolbox [00:01:41]. It operates under the Apache 2.0 license, which is a permissive variant similar to MIT [00:01:52].

### Key Features
*   **Modular Design**: The detection framework is decomposed into various components, allowing users to easily construct and customize object detection frameworks by combining different modules [00:07:09].
*   **Framework Support**: It directly supports popular and contemporary detection frameworks such as Faster R-CNN, Mask R-CNN (used for segmentation), and RetinaNet [00:07:19].
*   **GPU Acceleration**: Basic bounding box and mask operations (segmentation) run on GPUs [00:07:37].
*   **Performance**: Training speed is either faster than or comparable to other detection codebases, including Detectron2 [00:07:41].
*   **Origin**: The toolbox is derived from the codebase developed by the MMDetection team, which won the COCO detection challenge in 2018 [00:08:01].
*   **State-of-the-Art (SOTA) Models**: The 3x version includes RTMDet, a family of fully convolutional single-stage detectors, which achieves a strong parameter-accuracy trade-off and new state-of-the-art performance in instant segmentation and rotated object detection tasks [00:09:33]. It also boasts SOTA results for object detection in aerial images and real-time segmentation for MS COCO [00:09:55].

## Installation and Setup
[[using_mmdetection_in_python | MMDetection]] can be installed via `pip` [00:02:13]. The master branch is compatible with PyTorch 1.5+ [00:07:03].

Installation steps:
1.  **Create a virtual environment**:
    ```bash
    pi m virtualenv mmdet
    pi m activate mmdet
    ```
    [00:03:41]
2.  **Install `openmim`**:
    ```bash
    pip install openmim
    ```
    [00:30:20]
3.  **Install `mmcv-full`**:
    ```bash
    mim install mmcv-full
    ```
    [00:30:38]
    *   Note: `mmcv-full` is expected to be renamed to `mmcv` [00:26:57].
4.  **Install PyTorch with CUDA**: It's crucial to install the correct PyTorch version compatible with your CUDA version (e.g., CUDA 11.6 compatible PyTorch) [00:05:18].
5.  **Clone the MMDetection repository**:
    ```bash
    git clone https://github.com/open-mmlab/mmdetection.git
    cd mmdetection
    ```
    [00:23:28]
6.  **Install MMDetection in editable mode**:
    ```bash
    pip install -v -e .
    ```
    [00:23:43]
7.  **Troubleshooting `distutils` error**: A common issue is a `distutils` version conflict. Downgrading `setup-tools` can resolve this [00:34:37].
    ```bash
    pip install setuptools==59.5.0
    ```
    [00:34:37]

## Running Inference
To run an inference demo, users need to download specific config and checkpoint files using the `mim` tool [00:20:28].

Example Python code for inference:
```python
import mmdet
from mmdet.apis import init_detector, inference_detector, show_result_pyplot
import os

# Download model configuration and checkpoint files
# For example, using a pre-trained Faster R-CNN with ResNet101
config_file = 'configs/faster_rcnn/faster_rcnn_r101_fpn_2x_coco.py'
checkpoint_file = 'https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r101_fpn_2x_coco/faster_rcnn_r101_fpn_2x_coco_bbox_mAP-0.398_20200504_163329-873a6a95.pth'

# Initialize the detector
# Ensure the config_file path is correct relative to your current directory or provide full path
detector = init_detector(config_file, checkpoint_file, device='cuda:0')

# Path to the image
image_path = '/tmp/AI_astronaut.png' # Example image path

# Perform inference
result = inference_detector(detector, image_path)

# Visualize the results
show_result_pyplot(detector, image_path, result, score_thr=0.3, out_file='result.jpg')
```
[01:17:19]

When testing with different models (e.g., MobileNet vs. ResNet 101):
*   A smaller model like MobileNet may produce lower confidence scores or miss some objects, especially in complex or AI-generated images [01:09:52]. For instance, it detected a "bottle" and "dog" with low confidence in an AI astronaut image [00:36:50].
*   A larger model like ResNet 101 often provides higher confidence scores and detects more objects in crowded scenes [01:10:34]. In a real photo of a stadium, it accurately detected many people with high confidence (e.g., 0.99, 1.0, 0.96) and additional objects like cell phones [01:10:58].

## Project Health and Community Contribution
The [[openmmlab_project | OpenMMLab project]] and [[using_mmdetection_in_python | MMDetection]] demonstrate good project health:
*   **Continuous Integration (CI)**: The project uses CI tools to build packages whenever code is pushed. While the build status might show as failing at times, the continuous integration pipeline is active [00:08:17].
*   **Code Coverage**: Around 60% of the codebase is covered by tests, which is considered acceptable for an open-source project [00:08:44].
*   **Active Development**: Contributions have been consistent since 2018, showing a stable contribution graph [01:15:55].
*   **Maintainers**: There's evidence of initial contributors (e.g., HELOC, YH Cow) and a transition to new maintainers (e.g., ZW Wayne) who continue to push the project forward [01:16:12].
*   **Regular Releases**: There are frequent releases, with updates as recent as two and three weeks prior to the transcript [01:18:23].
*   **Issue Management**: The project actively closes issues, indicating that questions and problems are being addressed [01:18:06].

The project welcomes community contributions, such as fixing documentation bugs [00:39:22]. A pull request to fix a typo in the `mim` download API argument (from `destination_dur` to `dest_root`) was demonstrated as an example of contributing to an open-source project [00:41:42].

Overall, [[using_mmdetection_in_python | MMDetection]] provides a robust and versatile open-source toolkit for object detection, offering a wide range of models in its model zoo and flexibility for deployment on both GPU and CPU [01:18:50].