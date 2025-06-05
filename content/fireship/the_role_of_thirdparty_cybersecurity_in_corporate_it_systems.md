---
title: The role of thirdparty cybersecurity in corporate IT systems
videoId: 4yDm6xNeYas
---

From: [[fireship]] <br/> 

Third-party cybersecurity firms play a significant role in managing the security of modern corporate IT systems <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>. Large corporations often outsource their cybersecurity needs to these specialized companies, rather than maintaining extensive in-house teams <a class="yt-timestamp" data-t="00:03:29">[00:03:29]</a>. This approach is driven by the immense pressure on public mega-corporations to secure their computer systems and comply with constant audits by third parties <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

## How Third-Party Cybersecurity Operates

An example of such a firm is CrowdStrike, an enterprise cybersecurity company widely used by a substantial number of Fortune 500 companies, with over 500 clients on the Fortune 1000 list <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>.

CrowdStrike's primary product, Falcon, provides end-point protection <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. This tool uses artificial intelligence and analytics to detect threats in real-time <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Integration and Functionality
The Falcon sensor is installed like regular software but integrates with the operating system at a low level, often utilizing kernel mode drivers <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. It operates in the background, continuously monitoring for anomalies, collecting telemetry data, and generating reports <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.

Crucially, this kind of third-party software resides in the critical path of a computer, meaning its failure can lead to the failure of the entire system <a class="yt-timestamp" data-t="00:01:39">[00:01:39]</a>.

## Consequences of Failures

On July 19th, 2024, an automated software update pushed by CrowdStrike contained faulty code, causing millions, if not billions, of Windows computers worldwide to experience a "blue screen of death" <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. This incident led to significant disruptions:

*   Airports shutting down <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.
*   Hospitals being unable to treat patients <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.
*   Banks being unable to process transactions <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   The London Stock Exchange was disrupted <a class="yt-timestamp" data-t="00:02:13">[00:02:13]</a>.
*   Most Indian airports went down, leading to manual boarding pass issuance <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

CrowdStrike clarified that the incident was not a [[website_security_vulnerabilities | security incident]] or [[security_vulnerabilities_and_exploits | cyber attack]] <a class="yt-timestamp" data-t="00:02:22">[00:02:22]</a>. Instead, it was an issue with an [[impact_of_faulty_software_updates_on_global_systems | automated software update]] <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>. This event starkly highlighted the [[vulnerability_of_critical_infrastructures_to_software_errors | vulnerability of critical infrastructures to software errors]] <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a> and the [[lessons_learned_from_catastrophic_software_failures | lessons learned from catastrophic software failures]] <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a> when third-party software has deep system access <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. The [[challenges_with_automated_software_updates_and_system_safety | challenges with automated software updates and system safety]] were brought to the forefront <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

### Recovery Efforts
Restoring affected computers required specific steps, including booting into fail mode, manually removing the problematic driver (`c291.sys`), and reattaching the fixed volume to the impacted virtual server <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>. This process was complex and typically beyond the capabilities of most employees, requiring significant IT intervention <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. The incident necessitated extensive [[crisis_management_and_recovery_strategies_after_it_failures | crisis management and recovery strategies after IT failures]] across affected organizations.

## Implications for Corporate IT
The incident underscored that while third-party firms are hired to enhance security, giving them kernel access to widespread corporate systems can introduce a single point of failure <a class="yt-timestamp" data-t="00:03:41">[00:03:41]</a>. An automatic update with even a minor error can have global repercussions, nearly destroying entire systems <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. This also highlighted the [[consequences_of_software_glitches_in_financial_systems | consequences of software glitches in financial systems]] and other critical infrastructure.

<small>*(The information provided is based on the transcript from July 19th, 2024)*</small>