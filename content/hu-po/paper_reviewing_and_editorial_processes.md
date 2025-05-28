---
title: Paper reviewing and editorial processes
videoId: VgA02gmAgdA
---

From: [[hu-po]] <br/> 

The "AI Scientist" framework, an automated system for scientific discovery, incorporates a simulated review process as a crucial final step in its comprehensive workflow <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. This process mimics the peer review system in machine learning research, but it is entirely handled by Large Language Models (LLMs) <a class="yt-timestamp" data-t="00:07:21">[00:07:21]</a>.

## The AI Scientist's Review Process

The AI Scientist framework leverages LLMs throughout the entire scientific process, from generating novel research ideas and writing code to executing experiments, visualizing results, and finally, describing findings in a full scientific paper <a class="yt-timestamp" data-t="00:07:06">[00:07:06]</a>. This includes a simulated review process for evaluation <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>.

Key aspects of the AI-driven review process include:
*   **Idea Scoring and Archiving** The LLMs generate many potential ideas, then filter them, with a "novelty check" against existing papers via Semantic Scholar <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. This involves looking at ideas and similar concepts to make selections <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.
*   **Self-Reflection and Refinement** While LLMs can produce verbose and repetitive text, the system performs a final round of self-reflection section by section to summarize and filter down content <a class="yt-timestamp" data-t="00:28:51">[00:28:51]</a>. LLMs like GPT-4o and Claude have explicit system prompts to prevent overly verbose styles <a class="yt-timestamp" data-t="00:29:05">[00:29:05]</a>.
*   **LLM Reviewer Agent** A GPT-4 based agent conducts paper reviews based on criteria similar to NeurIPS (formerly NIPS) conferences <a class="yt-timestamp" data-t="00:29:32">[00:29:32]</a>. This agent assigns numerical scores for soundness, presentation, contribution, overall confidence, and lists weaknesses and strengths, concluding with a preliminary binary decision (accept/reject) <a class="yt-timestamp" data-t="00:31:27">[00:31:27]</a>.

## Evaluation and Performance of AI Reviewers

To evaluate the automated reviewer, it was given 500 ICLR 2022 papers with "ground truth" review data from the publicly available OpenReview dataset <a class="yt-timestamp" data-t="00:31:52">[00:31:52]</a>.
*   The automated reviewer achieved "superhuman F1 scores and human-level AUC (Area Under the Curve)" <a class="yt-timestamp" data-t="00:32:32">[00:32:32]</a>.
*   It rejects fewer high-quality papers (lower false negative rate) but has a higher false positive rate, indicating room for improvement <a class="yt-timestamp" data-t="00:33:28">[00:33:28]</a>.
*   Adding "tricks" like Chain of Thought, self-reflection, and ensembling (where multiple outputs are generated and reflected upon to pick the best one) improves the accuracy of LLM reviewer decisions <a class="yt-timestamp" data-t="00:36:21">[00:36:21]</a>, <a class="yt-timestamp" data-t="00:37:11">[00:37:11]</a>. For example, GPT-4o with five rounds of self-reflection and five ensembled reviews performed best within a limited compute budget <a class="yt-timestamp" data-t="00:37:11">[00:37:11]</a>.

## Challenges and Limitations

Despite the advancements, several challenges remain:
*   **Truthfulness and Hallucination**: AI-generated papers may contain factual inaccuracies, such as claiming to use specific GPUs (V100) when different ones (H100) were actually used, or guessing software versions (PyTorch) <a class="yt-timestamp" data-t="00:45:51">[00:45:51]</a>. This impacts reproducibility <a class="yt-timestamp" data-t="00:46:28">[00:46:28]</a>.
*   **Bias in Reporting**: AI-generated papers tend to put a "positive spin" even on negative results, mirroring human tendencies to highlight favorable outcomes <a class="yt-timestamp" data-t="00:46:42">[00:46:42]</a>.
*   **Difficulty in Verification**: Identifying shortcomings in AI-generated papers often requires domain knowledge <a class="yt-timestamp" data-t="00:47:42">[00:47:42]</a>. As models become more advanced (e.g., GPT-50, GPT-60), humans may struggle to understand and evaluate their ideas, raising concerns about "super alignment" <a class="yt-timestamp" data-t="00:48:41">[00:48:41]</a>, <a class="yt-timestamp" data-t="00:49:01">[00:49:01]</a>.
*   **[[Data Curation and Model Evaluation in AI | Data Contamination]]**: There's a possibility that LLMs like GPT-4o and Sonnet were trained on the OpenReview database, meaning their "reviews" might be based on memorized data rather than independent evaluation <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. While preliminary analysis suggests LLMs don't reproduce old reviews exactly, it doesn't definitively prove they haven't memorized portions of the data <a class="yt-timestamp" data-t="01:01:21">[01:01:21]</a>.

### Ethical Concerns
The ethical implications of AI in scientific publishing are significant. The paper suggests that "papers and reviews that are substantially AI-generated must be marked as such for full transparency" <a class="yt-timestamp" data-t="01:10:01">[01:10:01]</a>.

## Future Implications

The development of automated paper reviewing raises fundamental questions about the future of scientific research and publishing:
*   **Changing Format of Papers**: If AI takes over publishing and review, the traditional paper format, optimized for human readability, may become obsolete <a class="yt-timestamp" data-t="01:10:51">[01:10:51]</a>. A new format, optimized for AI, could emerge <a class="yt-timestamp" data-t="01:11:32">[01:11:32]</a>.
*   **Cost Dynamics**: The bulk of the cost for running the AI Scientist is currently associated with LLM API calls for coding and paper writing, rather than the compute required for running experiments on GPUs <a class="yt-timestamp" data-t="01:11:45">[01:11:45]</a>. This highlights the value placed on AI-driven cognitive tasks.
*   **The [[impacts_of_ai_on_human_roles_in_scientific_research | Role of Human Scientists]]**: While the paper suggests human scientists will "move up the food chain" and their role will change, it is debated whether humans will retain a significant purpose in a world where AI systems surpass human intelligence in scientific discovery <a class="yt-timestamp" data-t="01:15:21">[01:15:21]</a>, <a class="yt-timestamp" data-t="01:24:43">[01:24:43]</a>. The increasing automation and complexity of AI research may lead to a future where human contribution to scientific progress is minimal or non-existent <a class="yt-timestamp" data-t="01:18:32">[01:18:32]</a>.

This shift means that the value of traditional paper writing may decrease over time, potentially leading to an increase in industry focus on applications rather than fundamental research <a class="yt-timestamp" data-t="01:20:54">[01:20:54]</a>. The "golden era" of papers, arguably the 2010s, may already be in the past as AI systems take over more of the research process <a class="yt-timestamp" data-t="01:21:34">[01:21:34]</a>.