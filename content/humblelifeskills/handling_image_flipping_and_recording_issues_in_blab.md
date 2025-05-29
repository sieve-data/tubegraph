---
title: Handling image flipping and recording issues in Blab
videoId: FEefAxMOJ4o
---

From: [[humblelifeskills]] <br/> 

When using [[using_wirecast_with_blab | Wirecast]] to stream to Blab, users may encounter specific challenges related to image orientation and recorded output. While connecting the two platforms is straightforward, ensuring correct display and recording requires attention to browser settings and awareness of platform limitations <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Connecting Wirecast to Blab

To integrate your Wirecast output with Blab:
1.  **Enable Virtual Camera Out**: In Wirecast, navigate to "Output" at the top menu, then select "Virtual Camera Out" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
2.  **Select Virtual Microphone**: Ensure "Virtual Microphone" is also ticked in the settings <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
3.  **Adjust Resolution (if needed)**: Initially, streaming in HD 1080p might cause issues, such as the Blab interface endlessly "spinning" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. If this occurs, dropping the resolution to 720p may resolve the problem <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. The reason for this spinning might be related to data transmission speed <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.
4.  **Start Output**: Once settings are confirmed, click "Start" in Wirecast <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Wirecast will then display your frame rate (e.g., 30 frames per second) and CPU usage <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

Blab should automatically detect and display your Wirecast feed once you start a new blab session <a class="yt-timestamp" data-t="01:21:00">[01:21:00]</a>.

### Configuring Browser Settings

For the Wirecast feed to be properly recognized by Blab, verify your browser's camera and microphone settings. Using Chrome, click on the camera icon in the browser bar to ensure "Wirecast Virtual Microphone" and "Wirecast Virtual Camera" are selected <a class="yt-timestamp" data-t="02:24:00">[02:24:00]</a>. These options will only appear after Wirecast's virtual camera out is active <a class="yt-timestamp" data-t="02:29:00">[02:29:00]</a>. If problems persist after selection, a browser refresh (which necessitates setting up a new blab) may be required <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.

## Image Flipping and Aspect Ratio Issues

Upon connecting Wirecast to Blab, two common visual issues may arise:
*   **Image Reversal**: The image displayed on Blab appears horizontally flipped or reversed <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>. This means what appears on your left in Wirecast might show on the right for Blab viewers <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.
*   **Aspect Ratio Change**: The feed might switch from a 16:9 perspective (common in Wirecast setups) to a 4:3 aspect ratio on Blab, potentially cropping content on the sides <a class="yt-timestamp" data-t="01:39:00">[01:39:00]</a>.

### Addressing Image Flipping for Live Streams

To correct the image for live viewers on Blab, you can use Wirecast's "Horizontally Flip" option within the "Edit Shot" settings <a class="yt-timestamp" data-t="03:18:00">[03:18:00]</a>. This will make the image appear correctly oriented for others watching the live stream <a class="yt-timestamp" data-t="03:34:00">[03:34:00]</a>.

## Recording Issues

While flipping the image in Wirecast resolves the live display issue, it introduces a significant problem for recorded output:
*   **Reversed Recorded Files**: The "on-air" recording function of Blab will save the video with the image flipped *back* to its original, reversed state <a class="yt-timestamp" data-t="03:43:00">[03:43:00]</a>. This means that if you flip the image for live viewing, the recorded file will be backwards <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.
*   **Impact on Usability**: As a result, the recorded output becomes largely unusable if proper orientation is critical <a class="yt-timestamp" data-t="03:58:00">[03:58:00]</a>.

This recording discrepancy is a known issue, and discussions have been initiated with Blab support regarding this behavior <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.