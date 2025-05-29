---
title: Resetting Bluetooth settings
videoId: IEl4LRnSbe4
---

From: [[dr_tutoriales]] <br/> 

This guide outlines how to configure and re-initialize the Bluetooth service on a Windows 10 computer, a process that can effectively reset its operational state and resolve connectivity issues <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>.

## Configure Bluetooth Compatibility Service

The first step involves adjusting the settings of the Bluetooth compatibility service to ensure it starts automatically and is properly initialized.

1.  **Access Services**: Navigate to the Windows search bar (or "home bar") <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a> and type "services" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Select the "Services" application from the results to open the Services window <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
2.  **Locate Bluetooth Compatibility Service**: Within the Services window, scroll through the alphabetical list to find "Bluetooth compatibility service" <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a> <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
3.  **Access Properties**: Right-click on "Bluetooth compatibility service" and select "Properties" <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>.
4.  **Set Startup Type to Automatic**: In the Properties window, set the "Startup type" to "Automatic" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. This ensures the service starts automatically with Windows, a key step in [[setting_bluetooth_service_to_automatic | setting Bluetooth service to automatic]] <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
5.  **Apply and Accept Changes**: Click "Apply" and then "OK" to save the changes <a class="yt-timestamp" data-t="00:01:52">[00:01:52]</a>.
6.  **Restart the Service**: Right-click on "Bluetooth compatibility service" again and select "Restart" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>. This step re-initializes the service with the new settings <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. Wait for the service to restart <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.

## Verify Bluetooth Icon Visibility

After configuring the service, ensure the Bluetooth icon is visible in the notification area for easy access.

1.  **Open Bluetooth Settings**: Close the Services window <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. Go back to the Windows search bar and type "Bluetooth" <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. Select "Bluetooth & other devices settings" <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
2.  **Access More Bluetooth Options**: In the "Bluetooth & other devices" window, click on "More Bluetooth options" located on the right side <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
3.  **Enable Notification Area Icon**: Ensure the checkbox for "Show Bluetooth icon in the notification area" is selected <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>. If it's not, check it and click "OK" <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. This will make the Bluetooth icon visible, indicating that Bluetooth is enabled on the computer <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. This contributes to [[activating_bluetooth_on_windows_10 | activating Bluetooth on Windows 10]] <a class="yt-timestamp" data-t="00:00:06">[00:00:06]</a>.

## Connecting a Mobile Device (Demonstration)

To verify the Bluetooth functionality, you can attempt to [[connecting_mobile_device_via_bluetooth | connect a mobile device]] to your computer.

1.  **Navigate to Bluetooth & other devices**: Return to the "Bluetooth & other devices" settings <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>.
2.  **Add a Device**: Click on "Add Bluetooth or other device" <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.
3.  **Select Bluetooth Device**: Choose "Bluetooth" from the options <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.
4.  **Pair Device**: Your mobile device (e.g., iPhone) should appear in the list <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>. Select it, and accept the connection request on both your computer and the mobile device <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.
5.  **Confirm Connection**: Once linked, the device will be ready to communicate <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

This process ensures your Bluetooth service is properly configured and running, which can resolve various connectivity issues.