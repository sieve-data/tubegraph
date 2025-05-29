---
title: Challenges faced by robots in highradiation areas
videoId: -ZJiVQ61MpQ
---

From: [[asianometry]] <br/> 

Robots are deployed in hazardous, high-radiation environments like nuclear power plants to minimize human safety risks during decommissioning efforts <a class="yt-timestamp" data-t="00:24:19"></a>. However, these environments pose significant [[Robotics in nuclear disaster response | challenges]] for robotic systems.

## Effects of Radiation on Robotics

A nuclear accident releases various types of radiation, including alpha particles, beta particles, gamma rays, x-rays, and neutron particles <a class="yt-timestamp" data-t="07:02:18"></a>. When these particles interact with semiconductor materials, they can cause two primary effects:

*   **Displacement Effect**: Particles like neutrons and alpha particles can collide with a semiconductor, displacing its atoms and altering its structural arrangements <a class="yt-timestamp" data-t="07:16:18"></a>. This leads to changes in the device's properties, such as increased current leakage and decreased lifespan <a class="yt-timestamp" data-t="07:27:57"></a>.
*   **Ionization Effect**: Electrons, protons, and x-rays passing through semiconductors can create electron-hole pairs <a class="yt-timestamp" data-t="07:36:09"></a>. This can result in permanent glitches and unpredictable behavior <a class="yt-timestamp" data-t="07:44:40"></a>.

Either of these effects can disable a system directly, or their cumulative impact over time can lead to a complete breakdown <a class="yt-timestamp" data-t="07:50:20"></a>. This damage occurs at multiple levels: device, circuit, and system <a class="yt-timestamp" data-t="08:01:45"></a>.

## Radiation Hardening Strategies

To counter these effects, radiation hardening must be applied at all levels:

*   **Device Level**: This involves modifying components like transistors <a class="yt-timestamp" data-t="08:10:39"></a>. Strategies include changing transistor layouts, adding insulating substrates (e.g., using silicon on insulator fabrication), or increasing the size of devices (larger gate sizes have higher current capacities) <a class="yt-timestamp" data-t="08:14:46"></a>.
*   **Circuit Level**: Since circuits are composed of multiple devices, hardening at this level includes duplicating critical circuits or incorporating additional circuits to monitor the main circuit for damage <a class="yt-timestamp" data-t="08:29:43"></a>.
*   **System Level**: Beyond hardware-based protections, system-level designs can incorporate software benefits <a class="yt-timestamp" data-t="08:42:55"></a>. Obvious measures include adding physical radiation armor and building in redundancies <a class="yt-timestamp" data-t="08:47:49"></a>. Software can introduce preventive scrubbing algorithms to correct errors <a class="yt-timestamp" data-t="08:51:39"></a>.

## Real-World Challenges and Robot Failures

The robot named Kinsei, developed by the Neito Project at the Chiba Institute of Technology, was originally designed as a search and rescue robot and was made from conventional electronics <a class="yt-timestamp" data-t="08:56:10"></a> <a class="yt-timestamp" data-t="06:25:21"></a>. When modified for Fukushima, its radiation resistance was unknown <a class="yt-timestamp" data-t="08:56:10"></a>. Initial concerns suggested the need for a 2-centimeter-thick lead plate, which would add significant weight and potentially hinder the mission <a class="yt-timestamp" data-t="09:03:09"></a>.

Gamma ray testing revealed that Kinsei's essential components (including its 180-nanometer CPU, motherboard, and motor driver boards) could withstand a dose of about 200 grays (20,000 rads) <a class="yt-timestamp" data-t="09:13:30"></a>. Given that initial radiation measurements at Fukushima were around 100 grays, it was determined Kinsei could operate for over 100 hours with only a 10% chance of failure <a class="yt-timestamp" data-t="09:26:08"></a>.

Despite these measures, real-world deployment still faced [[Challenges faced in Soviet space program | challenges]]:
*   The first Kinsei robot was abandoned in October 2011 after five successful missions due to a broken communication link on the third floor of the reactor building <a class="yt-timestamp" data-t="09:45:16"></a>. Kinsei 2 and 3 were redesigned to address this flaw <a class="yt-timestamp" data-t="09:54:19"></a>.
*   The Scorpion robot, designed to inspect Unit 2, was deployed in 2017 but its left tread failed for unknown reasons once inside, leading to its abandonment <a class="yt-timestamp" data-t="13:40:07"></a>.
*   Other robots, like the Pakbot, faced limitations due to their radio communication range and inability to easily navigate stairs <a class="yt-timestamp" data-t="05:56:22"></a>.

These incidents highlight the persistent [[Challenges in Semiconductor Lithography | challenges]] of operating complex robotic systems in extremely harsh, high-radiation environments.