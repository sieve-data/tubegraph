---
title: Overview of OpenAIs o1 Model
videoId: MhlNfCIDToo
---

From: [[everyinc]] <br/> 

OpenAI has released its new o1 model, available to users through the ChatGPT model selector <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

## o1 Model Variants

The o1 model comes in two versions:

*   **o1 preview**
    *   Smarter and slower <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
    *   Possesses more knowledge of the world <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a>, making it suitable for questions requiring general knowledge <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.
*   **o1 mini**
    *   Faster, but with less world knowledge <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>.
    *   Excels at math and coding problems, having achieved an 800 on SAT Math <a class="yt-timestamp" data-t="00:00:27">[00:00:27]</a>.
    *   Despite its mathematical prowess, it has not "read Shakespeare" <a class="yt-timestamp" data-t="00:00:29">[00:00:29]</a>.
    *   Recommended for reasoning-specific problems <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## [[Chain of Thought Reasoning in AI Models | Chain of Thought Reasoning]]

The primary differentiator for o1 is its native implementation of [[Chain of Thought Reasoning in AI Models | Chain of Thought reasoning]] <a class="yt-timestamp" data-t="00:01:22">[00:01:22]</a>.

### How it Works

When posed with a complex problem, o1 displays "thinking" and provides a summary of its thought process, such as "presenting a proof," "observing even numbers," or "revisiting ancient beliefs" <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. This visible thought process precedes the final answer, providing a detailed and accurate solution, for example, proving the square root of two is irrational and explaining its historical impact <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

### Evolution of [[Chain of Thought Reasoning in AI Models | Chain of Thought]]

[[Chain of Thought Reasoning in AI Models | Chain of Thought reasoning]] is a concept that has existed prior to o1, observed in original GPT models <a class="yt-timestamp" data-t="00:01:27">[00:01:27]</a>. Previously, asking a GPT model to "think step by step" or "think out loud" would improve its accuracy and reduce hallucinations <a class="yt-timestamp" data-t="00:01:32">[00:01:32]</a>. This is because GPT models tend to "intuitively blurt out" answers without internal processing; they "think by writing" <a class="yt-timestamp" data-t="00:01:43">[00:01:43]</a>. Just as performing long division on paper yields better results than doing it purely in one's head, explicit step-by-step thinking improves AI performance <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>.

With o1, this [[Chain of Thought Reasoning in AI Models | Chain of Thought reasoning]] is integrated natively, meaning the model has been trained through reinforcement learning to always engage in this process when responding to a question <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>.

### A New Paradigm for AI Performance

Traditionally, improving AI model performance involved adding more data or increasing computational power <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. However, o1 introduces a new approach: scaling performance by scaling the amount of time the model spends "thinking" during inference (when responding to a prompt) <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. For example, a response might involve 7 seconds of thought <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

## Implications for Users

This new paradigm has significant implications:

*   **Tackling Difficult Problems**: Future models may be able to address much more complex problems by dedicating extended "thinking" time (hours or even days) <a class="yt-timestamp" data-t="00:02:45">[00:02:45]</a>.
*   **New Human Skills**: The ability to [[prompting_techniques_for_o1_model | prompt models]] like o1 effectively may become a crucial skill in an "allocation economy," where compensation is based on the ability to allocate intelligence <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. Users will need to discern when to utilize an expensive, long-running model like o1 <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>.
*   **Cost and Time**: Running o1 can be time-consuming and costly, potentially taking minutes, hours, or days <a class="yt-timestamp" data-t="00:03:26">[00:03:26]</a>. Therefore, users must be adept at formulating prompts that are most likely to succeed and justify the investment <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>.

### [[prompting_techniques_for_o1_model | Prompting Techniques]] for o1

[[prompting_techniques_for_o1_model | Prompting o1]] differs from prompting regular ChatGPT models like GPT-4 <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. OpenAI has observed that o1 performs better with shorter, more direct prompts that get straight to the point <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. Unlike GPT-4, which can handle extensive context without significant degradation, o1 requires users to be more selective about the information provided to keep its [[Chain of Thought Reasoning in AI Models | Chain of Thought]] on track <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.

## Use Cases and Impact

o1 is particularly useful for 10-20% of daily prompts that demand a higher level of reasoning <a class="yt-timestamp" data-t="00:04:07">[00:04:07]</a>. While valuable for individual users, it is expected to be a significant asset for businesses engaged in [[building_applications_with_ai | building with AI]] <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. Businesses often encounter more complex queries requiring extensive reasoning and long processing times <a class="yt-timestamp" data-t="00:04:20">[00:04:20]</a>. For example, Every, a daily tech newsletter, saw a 20% improvement in an internal incubation project through simple use of o1 <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.