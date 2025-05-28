---
title: Metaquest Developer Hub usage
videoId: xoRnHc_GkAY
---

From: [[hu-po]] <br/> 

The [[metaquest_developer_hub|Meta Quest Developer Hub]] (MQDH) is a standalone companion tool designed to help developers easily manage their Meta Quest devices and facilitate the development of VR applications [00:39:11, 00:39:49].

## Installation and Setup
To begin using the [[metaquest_developer_hub|Meta Quest Developer Hub]]:
1.  **Download**: Obtain the installation file, typically an executable for Windows [00:39:49, 00:40:45].
2.  **Extract and Run**: Extract the contents of the downloaded file and double-click the installer to run it [00:40:45, 00:41:00].
3.  **Log In**: Upon first launch, log in with your Meta account or create a new developer account if you don't have one. This is necessary to access the full features of the Hub [00:44:50, 00:45:04].
4.  **ADB Client**: The MQDH includes an Android Debug Bridge (ADB) client. If you have an existing ADB client, the Hub may detect it. You can specify the ADB path within the Hub's settings if needed [00:45:24, 00:46:26]. It's recommended to store Hub-related files in a dedicated folder, such as "Meta Quest Pro" [00:45:40, 00:46:26].

## Connecting Your Meta Quest Headset
Connecting your headset to the [[metaquest_developer_hub|Meta Quest Developer Hub]] is crucial for development:
1.  **Physical Connection**: Connect your Meta Quest headset to your development PC via a USB cable [00:47:57, 00:48:09].
2.  **Enable Developer Mode (on Meta App)**:
    *   Open the Meta (Oculus) app on your PC [00:53:34].
    *   Navigate to Menu > Devices [00:54:09].
    *   Select your Quest Pro device [00:54:13].
    *   Find and enable "Developer Mode" [00:54:14, 00:54:23].
3.  **Enable Developer Mode (on Headset)**:
    *   On the Quest device itself, go to Settings, then navigate to the "Developer" section [00:49:12, 00:49:25].
    *   Enable USB debugging [01:02:30, 01:02:33].
    *   When prompted in the headset, "Always allow from this computer" [00:54:40, 00:54:43].
4.  **Bluetooth**: Ensure Bluetooth is enabled on your computer for device setup [00:47:57, 00:48:00].
5.  **Oculus App Status**: It's advisable to close the Oculus app before starting MQDH setup to avoid conflicts [00:48:21, 00:48:31]. The MQDH will indicate when the device is connected [00:50:25, 00:50:28].

## Key Features and Functionality
Once connected, the [[metaquest_developer_hub|Meta Quest Developer Hub]] provides various tools:
*   **Device Management**: Set up and monitor your connected Meta Quest devices [00:47:57].
*   **Development Tools**: Access tools like:
    *   Meta Avatars [00:47:22].
    *   GPU Sub Trace [00:47:22].
    *   Mixed Reality Capture tools [00:47:26].
    *   Oculus Mobile SDKs [00:47:34].
    *   Specific support for Unity and [[unreal_engine_plugin_management|Unreal Engine]] development [00:47:38, 00:47:41].
    *   Hand gameplay features [00:47:41].
*   **Debugging and Monitoring**:
    *   Record videos and take screenshots from the headset [00:55:21, 00:55:24].
    *   Enable ADB over Wi-Fi for wireless debugging, allowing you to disconnect the USB cable once active [00:55:25, 00:56:10, 00:57:36, 00:57:38].
    *   View device logs, which can show warnings related to Wi-Fi, Halo camera, audio triggers, or hand tracking [00:58:13, 00:58:27, 00:58:55].
    *   Access OVR metrics tool, GPU profiling, and trace analysis [00:55:31, 00:55:37].
*   **Application Management**: Install apps directly onto the headset [00:55:50, 00:55:54].

## Integration with Unreal Engine
The [[metaquest_developer_hub|Meta Quest Developer Hub]] indirectly supports [[quest_pro_integration_in_unreal_engine_5|Unreal Engine 5]] development by providing the necessary ADB and SDK environment. However, direct "launch on device" from Unreal Engine requires additional setup:
*   **SDK Location**: You will need to configure the Android SDK location within [[quest_pro_integration_in_unreal_engine_5|Unreal Engine 5]]'s Project Settings (Platforms > Android SDK) [01:15:50, 01:16:02].
*   **Android Studio**: Installing Android Studio can help ensure the necessary Android SDK components are present and properly configured for Unreal Engine to build and package projects for Android devices like the Quest Pro [01:20:22, 01:20:27, 01:40:49, 01:43:24].
*   **Packaging Projects**: Even after setting up the SDK, packaging a project for Android (e.g., Android ASTC) may still encounter issues if the SDK isn't found or correctly configured within Unreal Engine [01:11:07, 01:11:12, 01:11:46, 01:11:49].
*   **Plugin Requirement**: Direct headset connection for VR preview in Unreal Engine often depends on having the correct plugins (like Meta XR plugin) installed and enabled within Unreal Engine [01:03:46, 01:03:50, 01:36:18, 01:36:28].

## Troubleshooting Tips
Setting up development environments like this can be complex due to many dependencies and versioning issues [01:49:00, 01:49:17].
*   **Restarting**: Restarting the Unreal Editor after installing plugins or changing settings is often required for changes to take effect [00:43:40, 00:40:40, 00:44:00, 00:44:09, 01:34:34, 01:34:38].
*   **SDK Issues**: Errors like "SDK for Android is not installed properly" indicate missing or incorrectly configured Android SDK components, which often necessitates installing or updating Android Studio and its SDK tools [01:11:46, 01:11:49, 01:40:08, 01:40:43].
*   **Connection Problems**: If the headset isn't detected, double-check USB connections, developer mode settings, and ensure the Oculus app isn't interfering [00:08:06, 01:32:23, 01:32:27].

The ideal future development environment would be a virtualized solution, like a Docker container, to eliminate compatibility and setup complexities [01:49:25, 01:49:44].