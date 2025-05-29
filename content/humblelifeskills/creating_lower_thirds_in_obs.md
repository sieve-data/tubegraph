---
title: Creating lower thirds in OBS
videoId: UidA1YFBSwg
---

From: [[humblelifeskills]] <br/> 

Creating lower thirds in OBS (Open Broadcaster Software) is possible even though OBS does not have native support for them <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>. There are three primary methods to achieve this: static overlays, animated overlays using Keynote, and advanced interactive overlays using custom browser docks (Windows only) <a class="yt-timestamp" data-t="00:32:02">[00:32:02]</a>.

## Method 1: Static Lower Thirds
This method involves designing the lower third as an image and adding text overlays in OBS.

### Design in Keynote
[[static_lower_thirds_using_keynote | Keynote]] is a free software that can be used for this purpose <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.
1.  **Set Slide Size**: Go to "slide size" and select "custom slide size" <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>.
    *   Use 1920x1080 for Full HD, or 1280x720 for 720p <a class="yt-timestamp" data-t="00:02:38">[00:02:38]</a>. OBS will scale it down if you're streaming at a lower resolution <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
2.  **Create Shapes**: Add shapes (e.g., a square for the main bar) and apply gradient fills to match your desired design <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>. You can adjust colors and gradient directions <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
3.  **Add Rounded Shapes**: Use rounded shapes for stylistic elements, adjusting corner radius as needed <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
4.  **Position Elements**: Arrange the shapes to form the lower third layout <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. Ensure that rounded corners are off the page if you want straight edges <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.
5.  **Export as PNG**: Export the design as an image, specifically a PNG file <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. This allows for transparency.

### Implementing in OBS
1.  **Create a New Scene**: In OBS, create a new scene (e.g., "overlay") <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.
2.  **Add Image Source**: Add an "Image" source and browse to the PNG file you exported <a class="yt-timestamp" data-t="00:07:00">[00:07:00]</a>. Since it was sized 1920x1080, it should fit perfectly <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>.
3.  **Add Text Sources**: Add "Text (GDI+)" sources for your main title and subtitle <a class="yt-timestamp" data-t="00:07:26">[00:07:26]</a>.
    *   Position and style the text within the lower third graphic <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.
    *   To make changes easier, duplicate text sources instead of referencing, to ensure changes to one don't affect others <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
    *   You can set the text to "read from file" to dynamically update the text by editing an external text file, which is useful if you are uncomfortable editing within OBS <a class="yt-timestamp" data-t="00:10:03">[00:10:03]</a>.
4.  **Lock Background**: Lock the image source in OBS so you don't accidentally move it when adjusting text <a class="yt-timestamp" data-t="00:07:57">[00:07:57]</a>.

## Method 2: Animated Lower Thirds
This method involves creating an animated movie file of your lower third in Keynote and using it as a media source in OBS.

### Animate in Keynote
[[animated_lower_thirds_using_keynote | Keynote]] allows you to animate elements for a dynamic lower third <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>.
1.  **Add Animations**: Select each element (shapes, text) and add "move in" or "dissolve" effects under the "animate" tab <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
2.  **Set Build Order**: Use the "build order" panel to sequence the animations. Set them to happen "after transition" or "after build" with slight delays for a smooth effect <a class="yt-timestamp" data-t="00:11:44">[00:11:44]</a>.
3.  **Export as Movie**:
    *   Ensure the slide background is set to "no fill" for transparency <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. If you leave a color, you may not get the transparent option <a class="yt-timestamp" data-t="00:20:35">[00:20:35]</a>.
    *   Export as a movie file <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.
    *   Under custom resolution, select "ProRes 4444" <a class="yt-timestamp" data-t="00:20:06">[00:20:06]</a>. This option provides a transparent background <a class="yt-timestamp" data-t="00:20:09">[00:20:09]</a>.

### Implementing in OBS
1.  **Create New Scene**: Create a new scene in OBS (e.g., "animated overlay") <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>.
2.  **Add Media Source**: Add a "Media Source" and select your exported movie file <a class="yt-timestamp" data-t="00:21:29">[00:21:29]</a>.
3.  **Configure Media Source**:
    *   Ensure "Loop" is *unchecked* so it plays once <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.
    *   Check "Show nothing when playback ends" <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>.
    *   Optionally, check "Close file when inactive" to free up memory <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>.
    *   You can also add "build out" animations in Keynote to have the lower third animate off screen <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>.

## Method 3: Advanced Lower Thirds with Custom Docs (Windows OBS Only)
This method utilizes a newer feature in OBS (version 25 onwards) that allows for interactive lower thirds via custom browser docks <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>. This feature is currently only available for [[windowsspecific_obs_features | Windows-specific OBS features]] <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.

### How it Works
This system provides an interactive control panel within OBS where you can type a name and job role, or select from a list of predefined names <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>. Clicking "show" updates a browser source overlay on your video <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.

1.  **Download OBS Tools**: This system uses a zip file (e.g., "OBS tools") containing CSS, fonts, images, JavaScript, and HTML files <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.
2.  **Mechanism**: It uses the Broadcast Channel API in HTML and JavaScript, which allows different sections of code (like the control panel and the overlay) to communicate and update information <a class="yt-timestamp" data-t="00:25:27">[00:25:27]</a>. The control panel is a custom doc (HTML/CSS) with a list of names that, when clicked, change the names displayed <a class="yt-timestamp" data-t="00:26:07">[00:26:07]</a>.
3.  **Customization**:
    *   The design is controlled by CSS (e.g., `common_CSS_style_001.css`), allowing customization of layout, fonts, and colors <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>.
    *   Logos are image files that can be replaced <a class="yt-timestamp" data-t="00:31:29">[00:31:29]</a>.
    *   You can even use transparent images or animated GIFs for backgrounds <a class="yt-timestamp" data-t="00:31:51">[00:31:51]</a>.

### Setup (Windows Only)
1.  **Add Custom Browser Doc**: In OBS, go to "View" > "Docs" > "Custom Browser Docs" <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>.
    *   Give it a name (e.g., "lower thirds control panel") <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.
    *   Point it to the `lower_third_control_panel.html` file from the downloaded tools <a class="yt-timestamp" data-t="00:28:53">[00:28:53]</a>. This will make the control panel appear as a dockable window in OBS <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.
2.  **Add Browser Source**: In your OBS scene, add a "Browser Source" <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.
    *   Check "Local file" and browse to the `browser_source.html` (or `receiver_demo.html`) file <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.
    *   When you update information in the custom doc, it will automatically update this browser source <a class="yt-timestamp" data-t="00:30:12">[00:30:12]</a>.

This method is highly interactive and ideal for live streams with multiple guests or dynamic information, as it keeps assets local and reduces latency <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>.