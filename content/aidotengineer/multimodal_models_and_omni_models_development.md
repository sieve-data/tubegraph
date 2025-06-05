---
title: Multimodal models and omni models development
videoId: b0xlsQ_6wUQ
---

From: [[aidotengineer]] <br/> 

Wen aims to develop a generalist model and agent, utilizing a series of large language models and large [[multimodal_ai_and_the_future_of_human_interaction | multimodal models]] <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## Current Multimodal Capabilities

Wen's chat interface, `chat.wen.ai`, allows users to interact with the latest models, including [[multimodal_ai_and_the_future_of_human_interaction | multimodal models]] that support image and video uploads <a class="yt-timestamp" data-t="00:00:46">[00:00:46]</a>. Users can also engage with their "omni models" via voice and video chat <a class="yt-timestamp" data-t="00:00:50">[00:00:50]</a>.

The development of [[multimodal_ai_and_the_future_of_human_interaction | multimodal models]] has primarily focused on vision-language models <a class="yt-timestamp" data-t="01:37:37">[01:37:37]</a>.

### Wen 2.5 VL (Vision Language)
Released in January, Wen 2.5 VL demonstrated competitive performance in various vision-language benchmarks, including:
*   Understanding benchmarks like MMU <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>
*   Math benchmark like Math Vista <a class="yt-timestamp" data-t="01:57:02">[01:57:02]</a>
*   General VQA benchmarks <a class="yt-timestamp" data-t="01:57:05">[01:57:05]</a>

Wen has also explored "thinking" capabilities for vision-language models, such as with Wen VQ <a class="yt-timestamp" data-t="01:59:00">[01:59:00]</a>. Similar to language models, a larger "thinking budget" (maximum thinking tokens) for these models leads to better performance in reasoning tasks, particularly mathematics <a class="yt-timestamp" data-t="01:06:08">[01:06:08]</a>.

### Omni Model Development
The ultimate goal for [[multimodal_ai_and_the_future_of_human_interaction | multimodal models]] is to build an "omni model" capable of accepting multiple input modalities and generating multiple output modalities <a class="yt-timestamp" data-t="01:53:08">[01:53:08]</a>.

The current omni model is a 7 billion parameter large language model <a class="yt-timestamp" data-t="01:13:16">[01:13:16]</a>. It possesses the following capabilities:
*   **Input Modalities**: Text, vision (images and videos), and audio <a class="yt-timestamp" data-t="01:18:21">[01:18:21]</a>
*   **Output Modalities**: Text and audio <a class="yt-timestamp" data-t="01:31:28">[01:31:28]</a>
*   **Applications**: Can be used in voice chat, video chat, and text chat <a class="yt-timestamp" data-t="01:44:41">[01:44:41]</a>
*   **Performance**: Achieves state-of-the-art performance in audio tasks for its size <a class="yt-timestamp" data-t="01:49:49">[01:49:49]</a>. Surprisingly, it even outperforms Wen 2.5 VL (7 billion) in vision-language understanding tasks <a class="yt-timestamp" data-t="01:50:57">[01:50:57]</a>.

There is still room for improvement, particularly in recovering performance drops in language and [[multiagentic_systems_in_ai | agent tasks]] <a class="yt-timestamp" data-t="01:26:00">[01:26:00]</a>. This is expected to be addressed by enhancing data quality and training methods <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

## Future Directions for Multimodal and Omni Models

Wen's future plans for [[multimodal_ai_and_the_future_of_human_interaction | multimodal models]] and omni models include:

*   **Scaling Modalities**: Increasing the number of input and output modalities the models can handle <a class="yt-timestamp" data-t="02:25:00">[02:25:00]</a>. This is seen as a way to enhance model capability and productivity <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>. For example, vision language understanding is crucial for developing [[multiagentic_systems_in_ai | GUI agents]] <a class="yt-timestamp" data-t="02:43:00">[02:43:00]</a>.
*   **Unifying Understanding and Generation**: The goal is to integrate understanding and generation capabilities for modalities like images, similar to GPT-4's ability to generate high-quality images <a class="yt-timestamp" data-t="02:07:00">[02:07:00]</a>.
*   **Truly Omni Models**: Future iterations aim for models capable of generating high-quality images and videos, achieving a "truly omni model" status <a class="yt-timestamp" data-t="01:33:00">[01:33:00]</a>.

Wen emphasizes the transition from training models to training [[multiagentic_systems_in_ai | agents]], especially by leveraging reinforcement learning with environment interaction <a class="yt-timestamp" data-t="02:40:00">[02:40:00]</a>. The belief is that the field is currently in an "era of agents" <a class="yt-timestamp" data-t="02:56:00">[02:56:00]</a>.