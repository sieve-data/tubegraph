---
title: Windowsspecific OBS features
videoId: UidA1YFBSwg
---

From: [[humblelifeskills]] <br/> 

OBS Studio often rolls out new features for Windows before they are available on macOS. This can be due to various reasons, including stability issues where new features might "fall over and crash on a Mac" <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Animated Lower Thirds with Control Panel

One notable feature available exclusively on Windows is an advanced method for creating and controlling animated lower thirds <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>. This functionality was sourced from the OBS Broadcaster site and includes a control panel <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>. It functions as a plugin that currently "only works with custom Doc's on Windows" <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>, and was observed as a new feature in OBS version 25 <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>.

This system provides an interactive area within OBS where users can input names and job roles <a class="yt-timestamp" data-t="00:23:38">[00:23:38]</a>. It supports lists of individuals, making it ideal for live streams with multiple guests, allowing names to be pre-set and updated with a simple click <a class="yt-timestamp" data-t="00:23:44">[00:23:44]</a>. When activated, the control panel updates a browser source overlay on the video feed <a class="yt-timestamp" data-t="00:23:54">[00:23:54]</a>.

### Technical Implementation

The control panel utilizes OBS's custom browser docks feature, accessible on Windows via `View > Docs > Custom Browser Docs` <a class="yt-timestamp" data-t="00:24:15">[00:24:15]</a>. Users can search for "[obs_custom_browser_docs | doc web browser sources in OBS]]" for more detailed instructions <a class="yt-timestamp" data-t="00:24:17">[00:24:17]</a>.

The functionality relies on a downloaded "OBS tools" zip file, which contains:
*   CSS files <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>
*   Font files <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>
*   Image files (e.g., logos) <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>
*   JavaScript files <a class="yt-timestamp" data-t="00:24:49">[00:24:49]</a>
*   Two HTML files (one for the control panel and one for the browser source overlay) <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>

The core communication between the control panel and the overlay is managed by a new function called `broadcast channel` <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>, which is part of the Broadcast Channel API <a class="yt-timestamp" data-t="00:25:33">[00:25:33]</a>. This API allows different sections of code, such as separate windows or docks, to interact and communicate with each other <a class="yt-timestamp" data-t="00:25:48">[00:25:48]</a>.

To set up:
1.  Add a custom dock in OBS (e.g., named "Lower Thirds Control Panel") and point it to the control panel HTML file <a class="yt-timestamp" data-t="00:28:48">[00:28:48]</a>.
2.  Add a browser source in OBS and set its local file path to the receiver demo HTML file <a class="yt-timestamp" data-t="00:30:08">[00:30:08]</a>.

The appearance of the lower third can be customized by editing the CSS and replacing image assets <a class="yt-timestamp" data-t="00:30:36">[00:30:36]</a>. As these assets are local HTML files on the machine, they offer low latency and allow for advanced local server environments like PHP for dynamic data pulling <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.