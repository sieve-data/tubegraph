---
title: OBS custom browser docs
videoId: UidA1YFBSwg
---

From: [[humblelifeskills]] <br/> 

OBS Custom Browser Docks are a feature that allows users to create interactive control panels and dynamic overlays directly within OBS, primarily utilizing web technologies like HTML, CSS, and JavaScript <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>. Introduced possibly in version 25 of OBS, this functionality significantly enhances live stream management and graphic customization <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>.

## What are Custom Browser Docks?

Custom Browser Docks provide an area within OBS where users can interact with their stream elements dynamically <a class="yt-timestamp" data-t="00:23:31">[00:23:31]</a>. Unlike static image overlays or pre-rendered animated videos, custom docks offer real-time control over on-screen graphics <a class="yt-timestamp" data-t="00:27:59">[00:27:59]</a>.

## Functionality and Capabilities

Custom docks are particularly useful for managing [[creating_lower_thirds_in_obs | lower thirds]] and other on-screen text, especially during live streams with multiple guests <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>:
*   **Dynamic Text Input**: Users can type names and job roles directly into a control panel within OBS <a class="yt-timestamp" data-t="00:23:34">[00:23:34]</a>.
*   **Pre-configured Lists**: A list of names and roles can be pre-set, allowing quick selection and update of on-screen information with a single click <a class="yt-timestamp" data-t="00:23:47">[00:23:47]</a>.
*   **Real-time Updates**: Changes made in the custom dock instantly update the associated browser source overlay on the video <a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.
*   **Customization**: The visual appearance of the overlays (e.g., logo, text layout, background) can be customized using CSS and by replacing image files <a class="yt-timestamp" data-t="00:30:36">[00:30:36]</a>. Animated GIFs can even be used as backgrounds for overlays <a class="yt-timestamp" data-t="00:31:54">[00:31:54]</a>.
*   **Local Processing**: Custom docks run on local HTML files, meaning there is no lag or latency associated with pulling data from the web <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.

## How Custom Docks Work (Technical Details)

The core mechanism behind OBS Custom Browser Docks involves standard web technologies communicating via a specific API:
*   **HTML, CSS, and JavaScript**: Custom docks are built using these foundational web languages <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.
    *   HTML defines the structure and content of the control panel and the overlay <a class="yt-timestamp" data-t="00:25:08">[00:25:08]</a>.
    *   CSS styles the appearance of both the control panel and the on-screen overlay <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.
    *   JavaScript handles the interactive logic, allowing user input and communication between the control panel and the overlay <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>.
*   **Broadcast Channel API**: A new function called `BroadcastChannel` is utilized <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>. This API allows different sections of code, such as the control panel (a custom dock) and the on-screen browser source (the overlay), to interact and communicate with each other <a class="yt-timestamp" data-t="00:25:41">[00:25:41]</a>. When a button is clicked in the control panel, it sends a message through this channel, updating the linked browser source <a class="yt-timestamp" data-t="00:25:55">[00:25:55]</a>.

## Platform Availability

Currently, OBS Custom Browser Docks are a [[windowsspecific_obs_features | Windows-specific OBS feature]] <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>. They do not work on macOS versions of OBS at this time <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>. This limitation is noted to be due to potential stability issues with new features on Mac compared to PC, leading to a staggered release <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>. Streamlabs OBS for Mac also lacks customizable docks, offering only a chat dock <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.

## Setting up a Custom Dock (Windows)

For Windows users, setting up a custom dock involves these general steps:
1.  **Download Files**: Obtain the necessary HTML, CSS, and JavaScript files for the custom dock (e.g., from a provided zip download like "OBS tools") <a class="yt-timestamp" data-t="00:24:33">[00:24:33]</a>.
2.  **Add Custom Browser Dock**: In OBS, go to "View" > "Docs" > "Custom Browser Docs" <a class="yt-timestamp" data-t="00:24:11">[00:24:11]</a>.
3.  **Configure Control Panel**: Give the dock a name (e.g., "Lower Thirds Control Panel") and point it to the control panel's HTML file (e.g., `lower_third_control_panel.html`) <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>. This will make the control panel appear as a dockable window in OBS <a class="yt-timestamp" data-t="00:28:57">[00:28:57]</a>.
4.  **Add Browser Source for Overlay**: Create a new scene or add a new source to an existing scene. Choose "Browser Source" <a class="yt-timestamp" data-t="00:29:55">[00:29:55]</a>.
5.  **Point to Overlay HTML**: In the browser source properties, select "Local file" and navigate to the HTML file for the overlay (e.g., `browser_source.html`) <a class="yt-timestamp" data-t="00:30:06">[00:30:06]</a>.
6.  **Interact**: Any changes made in the custom control panel dock will automatically update the browser source overlay on the screen <a class="yt-timestamp" data-t="00:30:10">[00:30:10]</a>.

## Potential Applications

The ability to create custom interactive docks within OBS opens up a wide range of possibilities for live streamers to enhance their [[building_and_adjusting_scene_assets_in_obs | scene assets]] and overall production <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a>:
*   **Live Stream Management**: Quickly update guest names, topics, or scores <a class="yt-timestamp" data-t="00:27:47">[00:27:47]</a>.
*   **Dynamic Information Display**: Pull real-time data (e.g., from web APIs) and display it on stream via locally running HTML files <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>.
*   **Interactive Overlays**: Create complex overlays that respond to user input or other triggers within OBS <a class="yt-timestamp" data-t="00:32:22">[00:32:22]</a>.
*   **Multi-Monitor Setups**: Utilize multiple screens with various docks for chat, asset management, and up-to-date information <a class="yt-timestamp" data-t="00:29:28">[00:29:28]</a>.

This feature is highly anticipated for future macOS OBS releases, as it promises to revolutionize how users manage and interact with their live stream graphics <a class="yt-timestamp" data-t="00:28:22">[00:28:22]</a>.