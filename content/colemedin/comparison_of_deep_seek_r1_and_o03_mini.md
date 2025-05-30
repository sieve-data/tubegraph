---
title: Comparison of deep seek R1 and o03 mini
videoId: xfFyAumTjT0
---

From: [[colemedin]] <br/> 

Following the release of [[deepseek_r1_model_features | DeepSeek R1]], an open-source reasoning LLM, OpenAI responded by releasing 03 mini (GPT-4o mini), their next-generation advanced reasoning model <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Both models are considered highly impressive reasoning LLMs <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

This article compares [[comparing_llama_32_to_gpt_40_mini | 03 mini]] and [[deepseek_r1_model_features | DeepSeek R1]], focusing on their performance in coding tasks using Bolt.DIY, an open-source AI coding assistant <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Key Differences and Strengths
While both are reasoning LLMs, they operate differently "under the hood" <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **Open Source Status**: [[deepseek_r1_model_features | DeepSeek R1]] is open-source, while 03 mini is not <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.
*   **Architecture**:
    *   03 mini utilizes a dense Transformer architecture <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
    *   [[deepseek_r1_model_features | DeepSeek R1]] is a mixture-of-experts model combined with reinforcement learning from human feedback (RLHF) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.
*   **Task Specialization**:
    *   03 mini is generally considered better for more "directed tasks," often seen in AI agents <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
    *   [[deepseek_r1_model_features | DeepSeek R1]] excels at "logical freethinking tasks," such as solving logic problems and deep research <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **Cost**: Generally, [[deepseek_r1_model_features | DeepSeek R1]] is much cheaper than 03 mini <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. However, during testing, the Nitro version of R1 (via OpenRouter's Together AI) was used due to DeepSeek API outages, making it more expensive than the standard R1 <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## Testing Methodology
The comparison involved using Bolt.DIY, an open-source AI coding assistant, to generate applications with both 03 mini and [[deepseek_r1_model_features | DeepSeek R1]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. Bolt.DIY allows users to integrate various LLMs and provides features like error pasting for easy debugging <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.

The tests progressed from simple to more complex prompts, aiming to assess coding ability, functionality, user interface (UI), and problem-solving.

### Sponsor: Reple Cloud
Reple Cloud is a cloud platform and open-source app marketplace offering competitive pricing, elastic auto-scaling (saving an average of 93% on cloud bills by only paying for active instance usage), and one-click deployments for open-source applications <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>. It hosts a wide range of open-source apps, including Bolt.DIY <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

## Application Development Comparison

### Test 1: Simple React with Tailwind To-Do App
*   **03 Mini Performance**:
    *   Built the app in approximately 10 seconds <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
    *   Did not run the command to start the site, requiring manual execution (`npm run dev`) <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   Functionality was good, allowing tasks to be added, marked off, and deleted <a class="yt-timestamp" data-t="00:06:35">[00:06:35]</a>.
    *   Had minor oddities, such as crediting an "unsplash" background photo that wasn't present <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>.
*   **[[deepseek_r1_model_features | DeepSeek R1]] Performance**:
    *   Took longer (20-30 seconds) than 03 mini <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
    *   Automatically ran the command to start the site, offering a "true one-shot" build <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
    *   Produced a more feature-rich UI, including a task counter ("0 of 2 complete") that updated in real-time, showing better reasoning for user needs <a class="yt-timestamp" data-t="00:07:44">[00:07:44]</a>.
    *   Displayed a "your task list is empty and serene" message when no tasks were present <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
*   **Initial Findings**: [[speed_and_performance_comparison_with_other_llms | Speed]] went to 03 mini, but functionality and UI went to [[deepseek_r1_model_features | DeepSeek R1]] <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### Test 2: Complex AI Agent Chat Front-end
This test involved a detailed prompt to create a chat front-end integrating with Superbase for authentication and chat history management <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.
*   **03 Mini Performance**:
    *   Required "a few tries" to reach a working state <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.
    *   Initially mixed up routes, showing a Remix starter template <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>.
    *   Needed several error corrections via Bolt.DIY's automated error pasting feature <a class="yt-timestamp" data-t="00:12:04">[00:12:04]</a>.
    *   Successfully loaded conversation history and allowed continuing conversations <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
    *   Duplicated user messages in the chat history, indicating a misunderstanding of how messages came from the database <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
*   **[[deepseek_r1_model_features | DeepSeek R1]] Performance**:
    *   Took "a lot longer" than 03 mini <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
    *   Compiled on a single shot, unlike 03 mini <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
    *   UI appearance was generally better than 03 mini's output <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
    *   Initially failed to load conversations, a functional glitch <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.
    *   Also had the same duplicate user message error <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.
    *   Overall, more features but also more glitches than 03 mini <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.
*   **Interim Findings**: The [[speed_and_performance_comparison_with_other_llms | speed difference]] was exaggerated with complexity. 03 mini required more iterations to compile but resulted in fewer glitches. [[deepseek_r1_model_features | DeepSeek R1]] provided a better UI but had more functional issues <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

### Test 3: Fully Functional Chess Site (Creative Freedom)
This test used a very simple prompt ("Build me a fully functional chess site") to see how each LLM handled creative freedom <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>.
*   **03 Mini Performance**:
    *   Messed up several times, initially reverting to the Remix starter template <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
    *   Produced a chess board that allowed pieces to be moved <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
    *   Did not understand basic chess rules (e.g., pawn's two-square first move, king capture, putting oneself in check) <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.
*   **[[deepseek_r1_model_features | DeepSeek R1]] Performance**:
    *   Produced a significantly better-looking UI for the chess board <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>.
    *   Also failed to enforce chess rules, allowing pieces to move anywhere, similar to 03 mini in terms of functionality <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.
*   **Final Test Findings**: [[deepseek_r1_model_features | DeepSeek R1]] again excelled in UI, but 03 mini had a slight edge in attempting to handle illegal moves (even if imperfectly), and [[speed_and_performance_comparison_with_other_llms | speed]] was still with 03 mini <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

## Conclusion
Both [[deepseek_r1_model_features | DeepSeek R1]] and 03 mini are incredible models with distinct strengths and weaknesses.
*   **03 Mini**: Generally superior in [[speed_and_performance_comparison_with_other_llms | speed]] and raw functionality <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. It might require more iterations to get to a working state but handles some functional aspects better.
*   **[[deepseek_r1_model_features | DeepSeek R1]]**: Excels in UI/UX and seems better at understanding user intent and providing more feature-rich outputs, even if it sometimes struggles with correct functional implementation <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

There appears to be an opportunity to use these two LLMs together, potentially leveraging 03 mini for core functionality and [[deepseek_r1_model_features | DeepSeek R1]] for enhanced UI and feature generation <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.