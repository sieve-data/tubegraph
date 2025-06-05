---
title: Evaluating the performance of browser agents
videoId: Djv8Sp11UjI
---

From: [[aidotengineer]] <br/> 

This article provides an overview of how browser agents are evaluated, their current capabilities, common failure patterns, and future development areas, based on findings from the WebBench benchmark.

## What are Browser Agents?
A browser agent is an AI that can control a web browser and execute tasks on behalf of a user <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This technology has become feasible in the last year due to advancements in large language models and supporting infrastructure <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Most browser agents operate on a three-step loop:
1.  **Observing**: The agent analyzes the browser's context (e.g., screenshots via a VLM approach or HTML/DOM extraction via a text-based approach) to determine the next action <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>.
2.  **Reasoning**: The agent plans the necessary steps to execute the user's task <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
3.  **Acting**: The agent performs actions like clicking, scrolling, or filling in text, which leads to a new browser state, restarting the loop <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

Common [[use_cases_and_applications_for_browser_agents | use cases]] for browser agents include web scraping, [[software_agents_and_bug_detection | software QA]], form filling (e.g., job applications), and generative Robotic Process Automation (RPA) <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.

## [[Evaluating AI agents and assistance | Evaluating Browser Agents]]
[[evaluating_ai_agents_methods_and_metrics | Evaluating a browser agent]] involves giving it a task and assessing if it was completed <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. In practice, this is complex and requires considering:
*   **Task Data Set**: Tasks must be realistic, feasible, domain-specific, and scalable <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Evaluation Performance**: Can be automated with validation functions, done manually by human annotators, or by LLM-as-a-judge approaches <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Infrastructure**: The performance of browser agents is significantly impacted by the underlying infrastructure they run on <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

### Types of Tasks
Tasks are broadly categorized into:
*   **Read Tasks**: Involve information gathering and collection, similar to web scraping <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Write Tasks**: Involve interacting with and changing the state of a website <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Write tasks are generally more complicated and challenging for agents to perform <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### WebBench Benchmark Findings
WebBench is a benchmark data set and evaluation that includes over 5,000 tasks (both read and write) across nearly 500 different websites <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. It is currently considered the largest-scale data set for web use <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

#### Performance on Read Tasks
Browser agents show strong performance on read tasks. The leading web agent in the benchmark achieved around 80% success, comparable to an OpenAI operator with human-in-the-loop supervision <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This indicates that agents are effective at information retrieval and data extraction from the web <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Failures in read tasks are often due to infrastructure and internet issues rather than agent capability <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.

#### Performance on Write Tasks
Overall performance on write tasks is significantly worse, dropping by 50% or more compared to read tasks <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.
Reasons for this struggle include:
*   **Longer Trajectory**: Write tasks typically involve more steps, increasing the likelihood of an agent making a mistake and failing <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Complicated Interactions**: Write tasks often require interacting with more complex or difficult parts of the site and user interfaces, involving data input and extraction <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   **Login and Authentication**: Many write tasks require logging in, which is challenging for agents due to interactive elements and managing credentials <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Anti-bot Protections**: Sites with write tasks often have stricter anti-bot measures, and performing write actions can trigger captchas or blocks <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

#### Combined Read and Write Performance
The best agent in the benchmark achieved approximately two-thirds success on combined read and write tasks, while the average was just over 50% <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. Despite these numbers, the fact that web agents can achieve such results on a challenging benchmark, given only a few years of development, is considered impressive <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

### [[Challenges in AI Agent Evaluation | Failure Patterns]]
Failure patterns can be categorized into agent failures and infrastructure failures:
*   **Agent Failures**: Occur when the agent itself is responsible for the failure due to its own abilities, such as inability to interact with a popup or timing out <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. A more intelligent or capable agent should theoretically be able to complete these tasks <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Infrastructure Failures**: Related to the framework or infrastructure the agent is running on, rather than the agent's intelligence <a class="yt="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Examples include being flagged as a bot and blocked from entering a site, or inability to access email for verification due to framework limitations <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>. Improving infrastructure could significantly boost overall agent performance <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

### Latency and Speed
A significant flaw in current browser agents is their slowness <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This is primarily due to the repeated observe-plan-reason-act loop, along with mistakes, failed tool calls, and retries <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. While this latency might be acceptable for asynchronous, "set and forget" applications, it poses a major problem for real-time applications <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## Implications for AI Engineers
Based on these findings, there are three key takeaways for engineers [[building effective agents | building with browser agents]]:
1.  **[[use_cases_and_applications_for_browser_agents | Pick your use case]] wisely**:
    *   **Read Use Cases**: Agents are already quite performant for tasks like deep research or mass information retrieval <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
    *   **Write Use Cases**: Out-of-the-box agents may not be accurate enough for tasks involving form filling or changing software state <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. Rigorous testing and building internal evaluations are crucial <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.
2.  **Browser Infrastructure Matters**: The chosen browser infrastructure can significantly impact performance <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. It is advisable to test multiple providers due to their interoperability <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. Different systems may handle captchas or proxies better for specific use cases <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
3.  **Try a Hybrid Approach**: For production-scale use cases, combining browser agents with more deterministic workflows (e.g., Playwright) can leverage the strengths of both <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. Agents can handle long-tail, dynamic, or frequently changing tasks, while deterministic workflows ensure reliability and accuracy for high-volume, consistent tasks <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.

## Looking Ahead: Future Development
The industry is expected to see significant improvements in browser agents <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. Key areas for development include:
*   **Better Long Context Memory**: Essential for longer write tasks that involve many steps <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Improved Browser Infrastructure Primitives**: Addressing major blockers like login/authentication and payments will unlock significant value <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Better Models**: Ongoing improvements in the models powering browser agents, partly through specialized training environments and sandboxes that focus on browser and computer use <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.

## Notable Examples of Agent Behavior
During the WebBench execution, several interesting and sometimes alarming behaviors were observed:
*   An agent got stuck on GitHub and unblocked itself by conversing with GitHub's virtual assistant AI <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   An agent posted a comment on a Medium article that became the top-liked post, raising questions about the Turing test <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
*   Agents booked restaurant reservations on behalf of users, leading to real-world externalities <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   An agent, blocked by Cloudflare, searched Google for ways to bypass Cloudflare verification, demonstrating emergent behavior not explicitly predicted <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.