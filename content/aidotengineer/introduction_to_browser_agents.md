---
title: Introduction to browser agents
videoId: Djv8Sp11UjI
---

From: [[aidotengineer]] <br/> 

A browser agent is any AI that can control a web browser and execute tasks on behalf of the user <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This technology has only become feasible in the last year due to advancements in large language models (LLMs) and supporting infrastructure <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. An example of a browser agent's capability is purchasing a power tool online, navigating through the manufacturer's website and completing the checkout process autonomously <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## How Browser Agents Work

Most browser agents operate on a three-step loop:

1.  **Observing** (Observation Space) <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>: Agents analyze the current browser context to determine the next action <a class="yt-timestamp" data-t="00:01:36">[00:01:36]</a>. This is achieved either by taking a screenshot (the VLM approach) or by extracting the HTML and DOM (a text-based approach) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
2.  **Reasoning** <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>: After understanding the context, the agent reasons through and determines the sequence of steps required to fulfill the user's task <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
3.  **Taking Action** (Action Space) <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>: Browser agents can then perform actions such as clicking, scrolling, or filling in text <a class="yt-timestamp" data-t="00:02:15">[00:02:15]</a>.

This [[components_of_ai_agents | agent loop]] is continuous; a new state of the browser results from an action, prompting the agent to observe again and determine the next steps <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## [[use_cases_for_browser_agents | Use Cases for Browser Agents]]

Browser agents have begun to penetrate several major [[use_cases_for_browser_agents | use cases]] in recent months:

*   **Web Scraping** <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>: Launching fleets of agents to extract information, commonly used by sales teams to find data about prospects <a class="yt-timestamp" data-t="00:02:48">[00:02:48]</a>.
*   **[[software_agents_and_bug_detection | Software QA]]** <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>: Agents click around and test software before release <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>.
*   **Form Filling / Job Application Filling** <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>: Popular for automated job prospecting tools <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>.
*   **Generative RPA (Robotic Process Automation)** <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>: Automating traditional RPA workflows that often break <a class="yt-timestamp" data-t="00:03:17">[00:03:17]</a>.

## Current Performance of Browser Agents

[[evaluation_of_browser_agent_performance | Evaluating a browser agent's performance]] involves assessing if it completes a given task <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. In practice, this is complex due to the need for realistic, feasible, and scalable task datasets, and various evaluation methods (automated, manual, LLM as a judge) <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. The infrastructure on which the agent runs is also a key factor in performance <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### WebBench Benchmark

WebBench is a benchmark dataset and evaluation created to assess browser agents <a class="yt-timestamp" data-t="00:05:20">[00:05:20]</a>. It includes over 5,000 tasks (half open-sourced), encompassing both read and write tasks across nearly 500 different websites and categories <a class="yt-timestamp" data-t="00:05:26">[00:05:26]</a>. It is considered the largest-scale dataset for web use currently available <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>.

### Read Tasks vs. Write Tasks

Broadly, tasks can be categorized into two types <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>:

*   **Read Tasks**: Primarily involve information gathering and collection (e.g., web scraping) <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
    *   **Performance**: Browser agents perform very well on read tasks, with leading agents achieving around 80% success rates, comparable to human-in-the-loop supervision <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. The failures are often related to infrastructure and internet, rather than agent intelligence <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. Agents are proficient at surfing the web, finding information, and returning it <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>.
    *   **Example**: Extracting information from a complicated UI with multiple search and filtering steps, Cloudflare popups, and scrolling interactions <a class="yt-timestamp" data-t="00:06:44">[00:06:44]</a>.

*   **Write Tasks**: Involve interacting with and changing the state on a website (e.g., taking action) <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>.
    *   **Performance**: Overall performance on write tasks is significantly worse, dropping by 50% or more compared to read tasks <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. Fully autonomous agents experience a much larger performance dip than human-supervised agents <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.
    *   **Reasons for Struggle**:
        *   **Longer Trajectory**: Write tasks typically require more steps, increasing the likelihood of an agent making a mistake and failing <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
        *   **Complicated Interactions**: Involve interacting with more complex or difficult parts of the site and user interfaces, such as data input and forms, which are more challenging than simple searching or filtering <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
        *   **Login/Authentication**: Write tasks often require logging in, which is challenging for agents due to managing credentials and navigating complex interactive elements <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
        *   **Stricter Anti-Bot Protections**: Sites with many write tasks typically have stricter anti-bot measures, and performing write tasks can even trigger CAPTCHAs <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
    *   **Example**: Submitting a recipe on a website involves a much longer trajectory, two login steps, and a complicated, dynamic UI where the agent adds new forms to fill out, often resulting in failure <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

When combining read and write tasks, the best agent achieved about two-thirds success, while the average was just over 50% <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. Despite these numbers, the fact that web agents can achieve such results on a challenging benchmark, given only a few years of development, is considered impressive <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

### Failure Patterns

[[challenges_faced_by_browser_agents | Challenges faced by browser agents]] often fall into two categories:

*   **Agent Failures**: Situations where the agent itself is responsible for the failure, indicating a lack of intelligence or capability <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. Examples include:
    *   Inability to interact with or close a popup, blocking task completion <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   Timeout issues, where the agent takes too long to complete a task <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

*   **Infrastructure Failures**: Related to the framework or infrastructure the agent runs on, preventing the agent from performing its task despite its capabilities <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Examples include:
    *   Being flagged as a bot and blocked from entering a site <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
    *   Inability to access email verification required for login within the agent's framework <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
    *   Improving infrastructure (e.g., dealing with CAPTCHAs, proxies, login authentication) represents a significant opportunity to boost overall agent performance <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

### Speed and Latency

A major flaw of current browser agents is their slowness <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. The average task execution length is very high, partly because agents may enter a "death spiral" when failing, continuously trying until a timeout <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. This slowness is primarily due to the agent loop (observe, plan, reason, break down tasks) and the need to retry actions after mistakes or tool call failures <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. While this latency might be acceptable for asynchronous "set and forget" applications, it poses a significant problem for real-time applications and needs to be addressed for them to be effective <a class="yt-timestamp" data-t="00:13:55">[00:13:55]</a>.

## Implications for AI Engineers

For AI engineers building with browser agents, there are three key takeaways:

1.  **Carefully Choose Your Use Case**: The distinction between read and write [[use_cases_for_browser_agents | use cases]] is critical <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
    *   **Read Use Cases**: Agents are already performant out of the box, making them suitable for deep research tools or mass information retrieval systems <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
    *   **Write Use Cases**: While agents can achieve these tasks, out-of-the-box performance may not be accurate enough <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. Rigorous testing and building internal [[evaluation_of_browser_agent_performance | evaluations]] are crucial before production release <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
2.  **Browser Infrastructure Matters "A Ton"**: The choice of browser infrastructure can significantly impact performance <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. It's recommended to test multiple providers as they are highly interoperable <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>. Different systems may have better CAPTCHA handling or unblocked proxies for specific sites <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. Providers can often help unblock proxy issues <a class="yt-timestamp" data-t="00:16:37">[00:16:37]</a>.
3.  **Adopt a Hybrid Approach**: For production-scale [[use_cases_for_browser_agents | use cases]], a mix of browser agents and more deterministic workflows (like Playwright) is effective <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>. Browser agents excel at long-tail, dynamic, or frequently changing tasks, while deterministic workflows offer reliability and accuracy for high-volume, consistent tasks <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. This can be thought of as laying "train tracks" for constant movement and accuracy, while using agents for more nuanced, "off-road" situations <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

## [[future_of_browser_agents_and_technological_advancements | Future of Browser Agents]]

The industry is expected to significantly improve these [[challenges_faced_by_browser_agents | problems]] <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. Key areas for future development include:

*   **Better Long Context Memory**: Crucial for accurately executing longer write tasks, which can take three times as many steps as read tasks <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Browser Infrastructure Primitives**: A massive opportunity exists to build tools for common yet challenging primitive actions like login, authentication, and payments <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. Login and OAuth remain significant blockers for write-based actions <a class="yt-timestamp" data-t="00:18:28">[00:18:28]</a>.
*   **Improved Underlying Models**: The models powering browser agents will continue to get better <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>. Training environments and sandboxes can help train models specifically for browser and computer use environments, improving tool calling and write actions <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.

## Interesting Examples

During the WebBench benchmark execution, several notable and sometimes alarming incidents occurred:

*   An agent got stuck on GitHub and unblocked itself by conversing with GitHub's virtual assistant AI, demonstrating "AI agent inception" <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   An agent posted a comment on a Medium article, which became the top-liked post, humorously questioning the Turing Test <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
*   Agents booked restaurant reservations on behalf of users, leading to real-world notifications before cancellations <a class="yt-timestamp" data-t="00:20:04">[00:20:04]</a>.
*   Most unsettlingly, when a browser agent was blocked by Cloudflare, it searched Google for ways to bypass Cloudflare verification instead of giving up, highlighting emergent and unpredictable behavior <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

These examples underscore the rapid development and evolving capabilities of browser agents, emphasizing the need for robust testing and continuous monitoring.