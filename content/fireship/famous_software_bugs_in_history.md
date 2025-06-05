---
title: Famous software bugs in history
videoId: Iq_r7IcNmUk
---

From: [[fireship]] <br/> 

Software bugs, often dismissed with the phrase "it's not a bug, it's a feature" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, can have serious real-world consequences, ranging from minor annoyances to catastrophic failures <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. This article explores significant historical software bugs and their impact.

## Origin of "It's a Feature"

The phrase "it's not a bug, it's a feature" is often used by programmers to justify problematic code <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. One famous instance where this "excuse" became an actual feature was in the original *Sid Meier's Civilization* game <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>.

*   **Gandhi's Nuclear Aggression**
    *   **Year:** Original *Civilization* game <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>
    *   **What happened:** Gandhi's aggression level was set to an unsigned integer of one, making him a pacifist <a class="yt-timestamp" data-t="00:00:09">[00:00:09]</a>. When another civilization adopted diplomacy, it reduced aggression by two <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. This resulted in `1 - 2 = 255`, an unsigned integer underflow <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>, maxing out Gandhi's aggression and turning him into a "thermonuclear enthusiast" <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>.
    *   **Consequence:** Players enjoyed this bug so much it became an urban legend and a deliberate feature in later games <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.

## Tier 1: Surface-Level Bugs

### Zune Bug
*   **Year:** 2008 <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>
*   **What happened:** On December 31st, 2008, every Microsoft Zune device globally froze and became inoperable, displaying a loading bar stuck at 100% <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.
*   **Technical Cause:** The device's software was not programmed to account for the extra day in a leap year <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>. Upon reaching the 366th day of a leap year, a logic error in handling the day count caused the device to enter an inescapable loop and freeze <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.
*   **Consequence:** Devices could only be fixed manually by removing the battery <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Pentium FDIV Bug
*   **Year:** 1994 <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>
*   **What happened:** Intel's Pentium chip occasionally returned an incorrect value during floating-point division <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. This occurred in about 1 in 9 billion division operations <a class="yt-timestamp" data-t="00:01:45">[00:01:45]</a>.
*   **Technical Cause:** The core issue was related to the SRT division algorithm, specifically, five missing entries in a 1,066-entry lookup table used to speed up division <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. This caused certain number combinations to return incorrect results at the hardware level <a class="yt-timestamp" data-t="00:02:16">[00:02:16]</a>.
*   **Consequence:** Intel initially downplayed the issue, but IBM suspended the use of Intel chips in their PCs, leading to a massive PR crisis <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

### Apple FaceTime Eavesdropping Bug
*   **Year:** 2019 <a class="yt-timestamp" data-t="00:02:23">[00:02:23]</a>
*   **What happened:** A [[security_vulnerabilities_and_exploits | security vulnerability]] allowed iPhone users to eavesdrop on the audio of another person's phone during a FaceTime call before they even answered <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. If the recipient pressed the power button to dismiss the call, their camera would also activate <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>.
*   **Technical Cause:** The bug stemmed from the system not checking the state of the call before activating the audio stream <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **Consequence:** Discovered by a 14-year-old, Apple initially ignored his report <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>. After the bug went viral on social media, Apple disabled group FaceTime entirely and released a patch <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. The company later awarded the teenager a bug bounty and education funding <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.

### Chase ATM Glitch
*   **Year:** 2024 <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>
*   **What happened:** A glitch in JP Morgan Chase's ATM system, which runs on proprietary code written decades ago using languages like Cobol <a class="yt-timestamp" data-t="00:03:23">[00:03:23]</a>, allowed individuals to withdraw funds immediately after depositing a check, bypassing the usual clearing period <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.
*   **Consequence:** Viral videos showed people withdrawing tens of thousands of dollars they didn't have <a class="yt-timestamp" data-t="00:03:36">[00:03:36]</a>. This constituted check fraud, leading to individuals having bank accounts "deep in the red" and facing lawsuits and potential criminal charges <a class="yt-timestamp" data-t="00:03:47">[00:03:47]</a>. This is an example of [[consequences_of_software_glitches_in_financial_systems | consequences of software glitches in financial systems]].

## Tier 2: Below the Surface

### AT&T Long-Distance Crash
*   **Year:** 1990 <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>
*   **What happened:** A single faulty line of code in a software update caused AT&T's long-distance network switches to crash and reboot automatically <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. This triggered a cascade of failures as rebooting switches caused neighboring ones to fail, ultimately taking out the entire network <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Technical Cause:** The bug was in a C program that included a `break` statement within an `if` clause nested inside a `switch` clause <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>. When a second message was received while the switch was processing the first, the program prematurely dropped out of the `if` clause, overwriting crucial data and causing the switch to reset <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Consequence:** This domino effect blocked 50 million calls globally <a class="yt-timestamp" data-t="00:05:14">[00:05:14]</a>.

### F-35 Fighter Jet Oxygen System Bug
*   **Year:** 2012 <a class="yt-timestamp" data-t="00:05:25">[00:05:25]</a>
*   **What happened:** Pilots flying F-35 fighter jets experienced hypoxia-like symptoms, including dizziness and disorientation, due to issues with the On-Board Oxygen Generation System (OBOGS) <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>.
*   **Technical Cause:** The underlying software for the OBOGS was not robust enough to account for real-time variables such as rapid altitude changes or variations in pilot breathing patterns <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>. The principle of "garbage in, garbage out" applied to the data controlling oxygen supply <a class="yt-timestamp" data-t="00:05:47">[00:05:47]</a>. The code was likely C++ <a class="yt-timestamp" data-t="00:05:59">[00:05:59]</a>.
*   **Consequence:** Though no fatalities occurred, it put pilots at risk <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>. The issue was later resolved with a software update <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.

### Heathrow Terminal 5 Baggage System Failure
*   **Year:** 2008 <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>
*   **What happened:** Days after its opening, a software bug in the automated baggage handling system at Heathrow Terminal 5 led to over 500 canceled flights and 42,000 lost bags <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. The system, with 30 miles of conveyor belts and RFID/barcode tracking, was designed to manage 12,000 bags per hour <a class="yt-timestamp" data-t="00:06:16">[00:06:16]</a>.
*   **Technical Cause:** When the system was pushed to production, several different software systems failed to communicate effectively <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Employees couldn't log in, and RFID tracking systems failed to track bags, causing a complete system breakdown <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. This is an example of [[lessons_learned_from_catastrophic_software_failures | lessons learned from catastrophic software failures]].
*   **Consequence:** The issue cost £16 million to fix <a class="yt-timestamp" data-t="00:06:34">[00:06:34]</a>.

### Vancouver Stock Exchange Rounding Error
*   **Year:** 1982 <a class="yt-timestamp" data-t="00:06:42">[00:06:42]</a>
*   **What happened:** The value of the Vancouver Stock Exchange index began to slowly decrease over two years, dropping from 1,000 to 520, due to a subtle rounding error <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.
*   **Technical Cause:** The software truncated each stock price change to two decimal places instead of rounding <a class="yt-timestamp" data-t="00:07:03">[00:07:03]</a>. While minor for individual stocks, this created a cumulative rounding error over time across thousands of stocks <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>.
*   **Consequence:** The index's value had to be completely recalculated from scratch <a class="yt-timestamp" data-t="00:07:14">[00:07:14]</a>.

### Morris Worm
*   **Year:** 1988 <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>
*   **What happened:** Robert Morris, a Cornell graduate student, released a self-replicating computer program, the Morris worm, to gauge the size of the internet <a class="yt-timestamp" data-t="00:07:24">[00:07:24]</a>. However, a bug in the code caused it to rapidly spread across Unix-based systems, overwhelming their resources and crashing thousands of computers <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>.
*   **Technical Cause:** The worm exploited weaknesses in protocols like Sendmail and a buffer overflow [[security_vulnerabilities_and_exploits | vulnerability]] in the finger program, which provided user information <a class="yt-timestamp" data-t="00:07:43">[00:07:43]</a>. It then executed code remotely and replicated itself <a class="yt-timestamp" data-t="00:07:52">[00:07:52]</a>. The critical bug was its re-infection mechanism, which would reinfect the same computer repeatedly <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>.
*   **Consequence:** It took out 6,000 computers, approximately 10% of the total internet at the time, including MIT, UC Berkeley, and NASA <a class="yt-timestamp" data-t="00:07:39">[00:07:39]</a>. Morris received the first felony conviction under the Computer Fraud and Abuse Act <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Tier 3: Things Start to Blow Up

### Mars Climate Orbiter
*   **Year:** 1999 <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>
*   **What happened:** NASA's Mars Climate Orbiter, valued at $125 million, burned up upon entering Mars' atmosphere <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Technical Cause:** One software team used Imperial units (pound-force), while another team used metric units (Newton-seconds) for calculations related to the orbiter's trajectory <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.
*   **Consequence:** Total loss of the spacecraft due to a unit conversion error <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>.

### Ariane 5 Rocket Explosion
*   **Year:** 1996 <a class="yt-timestamp" data-t="00:08:33">[00:08:33]</a>
*   **What happened:** The Ariane 5 rocket exploded exactly 37 seconds after liftoff <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
*   **Technical Cause:** A software bug in the inertial reference system led to a critical data conversion error <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>. A 64-bit floating-point number representing horizontal velocity was incorrectly converted to a 16-bit integer <a class="yt-timestamp" data-t="00:08:44">[00:08:44]</a>. This made the rocket believe it was 90 degrees off course <a class="yt-timestamp" data-t="00:08:51">[00:08:51]</a>.
*   **Consequence:** The rocket self-destructed when it attempted to correct its perceived trajectory at high velocity <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>. Luckily, no people were on board <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### Toyota Prius Braking Delay
*   **Year:** 2010 <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>
*   **What happened:** A bug in the Toyota Prius anti-lock braking system caused momentary delays in braking under specific conditions, such as icy roads or potholes <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.
*   **Technical Cause:** The computer created a 0.4-second delay when switching from regenerative braking to friction braking <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>.
*   **Consequence:** This resulted in a recall of 400,000 vehicles <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### Citi Bank Bad UI Disaster
*   **Year:** 2020 <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>
*   **What happened:** Citi Bank intended to make an interest payment of $8 million but accidentally transferred the full loan amount of approximately $900 million <a class="yt-timestamp" data-t="00:09:33">[00:09:33]</a>. This is an example of [[consequences_of_software_glitches_in_financial_systems | consequences of software glitches in financial systems]].
*   **Technical Cause:** The software had a confusing, three-screen payment process <a class="yt-timestamp" data-t="00:09:44">[00:09:44]</a>. The user interface (UI) made it appear as though checking certain boxes would ensure only interest was paid, but it actually did the opposite <a class="yt-timestamp" data-t="00:09:46">[00:09:46]</a>.
*   **Consequence:** After Citi Bank requested the money back, the lenders refused, and a court ruled in favor of the lenders, allowing them to keep the $900 million <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>.

### Y2K Bug
*   **Year:** Approaching 2000 <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>
*   **What happened:** In the early days of programming, years were often represented using only two digits (e.g., '99' for 1999) <a class="yt-timestamp" data-t="00:10:11">[00:10:11]</a>. As the year 2000 approached, there was widespread panic that computers would interpret '00' as 1900 instead of 2000, causing global systems to fail <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>.
*   **Consequence:** While the media hysteria was significant, leading to billions of dollars spent in preparation, the Y2K issue did not cause any widespread disasters <a class="yt-timestamp" data-t="00:10:26">[00:10:26]</a>.

## Tier 4: Widespread Damage

### Knight Capital Money Burn Speedrun
*   **Year:** Not specified, but referred to as "a single day" <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>
*   **What happened:** Knight Capital, a company using algorithms for stock market trades, accidentally deployed code linked to an outdated testing algorithm called "Power Peg" <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>. This algorithm was designed to manipulate virtual markets by buying high and selling low <a class="yt-timestamp" data-t="00:10:53">[00:10:53]</a>.
*   **Technical Cause:** Developers used a variable name linked to the inactive Power Peg algorithm <a class="yt-timestamp" data-t="00:10:47">[00:10:47]</a>. When pushed to production, the algorithm went haywire, flooding the New York Stock Exchange with 4 million incorrect trades in just 45 minutes <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This is an example of [[consequences_of_software_glitches_in_financial_systems | consequences of software glitches in financial systems]].
*   **Consequence:** Knight Capital lost $440 million in a single day, wiping out 75% of its investors' equity <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>.

### Heartbleed Vulnerability
*   **Year:** 2014 <a class="yt-timestamp" data-t="00:11:19">[00:11:19]</a>
*   **What happened:** Heartbleed was a critical [[security_vulnerabilities_and_exploits | vulnerability]] in OpenSSL, a widely used cryptographic software library for securing internet communications <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Technical Cause:** The bug was a simple coding oversight: a missing bounds check in the implementation of the Transport Layer Security (TLS) heartbeat extension <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>. This allowed an attacker to send a malicious heartbeat request with an improper input validation, causing the server to send back more data than it should, potentially revealing confidential memory contents <a class="yt-timestamp" data-t="00:11:40">[00:11:40]</a>.
*   **Consequence:** Attackers could repeatedly request memory contents, gaining access to highly confidential data without detection <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>. Two-thirds of internet servers were vulnerable <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>.

### Toyota Unintended Acceleration
*   **Year:** Not specified, but after 2010 Prius braking issue <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>
*   **What happened:** Toyota vehicles experienced unintended acceleration, where cars would suddenly speed up uncontrollably <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
*   **Technical Cause:** An investigation revealed that a software bug in the electronic throttle control system was partly to blame <a class="yt-timestamp" data-t="00:12:17">[00:12:17]</a>. The code had terrible error handling logic, lacked redundancy, and was structured with multiple failure points that could cascade through the entire system <a class="yt-timestamp" data-t="00:12:23">[00:12:23]</a>.
*   **Consequence:** This led to 6,200 complaints, 52 injuries, and 89 deaths <a class="yt-timestamp" data-t="00:12:08">[00:12:08]</a>. Toyota had to recall 9 million vehicles and pay $1.2 billion in fines and settlements <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>. This is an example of [[impact_of_software_bugs_on_different_industries | impact of software bugs on different industries]].

### CrowdStrike Configuration File Debacle
*   **Year:** A few months before video, implying 2023 <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>
*   **What happened:** Cybersecurity company CrowdStrike pushed a bad configuration file (Channel File 291) to production for its Falcon sensor, which has kernel-level access to client machines <a class="yt-timestamp" data-t="00:12:53">[00:12:53]</a>.
*   **Technical Cause:** The bad configuration file caused millions of Windows machines to enter the "blue screen of death" <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. This is an example of [[impact_of_faulty_software_updates_on_global_systems | impact of faulty software updates on global systems]].
*   **Consequence:** Hospitals shut down, flights were canceled, and businesses were severely impacted <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. This highlights the [[vulnerability_of_critical_infrastructures_to_software_errors | vulnerability of critical infrastructures to software errors]].

### Northeastern Blackout
*   **Year:** August 14, 2003 <a class="yt-timestamp" data-t="00:13:09">[00:13:09]</a>
*   **What happened:** Nearly 50 million people in the United States and Canada lost power in a massive blackout <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.
*   **Technical Cause:** FirstEnergy Corporation's power grid monitoring system had poor error handling code <a class="yt-timestamp" data-t="00:13:16">[00:13:16]</a>. If multiple alarms were generated in a short period, the entire system would enter an unrecoverable state without notifying operators <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. This meant no new alarms were shown and existing ones were not cleared, giving operators a false sense of normal operation <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This illustrates the [[vulnerability_of_critical_infrastructures_to_software_errors | vulnerability of critical infrastructures to software errors]].
*   **Consequence:** Half the country lost power <a class="yt-timestamp" data-t="00:13:37">[00:13:37]</a>. Luckily, nobody died <a class="yt-timestamp" data-t="00:13:38">[00:13:38]</a>.

## Tier 5: Tragic Consequences

### Royal Air Force Helicopter Crash
*   **Year:** 1994 <a class="yt-timestamp" data-t="00:13:44">[00:13:44]</a>
*   **What happened:** A military helicopter of the Royal Air Force crashed in Scotland during foggy conditions <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. The aircraft's automatic throttle control, which takes inputs from sensors, became overloaded in the challenging conditions and malfunctioned <a class="yt-timestamp" data-t="00:13:48">[00:13:48]</a>.
*   **Technical Cause:** The throttle control software was not adequately tested under these specific challenging conditions <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. Pilots lost total control when attempting to regain manual control <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>.
*   **Consequence:** 25 people died in the crash <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.

### Therac-25 Radiation Machine
*   **Year:** Early to mid-1980s (referred to as "most famous deadly software bug") <a class="yt-timestamp" data-t="00:14:11">[00:14:11]</a>
*   **What happened:** The Therac-25 was a radiation machine used to treat cancer patients <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>. Due to inadequate error handling and a race condition bug, the device delivered lethal doses of radiation instead of therapeutic ones <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.
*   **Technical Cause:** The device had inadequate error handling <a class="yt-timestamp" data-t="00:14:22">[00:14:22]</a> and when it encountered a race condition, it would deliver lethal doses <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>. Crucially, mechanical interlocks that provided physical safeguards were removed, and the system relied entirely on software <a class="yt-timestamp" data-t="00:14:35">[00:14:35]</a>.
*   **Consequence:** At least three patients died after receiving radiation doses 100 times higher than intended <a class="yt-timestamp" data-t="00:14:30">[00:14:30]</a>.

### Patriot Missile System Failure
*   **Year:** 1991 (Gulf War) <a class="yt-timestamp" data-t="00:14:48">[00:14:48]</a>
*   **What happened:** During the Gulf War, a Scud missile launched by Iraq should have been easily intercepted by the Patriot missile system, but it was not <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Technical Cause:** There was a bug in the system's clock and timing calculations <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. The system had a 24-bit timer that tracked time in tenths of seconds <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>. After operating for over 100 hours without a reset, the timer overflowed, causing it to report incorrect information about incoming threats <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>.
*   **Consequence:** The incoming Scud missile killed 28 American soldiers <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

### USS Vincennes Aegis Combat System Disaster
*   **Year:** 1988 <a class="yt-timestamp" data-t="00:15:20">[00:15:20]</a>
*   **What happened:** The Aegis Combat System on the USS Vincennes accidentally shot down a civilian plane from Iran, killing 290 people on board <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.
*   **Technical Cause:** The investigation revealed that a lack of user-friendly information on the system's display was a key reason for misidentifying the friendly plane as a threat <a class="yt-timestamp" data-t="00:15:28">[00:15:28]</a>. A timing lag led to misleading altitude data <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
*   **Consequence:** 290 civilian lives were lost due to a tragic mistake <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>.

### Boeing 737 MAX MCAS System
*   **Year:** 2018 (Lion Air Flight 610) and 2019 (Ethiopian Airlines Flight 302) <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>
*   **What happened:** Two tragic flights, Lion Air Flight 610 and Ethiopian Airlines Flight 302, crashed due to a faulty automated system <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **Technical Cause:** Modern jets like the 737 MAX use a Maneuvering Characteristics Augmentation System (MCAS) to automatically push the nose down to prevent a stall <a class="yt-timestamp" data-t="00:15:52">[00:15:52]</a>. While there were two angle of attack sensors, the system was programmed to initiate the nose-down sequence if only one of them provided erroneous data <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>. This major oversight meant that a single faulty sensor could cause the plane to repeatedly push its nose down <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.
*   **Consequence:** 346 passengers and crew lost their lives <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. Boeing's reputation was severely damaged, and all 737 MAX planes were grounded <a class="yt-timestamp" data-t="00:16:23">[00:16:23]</a>. The fix required ensuring both sensors provided consistent data before activating the nose-down command <a class="yt-timestamp" data-t="00:16:28">[00:16:28]</a>. This is an example of [[impact_of_software_bugs_on_different_industries | impact of software bugs on different industries]].

While writing entirely bug-free code is challenging <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>, these [[lessons_learned_from_catastrophic_software_failures | lessons learned from catastrophic software failures]] underscore the importance of robust testing and thorough error handling in software development.