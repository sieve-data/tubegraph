---
title: MediaPipe Selfie Segmentation Solution
videoId: dW4n9z9O0xc
---

From: [[shivaylamba]] <br/> 

The MediaPipe Selfie Segmentation Solution was recently announced by the MediaPipe team at Google <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. This solution utilizes machine learning to identify and separate human subjects from their backgrounds in real-time, enabling various selfie effects and video conferencing capabilities <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

## [[introduction_to_mediapipe | Introduction to MediaPipe]]

[[introduction_to_mediapipe | MediaPipe]] is a solution developed by Google, initially used internally for a long time before its public release in 2019 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It powers many Google services, including YouTube streaming <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>. [[introduction_to_mediapipe | MediaPipe]] integrates with TensorFlow Lite <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a> and gained support for machine learning upon its public launch <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.

[[introduction_to_mediapipe | MediaPipe]] is highly popular for running diverse [[applications_of_mediapipe_in_machine_learning | machine learning solutions]] on low-power devices, providing "live ML anywhere" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. It offers open-source, cross-platform [[applications_of_mediapipe_in_machine_learning | machine learning solutions]] for live and streaming media, including video-based and audio-visual applications <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. It supports desktop, Android, iOS, and web platforms with JavaScript support <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### Key Features of [[introduction_to_mediapipe | MediaPipe]]
*   **Hardware Acceleration:** Enables ML inference and training on both CPU and GPU <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Build Once, Deploy Anywhere:** Solutions built with [[introduction_to_mediapipe | MediaPipe]] can be deployed across various platforms, including IoT, web, desktop, iOS, and Android <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Free and Open Source:** The entire framework and its solutions are freely available on GitHub <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

### Popular ML Solutions Provided by [[introduction_to_mediapipe | MediaPipe]]
[[applications_of_mediapipe_in_machine_learning | MediaPipe]] offers several popular machine learning solutions:
*   **Human Pose Detection and Tracking:** Tracks 33 landmarks across the entire body, enabling applications like AI training buddies or virtual physiotherapists <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. It is similar to TensorFlow.js's PoseNet model <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
*   **Face Mesh:** Maps 468 landmarks on the face, allowing for a wide range of facial recognition and effect applications <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Hand Tracking:** Uses landmarks to track the entire hand <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Holistic Model:** Combines pose, face, and hand tracking for comprehensive human analysis <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **Hair Segmentation** <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
*   **Object Detection and Tracking:** Similar to TensorFlow.js's COCO SSD model, it uniquely detects different types of objects <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Face Detection** <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
*   **Iris Tracking** <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
*   **3D Object Detection:** Based on the DetectorOn model <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

## [[understanding_segmentation_and_its_applications | Understanding Segmentation]]

[[understanding_segmentation_and_its_applications | Segmentation]] is a machine learning technique that identifies objects in the foreground of an image and separates them from the background <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. It achieves this by creating a "segmentation mask" around the tracked object, which can then be used to apply various effects, such as changing the background or adding specific visual modifications to the foreground object <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

The MediaPipe Selfie Segmentation Solution specifically segments prominent humans within a scene <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. Similar to existing TensorFlow models, it can segment multiple human beings in real-time, enabling applications like selfie effects or background changes in video conferencing tools <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.

## [[implementation_of_mediapipe_models | Implementation of MediaPipe Models]] for Selfie Segmentation

The MediaPipe Selfie Segmentation Solution utilizes two main models: the **General Model** and the **Landscape Model** <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. Both are based on the popular **MobileNet V3** model, commonly used for object tracking and detection in machine learning frameworks like TensorFlow.js <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

The primary difference between the General and Landscape models lies in their input tensor sizes <a class="yt-timestamp" data-t="00:07:19">[00:07:19]</a>:
*   **General Model:** Takes an input tensor of 256x256x3 (height, width, RGB channels) and outputs a 256x256x1 segmentation mask <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
*   **Landscape Model:** Uses a smaller input tensor of 144x256x3 <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>. This smaller input size makes the Landscape Model faster and lighter-weight, making it suitable for devices with varying capabilities <a class="yt-timestamp" data-t="00:08:19">[00:08:19]</a>.

The input image automatically resizes to match the required input tensor dimensions before being fed into the machine learning model <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.

### Real-world [[applications_of_mediapipe_in_machine_learning | Applications]]
A variant of the Landscape Model is used to power **Google Meet**, specifically enabling its background changing capabilities <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>. This is implemented on the web using WebGL <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. The General Model powers **ML Kit** <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Machine Learning Pipeline (Graphs, Calculators, Packets)
The underlying architecture of [[introduction_to_mediapipe | MediaPipe]] solutions involves **graphs**, **calculators**, and **packets** <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Packets:** Contain information, such as landmarks and tracking data <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>.
*   **Graphs:** Define the paths that packets follow through the machine learning model, from input to various processing stages <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. Graphs are typically defined in `.pbtxt` files <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
*   **Calculators:** These are nodes within the graph that define how packets function and how calculations and transformations occur <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.

### Solution APIs
[[implementation_of_mediapipe_models | MediaPipe]] provides APIs for [[implementation_of_mediapipe_models | implementing]] the selfie segmentation solution in various languages:
*   **Python API:** Can be used by installing the necessary `mediapipe` Python package via `pip install mediapipe` <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>. It integrates with libraries like OpenCV for webcam input processing <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   **JavaScript API:** Available via CDN or npm packages, allowing for web-based [[implementation_of_mediapipe_models | implementations]] using HTML canvas and webcam input <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. The JavaScript API allows for dynamic manipulation of canvas elements to change background styles or apply masking effects based on the segmentation output <a class="yt-timestamp" data-t="00:19:48">[00:19:48]</a>. Asynchronous functions are used to ensure the model is fully loaded before processing input <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.

## Web Demo Example
A web demo provided by the [[introduction_to_mediapipe | MediaPipe]] team showcases the selfie segmentation in action <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. In this demo, the human subject is segmented, and the background is filled with a solid color, such as blue <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. The demo allows users to switch between the lighter Landscape Model (default) and the General Model to observe performance differences <a class="yt-timestamp" data-t="00:16:43">[00:16:43]</a>. It also demonstrates the raw segmentation mask as a green outline around the detected human form, including hands and face <a class="yt-timestamp" data-t="00:17:13">[00:17:13]</a>. The demo code, written in JavaScript, illustrates how to change the background fill style (e.g., to black or white) by modifying the canvas properties based on the segmentation output <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.