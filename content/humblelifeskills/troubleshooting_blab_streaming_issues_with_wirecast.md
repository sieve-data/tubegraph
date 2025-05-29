---
title: Troubleshooting Blab streaming issues with Wirecast
videoId: FEefAxMOJ4o
---

From: [[humblelifeskills]] <br/> 

Integrating Wirecast with Blab allows users to bring their Wirecast-produced content, including multiple shots and overlays, directly into a Blab session. This guide covers the setup process and common issues encountered when streaming to Blab using Wirecast's virtual camera output.

## Connecting Wirecast to Blab

To send your Wirecast output to Blab:
1.  Set up your desired stage and sources in Wirecast <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.
2.  Go to "Output" at the top menu bar in Wirecast <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
3.  Select "Virtual Camera Out" <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
4.  Ensure "Virtual microphone" is ticked <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
5.  Click "Start" <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This will activate the virtual camera and microphone, which will then be detectable by other applications <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
6.  Once started, Wirecast will display your frame rate and CPU usage, indicating the output is active <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.
7.  In your browser (e.g., Chrome) while on Blab, click on the camera/microphone icon in the browser bar <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.
8.  Select "Wirecast Virtual microphone" and "Wirecast Virtual camera" as your input devices <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. These options only appear once [[setting_up_virtual_camera_out_in_wirecast | Wirecast's virtual camera out]] has been started <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
9.  If the camera feed doesn't appear immediately or if the options don't show, you may need to refresh your browser after selecting the Wirecast inputs <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. This might require setting up a new Blab session <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Common Issues and Solutions

### Resolution and Performance Issues
*   **Problem:** Attempting to stream in HD 1080p resulted in the Blab feed "spinning and spinning," possibly due to an inability to send data fast enough <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.
*   **Solution:** Dropping the output resolution to 720p resolved the spinning issue without significantly impacting the visual quality on Blab <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. Users might try 1080p again in the future as conditions change <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>.

### Image Flipping and Recording Problems
*   **Problem:** The image streamed from Wirecast to Blab automatically flips horizontally, meaning what appears correct to the streamer is reversed for others <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. Additionally, Blab's "on the air" recording feature saves the reversed image, making the recorded file unusable <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>.
*   **Workaround (for live stream only):** To correct the image for live viewers, use Wirecast's "Horizontally Flip" option within the "Edit Shot" settings <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This will make the image appear correctly oriented for others on Blab <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   **Note:** This workaround does *not* fix the issue for the recorded file, which will still be reversed <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. This is a known issue that has been reported to Blab <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### Aspect Ratio Discrepancy
*   While Wirecast sources might be in 16:9 aspect ratio, Blab may display the feed in a 4:3 perspective <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>. This means parts of your Wirecast shot might be cut off on the sides <a class="yt-timestamp" data-t="00:02:06">[00:02:06]</a>.

Overall, [[using_wirecast_with_blab | connecting Wirecast to Blab]] is straightforward once the [[setting_up_virtual_camera_out_in_wirecast | virtual camera output]] is correctly configured and selected in the browser <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. Users should be aware of potential resolution and image flipping issues.