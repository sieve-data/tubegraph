---
title: Coding capabilities of reasoning llms
videoId: xfFyAumTjT0
---

From: [[colemedin]] <br/> 

The release of DeepSeek R1, an [[opensource_reasoning_llms | open-source reasoning LLM]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, was quickly followed by OpenAI's O3 Mini, their next-generation advanced reasoning model <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. Both are impressive reasoning LLMs, leading to comparisons, particularly in their [[ai_coding_assistants | coding]] abilities <a class="yt-timestamp" data-t="00:00:37">[00:00:37]</a>. This article uses Bolt.DIY, an [[ai_coding_assistant_development | open-source AI coding assistant]] <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>, to compare their performance in building applications.

## Model Overview and Key Differences

While both DeepSeek R1 and O3 Mini are considered reasoning LLMs, they operate with entirely different architectures <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>.
*   **DeepSeek R1**: This model is [[opensource_reasoning_llms | open-source]] <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>. It uses a mixture of experts (MoE) combined with reinforcement learning from human feedback (RLHF) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. R1 is often considered better for more logical, free-thinking tasks like solving logic problems and deep research <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.
*   **OpenAI O3 Mini**: This model is not [[opensource_reasoning_llms | open-source]] <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. It employs a dense Transformer architecture, similar to most OpenAI models <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>. O3 Mini is generally considered better for more directed tasks, often seen in [[understanding_ai_agent_components_and_reasoning_patterns | AI agents]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.

Both models are described as "absolutely incredible" <a class="yt-timestamp" data-t="00:00:59">[00:00:59]</a>. Pricing-wise, DeepSeek R1 (normal version) is generally much more affordable than O3 Mini <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>.

## Comparison Methodology

The comparison utilizes Bolt.DIY, an [[ai_coding_assistants | open-source AI coding assistant]] available at `bolt.DIY` <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. O3 Mini is accessed directly through the OpenAI API, while DeepSeek R1 is accessed via OpenRouter (specifically the Nitro version due to DeepSeek API outages) <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. The tests progress from simple to more complex application builds.

## Coding Test Cases

### 1. Simple To-Do Application

**O3 Mini Performance**:
*   Built the app in approximately 10 seconds <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.
*   Did not run the command to start the site, requiring manual execution (`npm run dev`) <a class="yt-timestamp" data-t="00:06:10">[00:06:10]</a>.
*   Functionality was good, allowing adding, marking off, and deleting tasks <a class="yt-timestamp" data-t="00:06:36">[00:06:36]</a>.
*   Included a minor "background photo is by Unsplash" comment despite no background image <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.

**DeepSeek R1 Performance**:
*   Took longer, about 20-30 seconds <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>.
*   Automatically ran the command to start the site, providing a "true one-shot" experience <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   Produced a more feature-rich application, including a "X of Y complete" counter for tasks that updated in real-time, demonstrating better reasoning about user needs <a class="yt-timestamp" data-t="00:07:45">[00:07:45]</a>.
*   Included a "Your task list is empty and serene" message when no tasks were present <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

**Initial Conclusion (Simple App)**: O3 Mini excelled in speed <a class="yt-timestamp" data-t="00:07:13">[00:07:13]</a>, while R1 showed better functionality and UI, understanding the prompt with more depth <a class="yt-timestamp" data-t="00:07:27">[00:07:27]</a>.

### 2. Complex Chat Front-End for AI Agents

This prompt was more challenging, aiming to create a chat front-end integrating with Superbase for authentication and chat history <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>.

**O3 Mini Performance**:
*   Took multiple attempts to reach a working state, initially showing a starter template and requiring several error fixes <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>. Bolt.DIY's error correction feature (pasting errors for the LLM to fix) was used <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   Successfully logged in and loaded conversation history <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.
*   Could continue conversations and receive responses from an [[understanding_ai_agent_components_and_reasoning_patterns | n8n agent]] <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>.
*   Duplicated the user message in the chat history, a common issue <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.

**DeepSeek R1 Performance**:
*   Took significantly longer than O3 Mini for this complex task <a class="yt-timestamp" data-t="00:13:27">[00:13:27]</a>.
*   Compiled correctly on the first attempt, unlike O3 Mini <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.
*   The UI looked much better than O3 Mini's output <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.
*   Initially failed to load conversations <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>, but worked after further prompts to correct functionality <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.
*   Also had the duplicate user message error <a class="yt-timestamp" data-t="00:14:28">[00:14:28]</a>.

**Conclusion (Complex Detailed App)**: O3 Mini was faster, but required more iterations to achieve a working state <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>. R1 was slower but compiled on the first try and produced a visually superior UI, though both had minor functional glitches like message duplication <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a>.

### 3. Fully Functional Chess Site (Creative Freedom)

This test involved a single-sentence prompt: "Build me a fully functional chess site," allowing for creative freedom <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

**O3 Mini Performance**:
*   Messed up a couple of times, similar to the previous test, starting with a welcome template <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
*   Produced a chessboard that allowed piece movement and captures <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>.
*   Did not properly understand or enforce chess rules (e.g., pawn not moving two spaces on first move, allowing capturing of the king, allowing self-check) <a class="yt-timestamp" data-t="00:16:09">[00:16:09]</a>.

**DeepSeek R1 Performance**:
*   Produced a chessboard with a significantly better UI than O3 Mini <a class="yt-timestamp" data-t="00:17:04">[00:17:04]</a>.
*   Functionality also failed to adhere to chess rules; pieces could move "all over the place" and did not enforce legal moves <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>.

**Conclusion (Complex Creative App)**: R1 consistently delivered a better UI <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>, but both models struggled significantly with implementing complex game logic and adhering to specific rules without explicit guidance <a class="yt-timestamp" data-t="00:17:17">[00:17:17]</a>. O3 Mini had a slight edge in attempting (though imperfectly) to handle illegal moves <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

## Overall Summary

Both DeepSeek R1 and OpenAI O3 Mini are fantastic LLMs for [[using_local_language_models_llm_for_code_generation | code generation]] <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   **O3 Mini**: Excels in speed and raw functionality, though it may require more iterations to fix errors and is better for "directed tasks" <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
*   **DeepSeek R1**: Superior in UI design and its ability to reason about what the user truly wants to build, even with less explicit prompts, though it can be slower and occasionally struggles with correctly implementing complex functionality <a class="yt-timestamp" data-t="00:18:34">[00:18:34]</a>.

There appears to be an opportunity for [[combining_lightweight_models_with_reasoning_llms | combining these two LLMs]] to leverage O3 Mini's functional strengths and R1's UI capabilities and intuitive understanding <a class="yt-timestamp" data-t="00:18:08">[00:18:08]</a>. Bolt.DIY stands out as an effective [[ai_coding_assistants | AI coding assistant]] for facilitating these comparisons, supporting any LLM desired <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.