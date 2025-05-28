---
title: MMDetection open source object detection toolkit
videoId: SWB2pTY3UDM
---

From: [[hu-po]] <br/> 

MMDetection is an [[open_source_ai_models_and_accessibility | open-source object detection]] toolbox built upon [[using_pytorch_for_object_detection | PyTorch]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. It is part of the OpenMMLab project <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, an [[open_source_ai_models_and_accessibility | open-source community]] that contributes to various AI projects <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. MMDetection itself is an [[open_source_ai_models_and_accessibility | open-source project]] <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a> under the Apache 2 license, a permissive license allowing broad use <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.

## Key Features

MMDetection offers several notable features:
*   **Modular Design**: It decomposes the detection framework into different components, allowing users to easily construct custom object detection frameworks by combining various modules <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.
*   **Toolbox Support**: It directly supports popular and contemporary detection frameworks such as Faster R-CNN, Mask R-CNN, and RetinaNet <a class="yt-timestamp" data-t="00:07:23">[00:07:23]</a>. Mask R-CNN and Faster R-CNN are also used for [[image_segmentation_techniques | segmentation]] <a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **GPU Acceleration**: All basic bounding box and mask operations run on GPUs, leading to training speeds that are faster than or comparable to other detection codebases, including Detectron2 <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   **Award-Winning Origin**: The toolbox stems from a codebase developed by the MMDetection team, who won the COCO detection challenge in 2018 <a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
*   **State-of-the-Art Performance**: Newer versions like RTMDet achieve state-of-the-art performance on instant [[image_segmentation_techniques | segmentation]] and rotated object detection tasks <a class="yt-timestamp" data-t="00:09:51">[00:09:51]</a>, including on aerial images and real-time [[image_segmentation_techniques | segmentation]] for MS COCO <a class="yt-timestamp" data-t="01:00:03">[01:00:03]</a>.

## [[setting_up_and_installing_mmdetection_environment | Setting Up and Installing MMDetection Environment]]

The process of [[setting_up_and_installing_mmdetection_environment | installing MMDetection]] involves several steps to manage dependencies and ensure compatibility.

### Initial Installation and Dependencies
1.  **Create a Virtual Environment**: It is recommended to create a new Python virtual environment for MMDetection <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.
    ```bash
    pi m virtual mmdet
    pi m activate mmdet
    ```
2.  **Install MMDetection via Pip**:
    ```bash
    pip install mmdet
    ```
    This command installs packages like `SciPy`, `PyCocoTools`, `NumPy`, `Matplotlib`, and `Pillow` <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>, but notably *not* [[using_pytorch_for_object_detection | PyTorch]] or CUDA <a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>.
3.  **Install PyTorch**: MMDetection's master branch is designed to work with [[using_pytorch_for_object_detection | PyTorch]] 1.5+ <a class="yt-timestamp" data-t="00:07:05">[00:07:05]</a>. The correct [[using_pytorch_for_object_detection | PyTorch]] version must be installed, specifically with the compatible CUDA version (e.g., CUDA 11.6) <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.
    ```bash
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu116
    ```
4.  **Install MMCV**: MMDetection requires MMCV. The `openmim` tool can be used to install `mmcv-full` which includes comprehensive CPU and CUDA operations <a class="yt-timestamp" data-t="00:13:19">[00:13:19]</a>.
    ```bash
    pip install openmim
    mim install mmcv-full
    ```
    This step also installs `addict` and `opencv-python` <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>. `addict` is a Python dictionary subclass that allows items to be accessed and set like attributes using dot notation <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>.

### Troubleshooting and Reinstallation

*   **Module Not Found Errors**: If `mmdet` or `mmcv` modules are not found, it might be due to incorrect installation or an outdated API <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>.
*   **Cloning the Repository**: If pip installation from PyPI is problematic, cloning the MMDetection GitHub repository and installing in editable mode (development mode) is an alternative <a class="yt-timestamp" data-t="00:23:52">[00:23:52]</a>.
    ```bash
    git clone https://github.com/open-mmlab/mmdetection.git
    cd mmdetection
    pip install -v -e .
    ```
*   **`distutils` Compatibility Issues**: A common issue was `setup.py` failing due to `distutils` being replaced <a class="yt-timestamp" data-t="00:21:51">[00:21:51]</a>. Downgrading `setuptools` to an older version can resolve this <a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>.
    ```bash
    pip install setuptools==65.5.0 # Example older version
    ```
*   **Checking Python and PyTorch Versions**: Verify that the installed Python version (e.g., 3.8.0) and [[using_pytorch_for_object_detection | PyTorch]] version (e.g., 1.13) are compatible with the MMDetection version being used <a class="yt-timestamp" data-t="00:29:15">[00:29:15]</a>.

## Usage and Inference

After [[setting_up_and_installing_mmdetection_environment | installation]], MMDetection can be used for object detection inference.

### Basic Inference Steps
1.  **Download Config and Checkpoint Files**: For inference, a configuration file (e.g., `yolov3_mobilenet_v2_320_coco.py`) and its corresponding checkpoint file (model weights) are required <a class="yt-timestamp" data-t="00:20:30">[00:20:30]</a>. These can be downloaded using the `mim` command or directly from the [[exploring_mmdetection_model_zoo | model zoo]] <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.
    ```python
    from mim import download
    download(config_path, dest_root='.') # Note: API might change from 'destination_dir' to 'dest_root'
    ```
    > [!NOTE] API Changes
    > The argument for the download destination has changed from `destination_dir` to `dest_root` in the `mim.download` function <a class="yt-timestamp" data-t="00:38:45">[00:38:45]</a>. This highlights a common challenge in maintaining [[open_source_ai_models_and_accessibility | open-source projects]] where documentation might lag behind code changes <a class="yt-timestamp" data-t="00:39:19">[00:39:19]</a>.

2.  **Initialize Detector**: Use the `initialize_detector` function from `mmdet.apis` to load the model <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>.
3.  **Perform Inference**: Use `inference_detector` to get detection results <a class="yt-timestamp" data-t="00:17:09">[00:17:09]</a>.
4.  **Visualize Results**: The `show_result_pyplot` function can visualize the detection results on an image <a class="yt-timestamp" data-t="00:47:20">[00:47:20]</a>.

### Example Code Snippet

```python
import os
from mmdet.apis import inference_detector, init_detector, show_result_pyplot

# Define model configuration and checkpoint paths
# Example using YOLOv3 MobileNetV2
config_file = 'mmdetection/configs/yolov3/yolov3_mobilenet_v2_320_coco.py'
checkpoint_file = 'yolov3_mobilenet_v2_320_coco_20210719_215349-d1703272.pth'

# Example using Faster R-CNN ResNet101 (larger model)
# config_file = 'mmdetection/configs/faster_rcnn/faster_rcnn_r101_fpn_1x_coco.py'
# checkpoint_file = 'faster_rcnn_r101_fpn_1x_coco_20200130-f7051d33.pth'

# Initialize the detector
# device='cuda:0' for GPU, device='cpu' for CPU
model = init_detector(config_file, checkpoint_file, device='cuda:0') <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>

# Prepare input images
image_paths = [
    '/tmp/AI_astronaut.png',
    '/tmp/AI_cowboy.png',
    '/tmp/people.png'
]

# Loop through images and perform inference
for img_path in image_paths:
    # Perform inference
    result = inference_detector(model, img_path) <a class="yt-timestamp" data-t="00:48:31">[00:48:31]</a>

    # Visualize the results and save to a file
    output_filename = f"result_{os.path.basename(img_path)}"
    model.show_result(img_path, result, out_file=output_filename) # Use model.show_result for saving to file
    print(f"Results saved to {output_filename}")
```

### Inference Performance

Testing with different models demonstrates varying performance:
*   **YOLOv3 MobileNetV2**: A smaller model that might produce lower confidence scores or miss some objects, especially in crowded scenes <a class="yt-timestamp" data-t="01:00:13">[01:00:13]</a>. For example, it identified a "person" and "horse" in an AI-generated image with decent confidence <a class="yt-timestamp" data-t="00:54:53">[00:54:53]</a>, but struggled with AI-generated textures, misclassifying objects as "dog," "bottle," or "teddy bear" <a class="yt-timestamp" data-t="00:36:56">[00:36:56]</a>.
*   **Faster R-CNN ResNet101**: A larger model that generally provides higher confidence scores and better detection capabilities, especially in dense environments <a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>. It detected significantly more people in a crowded stadium photo compared to the smaller model <a class="yt-timestamp" data-t="01:11:06">[01:11:06]</a> and also identified additional objects like cell phones <a class="yt-timestamp" data-t="01:11:33">[01:11:33]</a>.

> [!NOTE] AI-Generated Image Challenges
> AI-generated images with unusual textures can cause detection models to produce unexpected classifications (e.g., a "teddy bear" or "toothbrush" in an astronaut image) <a class="yt-timestamp" data-t="01:10:10">[01:10:10]</a>. Even applying super-resolution techniques (like "crispying" an image) may not improve detection accuracy, and can sometimes worsen it <a class="yt-timestamp" data-t="01:14:55">[01:14:55]</a>.

## [[exploring_mmdetection_model_zoo | Model Zoo]] and Benchmarks

MMDetection provides an extensive [[exploring_mmdetection_model_zoo | model zoo]] with various pre-trained models. These can be found at the OpenMMLab website under the "Benchmark and Model Zoo" section <a class="yt-timestamp" data-t="01:01:04">[01:01:04]</a>. The [[exploring_mmdetection_model_zoo | model zoo]] includes diverse architectures like YOLOv3 and Faster R-CNN with different backbones (e.g., MobileNetV2, ResNet101) <a class="yt-timestamp" data-t="00:58:12">[00:58:12]</a>. Users can download specific config and checkpoint files for their desired models <a class="yt-timestamp" data-t="01:06:18">[01:06:18]</a>.

## Project Health and Community

MMDetection appears to be a healthy [[open_source_ai_models_and_accessibility | open-source project]] with consistent maintenance and development:
*   **Contribution Graph**: Contributions have been steady since around 2018, showing continuous additions over time <a class="yt-timestamp" data-t="01:16:09">[01:16:09]</a>. While some initial major contributors might have moved on, new maintainers have taken over <a class="yt-timestamp" data-t="01:16:40">[01:16:40]</a>.
*   **Code Coverage**: The project maintains a 60% code coverage by tests, which is considered acceptable for an [[open_source_ai_models_and_accessibility | open-source project]] <a class="yt-timestamp" data-t="00:09:27">[00:09:27]</a>. Tests ensure that the software behaves properly and covers various edge cases <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
*   **Build Status**: The build status, though sometimes failing (indicated by a red badge), reflects continuous integration (CI) where packages are built upon code pushes <a class="yt-timestamp" data-t="00:08:39">[00:08:39]</a>.
*   **Releases**: MMDetection has a good amount of releases (45 total), with recent releases indicating active development, such as updates two and three weeks prior <a class="yt-timestamp" data-t="01:18:23">[01:18:23]</a>.
*   **Issue Resolution**: The project actively closes issues, demonstrating responsiveness to user questions and bug reports <a class="yt-timestamp" data-t="01:18:09">[01:18:09]</a>.

## Conclusion

MMDetection is a robust and actively maintained [[open_source_ai_models_and_accessibility | open-source object detection]] framework based on [[using_pytorch_for_object_detection | PyTorch]] <a class="yt-timestamp" data-t="01:18:56">[01:18:56]</a>. It offers a wide range of models in its [[exploring_mmdetection_model_zoo | model zoo]], supporting both large and small models that work with GPUs and CPUs <a class="yt-timestamp" data-t="01:19:05">[01:19:05]</a>. Its modular design and comprehensive features make it a valuable toolkit for various object detection projects <a class="yt-timestamp" data-t="01:19:11">[01:19:11]</a>.