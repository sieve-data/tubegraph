---
title: Configuring object detection models
videoId: SWB2pTY3UDM
---

From: [[hu-po]] <br/> 

[[mmdetection_overview | MMDetection]] is an open-source [[object_detection_with_pytorch | object detection]] toolbox built on PyTorch, part of the OpenMMLab project, an open-source community focused on computer vision. <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>, <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a> It uses an Apache 2 permissive license. <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>

## Key Features

[[mmdetection_overview | MMDetection]] offers:
*   **Modular Design**: The detection framework is decomposed into different components, allowing users to easily construct custom [[object_detection_with_pytorch | object detection]] frameworks by combining various modules. <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>
*   **Framework Support**: It directly supports popular and contemporary [[object_detection_with_pytorch | detection frameworks]] such as Faster R-CNN, Mask R-CNN (used for segmentation), and RetinaNet. <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>, <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>
*   **GPU Acceleration**: Basic bounding box and mask operations run on GPUs, resulting in training speeds that are faster than or comparable to other detection codebases, including Detectron2. <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>, <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>
*   **State-of-the-Art Performance**: The toolbox originated from the mmdet team, who won the COCO detection challenge in 2018. <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a> A newer version, RTMDet, achieves state-of-the-art performance in instance segmentation and rotated [[object_detection_with_pytorch | object detection]] tasks. <a class="yt-timestamp" data-t="00:09:40">[00:09:40]</a>, <a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a>

## Installation and Setup

### Basic Installation
1.  **Create a Virtual Environment**: Use `pipenv` or `pyenv` (e.g., `pyenv virtualenv mmdet`). <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>
2.  **Install `openmim`**: `pip install openmim`. <a class="yt-timestamp" data-t="00:30:23">[00:30:23]</a>
3.  **Install `mmcv-full`**: `mim install mmcv-full` ensures comprehensive features including CPU and CUDA operations. <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>, <a class="yt-timestamp" data-t="00:30:38">[00:30:38]</a>
    *   Note: The `mmcv-full` package may be renamed to `mmcv`. <a class="yt-timestamp" data-t="00:26:57">[00:26:57]</a>
4.  **Install PyTorch**: Install a PyTorch version compatible with your CUDA version (e.g., for CUDA 11.6, install PyTorch 1.5+). <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>, <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>
5.  **Install `mmdet`**:
    *   **From Pip**: `pip install mmdet`. <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a> This initial installation does not include PyTorch or CUDA. <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>
    *   **From Source (recommended for full functionality)**:
        1.  Clone the [[mmdetection_overview | MMDetection]] GitHub repository: `git clone https://github.com/open-mmlab/mmdetection.git`. <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>
        2.  Navigate into the cloned directory: `cd mmdetection`. <a class="yt-timestamp" data-t="00:23:35">[00:23:35]</a>
        3.  Install in editable mode: `pip install -v -e .`. <a class="yt-timestamp" data-t="00:23:45">[00:23:45]</a>
            *   This step may require `ninja` for compilation: `pip install ninja`. <a class="yt-timestamp" data-t="00:33:26">[00:33:26]</a>

### Dependency Troubleshooting
*   **`distutils` compatibility issue**: If you encounter `setup.py` errors related to `distutils`, downgrade `setuptools` to an older version (e.g., `pip install setuptools==65.5.0`). <a class="yt-timestamp" data-t="00:34:37">[00:34:37]</a>

## Model Configuration and Inference

[[model_training_and_evaluation_methods | Model training and evaluation methods]] in [[mmdetection_overview | MMDetection]] involve using pre-trained models and configuration files.

### Verifying Installation and Running Inference

To verify the installation and run an inference demo:
1.  **Download Model Checkpoints and Configs**: Use the `mim` command-line tool.
    *   `mim download mmdet --config yolov3_mobilenet_v2_320_coco --dest-root .` <a class="yt-timestamp" data-t="00:24:28">[00:24:28]</a>
        *   *Note*: The argument `dest-root` was previously `destination_dur` and was updated in the documentation. <a class="yt-timestamp" data-t="00:38:24">[00:38:24]</a>, <a class="yt-timestamp" data-t="00:41:42">[00:41:42]</a>
2.  **Run Inference**:
    ```python
    from mmdet.apis import init_detector, inference_detector, show_result_pyplot
    import os

    # Load configuration and checkpoint files
    config_file = 'yolov3_mobilenet_v2_320_coco.py'
    checkpoint_file = 'yolov3_mobilenet_v2_320_coco_20210719_215306-bd5e1b29.pth' # Example checkpoint

    # Build the detector
    model = init_detector(config_file, checkpoint_file, device='cuda:0') # Or 'cpu' for CPU inference

    # List of images to test
    image_paths = [
        '/tmp/AI_astronaut.png',
        '/tmp/AI_cowboy.png',
        '/tmp/people.png'
    ]

    for img_path in image_paths:
        # Perform inference
        result = inference_detector(model, img_path)

        # Visualize the results
        output_filename = os.path.join('/tmp', os.path.basename(img_path).replace('.', '_result.'))
        show_result_pyplot(model, img_path, result, score_thr=0.3, out_file=output_filename)
        print(f"Results saved to: {output_filename}")
    ```
    *   `init_detector` initializes the model using the config and checkpoint files. <a class="yt-timestamp" data-t="01:09:04">[01:09:04]</a>, <a class="yt-timestamp" data-t="01:09:06">[01:09:06]</a>
    *   `inference_detector` performs the [[object_detection_with_pytorch | object detection]] on the given image. <a class="yt-timestamp" data-t="01:17:15">[01:17:15]</a>
    *   `show_result_pyplot` visualizes the detection results on an image, optionally saving the output to a file. <a class="yt-timestamp" data-t="01:17:17">[01:17:17]</a>

### Model Zoo and Performance

[[mmdetection_overview | MMDetection]] provides a comprehensive [[multimodal_model_benchmarks | model zoo]] with various pre-trained models. <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>

*   **Model Comparison**:
    *   **YOLOv3 MobileNet v2**: A smaller model that might struggle with complex or "weird texture" AI-generated images, showing low confidence or incorrect detections (e.g., detecting a "dog" or "bottle" in an astronaut image). <a class="yt-timestamp" data-t="00:36:54">[00:36:54]</a>, <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>
    *   **Faster R-CNN ResNet-101**: A larger model that generally provides higher confidence scores and detects more objects, especially in crowded scenes. For example, it can detect many individuals in a crowd and even smaller objects like cell phones. <a class="yt-timestamp" data-t="01:06:13">[01:06:13]</a>, <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a>, <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>, <a class="yt-timestamp" data-t="01:11:13">[01:11:13]</a>
        *   However, even larger models can misinterpret AI-generated images, sometimes identifying objects like "teddy bears" or "toothbrushes" in a rendered astronaut scene, indicating potential issues with specific textures or generalization to non-photorealistic images. <a class="yt-timestamp" data-t="01:09:48">[01:09:48]</a>, <a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>

### Open Source Project Health

The [[mmdetection_overview | MMDetection]] repository demonstrates characteristics of a healthy open-source project:
*   **Consistent Contributions**: Regular contributions since roughly 2018, indicating steady development. <a class="yt-timestamp" data-t="01:15:52">[01:15:52]</a>
*   **Active Maintenance**: A transition of maintainers over time, with new contributors taking over from initial authors. <a class="yt-timestamp" data-t="01:16:36">[01:16:36]</a>
*   **Resolved Issues**: A good number of closed issues signifies active engagement with community questions and bug fixes. <a class="yt-timestamp" data-t="01:18:06">[01:18:06]</a>
*   **Frequent Releases**: Over 45 total releases, with recent updates occurring every few weeks, indicating ongoing development and improvements. <a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a>, <a class="yt-timestamp" data-t="01:18:37">[01:18:37]</a>

[[mmdetection_overview | MMDetection]] provides a robust and versatile toolkit for [[object_detection_with_pytorch | object detection]] tasks, supporting various models and offering good performance for both CPU and GPU inference. <a class="yt-timestamp" data-t="01:18:56">[01:18:56]</a>, <a class="yt-timestamp" data-t="01:19:03">[01:19:03]</a>