---
title: Methods to enhance audio volume during recording
videoId: RTE-pSwaDe4
---

From: [[dr_tutoriales]] <br/> 

Increasing microphone volume can facilitate subsequent editing and improve clarity for subscribers and listeners during streaming or other platforms <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

## Method 1: Adjusting Volume via Windows Sound Settings

This method allows users to [[how_to_increase_microphone_volume_on_windows_10 | How to increase microphone volume on Windows 10]] directly through the operating system's settings.

### Steps to Adjust Volume in Windows 10 <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>

1.  **Access Sound Settings**: Go to the Start taskbar and type "sound" <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. Select "Sound settings" <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This is part of [[adjusting_sound_settings_for_microphones | adjusting sound settings for microphones]].
2.  **Navigate to Input**: In the sound settings, go to the "Input" section, not "Output" (which controls speakers) <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.
3.  **Select Microphone**: Ensure the desired microphone is selected <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. The audio volume bar should increase as sound is detected <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.
4.  **Open Device Properties**: Click on "Properties of the device" <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This utilizes [[using_device_properties_to_manage_microphone_settings | device properties to manage microphone settings]].
5.  **Adjust Microphone Volume**:
    *   The microphone volume can be set up to 100% <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>. This is generally the maximum volume a microphone can capture without reducing sound quality <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
    *   If the volume is increased beyond this standard, the sound quality may decrease considerably <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This demonstrates the [[impact_of_increasing_microphone_volume_on_audio_quality | Impact of increasing microphone volume on audio quality]].

### Alternative for Older Windows Versions <a class="yt-timestamp" data-t="00:01:55">[00:01:55]</a>

For computers not running Windows 10, a different window may appear <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. In this scenario:

1.  Go to the "Levels" section <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
2.  The microphone volume can be set to 100% here <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.
3.  Click "Apply" to confirm changes <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

## Method 2: Using OBS Studio for Volume Control

[[using_obs_studio_for_screen_recording | OBS Studio]] is a program that facilitates recording videos at desired volumes <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>, which can then be modified or converted to audio format <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. It is particularly useful for passing audio at higher volumes <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

### Steps to Adjust Volume in OBS Studio <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>

1.  **Select Microphone**: Go to the "Microphones and Auxiliaries" section <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
2.  **Properties**: Click "Settings" then "Properties" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a> and choose the microphone to be used <a class="yt-timestamp" data-t="00:03:04">[00:03:04]</a>.
3.  **Advanced Audio Properties**:
    *   Go to the "Audio Mixer" window <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.
    *   Right-click and select "Advanced Audio Properties" <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
4.  **Adjust Microphone Volume**:
    *   This window displays different microphones or audio sources interacting in the recording <a class="yt-timestamp" data-t="00:03:24">[00:03:24]</a>.
    *   The standard volume is typically 0.0 decibels <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>.
    *   The volume can be progressively increased <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

:::caution
Increasing the volume in OBS Studio beyond the standard level is a technique that increases volume but can reduce the [[impact_of_increasing_microphone_volume_on_audio_quality | quality of the audio]], making it sound "a little worse but higher" <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. This should be kept in mind <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>.
:::