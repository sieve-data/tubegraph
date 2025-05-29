---
title: Setting up Virtual Camera Out in Wirecast
videoId: FEefAxMOJ4o
---

From: [[humblelifeskills]] <br/> 

To get your [[Wirecast]] shot into a platform like [[Blab]], you utilize the Virtual Camera Out feature. This process is straightforward once your stage and sources are set up <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>.

## Initial Setup in Wirecast

1.  Go to **Output** at the top menu in [[Wirecast]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
2.  Select **Virtual Camera Out** <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
3.  Scroll down and ensure **Virtual Microphone** is also ticked <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>.

### Resolution and Frame Rate Considerations

Initially, running in HD 1080p may cause [[troubleshooting_blab_streaming_issues_with_wirecast | issues]] with [[Blab]], such as continuous spinning <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Dropping the resolution to 720p can resolve this, though the exact cause (e.g., data sending speed) may be unclear <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a> <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. The visual difference on [[Blab]] at 720p may be minimal <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. For more information, see [[adjusting_frame_rates_and_resolution_in_wirecast | Adjusting frame rates and resolution in Wirecast]].

## Starting the Virtual Output

Once the desired settings are selected, click **Start** <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. After starting, [[Wirecast]] will display your frame rate (e.g., 30 frames per second) and CPU usage (e.g., 30%) <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.

## Connecting to Blab

When starting a new [[Blab]] session, your [[Wirecast]] feed should automatically appear <a class="yt-timestamp" data-t="00:01:21">[00:01:21]</a>.

### Browser Settings and Troubleshooting

To ensure the connection works correctly, especially if the feed doesn't come through automatically:

1.  In your browser (e.g., Chrome), click on the icon in the browser bar <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a> <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.
2.  Verify that **Wirecast Virtual Microphone** and **Wirecast Virtual Camera** are selected <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. These options only appear after the [[Wirecast]] virtual camera and microphone outputs have been started <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
3.  If no connection is established after selecting them, you may need to refresh your browser, which might require setting up a new [[Blab]] <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a> <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.

## Image Orientation and Aspect Ratio

Upon connecting to [[Blab]], you might notice:

*   The image is flipped horizontally <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   The perspective is 4:3, even if your [[Wirecast]] setup is 16:9 <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a> <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a>.

### Correcting Flipped Images

To ensure other viewers see the correct orientation:

1.  In [[Wirecast]], go into **Edit Shot** <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
2.  Select the option to **Horizontally Flip** the image <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
3.  After flipping, the image on the [[Blab]] website will appear correctly <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

> [!CAUTION] Recorded Output
> While flipping the image allows live viewers to see it correctly, the recorded output from [[Blab]] may still show the image reversed. This can make the recorded file unusable if the orientation is critical <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a> <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a> <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Developers are aware of this issue and are being contacted about it <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.