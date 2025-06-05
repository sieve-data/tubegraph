---
title: Capabilities and limitations of o1 in coding benchmarks
videoId: 6xlPJiNpCVw
---

From: [[fireship]] <br/> 

OpenAI recently unveiled its new state-of-the-art model, O1, which is presented as a significant advancement in deep thinking or reasoning models <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This model reportedly obliterates past benchmarks across math, coding, and PhD-level science <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>. Despite high hopes, O1 is explicitly stated not to be Artificial Super Intelligence (ASI) or Artificial General Intelligence (AGI), nor is it considered GPT-5 <a class="yt-timestamp" data-t="00:00:39">[00:00:39]</a>. While OpenAI maintains a mission of openness, many of the interesting details about O1 remain closed off <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## O1's Performance in Coding Benchmarks

[[Overview of OpenAIs o1 model | O1]] demonstrates impressive gains in various coding benchmarks, particularly when [[comparison_between_o1_and_previous_openai_models | compared to previous OpenAI models]] like GPT-4 <a class="yt-timestamp" data-t="00:01:13">[00:01:13]</a> <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

*   **International Olympiad in Informatics (IOI)**: O1 achieved the 49th percentile when allowed 50 submissions per problem <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Remarkably, it broke the gold medal submission when granted 10,000 submissions <a class="yt-timestamp" data-t="00:01:31">[00:01:31]</a>.
*   **Codeforces ELO**: O1's Codeforces ELO score surged from the 11th percentile (with GPT-4) to the 93rd percentile <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>.
*   **Collaboration with Cognition Labs**: OpenAI has also been collaborating with Cognition Labs, the company behind Devon, an AI aiming to replace programmers <a class="yt-timestamp" data-t="00:01:42">[00:01:42]</a>. While Devon, when utilizing the GPT-4 brain, solved only 25% of problems, its success rate jumped to 75% when using the O1 brain <a class="yt-timestamp" data-t="00:01:48">[00:01:48]</a>.

## How O1 Approaches Problems: "Chain of Thought"

The underlying mechanism that makes [[Overview of OpenAIs o1 model | O1]] special is its reliance on reinforcement learning to perform complex reasoning <a class="yt-timestamp" data-t="00:02:34">[00:02:34]</a>. When presented with a problem, O1 produces a "chain of thought" before delivering the final answer to the user <a class="yt-timestamp" data-t="00:02:39">[00:02:39]</a>. This process involves generating "reasoning tokens," which are like internal outputs that help the model refine its steps and backtrack when necessary <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>. This allows it to produce complex solutions with fewer hallucinations compared to previous models <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>. However, this method requires more time, computing power, and cost <a class="yt-timestamp" data-t="00:03:06">[00:03:06]</a>.

For instance, in a coding example involving transposing a matrix in bash, O1 first analyzes the input/output shapes, considers programming language constraints, and then proceeds through multiple steps before generating the response <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. Although the actual chain of thought is hidden from the end user (who still pays for the tokens) <a class="yt-timestamp" data-t="00:03:27">[00:03:27]</a>, this "thinking" process aims for greater accuracy.

## Practical Coding Test: "Drug Wars" Game

To assess [[Overview of OpenAIs o1 model | O1]]'s real-world coding capabilities, it was tasked with recreating the classic MS-DOS game "Drug Wars" in C with a GUI, a task that took a human approximately 100 hours to build <a class="yt-timestamp" data-t="00:04:05">[00:04:05]</a>.

*   **GPT-4's Attempt**: When GPT-4 was given the same prompt, it produced code that nearly worked but required multiple follow-up prompts to achieve a basic, albeit limited, functional game <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>.
*   **O1's Attempt**: [[Overview of OpenAIs o1 model | O1]], utilizing its "chain of thought" process (generating reasoning tokens), compiled immediately and seemed to follow all game requirements at first glance <a class="yt-timestamp" data-t="00:04:33">[00:04:33]</a> <a class="yt-timestamp" data-t="00:04:47">[00:04:47]</a>.

### Limitations in Practical Application

Despite the initial promise, O1's generated "Drug Wars" game proved to be quite buggy in practice <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Users encountered infinite loops with certain game elements, and the UI was subpar <a class="yt-timestamp" data-t="00:04:58">[00:04:58]</a>. Attempting to fix these issues with further prompts led to more hallucinations and additional bugs <a class="yt-timestamp" data-t="00:05:03">[00:05:03]</a>.

## Conclusion

While [[Overview of OpenAIs o1 model | O1]] represents a significant leap forward in AI capabilities and achieves impressive results on benchmarks, particularly in [[comparison_with_other_ai_models_in_coding | coding competitions]], its practical application still reveals limitations <a class="yt-timestamp" data-t="00:02:04">[00:02:04]</a>. The "chain of thought" approach, which allows for more complex reasoning and fewer hallucinations initially, does not eliminate all bugs or ensure true intelligence in complex software development <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>. Ultimately, O1 is likened to GPT-4 with an enhanced ability to recursively prompt itself, rather than a fundamentally game-changing AI <a class="yt-timestamp" data-t="00:05:29">[00:05:29]</a>.