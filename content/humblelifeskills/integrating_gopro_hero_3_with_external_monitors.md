---
title: Integrating GoPro Hero 3 with external monitors
videoId: rw8Z6ZJQ_kk
---

From: [[humblelifeskills]] <br/> 

The GoPro Hero 3 Black Edition, released approximately a week and a half prior to this discussion, is highlighted for its excellent picture quality and stable operation. While generally performing well, the presenter notes a few instances of problems, which are not detailed in this segment <a class="yt-timestamp" data-t="00:00:33">[00:00:33]</a>. The primary focus of this follow-up is to explore getting video output from the camera via [[hdmi_output_from_gopro_hero_3 | HDMI]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## HDMI Output and Cables

The [[hdmi_output_from_gopro_hero_3 | GoPro Hero 3]] features a micro HDMI port on its side <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>. To connect, a special micro HDMI cable is required, as standard cables will not fit <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. The presenter acquired both a short and a "Cable Matters" brand cable for this purpose <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.

When connecting the HDMI cable to the GoPro, the fit is described as "fairly solid" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. However, concern is raised about the weight of the cable pulling on the port, suggesting a need for a clip or cable management system to prevent damage to the port over time <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.

## External Monitoring and Capture Options

Initially, the presenter intended to connect the GoPro's [[hdmi_output_from_gopro_hero_3 | HDMI output]] to a Mac Pro equipped with a [[using_gopro_with_blackmagic_intensity_extreme | Blackmagic Intensity card]] (specifically the mobile "Extreme" version) <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. This card is designed to capture full-frame HD video up to 1080p, offloading processing from the graphics card and CPU, resulting in low latency capture <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>. However, the Mac Pro was unable to write high-definition videos, leading to a change of plans for the demonstration <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

Instead, a Lilliput 7-inch LCD field monitor was used for the demonstration <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. This portable monitor is useful for viewing shots outdoors and has potential applications for in-car setups, possibly integrating with devices like a Raspberry Pi <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

## Testing HDMI Output to Field Monitor

The process of connecting the [[hdmi_output_from_gopro_hero_3 | GoPro Hero 3]] to the Lilliput field monitor involved:
1.  Plugging the HDMI cable into the monitor's input <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>.
2.  Switching the monitor on <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
3.  Setting the monitor mode to camera <a class="yt-timestamp" data-t="00:05:35">[00:05:35]</a>.

Upon connection, the monitor immediately detected an [[hdmi_output_from_gopro_hero_3 | HDMI signal]] <a class="yt-timestamp" data-t="00:05:42">[00:05:42]</a>.

### Displayed Information
The external monitor displayed various informational overlays from the GoPro, including:
*   "Protune" in the top left corner <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   Resolution and frame rate (e.g., 1080 25) <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>.
*   Battery status <a class="yt-timestamp" data-t="00:06:08">[00:06:08]</a>.
*   Wi-Fi status (off) <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.
*   GoPro setup prompts <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   All GoPro settings, such as Protune options, were visible on the HDMI screen as the user navigated them <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

### Clean HDMI Out Consideration
A key goal for many users is "clean HDMI out," where only the video signal is displayed without any on-screen camera information or overlays. This is often problematic with DSLRs, though some, like the Nikon D800, offer it, while others, like the Canon Mark III (prior to potential firmware updates), do not <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>. The GoPro Hero 3, as tested, initially displays its UI elements on the external monitor <a class="yt-timestamp" data-t="00:05:48">[00:05:48]</a>. The presenter expresses a need to investigate if there are settings within the GoPro to disable these on-screen displays for a "clean" output <a class="yt-timestamp" data-t="00:06:53">[00:06:53]</a>.

## Conclusion

The initial test successfully demonstrated that a "decent picture" can be obtained from the [[hdmi_output_from_gopro_hero_3 | GoPro Hero 3]] via [[using_hdmi_cables_with_gopro_hero_3 | HDMI]] to an external field monitor without needing to adjust any specific settings beforehand <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>. The next step identified is to determine how to capture this output into a machine and achieve a clean video feed <a class="yt-timestamp" data-t="00:07:31">[00:07:31]</a>.