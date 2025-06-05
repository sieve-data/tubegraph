---
title: Comparison between o1 and previous OpenAI models
videoId: 6xlPJiNpCVw
---

From: [[fireship]] <br/> 

OpenAI's o1 model was released ahead of schedule, surprising many who anticipated models like GPT-5 or Q\* (Qstar Strawberry) <a class="yt-timestamp" data-t="00:01:01">[00:01:01]</a>. The name "O" is humorously suggested to stand for "oh we're all going to die" <a class="yt-timestamp" data-t="00:01:10">[00:01:10]</a>. This model represents a new paradigm of deep thinking or reasoning, departing from previous basic GPT iterations <a class="yt-timestamp" data-t="00:00:15">[00:00:15]</a>.

## Key Characteristics of o1

While initially causing widespread concern about its potential impact on jobs, o1 is not considered ASI, AGI, or even good enough to be called GPT-5 <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a> <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. OpenAI has kept details about o1 closed off, despite its mission of openness <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a> <a class="yt-timestamp" data-t="00:00:45">[00:00:45]</a>.

Technically, three new o1 models were released: o1 mini, o1 preview, and o1 regular <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. As of the release, only mini and preview are accessible to the general public, with o1 regular potentially available via a $2,000 Premium Plus plan <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a> <a class="yt-timestamp" data-t="00:02:30">[00:02:30]</a>.

## Architectural Differences and Reasoning Capabilities

A core feature distinguishing o1 models is their reliance on reinforcement learning to perform complex reasoning <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a> <a class="yt-timestamp" data-t="00:02:35">[00:02:35]</a>. This means o1 models produce a "chain of thought" before providing an answer to the user, effectively "thinking" through the problem <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a> <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>.

This process involves generating "reasoning tokens," which are like intermediate outputs that help the model refine its steps and backtrack when necessary <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a> <a class="yt-timestamp" data-t="00:02:58">[00:02:58]</a>. This method allows o1 to produce complex solutions with fewer hallucinations compared to previous models <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. However, the trade-off is that responses require more time, computing power, and cost <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

While the "chain of thought" is hidden from the end user, these reasoning tokens are still factored into the cost at $60 per 1 million tokens <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a> <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. This concept of reinforcement learning for complex problem-solving isn't entirely new; Google has used similar approaches with AlphaProof and AlphaCoder for years, but o1 is the first time such a model has become generally available to the public <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a> <a class="yt-timestamp" data-t="00:03:59">[00:03:59]</a>.

## Performance [[comparison_of_ai_models_costs_and_effectiveness | Comparisons]] with GPT-4

o1 demonstrates significant gains in accuracy compared to [[Overview of OpenAIs o1 model | GPT-4]], particularly in:

*   **PhD-level physics** <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>.
*   **Massive Multitask Language Understanding (MMLU) benchmarks** for Math and formal logic <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>.

The most notable improvements are seen in its coding ability:

*   **International Olympiad in Informatics (IOI)**: GPT-4 was in the 49th percentile with 50 submissions per problem, while o1 achieved a gold medal submission when allowed 10,000 submissions <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a> <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Codeforces ELO**: o1's ELO score jumped from GPT-4's 11th percentile to the 93rd percentile <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

o1 has also shown remarkable improvement in collaboration with Cognition Labs' Devon:

*   When using a [[Overview of OpenAIs o1 model | GPT-4]] "brain," only 25% of problems were solved <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.
*   With o1, the problem-solving rate increased to 75% <a class="yt-timestamp" data-t="00:01:53">[00:01:53]</a>.

### Practical Application: Game Development

A practical test involved recreating the MS-DOS game "Drug Wars" with a GUI in C:

*   [[Overview of OpenAIs o1 model | GPT-4]] produced code that almost worked, but required several follow-up prompts to compile, and the game logic remained limited <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a> <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a> <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
*   o1, after going through its "chain of thought," compiled immediately and initially appeared to follow all game requirements <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a> <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a> <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. However, the resulting application was buggy, including an infinite loop with a specific character and a terrible UI <a class="yt-timestamp" data-t="00:04:54">[00:04:54]</a>. Further prompts to fix these issues led to more hallucinations and bugs <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.

## Conclusion

Despite its impressive benchmark improvements and the "chain of thought" approach, o1 is not considered truly intelligent <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>. It is fundamentally described as [[Overview of OpenAIs o1 model | GPT-4]] with the added ability to recursively prompt itself, rather than a fundamentally game-changing advancement <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a> <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.