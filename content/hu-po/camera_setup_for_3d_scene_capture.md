---
title: Camera setup for 3D scene capture
videoId: hDuy1TgD8I4
---

From: [[hu-po]] <br/> 

Capturing dynamic 3D scenes for applications such as [[3d_scene_representation_and_simulation | 3D scene representation and simulation]] and [[3d_modeling_and_tracking_using_gaussian_splatting | 3D modeling and tracking using Gaussian splatting]] often relies on sophisticated camera setups. These setups provide the necessary data for accurate reconstruction and tracking of moving objects and environments.

## Multi-Camera Studio Environment

A prominent example of an advanced camera setup for dynamic 3D scene capture is a large-scale geodesic dome studio <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### Studio Specifications
*   **Dimensions**: These studios can have a radius of 5.49 meters and a total height of 4.15 meters <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. The center of the dome might be raised 1.4 meters above a hemisphere to allow increased access to the edges <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.
*   **Panel Structure**: They are often constructed from multiple panels, such as six pentagonal, 40 hexagonal, and 10 trimmed base panels <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   **Camera Density**: Such a studio can house a large number of cameras, for instance, 480 cameras, positioned around the area of interest <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. These cameras are synchronized to a central clock system <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
*   **Calibration**: A key advantage of these static structures is that the exact position of every camera is known beforehand <a class="yt-timestamp" data-t="00:04:21">[00:04:21]</a>. This precise calibration is often achieved by using a checkerboard pattern <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>, ensuring that every picture is taken at the same exact time with a known camera position <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. This level of control is considered a "cheat code" for 3D reconstruction <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Similar camera spheres have also been used in prior research, such as the original Nerf paper <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>.

### Camera Properties and Matrices
For 3D scene reconstruction, each camera's intrinsic (KC) and extrinsic (E) matrices are crucial <a class="yt-timestamp" data-t="00:58:06">[00:58:06]</a>:
*   **Extrinsic Matrix (E)**: This matrix tells you where the camera is in 3D space <a class="yt-timestamp" data-t="00:58:20">[00:58:20]</a>.
*   **Intrinsic Matrix (KC)**: This matrix describes the internal properties of the camera, such as focal length and distortions (e.g., fisheye effect) <a class="yt-timestamp" data-t="00:58:31">[00:58:31]</a>.
The precise knowledge of these matrices, particularly the extrinsic one, provides a strong starting point for reconstruction that is very difficult to replicate in real-world scenarios outside of controlled studio environments <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a>.

## Data Acquisition and Training
In the context of the Panoptic Sports dataset, captured using a geodesic dome studio <a class="yt-timestamp" data-t="02:02:04">[02:02:04]</a>:
*   **Camera Count**: While the dome can house 480 cameras <a class="yt-timestamp" data-t="00:47:44">[00:47:44]</a>, specific studies might use a subset, for example, 31 cameras <a class="yt-timestamp" data-t="02:02:18">[02:02:18]</a>.
*   **Data Split**: These 31 cameras can be split into 27 for training and 4 for testing <a class="yt-timestamp" data-t="02:02:20">[02:02:20]</a>. Test cameras are typically positioned to represent novel views (e.g., cameras 0, 10, 15, and 30) <a class="yt-timestamp" data-t="02:02:23">[02:02:23]</a>.
*   **Spatial Distribution**: The cameras are generally positioned in a hemisphere around the area of interest <a class="yt-timestamp" data-t="02:02:30">[02:02:30]</a>. This uniform distribution across multiple viewpoints is crucial for the quality of the results <a class="yt-timestamp" data-t="02:02:57">[02:02:57]</a>. If cameras were clustered, the results would be significantly worse <a class="yt-timestamp" data-t="02:02:51">[02:02:51]</a>.
*   **Image Resolution**: Captured images can be of resolutions like 640x360 <a class="yt-timestamp" data-t="02:03:14">[02:03:14]</a>.

## Types of Cameras and Their Use
*   **Multi-camera Capture**: This setup involves multiple cameras recording simultaneously, providing rich spatial information from different viewpoints <a class="yt-timestamp" data-t="00:44:44">[00:44:44]</a>. This inherently provides "correspondence information," which means identifying the same point in space across different camera views <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>.
*   **Monocular Video**: This uses a single camera (e.g., a cell phone) to capture a video. While seemingly different from multi-camera setups, moving a single camera over time effectively creates multiple viewpoints, similar to having multiple static cameras <a class="yt-timestamp" data-t="00:51:47">[00:51:47]</a>. The core need is to observe the scene from various viewpoints <a class="yt-timestamp" data-t="00:52:27">[00:52:27]</a>.
*   **Kinect Cameras**: These are structured light cameras that were popular for robotics <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>. They provide explicit depth information in the form of point clouds <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>. In a multi-camera setup like the geodesic dome, some studies might utilize 10 available depth cameras synchronized to the main system <a class="yt-timestamp" data-t="02:03:27">[02:03:27]</a>. However, the accuracy of real-world depth cameras is often a [[limitations_and_assumptions_of_dynamic_3d_modeling | limitation]] <a class="yt-timestamp" data-t="01:54:12">[01:54:12]</a>.
    *   **Point Clouds**: Raw point clouds from laser sensors (like those on autonomous vehicles) often show circular patterns due to the sensor's rotation <a class="yt-timestamp" data-t="00:35:10">[00:35:10]</a>. These points typically only contain XYZ position and RGB color data <a class="yt-timestamp" data-t="00:36:03">[00:36:03]</a>.
*   **Reference Frames**: To aid [[optimization_techniques_and_challenges_for_3d_scene_representation | optimization techniques]], methods may acquire "pseudoground truth" foreground/background segmentation masks by differencing each frame with a reference frame where no foreground objects are present <a class="yt-timestamp" data-t="02:03:54">[02:03:54]</a>. This assumes consistent lighting, which may not hold true in real-world, outdoor scenarios <a class="yt-timestamp" data-t="02:04:07">[02:04:07]</a>.

## Challenges and Considerations
The highly controlled and calibrated environment of a multi-camera studio, while enabling excellent results, presents significant [[challenges_and_limitations_in_3d_generation | challenges and limitations in 3D generation]] for broader application:
*   **Real-world Applicability**: The methods presented often require multi-camera setups and do not work for off-the-shelf monocular video <a class="yt-timestamp" data-t="02:21:27">[02:21:27]</a>. Achieving perfect extrinsic camera matrices and uniform camera distribution is difficult outside of specialized studios <a class="yt-timestamp" data-t="02:21:38">[02:21:38]</a>.
*   **Initial Scene Visibility**: The methods are typically only able to track parts of the scene that are visible in the initial frame and would fail to reconstruct new objects entering the scene <a class="yt-timestamp" data-t="01:05:55">[01:05:55]</a>.
*   **Depth Camera Accuracy**: Despite their utility, real-world depth cameras are often considered inaccurate and unreliable, unlike synthetic scene data <a class="yt-timestamp" data-t="01:05:55">[01:05:55]</a>.
*   **Lighting Consistency**: Studio environments provide uniform lighting, which simplifies tasks like foreground/background segmentation <a class="yt-timestamp" data-t="01:57:24">[01:57:24]</a>. This is difficult to replicate in natural environments where lighting can change. <a class="yt-timestamp" data-t="02:04:23">[02:04:23]</a>.