---
title: Development and technology behind Worldcoins ORB device
videoId: 6bXEdm51dlc
---

From: [[mk_thisisit]] <br/> 

The Worldcoin project introduces the ORB, a sophisticated device designed to establish a unique digital identity for individuals online, primarily to distinguish humans from bots in an increasingly AI-driven internet <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>.

## The Problem Worldcoin Addresses

Estimates suggest that up to half of all internet activity originates from bots <a class="yt-timestamp" data-t="00:00:05">[00:00:05]</a>. The proliferation of disinformation and misinformation, coupled with the rising difficulty in differentiating human interactions from automated ones, highlights a critical need for a solution that can verify human identity while preserving privacy <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. The project aims to provide infrastructure that accelerates humanity's [[sam_altman_and_the_vision_for_futuristic_global_technologies | development]] and allows it to thrive in a new era of powerful tools <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Without a reliable method to distinguish humans, the internet could cease to function effectively <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.

## The ORB Device: A Digital Passport

The ORB provides a "digital passport" on a user's phone, known as World ID, which proves the individual is a unique human being and not a bot <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This World ID is intended for global use to build a fraud-free network where every participant is a verified human <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

### Development and Origin
The ORB is a highly sophisticated device, designed by physicists in Germany and manufactured there <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Its purpose is to be tamper-proof and capable of handling sensitive data <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>. The first prototype of the ORB was created in what is referred to as a "garage" or workshop, where engineers developed the initial technologies <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. This location now primarily serves as a repair and refurbishment center for ORB equipment from around the world <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

### Design Philosophy
The ORB's distinctive spherical shape was a deliberate design choice. While a box with sharp edges might be easier to manufacture, the sphere was deemed more attractive, recognizable, and less intimidating <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. This shape also serves as a metaphor for the Earth, symbolizing the project's global ambition and connection to the "World" in its name <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. The design incorporates elements like the angle of the ring, which matches the Earth's rotation at the equator, aiming for familiarity and accessibility <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. The ORB was also designed with an Open Source model in mind, aiming for decentralization and ease of disassembly without requiring extensive tools <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

### Internal Components
The ORB comprises several key groups of elements <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>:
*   **Housings/Cosmetic Elements**: What people initially see <a class="yt-timestamp" data-t="00:05:54">[00:05:54]</a>.
*   **Optical Module**: Considered the "heart of the device," this element is unique and crucial for its operation, consisting of many special sensors and optical paths <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   **Structural Elements**: A base, structural ring, and body provide mounting and support <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **Cooling System**: Manages thermal performance <a class="yt-timestamp" data-t="00:06:13">[00:06:13]</a>.
*   **Electronics**: Includes PCBA modules, the motherboard, and a protective board <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.

## Core Technology: Iris Scans
The most challenging task in the ORB's development was verifying the iris to obtain a sufficiently high-quality image for over 8 billion potential users <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>.

### Why Iris Scans?
The choice of iris scanning as the biometric solution was made after studying various options like fingerprints, face scans, and DNA <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Iris entropy is very high, meaning there are significant differences between individuals <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. On a scale of billions of users, or in terms of susceptibility to abuse, the iris proved to be the most effective and least susceptible to fraud <a class="yt-timestamp" data-t="00:07:22">[00:07:22]</a>. Additionally, the iris does not change significantly with age, making it a reliable long-term solution <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>. While DNA and hand vein scans also offer high distinguishing capabilities, iris scanning technology is already widely used, for example, by governments in India (Aadhaar project, used by 1.2 billion people) and at many airports <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>. This established precedent reduced the technological risk for Worldcoin <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>.

### How it Works
Unlike traditional biometric systems like Face ID, which perform a one-to-one comparison (verifying if a person is the device owner) <a class="yt-timestamp" data-t="00:07:58">[00:07:58]</a>, World ID requires a one-to-many comparison to verify a unique human being against all other registered individuals <a class="yt-timestamp" data-t="00:08:26">[00:08:26]</a>.

When a user interacts with an ORB:
1.  The ORB takes a picture of the user's face and iris <a class="yt-timestamp" data-t="00:11:53">[00:11:53]</a>.
2.  The data is processed immediately on the device to check if it's a human, not an animal <a class="yt-timestamp" data-t="00:12:31">[00:12:31]</a>.
3.  If human, the iris is scanned and assigned a unique binary "iris code" <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
4.  Only this iris code is transmitted to the system to verify uniqueness <a class="yt-timestamp" data-t="00:13:05">[00:13:05]</a>.
5.  Photos and images are stored *only* on the user's device and are deleted from the ORB, with no copies kept by Worldcoin <a class="yt-timestamp" data-t="00:13:11">[00:13:11]</a>.

## Privacy and Data Handling
A key aspect of the ORB's operation is its commitment to privacy. The device is designed not to store or know any personal identifiable information (PII) about the user <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>. Worldcoin, as an organization, explicitly states it does not have user data; data is physically stored on the individual's device <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>. This decentralized approach ensures that once the ORB verifies a unique person and assigns an iris code, a copy of this encrypted data is sent only to the user's device <a class="yt-timestamp" data-t="00:12:06">[00:12:06]</a>.

## Futuristic Vision and Challenges
Worldcoin views its project as highly futuristic <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>, aligning with [[sam_altman_and_the_vision_for_futuristic_global_technologies | Sam Altman]]'s vision for transformative global technologies <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>. The ORB's technology, particularly iris scanning, is seen as a gateway to the [[application_development_for_augmented_reality | digital world]] in the era of AR/VR, where eyes might become crucial for secure authentication <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

The project faces significant challenges, primarily related to education and addressing global concerns <a class="yt-timestamp" data-t="00:13:36">[00:13:36]</a>. Different regions have varying priorities: in Argentina, Web3 and cryptocurrencies are widely understood, leading to high adoption <a class="yt-timestamp" data-t="00:14:06">[00:14:06]</a>, while in places like Japan or Korea, concerns about data control and privacy are paramount <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. Europe, in particular, demonstrates a strong emphasis on privacy <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>. Worldcoin aims to meet these diverse priorities, emphasizing that their approach maintains high security levels <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>. The company continues to expand into European countries, actively cooperating with data protection authorities <a class="yt-timestamp" data-t="00:15:46">[00:15:46]</a>.

The project acknowledges that combining biometrics and cryptocurrencies can be controversial, especially as it presents a vision for a distant future <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>. However, it believes that the underlying problem of distinguishing humans from bots on the internet, and the robust privacy-preserving technology of the ORB, offer solutions to important global challenges <a class="yt-timestamp" data-t="00:16:56">[00:16:56]</a>.