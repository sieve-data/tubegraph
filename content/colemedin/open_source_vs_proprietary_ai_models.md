---
title: Open source vs proprietary AI models
videoId: xfFyAumTjT0
---

From: [[colemedin]] <br/> 

After the release of DeepSeek R1, an [[open_source_ai_agent_development | open source]] reasoning large language model (LLM), OpenAI quickly responded by releasing O3 Mini, their next-generation advanced reasoning model <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This article compares these two impressive reasoning LLMs, focusing on their performance in coding tasks using the [[opensource_ai_coding_assistant_development | open source AI coding assistant]] bolt.DIY <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Key Differences Between DeepSeek R1 and OpenAI O3 Mini

While both are powerful reasoning LLMs, there are significant [[differences_in_architecture_and_functionality_of_ai_models | differences in architecture and functionality of AI models]] <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>:

*   **Open Source vs. Proprietary**: R1 is [[opensource_benefits_and_enterprise_security_in_ai_tools | open source]], whereas O3 Mini is not <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Architecture**:
    *   OpenAI O3 Mini utilizes a dense Transformer architecture, typical of most OpenAI models <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   DeepSeek R1 employs a Mixture of Experts (MoE) combined with reinforcement learning from Human Feedback (RLHF), representing a completely different architecture <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Strengths**:
    *   O3 Mini is generally considered better for more directed tasks, often seen in [[open_source_ai_agent_development | AI agents]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
    *   R1 excels at more logical, free-thinking tasks, such as solving logic problems and deep research <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Other Differences**: These include context limits and total parameters for the models <a class="yt-timestamp" data-t="00:01:19">[00:01:19]</a>.

### Pricing
While pricing can vary, generally DeepSeek R1 is more affordable than O3 Mini <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. However, a Nitro version of R1 used for testing due to API outages was more expensive than its standard version <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## Testing Methodology

The comparison was performed using bolt.DIY, an [[open_source_ai_coding_assistants_and_community_building | open source AI coding assistant]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. O3 Mini was accessed directly through the OpenAI API, while DeepSeek R1 was accessed via OpenRouter due to DeepSeek API outages <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. The tests involved building:
1.  A simple to-do application.
2.  A more complex chat frontend for [[open_source_ai_agent_development | AI agents]].
3.  A fully functional chess site with minimal prompting.

### Repo Cloud: Hosting Open Source Projects
Repo Cloud, a cloud platform and [[open_source_ai_tools_for_database_management | open source]] app marketplace, offers competitive pricing and elastic auto-scaling, allowing users to pay only when instances are used <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. It supports one-click deployments for numerous [[open_source_ai_tools_for_database_management | open source]] applications, including bolt.DIY <a class="yt-timestamp" data-t="00:09:52">[00:09:52]</a>. This platform can save users an average of 93% on cloud bills compared to traditional providers like AWS EC2, DigitalOcean, and Linode <a class="yt-timestamp" data-t="00:09:11">[00:09:11]</a>.

## Test Case 1: Simple To-Do Application

### OpenAI O3 Mini Performance
O3 Mini built the simple application in approximately 10 seconds <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>. It successfully created a functional to-do list where tasks could be added, marked off, and deleted <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>. However, it failed to run the command to start the site, requiring manual intervention <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### DeepSeek R1 Performance
DeepSeek R1 took longer, about 20-30 seconds, to build the same application <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. Despite being slower, R1 performed a "true one-shot" by also running the command to start the site <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>. R1 also produced a more feature-rich application, such as displaying the number of complete tasks and a "task list empty" message, demonstrating better reasoning about user needs <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.

**Initial Verdict**: O3 Mini excelled in speed, while R1 showed superior functionality and thoughtful UI design <a class="yt-timestamp" data-t="00:07:10">[00:07:10]</a>.

## Test Case 2: Complex AI Agent Chat Frontend

This test involved building a chat frontend that integrates with Superbase for authentication and chat history management <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

### OpenAI O3 Mini Performance
O3 Mini required a few attempts and error corrections to reach a working state <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. It initially mixed up routes and encountered other errors that had to be fixed using bolt.DIY's error-correction feature <a class="yt-timestamp" data-t="00:11:55">[00:11:55]</a>. Once functional, the application allowed conversation history loading and sending messages, but it duplicated user messages due to misinterpreting database message handling <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

### DeepSeek R1 Performance
R1 took significantly longer than O3 Mini to complete this complex task, highlighting the speed difference with more intricate applications <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>. However, R1 compiled correctly in a single shot, unlike O3 Mini <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. While it produced a visually appealing UI with more functionality, it also suffered from the duplicate message issue and failed to load previous conversations initially <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

**Verdict**: O3 Mini demonstrated better raw functionality and stability, despite needing several corrections. R1 produced a nicer UI and compiled on the first try but had more glitches with core functionality like loading conversations <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

## Test Case 3: Fully Functional Chess Site (Creative Freedom)

This test provided a single sentence prompt: "Build me a fully functional chess site" <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

### OpenAI O3 Mini Performance
O3 Mini again encountered initial errors and struggled with routing, starting with a default template before producing a chessboard <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>. While it created a functional board, it did not fully adhere to chess rules; for example, pawns could not move two spaces on the first move, and it was possible to capture the king or put oneself in check <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

### DeepSeek R1 Performance
DeepSeek R1 produced a much more visually appealing chessboard <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. However, its functionality was severely limited, with pieces being able to move freely across the board without adhering to any chess rules, making it more of a visual representation than a functional game <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

**Verdict**: R1 maintained its lead in UI design, but O3 Mini provided slightly better adherence to the complex rules of chess, even if imperfect <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

## Conclusion: Pros and Cons

Both DeepSeek R1 and OpenAI O3 Mini are incredible LLMs with distinct strengths <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>:

*   **OpenAI O3 Mini**:
    *   **Pros**: Faster generation <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>, better at implementing raw functionality and adhering to rules (though imperfectly) <a class="yt-timestamp" data-t="00:17:56">[00:17:56]</a>.
    *   **Cons**: May require more iterations to fix errors, less intuitive UI.
*   **DeepSeek R1**:
    *   **Pros**: Superior UI design <a class="yt-timestamp" data-t="00:17:48">[00:17:48]</a>, better reasoning about user intent and adding thoughtful features <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>, often compiles on the first shot even for complex tasks <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
    *   **Cons**: Slower generation <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>, may implement functionality with more glitches.

There appears to be an opportunity to combine these two LLMs, leveraging O3 Mini for functionality and R1 for enhanced features and UI <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. The choice between them often depends on the specific task requirements, prioritizing speed and core functionality versus superior UI and creative interpretation <a class="yt-timestamp" data-t="00:18:50">[00:18:50]</a>.