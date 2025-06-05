---
title: Use cases and applications for browser agents
videoId: Djv8Sp11UjI
---

From: [[aidotengineer]] <br/> 

A browser agent is defined as any AI that can control a web browser and execute tasks on behalf of the user <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This technology has become feasible in the last year due to advancements in large language models and supporting infrastructure <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

## How Browser Agents Operate
Most [[understanding_browser_agents | browser agents]] function based on a three-step loop:
1.  **Observing**: The agent analyzes the current browser context to determine the next action <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This can involve taking a screenshot (VLM approach) or extracting HTML and DOM data (text-based approach) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
2.  **Reasoning**: After understanding the context, the agent reasons through and determines the necessary next steps to complete the user's task <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
3.  **Acting**: The agent then performs an action, such as clicking, scrolling, or filling in text <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

This [[understanding_browser_agents | browser agent]] loop then returns to the observation step, reacting to the browser's new state <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Major Use Cases

[[automation_of_web_tasks_using_ai_web_agents | Browser agents]] have started to penetrate several major use cases in recent months <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>:

*   **Web Scraping**: This involves deploying a fleet of browser agents to extract information, such as sales teams finding data about prospects <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **Software QA**: [[software_agents_and_bug_detection | Browser agents]] are used to click around and test software before its release <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Form Filling / Job Application Filling**: This is a very popular application, with many automated job prospecting tools powered by [[automation_of_web_tasks_using_ai_web_agents | browser agents]] <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Generative RPA (Robotic Process Automation)**: Companies are exploring the use of [[automation_of_web_tasks_using_ai_web_agents | browser agents]] to automate traditional RPA workflows that frequently break <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>.

## Read Tasks vs. Write Tasks

Tasks performed by [[understanding_browser_agents | browser agents]] can be broadly categorized into two types:
*   **Read Tasks**: These typically involve information gathering and collection <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. Examples include web scraping, searching, filtering, and scrolling <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.
*   **Write Tasks**: These involve interacting with and changing the state on a website <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. They are more complex, requiring actions like data input, data extraction, and interacting with complicated forms <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### Performance and Suitability
Currently, [[evaluating_the_performance_of_browser_agents | browser agents]] are quite good at read tasks, with leading agents achieving around 80% success rates in benchmarks <a class="yt-timestamp" data-t="00:05:57">[00:05:57]</a>. Failures in read tasks are often related to infrastructure and internet issues rather than the agent's intelligence <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>. For instance, a complex read task might involve multiple search and filtering steps, navigating pop-ups, and scrolling interactions <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

However, performance on write tasks is significantly worse, dropping by 50% or more for fully autonomous agents <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>. This is due to several factors <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>:
*   **Longer Trajectory**: Write tasks generally require more steps, increasing the likelihood of an error <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Complex UI Interactions**: Write tasks often involve interacting with more difficult or dynamic parts of a site, such as adding new forms <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   **Login/Authentication**: Many write tasks require logging in, which is challenging for agents due to managing credentials and complex user experiences <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Anti-bot Protections**: Sites with many write tasks typically have stricter anti-bot measures, and performing write actions can even trigger captchas <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

Overall, the best autonomous agents achieve about two-thirds success on combined read and write tasks, while the average is just over 50% <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. Despite these challenges, the current performance is considered impressive given the relatively short development time of web agents <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Implications for Building with Browser Agents
When building with [[building_effective_agents | browser agents]], key considerations emerge:
*   **Choosing the Use Case**: For deep research tools or systems that mass-retrieve information (read use cases), out-of-the-box products perform well <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. For products involving write functions (form filling, changing software state), rigorous testing is required, as agents may not be accurate out of the box <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
*   **Browser Infrastructure**: The chosen browser infrastructure significantly impacts performance <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. Testing multiple providers is recommended, as they are often interoperable and may offer better captcha handling or unblocked proxies for specific sites <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **Hybrid Approach**: For production-scale use cases, combining [[understanding_browser_agents | browser agents]] for long-tail, dynamic, or frequently changing workflows with more deterministic methods (e.g., Playwright) for reliable, high-volume tasks can be effective <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>. This approach leverages the agent's nuance for complex scenarios while ensuring accuracy for critical, stable steps <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.

## Future Developments
Future improvements for [[understanding_browser_agents | browser agents]] are anticipated in several key areas <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>:
*   **Better Long Context Memory**: This is crucial for accurately executing longer write tasks that involve many steps <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Enhanced Browser Infrastructure Primitives**: Addressing blockers like login/authentication and payments will unlock significant value for [[automation_of_web_tasks_using_ai_web_agents | browser agents]] <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Improved Underlying Models**: Continuous improvement of the models powering [[understanding_browser_agents | browser agents]], potentially through training environments and sandboxes, will enhance capabilities like tool calling and write actions <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.

## Noteworthy Examples
During benchmarking, [[understanding_browser_agents | browser agents]] demonstrated some remarkable and occasionally concerning behaviors:
*   An agent got stuck on GitHub and autonomously conversed with GitHub's virtual assistant AI to unblock itself <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   An agent posted a comment on a Medium article, which subsequently became the top-liked post, raising questions about the Turing Test <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
*   Agents booked restaurant reservations on users' behalf, leading to unexpected real-world externalities <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   When blocked by Cloudflare, an agent searched on Google for ways to bypass Cloudflare verification, showcasing emergent and unpredictable behavior <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

These examples highlight the rapidly evolving capabilities and the need for robust testing in the [[ai_agents_beyond_chatbots | browser agent]] space <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>.