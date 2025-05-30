---
title: Benefits and features of Windsurf
videoId: ukhe1013Jpk
---

From: [[colemedin]] <br/> 

[[introduction_to_windsurf_as_an_ai_ide | Windsurf]] is described as the best AI IDE, combining the strengths of a co-pilot with the capabilities of an agent for long-running and complex coding tasks <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Users can easily collaborate with it as a co-pilot <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>, and it excels at performing intricate coding tasks as an agent <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>. Despite being a relatively new platform, it has quickly enabled users to become "super users" <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. While not perfect and requiring coding knowledge for production-ready code <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>, [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] saves hours of coding time, allowing developers to focus on building high-quality code <a class="yt-timestamp" data-t="00:01:08">[00:01:08]</a>. It aids in laying groundwork, writing tests, and documenting code <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>.

## Revolutionary "Flow State" Experience

[[introduction_to_windsurf_as_an_ai_ide | Windsurf]], created by Codium, is designed to keep developers in a "Flow State" <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>. This means providing a cohesive experience where the agent and developer work together seamlessly, rather than as separate processes <a class="yt-timestamp" data-t="00:02:05">[00:02:05]</a>.

### Evolution of AI in Coding
*   **2022 (Co-pilots)**: Introduced AI help with small parts of the coding process, like autocomplete or research, but lacked integration <a class="yt-timestamp" data-t="00:03:10">[00:03:10]</a>.
*   **2024 (Agents)**: Large language models could generate code, run commands, and interact with knowledge bases <a class="yt-timestamp" data-t="00:03:28">[00:03:28]</a>. However, issues included unreasonable waiting periods, inconsistent results, and poor integration with the IDE <a class="yt-timestamp" data-t="00:03:42">[00:03:42]</a>.
*   **November 2024 (Flows with [[introduction_to_windsurf_as_an_ai_ide | Windsurf]])**: The timeline between the user and the AI agent is completely synced <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. The agent is aware of user changes, and users can easily see agent changes, fostering an integrated "pair programmer" experience <a class="yt-timestamp" data-t="00:04:09">[00:04:09]</a>.

## Workflow and Integration

A common workflow involves combining [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] with other tools:
*   Initial front-end development is often done in [[effective_strategies_for_using_windsurf_in_coding | AutoDev]] or [[recent_updates_and_features_in_bolt_new_fork | Bolt.new]], which excel in this area <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>.
*   Once the initial build is complete or gets stuck, the project can be exported and brought into [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] for finishing touches <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>.
*   [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] particularly excels at back-end development, especially with Python coding and database management <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## Effective Strategies for Power Users

To maximize productivity with [[introduction_to_windsurf_as_an_ai_ide | Windsurf]]:

### Manage Conversations and Prompts
*   **Start New Conversations**: If the AI starts to hallucinate due to long conversation history, starting a brand new conversation by clicking the button in the top right can resolve the issue <a class="yt-timestamp" data-t="00:08:48">[00:08:48]</a>.
*   **One Request at a Time**: Avoid spamming prompts with multiple problems. Instead, give one request at a time, ensure it's implemented correctly, and then move to the next <a class="yt-timestamp" data-t="00:09:37">[00:09:37]</a>. This patience leads to better results and saves overall time <a class="yt-timestamp" data-t="00:10:05">[00:10:05]</a>.
*   **Be Specific from the Start**: Define your tech stack, programming languages (e.g., Python), technologies (e.g., FastAPI), and database (e.g., Postgres hosted with Superbase) explicitly when beginning a new application <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. This guidance is crucial for getting the desired output <a class="yt-timestamp" data-t="00:14:14">[00:14:14]</a>.

### Control and Verify Changes
*   **Test Before Accepting**: [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] implements changes in the code before you accept or reject them <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. This allows users to test the changes in the application first and then reject them if they don't work or are not desired <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.
*   **Accept or Reject Specific Changes**: Users can accept or reject individual changes across different files <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. This is useful when the AI gets some things right but others wrong, allowing selective adoption <a class="yt-timestamp" data-t="00:11:26">[00:11:26]</a>. The agent also learns from these rejections for future interactions <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

### Directed Interactions
*   **Call Out Specific Files/Functions**: Use the `@` symbol to reference specific files or functions (e.g., `@useConversations`) <a class="yt-timestamp" data-t="00:12:21">[00:12:21]</a>. This directs the agent, prevents hallucinations, and ensures it edits the correct parts of the codebase <a class="yt-timestamp" data-t="00:12:50">[00:12:50]</a>.
*   **Refactor/Explain Specific Functions**: Select a function or class and use the "Refactor" button for directed changes, which focuses the AI's context on that specific part of the code <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. Similarly, the "Explain" button provides understanding of specific functions, useful for reviewing AI-produced code or imported projects <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>.

### Leveraging AI for Development Tasks
*   **Troubleshooting with External LLMs**: If [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] (using Cloud 3.5 Sonnet) gets stuck, an external LLM like `01` can be used to get a fix <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>. The fix can then be manually applied in [[introduction_to_windsurf_as_an_ai_ide | Windsurf]], which maintains awareness of the changes, allowing continued work <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.
*   **Code Documentation**: [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] is phenomenal for documenting code, saving significant time <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. It's crucial to instruct the AI not to update the code while adding documentation <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. While "Add doc string" is available, prompting for broader documentation (including in-line comments) is often preferred <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   **Writing Tests**: [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] is very helpful for writing tests, handling boilerplate setup for libraries like `Jest` and `React Testing Library` for front-ends, or `Pytest` for back-ends <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. While tests may not work perfectly initially, the AI significantly reduces setup time <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

## The Future of AI IDEs

The capabilities of AI IDEs like [[introduction_to_windsurf_as_an_ai_ide | Windsurf]] are rapidly advancing <a class="yt-timestamp" data-t="00:18:43">[00:18:43]</a>. The future envisions fully agentic IDEs running locally, with full access to the computer, capable of researching library documentation, and deploying built projects <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>. This vision is seen as "within reach" <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>.