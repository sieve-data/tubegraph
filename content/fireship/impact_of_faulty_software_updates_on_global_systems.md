---
title: Impact of faulty software updates on global systems
videoId: 4yDm6xNeYas
---

From: [[fireship]] <br/> 

On July 19th, 2024, a routine software update pushed by the enterprise cyber security firm CrowdStrike led to widespread disruption, causing millions, if not billions, of Windows computers to become inoperable with a blue screen of death <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a> <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. This incident demonstrated the significant [[vulnerability_of_critical_infrastructures_to_software_errors | vulnerability of critical infrastructures]] and the global economy to errors in system-level software <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## The CrowdStrike Incident

Corporate America entered a state of panic as work computers worldwide were "bricked" <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. A large number of Fortune 500 companies, over 500 clients on the Fortune 1000 list, rely on CrowdStrike for their cyber security <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a> <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

### CrowdStrike's Falcon Product

CrowdStrike's primary product, Falcon, is an endpoint protection tool that uses artificial intelligence and analytics to detect threats in real-time <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a> <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The Falcon sensor integrates with the operating system at a low level, often utilizing kernel mode drivers, constantly running in the background to monitor for anomalies <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a> <a class="yt-timestamp" data-t="00:01:23">[00:01:23]</a> <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. This design means it resides in the "critical path" of a computer, implying that its failure could lead to the entire system failing <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.

### The Root Cause

An [[challenges_with_automated_software_updates_and_system_safety | automated software update]] pushed by CrowdStrike contained faulty code <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a> <a class="yt-timestamp" data-t="00:01:49">[00:01:49]</a>. Every Windows computer that received this update became inoperable <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>. Mac OS and Linux users were unaffected by this particular incident <a class="yt-timestamp" data-t="00:01:11">[00:01:11]</a>.

## Global Consequences

The [[impact_of_software_bugs_on_different_industries | consequences of this software glitch]] were severe and far-reaching:

*   **Transportation:** Airports, including most Indian airports, experienced shutdowns, leading to manual boarding pass issuance <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a> <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Healthcare:** Hospitals were rendered unable to treat patients <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Finance:** Banks faced issues accessing money, and the London Stock Exchange was disrupted <a class="yt-timestamp" data-t="00:01:18">[00:01:18]</a> <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>. This highlights the [[consequences_of_software_glitches_in_financial_systems | severe consequences of software glitches in financial systems]].
*   **General Business:** Millions of corporate Windows computers globally were rendered unusable <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a> <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>.

CrowdStrike clarified that this was not a [[security_vulnerabilities_and_exploits | security incident]] or a cyber attack, but rather an internal error <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a> <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.

### Challenges in Recovery

The recovery process for affected machines was complex and required manual intervention:

*   Each affected computer needed to be rebooted in "fail mode" to allow for the manual removal of the problematic driver <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a> <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.
*   Most employees lack the necessary permissions or technical knowledge to perform this intricate process <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a> <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>.
*   The described "easy" fix involved detaching the operating system disk, creating snapshots, mounting volumes to new virtual servers, navigating to specific directories, deleting a particular file (`c291.SYS`), and then reattaching the fixed volume <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   This situation placed an immense burden on IT departments, likened to being a surgeon in World War I <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a> <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Broader Implications

The incident underscored a critical vulnerability in modern IT infrastructure:

> [03:00:59] "What we have here is a situation where the cure is more harmful than the disease." <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>

Public corporations are under immense pressure to secure their systems and are frequently audited by third parties <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a> <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. Instead of building large internal cybersecurity teams, many opt to pay firms like CrowdStrike millions annually to handle their security <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a> <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. This provides a third party to blame if their system is hacked <a class="yt-timestamp" data-t="00:03:38">[00:03:38]</a>.

However, a key oversight was allowing a single company kernel access to the computers of most Fortune 500 companies <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a> <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This centralization meant that a single [[challenges_with_automated_software_updates_and_system_safety | automatic update]] with a "misplaced zero" could nearly destroy the entire world's IT infrastructure, demonstrating a profound [[lessons_learned_from_catastrophic_software_failures | lesson learned from catastrophic software failures]] <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a> <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This event will likely prompt discussions on [[crisis_management_and_recovery_strategies_after_it_failures | crisis management and recovery strategies]] for future IT failures.