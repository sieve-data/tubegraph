---
title: OpenAIs new model release and its implications
videoId: ZEi4OTuFa3I
---

From: [[redpointai]] <br/> 

Percy Liang, a leading AI researcher and co-founder of Together AI, provides insights into [[the_evolution_and_impact_of_openais_models | OpenAI's new "O1" model]] and its broader implications for AI development and research. The model signals a significant shift in the field, moving towards more ambitious, long-term AI tasks and agent-based systems <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>.

## Initial Reactions and Paradigm Shift

From a product perspective, Liang initially found O1 to be slow and difficult to use for many desired tasks <a class="yt-timestamp" data-t="00:00:57">[00:00:57]</a>. He even switched back to GPT-4 for certain applications, like writing a React app, because immediate, faster feedback was prioritized over O1's capabilities, highlighting that evaluation is multi-dimensional, considering cost, speed, accuracy, and customizability <a class="yt-timestamp" data-t="00:09:05">[00:09:05]</a>.

However, from a research standpoint, O1 represents a shift towards "test time compute," where models are designed to solve tasks over extended periods (days, weeks, or even months), rather than providing instant prompt-response interactions <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. This direction could enable AI to tackle more ambitious projects, such as inventing new research or developing new drugs <a class="yt-timestamp" data-t="00:02:07">[00:02:07]</a>.

This also marks a return to the concept of AI [[openais_agent_development_tools | agents]], reminiscent of the earlier focus on reinforcement learning <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. In this new paradigm, language model generations are interpreted as actions in a broader space, allowing agents to gain experience and learn from feedback over time in complex tasks <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Performance and Evaluation Challenges

O1 demonstrates incredible ability in specific domains like math and coding, where reasoning chains are crucial and better supervision can be applied <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>, <a class="yt-timestamp" data-t="00:09:48">[00:09:48]</a>. Percy Liang and his team also tested O1 on Sidebench, a "Capture the Flag" cybersecurity benchmark <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>. While O1 improved on subtask performance, it did not show a huge overall bump because it ignored existing agent templates and frameworks, acting like a "normal language model" rather than integrating with the established structure <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. This highlights the importance of compatibility when integrating new AI models into larger systems <a class="yt-timestamp" data-t="00:05:49">[00:05:49]</a>.

The landscape of AI evaluation is complex due to the unknown nature of training data for proprietary models, making it difficult to trust benchmark results <a class="yt-timestamp" data-t="00:30:26">[00:30:26]</a>. As models become more capable, new benchmarks are constantly needed <a class="yt-timestamp" data-t="00:31:10">[00:31:10]</a>. Liang suggests that AI models themselves can be used to generate benchmarks, such as in their "Auto Bencher" paper, to create more challenging and diverse inputs <a class="yt-timestamp" data-t="00:32:13">[00:32:13]</a>. He advocates for the use of rubrics in evaluation to provide concrete, anchored judgments, similar to grading exams <a class="yt-timestamp" data-t="00:33:35">[00:33:35]</a>.

## Implications for AI Development and Research

### Shift in Scaffolding and Debugging
[[Open source models versus proprietary AI models | The internalization of reasoning within O1]] means that the current "scaffolding" of chaining prompts, commonly used with models like GPT-4, may become dispensable <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. While this can lead to more powerful models, it also makes debugging difficult because the internal trace of the model's operations is not exposed to the user <a class="yt-timestamp" data-t="00:07:02">[00:07:02]</a>. This lack of transparency, while potentially a competitive advantage for [[pros_and_cons_of_building_proprietary_ai_models | proprietary models]], limits a developer's ability to customize and debug applications, especially for novel use cases <a class="yt-timestamp" data-t="00:07:49">[00:07:49]</a>.

### Impact on Inference Market
The "test time compute" paradigm of O1 has significant implications for the inference market. Liang views inference as a fundamental, low-level building block that needs to be robust and affordable <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a>. This shift allows for opportunities to optimize inference for specific use cases, such as high-throughput settings that require generating numerous possibilities for agentic workflows <a class="yt-timestamp" data-t="00:45:56">[00:45:56]</a>.

### Qualitative Changes and Future Milestones
Liang believes that [[the_future_of_ai_models_and_open_source_development | AI capabilities are still moving rapidly]], with O1 representing a "qualitative change" in how these systems might be used <a class="yt-timestamp" data-t="00:49:50">[00:49:50]</a>. He suggests that meaningful milestones for AI include solving open math problems or discovering new insights that extend human knowledge, moving beyond merely mimicking expert human behavior <a class="yt-timestamp" data-t="00:48:22">[00:48:22]</a>. He anticipates that AI will be able to contribute novel insights in fields like ML research within the next few years <a class="yt-timestamp" data-t="00:58:33">[00:58:33]</a>.

## Broader Ecosystem and Regulation
Liang emphasizes that [[the_evolution_and_impact_of_openais_models | thinking about AI's role must be holistic]], extending beyond just the model to the larger ecosystem of actors with varying incentives <a class="yt-timestamp" data-t="00:15:14">[00:15:14]</a>. He advocates for regulations that prioritize transparency and disclosure, enabling policymakers, researchers, and third-party auditors to understand AI's risks and benefits <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>. He believes that regulation should focus on transparency and obligations for downstream decision-makers to understand the AI's outputs, much like nutrition labels on food <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>.

Liang considers [[open_source_ai_models_and_limitations | "agents" to be both overhyped and underhyped]] <a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>. While the concept has seen a full hype cycle, the potential of agents remains significant, especially in areas like scientific discovery and improving researcher productivity, which he feels are currently underexplored application areas <a class="yt-timestamp" data-t="00:59:06">[00:59:06]</a>.