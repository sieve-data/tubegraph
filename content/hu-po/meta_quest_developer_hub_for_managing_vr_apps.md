---
title: Meta Quest Developer Hub for managing VR apps
videoId: xoRnHc_GkAY
---

From: [[hu-po]] <br/> 

The Meta Quest Developer Hub (MQDH) is a standalone companion tool designed to easily manage and develop virtual reality (VR) applications for Meta Quest devices <a class="yt-timestamp" data-t="00:39:11">[00:39:11]</a>. It provides a centralized interface for various development tasks, from device management to app promotion <a class="yt-timestamp" data-t="00:39:49">[00:39:49]</a>.

## Installation and Setup

To use MQDH:
1.  Download the Meta Quest Developer Hub for Windows <a class="yt-timestamp" data-t="00:39:49">[00:39:49]</a>.
2.  Run the installer and double-click the setup file <a class="yt-timestamp" data-t="00:41:00">[00:41:00]</a>.
3.  Once installed, the MQDH icon will appear on your desktop <a class="yt-timestamp" data-t="00:43:42">[00:43:42]</a>.
4.  Launch the MQDH and log in with your Meta account <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>. If you don't have one, you will need to create a developer account and join an organization to develop [[installing_oculus_quest_integration_in_unreal_engine_5 | Oculus VR]] apps <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>, such as a "Booboo verse" organization <a class="yt-timestamp" data-t="00:38:43">[00:38:43]</a>.

## Key Features

### Device Management
The MQDH includes a device manager to set up and monitor your Quest headset <a class="yt-timestamp" data-t="00:47:49">[00:47:49]</a>.
To connect your headset:
*   Ensure Bluetooth is enabled on your computer <a class="yt-timestamp" data-t="00:47:57">[00:47:57]</a>.
*   Enable developer mode in the Oculus companion app on your phone <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>, which can be found under Menu > Devices > Quest Pro > Developer Mode <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>.
*   Plug the headset into the computer via a USB-C cable <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a> <a class="yt-timestamp" data-t="00:50:00">[00:50:00]</a>.
*   Allow USB debugging access from your computer by putting on the headset and confirming the prompt <a class="yt-timestamp" data-t="00:54:25">[00:54:25]</a> <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.

Once connected, you can:
*   View device status <a class="yt-timestamp" data-t="00:50:38">[00:50:38]</a>.
*   Record videos and take screenshots <a class="yt-timestamp" data-t="00:55:21">[00:55:21]</a>.
*   Enable [[troubleshooting_connectivity_issues_with_oculus_quest_pro | ADB over Wi-Fi]] for wireless debugging and deployment <a class="yt-timestamp" data-t="00:55:25">[00:55:25]</a> <a class="yt-timestamp" data-t="00:57:36">[00:57:36]</a>.
*   Access device logs, which may show warnings for various components like Wi-Fi or Halo camera <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a> <a class="yt-timestamp" data-t="00:58:37">[00:58:37]</a>. Logs can be filtered using regex <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>.

### App Management and Tools
MQDH facilitates the creation and management of VR applications:
*   You can create new apps, which involves an app metadata submission process <a class="yt-timestamp" data-t="00:42:15">[00:42:15]</a> <a class="yt-timestamp" data-t="00:42:45">[00:42:45]</a>.
*   The dashboard allows for app promotion, testing, and various other functionalities <a class="yt-timestamp" data-t="00:42:55">[00:42:55]</a> <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>.
*   [[application_of_light_glue_in_vr_and_ar | App Lab ads]] can be used to promote VR apps through Facebook and Instagram <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>.

The hub also provides access to various tools and SDKs:
*   It detects and configures ADB clients <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a>.
*   It includes resources for Meta Avatars, GPU sub-trace, mixed reality capture tools, applications, and SDKs like the [[installing_oculus_quest_integration_in_unreal_engine_5 | Oculus Mobile SDK]] <a class="yt-timestamp" data-t="00:47:22">[00:47:22]</a>.
*   It supports development with Unity and [[game_development_using_unreal_engine_5 | Unreal Engine]], including features for hand gameplay <a class="yt-timestamp" data-t="00:47:38">[00:47:38]</a>.
*   Additional tools like OVR metrics tool, GPU profiling, and trace analysis are available <a class="yt-timestamp" data-t="00:55:31">[00:55:31]</a>.

## Integration with Unreal Engine 5

While direct launching of a VR preview from Unreal Engine 5 might be grayed out <a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>, MQDH plays a crucial role in the development workflow for Meta Quest. It helps in:
*   Enabling necessary [[configuring_unreal_engine_5_plugins_for_vr_development | Meta XR plugins]] within Unreal Engine <a class="yt-timestamp" data-t="01:03:48">[01:03:48]</a>.
*   Providing the [[setting_up_android_sdk_for_oculus_quest_development | Android SDK]] and [[setting_up_android_sdk_for_oculus_quest_development | ADB]] required for packaging and deploying projects to the Quest headset <a class="yt-timestamp" data-t="01:14:41">[01:14:41]</a> <a class="yt-timestamp" data-t="01:17:36">[01:17:36]</a>.
*   Setting up Android Studio and its SDK components, which are often prerequisites for Unreal Engine's Android packaging <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a> <a class="yt-timestamp" data-t="01:40:49">[01:40:49]</a>.

> [!NOTE] Troubleshooting Tip
> If Unreal Engine reports the Android SDK is not installed properly, try running `setup_android.bat` located in the Unreal Engine installation directory (e.g., `C:\Program Files\Epic Games\UE_5.0\Engine\Extras\Android`) <a class="yt-timestamp" data-t="01:46:05">[01:46:05]</a> <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a>. This can help resolve dependency issues <a class="yt-timestamp" data-t="01:47:41">[01:47:41]</a>. Often, a computer restart is needed after installing SDKs or setting up MQDH <a class="yt-timestamp" data-t="01:43:42">[01:43:42]</a> <a class="yt-timestamp" data-t="01:48:40">[01:48:40]</a>.

The process of setting up all dependencies for VR development, including MQDH, can be complex due to the "heterogeneity" of different systems and versions <a class="yt-timestamp" data-t="01:49:23">[01:49:23]</a>. Ideally, a virtualized development environment like Docker would simplify this process <a class="yt-timestamp" data-t="01:49:25">[01:49:25]</a>.