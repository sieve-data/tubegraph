---
title: Building and adjusting scene assets in OBS
videoId: 4t76td7JdpA
---

From: [[humblelifeskills]] <br/> 

The real work in OBS goes into building the assets – the small elements that make up your scenes and sources, which can take significant time to perfect <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. This includes animations, 3D looks, and layered images <a class="yt-timestamp" data-t="00:00:56">[00:00:56]</a>. Learning how to operate OBS is relatively straightforward; the complexity lies in asset creation <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Converting from 4:3 to 16:9 Layout

To begin [[transitioning_from_43_to_169_layout_in_obs | transitioning from a 4:3 to 16:9 layout in OBS]], the first step is to create copies of your existing profiles and scene collections <a class="yt-timestamp" data-t="00:01:14">[00:01:14]</a>. This is done by [[duplicating_profiles_and_scene_collections_in_obs | duplicating the profile]] and naming the copy, for example, "sixteen by nine" <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. A scene collection copy also needs to be made and verified to ensure that any changes made will not affect the original 4:3 version <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

### Adjusting Video Settings

Once copies are made, navigate to OBS settings and change the video output <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>:
*   Set the **base canvas** to 1920x1080 (HD resolution) <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
*   Adjust the **frame rate** to 30 frames per second (FPS), especially if [[using_obs_with_older_machines | using OBS with older machines]] that may struggle with higher resolutions and frame rates <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. Higher resolutions push more pixels, demanding more from the machine <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

After applying these changes, the stage will shift to a 16:9 perspective, appearing more horizontal or rectangular <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. You can confirm the change by switching back to the 4:3 profile to see it jump back to the square layout <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

## Scene and Asset Adjustments

Transitioning to 16:9 means many existing scene elements will need significant adjustments due to the increased screen real estate <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

### Intros and Outros
Existing intros and outros, which might have been designed for a 1000x1000 pixel (square) resolution, will appear small and off-center in a 16:9 canvas <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. They will need to be converted to 1920x1080 <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>. This provides an opportunity to create brand new animations that leverage the extra space <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>.

### Layouts and Overlays
All existing scene layouts will need to be reconfigured <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   **Bottom Bars/Overlays**: Unlock and stretch elements like bottom bars to fill the 16:9 width <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>. Use the Alt key to adjust the perspective and position precisely <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
*   **Backgrounds**: Animated backgrounds may already be wider than 4:3, but the 4:3 stage simply cut off the additional width <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>. These can now be fully displayed or extended to fill the canvas <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>.
*   **QR Codes and Text**: The additional real estate allows for making elements like QR codes larger, making them easier to scan <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>. Text elements can be extended across the screen, or formatted into multiple lines to fill the width <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.
*   **Camera/Mic Feeds**: While camera and mic feeds might initially appear displaced, they will align once integrated into the new 16:9 layouts <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>.

### Design Considerations with New Space
The increased screen space in 16:9 opens up new design possibilities <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   **Video Blocks**: Consider adding new video blocks or sections, perhaps for showing a desktop or specific application <a class="yt-timestamp" data-t="00:06:49">[00:06:49]</a>. This could involve using a window capture or display capture source <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.
*   **Notepads/Text Displays**: The extra space can be utilized for a visible notepad or dynamic text display <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   **Dynamic Content**: Instead of static text, consider animating call-to-action messages that cycle through the available space <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.
*   **Styling Variation**: Use the opportunity to create different styling for various scenes to keep content fresh and avoid a repetitive template feel <a class="yt-timestamp" data-t="00:17:47">[00:17:47]</a>.

> [!TIP] Manual Adjustment vs. Copy/Paste
> While copy-pasting settings might seem efficient, manually adjusting each scene can ensure precise alignment and cater to unique scene requirements <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.

## Workflow Tips

*   **Lock Layers**: Always lock layers once they are positioned correctly to prevent accidental movement <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>. Clicking off a selected box can automatically re-select the background if unlocked <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>.
*   **Read Text from File**: For dynamic text (like topics or titles), instead of typing directly into OBS, tick the "read from file" option <a class="yt-timestamp" data-t="00:14:17">[00:14:17]</a>. This allows you to update content by simply modifying a text file on your machine, minimizing the need to interact with OBS directly and reducing the risk of accidental changes <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>.
    *   Ensure you know the maximum character limit per line to avoid text going off-screen <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **Utilize a Second Screen**: For capturing applications or desktops, a second screen can be beneficial. If OBS is cooperative, you can capture the second screen and run a browser there to walk viewers through content while still maintaining other scene elements on your primary display <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>.

After making these adjustments, you can use the 16:9 profile for YouTube videos or live streams <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.