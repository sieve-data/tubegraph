---
title: Adjusting frame rates and resolution in Wirecast
videoId: FEefAxMOJ4o
---

From: [[humblelifeskills]] <br/> 

When using [[wirecast_features_and_capabilities | Wirecast]] for live streaming, particularly with platforms like [[using_wirecast_with_blab | Blab]], adjusting output settings such as resolution and frame rate is crucial for optimal performance <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. These settings are configured through the `Output` menu <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

## Resolution Settings

To adjust resolution, navigate to `Output` at the top of the [[wirecast_features_and_capabilities | Wirecast]] interface, then select [[setting_up_virtual_camera_out_in_wirecast | Virtual Camera Out]] <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.

While [[wirecast_features_and_capabilities | Wirecast]] can run at HD 1080p <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>, streaming to platforms like [[using_wirecast_with_blab | Blab]] may encounter [[troubleshooting_blab_streaming_issues_with_wirecast | issues]] such as the stream "spinning and spinning" <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>. This can necessitate lowering the resolution <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. In such cases, dropping down to 720p might be effective <a class="yt-timestamp" data-t="00:00:32">[00:00:32]</a>. It was noted that 720p did not significantly alter the visual quality on [[using_wirecast_with_blab | Blab]] <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>, and the issue was potentially due to an inability to send data fast enough <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Frame Rate and Performance Monitoring

After selecting the desired output settings, click `Start` within the [[setting_up_virtual_camera_out_in_wirecast | Virtual Camera Out]] menu <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. [[wirecast_features_and_capabilities | Wirecast]] displays the current frame rate, typically around 30 frames per second (fps), and CPU usage <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. A CPU usage of around 30% is generally considered optimal <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>.

## Aspect Ratio Considerations

When streaming from [[wirecast_features_and_capabilities | Wirecast]] to a platform like [[using_wirecast_with_blab | Blab]], you might notice that the output image flips horizontally and appears in a 4x3 perspective, even if your original source in [[wirecast_features_and_capabilities | Wirecast]] is 16x9 <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>. This means the image appears reversed to the streamer <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>.

To correct the horizontal flip for viewers, you can edit the shot in [[wirecast_features_and_capabilities | Wirecast]] and horizontally flip it <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>. After flipping, the image will appear the correct way around on the streaming website <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

### Important Note on Recording

While flipping the image in [[wirecast_features_and_capabilities | Wirecast]] corrects the live stream for viewers, it's important to note that this horizontal flip might affect the "on the air" recording output <a class="yt-timestamp" data-t="00:03:46">[00:03:46]</a>. The recorded file might still have the image flipped back to front <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. As of the time of this transcript, this made the recorded output less useful, despite being correct during live streaming <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.