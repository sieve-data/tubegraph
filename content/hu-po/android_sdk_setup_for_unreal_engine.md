---
title: Android SDK setup for Unreal Engine
videoId: xoRnHc_GkAY
---

From: [[hu-po]] <br/> 

Setting up the Android SDK is crucial for developing and packaging applications for Android-based VR headsets, such as the [[quest_pro_integration_in_unreal_engine_5 | Meta Quest Pro]], within Unreal Engine 5 (UE5) <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. This process involves configuring Unreal Engine project settings, installing necessary Android development tools, and ensuring proper device connectivity.

## Initial Plugin Setup

To begin, ensure the relevant plugins for your VR headset are correctly integrated:

*   Place the [[quest_pro_integration_in_unreal_engine_5 | Oculus Quest integration]] files into the Epic Games plugin folder <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   In Unreal Editor, navigate to `Edit > Plugins` <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
*   After placing the plugins, a restart of the Unreal Editor is typically required for them to appear and load properly <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>, <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   Enable the following Oculus plugins: Oculus VR, Oculus Subsystem, and Oculus Audio <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
*   Consider enabling OpenXR-related plugins like OpenXR Hand Tracking and OpenXR Eye Tracking, along with Mixed Reality Capture Framework, by typing "XR" in the plugin search bar <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   Restart Unreal Editor again after enabling the desired plugins <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
*   Ensure at least one Unreal Engine level (map) is saved <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>. The VR Starter template usually comes with a suitable map <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
*   Set both the editor startup and game default maps to your chosen VR template map in `Edit > Project Settings > Maps & Modes` <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

## Unreal Engine Project Settings Configuration for Android

Several project settings need adjustment for Android development:

*   In `Edit > Project Settings`, under the `Engine` section, navigate to `Input` <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
*   In the `Mobile` section, set `Default Touch Interface` to `Clear` (which means `None`) <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   Scroll down to the `Platforms` section and select `Android` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   Set `Minimum SDK Version` and `Target SDK Version` to `29` <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   If `Configure Now` is available in the APK Packaging section, click it <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.
*   In `Engine > Rendering > Mobile`, set `Mobile MSAA` (Multi-Sample Anti-Aliasing) to `4X` <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   Also in the `Rendering` section, under `VR`, ensure `Mobile HDR` is turned `off` <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.
*   Changes made in Project Settings are usually saved automatically <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.

## Addressing Android Debug Bridge (ADB) Requirements

Connecting your headset to a PC for development often requires Android Debug Bridge (ADB):

*   The Android Debug Bridge is a versatile command-line tool for communicating with an Android device <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
*   To enable connection, `USB Debugging` must be turned on within the headset's settings <a class="yt-timestamp" data-t="00:49:18">[00:49:18]</a>, <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>.
*   After connecting the headset via USB, you may need to "Always allow from this computer" when prompted on the headset <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.
*   ADB over Wi-Fi can be enabled in the headset settings, allowing wireless connection after initial USB setup <a class="yt-timestamp" data-t="00:56:34">[00:56:34]</a>, <a class="yt-timestamp" data-t="00:57:29">[00:57:29]</a>. This allows viewing device logs <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>.

## Installing Android Studio and SDK Tools

Unreal Engine requires the Android SDK, which is typically installed via Android Studio:

*   The Android SDK is needed for proper installation <a class="yt-timestamp" data-t="01:17:27">[01:17:27]</a>.
*   Download and install Android Studio, opting for a standard installation <a class="yt-timestamp" data-t="01:21:07">[01:21:07]</a>.
*   After installation, open Android Studio.
*   Navigate to `Configure > SDK Manager` (or `Tools > SDK Manager`) <a class="yt-timestamp" data-t="01:41:47">[01:41:47]</a>, <a class="yt-timestamp" data-t="01:42:30">[01:42:30]</a>.
*   In the `SDK Tools` tab, check the box for `Android SDK Command-line Tools (latest)` <a class="yt-timestamp" data-t="01:43:12">[01:43:12]</a>. Click `Apply` to download and install <a class="yt-timestamp" data-t="01:43:24">[01:43:24]</a>.

### Meta Quest Developer Hub (MQDH)

The Meta Quest Developer Hub (MQDH) is a standalone companion tool that can assist with managing devices and development:

*   It is available for download on Windows <a class="yt-timestamp" data-t="00:39:49">[00:39:49]</a>.
*   To use MQDH, a developer account part of an organization on the Oculus Developer Dashboard is required <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>, <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.
*   MQDH can detect existing ADB clients or allows specifying the ADB client path <a class="yt-timestamp" data-t="00:46:23">[00:46:23]</a>.
*   It provides tools for device management, recording videos, screenshots, and enabling ADB over Wi-Fi <a class="yt-timestamp" data-t="00:55:13">[00:55:13]</a>.

## Packaging Project Attempts and Troubleshooting

After setting up the SDK, you can attempt to package your Unreal Engine project for Android:

*   In Unreal Engine 5, the packaging option is found under `Platforms > Android > Android ASTC` <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>, <a class="yt-timestamp" data-t="01:11:31">[01:11:31]</a>.
*   You can select `Use Project Settings` and `Development` as packaging options <a class="yt-timestamp" data-t="01:11:35">[01:11:35]</a>.
*   If the SDK for Android is reported as "not installed properly" during packaging <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>, navigate to the Unreal Engine installation directory (e.g., `C:\Program Files\Epic Games\UE_5.x\Engine\Extras\Android`) <a class="yt-timestamp" data-t="01:46:05">[01:46:05]</a>.
*   Run the `SetupAndroid.bat` batch file within this directory <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a>. This script helps configure SDK paths and accept licenses.
*   Restarting the computer may be necessary after these installations and configurations for all paths and dependencies to be recognized correctly <a class="yt-timestamp" data-t="01:48:37">[01:48:37]</a>.

> [!NOTE]
> Setting up development environments like this can be complex due to varying dependencies and versions <a class="yt-timestamp" data-t="01:49:05">[01:49:05]</a>. A more streamlined approach, such as a virtualized development environment, would be beneficial to avoid manual configuration issues <a class="yt-timestamp" data-t="01:49:25">[01:49:25]</a>.