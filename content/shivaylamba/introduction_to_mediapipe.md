---
title: Introduction to MediaPipe
videoId: dW4n9z9O0xc
---

From: [[shivaylamba]] <br/> 

MediaPipe is a solution developed and used extensively at Google for a long time before its public release in 2019 <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. It was previously a "black box" to the general public <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a> but has been used internally at Google to power various services, including YouTube streaming <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

Since its public launch in 2019, MediaPipe gained support for [[Applications of MediaPipe in Machine Learning | machine learning]] and is now powered by TensorFlow Lite <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. It has become popular for running [[Applications of MediaPipe in Machine Learning | machine learning solutions]] on low-power devices <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>, essentially providing "live ML anywhere" <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

## Core Purpose and Features
MediaPipe offers open-source, cross-platform [[Applications of MediaPipe in Machine Learning | machine learning solutions]] for live and streaming media <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>. It supports various platforms including desktop, Android, iOS, and web (with JavaScript support) <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>.

Key features include:
*   **Hardware Acceleration** It provides ML inference and training on hardware, utilizing both CPU and GPU for faster model processing <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **"Build Once, Deploy Anywhere"** A single model can be built and then deployed across various platforms such as IoT, web, desktop, iOS, and Android <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Free and Open Source** All solutions are freely available and open source <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. The official repository is on GitHub <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

## Popular Machine Learning Solutions
MediaPipe provides a range of popular ML solutions <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>, including:
*   **Human Pose Detection and Tracking** Tracks 33 landmarks across the entire body, enabling applications like AI training buddies or physiotherapists <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Face Mesh** Tracks almost 468 landmarks on the face for various applications <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Hand Tracking** Uses landmarks to track the entire hand <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Holistic Model** Combines pose, face, and hand tracking <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   **Hair [[Understanding Segmentation and its Applications | Segmentation]]** <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>
*   **Object Detection and Tracking** Similar to TensorFlow.js's COCO SSD model, it uniquely detects different types of objects <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Face Detection** <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>
*   **Iris Tracking** <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>
*   **3D Object Detection** Based on the Detectoron model <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **[[MediaPipe Selfie Segmentation Solution | Selfie Segmentation Solution]]** One of the latest solutions, enabling the segmentation of prominent humans in a scene for selfie effects or background changes in video conferencing applications like Google Meet <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>, <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.

## MediaPipe Framework Concepts
To understand how MediaPipe works internally, it's essential to grasp its framework concepts <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>. These include:
*   **Graphs** Define the paths that "packets" (containing information about landmarks and tracking) follow between "nodes" within the machine learning model <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>. Graphs are typically defined in `.pbtxt` text files <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
*   **Calculators** These are configurations within the "nodes" that define how packets function and how calculations and transformations happen on them <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   **Packets** Contain information about landmarks and tracking, and they flow through the graph <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.

## [[Implementation of MediaPipe Models | Model Implementation]]
MediaPipe models like the [[MediaPipe Selfie Segmentation Solution | selfie segmentation solution]] use models based on MobileNetV3, a popular machine learning model for tasks like object tracking and detection <a class="yt-timestamp" data-t="00:06:57">[00:06:57]</a>.

The input for these models are tensors, which are multi-dimensional arrays containing numerical values representing input information like an image <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>. The output is typically a segmentation mask, also represented as a tensor <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

MediaPipe provides solutions APIs for various languages, including Python and JavaScript <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>, <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>. For web-based applications, models are loaded and run using WebGL <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>. Example applications and instructions are available for Android, iOS, and desktop platforms <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>.