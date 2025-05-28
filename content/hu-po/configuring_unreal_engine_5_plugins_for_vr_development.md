---
title: Configuring Unreal Engine 5 plugins for VR development
videoId: xoRnHc_GkAY
---

From: [[hu-po]] <br/> 

Configuring [[installing_oculus_quest_integration_in_unreal_engine_5 | Oculus Quest integration]] within Unreal Engine 5 for virtual reality (VR) [[game_development_using_unreal_engine_5 | game development]] involves several steps, from loading plugins to setting up project settings and external tools like the Android SDK and [[meta_quest_developer_hub_for_managing_vr_apps | Meta Quest Developer Hub]].

## Initial Plugin Integration

To begin, the Oculus Quest integration plugin was manually placed into the `epic games plugin folder` <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>. After this, Unreal Engine needs to be restarted for the newly added plugins to be recognized <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>, <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.

Once restarted, the following Oculus and XR-related plugins were enabled through `Edit > Plugins`:
*   Oculus VR <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>
*   Oculus Subsystem <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>
*   Oculus Audio <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>
*   Mixed Reality Capture Framework <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>
*   OpenXR <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>
*   OpenXR Hand Tracking <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>
*   OpenXR Eye Tracking <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>
*   OpenXR Microsoft Hand Interaction <a class="yt-timestamp" data-t="00:06:32">[00:06:32]</a>

After enabling these, another restart of the Unreal Editor was required <a class="yt-timestamp" data-t="00:06:45">[00:06:45]</a>.

## Project Settings Configuration

Configuring project settings is crucial for VR development. These settings are accessed via `Edit > Project Settings`.

### Maps and Modes
Both the editor startup and game default maps were set to the VR template map <a class="yt-timestamp" data-t="00:08:54">[00:08:54]</a>.

### Input
Under `Engine > Input`, the `Default Touch Interface` in the `Mobile` section was set to `None` <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.

### Platforms - Android
Since Oculus Quest devices run on Android, specific Android platform settings need to be configured:
*   Navigate to `Platforms > Android` <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>.
*   Set `Minimum SDK Version` and `Target SDK Version` to `29` <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>.
*   In the `Advanced APK Packaging` section, ensure `Package for Oculus mobile devices` is enabled <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

### Rendering
Under `Engine > Rendering`:
*   In the `Mobile` section, set `Mobile MSAA` (Multi-Sample Anti-Aliasing) to `4X` <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   Enable `Use Half Precision` <a class="yt-timestamp" data-t="00:14:10">[00:14:10]</a>.
*   In the `VR` section, ensure `Mobile HDR` is turned `Off` <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

## Headset Connection and Developer Setup

Connecting the Oculus Quest Pro headset to the development PC and preparing it for deployment involves several external tools and device settings.

### Oculus App and Developer Mode
The Oculus desktop application is used to manage device connections <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. Initially, the headset showed as "not connected" <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>, often due to Air Link mode preventing USB connection <a class="yt-timestamp" data-t="00:19:56">[00:19:56]</a>.

To enable development, the Oculus account linked to the headset needs to be part of an "organization" <a class="yt-timestamp" data-t="00:37:31">[00:37:31]</a>. This requires logging into the Meta developer dashboard and creating an organization (e.g., "Booboo verse") <a class="yt-timestamp" data-t="00:38:10">[00:38:10]</a>, <a class="yt-timestamp" data-t="00:38:43">[00:38:43]</a>.

On the headset itself, Developer Mode must be enabled. This is done through the Meta Quest mobile app: `Menu > Devices > Select Quest Pro > Developer Mode > Turn On` <a class="yt-timestamp" data-t="00:53:52">[00:53:52]</a>, <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>. When connecting the headset via USB, allow access from the computer and `Always allow from this computer` <a class="yt-timestamp" data-t="00:54:40">[00:54:40]</a>.

### Android SDK and ADB
For deploying applications to Android-based VR headsets, the Android SDK is necessary. This includes the Android Debug Bridge (ADB), a command-line tool for communicating with Android devices <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

The full Android Studio IDE can be downloaded, which includes the SDK <a class="yt-timestamp" data-t="00:17:33">[00:17:33]</a>, <a class="yt-timestamp" data-t="01:20:22">[01:20:22]</a>. After installation, within Android Studio's `SDK Manager` (`Configure > SDK Manager`), ensure `SDK Command-line Tools` is checked and applied <a class="yt-timestamp" data-t="01:42:50">[01:42:50]</a>.

Unreal Engine requires the correct path to the Android SDK. This can be set in `Project Settings > Platforms > Android SDK` <a class="yt-timestamp" data-t="01:15:50">[01:15:50]</a>. A batch file (`SetupAndroid.bat`) located in `Epic Games\UE_5.x\Engine\Extras\Android` may need to be run to configure the environment <a class="yt-timestamp" data-t="01:47:08">[01:47:08]</a>.

### Meta Quest Developer Hub (MQDH)
The [[meta_quest_developer_hub_for_managing_vr_apps | Meta Quest Developer Hub]] (MQDH) is a standalone companion tool designed to manage development for Meta Quest devices <a class="yt-timestamp" data-t="00:39:11">[00:39:11]</a>, <a class="yt-timestamp" data-t="00:39:46">[00:39:46]</a>. MQDH provides features such as device manager, app installation, ADB over Wi-Fi, and real-time device logs <a class="yt-timestamp" data-t="00:55:13">[00:55:13]</a>, <a class="yt-timestamp" data-t="00:57:38">[00:57:38]</a>.

## Packaging and Deployment Challenges

Even with plugins loaded and SDKs installed, challenges can arise in packaging projects for VR devices. The option to `Package Project` is found under `Platforms > Android > Android (ASTC)` <a class="yt-timestamp" data-t="01:11:00">[01:11:00]</a>, not directly in the `File` menu as in older Unreal Engine versions <a class="yt-timestamp" data-t="01:09:56">[01:09:56]</a>.

Common issues include:
*   **"SDK for Android is not installed properly"** <a class="yt-timestamp" data-t="01:11:46">[01:11:46]</a>: This typically indicates incorrect paths or missing components of the Android SDK.
*   **VR Preview Grayed Out**: This means the Head-Mounted Display (HMD) is not detected or properly connected/configured <a class="yt-timestamp" data-t="01:00:12">[01:00:12]</a>.

The process of setting up these environments can be complex due to the varying versions of software, dependencies, and system heterogeneity <a class="yt-timestamp" data-t="01:49:05">[01:49:05]</a>. Ideally, a virtualized development environment could streamline this by providing all necessary components in a pre-configured state <a class="yt-timestamp" data-t="01:49:30">[01:49:30]</a>.