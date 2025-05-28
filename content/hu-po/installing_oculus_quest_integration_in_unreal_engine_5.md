---
title: Installing Oculus Quest integration in Unreal Engine 5
videoId: xoRnHc_GkAY
---

From: [[hu-po]] <br/> 

Integrating Oculus Quest devices with [[game_development_using_unreal_engine_5 | Unreal Engine 5]] for VR development involves several steps, including plugin setup, project configuration, and setting up the Android development environment. This process can be complex due to dependency management and version compatibility issues <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.

## Plugin Setup

1.  **Transfer Plugins**: Manually place the Oculus Quest integration files into the Epic Games plugin folder <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
2.  **Load Plugins in Unreal Engine**:
    *   Navigate to `Edit > Plugins` in the Unreal Engine editor <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   After adding new plugins, a restart of the Unreal Editor is required for them to appear and load properly <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>, <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
3.  **Enable Essential Plugins**:
    *   Search for and enable all relevant Oculus plugins, such as `Oculus VR`, `Oculus Subsystem`, and `Oculus Audio` <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
    *   Enable `OpenXR` and related plugins like `OpenXR Hand Tracking`, `OpenXR Eye Tracking`, and `OpenXR Microsoft Hand Interaction` <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
    *   A subsequent restart of the Unreal Editor is necessary after enabling these plugins <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## Project Settings Configuration for VR Development

Within `Edit > Project Settings`, several adjustments are needed:

1.  **Maps & Modes**:
    *   Set both the `Editor Startup Map` and the `Game Default Map` to your VR template map (e.g., `VR Template Map`) <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>, <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
2.  **Engine - Input**:
    *   Locate the `Mobile` section <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
    *   For `Default Touch Interface`, select `Clear` to set its value to `None` <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
3.  **Platforms - Android**:
    *   Scroll down to the `Platforms` section and select `Android` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   In the `APK Packaging` section, set `Minimum SDK Version` and `Target SDK Version` to `29` <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    *   Open `Advanced APK Packaging` for Oculus mobile devices <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>, <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.
4.  **Engine - Rendering**:
    *   Under the `Mobile` section, ensure `Mobile MSAA (Multi-Sample Anti-Aliasing)` is set to `4X` <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
    *   In the `VR` section, make sure `Mobile HDR` is turned `Off` <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

## Setting up Android Development Environment

Proper Android SDK setup is crucial for [[game_development_using_unreal_engine_5 | game development using Unreal Engine 5]] for Oculus Quest.

1.  **Android Debug Bridge (ADB)**:
    *   ADB is a versatile command-line tool for communicating with Android devices <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
    *   It is part of the Android SDK <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
    *   Initially, attempts were made to download `command line tools only` for the SDK <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
2.  **Android Studio**:
    *   To fully resolve "SDK for Android is not installed properly" errors when packaging, [[setting_up_android_sdk_for_oculus_quest_development | installing Android Studio]] is recommended as it includes the necessary SDK components <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>.
    *   After installation, open Android Studio and navigate to `SDK Manager` (found under `Help > Windows` or `Configure > SDK Manager`) <a class="yt-timestamp" data-t="01:42:30">[01:42:30]</a>.
    *   In the `SDK Tools` tab, check the box for `SDK command line tools (latest)` and click `Apply` to download <a class="yt-timestamp" data-t="01:43:12">[01:43:12]</a>.
3.  **Unreal Engine's Android Setup Script**:
    *   After installing Android Studio and its SDK components, run the `SetupAndroid.bat` file located in `[Unreal Engine Installation Path]\Engine\Extras\Android` <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a>. This script helps configure Unreal Engine to find the Android SDK paths <a class="yt-timestamp" data-t="01:48:03">[01:48:03]</a>.

## Oculus Developer Account and Meta Quest Developer Hub

1.  **Oculus Developer Organization**: To develop Oculus VR apps, your developer account must be a member of an organization. Create one via the developer dashboard <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.
2.  **[[meta_quest_developer_hub_for_managing_vr_apps | Meta Quest Developer Hub (MQDH)]]**:
    *   MQDH is a standalone companion tool for managing VR apps <a class="yt-timestamp" data-t="00:39:11">[00:39:11]</a>, <a class="yt-timestamp" data-t="00:39:46">[00:39:46]</a>. Download and install it for Windows <a class="yt-timestamp" data-t="00:39:52">[00:39:52]</a>.
    *   Log in with your Meta account and configure the ADB client path within MQDH <a class="yt-timestamp" data-t="00:44:59">[00:44:59]</a>, <a class="yt-timestamp" data-t="00:46:23">[00:46:23]</a>.
3.  **Headset Connection and Developer Mode**:
    *   **Air Link Interference**: If Air Link was previously used, it might prevent a stable USB connection for development <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>. Disconnect Air Link mode to ensure proper USB connectivity <a class="yt-timestamp" data-t="00:57:29">[00:57:29]</a>.
    *   **Enable Developer Mode**: On your Oculus Quest Pro, go into the companion app (`Menu > Devices > [Your Headset] > Developer Mode`) and turn it `On` <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>, <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>.
    *   **USB Connection**: Plug your headset into the development PC via a USB-C cable <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.
    *   **Allow Access**: Put on your headset and grant permission to `Always allow from this computer` for USB debugging <a class="yt-timestamp" data-t="00:54:25">[00:54:25]</a>, <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.
    *   **ADB over Wi-Fi**: Within the [[meta_quest_developer_hub_for_managing_vr_apps | Meta Quest Developer Hub]], you can enable `ADB over Wi-Fi` for wireless debugging once a USB connection is established <a class="yt-timestamp" data-t="00:56:25">[00:56:25]</a>, <a class="yt-timestamp" data-t="00:57:36">[00:57:36]</a>.

## Packaging and Deployment (Troubleshooting)

1.  **Packaging the Project**:
    *   In [[game_development_using_unreal_engine_5 | Unreal Engine 5]], the `Package Project` option is found under `Platforms > Android > Android ASTC` (it is no longer directly in the `File` menu) <a class="yt-timestamp" data-t="01:10:57">[01:10:57]</a>.
    *   Select `Use Project Settings` and `Development` for packaging <a class="yt-timestamp" data-t="01:11:35">[01:11:35]</a>.
2.  **Common Issues**:
    *   **"SDK for Android is not installed properly"**: This is a frequent error indicating misconfigured or missing Android SDK components, often resolved by a proper Android Studio installation and configuration <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>, <a class="yt-timestamp" data-t="01:45:44">[01:45:44]</a>.
    *   **`VR Preview` Greyed Out**: If the `VR Preview` option is unavailable, it usually means the HMD (head-mounted display) is not properly detected or connected, or necessary runtime/plugins are not installed/enabled <a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>, <a class="yt-timestamp" data-t="00:33:16">[00:33:16]</a>.
    *   [[troubleshooting_connectivity_issues_with_oculus_quest_pro | Connectivity issues with Oculus Quest Pro]] can arise from Air Link being active or developer mode not being correctly enabled <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.

> [!NOTE]
> This process is often involved and time-consuming due to the need to install various tools and manage dependencies across different software versions <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>. A consistent development environment, ideally virtualized, could simplify such setups <a class="yt-timestamp" data-t="01:49:25">[01:49:25]</a>.