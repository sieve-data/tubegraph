---
title: Current limitations of AI in multistep reasoning and creativity
videoId: Z5dompWURVo
---

From: [[jimruttshow8596]] <br/> 

Current Large Language Models (LLMs), which are primarily Transformer Nets trained to predict the next token in a sequence and then tuned for specific functions <a class="yt-timestamp" data-t="00:04:38">[00:04:38]</a>, are not expected to achieve full human-level [[possibilities_for_achieving_humanlevel_agi | Artificial General Intelligence]] (AGI) on their own <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>. While they can perform many amazing and useful functions and might even pass the Turing Test <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>, their architecture presents fundamental challenges to advanced reasoning and creativity <a class="yt-timestamp" data-t="00:32:12">[00:32:12]</a>.

## Hallucination Problem

A notable limitation of LLMs is their tendency to "hallucinate" <a class="yt-timestamp" data-t="00:09:32">[00:09:32]</a>. This means they can generate factually incorrect information or make up non-existent papers and entities <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. While external probes and techniques, such as running multiple queries and calculating entropy or paraphrasing prompts, can filter out many hallucinations <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>, this does not indicate genuine understanding. Humans avoid hallucinations through a "reality discrimination function" and reflective self-modeling <a class="yt-timestamp" data-t="00:12:12">[00:12:12]</a>, a capability LLMs currently lack <a class="yt-timestamp" data-t="00:12:40">[00:12:40]</a>.

## Limitations in Multistep Reasoning

LLMs struggle with complex multi-step reasoning, which is crucial for tasks like writing original science papers <a class="yt-timestamp" data-t="00:30:04">[00:30:04]</a>.

*   **Scientific and Mathematical Discovery**: Current LLMs are not able to "create Einstein" or invent concepts like quantum gravity or supercomputing <a class="yt-timestamp" data-t="00:31:30">[00:31:30]</a>. They typically do not come up with surprising hypotheses to experts <a class="yt-timestamp" data-t="00:36:19">[00:36:19]</a>. While they can "turn the crank" on advanced mathematics and flesh out theories from initial ideas <a class="yt-timestamp" data-t="00:38:48">[00:38:48]</a>, they cannot yet perform science as well as a master's student or a professional scientist <a class="yt-timestamp" data-t="00:36:46">[00:36:46]</a>. They require an "original seed of an idea from the humans" and curation at multiple stages <a class="yt-timestamp" data-t="00:39:09">[00:39:09]</a>.
*   **Lack of Deep Judgment**: LLMs possess "no deep judgment" <a class="yt-timestamp" data-t="00:39:17">[00:39:17]</a>. They cannot determine if a mathematical definition is "interesting" or a "dead end" <a class="yt-timestamp" data-t="00:40:04">[00:40:04]</a>, a discernment that experienced mathematicians make based on "math aesthetics" <a class="yt-timestamp" data-t="00:40:18">[00:40:18]</a>.

## Limitations in Creativity

The natural state of LLM output is often described as "banal" <a class="yt-timestamp" data-t="00:31:12">[00:31:12]</a>, "derivative, and imitative" <a class="yt-timestamp" data-t="00:33:20">[00:33:20]</a>.

*   **Original Artistic Creativity**: LLMs struggle with original artistic creativity, such as inventing new musical genres <a class="yt-timestamp" data-t="00:30:14">[00:30:14]</a> or creating "incredible new genres of music" <a class="yt-timestamp" data-t="00:29:50">[00:29:50]</a>. While clever prompting can move their output "way outside of its centers" <a class="yt-timestamp" data-t="00:34:36">[00:34:36]</a>, it generally doesn't reach the level of a great creative human <a class="yt-timestamp" data-t="00:34:39">[00:34:39]</a>. For example, while they can generate a decent blues guitar solo <a class="yt-timestamp" data-t="00:35:35">[00:35:35]</a>, they are not comparable to musicians like Jimmy Hendrix or Allan Holdsworth, who invented new chords, scales, and emotionally evocative music <a class="yt-timestamp" data-t="00:35:21">[00:35:21]</a>.

## Architectural Roots of Limitations

These shortcomings are attributed to the fundamental architecture of LLMs:
*   They primarily recognize "surface level patterns" in the data they are fed <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>, creating a "humongous well-weighted well-indexed library of surface level patterns" <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>.
*   There is no clear evidence that they are learning abstractions in the same way humans do <a class="yt-timestamp" data-t="00:32:47">[00:32:47]</a>. Human abstraction is guided by "agentic nature," such as survival and reproduction, leading to the development of heuristics to navigate complex environments <a class="yt-timestamp" data-t="00:42:18">[00:42:18]</a>.
*   LLMs are focused on predicting the next token in a sequence <a class="yt-timestamp" data-t="00:57:11">[00:57:11]</a>. The LLM itself is a program, not a sequence, making it unsuited for "recognizing patterns in itself and recursing" <a class="yt-timestamp" data-t="00:57:17">[00:57:17]</a>.

## [[approaches_to_evolving_ai_architectures | Approaches to Evolving AI Architectures]]

To address these limitations, several [[innovative_approaches_in_ai_research | innovative approaches in AI research]] are being explored:

*   **Increased Recurrence**: Introducing more recurrence into Transformer networks, similar to LSTMs, could help generate more interesting abstractions <a class="yt-timestamp" data-t="00:46:46">[00:46:46]</a>.
*   **Alternative Training Methods**: Exploring methods like predictive coding-based training instead of or in conjunction with backpropagation, especially for highly recurrent networks, is a promising area <a class="yt-timestamp" data-t="00:47:36">[00:47:36]</a>.
*   **Hybrid Architectures**:
    *   Combining LLMs with other systems like AlphaZero (for planning and strategic thinking) <a class="yt-timestamp" data-t="00:48:17">[00:48:17]</a> and neural knowledge graphs <a class="yt-timestamp" data-t="00:48:21">[00:48:21]</a>, where LLMs might serve as an integration hub <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>.
    *   Integrating LLMs as supporting actors within a self-modifying, self-rewriting weighted labeled metagraph, which serves as the central hub for knowledge representation and cognitive operations (e.g., OpenCog Hyperon) <a class="yt-timestamp" data-t="00:55:07">[00:55:07]</a>. This approach focuses on reflection, recognizing patterns in its own mind, and is naturally suited for logical reasoning and evolutionary programming <a class="yt-timestamp" data-t="00:56:54">[00:56:54]</a>.

These directions aim to overcome the inherent [[the_limitations_of_current_ai_architectures | limitations of current AI architectures]] by building systems capable of deeper abstraction, multi-step reasoning, and genuine creativity, moving beyond mere surface pattern recognition <a class="yt-timestamp" data-t="00:32:33">[00:32:33]</a>.