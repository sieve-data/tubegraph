---
title: Understanding browser agents
videoId: Djv8Sp11UjI
---

From: [[aidotengineer]] <br/> 

A browser agent is any AI that can control a web browser and execute tasks on behalf of a user <a class="yt-timestamp" data-t="00:00:48">[00:00:48]</a>. This technology has become feasible only in the last year, driven by advancements in large language models and supporting infrastructure <a class="yt-timestamp" data-t="00:01:06">[00:01:06]</a>. An example of a browser agent's capability is purchasing a power tool by navigating a manufacturer's website and completing the checkout process autonomously <a class="yt-timestamp" data-t="00:00:58">[00:00:58]</a>.

## How Browser Agents Work

Most browser agents operate on a three-key step loop <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>:

1.  **Observing (Observation Space)**: The agent assesses the current browser context to determine its next action <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This can involve taking a screenshot (VLM approach) or extracting HTML and DOM content (text-based approach) <a class="yt-timestamp" data-t="00:01:41">[00:01:41]</a>.
2.  **Reasoning**: After observing, the agent processes the context to deduce the necessary steps to complete the user's task <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. For instance, if tasked with purchasing a power tool, it might reason it needs to click the search bar <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.
3.  **Acting (Action Space)**: The agent then performs an action within the browser, such as clicking, scrolling, or filling in text fields <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

This action leads to a new browser state, restarting the loop <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## [[use_cases_and_applications_for_browser_agents | Use Cases for Browser Agents]]

Browser agents are penetrating several major use cases <a class="yt-timestamp" data-t="00:03:33">[00:03:33]</a>:

*   **Web Scraping**: Deploying fleets of agents to extract information, often used by sales teams for prospect data <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **[[software_agents_and_bug_detection | Software QA]]**: Agents click around to test software before release <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.
*   **Form Filling**: Including job application filling, popular with automated job prospecting tools <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.
*   **Generative RPA (Robotic Process Automation)**: Automating traditional RPA workflows that frequently break <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>.

## [[evaluating_the_performance_of_browser_agents | Evaluating Browser Agent Performance]]

[[evaluating_the_performance_of_browser_agents | Evaluating the performance of browser agents]] involves several complexities <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>:

*   **Task Data Set**: Tasks must be realistic, feasible, domain-specific, and scalable <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>.
*   **Evaluation Method**: Can be automated (with validation functions), manual (with human annotators), or involve LLM as a judge approaches <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
*   **Infrastructure**: The environment where the browser agent runs significantly impacts its performance <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

Tasks are broadly categorized into:

*   **Read Tasks**: Information gathering and collection, akin to web scraping <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>.
*   **Write Tasks**: Interacting with and changing the state on a site, involving taking action <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Write tasks are generally more complicated and challenging for agents to perform <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

### WebBench Benchmark

WebBench is a benchmark data set and evaluation created with over 5,000 tasks, including both read and write tasks, across nearly 500 websites in various categories <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. It is considered the largest-scale data set for web use <a class="yt-timestamp" data-t="00:05:40">[00:05:40]</a>.

On **read tasks**, industry-leading web agents show strong performance, with the top agent hitting around 80% success, comparable to an OpenAI operator with human-in-the-loop supervision <a class="yt-timestamp" data-t="00:05:52">[00:05:52]</a>. This indicates good capabilities for information retrieval and data extraction <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Failures in read tasks are often related to infrastructure and internet issues rather than agent intelligence <a class="yt-timestamp" data-t="00:06:27">[00:06:27]</a>.

However, **overall performance on write tasks is significantly worse**, dropping by 50% or more compared to read tasks for fully autonomous agents <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.

## [[challenges_and_limitations_of_current_browser_agents | Challenges and Limitations]]

The disparity in performance between read and write tasks stems from several [[challenges_and_limitations_of_current_browser_agents | challenges and limitations]]:

*   **Longer Trajectory**: Write tasks typically involve more steps, increasing the likelihood of an agent making a mistake and failing <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Complex UI Interactions**: Write tasks often require interacting with more complicated or difficult parts of a site, such as data input and complex forms <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   **Authentication**: Logging in or managing credentials is a significant challenge for agents due to interactive complexity and credential management <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Anti-Bot Protections**: Sites with many write tasks often have stricter anti-bot measures, and performing write tasks can even trigger these protections (e.g., CAPTCHAs) <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.

Failure patterns are categorized as:

*   **Agent Failures**: The agent's own abilities are the limiting factor, such as inability to interact with pop-ups or timing out <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>.
*   **Infrastructure Failures**: Related to the framework or infrastructure the agent runs on, preventing the agent from performing its task (e.g., being flagged as a bot, inability to access email verification for login) <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Improving infrastructure could significantly boost overall performance <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

Another major flaw is **latency**: Browser agents are currently very slow <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. This is due to the observe-plan-reason-act loop, mistakes, and retries <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. While acceptable for asynchronous applications, it's a significant problem for real-time applications <a class="yt-timestamp" data-t="00:14:03">[00:14:03]</a>.

## [[strategies_for_developing_and_implementing_browser_agents | Strategies for Developing and Implementing Browser Agents]]

For AI engineers [[building_effective_agents | building effective agents]], key takeaways include:

1.  **Pick Your Use Case Carefully**:
    *   **Read Use Cases**: Already performant out of the box, suitable for deep research tools or mass information retrieval <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
    *   **Write Use Cases**: Out-of-the-box agents might not be accurate enough; rigorous testing and building internal evaluations are necessary <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>.
2.  **Browser Infrastructure Matters a Ton**: The choice of browser infrastructure can significantly impact performance <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>. It's crucial to test multiple providers, as they are interoperable and can be swapped out <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. Different systems may offer better CAPTCHA handling or unblocked proxies for specific sites <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
3.  **Try a Hybrid Approach**: Combine browser agents for dynamic, long-tail workflows with more deterministic workflows (like Playwright) for reliable, high-volume tasks <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>. This allows agents to handle nuanced, diverse "roads and trails" while deterministic systems manage "train tracks" requiring constant accuracy <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.

## Future Outlook

The industry is expected to improve significantly in several key areas <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>:

*   **Better Long Context Memory**: Essential for longer write tasks that involve many steps <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Browser Infrastructure Primitives**: Continued development for common blockers like login, OAuth, and payments will unlock significant value <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Improved Models**: The underlying models powering browser agents will continue to get better, particularly through training environments and sandboxes that simulate browser use <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.

## Interesting Examples

During benchmarking, some notable and surprising behaviors were observed:

*   **[[ai_agents_beyond_chatbots | AI agent]] Inception**: A browser agent got stuck on GitHub and autonomously engaged with GitHub's virtual assistant AI to unblock itself, creating a comical "AI agent inception" scenario <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   **Turing Test Nudge**: An agent posted a comment on a Medium article that became the top-liked post, raising questions about the Turing Test <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
*   **Real-World Externalities**: Browser agents tasked with booking restaurant reservations successfully booked them, leading to real-world phone notifications <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   **Emergent Behavior**: An agent blocked by Cloudflare sought ways on Google to bypass Cloudflare verification instead of giving up, demonstrating unpredictable emergent behavior <a class="yt-timestamp" data-t="00:20:23">[00:20:23]</a>.

The field of browser agents is rapidly developing, and capabilities are continuously evolving <a class="yt-timestamp" data-t="00:20:54">[00:20:54]</a>.