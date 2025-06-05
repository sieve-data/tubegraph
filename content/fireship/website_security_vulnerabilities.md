---
title: Website security vulnerabilities
videoId: xR5d4Ba4FZg
---

From: [[fireship]] <br/> 

On November 23, 2024, "The Real World," formerly known as Andrew Tate's Hustler's University, was subjected to an "egregious attack" by hackers who identified themselves as "Agents from The Matrix" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The attackers gained non-consensual penetration into the website, describing it as "hilariously insecure" <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Impact of the Data Breach

The attack resulted in a significant [[impact_of_data_breaches_on_internet_history_archives | data breach]] that exposed approximately 14 GB of data <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This included:
*   Extremely valuable course content <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   Usernames and email addresses of over 700,000 members <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, specifically 795,000 <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>.
*   Contents of public and private chat rooms <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

The leaked data was published on dss.com, a non-profit organization that specializes in analyzing hack data sets <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Individuals who were members of Hustler's University can check if their data was compromised on haveibeenpwned.com <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### Post-Breach Actions

Beyond the data leak, the attackers also leveraged their access to the main chat room, flooding it with emojis such as the transgender flag, a feminist fist, and images of Andrew Tate wearing a rainbow flag. This occurred while Tate was live streaming on Rumble <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>.

## Technical Vulnerabilities

Through reverse engineering of the website's [[technical_details_of_the_websites_tech_stack | tech stack]], several potential [[security_vulnerabilities_and_exploits | security vulnerabilities]] were identified:

### Revealed Tech Stack
The website's [[technical_details_of_the_websites_tech_stack | technical details of the websites tech stack]] included:
*   **Frontend:** Vite with ReactJS for the main application <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>, Next.js for the main signup page <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>, Typescript, Tailwind CSS, WebSockets, and REST <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   **Mobile Development:** Capacitor was used as a tool to wrap the web application for iOS and Android <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   **Backend Hosting:** Cloudflare <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   **Backend Framework:** Evidence suggests the use of the Rocket Rust framework, indicated by "rocket" text on a 404 page <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **Chat Framework:** The platform appears to use a closed-source fork of Revolt Chat, an open-source TypeScript-based chat framework built with Rust Rocket <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.

### Suspected Software Misappropriation
It is alleged that Hustler's University stole software from Revolt Chat in 2022 by violating its AGPL license <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. Revolt, developed by a teenager, accused Tate of software theft <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. As of the breach, "The Real World" seemingly continues to use a closed-source fork of Revolt <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Code Obfuscation Issues
A critical [[security_vulnerabilities_and_exploits | security vulnerability]] identified was that the website's frontend JavaScript bundle included all code comments and was not obfuscated <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. This lack of obfuscation made it significantly easier for attackers to reverse engineer the code and potentially identify pathways to "break authentication" on the API <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>.