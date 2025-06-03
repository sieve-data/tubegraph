---
title: Applications of MediaPipe in Machine Learning
videoId: dW4n9z9O0xc
---

From: [[shivaylamba]] <br/> 

[[introduction_to_mediapipe | MediaPipe]] is a solution developed by Google that offers various open-source and cross-platform machine learning solutions for live and streaming media <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Initially used internally at Google for many years, it was released to the public in 2019 <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. [[introduction_to_mediapipe | MediaPipe]] is powered by TensorFlow Lite and gained support for machine learning upon its public launch <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. It is widely used for running machine learning solutions on low-power devices <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>.

## Key Features of [[introduction_to_mediapipe | MediaPipe]]
[[introduction_to_mediapipe | MediaPipe]] provides "live ML anywhere" capabilities <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Its notable features include:
*   **Cross-platform Support**: Solutions can run on desktop, Android, iOS, and web (with JavaScript support) <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.
*   **Hardware Acceleration**: It supports ML inference and training on both CPU and GPU for faster model performance <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
*   **"Build Once, Deploy Anywhere"**: A single model can be deployed across various platforms, including IoT, web, desktop, iOS, and Android mobile solutions <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Free and Open Source**: The entire framework and its solutions are openly available on GitHub <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

## Popular Machine Learning Solutions
[[introduction_to_mediapipe | MediaPipe]] offers a range of pre-built ML solutions:
*   **Human Pose Detection and Tracking**: Tracks 33 different landmarks across the entire body, enabling applications like personal AI training buddies or physiotherapists <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>.
*   **Face Mesh**: Maps 468 landmarks on the face, allowing for various advanced facial applications <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.
*   **Hand Tracking**: Uses landmarks to track the entire hand <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.
*   **Holistic Model**: Combines pose, face, and hand tracking into a single solution <a class="yt-timestamp" data-t="00:02:28">[00:02:28]</a>.
*   **Hair [[understanding_segmentation_and_its_applications | Segmentation]]**: A specialized segmentation solution <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.
*   **Object Detection and Tracking**: Similar to TensorFlow.js's COCO-SSD model, it uniquely detects and tracks different types of objects <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Face Detection**: Detects human faces within an image or video <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.
*   **Iris Tracking**: Tracks the iris of the eye <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **3D Object Detection**: Essentially a detector based on a model <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation Solution]]
The [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation Solution]] is a recent addition to [[introduction_to_mediapipe | MediaPipe]]'s offerings, announced shortly before the recording <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

### Understanding [[understanding_segmentation_and_its_applications | Segmentation]]
[[understanding_segmentation_and_its_applications | Segmentation]] is a machine learning technique that identifies objects in the foreground, separating them from the background <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. It creates a "segmentation mask" around the tracked object, allowing for various effects like background changes or adding effects to the object itself <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>. The [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation Solution]] specifically segments prominent humans in a scene <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### Models and Technology
The [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation Solution]] utilizes two main models, both based on the popular MobileNetV3 model:
1.  **General Model**: Uses an input tensor of 256x256x3 <a class="yt-timestamp" data-t="00:07:54">[00:07:54]</a>.
2.  **Landscape Model**: Uses a smaller input tensor of 144x256x3, making it faster and lighter-weight <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.

These models process input images by resizing them to the required input dimensions <a class="yt-timestamp" data-t="00:08:42">[00:08:42]</a>.

### Application in Google Meet
A direct implementation of the [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation Solution]] is used in Google Meet, specifically a variant of the landscape model, to power background changing capabilities <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This functionality runs on the web using WebGL <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

### Machine Learning Pipeline
The internal workings of [[introduction_to_mediapipe | MediaPipe]] models, including the selfie segmentation, involve core concepts:
*   **Graphs**: Define the paths that "packets" (containing information about landmarks and tracking) follow through the model's nodes <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>.
*   **Calculators**: Define how calculations and transformations happen on these packets at each node <a class="yt-timestamp" data-t="00:11:04">[00:11:04]</a>.
*   **Packets**: Multi-dimensional arrays that carry algebraic values and information about the input <a class="yt-timestamp" data-t="00:07:25">[00:07:25]</a>.

## [[implementation_of_mediapipe_models | Implementation]] and APIs
[[introduction_to_mediapipe | MediaPipe]] solutions can be implemented using various APIs:
*   **Python API**: Requires installing `mediapipe` package via pip <a class="yt-timestamp" data-t="00:13:03">[00:13:03]</a>.
*   **JavaScript API**: Can be used via CDN or npm packages, often integrated with HTML canvas for webcam input and real-time effects <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>.
*   **C++ API**: Primarily used for desktop applications <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Android/iOS**: Specific instructions are provided for building and deploying examples on these mobile platforms <a class="yt-timestamp" data-t="00:14:33">[00:14:33]</a>.

## Web Demo of Selfie [[understanding_segmentation_and_its_applications | Segmentation]]
A web-based demo illustrates the [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation Solution]]'s functionality <a class="yt-timestamp" data-t="00:15:23">[00:15:23]</a>. The demo shows a user's body being segmented, with the background filled with a chosen color (e.g., blue, black, or white) <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. It also displays the segmentation mask as a green outline <a class="yt-timestamp" data-t="00:17:15">[00:17:15]</a>. Users can switch between the landscape and general models to observe performance differences <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. The JavaScript code in the demo manages the canvas, webcam input, model loading, and applying the desired background effects <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.