---
title: Generative AI and causal reasoning
videoId: gazCIKYEv44
---

From: [[causalpython]] <br/> 

The integration of [[causal_reasoning_in_ai | causal reasoning]] with generative artificial intelligence (AI) is a key area of interest, particularly in addressing limitations and expanding the capabilities of current models <a class="yt-timestamp" data-t="00:51:02">[00:51:02]</a>.

## Challenges in Generative AI

Current generative AI models, such as those used for image generation (e.g., Midjourney, Stable Diffusion), face challenges when users attempt to make specific, semantically meaningful edits <a class="yt-timestamp" data-t="00:51:02">[00:51:02]</a>. For instance, if an image is generated, and a user wants to change the color of glasses from blue to red, the model often produces unexpected artifacts or alters other parts of the image that should remain constant <a class="yt-timestamp" data-t="00:51:52">[00:51:52]</a>. This happens because the model struggles with counterfactual questions, where the desire is to change only one specific aspect without affecting causally independent elements <a class="yt-timestamp" data-t="00:51:43">[00:51:43]</a>.

Unlike text-based generative models like ChatGPT, where users can easily edit generated text, images lack this semantic control <a class="yt-timestamp" data-t="00:53:31">[00:53:31]</a>. The inability to operate on a semantic level, rather than just the form of the artifact, highlights a gap in current generative AI capabilities <a class="yt-timestamp" data-t="00:53:51">[00:53:51]</a>.

## The Role of Causal Reasoning

[[Causality in AI | Causal abstractions]] and [[causal_reasoning_in_ai | causal reasoning]] can significantly improve generative AI by allowing for more precise and controllable modifications <a class="yt-timestamp" data-t="00:54:11">[00:54:11]</a>. If models could operate semantically on [[causal_reasoning_in_ai | causal representations]] embedded within the generated content, it would enable users to adjust specific attributes (e.g., changing a baseball hat to a pirate hat) without unintended side effects like altered ears or background artifacts <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>. This would provide "knobs" for users to make targeted adjustments, augmenting their creative process <a class="yt-timestamp" data-t="01:01:58">[01:01:58]</a>.

### Large Language Models and Causal Understanding

The concept of Large Language Models (LLMs) learning a "world model" essentially refers to their ability to learn a [[causality_in_ai | causal model]] of the world <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. While LLMs can answer [[causal_reasoning_in_ai | causal questions]] empirically (e.g., "Does smoking cause cancer?" or generating Python code for causal analysis), they are prone to "hallucinations," or generating information that appears true but is incorrect <a class="yt-timestamp" data-t="00:57:13">[00:57:13]</a>.

The [[causal_reasoning_in_ai | Causal Hierarchy Theorem]] (also known as Pearl's Causal Ladder) is relevant here, distinguishing between different levels of [[causal_reasoning_in_ai | causal reasoning]]:
*   **Level 1: Associational** - Based on observational statistics <a class="yt-timestamp" data-t="00:56:06">[00:56:06]</a>.
*   **Level 2: Interventional** - Understanding cause and effect through interventions <a class="yt-timestamp" data-t="00:56:08">[00:56:08]</a>.
*   **Level 3: Counterfactual** - Reasoning about hypothetical scenarios ("what if things had been different?") <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>.

To reliably answer questions at higher levels of this hierarchy, models need assumptions at the corresponding level. For instance, counterfactual questions require Level 3 assumptions, often in the form of a structural [[causality_in_ai | causal model]] <a class="yt-timestamp" data-t="00:56:42">[00:56:42]</a>. The challenge is determining if these necessary assumptions exist within the LLM's architecture or learned parameters, or if they are only present in the prompt <a class="yt-timestamp" data-t="00:58:40">[00:58:40]</a>.

One approach to reducing hallucinations and improving the reliability of LLMs in answering [[causal_reasoning_in_ai | causal questions]] is to incorporate [[causality_in_ai | causal information]] directly into the Transformer architecture itself <a class="yt-timestamp" data-t="01:00:08">[01:00:08]</a>. This would provide theoretical guarantees, similar to those achieved with latent variable models using the do-calculus <a class="yt-timestamp" data-t="01:00:23">[01:00:23]</a>.

## [[The future of AI integrating generative AI and causal AI | The Future of AI Integrating Generative AI and Causal AI]]

There is a growing emphasis on leveraging deeper structural information, including [[causality_in_ai | causal]] and hierarchical structures, rather than just scaling models with ever-larger datasets <a class="yt-timestamp" data-t="01:03:13">[01:03:13]</a>. This shift aims to improve model efficiency and capabilities with smaller datasets, opening up new possibilities. For example, in code generation, incorporating knowledge about repository history and commit messages could provide a richer, more structured understanding than just feeding individual code documents <a class="yt-timestamp" data-t="01:04:18">[01:04:18]</a>. This approach of leveraging "depth" in information, as opposed to just "breadth" of data, is seen as a promising direction for future AI development <a class="yt-timestamp" data-t="01:05:17">[01:05:17]</a>.