---
title: Designing a portable Raspberry Pi cluster box
videoId: SUf2eKF-zYg
---

From: [[humblelifeskills]] <br/> 

A new project, temporarily named "Switchboard," aims to build a portable cluster box housing multiple [[Building a Raspberry Pi cluster for various functions | Raspberry Pis]] for diverse functions, moving beyond the traditional single-job computing cluster <a class="yt-timestamp" data-t="02:07:10">[02:07:10]</a>.

## The "Switchboard" Concept

The core idea is to have individual [[Building a Raspberry Pi cluster for various functions | Raspberry Pi]] units, stacked together in a "cluster configuration," but each performing a different function <a class="yt-timestamp" data-t="04:47:39">[04:47:39]</a>. This contrasts with a traditional cluster where multiple Pis compute a single task <a class="yt-timestamp" data-t="04:38:09">[04:38:09]</a>. The project involves sketching out numerous ideas for functionality and design <a class="yt-timestamp" data-t="01:59:04">[01:59:04]</a>.

## Project Goals and Functions

The goal is to create a multi-functional, portable system <a class="yt-timestamp" data-t="10:57:48">[10:57:48]</a>. Planned functions for the individual Raspberry Pi "slices" include:
*   **Media Playback** <a class="yt-timestamp" data-t="05:09:47">[05:09:47]</a>: Primarily running Kodi (kodi.tv) as a media player <a class="yt-timestamp" data-t="01:15:36">[01:15:36]</a> <a class="yt-timestamp" data-t="05:09:47">[05:09:47]</a>. The current [[raspberry_pi_media_setup_in_a_caravan | caravan media setup]] uses an older Raspberry Pi with Kodi connected to a sound dock, router, and a three-terabyte drive <a class="yt-timestamp" data-t="01:36:20">[01:36:20]</a> <a class="yt-timestamp" data-t="01:45:01">[01:45:01]</a>.
*   **[[Using Raspberry Pi for Minecraft server setup | Minecraft Server]]** <a class="yt-timestamp" data-t="05:12:12">[05:12:12]</a>: Inspired by a daughter's request to run Minecraft <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. A new [[Using Raspberry Pi for Minecraft server setup | Raspberry Pi 2]] will be used for this, with the older Pi being transferred to the daughter <a class="yt-timestamp" data-t="02:54:19">[02:54:19]</a>.
*   **Mumble Server** <a class="yt-timestamp" data-t="05:14:02">[05:14:02]</a>: For audio communication, similar to TeamSpeak <a class="yt-timestamp" data-t="05:14:48">[05:14:48]</a>.
*   **Graphing and Tweet Walls** <a class="yt-timestamp" data-t="05:19:15">[05:19:15]</a> <a class="yt-timestamp" data-t="07:37:34">[07:37:34]</a>.
*   **Dropcam Preview** <a class="yt-timestamp" data-t="05:21:49">[05:21:49]</a>.
*   **Audio Pi** <a class="yt-timestamp" data-t="05:22:24">[05:22:24]</a>: For high-end audio file music serving <a class="yt-timestamp" data-t="05:23:46">[05:23:46]</a>.
*   **Solar and Power Tracking** <a class="yt-timestamp" data-t="05:25:27">[05:25:27]</a> <a class="yt-timestamp" data-t="07:40:24">[07:40:24]</a>.
*   **Newsletter Sign-up** <a class="yt-timestamp" data-t="05:29:08">[05:29:08]</a>: Potentially for event use <a class="yt-timestamp" data-t="05:30:26">[05:30:26]</a>.
*   **Network Mapping and CPU Analysis** <a class="yt-timestamp" data-t="08:28:13">[08:28:13]</a>: Using tools like Nagios <a class="yt-timestamp" data-t="08:32:00">[08:32:00]</a> to monitor individual Pi performance <a class="yt-timestamp" data-t="08:35:05">[08:35:05]</a>.

The project intends to develop images/files for each function, making them downloadable for users to easily load onto an SD card and use <a class="yt-timestamp" data-t="09:42:04">[09:42:04]</a>.

## Hardware Specifications and Design Elements

The project will primarily use the new [[Rackmount servers specifications | Raspberry Pi 2]], which is six times faster than the previous model <a class="yt-timestamp" data-t="02:48:47">[02:48:47]</a>. Its specifications include:
*   One gigabyte of RAM <a class="yt-timestamp" data-t="03:12:00">[03:12:00]</a>
*   Broadcom quad-core CPU <a class="yt-timestamp" data-t="03:17:41">[03:17:41]</a>
*   Micro USB slot for power <a class="yt-timestamp" data-t="03:21:04">[03:21:04]</a>
*   Four USB ports (two more than the previous model) <a class="yt-timestamp" data-t="03:21:921">[03:21:921]</a>
*   Full-size HDMI port <a class="yt-timestamp" data-t="03:25:471">[03:25:471]</a>
*   Four-pole stereo output <a class="yt-timestamp" data-t="03:25:991">[03:25:991]</a>
*   Composite video port <a class="yt-timestamp" data-t="03:27:081">[03:27:081]</a>
The Raspberry Pi is described as a "computer in a box," a UK invention from Cambridge, costing around 30-35 pounds for the unit <a class="yt-timestamp" data-t="03:46:121">[03:46:121]</a> <a class="yt-timestamp" data-t="04:07:051">[04:07:051]</a>.

The portable box will be:
*   **Laser-cut** <a class="yt-timestamp" data-t="05:35:051">[05:35:051]</a>, with a design that allows for handles <a class="yt-timestamp" data-t="12:01:21">[12:01:21]</a>.
*   **Cooled** using Fractal Design Silent Series R2 case fans <a class="yt-timestamp" data-t="05:41:091">[05:41:091]</a> <a class="yt-timestamp" data-t="05:43:081">[05:43:081]</a>. The fans will create airflow, pulling air in from the top and exhausting at the bottom, or vice-versa, depending on configuration <a class="yt-timestamp" data-t="06:12:081">[06:12:081]</a>. An aluminum filter will be placed at the bottom <a class="yt-timestamp" data-t="09:21:041">[09:21:041]</a>.
*   **Powered** by either a bank of batteries or a large power source with split micro USBs <a class="yt-timestamp" data-t="10:02:11">[10:02:11]</a>. Reset switches are also being considered <a class="yt-timestamp" data-t="10:10:041">[10:10:041]</a>.
*   **Connected** via Ethernet to a switch, possibly a 10-port or 4-gigabit switch, using flat cabling to save space <a class="yt-timestamp" data-t="10:24:26">[10:24:26]</a> <a class="yt-timestamp" data-t="10:39:12">[10:39:12]</a>.

## Integration and Portability

The "Switchboard" is designed to solve a problem in the caravan, allowing for centralized management of [[raspberry_pi_media_setup_in_a_caravan | Raspberry Pi]] units instead of having separate ones in each location <a class="yt-timestamp" data-t="10:49:15">[10:49:15]</a>. It's intended to fit into 13.3-inch cupboards in the caravan, which can be fitted with LCD screens <a class="yt-timestamp" data-t="06:47:041">[06:47:041]</a> <a class="yt-timestamp" data-t="07:00:031">[07:00:031]</a>. The central unit will power different screens via a breakout and splitter system <a class="yt-timestamp" data-t="09:04:12">[09:04:12]</a>.

> [!NOTE] Current Caravan Media Setup
> The caravan currently uses a 99-pound IPS screen mounted on the wall, allowing viewing from bed <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>. This screen is connected to a Raspberry Pi running Kodi <a class="yt-timestamp" data-t="01:12:02">[01:12:02]</a>. The [[raspberry_pi_media_setup_in_a_caravan | Raspberry Pi]], a router, and a three-terabyte drive are connected together in a neat package within the caravan <a class="yt-timestamp" data-t="01:45:01">[01:45:01]</a>.

Beyond the caravan, the box will be portable, allowing [[Implementing Raspberry Pi for event and educational purposes | taking it to different events]] and swapping SD cards for various functions <a class="yt-timestamp" data-t="10:57:48">[10:57:48]</a>. Examples include:
*   A channel manager for multi-screen displays <a class="yt-timestamp" data-t="11:08:18">[11:08:18]</a>.
*   [[Implementing Raspberry Pi for event and educational purposes | Training kids at Coda Dojo]] by having the box with different SD cards for [[Using Raspberry Pi for Minecraft server setup | Minecraft]] <a class="yt-timestamp" data-t="11:26:01">[11:26:01]</a>. This could enable a 10-user machine in a small box, linked to screens already at the venue <a class="yt-timestamp" data-t="11:34:03">[11:34:03]</a>.
The possibility of offering a wooden sleeve for clients to hire the box is also being considered <a class="yt-timestamp" data-t="11:16:03">[11:16:03]</a>.

## Project Development and Future Plans

The project is planned to be developed weekly, depending on budget, with the aim of adding a new [[Building a Raspberry Pi cluster for various functions | Raspberry Pi]] to the stack each week <a class="yt-timestamp" data-t="04:19:07">[04:19:07]</a> <a class="yt-timestamp" data-t="07:56:06">[07:56:06]</a>. Each addition will be accompanied by a video demonstrating its utilization <a class="yt-timestamp" data-t="08:04:06">[08:04:06]</a>. While a single [[Dell PowerEdge 2650 server features | Raspberry Pi 2]] could handle multiple functions due to its speed, the preference is for individual units for clarity and modularity <a class="yt-timestamp" data-t="08:12:09">[08:12:09]</a>.

The process is expected to be messy initially but will iterate over time <a class="yt-timestamp" data-t="10:14:14">[10:14:14]</a>. Considerations for future development include:
*   Making some Pis headless <a class="yt-timestamp" data-t="10:19:07">[10:19:07]</a>.
*   Audio routing strategies <a class="yt-timestamp" data-t="10:21:04">[10:21:04]</a>.
*   Integrating Ethernet into a switch <a class="yt-timestamp" data-t="10:24:26">[10:24:26]</a>.
*   Designing the external box using 3D laser-cut wood <a class="yt-timestamp" data-t="11:51:01">[11:51:01]</a>.