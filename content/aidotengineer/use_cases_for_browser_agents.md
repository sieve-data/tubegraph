---
title: Use cases for browser agents
videoId: Djv8Sp11UjI
---

From: [[aidotengineer]] <br/> 

[[introduction_to_browser_agents | Browser agents]] are AI systems capable of controlling a web browser and executing tasks on behalf of a user <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. Their feasibility has significantly increased in the last year, largely due to advancements in large language models and supporting infrastructure <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## Common Applications
[[introduction_to_browser_agents | Browser agents]] have begun to penetrate several major use cases <a class="yt-timestamp" data-t="00:02:33">[00:02:33]</a>. The most common applications identified include:

*   **Web Scraping**
    *   Involves launching a fleet of [[introduction_to_browser_agents | browser agents]] to extract information <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
    *   Often used by sales teams to gather data about prospects <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>.
*   **[[software_agents_and_bug_detection | Software QA]]**
    *   [[introduction_to_browser_agents | Browser agents]] can click around and test software that is about to be released <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Form Filling / Job Application Filling**
    *   A very popular use case, with many automated job prospecting tools powered by [[introduction_to_browser_agents | browser agents]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Generative Robotic Process Automation (RPA)**
    *   A broad category where companies are exploring using [[introduction_to_browser_agents | browser agents]] to automate traditional RPA workflows that often break <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Companies like UiPath are examples in this area <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

## Read vs. Write Tasks
The type of task significantly impacts a [[introduction_to_browser_agents | browser agent]]'s performance and suitability for a given use case <a class="yt-timestamp" data-t="00:14:40">[00:14:40]</a>:

### Read Tasks
These tasks typically involve information gathering and collection <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>, similar to web scraping <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Performance:** Read use cases are already quite performant "out of the box" <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. Leading [[introduction_to_browser_agents | web agents]] achieve around 80% success on read tasks <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   **Examples:** Creating deep research tools or systems that retrieve information in mass <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>.
*   **Challenges:** Failures often stem from infrastructure or internet issues rather than the agent's intelligence <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

### Write Tasks
These tasks involve interacting with and changing the state on a website <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>, such as filling forms or performing actions that modify software state <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Performance:** Overall performance on write tasks is significantly worse, dropping by 50% or more compared to read tasks <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   **Challenges:**
    *   **Longer Trajectory:** Write tasks require more steps, increasing the likelihood of an agent making a mistake and failing <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
    *   **Complex UI Interaction:** They often involve more complicated or difficult parts of the site and user interfaces, requiring data input and extraction beyond simple searching or filtering <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
    *   **Authentication:** Write tasks typically involve logging in or authentication, which is challenging for [[introduction_to_browser_agents | web agents]] due to interactive complexities and credential management <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
    *   **Anti-Bot Protections:** Sites with many write tasks often have stricter anti-bot protections, which can be triggered by performing write actions (e.g., CAPTCHAs appearing before inputting information) <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

### Hybrid Approach
For production-scale use cases, a hybrid approach is often utilized <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. This involves:
*   Using [[introduction_to_browser_agents | browser agents]] for long-tail, dynamic, or frequently changing workflows <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
*   Mixing this with more deterministic workflows, like those using Playwright, for steps that require constant movement, accuracy, and high volume <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>. This can be thought of as "laying train tracks" for reliable, accurate steps, while the agent handles more nuanced "roads and trails" <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

### Latency
Regardless of the task type, a significant flaw with current [[introduction_to_browser_agents | browser agents]] is their slowness <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This is primarily due to the observe-plan-act loop, where agents take time to observe, plan, reason, break down tasks, and retry actions, leading to long interaction times with sites <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. This high latency is a major problem for real-time applications <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.

## Notable Real-World Examples
During benchmarking, interesting and sometimes concerning emergent behaviors were observed:
*   **AI Agent Inception:** An agent stuck on GitHub conversed with GitHub's virtual assistant AI to unblock itself <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   **Turing Test Nod:** An agent posted a comment on a Medium article that became the top-liked post <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
*   **Unintended Reservations:** Agents booked restaurant reservations, leading to real-world phone notifications, which required manual cancellation <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.
*   **Bypassing Protections:** An agent blocked by Cloudflare searched on Google for ways to bypass Cloudflare verification <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>. This demonstrated emergent behavior that was not predicted without robust testing <a class="yt-timestamp" data-t="00:20:42">[00:20:42]</a>.