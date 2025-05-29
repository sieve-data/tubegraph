---
title: Startup Challenges in Hardware Development
videoId: GADD8bNDMIk
---

From: [[thepipeline_xyz]] <br/> 

Building hardware products presents unique and significant [[challenges_and_strategies_for_crypto_startups | challenges]] compared to software development <a class="yt-timestamp" data-t="00:07:30">[00:07:30]</a>. Nix, from the Pulse team, vividly describes the process as "chewing glass that is on fire" <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.

## Key Difficulties in Hardware Development

Unlike software, where issues can often be resolved with a quick update, a mistake in hardware can necessitate a complete restart of the production process <a class="yt-timestamp" data-t="00:08:17">[00:08:17]</a>. The Pulse team spent an entire summer in stealth, navigating the demanding "gauntlet of production" <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This intensive period involved:

*   **Supplier Management**
    *   Finding suitable suppliers <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>.
    *   Testing their capabilities <a class="yt-timestamp" data-t="00:08:55">[00:08:55]</a>.
    *   Benchmarking them against competitors <a class="yt-timestamp" data-t="00:08:57">[00:08:57]</a>.
*   **Design and Logistics**
    *   Developing appropriate designs <a class="yt-timestamp" data-t="00:08:59">[00:08:59]</a>.
    *   Handling complex logistics, fulfillment, and delivery <a class="yt-timestamp" data-t="00:09:04">[00:09:04]</a>.
    *   Customizing branding <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>.

These steps cannot be short-circuited; they require thorough execution from beginning to end <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>. The commitment required is significant; one of Pulse's co-founders relocated to China full-time to oversee manufacturing, with the agreement not to return until the final wearable leaves the production line <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>, <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

## Advantages of Building Hardware

Despite the difficulties, building hardware offers several strategic advantages for a startup like Pulse:

*   **Creating a Moat**
    *   It establishes a competitive barrier, preventing other teams like Whoop or Oura Ring from displacing them by, for example, revoking API access <a class="yt-timestamp" data-t="00:10:34">[00:10:34]</a>.
*   **Unique Features and Ecosystem**
    *   The Pulse wearable includes an NFC chip, allowing for direct crypto wallet integration <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. This feature supports a "proof of pulse" narrative, verifying one wallet per human without doxing the user <a class="yt-timestamp" data-t="00:10:56">[00:10:56]</a>.
    *   It enables Pulse to offer its API and SDK to other teams interested in building software on top of their device <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. Pulse views its wearable as an infrastructure piece that other teams can leverage <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>.

## Design and Market Inspiration

The Pulse team extensively researched the existing wearable market to understand why users gravitated towards products like Whoop, Oura Ring, UltraHuman Ring, Fitbit, and Apple Watch <a class="yt-timestamp" data-t="00:12:25">[00:12:25]</a>. They identified flaws and glean insights from these existing solutions <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.

While many users adopt wearables like Whoop primarily for sleep tracking, Pulse aims to go beyond basic health and fitness <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. Pulse is designed as a "lifestyle wearable" focused on enhancing productivity <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>. This includes tracking not just sleep and exercise, but also diet, stress levels, sun exposure, socializing, and overall fulfillment, all contributing to a user's productivity <a class="yt-timestamp" data-t="00:13:23">[00:13:23]</a>. This broader scope differentiates Pulse from competitors <a class="yt-timestamp" data-t="00:14:02">[00:14:02]</a>.

## Data Collection and Automation

Pulse leverages various sensors on the wearable device to automatically detect user activities:

*   **Accelerometer:** Tracks acceleration and deceleration, indicating movement, lifting, or placing objects, which helps infer physical exercise like weightlifting or running <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a>.
*   **Temperature Sensors:** Provide environmental data to determine if a user is outdoors or indoors (e.g., detecting a significant temperature spike in a hot yoga class) <a class="yt-timestamp" data-t="00:30:48">[00:30:48]</a>.
*   **Heart Rate Monitor:** Essential for identifying activities like running, where heart rate typically elevates and remains consistent <a class="yt-timestamp" data-t="00:31:06">[00:31:06]</a>.

By analyzing these biometrics, Pulse aims to automatically track about 50 common fitness and lifestyle activities, including swimming, running, boxing, weightlifting, yoga, and Pilates <a class="yt-timestamp" data-t="00:31:24">[00:31:24]</a>.

Beyond specific activities, Pulse also monitors general lifestyle data, such as prolonged sitting, and can nudge users towards more energetic and productive behaviors <a class="yt-timestamp" data-t="00:31:53">[00:31:55]</a>.

## Crypto-Native Approach and Data Ownership

Pulse integrates a crypto-native approach to address issues prevalent in traditional wearable data management. While existing wearables sell user data without reward <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>, Pulse uses crypto rails to ensure transparency in data brokerage <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

This means users are notified if a third party, like a university, wants to acquire their data for studies and can decide whether to license it <a class="yt-timestamp" data-t="00:06:24">[00:06:24]</a>. Crypto rails provide transparency regarding what data is shared, for how long, and its intended use <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

Furthermore, Pulse prioritizes data security by encrypting as much data as possible on-chain using MPC-powered encryption <a class="yt-timestamp" data-t="00:35:51">[00:35:51]</a>. This design ensures that only the user can decrypt their data, preventing third-party access, including from Pulse itself <a class="yt-timestamp" data-t="00:36:08">[00:36:08]</a>. Utilizing fully homomorphic encryption, users can gain insights from their data without risking exposure to third parties, thereby mitigating risks of data hacks that have affected traditional platforms <a class="yt-timestamp" data-t="00:36:32">[00:36:32]</a>.

This model, described as "live to earn," differentiates Pulse by rewarding users for contributing their day-to-day life data, regardless of their health activities <a class="yt-timestamp" data-t="00:33:02">[00:33:02]</a>. The goal is to build a comprehensive "Health Digital Twin" by exploring incentives for users to contribute other data like blood work, DNA, and electronic health records <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>.