---
title: Chain of Thought Reasoning in AI Models
videoId: MhlNfCIDToo
---

From: [[everyinc]] <br/> 

OpenAI has introduced new `o1` models, `o1 preview` and `o1 mini`, which natively incorporate **Chain of Thought** (CoT) reasoning, representing a new paradigm for AI performance <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>.

## Introducing the o1 Models
The `o1` models are accessible through ChatGPT's model selector <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>.

*   **`o1 preview`**: This model is smarter and has more knowledge of the world, making it suitable for questions requiring extensive general information. However, it is slower <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>.
*   **`o1 mini`**: This model is faster but possesses less general world knowledge. It excels at math and coding problems, having achieved an 800 on SAT Math, but has not "read Shakespeare" <a class="yt-timestamp" data-t="00:00:21">[00:00:21]</a>. For reasoning-specific problems, `o1 mini` is preferred <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

When `o1` models process a complex query, such as proving that the square root of two is irrational and explaining its historical impact, they display a "thinking" phase <a class="yt-timestamp" data-t="00:00:49">[00:00:49]</a>. Users can observe a summary of the model's thought process, which might include steps like "presenting a proof," "observing even numbers," and "revisiting ancient beliefs" <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. This deliberate thought process allows `o1` to handle complex problems that previous models like GPT-4o might not have answered as effectively <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

## The Mechanism of Chain of Thought Reasoning
Chain of Thought reasoning has been recognized for some time <a class="yt-timestamp" data-t="00:01:25">[00:01:25]</a>. Earlier GPT models showed improved accuracy and reduced hallucinations when prompted to "think about their answer step by step" or "think out loud" <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. This is because GPT models typically "think by writing to you," and externalizing their thought process enhances their reasoning capabilities, similar to how performing long division on paper is more accurate than doing it in one's head <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

The key distinction with `o1` is that it performs Chain of Thought reasoning natively, having been trained through reinforcement learning to always engage in CoT when responding to a question <a class="yt-timestamp" data-t="00:01:59">[00:01:59]</a>.

## A New Paradigm for AI Performance
Historically, improving AI model performance involved adding more data or increasing computational resources <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. However, `o1` introduces a new method: scaling the amount of time the model uses to "think" <a class="yt-timestamp" data-t="00:02:24">[00:02:24]</a>. OpenAI found that increasing the thinking time during inference—when the AI responds to a prompt—directly scales performance <a class="yt-timestamp" data-t="00:02:29">[00:02:29]</a>. For example, a response that took 7 seconds of thought yielded a better outcome <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>.

This implies a future where AI models might not respond immediately, especially for difficult questions, potentially taking hours or even days to return a comprehensive answer <a class="yt-timestamp" data-t="00:02:41">[00:02:41]</a>.

## Implications for Users and the Allocation Economy
The ability of models to tackle significantly more difficult problems implies a shift from a "knowledge economy" (where compensation is based on what one knows) to an "allocation economy" (where compensation depends on the ability to allocate intelligence) <a class="yt-timestamp" data-t="00:02:51">[00:02:51]</a>. In this new economy, the skill of prompting models like `o1` effectively will become crucial <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

Users will need to discern when to employ an expensive, long-running model like `o1` and how to maximize its output, given that its operation can incur significant time and monetary costs <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

### Prompting `o1` Models
Prompting `o1` differs from prompting traditional models like ChatGPT <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a>. OpenAI has discovered that `o1` performs better with shorter, more direct prompts that avoid excessive detail or extraneous information <a class="yt-timestamp" data-t="00:03:43">[00:03:43]</a>. This contrasts with models like GPT-4o, which can handle a lot of context without significant performance degradation <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>. To keep `o1`'s Chain of Thought on track, users must be selective about the information provided <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>.

## Business Applications
While `o1` models are beneficial for individual users requiring high-level reasoning (around 10-20% of daily prompts), the primary beneficiaries are expected to be businesses <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Businesses are more likely to have complex, long-running queries that demand significant reasoning capabilities <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. For example, one internal project saw a 20% improvement simply from integrating `o1` <a class="yt-timestamp" data-t="00:04:26">[00:04:26]</a>.