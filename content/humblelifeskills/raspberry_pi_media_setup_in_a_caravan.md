---
title: Raspberry Pi media setup in a caravan
videoId: SUf2eKF-zYg
---

From: [[humblelifeskills]] <br/> 

## Current Setup

The current media setup in the caravan utilizes a [[Raspberry Pi]] as the core media player <a class="yt-timestamp" data-t="00:01:12">[00:01:12]</a>.

Key components include:
*   **IPS Screen**: A 99-pound IPS screen is mounted on the caravan wall, allowing it to be brought out or watched from bed <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.
*   **Kodi**: The [[Raspberry Pi]] runs Kodi (kodi.tv), a media player that links up various content sources <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Audio**: The system is connected to a sound dock for audio output <a class="yt-timestamp" data-t="00:01:38">[00:01:38]</a>.
*   **Storage and Network**: A [[Raspberry Pi]], a [[wifi_router_setup | router]], and a three-terabyte hard drive are all connected together in a put-together package within the caravan <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.

## Planned Upgrade

The current [[Raspberry Pi]] will be replaced with the new [[Raspberry Pi]] 2 <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>. The [[Raspberry Pi]] 2 is six times faster than the previous model and features:
*   One gigabyte of RAM <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>
*   Broadcom quad-core CPU <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>
*   Micro USB slot <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>
*   Four USB ports (two more than the original) <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>
*   Full-size HDMI port <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>
*   Four-pole stereo output and composite video port <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>

This upgrade will allow Kodi to take advantage of the extra power provided by the [[Raspberry Pi]] 2 <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. The older [[Raspberry Pi]] will be repurposed to run a [[using_raspberry_pi_for_minecraft_server_setup | Minecraft server]] for the owner's daughter <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.

## Future Project: The "Switchboard" Raspberry Pi Cluster

A new project, named "Switchboard," is planned to further enhance media and utility within the caravan <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. This project involves [[building_a_raspberry_pi_cluster_for_various_functions | building a Raspberry Pi cluster]] where individual [[Raspberry Pi]] units are stacked together, each performing a different function <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.

### Project Goals
*   **Diverse Functions**: Instead of a traditional cluster focused on one job, each "slice" of the [[Raspberry Pi]] hardware will perform a unique task <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Potential functions include:
    *   Kodi media playback <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>
    *   [[using_raspberry_pi_for_minecraft_server_setup | Minecraft server]] <a class="yt-timestamp" data-t="00:05:12">[00:05:12]</a>
    *   Mumble server (audio/teamspeak) <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>
    *   Graphing <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>
    *   Tweet wall <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>
    *   Dropcam preview <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>
    *   High-end audio file music server <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>
    *   Solar and power tracking <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>
    *   Network mapping and CPU analysis (using tools like Nagios) <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>
*   **Integrated Housing**: All components will fit inside a custom laser-cut box, which will be a [[designing_a_portable_raspberry_pi_cluster_box | portable cluster box]] that can be held and transported <a class="yt-timestamp" data-t="00:03:35">[00:03:35]</a>.
*   **Cooling System**: The box design incorporates case fans (e.g., Fractal Design Silent Series R2) at the bottom or top to manage airflow over the stacked [[Raspberry Pi]]s <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>.
*   **Caravan Integration**: The primary motivation for this project is to utilize existing cupboard spaces in the caravan <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. Sections of these cupboards, which are 13.3 inches across, will be cut out to install LCD screens <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>.
*   **Centralized Control**: Instead of installing a separate [[Raspberry Pi]] in each cupboard screen, the "Switchboard" unit will power different screens through a breakout and splitter system <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Portability and Versatility**: The box will allow for easy swapping of SD cards for different functions, enabling its use for [[implementing_raspberry_pi_for_event_and_educational_purposes | events and educational purposes]], such as training kids at Coda Dojo with a 10-user [[using_raspberry_pi_for_minecraft_server_setup | Minecraft server]] machine <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Documentation**: The project aims to provide image files of the custom [[Raspberry Pi]] installations for others to download and use on their own SD cards <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>.

### Development Process

The project will involve weekly iterations, acquiring a new [[Raspberry Pi]] unit each week and documenting its integration and function <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>. Challenges include:
*   **Power Management**: Designing a power solution for multiple units, such as a battery bank or a large power source with micro USB splitters <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>.
*   **Connectivity**: Integrating multiple Ethernet connections into a switch for ten units, potentially using custom or flat cabling <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.
*   **Audio Routing**: Determining how to route audio effectively from multiple units <a class="yt-timestamp" data-t="00:10:21">[00:10:21]</a>.
*   **Enclosure Design**: Continuously designing and refining the laser-cut wooden box with handles and other features based on the growing cluster <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>.