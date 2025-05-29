---
title: Transitioning from 43 to 169 layout in OBS
videoId: 4t76td7JdpA
---

From: [[humblelifeskills]] <br/> 

Converting an existing 4:3 profile in OBS to a 16:9 aspect ratio involves significant adjustments to settings, scenes, and assets. While the process of learning to use OBS itself is relatively straightforward, the real work lies in [[building_and_adjusting_scene_assets_in_obs | building and adjusting scene assets]] to fit the new dimensions <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This can be a time-consuming and granular process, akin to "pixel pushing" <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.

## Initial Setup and Duplication

Before making significant changes, it's best practice to duplicate your existing OBS profile and scene collection <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This ensures that any modifications made for the 16:9 layout do not affect your original 4:3 setup <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.

### Duplicating Profiles and Scene Collections
1.  **Duplicate Profile:** Go to "Profile" and select "Duplicate" <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Name the new profile (e.g., "16x9") <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.
2.  **Duplicate Scene Collection:** Go to "Scene Collection" and select "Duplicate" <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Name this new collection accordingly <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>.
3.  **Verify Selection:** Ensure you are working on the newly duplicated 16:9 profile and scene collection <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

## Adjusting Core Video Settings

The fundamental step is to change the base canvas and output resolution within OBS settings to reflect the 16:9 aspect ratio <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

1.  **Access Video Settings:** Navigate to `Settings` > `Video` <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
2.  **Base (Canvas) Resolution:** Change the `Base (Canvas) Resolution` to 1920x1080 (HD) <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
3.  **Output (Scaled) Resolution:** Change the `Output (Scaled) Resolution` to 1920x1080 <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.
4.  **Common FPS Values:** Consider adjusting the frame rate. For older machines, 30 frames per second (fps) might be more manageable than higher rates like 60 fps, as higher resolutions push more pixels and demand more from your machine <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
5.  **Apply Changes:** Click `Apply` <a class="yt-timestamp" data-t="00:02:14">[00:02:14]</a>.

After applying, the stage will switch to the 16:9 perspective, appearing more horizontal or rectangular compared to the previous square 4:3 look <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. You can switch back to the 4:3 profile to confirm the changes are only applied to the new 16:9 profile <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Adjusting Scenes and Assets

With the canvas size updated, individual scenes and their contained assets will need to be reconfigured to fill the new 16:9 space effectively <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Intros and Outros
Original 1000x1000 pixel intros will appear small on a 1920x1080 canvas, as the content is now centered with a lot of empty space around it <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Resizing/Re-animating:** You will likely need to create brand new animations or redesign existing ones to properly fill the 16:9 space <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>. This allows for more creative use of the expanded screen real estate <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. The same applies to outro scenes <a class="yt-timestamp" data-t="00:04:14">[00:04:14]</a>.

### General Layouts and Master Scenes
All layouts will require changes <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. Master scenes might need to be stretched to 1920x1080 <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. Assets themselves might only need to be moved to the middle of the new canvas, though additional space can be used for new elements <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

### Step-by-Step Scene Adjustment (Example: "Steam Glider")
1.  **Unlock and Stretch Bottom Bar:** Unlock the bottom bar asset and stretch it horizontally to fill the new 16:9 width <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Use the `Alt` key while dragging to adjust the perspective and ensure it aligns with the 16:9 shot <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
2.  **Reposition Elements:**
    *   **Text:** Unlock text elements and move them to suitable positions <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
    *   **Dividers:** Reposition divider elements <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
    *   **QR Code:** Make elements like QR codes larger to take advantage of the increased screen real estate, making them easier to scan for viewers <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
3.  **Utilize New Space:** Consider how to use the additional horizontal space.
    *   **Video Blocks:** Add new "video blocks" <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.
    *   **Desktop/Application Capture:** Integrate a display or window capture to show your desktop, a notepad, or a browser (like Opera) <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. This might require a second monitor for optimal setup <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
    *   **Animated Call to Actions:** Convert static text areas into cycling animations for calls to action <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
4.  **Text Formatting:**
    *   **Font Size:** Font choices that were good for 4:3 might not scale well. Adjust font sizes or consider multi-line text to fill horizontal space <a class="yt-timestamp" data-t="00:08:46">[00:08:46]</a>.
    *   **Read from File:** For dynamic text that changes frequently (e.g., topics), use the "Read from file" option in text sources <a class="yt-timestamp" data-t="00:14:19">[00:14:19]</a>. This allows you to update text by simply editing a text file on your machine, rather than directly in OBS, which can be useful if you're nervous about making mistakes in the software <a class="yt-timestamp" data-t="00:14:23">[00:14:23]</a>. Ensure you know the maximum character count per line to avoid text going off-screen <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
5.  **Camera and Mic Placement:** The camera and microphone sources themselves might not change, but their placement within the new 16:9 layout will need adjustment to fit the new scene composition <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. You can resize and reposition the camera feed <a class="yt-timestamp" data-t="00:16:14">[00:16:14]</a>.
6.  **Lock Layers:** Always lock layers after positioning them to prevent accidental movement when adjusting other elements <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. This is particularly important with layered assets <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>.
7.  **Remove Obsolete Elements:** If your new design doesn't require certain elements from the 4:3 layout, remove them <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

## Challenges and Considerations

*   **Operating System Compatibility:** Specific OBS features like `Window Capture` or `Display Capture` might have issues or bugs depending on your operating system version (e.g., macOS Catalina) <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. Workarounds might be needed, such as ensuring applications are visible on screen for window capture to work <a class="yt-timestamp" data-t="00:11:07">[00:11:07]</a>.
*   **Second Screen:** Using a second screen can greatly assist in capturing desktop or browser content for integration into OBS scenes <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   **Iterative Design:** Be prepared to spend time tinkering and experimenting with different layouts and stylings to achieve a visually appealing and fresh look for each scene <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>. This allows for diverse content without feeling like a repeated template <a class="yt-timestamp" data-t="00:17:25">[00:17:25]</a>.

Once all intros, outros, and main scene layouts are adjusted, your OBS setup will be ready for 16:9 content, suitable for platforms like YouTube or for live streaming <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.