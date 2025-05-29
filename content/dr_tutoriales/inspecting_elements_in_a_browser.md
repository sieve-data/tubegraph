---
title: Inspecting elements in a browser
videoId: g26WthoEXLs
---

From: [[dr_tutoriales]] <br/> 

Inspecting elements in a browser is a technique used to view and interact with the underlying code (HTML, CSS, JavaScript) that constructs a webpage [00:01:00]. This process is essential for understanding how a page is built and can be used for various purposes, including troubleshooting or extracting specific content like video sources [00:01:06].

## Accessing the Inspection Tool

To access the inspection tool in a web browser, particularly for the purpose of downloading videos from Facebook:

1.  Navigate to the Facebook page containing the video you wish to download [00:00:20].
2.  Modify the URL in the address bar. Change `www` to `m` (e.g., `https://www.facebook.com/...` becomes `https://m.facebook.com/...`) to access the mobile version of the site within your computer's browser [00:00:34].
3.  Once on the mobile version, right-click on an empty space within the video player area [00:00:51].
4.  From the context menu, select "inspect" [00:00:57]. This action will open a window, typically on the right side of your screen, displaying the webpage's source code [00:00:57]. While understanding all the code is not necessary, paying attention to the next steps is crucial [00:01:06].

## Locating Video Source Through Inspection

After opening the inspection window, follow these steps to find the video's original source:

1.  Play the video for a brief period, approximately two to three seconds [00:01:12].
2.  In the inspection window, locate and click the "inspect video" button or the element selector tool [00:01:31].
3.  Hover your mouse cursor over the video element on the webpage. The corresponding code in the inspection window should highlight, indicating the video's origin [00:01:38].
4.  Double-click the highlighted code segment that represents the video's "origin" [00:01:46].
5.  Copy the URL found within this highlighted code, ensuring you copy from the `HTTP` part onwards [00:02:00].
6.  Open a new browser tab and paste the copied URL [00:02:05]. This will load the video in its original, root Facebook version [00:02:10].
7.  From this new tab, you can typically download the video by clicking on the three-dot menu icon associated with the video player and selecting "download" [00:02:14].