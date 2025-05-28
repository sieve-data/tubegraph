---
title: Troubleshooting connectivity issues with Oculus Quest Pro
videoId: xoRnHc_GkAY
---

From: [[hu-po]] <br/> 

This article outlines steps and challenges encountered when setting up an Oculus Quest Pro for development with Unreal Engine 5, focusing on common connectivity and configuration issues.

## Initial Unreal Engine 5 Plugin Setup

After placing the [[installing_oculus_quest_integration_in_unreal_engine_5 | Oculus Quest integration]] files into the Epic Games plugin folder <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>, the plugins initially did not load <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Enabling Plugins in Unreal Engine 5
To resolve this, the Unreal Editor had to be restarted <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>. Upon restart, the [[configuring_unreal_engine_5_plugins_for_vr_development | plugins]] loaded successfully <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

It was necessary to enable various Oculus-related plugins, including:
*   Oculus VR <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>
*   Oculus Subsystem <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>
*   Oculus Audio <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>
*   OpenXR Hand Tracking <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>
*   OpenXR Eye Tracking <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>
*   OpenXR Microsoft Hand Interaction <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>

After enabling these, another restart of the Unreal Editor was required <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>. The presence of "Meta XR plugins" was confirmed in UE5 <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>, although the specific "Meta XR plugin" was not found under the plugins menu at a later stage <a class="yt-timestamp" data-t="01:03:48">[01:03:48]</a>.

### Project Settings Configuration
*   **Maps and Modes:** Set both the editor startup and game default maps to the VR template map <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.
*   **Input (Mobile Section):** For "Default Touch Interface," select "Clear" to set the value to "None" <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Platform (Android):**
    *   Set "Minimum SDK Version" to 29 <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
    *   Set "Target SDK Version" to 29 <a class="yt-timestamp" data-t="00:11:50">[00:11:50]</a>.
    *   In the "Advanced APK Packaging" section, click the plus next to "Package for Oculus mobile devices" <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.
*   **Rendering (Mobile Section):**
    *   Ensure "Mobile MSAA" (Multi-Sample Anti-Aliasing) is set to 4X <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
    *   Check "Use Half Precision" <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   **Rendering (VR Section):** Ensure "Mobile HDR" is turned off <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

## Headset Connectivity Issues

Initial attempts to connect the Oculus Quest Pro to the PC via USB and the Oculus app showed a "General device problem not connected" status <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>. The "VR Preview" play button in Unreal Engine remained grayed out <a class="yt-timestamp" data-t="00:33:16">[00:33:16]</a>.

### Resolving Connection via Oculus App
1.  **Disable Air Link:** It was suspected that running in Air Link mode previously prevented USBC connection <a class="yt-timestamp" data-t="00:19:54">[00:19:54]</a>.
2.  **Launch Quest Link:** Launching Quest Link within the Oculus Quest headset was necessary to establish a connection <a class="yt-timestamp" data-t="00:24:08">[00:24:08]</a>. After this, the device showed as connected in the Oculus app <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>.

## Android SDK and ADB Setup

The Unreal Engine indicated that the SDK for Android was not installed properly <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>.

### Downloading and Installing Android SDK
1.  **Download Command Line Tools:** The "Windows command line tools only" version of the Android SDK was downloaded <a class="yt-timestamp" data-t="01:18:03">[01:18:03]</a>, which includes ADB (Android Debug Bridge) <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>.
2.  **Install Android Studio:** Despite attempting to avoid a full IDE <a class="yt-timestamp" data-t="01:18:11">[01:18:11]</a>, installing Android Studio was pursued as a way to ensure the SDK was properly installed <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>.
3.  **SDK Manager:** Within Android Studio, the "SDK Manager" (accessible via Help -> Windows -> SDK Manager <a class="yt-timestamp" data-t="01:42:50">[01:42:50]</a>) was used to check the box for "SDK Command Line Tools" (latest version) and apply the changes <a class="yt-timestamp" data-t="01:43:12">[01:43:12]</a>.

### Configuring ADB Path in Unreal Engine
To set the [[setting_up_android_sdk_for_oculus_quest_development | Android SDK]] path in Unreal Engine:
1.  Navigate to Project Settings -> Platforms -> Android SDK <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>.
2.  Locate the `SetupAndroid.bat` file within the Unreal Engine installation directory (e.g., `C:\Program Files\Epic Games\UE_X.X\Engine\Extras\Android`) and run it <a class="yt-timestamp" data-t="01:46:05">[01:46:05]</a>. This batch file aims to set up the Android development environment <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a>.

## Meta Quest Developer Hub (MQDH)

The [[meta_quest_developer_hub_for_managing_vr_apps | Meta Quest Developer Hub]] (MQDH) is a standalone companion tool <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>.

### MQDH Installation and Setup
1.  **Download MQDH:** The MQDH application was downloaded and installed <a class="yt-timestamp" data-t="00:39:49">[00:39:49]</a>.
2.  **Log in:** Log in with a Meta account <a class="yt-timestamp" data-t="00:44:59">[00:44:59]</a>.
3.  **Create Organization:** A developer account must be a member of an organization to develop Oculus VR apps <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>. A new organization, "Booboo verse," was created on the developer dashboard <a class="yt-timestamp" data-t="00:38:08">[00:38:08]</a>.
4.  **ADB Client Detection:** MQDH can detect existing ADB clients <a class="yt-timestamp" data-t="00:45:24">[00:45:24]</a> and allows specifying the ADB client path <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>.

### Device Manager in MQDH
The device manager in MQDH allows for:
*   Setting up a new device <a class="yt-timestamp" data-t="00:47:49">[00:47:49]</a>.
*   Enabling Bluetooth on the computer <a class="yt-timestamp" data-t="00:47:57">[00:47:57]</a>.
*   Enabling developer mode in the companion app <a class="yt-timestamp" data-t="00:48:00">[00:48:00]</a>.
*   Plugging the headset into the computer <a class="yt-timestamp" data-t="00:48:05">[00:48:05]</a>.

Once the device is connected, MQDH displays logs <a class="yt-timestamp" data-t="00:58:13">[00:58:13]</a> and allows enabling ADB over Wi-Fi, enabling wireless debugging after initial USB connection <a class="yt-timestamp" data-t="00:57:29">[00:57:29]</a>.

## Enabling Developer Mode on Quest Pro
To enable developer mode:
1.  On the Meta Quest companion app (on phone/PC), navigate to Menu -> Devices <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>.
2.  Select the connected Quest Pro device <a class="yt-timestamp" data-t="00:54:12">[00:54:12]</a>.
3.  Scroll down to "Developer Mode" and turn it on <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>.
4.  Put on the headset and allow USB debugging access from the connected computer, checking "Always allow from this computer" <a class="yt-timestamp" data-t="00:54:25">[00:54:25]</a>.

## Packaging and Deploying the Project

Attempting to package the project via `Platforms -> Android -> Android ASTC -> Package Project` in Unreal Engine resulted in an error stating the "SDK for Android is not installed properly" <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>. Even after installing Android Studio and configuring the SDK tools, the packaging process continued to fail with messages like "System cannot find the PATH specified" <a class="yt-timestamp" data-t="01:48:25">[01:48:25]</a>.

### Challenges Encountered
The process of setting up the environment for Unreal Engine 5 and Oculus Quest Pro development proved to be complex due to:
*   Dealing with various dependencies and their correct versions <a class="yt-timestamp" data-t="01:49:05">[01:49:05]</a>.
*   Difficulty in pinpointing the exact cause of errors due to the "heterogeneity of the different systems" <a class="yt-timestamp" data-t="01:49:17">[01:49:17]</a>.
*   The desire for a virtualized development environment (like Docker) to simplify setup <a class="yt-timestamp" data-t="01:49:25">[01:49:25]</a>.

The ultimate goal was to get a project working for actual game development and eventually integrate neural radiance fields into Unreal Engine <a class="yt-timestamp" data-t="01:49:52">[01:49:52]</a>.