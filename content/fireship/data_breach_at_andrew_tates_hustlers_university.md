---
title: Data breach at Andrew Tates Hustlers University
videoId: xR5d4Ba4FZg
---

From: [[fireship]] <br/> 

On November 23rd, 2024, "The Real World," formerly known as Andrew Tate's Hustler's University, suffered a significant data breach initiated by "Agents from The Matrix" <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. The attackers described the website as "hilariously insecure" <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>.

## The Platform

The Real World is a subscription-based platform that teaches "money making as a skill" <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Membership costs $50 per month <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>. The website currently claims over 100,000 active members, which would generate over $5 million per month in revenue <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>.

## Leaked Data

The [[website_security_vulnerabilities | non-consensual penetration]] exposed 14 GB of data <a class="yt-timestamp" data-t="00:00:11">[00:00:11]</a>. This included "extremely valuable course content" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>. More critically, the breach leaked:
*   Usernames and emails of over 700,000 members <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>, totaling 795,000 usernames and email addresses <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.
*   The [[content_of_leaked_data_from_chat_rooms | contents of their public and private chat rooms]] <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a> <a class="yt-timestamp" data-t="00:01:29">[00:01:29]</a>. These discussions covered topics such as AI automation, content creation, health and fitness, and cryptocurrency <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>. Andrew Tate also has his own cryptocurrency, "daddy," which dropped 40% and has been labeled a scam <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

The data was published on dss.com, a nonprofit that analyzes hacked datasets <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. Members of the [[hustle_culture_and_workplace_pressure | Hustler's University]] alumni can check if their data was compromised on haveibeenpwned.com <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

## Technical Details and Vulnerabilities

The website's [[website_security_vulnerabilities | insecurity]] was a key factor in the breach <a class="yt-timestamp" data-t="00:00:25">[00:00:25]</a>. Reverse engineering of the tech stack revealed:
*   The stack includes TypeScript, Tailwind CSS, WebSockets, and REST <a class="yt-timestamp" data-t="00:02:08">[00:02:08]</a>.
*   A desktop wrapper uses Capacitor for iOS and Android, described as a tool to run a web app in a web view on mobile platforms <a class="yt-timestamp" data-t="00:02:12">[00:02:12]</a>.
*   The main signup page uses Next.js <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>.
*   The main application uses Vite and React.js <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>.
*   DNS prefetch links in the document head suggest where backend services are hosted <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>.
*   The API URL indicates Cloudflare as the server <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>.
*   A 404 page containing the text "rocket" suggests the use of the Rocket Rust framework <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>. It is confirmed to be Rust Rocket, which is used to build Revolt Chat <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

### Software Theft Allegations
In 2022, the developer of Revolt, an open-source chat platform, accused Tate of stealing software by violating their AGPL license <a class="yt-timestamp" data-t="00:03:03">[00:03:03]</a>. At the time, Revolt was a small project developed by a teenager <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>. It appears Hustler's University is still using a closed-source fork of Revolt <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.

### Authentication Weakness
Hackers were able to break authentication on the API <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. A contributing factor was that the frontend JavaScript bundle included all code comments and was not obfuscated, making it easier to reverse engineer <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

## Hacker Actions and Impact

After gaining access, the hackers made their presence known by flooding the University's primary chat room with emojis, including the transgender flag, a feminist fist, and images of Andrew Tate wearing a rainbow flag <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. This [[incident_involving_lgbt_hackers | incident involving LGBT hackers]] occurred while Tate was live streaming on Rumble <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

The true victims of this penetration are the 800,000 graduates whose "highly respected diploma" from Hustler's University is now considered a "worthless piece of paper" <a class="yt-timestamp" data-t="00:03:56">[00:03:56]</a>.