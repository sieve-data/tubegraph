---
title: Differences in architecture and functionality of AI models
videoId: xfFyAumTjT0
---

From: [[colemedin]] <br/> 

The release of Deep Seek R1, an open-source reasoning Large Language Model (LLM), was quickly followed by OpenAI's O3 Mini, their next-generation advanced reasoning model <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Both are considered very impressive reasoning LLMs <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. A primary method for [[comparison_of_ai_frameworks | comparing these LLMs]] is by testing their coding capabilities using tools like bolt. DIY, an open-source AI coding assistant <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

## Core Distinctions

While both models are exceptional, they possess significant differences that affect their performance and utility <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>.

### Open Source vs. Proprietary

The most immediate difference is that Deep Seek R1 is [[open_source_vs_proprietary_ai_models | open source]], whereas OpenAI O3 Mini is not <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a>.

### Architectural Differences

Despite being in the same category of reasoning LLMs, their underlying architectures vary greatly <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>:
*   **OpenAI O3 Mini**: Utilizes a dense Transformer architecture, similar to most other OpenAI models <a class="yt-timestamp" data-t="00:02:27">[00:02:27]</a>.
*   **Deep Seek R1**: Employs a Mixture of Experts (MoE) architecture combined with reinforcement learning from Human Feedback (RLHF) <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>.

### Functional Strengths

Both models excel in different areas:
*   **OpenAI O3 Mini**: Generally considered better for more directed tasks, often seen in [[understanding_ai_agent_frameworks | AI agents]] <a class="yt-timestamp" data-t="00:01:26">[00:01:26]</a>.
*   **Deep Seek R1**: Considered superior for more logical, free-thinking tasks such as solving logic problems and deep research <a class="yt-timestamp" data-t="00:01:33">[00:01:33]</a>.

## Performance in Coding Tasks

Practical tests using bolt. DIY offer insights into their coding capabilities <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

### Simple Application Development (React with Tailwind To-Do App)

*   **OpenAI O3 Mini**:
    *   **Speed**: Built the app in about 10 seconds <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>, demonstrating faster completion.
    *   **Functionality**: Knocked the task "out of the park" <a class="yt-timestamp" data-t="00:06:23">[00:06:23]</a>, but failed to run the site command automatically, requiring manual intervention <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. The UI was simplistic <a class="yt-timestamp" data-t="00:07:32">[00:07:32]</a>.
*   **Deep Seek R1**:
    *   **Speed**: Took 20 to 30 seconds <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>, slower than O3 Mini.
    *   **Functionality**: Completely succeeded, even running the command to start the site automatically <a class="yt-timestamp" data-t="00:07:15">[00:07:15]</a>. It "reasoned better" about needed features, producing a more comprehensive UI with features like "0 of 2 complete" tasks <a class="yt-timestamp" data-t="00:07:37">[00:07:37]</a>.

### Complex Application Development (AI Agent Chat Front End)

This test involved [[building_and_deploying_custom_ai_front_ends | creating a full chat front end]] for [[understanding_ai_agent_frameworks | AI agents]], integrating with Supabase for authentication and chat history management <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>.

*   **OpenAI O3 Mini**:
    *   **Development Process**: Required several attempts and error corrections to reach a working state <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>, often starting with a default template and mixing up routes <a class="yt-timestamp" data-t="00:11:57">[00:11:57]</a>. bolt. DIY's error-fixing feature was utilized <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
    *   **Functionality**: Achieved a working app, capable of loading conversation history and continuing conversations <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>. A notable issue was the duplication of user messages <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>.
*   **Deep Seek R1**:
    *   **Development Process**: Took significantly longer than O3 Mini <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>, but compiled correctly on the first attempt <a class="yt-timestamp" data-t="00:13:30">[00:13:30]</a>.
    *   **Functionality**: The initial output looked "so so good" <a class="yt-timestamp" data-t="00:14:01">[00:14:01]</a> and "better than O3 Mini" <a class="yt-timestamp" data-t="00:14:04">[00:14:04]</a> in terms of UI. However, it had issues loading previous conversations <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a> and also produced duplicate user messages <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>. It offered more overall functionality <a class="yt-timestamp" data-t="00:14:49">[00:14:49]</a>.

### Complex Request with Simple Prompt (Chess Site)

This test aimed to assess creative freedom and complex reasoning with a single, simple prompt: "Build me a fully functional chess site" <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

*   **OpenAI O3 Mini**:
    *   **Development Process**: Faced similar initial issues, starting with the wrong template <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>.
    *   **Functionality**: Generated a chess board, but it did not fully understand chess rules (e.g., pawn movement, capturing the king, putting oneself in check) <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>. It did, however, attempt to handle illegal moves <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.
*   **Deep Seek R1**:
    *   **Functionality**: Produced a "so much better" UI than O3 Mini's chess board <a class="yt-timestamp" data-t="00:17:07">[00:17:07]</a>. However, its functionality was poor, not following chess rules at all, allowing pieces to move anywhere, and lacking checks for legal moves <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>.

## Conclusion

Both Deep Seek R1 and OpenAI O3 Mini are "fantastic LLMs" <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a> with distinct advantages:

*   **OpenAI O3 Mini**: Generally better for speed and "raw functionality" <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>, particularly in correctly implementing features.
*   **Deep Seek R1**: Excels in UI/UX and in "understanding what you want to build" <a class="yt-timestamp" data-t="00:18:36">[00:18:36]</a>, even if its implementation of complex functionality might be less precise <a class="yt-timestamp" data-t="00:18:39">[00:18:39]</a>.

There may be opportunities to leverage these models together, using O3 Mini for core functionality and R1 for enhanced UI and feature expansion <a class="yt-timestamp" data-t="00:15:08">[00:15:08]</a>.