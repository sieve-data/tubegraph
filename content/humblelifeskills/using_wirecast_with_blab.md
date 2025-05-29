---
title: Using Wirecast with Blab
videoId: FEefAxMOJ4o
---

From: [[humblelifeskills]] <br/> 

Integrating [[Wirecast features and capabilities | Wirecast]] with Blab allows users to send their staged shots and sources directly to a Blab broadcast <a class="yt-timestamp" data-t="00:00:04">[00:00:04]</a>.

## Setting Up Wirecast for Blab

1.  **Activate Virtual Camera Out**: After setting up your stage and sources in [[Wirecast features and capabilities | Wirecast]], go to the top menu, select `Output`, then `Virtual Camera Out` <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.
2.  **Select Virtual Microphone**: Ensure the `Virtual Microphone` option is ticked <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.
3.  **Adjust Resolution (If Necessary)**: Initially, a common issue was trying to run at HD 1080p, which caused Blab to keep spinning <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Dropping the resolution to 720p resolved this problem, though 720p doesn't significantly alter the appearance on Blab <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>.
4.  **Start Output**: Once the virtual camera and microphone are selected, click `Start` <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This will display your frame rate (e.g., 30 frames per second) and CPU usage in [[Wirecast features and capabilities | Wirecast]] <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>.

## Connecting Blab to Wirecast

1.  **Start a Blab Session**: Navigate to Blab and initiate a new broadcast <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
2.  **Verify Wirecast Feed**: Blab should automatically pull in the feed from your [[Wirecast features and capabilities | Wirecast]] output <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.
3.  **Browser Settings**: To ensure the connection is active, check your browser's camera and microphone settings (e.g., by clicking the camera icon in Chrome's address bar) <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
    *   Confirm that `Wirecast Virtual Microphone` and `Wirecast Virtual Camera` are selected <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
    *   These options only appear after you have started the [[Setting up Virtual Camera Out in Wirecast | Wirecast virtual camera out]] <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
4.  **Troubleshooting Connection Issues**: If the feed isn't coming through, select the [[Wirecast features and capabilities | Wirecast]] options in your browser settings and then refresh your browser. This will likely require starting a new Blab session <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

## Addressing Blab Image Flipping and Recording Issues

### Image Flipping
When streaming from [[Wirecast features and capabilities | Wirecast]] to Blab, the image often appears horizontally flipped to the broadcaster <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   Blab typically displays a 4:3 perspective, even if your [[Wirecast features and capabilities | Wirecast]] output is 16:9 <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.
*   To correct the image for viewers, you can horizontally flip the shot within [[Wirecast features and capabilities | Wirecast]] by going into `Edit Shot` and selecting the horizontal flip option <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. This will make the image appear correctly oriented on the Blab website <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Recording Output
A significant issue is that while live streaming, the flipped image appears correctly to viewers, the "on the air" recording feature in Blab reverses the image again, making the recorded file back to front <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This means the recorded output is currently not useful if you need the correct orientation <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

Connecting [[Wirecast features and capabilities | Wirecast]] to Blab is generally simple, primarily requiring correct selection of the virtual camera and microphone in your browser settings <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.