---
title: Implementation of MediaPipe Models
videoId: dW4n9z9O0xc
---

From: [[shivaylamba]] <br/> 

[[introduction_to_mediapipe | MediaPipe]] is an open-source, cross-platform framework developed by Google that provides pre-built machine learning (ML) solutions for live and streaming media [00:01:23]. Initially used internally at Google for various services, including YouTube streaming, it was made public in 2019 [00:00:30]. [[introduction_to_mediapipe | MediaPipe]] is powered by TensorFlow Lite and gained support for [[applications_of_mediapipe_in_machine_learning | machine learning]] in 2019 [00:00:54]. It is highly popular for running diverse [[applications_of_mediapipe_in_machine_learning | machine learning]] solutions on low-power devices, offering "live ML anywhere" [00:01:14].

## Key Features and Capabilities
[[introduction_to_mediapipe | MediaPipe]] offers several features that facilitate the implementation of its models:
*   **Live ML Anywhere** It provides open-source, cross-platform [[applications_of_mediapipe_in_machine_learning | machine learning]] solutions for live and streaming media, including video and audio-visual applications [00:01:19].
*   **Cross-Platform Support** Solutions can run on desktop, Android, iOS, and web platforms (with JavaScript support) [00:01:34].
*   **Hardware Acceleration** It supports ML inference and training on both CPU and GPU for faster model performance [00:03:21].
*   **"Build Once, Deploy Anywhere"** A single model can be built and deployed across various platforms, including IoT, web, desktop, iOS, and Android mobile devices [00:03:32].
*   **Free and Open Source** All solutions are freely available and open-source, with code hosted on GitHub [00:03:44].

## Popular MediaPipe ML Solutions
[[introduction_to_mediapipe | MediaPipe]] provides a range of pre-built [[applications_of_mediapipe_in_machine_learning | machine learning]] solutions:
*   **Human Pose Detection and Tracking** This solution tracks 33 landmarks across the entire human body, enabling applications like AI training buddies or virtual physiotherapists [00:01:50]. It is similar to TensorFlow.js's PoseNet model [00:02:10].
*   **Face Mesh** Tracks almost 468 landmarks on the face, allowing for various face-related applications [00:02:14].
*   **Hand Tracking** Uses landmarks to track the entire hand [00:02:25].
*   **Holistic Model** Combines pose, face, and hand tracking for a comprehensive solution [00:02:28].
*   **Other Solutions** Include hair segmentation, object detection and tracking (similar to TensorFlow.js's COCO SSD model), face detection, iris tracking, and 3D object detection (similar to the DetectorOn model) [00:02:39].

## Internal Workings: Framework Concepts
To understand how [[introduction_to_mediapipe | MediaPipe]] models are implemented, it is essential to grasp its core framework concepts [00:04:25]:
*   **Graphs** These define the paths that "packets" of information follow within the ML model [00:11:10]. Graphs are typically defined in `.pbtxt` files [00:11:28].
*   **Calculators** These are nodes within a graph that define how packets function and how computations are performed on them [00:11:04]. They describe transformations and calculations [00:11:07].
*   **Packets** These are data structures that contain information, such as landmarks and tracking data [00:10:34]. Packets flow between different calculators (nodes) within a graph [00:10:39].

The graph definition specifies the node structure, the calculator used, input and output streams, and whether the operations are CPU or GPU-based [00:11:37]. Subgraphs can perform specific actions like selfie segmentation or color adjustments [00:11:55].

## [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation Solution]]
The [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation Solution]] is a recent addition to the [[introduction_to_mediapipe | MediaPipe]] suite [00:04:46]. Segmentation is an [[applications_of_mediapipe_in_machine_learning | machine learning]] technique that identifies foreground objects and separates them from the background by creating a "segmentation mask" [00:05:08]. This allows for various effects, such as changing backgrounds or adding visual enhancements [00:05:48].

The [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation Solution]] specifically segments prominent humans in a scene [00:06:02]. It can uniquely identify multiple human beings in real-time, similar to other popular TensorFlow segmentation models [00:06:10]. This capability is useful for applications like selfie effects or background changes in video conferencing [00:06:30].

### Underlying Models
The [[mediapipe_selfie_segmentation_solution | MediaPipe Selfie Segmentation Solution]] uses two main models, both based on the popular MobileNet V3 model [00:06:51]:
*   **General Model**
    *   Input Tensor Size: 256x256x3 [00:07:54].
    *   Output Tensor Size: 256x256x1 (segmentation mask) [00:08:02].
    *   Powers the ML Kit [00:09:01].
*   **Landscape Model**
    *   Input Tensor Size: 144x256x3 [00:08:10].
    *   Has a smaller input size, making it faster and lighter-weight [00:08:19].
    *   A variant powers Google Meet's background changing feature [00:09:04]. This functionality on the web is run using WebGL [00:09:36].

Users can choose between the General and Landscape models based on device capabilities [00:08:28]. Input images are automatically resized to fit the model's required input dimensions before being fed into the [[applications_of_mediapipe_in_machine_learning | machine learning]] model [00:08:42].

### Solution API Configuration
The [[mediapipe_selfie_segmentation_solution | Selfie Segmentation Solution]] API allows for configuration via:
*   **Model Selection** Choosing between the General model (0) or the Landscape model (1) [00:12:25].
*   **Output** The output is a segmentation mask of the same dimensions as the input image [00:12:40].

### API Usage Examples

#### Python Implementation
To use the [[mediapipe_selfie_segmentation_solution | Selfie Segmentation Solution]] in Python, the `mediapipe` package must be installed (`pip install mediapipe`) [00:13:09].
```python
import mediapipe as mp
import cv2

# Initialize the Selfie Segmentation solution
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=1) # 1 for landscape model

# Capture webcam input
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Convert the BGR image to RGB.
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and get the segmentation mask.
    results = selfie_segmentation.process(image_rgb)
    segmentation_mask = results.segmentation_mask

    # Example: Apply a blue background to segmented area (demo similar)
    bg_image = image.copy()
    # Apply a blue background
    bg_image[:] = (255, 0, 0) # Blue color

    # Create a 3-channel mask for alpha blending
    condition = segmentation_mask > 0.1 # Threshold for segmentation
    fg_image = cv2.bitwise_and(image, image, mask=condition.astype(int))
    bg_image = cv2.bitwise_and(bg_image, bg_image, mask=(~condition).astype(int))

    output_image = cv2.add(fg_image, bg_image)

    cv2.imshow('MediaPipe Selfie Segmentation', output_image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
```
The webcam input is transformed into the desired tensor value and fed into the [[applications_of_mediapipe_in_machine_learning | machine learning]] model [00:13:30].

#### JavaScript Implementation (Web Demo)
For web-based applications, [[mediapipe_selfie_segmentation_solution | MediaPipe]] can be integrated via CDN or npm packages [00:13:54]. The demo showcases using HTML Canvas to take webcam input, transform its dimensions, use the [[applications_of_mediapipe_in_machine_learning | machine learning]] model for inference, and then display the results on the canvas [00:14:06].

In the web demo, the JavaScript code controls the visual effects:
*   `canvas.globalCompositeOperation = 'source-over';` and `canvas.fillStyle = '#0000FF';` (blue) fill the background for the segmentation effect [00:18:40].
*   Changing `canvas.fillStyle` to `white` (`#FFFFFF`) results in a white background [00:19:30].
*   The `async` function waits for the model to load before executing [00:20:04].

The demo also allows users to select between the Landscape (lighter) and General models, observing real-time performance impacts like frame drops [00:16:41]. When showing the segmentation mask directly, a green overlay highlights the detected human body, including hands and face [00:17:15].

## Example Applications
[[mediapipe_selfie_segmentation_solution | MediaPipe]] provides example applications and build instructions for Android, iOS, and desktop platforms [00:14:26]. These examples demonstrate how to run graphs on CPU or GPU [00:14:42]. The source code, including graph definitions and subgraphs, is open-sourced [00:12:11].