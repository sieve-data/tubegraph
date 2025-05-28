---
title: Connecting Oculus Quest to a PC for development
videoId: xoRnHc_GkAY
---

From: [[hu-po]] <br/> 

Developing for the Meta Quest platform using Unreal Engine requires careful configuration of both the Unreal Engine project and the development PC, as well as proper connection and setup of the Meta Quest headset. This guide outlines the steps and common troubleshooting points encountered during the setup process.

## 1. Unreal Engine Plugin Management

To enable Meta Quest (formerly Oculus Quest) development within Unreal Engine, the necessary plugins must be integrated and activated.

### Plugin Installation
1.  **Placement**: The Oculus Quest integration plugin (or Meta XR plugins) should be placed into the Unreal Engine's plugin folder, typically located within the Epic Games installation directory <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.
2.  **Activation**:
    *   After placing the plugin, restart the Unreal Engine editor <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.
    *   Navigate to `Edit > Plugins` within Unreal Engine <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
    *   Search for "Oculus" or "Meta XR" <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a> <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   Enable all relevant plugins:
        *   Oculus VR <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>
        *   Oculus subsystem <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>
        *   Oculus audio <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>
        *   OpenXR spatial anchors <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>
        *   OpenXR hand tracking <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>
        *   OpenXR eye tracking <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>
        *   OpenXR Microsoft hand interaction <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>
    *   A second restart of Unreal Engine may be required after enabling plugins <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## 2. Unreal Engine Project Settings Configuration

Specific project settings must be adjusted to correctly target the Meta Quest platform for development.

### Maps and Modes
1.  Go to `Edit > Project Settings > Maps and Modes` <a class="yt-timestamp" data-t="00:08:37">[00:08:37]</a>.
2.  Set both the `Editor Startup Map` and the `Game Default Map` to your desired VR level, such as the VR template map <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

### Engine Input Settings
1.  Navigate to `Edit > Project Settings > Engine > Input` <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>.
2.  Under the `Mobile` section, set `Default Touch Interface` to `Clear` (or `None`) <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

### Android Platform Settings
1.  In `Edit > Project Settings`, scroll down to `Platforms` and select `Android` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
    *   *Note*: Hololens is listed as a separate platform target <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>.
2.  Set `Minimum SDK Version` to 29 <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
3.  Set `Target SDK Version` to 29 <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
4.  Expand `Advanced APK Packaging` and add `For Oculus Mobile Devices` <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>.

### Rendering Settings for VR
1.  In `Edit > Project Settings`, under the `Engine` section, select `Rendering` <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.
2.  Under the `Mobile` sub-section, ensure `Mobile MSAA` (multi-sample anti-aliasing) is set to `4X` <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
3.  Under the `VR` sub-section, ensure `Mobile HDR` is turned `Off` <a class="yt-timestamp" data-t="00:14:15">[00:14:15]</a>.

## 3. Connecting the Meta Quest Headset

Establishing a connection between your PC and the Meta Quest headset is crucial for deploying and testing applications.

### Physical Connection
1.  Connect your headset to the development PC via a USB-C cable <a class="yt-timestamp" data-t="00:07:40">[00:07:40]</a> <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
2.  Ensure Air Link is not running, as it can prevent USB-C connections from being recognized <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.

### Developer Mode and USB Debugging
1.  **Meta Quest Developer Account**: You need to create a new organization under the developer dashboard on the Meta developer website <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>. For example, the organization name "Booboo verse" was used <a class="yt-timestamp" data-t="00:38:43">[00:38:43]</a>.
2.  **Enable Developer Mode**:
    *   Open the Meta Quest mobile app (or Oculus app) on your phone <a class="yt-timestamp" data-t="00:53:55">[00:53:55]</a>.
    *   Go to `Menu > Devices` <a class="yt-timestamp" data-t="00:54:09">[00:54:09]</a>.
    *   Select your Meta Quest Pro (or Quest headset) <a class="yt-timestamp" data-t="00:54:13">[00:54:13]</a>.
    *   Scroll down to `Developer Mode` and turn it `On` <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>.
3.  **Allow USB Debugging**: Put on your headset and accept any prompts to "Allow access to data" <a class="yt-timestamp" data-t="00:54:25">[00:54:25]</a> and "Always allow from this computer" <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.

## 4. Android SDK and ADB Setup

Proper installation of the Android SDK and Android Debug Bridge (ADB) is critical for Unreal Engine to communicate with and deploy applications to the Meta Quest.

### Android SDK Command Line Tools
1.  **Download**: Download the `command line tools only` version of the Android SDK from the Android developer website <a class="yt-timestamp" data-t="01:17:54">[01:17:54]</a> <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>.
2.  **Extract**: Extract the downloaded zip file to a preferred location (e.g., `downloads` folder) <a class="yt-timestamp" data-t="00:20:16">[00:20:16]</a>.
3.  **Configure Unreal Engine paths**: The system cannot find the PATH specified errors may indicate incorrect SDK paths in Unreal Engine. Manual configuration may be required <a class="yt-timestamp" data-t="01:44:09">[01:44:09]</a>.

### Android Studio (for SDK management)
While a full IDE, Android Studio includes the necessary SDK Manager to manage components.
1.  **Download and Install**: Download and install Android Studio <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>.
2.  **SDK Manager**:
    *   Open Android Studio <a class="yt-timestamp" data-t="01:40:49">[01:40:49]</a>.
    *   Go to `Configure > SDK Manager` (or `File > Settings > Appearance & Behavior > System Settings > Android SDK`) <a class="yt-timestamp" data-t="01:41:47">[01:41:47]</a>.
    *   In the `SDK Tools` tab, ensure `Android SDK Command-line Tools (latest)` is checked <a class="yt-timestamp" data-t="01:43:12">[01:43:12]</a>.
    *   Click `Apply` to download and install these components <a class="yt-timestamp" data-t="01:43:24">[01:43:24]</a>.
    *   A computer restart might be needed <a class="yt-timestamp" data-t="01:43:42">[01:43:42]</a>.

### Setting up Android Build Environment (Optional but Recommended)
1.  Navigate to `C:\Program Files\Epic Games\UE_5.0\Engine\Extras\Android` (or your Unreal Engine installation path) <a class="yt-timestamp" data-t="01:46:05">[01:46:05]</a>.
2.  Run `setup_android.bat` <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a>. This batch file helps configure the Android build environment for Unreal Engine <a class="yt-timestamp" data-t="01:47:41">[01:47:41]</a>.

## 5. Meta Quest Developer Hub (MQDH) Usage

The [[metaquest_developer_hub_usage | Meta Quest Developer Hub]] (`MQDH`) is a standalone companion tool that aids in managing devices and development workflows.
1.  **Download and Install**: Download and install the MQDH from the Meta developer website <a class="yt-timestamp" data-t="00:39:42">[00:39:42]</a> <a class="yt-timestamp" data-t="00:40:06">[00:40:06]</a>.
2.  **Log In**: Log in with your Meta account <a class="yt-timestamp" data-t="00:44:59">[00:44:59]</a>.
3.  **ADB Path**: MQDH can detect existing ADB clients or you can specify the ADB client path <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>.
4.  **Device Manager**:
    *   Use the `Device Manager` in MQDH to set up a new device <a class="yt-timestamp" data-t="00:47:49">[00:47:49]</a>.
    *   Ensure Bluetooth is enabled and developer mode is active in the companion app <a class="yt-timestamp" data-t="00:47:57">[00:47:57]</a>.
    *   Plug the headset into the computer <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.
    *   Verify the device status in MQDH <a class="yt-timestamp" data-t="00:50:38">[00:50:38]</a>.
5.  **ADB over Wi-Fi**: Activate `ADB over Wi-Fi` in MQDH once the device is connected via USB, allowing for wireless debugging and deployment after initial setup <a class="yt-timestamp" data-t="00:56:34">[00:56:34]</a> <a class="yt-timestamp" data-t="00:57:29">[00:57:29]</a>.
6.  **Device Logs**: MQDH can display real-time logs from the headset, which is useful for debugging <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a>.

## 6. Packaging and Deployment

Once all configurations are in place, the Unreal Engine project can be packaged for the Meta Quest and deployed.

### Packaging
1.  In Unreal Engine, go to `Platforms > Android` <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>.
2.  Select `Android (ASTC)` <a class="yt-timestamp" data-t="01:05:22">[01:05:22]</a>.
3.  Choose a destination folder for the packaged APK <a class="yt-timestamp" data-t="01:13:02">[01:13:02]</a>.
4.  If the Android SDK is not installed properly, an error will occur, requiring further configuration of the SDK paths <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.

### Deployment
*   The ideal workflow involves building the application (packaging it) and then deploying it to the headset <a class="yt-timestamp" data-t="01:06:01">[01:06:01]</a>.
*   The "Launch On" menu in Unreal Engine (accessible via the arrow beside the launch icon) should ideally show connected devices <a class="yt-timestamp" data-t="02:22:34">[02:22:34]</a>.

## 7. Troubleshooting Common Issues

Setting up the development environment can be complex due to numerous dependencies and versions.

### "VR Preview" Grayed Out
*   If the "VR Preview" option in Unreal Engine is grayed out <a class="yt-timestamp" data-t="00:33:16">[00:33:16]</a>, it typically means the HMD (head-mounted display) is not properly connected or recognized.
*   Ensure all setup steps, including plugin activation and developer mode on the headset, are completed <a class="yt-timestamp" data-t="00:33:30">[00:33:30]</a>.
*   Verify the Oculus runtime is installed <a class="yt-timestamp" data-t="00:33:47">[00:33:47]</a>.

### "SDK for Android is not installed properly"
*   This error means Unreal Engine cannot locate or validate the Android SDK installation <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.
*   Ensure Android Studio (or the command line tools) is fully installed and its SDK components are downloaded <a class="yt-timestamp" data-t="01:22:29">[01:22:29]</a>.
*   Verify the SDK path is correctly set in Unreal Engine's `Project Settings > Platforms > Android SDK` <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>.
*   Running `setup_android.bat` can often resolve path issues <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a>.

### Headset Not Detected
*   Check the physical USB connection <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a> <a class="yt-timestamp" data-t="00:32:23">[00:32:23]</a>.
*   Ensure developer mode and USB debugging are enabled on the headset and accepted via the headset prompts <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.
*   Close any conflicting software like Air Link <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.
*   Reconnecting the USB cable or restarting the PC and headset can sometimes resolve connection issues <a class="yt-timestamp" data-t="01:27:54">[01:27:54]</a>.

## Future Development
The ultimate goal is to integrate advanced technologies like neural radiance fields into Unreal Engine for AR/VR applications <a class="yt-timestamp" data-t="01:49:55">[01:49:55]</a>. This requires a stable development environment and a solid understanding of [[hardware_for_ai_training_and_deployment | hardware for AI training and deployment]] and [[vision_language_connectors_and_architectures | vision language connectors and architectures]]. The complexity of setting up these environments highlights the need for solutions like [[docker_usage_in_development | Docker usage in development]] to streamline dependency management <a class="yt-timestamp" data-t="01:49:25">[01:49:25]</a>.