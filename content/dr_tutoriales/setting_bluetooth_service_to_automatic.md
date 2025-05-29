---
title: Setting Bluetooth service to automatic
videoId: IEl4LRnSbe4
---

From: [[dr_tutoriales]] <br/> 

This article outlines the process for [[activating_bluetooth_on_windows_10 | activating Bluetooth]] on a Windows 10 computer by setting its compatibility service to automatic startup, ensuring it functions correctly <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>. This method is essential for smooth [[troubleshooting_bluetooth_connectivity | Bluetooth connectivity]] and device pairing <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## Steps to Set Bluetooth Service to Automatic

Follow these steps to configure the Bluetooth service:

### 1. Access Services Window
The first step is to access the 'Services' management console <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.
*   Navigate to the Windows Home bar <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>.
*   Search for "services" <a class="yt-timestamp" data-t="00:00:51">[00:00:51]</a>.
*   Open the 'Services' window that appears <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

### 2. Locate Bluetooth Compatibility Service
Within the 'Services' window, you need to find the specific Bluetooth service <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.
*   Scroll through the list of services to find "Bluetooth compatibility" <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>, also referred to as "Service of Bluetooth compatibility" <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
    *   *Note:* Services are typically listed in alphabetical order <a class="yt-timestamp" data-t="00:01:34">[00:01:34]</a>.

### 3. Configure Service Properties
Once found, configure the service's startup properties:
*   Right-click on "Service of Bluetooth compatibility" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
*   Select "Properties" from the context menu <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>.
*   In the 'Properties' window, set the 'Startup type' to "Automatic" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>.
*   Click "Apply" and then "Accept" (or "OK") to save the changes <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.

### 4. Restart the Service
To apply the changes immediately, the service needs to be restarted <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   Right-click on "Service of Bluetooth compatibility" again <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   Select "Restart" <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This [[resetting_bluetooth_settings | resets]] the changes implemented on the computer's Bluetooth system <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.
*   Confirm the restart if prompted <a class="yt-timestamp" data-t="00:02:10">[00:02:10]</a>.

### 5. Verify Bluetooth Settings (Optional but Recommended)
After configuring the service, it's good practice to verify the Bluetooth settings in Windows <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   Close the 'Services' window <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   Go back to the taskbar <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   Search for "Bluetooth" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   Open "Bluetooth settings and other devices" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
*   Click on "More options Bluetooth" on the right side <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   Ensure the "Show the Bluetooth icon in the notification area" option is selected <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. This will make the Bluetooth symbol visible, indicating it's enabled <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

## Demonstrating Bluetooth Connectivity

Once activated, you can connect a [[connecting_mobile_device_via_bluetooth | mobile device]] to your computer via Bluetooth <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

*   Go to "Bluetooth and other Devices" settings <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
*   Click "Add Bluetooth or other devices" <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
*   Select the device you wish to add <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
*   For example, an iPhone can be selected from the list of available devices <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.
*   On the [[connecting_mobile_device_via_bluetooth | mobile device]], accept the connection request from the computer <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
*   Once linked, the devices are ready to communicate and transmit data <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.