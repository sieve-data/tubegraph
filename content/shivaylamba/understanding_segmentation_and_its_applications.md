---
title: Understanding Segmentation and its Applications
videoId: dW4n9z9O0xc
---

From: [[shivaylamba]] <br/> 

Segmentation is a machine learning technique that identifies objects in the foreground of an image or video, distinguishing them from the background <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. It achieves this by creating a "segmentation mask" around the tracked object, making it possible to perform various effects or transformations on either the foreground or background <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. This unique identification allows for actions like changing backgrounds or adding effects to the segmented object <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>.

## MediaPipe's Role in Segmentation

[[Introduction to MediaPipe | MediaPipe]] is a solution developed by Google, used internally for a long time before being released to the public in 2019 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It powers many Google services, including YouTube streaming <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Since 2019, [[Introduction to MediaPipe | MediaPipe]] has supported machine learning, enabling it to run various machine learning solutions on low-power devices <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. It provides open-source, cross-platform machine learning solutions for live and streaming media <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. [[Introduction to MediaPipe | MediaPipe]] supports desktop, Android, iOS, and web platforms with JavaScript <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

Key features of [[Introduction to MediaPipe | MediaPipe]] include <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>:
*   ML inference and training on hardware (CPU, GPU) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   "Build once, deploy anywhere" capability across IoT, web, desktop, iOS, and Android <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   It is free and open-source <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Other [[Applications of MediaPipe in Machine Learning | MediaPipe ML Solutions]]

Beyond selfie segmentation, [[Introduction to MediaPipe | MediaPipe]] offers several popular machine learning solutions <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>:
*   **Human Pose Detection and Tracking** Identifies 33 landmarks across the entire body, useful for AI training buddies or physiotherapists <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Face Mesh** Tracks 468 landmarks on the face <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Hand Tracking** Uses landmarks to track the entire hand <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Holistic Model** Combines pose, face, and hand tracking <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **Hair Segmentation** <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
*   **Object Detection and Tracking** Similar to TensorFlow.js's COCO SSD model <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Face Detection** <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
*   **Iris Tracking** <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
*   **3D Object Detection** Based on the DetectorOn model <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## MediaPipe Selfie Segmentation Solution

The [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation solution]] focuses on segmenting prominent humans in a scene <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. This allows for various applications like adding selfie effects or changing backgrounds in video conferencing <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>.

### Technical Details of the Model

The [[mediapipe_selfie_segmentation_solution | Selfie Segmentation solution]] utilizes two main models <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>:
1.  **General Model**
2.  **Landscape Model**

Both models are based on the popular **MobileNet V3 model**, which is widely used in machine learning for object tracking and detection in Python and JavaScript <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>. The primary difference between the General and Landscape models is their input tensor size <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>.

*   **General Model Input**: 256x256x3 tensor <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Landscape Model Input**: 144x256x3 tensor <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

The Landscape model has a smaller input size, making it faster and lighter-weight compared to the General model <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>. The output for both is a segmentation mask (256x256x1 tensor for the General model) <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>. The input image is automatically resized to fit the model's required input dimensions <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Applications of Selfie Segmentation

A significant application of the [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation solution]] is in **Google Meet**, where a variant of the Landscape model powers its background changing capabilities <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This functionality runs on the web using WebGL <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

### MediaPipe's Internal Workflow (Pipeline Concepts)

Understanding how [[Introduction to MediaPipe | MediaPipe]] works internally involves concepts like graphs, calculators, and packets <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>:
*   **Packets**: Contain information about landmarks and tracking, flowing between nodes <a class="yt=" data-t="00:10:35">[00:10:35]</a>.
*   **Graphs**: Define the paths that these packets follow from one node to another within the machine learning model <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Graph definitions are typically found in `.pbtxt` files <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>.
*   **Calculators**: Configurations within nodes that define how packets function and how calculations and transformations occur on them <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

The entire source code, including graph and sub-graph definitions, is open-sourced by the [[Introduction to MediaPipe | MediaPipe]] team <a class="yt-timestamp" data-t="00:12:13">[00:12:13]</a>.

### API and Demo Applications

[[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation]] provides APIs for various platforms:
*   **Python API**: Users can install necessary [[Introduction to MediaPipe | MediaPipe]] Python packages (`pip install mediapipe`) and utilize functions for drawing selfie segmentation, processing webcam input, and feeding it into the ML model <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **JavaScript API**: Available via CDN or npm packages, it allows for webcam input processing, dimension changes, and rendering the output on an HTML canvas <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.

A web-based demo illustrates the [[mediapipe_selfie_segmentation_solution | selfie segmentation]] by changing the background color of the segmented human figure <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. The demo allows switching between the lighter Landscape model and the General model <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. It also demonstrates the segmentation mask itself, showing the green overlay on the identified human body parts <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. The demo's JavaScript code manipulates the canvas fill style to change the background color based on the segmentation mask <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.