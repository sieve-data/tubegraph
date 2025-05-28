---
title: Quest Pro integration in Unreal Engine 5
videoId: xoRnHc_GkAY
---

From: [[hu-po]] <br/> 

Integrating the Quest Pro with Unreal Engine 5 involves several steps, including proper plugin management, project settings configuration, and setting up the Android SDK and developer tools. This process can be challenging due to multiple dependencies and specific version requirements <a class="yt-timestamp" data-t="01:49:08">[01:49:08]</a>.

## Plugin Installation and Management

The initial step involves installing the necessary Oculus Quest integration plugins into Unreal Engine 5 <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

### Process
1.  **Placement**: The Oculus Quest integration plugin files are placed directly into the Epic Games plugin folder <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. This can also be done by dragging and dropping them into the appropriate folder <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.
2.  **Activation**: After placing the files, the Unreal Editor must be restarted for the plugins to be recognized <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
3.  **Enabling Plugins**: Navigate to `Edit > Plugins` <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
    *   Enable **Oculus VR**, **Oculus Subsystem**, and **Oculus Audio** <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>.
    *   Enable relevant **OpenXR** plugins such as **Spatial Anchors**, **Hand Tracking**, **Eye Tracking**, and **Microsoft Hand Interaction** <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
    *   A further restart of Unreal Editor is required after enabling these plugins <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.
    *   A crucial "Meta XR" plugin may also be required, which might not be immediately available or easily found <a class="yt-timestamp" data-t="01:03:48">[01:03:48]</a>.

## Project Settings Configuration

Properly configuring Unreal Engine project settings is essential for Quest Pro development <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.

### Steps
1.  **Map Settings**:
    *   Ensure at least one Unreal Engine level is saved <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
    *   Go to `Edit > Project Settings > Maps & Modes` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
    *   Set both "Editor Startup Map" and "Game Default Map" to the VR template map <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
2.  **Input Settings**:
    *   Under `Engine > Input`, locate the "Mobile" section <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>.
    *   For "Default Touch Interface," select "Clear" to set the value to "None" <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
3.  **Platform Settings (Android)**:
    *   Scroll down to the "Platforms" section and select **Android** <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   Under "APK Packaging," if necessary, click "Configure Now" <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
    *   Accept the SDK license <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>.
    *   Set "Minimum SDK Version" and "Target SDK Version" to `29` <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
    *   Open "Advanced APK Packaging" and hit the plus sign next to "Package for Oculus mobile devices" <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.
4.  **Rendering Settings**:
    *   Under `Engine > Rendering`, find the "Mobile" section <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
    *   Ensure "Mobile MSAA" (Multi-Sample Anti-Aliasing) is set to `4X` <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
    *   In the "VR" section of rendering settings, confirm "Mobile HDR" is turned **off** <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

## Connecting Oculus Quest to a PC for Development

[[connecting_oculus_quest_to_a_pc_for_development | Connecting the Oculus Quest to a PC for development]] requires specific setup, including the Android Debug Bridge (ADB) and the [[metaquest_developer_hub_usage | Meta Quest Developer Hub]].

### Challenges and Solutions
*   **Headset Connection**: Initially, the headset might not connect or be recognized, often showing "not connected" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>. This can be due to:
    *   **Air Link Mode**: If the headset was previously running in Air Link mode, it might prevent a direct USBC connection <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>. Disabling Air Link can resolve this <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.
    *   **Developer Mode**: Developer mode must be enabled on the headset via the companion Meta app <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>, specifically under `Menu > Devices > Quest Pro > Developer Mode` <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>.
    *   **USB Debugging**: Allow USB debugging and "Always allow from this computer" when prompted inside the headset <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.
    *   **Oculus App Status**: Ensure the Oculus app on the PC is running and shows the headset as connected <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.
*   **Android SDK & ADB**:
    *   The [[android_sdk_setup_for_unreal_engine | Android SDK setup for Unreal Engine]] is crucial <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>. This often means installing Android Studio to get the necessary command-line tools and SDK components <a class="yt-timestamp" data-t="01:17:33">[01:17:33]</a>.
    *   Specifically, the "SDK Command Line Tools (latest)" should be installed via Android Studio's SDK Manager <a class="yt-timestamp" data-t="01:43:12">[01:43:12]</a>.
    *   ADB (Android Debug Bridge) is a versatile command-line tool for device communication <a class="yt-timestamp" data-t="00:15:19">[00:15:19]</a>.
    *   Enable ADB over Wi-Fi for wireless debugging, which can be done through the headset's settings once connected via USB <a class="yt-timestamp" data-t="00:56:34">[00:56:34]</a>.
*   **[[metaquest_developer_hub_usage | Metaquest Developer Hub Usage]] (MQDH)**:
    *   MQDH is a standalone companion tool <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a> and is vital for managing device connection, developer mode, and sideloading applications <a class="yt-timestamp" data-t="00:44:50">[00:44:50]</a>.
    *   It allows viewing device logs, recording videos, screenshots, and installing apps <a class="yt-timestamp" data-t="00:55:13">[00:55:13]</a>.
    *   Users must be part of an organization on the Meta developer dashboard to develop Oculus VR apps <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>.
    *   MQDH allows setting the ADB path if multiple ADB clients are detected <a class="yt-timestamp" data-t="00:46:23">[00:46:23]</a>.

## Packaging and Deployment

Direct "VR Preview" in Unreal Engine might be grayed out even with the headset connected <a class="yt-timestamp" data-t="01:00:09">[01:00:09]</a>. An alternative workflow involves packaging the project into an Android Application Package (APK) and then deploying it to the headset.

### Packaging Process
1.  **Project Settings**: Ensure Android platform settings are correctly configured as described above.
2.  **Packaging Option**: In Unreal Engine 5, the "Package Project" option is found under `Platforms > Android > Android (ASTC)` <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.
3.  **SDK Path**: The Unreal Engine requires the correct Android SDK location to be specified in `Project Settings > Platforms > Android SDK` <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>. This often points to the `sdk` folder within the Android Studio installation or a specific resources folder within [[metaquest_developer_hub_usage | Meta Quest Developer Hub]] <a class="yt-timestamp" data-t="01:16:34">[01:16:34]</a>.
4.  **Setup Script**: Running `SetupAndroid.bat` from `Engine/Extras/Android` can help configure the necessary SDK paths <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a>.

### Troubleshooting
*   **SDK Not Installed Properly**: This common error indicates issues with Android SDK paths or missing components <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.
    *   Verify Android Studio components, especially the Command Line Tools, are installed <a class="yt-timestamp" data-t="01:43:12">[01:43:12]</a>.
    *   Manually point Unreal Engine to the correct Android SDK location <a class="yt-timestamp" data-t="01:44:09">[01:44:09]</a>.
*   **Restarting**: Often, restarting Unreal Engine or the computer is necessary after making significant changes to SDK installations or plugin settings <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Overall Challenges

The process of setting up Quest Pro integration in Unreal Engine 5 is often complex due to the "heterogeneity to the different systems" and the need to manage various dependencies and correct versions <a class="yt-timestamp" data-t="01:49:12">[01:49:12]</a>. This makes troubleshooting difficult, as error messages may not clearly indicate the root cause <a class="yt-timestamp" data-t="01:49:14">[01:49:14]</a>. An ideal solution would be a virtualized development environment (like a Docker container) to simplify setup <a class="yt-timestamp" data-t="01:49:25">[01:49:25]</a>.