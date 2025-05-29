---
title: Animated lower thirds using Keynote
videoId: UidA1YFBSwg
---

From: [[humblelifeskills]] <br/> 
## Animated Lower Thirds Using Keynote

[[customizing_layouts_and_intros_for_improved_presentation | Keynote]] is a free software primarily for Mac users, though it may also be available for PC <a class="yt-timestamp" data-t="02:20"></a>. It can be used to create both static and animated lower thirds for video production.

### Creating Static Lower Thirds in Keynote

Before animating, it's useful to understand how to build the static graphic:
1.  **Set Slide Size** <a class="yt-timestamp" data-t="02:31"></a>: Go to "Slide Size" and select "Custom Slide Size" <a class="yt-timestamp" data-t="02:34"></a>. Use `1920x1080` for Full HD, or `1280x720` for 720p, matching your OBS streaming resolution <a class="yt-timestamp" data-t="02:37"></a>.
2.  **Add Shapes** <a class="yt-timestamp" data-t="03:17"></a>: Insert a square shape and pull it across the stage to form the base of your lower third <a class="yt-timestamp" data-t="03:20"></a>. Add a rounded shape for the top element <a class="yt-timestamp" data-t="04:26"></a>. Adjust the corner radius of the rounded shape as needed <a class="yt-timestamp" data-t="04:44"></a>.
3.  **Apply Colors and Gradients** <a class="yt-timestamp" data-t="03:33"></a>: Format shapes with gradient fills <a class="yt-timestamp" data-t="03:33"></a>. You can use advanced gradient fill options for more control over color distribution <a class="yt-timestamp" data-t="04:09"></a>.
4.  **Position Elements** <a class="yt-timestamp" data-t="04:47"></a>: Arrange the shapes to create the desired lower third layout <a class="yt-timestamp" data-t="04:47"></a>. Adjust overall size by selecting all elements and scaling them down <a class="yt-timestamp" data-t="06:05"></a>.
5.  **Export for Static Use** <a class="yt-timestamp" data-t="06:18"></a>: To use this as a static graphic in OBS, export the slide as a PNG image <a class="yt-timestamp" data-t="06:22"></a>.
    *   In OBS, add this PNG as an image source <a class="yt-timestamp" data-t="07:00"></a>.
    *   Add separate text sources in OBS for the main title and subtitle <a class="yt-timestamp" data-t="07:26"></a>. This allows for easy editing of text within OBS <a class="yt-timestamp" data-t="07:51"></a>.
    *   Lock the background image layer in OBS to prevent accidental movement <a class="yt-timestamp" data-t="07:57"></a>.
    *   For dynamic text, you can set OBS text sources to "read from file", allowing updates by simply editing a text file outside OBS <a class="yt-timestamp" data-t="10:03"></a>.

### Creating Animated Lower Thirds in Keynote

Keynote allows for animation of individual elements, which can then be exported as a movie for use as an overlay.

1.  **Animate Elements** <a class="yt-timestamp" data-t="10:58"></a>:
    *   Select an element (e.g., the bottom rectangle) <a class="yt-timestamp" data-t="11:02"></a>.
    *   Go to the "Animate" tab on the right-hand side <a class="yt-timestamp" data-t="11:05"></a>.
    *   Add a "Build In" effect, such as "Move In" <a class="yt-timestamp" data-t="11:08"></a>. Adjust the direction (e.g., left to right) and duration (e.g., 0.5 seconds) <a class="yt-timestamp" data-t="11:12"></a>.
    *   Use the "Build Order" panel <a class="yt-timestamp" data-t="11:44"></a> to sequence animations. Set animations to happen "After Transition" or "After Build" to automate their playback without clicks <a class="yt-timestamp" data-t="11:52"></a>.
    *   Repeat for other graphical elements, sequencing them with slight delays for a smooth animation <a class="yt-timestamp" data-t="12:13"></a>.
2.  **Add and Animate Text** <a class="yt-timestamp" data-t="15:51"></a>:
    *   Insert text boxes directly into Keynote for the main title and subtitle <a class="yt-timestamp" data-t="16:12"></a>.
    *   Apply a "Build In" effect, such as "Dissolve" <a class="yt-timestamp" data-t="16:56"></a>.
    *   Adjust text color to contrast with the background graphic <a class="yt-timestamp" data-t="18:01"></a>.
    *   Ensure text animations also follow the build order after the graphics appear <a class="yt-timestamp" data-t="17:05"></a>.
3.  **Prepare for Export** <a class="yt-timestamp" data-t="19:35"></a>:
    *   Crucially, set the slide background to "No Fill" to ensure transparency <a class="yt-timestamp" data-t="20:24"></a>. This option must be set before exporting to see the "Export with transparent background" option <a class="yt-timestamp" data-t="20:45"></a>.
4.  **Export as Movie** <a class="yt-timestamp" data-t="19:57"></a>:
    *   Go to File > Export To > Movie <a class="yt-timestamp" data-t="19:57"></a>.
    *   Choose "Custom Resolution" and input `1920x1080` (or your chosen resolution) <a class="yt-timestamp" data-t="20:03"></a>.
    *   Select "ProRes 4444" as the format <a class="yt-timestamp" data-t="20:09"></a>. This codec supports alpha channels, providing a transparent background <a class="yt-timestamp" data-t="20:13"></a>.
    *   Ensure "Export with transparent background" is checked <a class="yt-timestamp" data-t="20:48"></a>.
5.  **Import into OBS** <a class="yt-timestamp" data-t="21:25"></a>:
    *   Add a "Media Source" in OBS and browse to your exported Keynote movie file <a class="yt-timestamp" data-t="21:29"></a>.
    *   In the media source properties, **uncheck "Loop"** so the animation plays once <a class="yt-timestamp" data-t="21:47"></a>.
    *   Check "Show nothing when playback ends" <a class="yt-timestamp" data-t="21:50"></a> and "Close file when inactive" <a class="yt-timestamp" data-t="21:52"></a>.

### Animating Out (Optional)

For a complete animation, you can add "Build Out" effects in Keynote to have the lower third elements move or fade off screen after a delay <a class="yt-timestamp" data-t="22:23"></a>. This creates a more polished intro and outro sequence for your lower third.