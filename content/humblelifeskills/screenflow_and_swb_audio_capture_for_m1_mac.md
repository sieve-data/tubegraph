---
title: Screenflow and SWB Audio Capture for M1 Mac
videoId: -A9gr361ARE
---

From: [[humblelifeskills]] <br/> 

For users looking to capture virtual audio on their Mac, especially with Big Sur or an M1 Mac in 2021, and who are operating on a budget without hardware solutions, software options are available <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This article discusses current recommendations for capturing system-wide audio.

## Challenges with Older Audio Capture Solutions

Previously, [[alternatives_to_soundflower_for_audio_capture | Soundflower]], an open-source kernel extension, was a common choice for virtual audio capture <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. However, due to continuous changes in how macOS handles and captures audio across different operating system versions, Soundflower became buggy <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>. The project officially ended in 2015 <a class="yt-timestamp" data-t="00:00:42">[00:00:42]</a>.

Other alternatives exist, such as Rogue Amoeba's Loopback, which is graphically intuitive but can be expensive <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. While powerful for routing audio from various applications and games <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>, its cost might lead users to consider a hardware solution instead <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. Rogue Amoeba is known for making excellent Mac audio software, particularly for podcasting <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.

Another utility, [[IShowU Audio Capture and its features | IShowU Audio Capture]], emerged when Soundflower became unreliable <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. However, its driver proved difficult to find and required specific installers for different macOS versions like Catalina, indicating ongoing compatibility issues with core audio changes <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

## Recommended Solution: IShowU Instant (ScreenFlow) with SWB Audio Capture

The company behind the original [[IShowU Audio Capture and its features | IShowU Audio Capture]] also develops [[automating_video_editing_with_screenflow | screen capture software]] <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>. Their latest screen recorder, IShowU Instant (sometimes referred to as [[automating_video_editing_with_screenflow | ScreenFlow]] in the context of general screen recording), is recommended as it is Big Sur and M1-ready <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>. It provides native Apple M1 support, leading to better system resource utilization and potentially higher FPS capture <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.

### Key Benefits

*   **Integrated Audio Driver:** Purchasing IShowU Instant not only provides a screen capture utility but also automatically installs the necessary audio driver <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>.
*   **SWB Audio Capture:** This driver, which appears as "swb shiny white box audio capture" in your Mac's audio settings <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>, enables the capture of virtual audio—such as game audio, music, and background Mac audio—and routing it into applications like Zoom, Microsoft Meet, or OBS <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Cost-Effective:** The software is affordably priced at around $24 <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. While the audio driver might be found for free, the bundle offers significant value <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Advanced Features Version:** An additional $15 upgrade offers features like capturing from iOS devices (iPad or iPhone via Lightning cable) and multi-channel audio support <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>. This allows routing various audio sources simultaneously during screen capture <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

### IShowU Instant Features and Interface

IShowU Instant presents a straightforward layout with presets on the left side and sections for video, audio, and timer settings <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

Key features include:

*   **Presets:** Users can create different presets for various scenarios, such as local recording, gaming, or direct YouTube uploads <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.
*   **Custom Input Rate:** The ability to set a custom input frame rate up to 60fps or potentially higher, which is beneficial for capturing games <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Audio Features:**
    *   **Compressor:** Prevents audio distortion by limiting volume peaks, ensuring consistent levels even when shouting <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>.
    *   **Graphic EQ:** Provides equalization controls for audio <a class="yt-timestamp" data-t="00:05:38">[00:05:38]</a>.
*   **Visuals:**
    *   **Webcam Control:** Reposition the webcam feed on the screen, toggle its visibility, or zoom it in/out during recording with hotkeys <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>.
    *   **On-screen Indicators:** Visualize key presses, show modifier keys, and even add click sounds <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
    *   **Watermarks & Backgrounds:** Include text watermarks or change the background <a class="yt-timestamp" data-t="00:06:15">[00:06:15]</a>.
*   **Output Options:** Set output frame rates to match input rates <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a> and share recordings directly to messages or YouTube <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.

The SWB audio driver automatically installs upon product installation and appears in the Mac's sound drop-down menu, allowing it to be selected as an audio device in other software like OBS <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>.

In conclusion, for those using Big Sur or an M1 Mac, IShowU Instant provides a reliable, up-to-date solution for [[capturing_systemwide_audio_on_mac | capturing systemwide audio on Mac]] and screen recording, avoiding the issues associated with older tools like [[alternatives_to_soundflower_for_audio_capture | Soundflower]] <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.