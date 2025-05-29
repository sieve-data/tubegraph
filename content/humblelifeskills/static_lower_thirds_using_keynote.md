---
title: Static lower thirds using Keynote
videoId: UidA1YFBSwg
---

From: [[humblelifeskills]] <br/> 

Lower thirds are essential graphical overlays for video production, providing information about individuals or topics on screen <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. While there is no built-in lower third support in OBS, they can be created manually <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>. One method is to create static lower third layouts using Keynote and then add editable text in OBS <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

## Why Use Keynote for Static Lower Thirds?

Keynote is a free software, primarily a Mac application, but is also available for PC <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. It allows for the creation of static graphical elements that can then be imported into OBS <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

## Creating the Static Lower Third in Keynote

1.  **Set Slide Size**:
    *   Open Keynote and go to slide size settings <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.
    *   Select "Custom Slide Size" and set it to 1920x1080 pixels for Full HD, which is ideal for OBS <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
    *   Alternatively, for 720p streaming (e.g., Twitch), you can use 1280x720 pixels <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. OBS will scale down larger resolutions if needed <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.

2.  **Design the Base Shape**:
    *   Insert a square shape <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.
    *   Stretch it across the stage to form the base of your lower third <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   Format it with a gradient fill, for example, a green-to-blue gradient as desired <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Adjust the scaling of the gradient to achieve the desired look <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

3.  **Add Additional Shapes**:
    *   Add a rounded rectangular shape on top of the base, typically in white <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
    *   Adjust the corner radius for a more pronounced curve <a class="yt-timestamp" data-t="00:04:31">[00:04:31]</a>.
    *   Place it on the stage, considering where text will be placed <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.
    *   Copy the rounded rectangle and change its color to a darker blue for a top bar overlay <a class="yt-timestamp" data-t="00:05:18">[00:05:18]</a>. Position it to complete the lower third design <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.
    *   Adjust the overall size of the created elements to fit well on the screen <a class="yt-timestamp" data-t="00:06:03">[00:06:03]</a>.

4.  **Export as an Image**:
    *   Export the slide as an image <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.
    *   Choose PNG format for transparency <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.
    *   Name and save the file, for example, "lower third" <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>.
    *   Ensure the background is set to "No Fill" in Keynote's format section to ensure a transparent background when exporting <a class="yt-timestamp" data-t="00:20:22">[00:20:22]</a>. If there's a color, you won't get the "Export with transparent background" option <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.

## Implementing the Static Lower Third in OBS

1.  **Add Image Overlay**:
    *   In OBS, create a new scene, e.g., "overlay" <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
    *   Add an "Image" source and select the exported lower third PNG file <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>.
    *   Since it was sized 1920x1080 in Keynote, it should fit perfectly in a 1920x1080 OBS canvas <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.

2.  **Add Editable Text**:
    *   Add a "Text (GDI+)" source for the main title (e.g., name/CEO) <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   Position and size the text to fit within the lower third graphic <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   To create the subtitle, duplicate the main title text source (avoid "reference" to allow independent editing) <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
    *   Rename the duplicate to "subtitle" and edit its content (e.g., job role) <a class="yt-timestamp" data-t="00:08:22">[00:08:22]</a>.
    *   Change the subtitle text color to ensure it's visible on the white section of the lower third <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.
    *   **Lock the background image** to prevent accidental movement <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

### Dynamic Text Updates

For easier management, you can configure text sources to "Read from file" <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. This allows you to update the text by modifying a simple text file on your computer without entering OBS <a class="yt-timestamp" data-t="00:10:06">[00:10:06]</a>. Be mindful of character limits to avoid text spilling off the graphic <a class="yt-timestamp" data-t="00:10:14">[00:10:14]</a>.

This method allows for fully editable text within OBS while using a static graphic from Keynote <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>. You can create multiple copies of this scene for different people or purposes <a class="yt-timestamp" data-t="00:09:31">[00:09:31]</a>.

For animated lower thirds, you can also use [[animated_lower_thirds_using_keynote | Keynote]] to export a movie file with animations <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>. Additionally, a new plugin with a control panel is available for [[creating_lower_thirds_in_obs | OBS on Windows]] for more advanced and dynamic lower third management <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.