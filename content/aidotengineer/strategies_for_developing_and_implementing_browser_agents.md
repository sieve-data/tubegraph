---
title: Strategies for developing and implementing browser agents
videoId: Djv8Sp11UjI
---

From: [[aidotengineer]] <br/> 

## Understanding Browser Agents
A browser agent is any AI that can control a web browser and execute tasks on behalf of the user <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. This technology has become feasible in the last year due to advancements in large language models and supporting infrastructure <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>.

Most browser agents operate on a three-step loop:
1.  **Observing**: The agent assesses the current browser context to determine the next action <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This can involve taking a screenshot (VLM approach) or extracting HTML and DOM information (text-based approach) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
2.  **Reasoning**: The agent processes the context to deduce the necessary steps to complete the user's task <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.
3.  **Action**: The agent performs an action within the browser, such as clicking, scrolling, or filling in text <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. After an action, the loop restarts with a new browser state <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

### [[use_cases_and_applications_for_browser_agents | Use Cases for Browser Agents]]
Browser agents have begun to penetrate several major use cases <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>:
*   **Web Scraping**: Deploying a fleet of agents to extract information, often used by sales teams to find prospect data <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Software QA**: Using agents to navigate and test software before release <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Form Filling / Job Application Filling**: Popular for automated job prospecting tools <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
*   **Generative RPA**: Automating traditional Robotic Process Automation (RPA) workflows that are prone to breaking <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## [[evaluating_the_performance_of_browser_agents | Evaluating Browser Agent Performance]]
Evaluating a browser agent involves giving it a task and determining if it completed it <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. In practice, this is complex due to:
*   **Task Data Set Creation**: Tasks need to be realistic, feasible, domain-specific, and scalable <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Evaluation Methods**: Evaluations can be automated (with validation functions), manual (with human annotators), or use LLM-as-a-judge approaches <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>.
*   **Infrastructure**: The performance of browser agents is significantly affected by the infrastructure they run on <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

Tasks can be categorized into two types <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>:
*   **Read Tasks**: Primarily involve information gathering and collection, similar to web scraping <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.
*   **Write Tasks**: Involve interacting with and changing the state on a website, requiring the agent to take action <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Write tasks are generally more complicated and challenging for both creation and agent performance <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### WebBench Benchmark Findings
WebBench is a benchmark data set and evaluation that includes over 5,000 tasks, half of which are open-sourced, across nearly 500 different websites <a class="yt-timestamp" data-t="00:05:19">[00:05:19]</a>.

*   **Read Task Performance**: Industry-leading web agents show good performance on read tasks, with the leading agent achieving around 80% success, close to a human-in-the-loop baseline <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>. This indicates agents are proficient at information retrieval and data extraction from the web <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Failures in read tasks are often related to infrastructure and internet issues rather than agent capability <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   **Write Task Performance**: Overall performance on write tasks is significantly worse, dropping by 50% or more compared to read tasks <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>.

#### [[challenges_and_limitation_of_current_browser_agents | Challenges and Limitations of Browser Agents]] for Write Tasks
Several factors contribute to the lower performance on write tasks <a class="yt-timestamp" data-t="00:07:33">[00:07:33]</a>:
*   **Longer Trajectory**: Write tasks typically involve more steps, increasing the likelihood of an agent making a mistake and failing the task <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Complicated UI Interaction**: Write tasks often involve more challenging or dynamic user interfaces, requiring data input and complex form interactions <a class="yt-timestamp" data-t="00:07:56">[00:07:56]</a>.
*   **Login and Authentication**: Many write tasks require logging in, which is challenging for agents due to interactive complexity and managing credentials <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Anti-bot Protections**: Sites with many write tasks often have stricter anti-bot measures, and performing write actions can trigger protections like CAPTCHAs <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

Overall, the best agents achieved about two-thirds success on combined read and write tasks, while the average was just over 50% <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. Despite these numbers, the fact that web agents can achieve such results on challenging benchmarks, given only a few years of development, is considered impressive <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Failure Patterns

### Agent Failures
These failures are primarily the responsibility of the agent's own capabilities <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Examples include:
*   Inability to interact with or close pop-ups that block task completion <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.
*   Timeout issues due to the agent taking too long to complete a task <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.

### Infrastructure Failures
These failures are related to the framework or infrastructure the agent is running on, preventing the agent from performing its task <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Examples include:
*   Being flagged and blocked as a bot from entering a site <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
*   Inability to access email verification for logins within the agent's framework <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.
Improving infrastructure, particularly in areas like CAPTCHA handling, proxies, and login authentication, could significantly boost agent performance <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

### Slowness
A major flaw with current agents is their speed <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This is due to:
*   The iterative observation, planning, and reasoning steps of the agent loop <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
*   Mistakes or failures in tool calls requiring retries <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   The time it takes to interact with and navigate sites <a class="yt-timestamp" data-t="00:13:51">[00:13:51]</a>.
While acceptable for async "set and forget" applications, this latency is a significant problem for real-time applications <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## Strategies for Building with Browser Agents

When [[building_effective_agents | building with browser agents]], AI engineers should consider these key takeaways:

### 1. Picking the Right Use Case
*   **Read Use Cases**: For tasks like deep research tools or mass information retrieval, current out-of-the-box browser agents are already quite performant <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>.
*   **Write Use Cases**: For products involving form filling or state-changing actions, be aware that out-of-the-box agents may not be as accurate <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. Rigorous testing and building internal evaluations are crucial before deploying them in production <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>.

### 2. Browser Infrastructure Matters
*   The choice of browser infrastructure can significantly impact performance <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
*   [[designing_and_optimizing_agent_environments | Test multiple providers]] as they are highly interoperable <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. Different systems may offer better CAPTCHA handling or unblocked proxies for specific sites <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. If experiencing proxy blocking on specific sites, contacting the provider can often resolve the issue <a class="yt-timestamp" data-t="00:16:34">[00:16:34]</a>.

### 3. Try a Hybrid Approach
*   Combine browser agents with more deterministic workflows, such as Playwright <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
*   Use agents for "long tail" tasks that are dynamic or change frequently <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
*   Utilize deterministic workflows for steps requiring constant movement, accuracy, and large volume reliability <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>.

## Future Developments
The industry is expected to improve many of the current problems facing browser agents <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>:
*   **Better Long Context Memory**: Crucial for accurately executing longer write tasks <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Improved Browser Infrastructure Primitives**: Addressing major blockers like login/authentication and payments will unlock significant value <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Better Underlying Models**: The models powering browser agents will continue to improve, particularly through training environments and sandboxes that enhance tool calling and write actions <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.

### Interesting Agent Behaviors
*   **AI Agent Inception**: A browser agent got stuck on GitHub and unblocked itself by conversing with GitHub's virtual assistant AI <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   **Turing Test Nods**: A browser agent posted a comment on a Medium article that became the top-liked post, raising questions about AI's indistinguishability from humans <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
*   **Real-World Externalities**: Browser agents booked restaurant reservations on users' behalf during testing, highlighting unintended real-world impacts <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **Emergent Behavior**: A browser agent, blocked by Cloudflare, searched Google for ways to bypass Cloudflare verification, demonstrating unpredictable emergent behavior <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.