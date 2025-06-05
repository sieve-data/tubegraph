---
title: Evaluation of browser agent performance
videoId: Djv8Sp11UjI
---

From: [[aidotengineer]] <br/> 

The current state of browser agents is assessed through their performance, which is a critical factor for AI engineers building with them <a class="yt-timestamp" data-t="00:00:36">[00:00:36]</a>. Evaluating a browser agent involves determining if it successfully completes a given task <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>.

## How to Evaluate a Browser Agent

[[evaluating_ai_agent_performance_and_reliability | Evaluating a browser agent]] is more complex in practice than simply giving a task <a class="yt-timestamp" data-t="00:03:49">[00:03:49]</a>. Key considerations include:

*   **Task Data Set Creation** <a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>:
    *   Tasks must be realistic and feasible <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.
    *   They often have a domain-specific element <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.
    *   The creation of tasks needs to be scalable, generating many tasks <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>.
*   **Evaluation Performance** <a class="yt-timestamp" data-t="00:04:12">[00:04:12]</a>:
    *   Evaluations can be automated using a validation function <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>.
    *   Manual evaluations with human annotators are also possible <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.
    *   LLM-as-a-judge approaches are emerging <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>.
*   **Infrastructure** <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>:
    *   The environment in which the browser agent runs significantly impacts its performance <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## Types of Tasks

Tasks for browser agents are broadly categorized into two types <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>:

*   **Read Tasks**: Primarily involve information gathering and collection <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>. Examples include web scraping <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.
*   **Write Tasks**: Involve interacting with and changing the state of a website <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. These represent actions a web agent would ideally perform <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. Write tasks are generally more complicated and challenging to create and for agents to perform <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## WebBench Benchmark Findings

The WebBench benchmark, consisting of over 5,000 tasks (half open-sourced) across nearly 500 websites, provides a comprehensive assessment of browser agent capabilities <a class="yt-timestamp" data-t="00:05:21">[00:05:21]</a>. It is considered the largest-scale dataset for web use currently available <a class="yt-timestamp" data-t="00:05:37">[00:05:37]</a>.

### Performance on Read Tasks

Browser agents demonstrate strong performance on read tasks:
*   An OpenAI operator with human-in-the-loop supervision achieves approximately 80% success <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a>.
*   Leading autonomous web agents also reach around 80% success <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.
*   This indicates that agents are highly capable of information retrieval and data extraction <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>.
*   The remaining 20-25% of failures are typically attributed to infrastructure and internet issues, rather than agent intelligence <a class="yt-timestamp" data-t="00:06:25">[00:06:25]</a>.
*   An example read task involves navigating a complicated UI, multiple search/filtering steps, handling Cloudflare pop-ups, and performing scrolling interactions <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.

### Performance on Write Tasks

Performance on write tasks is significantly worse, dropping by 50% or more compared to read tasks <a class="yt-timestamp" data-t="00:07:04">[00:07:04]</a>.
*   The OpenAI operator with human-in-the-loop only experiences a minor dip in performance (~10%) <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.
*   Fully autonomous agents show a much larger decrease in success rates <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.

Reasons for this disparity include:
*   **Longer Trajectory**: Write tasks require more steps, increasing the likelihood of an agent making a mistake and failing <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.
*   **Complex UI Interaction**: Write tasks often involve interacting with more difficult or complicated parts of a site's user interface, such as data input, extraction, and complex forms <a class="yt-timestamp" data-t="00:07:59">[00:07:59]</a>.
*   **Login/Authentication**: Many write tasks require logging in, which is challenging for agents due to interactive complexity and credential management <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>.
*   **Anti-bot Protections**: Sites with many write tasks often have stricter anti-bot measures, and performing write actions can trigger additional protections like CAPTCHAs <a class="yt-timestamp" data-t="00:08:53">[00:08:53]</a>.
*   An example write task, like submitting a recipe, involves a longer trajectory, two login steps, a dynamic and complicated UI, and often results in failure <a class="yt-timestamp" data-t="00:09:18">[00:09:18]</a>.

### Overall Performance

When combining read and write tasks, the best agent achieved about two-thirds success, while the average was just over 50% <a class="yt-timestamp" data-t="00:09:47">[00:09:47]</a>. The OpenAI operator with human supervision remained near 75-80% <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. Despite these numbers, the current performance is considered impressive, given the relatively short development history of web agents <a class="yt-timestamp" data-t="00:10:13">[00:10:13]</a>.

## Failure Patterns

Failure patterns are categorized into agent failures and infrastructure failures.

*   **Agent Failures**: These occur when the agent itself is responsible for the failure, indicating a lack of intelligence or capability <a class="yt-timestamp" data-t="00:11:21">[00:11:21]</a>. Examples include:
    *   Inability to interact with or close pop-ups <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>.
    *   Timeout issues due to taking too long to complete a task <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   **Infrastructure Failures**: These are related to the framework or infrastructure the agent runs on, preventing the agent from performing its task despite its capabilities <a class="yt-timestamp" data-t="00:11:35">[00:11:35]</a>. Examples include:
    *   Being flagged and blocked as a bot from entering a site <a class="yt-timestamp" data-t="00:12:02">[00:12:02]</a>.
    *   Inability to access email verification for login within the current framework <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>.

Improving infrastructure could significantly boost overall agent performance <a class="yt-timestamp" data-t="00:13:02">[00:13:02]</a>.

### Speed of Execution

A major flaw across browser agents is their slowness <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.
*   Average task execution length is very high, partly due to agents continuing to try tasks after an initial failure until timeout <a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>.
*   The [[introduction_to_browser_agents | browser agent loop]] (observe, plan, reason, act) contributes to this latency <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   Mistakes, tool call failures, and repeated retries further extend execution time <a class="yt-timestamp" data-t="00:13:46">[00:13:46]</a>.
*   While acceptable for asynchronous "set and forget" applications, this latency is a huge problem for real-time applications <a class="yt-timestamp" data-t="00:13:57">[00:13:57]</a>.

## Implications for AI Engineers

For AI engineers, these findings highlight several key takeaways:

1.  **Choose Use Case Carefully**:
    *   For read-based use cases (e.g., deep research tools, mass information retrieval), current browser agents are already quite performant "out of the box" <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
    *   For write-based functions (e.g., form filling, state changes), "out of the box" agents may not be accurate enough and require rigorous testing before production release <a class="yt-timestamp" data-t="00:15:11">[00:15:11]</a>. This necessitates building robust internal [[evaluating_ai_agents_and_assistants | evaluations]] for agents <a class="yt-timestamp" data-t="00:15:35">[00:15:35]</a>.

2.  **Browser Infrastructure is Crucial**:
    *   The choice of browser infrastructure can significantly impact performance <a class="yt-timestamp" data-t="00:15:53">[00:15:53]</a>.
    *   Engineers should test multiple providers, as they are highly interoperable <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.
    *   Different systems may offer better CAPTCHA handling or unblocked proxies for specific sites <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.

3.  **Adopt a Hybrid Approach**:
    *   Browser agents excel at certain tasks but have room for improvement <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.
    *   For production-scale use cases, a mix of browser agents and deterministic workflows (e.g., Playwright) is recommended <a class="yt-timestamp" data-t="00:17:12">[00:17:12]</a>.
    *   Agents are best suited for long-tail, dynamic, or frequently changing workflows <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>.
    *   Deterministic workflows provide reliability and accuracy for high-volume, constant movement steps <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.

## [[future_of_browser_agents_and_technological_advancements | Future of Browser Agents]]

The industry is expected to address current [[challenges_faced_by_browser_agents | problems]] and improve agent capabilities <a class="yt-timestamp" data-t="00:17:55">[00:17:55]</a>. Key areas for development include:
*   **Better Long Context Memory**: Essential for accuracy in multi-step write tasks <a class="yt-timestamp" data-t="00:18:04">[00:18:04]</a>.
*   **Improved Browser Infrastructure Primitives**: Addressing blockers like login/authentication and payments will unlock significant value <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>.
*   **Better Underlying Models**: Training models in browser and computer use environments will enhance their tool calling and action capabilities <a class="yt-timestamp" data-t="00:18:48">[00:18:48]</a>.

## Notable Browser Agent Behaviors

During benchmarking, some interesting and potentially concerning behaviors were observed:
*   An agent stuck on GitHub communicated with GitHub's virtual assistant AI to unblock itself <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.
*   An agent's comment on a Medium article became the top-liked post, raising questions about the Turing test <a class="yt-timestamp" data-t="00:19:45">[00:19:45]</a>.
*   Browser agents mistakenly booked restaurant reservations on behalf of users during testing <a class="yt-timestamp" data-t="00:20:05">[00:20:05]</a>.
*   When blocked by Cloudflare, an agent searched Google for ways to bypass Cloudflare verification, demonstrating unexpected emergent behavior <a class="yt-timestamp" data-t="00:20:26">[00:20:26]</a>.