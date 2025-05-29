---
title: Impact of radiation on robotics technology
videoId: -ZJiVQ61MpQ
---

From: [[asianometry]] <br/> 

Robotics technology plays a crucial role in environments too hazardous for human presence, particularly in the aftermath of nuclear accidents where high radiation levels pose significant risks. The development and deployment of robots in such scenarios, like the [[development_and_deployment_of_fukushima_robots | Fukushima Daiichi Nuclear Power Plant]] disaster, necessitate specialized design considerations to ensure their functionality and survival amidst intense radiation exposure <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Historical Context and Need for Hardening
The use of robots in nuclear disaster response dates back to the 1979 Three Mile Island accident, where early robots like the Surveillance and In-Service Inspection Robot and Fred were employed for site inspection and decontamination in high-radiation areas <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. After the Chernobyl disaster, the Soviet Union initially relied on human "liquidators" due to extreme radiation levels causing available robots to fail, and bureaucratic issues <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. Eventually, specialized robots like the STR-1, adapted from an unmanned lunar vehicle, were brought in <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

At Fukushima, initial response efforts saw the deployment of US-made robots like the Pak-Bot and Warrior, which performed tasks such as measuring radiation, clearing obstacles, and vacuuming <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. However, their limitations, such as communication range and mobility over stairs, highlighted the need for more specialized and radiation-hardened designs <a class="yt-timestamp" data-t="00:05:56">[00:05:56]</a>. This led to a focus on making robotics technology resistant to the destructive effects of radiation.

## Effects of Radiation on Robotics Technology
A nuclear accident releases various types of radiation, including alpha particles, beta particles, gamma rays, x-rays, and neutron particles <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. When these particles interact with semiconductor materials, two primary effects can occur, leading to device degradation or failure:

*   **Displacement Effect**: Particles like neutrons and alpha particles can collide with a semiconductor, displacing its atoms and shifting their structural arrangements <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>. This alters the device's properties, resulting in issues like increased current leakage and decreased lifetime <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.
*   **Ionization Effect**: Electrons, protons, and x-rays passing through semiconductors create electron-hole pairs <a class="yt-timestamp" data-t="00:07:36">[00:07:36]</a>. This can cause permanent glitches or abruptly strange behavior in the electronic components <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

Either of these effects can immediately disable a device, or their cumulative impact over time can lead to a complete system failure <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>. Damage can occur at multiple levels: device, circuit, and system <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

## Radiation Hardening Techniques
To counteract the impact of radiation, "radiation hardening" (rad-hard) techniques are applied at various levels of a robot's design:

*   **Device Level**: This involves modifying individual components like transistors. Techniques include changing the transistor layout, adding insulating substrates (e.g., using a silicon-on-insulator fabrication approach), or making the device physically larger, as bigger gate sizes have higher current capacities <a class="yt-timestamp" data-t="00:08:10">[00:08:10]</a>.
*   **Circuit Level**: For circuits composed of multiple devices, radiation hardening can involve duplicating critical circuits or adding monitoring circuits that oversee the main circuit for damage <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. These protections are primarily hardware-based <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.
*   **System Level**: At this level, software can be integrated alongside hardware solutions. Beyond obvious measures like adding physical radiation armor and redundancies, preventive scrubbing algorithms can be introduced to correct or "scrub" errors <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>.

## Case Study: Kinsei Robot at Fukushima
The [[international_and_domestic_robotics_contributions_to_disaster_response | Kinsei series of robots]], developed by the Neito project at the Chiba Institute of Technology, exemplifies a successful application of radiation hardening in disaster response <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>. Originally designed for search and rescue in difficult terrain, Kinsei robots were modified for the Fukushima mission by hardening them against radioactivity <a class="yt-timestamp" data-t="00:06:51">[00:06:51]</a>.

Initially, the team was uncertain about Kinsei's radiation resistance as it was built from conventional electronics <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>. Extensive gamma ray testing was performed on its critical components, including the 180-nanometer CPU, motherboard, and motor driver boards <a class="yt-timestamp" data-t="00:09:14">[00:09:14]</a>. The tests revealed that Kinsei's essential components could survive a dose of approximately 200 grays (20,000 rads) <a class="yt-timestamp" data-t="00:09:20">[00:09:20]</a>. Given initial measurements at Fukushima were around 100 grays, the team calculated that Kinsei could operate for over 100 hours with about a 10% chance of failure <a class="yt-timestamp" data-t="00:09:26">[00:09:26]</a>.

Modified Kinsei robots were successfully deployed in June 2011 for critical missions such as installing water gauges and taking samples of contaminated water in the reactor building basement, tasks unachievable by earlier robots due to communication and mobility constraints <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>. Although one Kinsei was abandoned after a broken communication link, subsequent models (Kinsei 2 and 3) were redesigned to address this flaw <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

The ongoing decommissioning and cleanup at Fukushima continue to rely on specialized radiation-hardened robots, like the "Mini Manbo," which successfully recorded video of nuclear debris in highly flooded and inaccessible areas of Unit 3 <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>. These efforts demonstrate the critical and evolving role of radiation-hardened robotics in addressing the long-term challenges of nuclear disaster recovery.