---
title: Setting up Android SDK for Oculus Quest development
videoId: xoRnHc_GkAY
---

From: [[hu-po]] <br/> 

Setting up a virtual reality (VR) development environment in Unreal Engine 5 for Oculus Quest devices involves several crucial steps, including [[installing_oculus_quest_integration_in_unreal_engine_5 | plugin integration]], project configuration, and Android SDK setup. This guide details the process based on a live demonstration.

## Initial Unreal Engine Setup

The first step involves integrating the Oculus Quest files into Unreal Engine's plugin folder. This process manually moves the Oculus Quest integration files into the Epic Games plugin folder <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

After placing the files, the Unreal Engine editor needs to be restarted for the newly added plugins to be recognized and loaded <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. Once restarted, all relevant Oculus plugins, such as Oculus VR, Oculus Subsystem, and Oculus Audio, can be enabled within the editor's plugin settings <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Additionally, other XR plugins like OpenXR Hand Tracking and OpenXR Eye Tracking can be enabled <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>, followed by another restart <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. This step is part of [[configuring_unreal_engine_5_plugins_for_vr_development | configuring Unreal Engine 5 plugins for VR development]].

## Configuring Unreal Engine Project Settings

Several project settings in Unreal Engine must be adjusted to ensure proper VR functionality:

*   **Maps and Modes**: Set both the editor startup map and the game default map to the desired VR template level, such as the VR template map <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>. This is found under `Edit > Project Settings > Maps and Modes` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
*   **Engine Input (Mobile Section)**: Navigate to `Engine > Input` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a> and within the "Mobile" section <a class="yt-timestamp" data-t="00:10:23">[00:10:23]</a>, clear the "Default Touch Interface" to set its value to "None" <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Platforms Android**: Under the `Platforms > Android` section <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>:
    *   Hit "Configure Now" in the APK packaging section <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>, if necessary.
    *   Accept the SDK license <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
    *   Set the "Minimum SDK Version" and "Target SDK Version" to `29` <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
    *   In "Advanced APK Packaging," add support for Oculus mobile devices <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
*   **Rendering (Mobile and VR Sections)**: Within the `Engine > Rendering` settings <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>:
    *   In the "Mobile" section <a class="yt-timestamp" data-t="00:13:43">[00:13:43]</a>, set "Mobile MSAA (Multi-Sample Anti-Aliasing)" to `4X` <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
    *   In the "VR" section <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>, ensure "Mobile HDR" is turned off <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

## Establishing Device Connectivity

Connecting the Oculus Quest Pro to the development PC for debugging is crucial. Initially, the headset may show a "General device problem not connected" status <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, possibly due to Air Link mode preventing a USB-C connection <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

To facilitate connectivity:
*   **Enable Quest Link**: Launch the Quest Link from the headset's settings to connect it <a class="yt-timestamp" data-t="00:24:12">[00:24:12]</a>.
*   **Developer Mode**: On the Meta Quest mobile app, navigate to `Menu > Devices`, select the Quest Pro, and enable "Developer Mode" <a class="yt-timestamp" data-t="00:54:09">[00:54:09]</a>. This activates additional settings in the headset.
*   **Allow USB Debugging**: When prompted in the headset, allow USB debugging from the computer <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.
*   **ADB over Wi-Fi**: Enable ADB over Wi-Fi in the headset to maintain a connection without a physical cable <a class="yt-timestamp" data-t="00:57:29">[00:57:29]</a>. This step is key for [[troubleshooting_connectivity_issues_with_oculus_quest_pro | troubleshooting connectivity issues with Oculus Quest Pro]].

## Installing Meta Quest Developer Hub

For streamlined device management and app deployment, the [[meta_quest_developer_hub_for_managing_vr_apps | Meta Quest Developer Hub (MQDH)]] is essential.

1.  **Developer Organization**: Create a new organization within the Oculus Developer Dashboard <a class="yt-timestamp" data-t="00:38:10">[00:38:10]</a>.
2.  **Download MQDH**: Download and install the MQDH application for Windows <a class="yt-timestamp" data-t="00:39:49">[00:39:49]</a>.
3.  **Configure ADB Path**: Within MQDH settings, specify the ADB client path <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>. MQDH can then be used to manage devices, record videos, take screenshots, and install apps directly <a class="yt-timestamp" data-t="00:55:13">[00:55:13]</a>.

## Finalizing Android SDK Setup in Unreal Engine

Even with MQDH, Unreal Engine might still report that the Android SDK is not installed properly <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.

1.  **Install Android Studio**: Download and install Android Studio. Even if the full IDE is not desired, it contains necessary SDK components <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>.
2.  **SDK Manager**: Inside Android Studio, navigate to `Configure > SDK Manager` <a class="yt-timestamp" data-t="01:41:47">[01:41:47]</a>. Under the "SDK Tools" tab, check the box for "SDK Command Line Tools" and apply the changes to download them <a class="yt-timestamp" data-t="01:43:12">[01:43:12]</a>.
3.  **Run SetupAndroid.bat**: Go to Unreal Engine's installation directory (e.g., `C:\Program Files\Epic Games\UE_5.0\Engine\Extras\Android`) <a class="yt-timestamp" data-t="01:46:09">[01:46:09]</a> and run `SetupAndroid.bat` <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a>. This script helps configure the Android SDK and NDK paths for Unreal Engine.

## Challenges and Outlook

The process of setting up development environments for VR, especially with multiple dependencies, can be complex and prone to issues with different versions and paths <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. A potential solution for simplifying this process could be using [[setting_up_docker_for_machine_learning_projects | Docker]] to create a virtualized development environment that abstracts away the complexities of installing various versions and dependencies <a class="yt-timestamp" data-t="01:49:25">[01:49:25]</a>. Future goals include moving towards actual game development and integrating advanced features like Neural Radiance Fields within Unreal Engine <a class="yt-timestamp" data-t="01:49:54">[01:49:54]</a>.