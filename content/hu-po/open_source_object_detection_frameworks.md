---
title: Open source object detection frameworks
videoId: SWB2pTY3UDM
---

From: [[hu-po]] <br/> 

[[MMDetection overview | MMDetection]] is presented as a prime example of an [[opensource_ai_models | open source]] object detection toolbox <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. These frameworks provide readily available tools and models for developers to implement computer vision tasks.

## MMDetection Features and Capabilities

[[MMDetection overview | MMDetection]] is an [[opensource_ai_models | open source]] object detection toolbox built on [[machine_learning_frameworks_pytorch_vs_tensorflow | PyTorch]] <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. It is a part of the OpenMMLab project, an [[opensource_ai_models | open source]] community that contributes to object detection <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a><a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

Key features include:
*   **License**: [[Opensource AI model availability and usage rights | MMDetection]] is released under the Apache 2 license, a permissive variant similar to MIT <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a><a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>.
*   **Modularity**: The framework decomposes the detection process into different components, allowing users to easily construct custom object detection frameworks by combining various modules <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a><a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   **Framework Support**: It directly supports popular and contemporary detection frameworks such as Faster R-CNN, Mask R-CNN (used for segmentation), and RetinaNet <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a><a class="yt-timestamp" data-t="00:07:29">[00:07:29]</a>.
*   **Performance**:
    *   Basic bounding box and mask operations run on GPUs <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.
    *   Training speed is faster than or comparable to other detection codebases, including Detectron2 <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   The [[MMDetection overview | MMDetection]] team won the [[benchmarking_vision_models_with_imagenet_and_coco | COCO detection challenge]] in 2018 <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a><a class="yt-timestamp" data-t="00:08:03">[00:08:03]</a>.
    *   Its RTMDet models have achieved state-of-the-art performance in various tasks, including object detection in aerial images and real-time segmentation for MS Coco <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a><a class="yt-timestamp" data-t="00:09:50">[00:09:50]</a><a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.

### Installation and Usage
MMDetection can be installed via `pip` <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. Installing the core `mmdet` package does not automatically install [[machine_learning_frameworks_pytorch_vs_tensorflow | PyTorch]] or CUDA <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a><a class="yt-timestamp" data-t="00:05:02">[00:05:02]</a>. Users need to install `mmcv-full` with specific CUDA and [[machine_learning_frameworks_pytorch_vs_tensorflow | PyTorch]] versions to leverage GPU capabilities <a class="yt-timestamp" data-t="00:05:13">[00:05:13]</a><a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>.

A common issue encountered during installation is a compatibility problem with newer versions of `setuptools` <a class="yt-timestamp" data-t="00:34:32">[00:34:32]</a><a class="yt-timestamp" data-t="00:34:52">[00:34:52]</a>. Downgrading `setuptools` to an older version can resolve this <a class="yt-timestamp" data-t="00:35:27">[00:35:27]</a><a class="yt-timestamp" data-t="00:35:30">[00:35:30]</a>.

### Model Zoo and Performance
[[MMDetection overview | MMDetection]] includes a "model zoo" with various pre-trained models <a class="yt-timestamp" data-t="00:56:04">[00:56:04]</a><a class="yt-timestamp" data-t="00:56:22">[00:56:22]</a>. Examples include YOLO MobileNet V2 and ResNet 101 <a class="yt-timestamp" data-t="00:58:09">[00:58:09]</a><a class="yt-timestamp" data-t="00:58:34">[00:58:34]</a>.

Testing with different models shows performance variations:
*   A smaller model like YOLO MobileNet V2 might detect objects with lower confidence or miss some in crowded scenes <a class="yt-timestamp" data-t="00:36:50">[00:36:50]</a><a class="yt-timestamp" data-t="01:10:00">[01:10:00]</a>.
*   A larger model, such as ResNet 101, generally provides higher confidence scores and can detect more objects, including additional details like cell phones in a crowd <a class="yt-timestamp" data-t="01:10:34">[01:10:34]</a><a class="yt-timestamp" data-t="01:10:58">[01:10:58]</a><a class="yt-timestamp" data-t="01:11:11">[01:11:11]</a><a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>.
*   The texture of an image, particularly [[opensource_ai_models | AI generated art]], can impact model detection accuracy, sometimes leading to misclassifications (e.g., perceiving a teddy bear or toothbrush in an astronaut image) <a class="yt-timestamp" data-t="01:07:02">[01:07:02]</a><a class="yt-timestamp" data-t="01:09:48">[01:09:48]</a><a class="yt-timestamp" data-t="01:10:07">[01:10:07]</a>. Image processing techniques like "super resolution" can sometimes negatively affect detection if they alter textures in unexpected ways <a class="yt-timestamp" data-t="01:14:49">[01:14:49]</a><a class="yt-timestamp" data-t="01:14:55">[01:14:55]</a>.

## [[Challenges in open source AI development | Challenges in Open Source AI Development]]

While [[opensource_ai_models | open source]] projects offer many benefits, they also present [[challenges_in_open_source_ai_development | challenges]]:
*   **Maintainability**: Ensuring consistent updates and addressing issues can be difficult <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a><a class="yt-timestamp" data-t="00:08:14">[00:08:14]</a>.
*   **Continuous Integration/Deployment (CI/CD)**: A failing build status (e.g., "build is failing") indicates issues with automated pipelines that compile and test the code when new changes are pushed <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a><a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a><a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
*   **Code Coverage**: This metric indicates the percentage of the codebase covered by tests <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a><a class="yt-timestamp" data-t="00:08:47">[00:08:47]</a>. While a high percentage (e.g., 100%) doesn't guarantee good code quality, a reasonable coverage (e.g., 60% for an [[opensource_ai_models | open source]] project) helps ensure software behaves properly and edge cases are considered <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a><a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a><a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>.
*   **Documentation Updates**: APIs and functions can change, leading to outdated documentation, as seen with the `mim download` function's `dest_dur` parameter being renamed to `dest_root` <a class="yt-timestamp" data-t="00:26:33">[00:26:33]</a><a class="yt-timestamp" data-t="00:26:36">[00:26:36]</a><a class="yt-timestamp" data-t="00:38:26">[00:38:26]</a><a class="yt-timestamp" data-t="00:38:42">[00:38:42]</a><a class="yt-timestamp" data-t="00:38:45">[00:38:45]</a>. Contributing to documentation fixes is a way to engage with [[opensource_ai_models | open source]] projects <a class="yt-timestamp" data-t="00:39:19">[00:39:19]</a>.

Despite these [[challenges_in_open_source_ai_development | challenges]], projects like [[MMDetection overview | MMDetection]] exhibit healthy development with consistent contributions and frequent releases <a class="yt-timestamp" data-t="01:16:05">[01:16:05]</a><a class="yt-timestamp" data-t="01:18:18">[01:18:18]</a><a class="yt-timestamp" data-t="01:18:39">[01:18:39]</a>.