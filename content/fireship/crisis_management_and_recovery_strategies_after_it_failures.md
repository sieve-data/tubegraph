---
title: Crisis management and recovery strategies after IT failures
videoId: 4yDm6xNeYas
---

From: [[fireship]] <br/> 

On July 19th, 2024, a major IT crisis unfolded as millions, potentially billions, of Windows computers worldwide experienced a "blue screen of death" <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This widespread failure was attributed to an update pushed by the enterprise cybersecurity firm CrowdStrike <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>.

## The Nature of the Failure

The incident was caused by an automated software update from CrowdStrike's Falcon product that contained "bad code" <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>. CrowdStrike's Falcon sensor integrates with the operating system at a low level, often using kernel mode drivers <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a>. As [[the_role_of_thirdparty_cybersecurity_in_corporate_it_systems | third-party software]] that sits in the critical path of a computer, its failure led to the entire system failing <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

The incident was explicitly stated by CrowdStrike not to be a security incident or a cyber attack <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

## Immediate Impact and Critical System Vulnerability

The [[impact_of_faulty_software_updates_on_global_systems | impact]] of this widespread failure was significant and immediate:
*   Airports began shutting down <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   Hospitals were unable to treat patients <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   Banks could not process money <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   The London Stock Exchange was disrupted <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   Most Indian airports ceased operations, requiring manual boarding pass writing <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.
*   Corporate America entered "panic mode" as work computers were bricked <a class="yt-timestamp" data-t="00:00:43">[00:00:43]</a>.

This event highlighted the [[vulnerability_of_critical_infrastructures_to_software_errors | vulnerability of critical infrastructures]] to software errors, especially when a single point of failure (like a widely-used third-party security product) has deep system access <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>.

## Recovery Strategies and Challenges

The nature of the IT failure presented unique challenges for recovery:
*   Affected computers required a reboot in "fail mode" <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   The problematic driver had to be removed manually <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
*   Most employees lacked the necessary access to perform these steps independently <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>, leading to IT departments being overwhelmed <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

CrowdStrike quickly provided a fix, albeit a technically complex one for the average user:
1.  Detach the operating system disk <a class="yt-timestamp" data-t="00:02:36">[00:02:36]</a>.
2.  Create a snapshot or backup of the disk <a class="yt-timestamp" data-t="00:02:37">[00:02:37]</a>.
3.  Mount a volume to a new virtual server <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
4.  Navigate to the `winder` drivers directory <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
5.  Locate and delete the file `c291.SYS` <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
6.  Detach the volume from the new virtual server <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
7.  Reattach the fixed volume to the impacted virtual server <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

An alternative, albeit facetious, suggestion for users was to uninstall Microsoft Windows and switch to Linux <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

## Lessons Learned and Implications for IT Management

This event served as a stark reminder of [[lessons_learned_from_catastrophic_software_failures | lessons learned from catastrophic software failures]].
*   The reliance on [[the_role_of_thirdparty_cybersecurity_in_corporate_it_systems | third-party cybersecurity]] solutions, while seemingly offloading responsibility, can introduce a new, centralized point of failure if that vendor has deep system access <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>.
*   The "cure" (a security update) proved more harmful than the "disease" (potential threats) in this specific instance <a class="yt-timestamp" data-t="00:03:19">[00:03:19]</a>.
*   Even a "misplaced zero" in an automatic update can have global consequences <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>.

The incident highlights the critical need for robust testing protocols, rollback capabilities, and diverse system architecture to prevent single points of failure, especially concerning deeply integrated system components.