---
title: Unreal Engine plugin management
videoId: xoRnHc_GkAY
---

From: [[hu-po]] <br/> 

Managing plugins in Unreal Engine is crucial for extending its functionality, especially for specialized development like virtual reality (VR) projects. This process involves installing, loading, and configuring plugins, often alongside specific SDKs and development tools.

## Installing and Loading Plugins

To install a plugin, it must be placed into the Epic Games plugin folder <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. After placing the plugin files, the Unreal Editor typically needs to be restarted for the new plugins to be detected and loaded <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

Once restarted, plugins can be loaded through the "Edit" > "Plugins" menu <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. For VR development, specific plugins like "Oculus VR," "Oculus subsystem," and "Oculus audio" are essential <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. Additionally, various XR-related plugins such as "Spatial Anchors," "OpenXR," "OpenXR Hand Tracking," and "OpenXR Eye Tracking" might need to be enabled <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. After enabling plugins, another restart of the Unreal Editor is required <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## Troubleshooting Plugin Issues

*   **Restarting the Editor**: A common solution for plugins not appearing or functioning correctly is to restart the Unreal Editor <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
*   **Plugin Naming**: Sometimes, specific plugins like "Meta XR" might not be present, and instead, older "Oculus VR" plugins are available <a class="yt-timestamp" data-t="01:03:48">[01:03:48]</a>.
*   **Developer Accounts**: For developing Oculus VR apps, a developer account that is a member of an organization is required <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>. This involves creating a new organization in the developer dashboard <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.

## [[android_sdk_setup_for_unreal_engine | Android SDK Setup for Unreal Engine]] for VR Development

Setting up Unreal Engine for VR development, particularly for devices like the Meta Quest Pro, requires specific configurations related to the Android SDK.

### Project Settings Configuration
In Unreal Engine's project settings, several adjustments are necessary:
*   **Maps & Modes**: Ensure both the editor startup map and the game default map are set to your VR template level <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Engine > Input**:
    *   Locate the "Mobile" section <a class="yt-timestamp" data-t="00:10:19">[00:10:19]</a>.
    *   Set "Default Touch Interface" to "Clear" (None) <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Platforms > Android**:
    *   Scroll down to the "Platforms" section and select "Android" <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   Under "APK Packaging," set "Minimum SDK Version" and "Target SDK Version" to 29 <a class="yt-timestamp" data-t="00:11:41">[00:11:41]</a>.
    *   Configure now <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a> and accept the SDK license <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
    *   Open "Advanced APK Packaging" and hit the plus button next to "Package for Oculus Mobile devices" <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   **Engine > Rendering**:
    *   Under the "Mobile" section, ensure "Mobile MSAA" is set to 4x <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
    *   Enable "Use Half Precision" <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
    *   Under the "VR" section, ensure "Mobile HDR" is turned off <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

### Android Debug Bridge (ADB) and [[metaquest_developer_hub_usage | Meta Quest Developer Hub]]
To communicate with the VR device, the Android Debug Bridge (ADB) is necessary <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.
*   **Installation**: ADB is typically included with Android Studio's command-line tools <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>.
*   **[[metaquest_developer_hub_usage | Meta Quest Developer Hub]] (MQDH)**: This standalone companion tool is essential for managing Meta Quest devices <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.
    *   Download and install the MQDH <a class="yt-timestamp" data-t="00:39:46">[00:39:46]</a>.
    *   Log in with a Meta account <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>.
    *   **ADB Path**: Configure the ADB client path within MQDH settings <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>.
    *   **Device Manager**: Set up a new device <a class="yt-timestamp" data-t="00:47:49">[00:47:49]</a>.
    *   **Enable Developer Mode**: On the Quest device, enable "Developer Mode" in the Oculus app <a class="yt-timestamp" data-t="00:53:34">[00:53:34]</a>.
    *   **USB Debugging**: Allow USB debugging access from the computer when prompted on the headset <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.
    *   **ADB over Wi-Fi**: This can be enabled within the MQDH to allow wireless communication with the headset <a class="yt-timestamp" data-t="00:56:34">[00:56:34]</a>. The device logs can be viewed via MQDH <a class="yt-timestamp" data-t="00:58:10">[00:58:10]</a>.

### Android SDK Tools Installation
*   **Android Studio**: Install Android Studio to acquire the necessary SDK <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>.
*   **SDK Manager**: Inside Android Studio, use the SDK Manager ("Configure" > "SDK Manager" or "Help" > "Windows" > "SDK Manager") <a class="yt-timestamp" data-t="01:41:47">[01:41:47]</a>.
*   **SDK Command Line Tools**: Check the box for "SDK Command Line Tools" and click apply to download them <a class="yt-timestamp" data-t="01:43:12">[01:43:12]</a>.
*   **SetupAndroid.bat**: Run the `SetupAndroid.bat` file located in Unreal Engine's `Engine\Extras\Android` directory to configure the Android SDK paths for Unreal Engine <a class="yt-timestamp" data-t="01:47:05">[01:47:05]</a>.

### Packaging Projects
Once the SDK is properly configured, projects can be packaged for Android. In Unreal Engine 5, the packaging option is found under "Platforms" > "Android" > "Android ASTC" <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>. Packaging might fail if the SDK for Android is not installed properly <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.

## General Challenges in Setup

Setting up development environments, especially for VR with Unreal Engine, can be complex due to several factors:
*   **Dependency Management**: It often requires installing many different tools and dependencies, each with specific versions <a class="yt-timestamp" data-t="01:49:05">[01:49:05]</a>.
*   **Version Compatibility**: Ensuring all tools and SDKs are compatible across their various versions can be challenging <a class="yt-timestamp" data-t="01:49:12">[01:49:12]</a>.
*   **Unclear Errors**: Error messages are often generic, making it difficult to pinpoint the exact issue <a class="yt-timestamp" data-t="01:49:17">[01:49:17]</a>.
*   **Heterogeneous Systems**: The wide variety of system configurations makes troubleshooting complex <a class="yt-timestamp" data-t="01:49:23">[01:49:23]</a>.
*   **Desire for Virtualized Environments**: A common sentiment among developers is the need for virtualized development environments (like Docker) to simplify setup and avoid version conflicts <a class="yt-timestamp" data-t="01:49:25">[01:49:25]</a>.