---
title: Overview of OpenAIs o1 model
videoId: 6xlPJiNpCVw
---

From: [[fireship]] <br/> 

OpenAI recently unveiled `o1` (pronounced "O-one"), a new state-of-the-art model that represents a significant leap in deep thinking and reasoning capabilities <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. Despite initial skepticism about the AI bubble bursting, `o1` has redefined benchmarks in areas like math, coding, and PhD-level science <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Sam Altman, CEO of [[open_source_advancements_in_ai_model_technology | OpenAI]], indicated that the company is "always two steps ahead" <a class="yt-timestamp" data-t="00:00:28">[00:00:28]</a>.

## What is o1?

`o1` is not just another iteration like GPT-5, nor is it considered AGI (Artificial General Intelligence) or ASI (Artificial Super Intelligence) <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. It was released ahead of schedule <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>. While "GPT" stands for Generative Pre-trained Transformer, the "O" in `o1` is humorously suggested to stand for "oh we're all going to die" <a class="yt-timestamp" data-t="00:01:05">[00:01:05]</a>.

### Key Capabilities and Benchmarks

[[comparison_between_o1_and_previous_openai_models | Compared to GPT-4]], `o1` shows massive accuracy gains, particularly in:
*   **PhD-level physics** <a class="yt-timestamp" data-t="00:01:16">[00:01:16]</a>
*   **Math and formal logic** on the massive multitask language understanding benchmarks <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>
*   **Coding ability** <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>:
    *   In the International Olympiad in Informatics, `o1` scored in the 49th percentile with 50 submissions per problem, and achieved a gold medal submission when allowed 10,000 submissions <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>.
    *   Its CodeForce ELO rating jumped from the 11th percentile (GPT-4) to the 93rd percentile <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.

[[open_source_advancements_in_ai_model_technology | OpenAI]] has also been working with Cognition Labs, the company behind the AI agent "Devin" <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. When paired with GPT-4, Devin solved 25% of problems, but with `o1`, this success rate soared to 75% <a class="yt-timestamp" data-t="00:01:50">[00:01:50]</a>. These impressive internal benchmarks from a VC-funded company aiming to raise more money are subject to scrutiny <a class="yt-timestamp" data-t="00:01:58">[00:01:58]</a>.

### Availability and Pricing

Three new `o1` models were released: `o1` mini, `o1` preview, and `o1` regular <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Only `o1` mini and `o1` preview are generally accessible, with `o1` regular still locked away, possibly requiring a $2,000 Premium Plus plan for access <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## How o1 Works: Deep Thinking and Reasoning

The core innovation in `o1` models is their reliance on **reinforcement learning** to perform complex reasoning <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. This means that when `o1` is presented with a problem, it produces a **chain of thought** before presenting the final answer <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>.

Much like a human, `o1` goes through a series of thoughts to reach a conclusion <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. In this process, it generates "reasoning tokens" which are internal outputs that help the model refine its steps and backtrack when necessary <a class="yt-timestamp" data-t="00:02:56">[00:02:56]</a>. This approach allows `o1` to produce complex solutions with fewer hallucinations compared to previous models <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

However, this deeper reasoning requires more time, computing power, and cost <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>. The actual chain of thought is hidden from the end-user, though users pay for these reasoning tokens at a rate of $60 per 1 million tokens <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>. Examples provided by [[open_source_advancements_in_ai_model_technology | OpenAI]] show `o1` creating a playable Snake game in a single shot <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>, a nonogram puzzle <a class="yt-timestamp" data-t="00:03:15">[00:03:15]</a>, and transposing a matrix in bash by first analyzing input/output shapes and programming language constraints <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>.

The concept of using reinforcement learning to dominate math and coding competitions by producing synthetic data is not entirely new; [[Google Open Source AI models | Google]] has been doing this with AlphaProof and AlphaCoder for years <a class="yt-timestamp" data-t="00:03:48">[00:03:48]</a>. However, `o1` is the first time such a model has become generally available to the public <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>.

## Real-World Testing and Limitations

In a practical test, `o1` was prompted to build the classic MS-DOS game "Drug Wars" with a GUI in C, a task that took a human approximately 100 hours to complete <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>. When GPT-4 was given the same prompt, it produced code that nearly worked but struggled to compile and had limited game logic even after follow-up prompts <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.

`o1`, in contrast, compiled immediately and seemingly followed all game requirements <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>. However, upon closer inspection, the application was found to be quite buggy, featuring infinite loops and a terrible UI <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Further attempts to fix these issues with additional prompts actually led to more hallucinations and bugs <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>. This demonstrated that `o1` is not truly intelligent <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.

## Conclusion

While there is "huge potential" in the chain of thought approach utilized by `o1` <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>, its capabilities might be overstated <a class="yt-timestamp" data-t="00:05:15">[00:05:15]</a>. Ultimately, `o1` is seen as another benign AI tool, functioning much like GPT-4 but with the added ability to recursively prompt itself <a class="yt-timestamp" data-t="00:05:27">[00:05:27]</a>. It is not considered fundamentally game-changing <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.