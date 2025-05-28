---
title: Comparison of Synthetic and Real Depth Data
videoId: WoiI_Pn9yHw
---

From: [[hu-po]] <br/> 

Depth data, crucial for [[Applications and Limitations of Monocular Depth | monocular depth estimation]] and 3D scene understanding, can be obtained from real-world sensors or generated synthetically. Each method presents distinct advantages and disadvantages, particularly when used for training AI models.

## Real-World Depth Data

Real-world depth data is captured using physical sensors, which measure the distance of objects from the camera.
*   **Capture Methods**
    *   **LiDAR Sensors** These devices emit laser pulses and measure the time it takes for the light to return after bouncing off objects, providing accurate depth measurements in specific units like millimeters or meters <a class="yt-timestamp" data-t="01:39:06">[01:39:06]</a>, <a class="yt-timestamp" data-t="01:14:06">[01:14:06]</a>.
    *   **Structured Light Sensors** Examples include Kinect and Intel RealSense cameras. These sensors project an infrared pattern onto a scene and analyze the deformation of the lines with a camera to predict depth <a class="yt-timestamp" data-t="01:49:05">[01:49:05]</a>, <a class="yt-timestamp" data-t="01:49:11">[01:49:11]</a>.
    *   **Stereo/Multi-view Setups** Traditionally, depth estimation leveraged camera geometry from multiple cameras simultaneously looking at the same scene, using correspondences or disparity to infer depth <a class="yt-timestamp" data-t="00:05:33">[00:05:33]</a>.

*   **Characteristics and Limitations**
    *   **Noise and Missing Values**: Real depth data often suffers from missing values and noise due to the physical constraints of the capture rig and the properties of the sensors <a class="yt-timestamp" data-t="01:47:20">[01:47:20]</a>. This includes issues like reflective surfaces diverting LiDAR beams <a class="yt-timestamp" data-t="01:47:32">[01:47:32]</a>, or shadowing effects in structured light sensors where light cannot reach certain areas <a class="yt-timestamp" data-t="01:49:35">[01:49:35]</a>.
    *   **Material Sensitivity**: All depth sensors are sensitive to the actual material properties of the scene, which can introduce artifacts <a class="yt-timestamp" data-t="01:48:54">[01:48:54]</a>, <a class="yt-timestamp" data-t="01:50:00">[01:50:00]</a>.
    *   **Practical Examples**: Ground truth depth maps from real sensors can appear "trash" or "gross," with missing sections, different pixel colors, and overall poor quality, making them difficult to train on directly <a class="yt-timestamp" data-t="01:50:51">[01:50:51]</a>, <a class="yt-timestamp" data-t="01:53:21">[01:53:21]</a>.

## Synthetic Depth Data

[[Synthetic data generation and its applications | Synthetic depth data]] is created in simulated environments, often game engines or 3D modeling software.

*   **Generation Method**: In a simulated scene, like a video game or game engine, the exact depth for every single pixel is known because there is a full and explicit scene representation <a class="yt-timestamp" data-t="01:51:14">[01:51:14]</a>.
*   **Characteristics and Advantages**:
    *   **Perfect Ground Truth**: Synthetic depth is inherently dense and complete, meaning every pixel has a valid and perfect ground truth depth value <a class="yt-timestamp" data-t="01:51:40">[01:51:40]</a>, <a class="yt-timestamp" data-t="01:52:03">[01:52:03]</a>.
    *   **Cleanliness**: It is the "cleanest possible form of depth," guaranteed by the rendering pipeline <a class="yt-timestamp" data-t="01:52:03">[01:52:03]</a>. This reduces noise in gradient updates during training <a class="yt-timestamp" data-t="01:52:14">[01:52:14]</a>.
    *   **Suitability for Training**: Synthetic depth is particularly useful for [[Finetuning with synthetic data | fine-tuning]] models, especially for dense prediction tasks like depth estimation or [[Comparison of segmentation data sets | panoptic segmentation]], where every pixel requires a value <a class="yt-timestamp" data-t="01:52:27">[01:52:27]</a>, <a class="yt-timestamp" data-t="01:52:41">[01:52:41]</a>. Models like Marigold [[Monocular Depth Estimation using Diffusion Models | Monocular Depth Estimation using Diffusion Models]] benefit significantly from being [[Finetuning Pretrained Models for Depth Estimation | fine-tuned]] on datasets like Hypersim and Virtual KITTI, which provide simulated, perfect ground truth depth <a class="yt-timestamp" data-t="00:19:00">[00:19:00]</a>, <a class="yt-timestamp" data-t="00:25:35">[00:25:35]</a>.

## Comparison and Implications for AI Training

The choice between synthetic and real depth data heavily influences the training and performance of depth estimation models.

*   **Marigold Paper's Approach**: The Marigold paper, which leverages pre-trained diffusion models like Stable Diffusion for [[Monocular Depth Estimation using Diffusion Models | monocular depth estimation]], primarily [[Finetuning with synthetic data | fine-tunes with synthetic data]] <a class="yt-timestamp" data-t="01:10:08">[01:10:08]</a>. This is because synthetic depth is perfect and dense, allowing the model to handle data without invalid pixels, which real sensor data often has <a class="yt-timestamp" data-t="01:51:40">[01:51:40]</a>.
*   **Out-of-Distribution Challenges**: Monocular depth estimators can struggle with unfamiliar content or "out-of-distribution" images if their knowledge of the visual world is restricted by their training data <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. This highlights the importance of broad and diverse training datasets, which pre-trained models like Stable Diffusion (trained on billions of internet-scale images like LAION-5B) provide <a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>, <a class="yt-timestamp" data-t="00:24:25">[00:24:25]</a>.
*   **Model Performance**: Advanced models can now produce depth predictions that are often *better* than noisy real-world ground truth from physical sensors <a class="yt-timestamp" data-t="01:06:56">[01:06:56]</a>. This is due to the inherent cleanliness of synthetic data and the comprehensive visual priors learned by large-scale pre-trained models <a class="yt-timestamp" data-t="01:06:03">[01:06:03]</a>.
*   **The Future of Depth Sensors**: The significant progress in [[Monocular Depth Estimation using Diffusion Models | monocular depth estimation]] using readily available RGB cameras and powerful AI models suggests a potential decline in the need for expensive, specialized depth sensors like LiDAR. Software-based solutions can be much cheaper and easier to deploy <a class="yt-timestamp" data-t="01:07:56">[01:07:56]</a>.

### Challenges with Apline Invariant Depth

While current [[Monocular Depth Estimation using Diffusion Models | monocular depth estimation]] models, like Marigold, achieve state-of-the-art results, they often provide "affine invariant" depth, not true metric depth <a class="yt-timestamp" data-t="01:14:23">[01:14:23]</a>.

*   **Meaning of Apline Invariant**: Apline invariant depth means the model predicts relative distances (e.g., this pixel is closer than that pixel), but not the actual physical distance in meters or other units <a class="yt-timestamp" data-t="01:14:27">[01:14:27]</a>, <a class="yt-timestamp" data-t="01:33:04">[01:33:04]</a>. The output values are normalized (e.g., between -1 and 1 or 0 and 1) <a class="yt-timestamp" data-t="01:44:07">[01:44:07]</a>.
*   **Implications**: This "fake depth" is problematic for applications requiring precise 3D measurements, such as SLAM (Simultaneous Localization and Mapping), [[Comparison of 3D Representation Techniques | 3D reconstruction]], or photogrammetry, where true distances are essential for initializing point clouds or other 3D representations <a class="yt-timestamp" data-t="01:46:50">[01:46:50]</a>, <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a>. Users would need to apply an additional scaling factor or fine-tune on datasets with true depth information to recover metric scale <a class="yt-timestamp" data-t="01:00:32">[01:00:32]</a>, <a class="yt-timestamp" data-t="01:27:54">[01:27:54]</a>.

The trend suggests a future where high-quality depth can be reliably estimated from standard RGB images, potentially making dedicated depth sensors obsolete for many applications.