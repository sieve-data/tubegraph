---
title: Optimizing video settings and performance for older computers
videoId: 4t76td7JdpA
---

From: [[humblelifeskills]] <br/> 

When working with older computer hardware, especially for video encoding and streaming, it's crucial to optimize your settings to ensure smooth performance and avoid taxing the machine too much. This often involves adjusting resolutions, frame rates, and adapting to potential software limitations <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>.

## Key Settings Adjustments in OBS

To improve performance on an older machine, consider modifying your video output settings within OBS:

-   **Base Canvas and Output Resolution**: While the base canvas can be set to HD (1920x1080) for a 16:9 perspective, you might need to manage the overall pixel load <a class="yt-timestamp" data-t="01:53:00">[01:53:00]</a>, <a class="yt-timestamp" data-t="02:17:00">[02:17:00]</a>.
-   **Frame Rate**: Reduce the Common FPS Value. For instance, lowering the frame rate to 30 frames per second (fps) can significantly reduce the processing load on an older computer <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>. Higher resolutions push more pixels, which can be very demanding on older hardware <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>, <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>.

## Managing Scenes and Assets

Even with an older machine, you can still create professional-looking content by strategically managing your scenes and assets:

-   **Scene Duplication**: Always duplicate your profiles and scene collections (e.g., when converting from 4:3 to 16:9) before making significant changes. This ensures that any adjustments do not affect your original setup and allows for safe experimentation <a class="yt-timestamp" data-t="01:15:00">[01:15:00]</a>, <a class="yt-timestamp" data-t="01:27:00">[01:27:00]</a>, <a class="yt-timestamp" data-t="01:40:00">[01:40:00]</a>.
-   **Asset Adaptation**: Intros, outros, and master scenes created for a 4:3 aspect ratio will need to be converted or recreated for 16:9 (e.g., from 1000x1000 pixels to 1920x1080 pixels) <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>, <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. This provides more "real estate" for creative layouts and additional content <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>, <a class="yt-timestamp" data-t="06:34:00">[06:34:00]</a>, <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>.
-   **Layer Management**: Utilize layer locking in OBS to prevent accidental changes to background elements or other locked sources, especially when making fine adjustments to overlapping elements <a class="yt-timestamp" data-t="06:56:00">[06:56:00]</a>, <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>.

### Creative Use of Space

The shift to a wider aspect ratio on older machines offers new design opportunities:

-   **Dynamic Layouts**: The increased space can be used to incorporate additional video blocks, display a second screen (like a browser or desktop), or integrate dynamic information like a notepad or scrolling text <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>, <a class="yt-timestamp" data-t="09:37:00">[09:37:00]</a>, <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>.
-   **QR Codes**: Larger screen real estate makes QR codes easier to scan, improving user interaction <a class="yt-timestamp" data-t="08:28:00">[08:28:00]</a>.
-   **Text Management**: Text elements can be extended across the wider screen or wrapped into multiple lines. For more control, consider using the "read from file" option for text sources, allowing updates from an external text file without modifying OBS directly <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>, <a class="yt-timestamp" data-t="14:19:00">[14:19:00]</a>. Just be mindful of character limits per line to avoid text going off-screen <a class="yt-timestamp" data-t="14:41:00">[14:41:00]</a>.

## Addressing OS-Specific Challenges

Older operating systems, such as macOS Catalina, can sometimes present unique challenges or bugs within OBS:

-   **Window Capture Issues**: You might encounter bugs where window capture properties are unavailable, making it difficult to capture specific application windows or displays <a class="yt-timestamp" data-t="10:00:00">[10:00:00]</a>, <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>.
-   **Workarounds**: As a workaround, you might need to adjust the application window size and position it on screen to be captured, or if available, utilize a second screen to capture content that isn't directly interacting with the primary OBS display <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>, <a class="yt-timestamp" data-t="12:10:00">[12:10:00]</a>.
-   **OBS Stability**: While OBS can sometimes be fragile on older systems, consistent updates have made it more reliable over time, reducing instances of crashes <a class="yt-timestamp" data-t="14:56:00">[14:56:00]</a>.

By carefully adjusting video settings and adapting your scene layouts, you can still achieve a professional look and reliable performance even when working with older computer hardware.