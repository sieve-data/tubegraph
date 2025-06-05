---
title: Challenges with automated software updates and system safety
videoId: 4yDm6xNeYas
---

From: [[fireship]] <br/> 

On July 19th, 2024, millions, if not billions, of Windows computers worldwide were rendered inoperable, commonly referred to as "instabricked," due to a faulty automated software update [00:00:07]. This incident, which led to a widespread "blue screen of death," highlights significant [[Impact of faulty software updates on global systems | challenges with automated software updates]] and their profound impact on system safety [00:00:05].

## The CrowdStrike Incident

The disruption was caused by an update pushed by Enterprise cybersecurity firm CrowdStrike [00:00:11]. CrowdStrike, a publicly traded company whose primary product is Falcon, provides endpoint protection using artificial intelligence and analytics to detect real-time threats [00:00:57]. A substantial number of Fortune 500 companies, including over 500 clients on the Fortune 1000 list, rely on CrowdStrike for their cybersecurity [00:00:49].

The Falcon sensor integrates with the operating system at a low level, often using kernel mode drivers, constantly monitoring for anomalies [00:01:23]. As third-party software positioned in a computer's critical path, its failure can lead to the entire system failing [00:01:39]. This is precisely what occurred when an automated software update contained "bad code" [00:01:48]. While CrowdStrike was quick to clarify it was not a security incident or cyberattack [00:02:21], the incident effectively "messed up the global economy" [00:00:28].

## Widespread Consequences

The faulty update led to severe operational disruptions across various critical sectors:
*   [[Vulnerability of critical infrastructures to software errors | Airports were forced to shut down]] [00:00:15], with most Indian airports going down and resorting to writing boarding passes by hand [00:02:15].
*   [[Vulnerability of critical infrastructures to software errors | Hospitals were unable to treat patients]] [00:00:16].
*   [[Vulnerability of critical infrastructures to software errors | Banks were unable to process money]] [00:00:17].
*   The London Stock Exchange experienced disruptions [00:02:13].
*   Corporate America entered "panic mode" as work computers were bricked [00:00:44].

The fix for affected computers was complex and required manual intervention: users needed to reboot in "fail mode" to manually remove the faulty driver [00:01:58]. The specific technical steps involved detaching the operating system disk, creating a snapshot, mounting a volume to a new virtual server, navigating to the `winder` driver's directory, locating and deleting the `c291.SYS` file, then detaching and reattaching the fixed volume to the impacted virtual server [00:02:35]. Most employees lacked the access to perform these steps independently, placing a significant burden on IT departments [00:02:04].

## Systemic Vulnerabilities

This [[Lessons learned from catastrophic software failures | catastrophic mistake]] highlights a critical vulnerability in modern IT infrastructure [00:00:36]. Companies often opt to pay third-party firms like CrowdStrike millions of dollars annually to handle cybersecurity, providing a convenient entity to blame if systems are hacked [00:03:33]. However, granting a single company kernel access to the computers of most Fortune 500 companies poses a significant risk [00:03:41]. It demonstrates that it "only takes one automatic update with a misplaced zero to nearly destroy the entire world" [00:03:49]. This incident underscores that, in some cases, the "cure is more harmful than the disease" [00:03:19].