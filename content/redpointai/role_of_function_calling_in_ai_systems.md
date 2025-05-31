---
title: Role of function calling in AI systems
videoId: zG-kxc0q_cE
---

From: [[redpointai]] <br/> 

Function calling is recognized as a crucial capability within AI systems, particularly for building advanced [[implications_of_autonomous_ai_agents | agents]] <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>. It serves as an extension point, allowing AI [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | models]] to interact with external tools and enhance the quality of their responses <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. Fireworks, a company specializing in inference for [[ai_inference_and_compound_ai_systems | compound AI systems]], has heavily invested in this area <a class="yt-timestamp" data-t="00:23:26">[00:23:26]</a>.

## What is Function Calling?

Function calling enables an AI [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | model]] to "call" or access other tools to improve the accuracy and utility of its answers <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. This is particularly important when building [[implications_of_autonomous_ai_agents | agents]] <a class="yt-timestamp" data-t="00:21:34">[00:21:34]</a>. In a broader sense, each individual small expert [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | model]] can be considered a tool within this framework <a class="yt-timestamp" data-t="00:24:38">[00:24:38]</a>.

## Complexities of Function Calling

The implementation of function calling is more intricate than simply calling a single tool <a class="yt-timestamp" data-t="00:21:50">[00:21:50]</a>. Key complexities include:
*   **Context Management** [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | Models]] need to maintain and understand a long context of conversation in multi-turn chat scenarios to influence which tools are best to call <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>.
*   **Multiple Tool Selection** Often, [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | models]] need to call into multiple tools, potentially hundreds, for a single query <a class="yt-timestamp" data-t="00:22:11">[00:22:11]</a>.
*   **Parallel and Sequential Execution** [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | Models]] must be capable of coordinating and executing calls to multiple tools both in parallel and sequentially <a class="yt-timestamp" data-t="00:22:25">[00:22:25]</a>.
*   **Orchestration and Precision** The ability to orchestrate and execute a complex plan of tool calls is crucial, and the precision of tool selection is vital for delivering accurate results <a class="yt-timestamp" data-t="00:22:41">[00:22:41]</a>, <a class="yt-timestamp" data-t="00:23:20">[00:23:20]</a>.
*   **Tuning Process** The intricate nature of function calling makes the tuning process for these [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | models]] very complicated <a class="yt-timestamp" data-t="00:23:23">[00:23:23]</a>.

For example, to fulfill a request like "chart of a stock price of top three cloud providers," an AI system using function calling would need to:
1.  Perform a search to identify the top three cloud providers <a class="yt-timestamp" data-t="00:22:59">[00:22:59]</a>.
2.  Execute three parallel function calls to retrieve each provider's stock price <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.
3.  Make another call to a charting tool to generate the visual representation <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>.

## Integration into Compound AI Systems

Function calling is a critical ingredient for tying together the components of [[ai_inference_and_compound_ai_systems | compound AI systems]] <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>. These systems are designed to go beyond single [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | model]] services by combining multiple [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | models]] across different modalities with various APIs to solve complex [[role_of_ai_in_future_business_operations | business]] problems <a class="yt-timestamp" data-t="00:02:40">[00:02:40]</a>, <a class="yt-timestamp" data-t="00:04:16">[00:04:16]</a>. The ability of a [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | model]] to intelligently orchestrate and call into different tools is essential for this composability <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>, <a class="yt-timestamp" data-t="00:24:31">[00:24:31]</a>.

Fireworks has developed its own F1 [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | model]] that operates as a complex logical reasoning inference system capable of parallel and sequential function calls, as well as orchestrating and executing complex plans <a class="yt-timestamp" data-t="00:19:37">[00:19:37]</a>, <a class="yt-timestamp" data-t="00:22:34">[00:22:34]</a>. This internal development helps them understand the system abstraction and complexity needed to build [[developers_approach_to_ai_models_and_agents | developer]]-facing tools that allow [[developers_approach_to_ai_models_and_agents | developers]] to build their own "F1s" <a class="yt-timestamp" data-t="00:28:02">[00:28:02]</a>.

## Future of Function Calling and Agentic Workflows

While still in early stages, the adoption curve for function calling and [[implications_of_autonomous_ai_agents | agentic]] workflows is beginning to take off <a class="yt-timestamp" data-t="00:23:36">[00:23:36]</a>, <a class="yt-timestamp" data-t="00:27:08">[00:27:08]</a>. These systems are currently more focused on human-in-the-loop [[role_of_ai_in_transforming_job_functions | automation]] rather than fully autonomous operation <a class="yt-timestamp" data-t="00:14:09">[00:14:09]</a>, primarily because human oversight is still necessary for evaluation, maintenance, and operation in production <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

Successful [[role_of_ai_in_general_intelligence_and_application_development | applications]] seen thus far include [[developing_ai_meeting_assistants | assistants]] for doctors (scribing), teachers, students (foreign language learning), coding ([[developing_ai_meeting_assistants | assistant]] to coding), and medical [[developing_ai_meeting_assistants | assistants]] for nurses <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>. B2B [[role_of_ai_in_general_intelligence_and_application_development | applications]] also leverage function calling for call center [[role_of_ai_in_transforming_job_functions | automation]] to make human agents more productive <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

The challenge for the industry remains in defining the right user experience and abstraction for [[implications_of_autonomous_ai_agents | agentic]] workflows <a class="yt-timestamp" data-t="00:27:14">[00:27:14]</a>. Despite the rapid changes in [[role_of_ai_models_in_advancing_robotics_and_autonomous_driving | model]] capabilities, the underlying trend toward specialization and customization through solutions like function calling remains constant <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>.