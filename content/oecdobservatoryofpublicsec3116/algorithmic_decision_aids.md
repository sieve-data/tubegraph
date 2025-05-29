---
title: Algorithmic decision aids
videoId: VJES_jPWf70
---

From: [[oecdobservatoryofpublicsec3116]] <br/> 

Professor Olivier Sibony, an expert in strategic thinking and the design of [[decision_making | decision processes]], has presented his work at the intersection of AI and [[Behavioral Insights | behavioral science]] at an OECD [[Behavioral Insights for Public Policy | Behavioral Science Meetup]] <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. His work delves into insights from his book *Noise: A Flaw in Human Judgment*, co-authored with Cass Sunstein and the late Daniel Kahneman <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a>. A key question explored is whether [[AI in decision making | AI]] can reduce flaws in human judgment or merely amplify biases and [[noise_and_variability_in_human_decisions | noise]] <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

## Defining Error: Bias vs. Noise

When discussing [[decision_making | decision-making]], it's crucial to understand two types of errors:
*   **Bias:** A predictable error, where errors consistently land in a similar area, indicating a systemic problem <a class="yt-timestamp" data-t="00:05:00">[00:05:00]</a>. The causes of such errors are often identifiable <a class="yt-timestamp" data-t="00:05:28">[00:05:28]</a>.
*   **Noise:** Random error, where errors are scattered unpredictably <a class="yt-timestamp" data-t="00:05:41">[00:05:41]</a>. There is no clear pattern or explanation for why the errors occur <a class="yt-timestamp" data-t="00:05:55">[00:05:55]</a>.

Many real-world errors are a combination of both bias and [[noise_and_variability_in_human_decisions | noise]] <a class="yt-timestamp" data-t="00:06:09">[00:06:09]</a>. Differentiating between them is important for effective error reduction, especially in [[AI in decision making | AI decision-making]] <a class="yt-timestamp" data-t="00:06:19">[00:06:19]</a>.

## Types of AI and Human Thinking

AI systems can be broadly categorized into two types, which remarkably mirror System 2 and System 1 thinking:

### Symbolic AI (Good Old-Fashioned AI - GOFAI)
*   **Description:** Follows explicit rules, uses symbolic representations, and adheres to logical processes <a class="yt-timestamp" data-t="00:07:20">[00:07:20]</a>.
*   **Analogy:** Similar to System 2 thinking—logical, slower, and generally reliable, providing consistent answers <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>.
*   **Limitations:** Can make "stupid mistakes" when faced with complex or nuanced real-world situations not explicitly covered by its rules <a class="yt-timestamp" data-t="00:07:35">[00:07:35]</a>.

### Machine Learning (Large Language Models - LLMs)
*   **Description:** Learns from data, starting from a blank slate to infer implicit rules or patterns <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>.
*   **Analogy:** Resembles System 1 thinking—associative, free-flowing, capable of complex tasks, but prone to "stupid mistakes" and biases <a class="yt-timestamp" data-t="00:09:25">[00:09:25]</a>.
*   **Limitations:**
    *   **Replicates Human Biases:** LLMs tend to replicate the biases found in the data they are trained on, including cognitive biases like those observed in the bat-and-ball test <a class="yt-timestamp" data-t="00:10:29">[00:10:29]</a>.
    *   **Confabulation:** Can produce "perfectly coherent nonsensical answers" by associating frequently appearing terms, even if the underlying logic is flawed or untrue <a class="yt-timestamp" data-t="00:10:48">[00:10:48]</a>. This is akin to a human "bullshitting" when they don't know the answer <a class="yt-timestamp" data-t="00:11:29">[00:11:29]</a>.
    *   **Lack of Truth Understanding:** LLMs have no inherent understanding of truth; their "best proxy for the truth is the frequency of something coming up as the answer to a question" <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.
    *   **Instability/Noise:** LLM answers can vary when asked the same question, a feature sometimes designed to make them feel "more natural" and human-like <a class="yt-timestamp" data-t="00:12:35">[00:12:35]</a>.

> [!WARNING]
> "You really cannot trust a large language model. This is really a bad tool to make decisions." <a class="yt-timestamp" data-t="00:11:39">[00:11:39]</a>
> "They are not stable and they don't know what the truth is." <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a>

## [[Challenges of trusting AI over human judgment | Challenges of Trusting AI Over Human Judgment]]

The public discourse often equates AI with LLMs, leading to a general distrust of [[AI in decision making | AI]] for decisions <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>. However, if LLMs replicate human flaws, this implies that "never trust an LLM" also leads to the conclusion: "never trust a human being either" <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a>.

Three key problems arise when using [[AI in decision making | AI]] as [[decision_making | decision aids]]:

### 1. Trust and Acceptability
*   **Empirical Evidence:** Decades of meta-analyses comparing human judges to simple formulas (even basic linear regression algorithms from the 1960s-80s) show that "the formula always at least matches the human judge" <a class="yt-timestamp" data-t="00:16:29">[00:16:29]</a>. In personnel selection, for instance, a formula using just three objective facts about a candidate outperforms job interviews <a class="yt-timestamp" data-t="00:17:27">[00:17:27]</a>.
*   **Human Resistance:** Despite this evidence, "people don't want to use them" <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>.
    *   **Reasons for Resistance:**
        *   Overconfidence in personal judgment: Experts often believe they are "better than average" or possess unique insights into qualitative data that algorithms cannot grasp <a class="yt-timestamp" data-t="00:19:59">[00:19:59]</a>.
        *   Lack of feedback: Professionals often don't receive accurate or timely feedback on the quality of their own [[decision_making | decisions]], hindering learning and incentive to improve <a class="yt-timestamp" data-t="00:24:44">[00:24:44]</a>.
        *   Desire for certainty: Humans prefer certainty and fail to acknowledge that any judgment under uncertainty is inherently probabilistic <a class="yt-timestamp" data-t="00:22:57">[00:22:57]</a>.
        *   Loss of control and preference for ambiguity <a class="yt-timestamp" data-t="00:23:42">[00:23:42]</a>.
*   **Overcoming Resistance:**
    *   Allow users to customize algorithms, even slightly, as this increases willingness to use them <a class="yt-timestamp" data-t="00:24:07">[00:24:07]</a>.
    *   Provide direct feedback on human accuracy <a class="yt-timestamp" data-t="00:24:36">[00:24:36]</a>.
    *   Align incentives with accuracy <a class="yt-timestamp" data-t="00:24:37">[00:24:37]</a>.

> [!NOTE] How high should the accuracy bar be for AI?
> "It doesn't have to be perfect, it just has to be better than you." <a class="yt-timestamp" data-t="00:25:43">[00:25:43]</a>

### 2. Humans Should Always Remain in Control
*   **Conventional Wisdom:** There's a near-universal agreement among executives, regulators, and scientists that "humans must stay in control" of [[AI in decision making | AI decision-making]] <a class="yt-timestamp" data-t="00:26:02">[00:26:02]</a>.
*   **The Paradox of Control:** If [[AI in decision making | AI]] is, on average, better than human judgment, its value comes precisely from the cases where the AI is right and the human is wrong <a class="yt-timestamp" data-t="00:27:10">[00:27:10]</a>. Overriding AI when it disagrees with human judgment essentially negates its value and can reinforce confirmation bias <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>.
*   **When to Trust AI:** Once an [[AI in decision making | AI]] model has been quality-controlled (i.e., proven to make better decisions on average, is not illegal, impractical, or biased), it should generally be trusted <a class="yt-timestamp" data-t="00:29:06">[00:29:06]</a>.
*   **The "Broken Leg Problem":** The only exception for overriding an [[AI in decision making | AI]] decision is when the human possesses decisive, case-specific information that the model lacks <a class="yt-timestamp" data-t="00:29:24">[00:29:24]</a>. This is a rare situation, not simply a case of "I know better" <a class="yt-timestamp" data-t="00:29:31">[00:29:31]</a>.

> [!IMPORTANT]
> "If you don't trust the model when it disagrees with you, it's a waste of time." <a class="yt-timestamp" data-t="00:29:19">[00:29:19]</a>
> "Most of the time once you've decided to trust a model you should trust the model on every case unless it's a broken leg." <a class="yt-timestamp" data-t="00:30:07">[00:30:07]</a>

### 3. Algorithmic Biases
*   **The Problem of Definition:** Defining what constitutes "unbiased" is extremely complex and often counter-intuitive <a class="yt-timestamp" data-t="00:33:18">[00:33:18]</a>. Different definitions of fairness or bias (e.g., equal error rates vs. equal risk scores given identical data) can be mathematically mutually exclusive <a class="yt-timestamp" data-t="00:32:31">[00:32:31]</a>.
*   **Reflecting Past Biases:** Algorithms often reflect the biases present in historical data <a class="yt-timestamp" data-t="00:35:33">[00:35:33]</a>. For example, if a company historically hired more men, an [[AI in decision making | AI]] recruiting tool trained on that data might disproportionately suggest male candidates <a class="yt-timestamp" data-t="00:35:37">[00:35:37]</a>.
*   **The "Mirror" Effect:** An algorithm reflecting past biases acts as a "mirror of your past behavior" <a class="yt-timestamp" data-t="00:36:07">[00:36:07]</a>. Scraping such an algorithm without addressing the underlying human biases only hides the truth <a class="yt-timestamp" data-t="00:36:09">[00:36:09]</a>.
*   **Forcing Desired Outcomes:** Attempting to force an algorithm to reflect desired outcomes (e.g., gender balance) that don't align with historical data can lead to absurd or unwanted results (e.g., black Nazis from image generation) <a class="yt-timestamp" data-t="00:34:31">[00:34:31]</a>.
*   **The Need for Clarity:** To program an AI to address bias, organizations need to clearly define their priorities and desired outcomes, which often involves making difficult decisions about societal values (e.g., how many women to hire, what level of risk to accept in bail decisions) <a class="yt-timestamp" data-t="00:39:14">[00:39:14]</a>. Humans often prefer to keep these criteria ambiguous in their own [[decision_making | decision-making]] <a class="yt-timestamp" data-t="00:38:50">[00:38:50]</a>.

## Implications for Users and Regulators

### For Users (Decision-Makers):
1.  **Self-Assessment:** How accurate are your [[decision_making | decisions]] without [[AI in decision making | AI]]? <a class="yt-timestamp" data-t="00:39:38">[00:39:38]</a>
2.  **AI's Potential:** How much better can your decisions be with [[AI in decision making | AI]]? <a class="yt-timestamp" data-t="00:39:41">[00:39:41]</a>
3.  **Defining Priorities:** What specific criteria or priorities will you explicitly tell the [[AI in decision making | AI]] to look for, moving beyond previous ambiguities? <a class="yt-timestamp" data-t="00:39:48">[00:39:48]</a>

### For Regulators:
1.  **Human Decision Quality:** Where should the quality of human [[decision_making | decisions]] be regulated, given that they may not be as good as assumed? <a class="yt-timestamp" data-t="00:40:02">[00:40:02]</a> This question is often overlooked in discussions about regulating AI <a class="yt-timestamp" data-t="00:40:15">[00:40:15]</a>.
2.  **AI Model Validation:** Who will validate the quality and performance of [[AI in decision making | AI]] models, ensuring they are genuinely better than human judgment? <a class="yt-timestamp" data-t="00:40:30">[00:40:30]</a>
3.  **Defining Unacceptable Bias:** What specific characteristics constitute a legally, politically, or socially unacceptable bias in algorithms? <a class="yt-timestamp" data-t="00:41:01">[00:41:01]</a>

## Debate Points

*   **Is noise always bad?** While the presented definition of noise is "unwanted variability," variability can be beneficial in certain contexts <a class="yt-timestamp" data-t="00:43:03">[00:43:03]</a>. This includes:
    *   **Markets:** Disagreement on value drives transactions <a class="yt-timestamp" data-t="00:43:59">[00:43:59]</a>.
    *   **Creativity:** Different approaches lead to solutions, with empirical outcomes determining success <a class="yt-timestamp" data-t="00:44:22">[00:44:22]</a>.
    *   **Matters of Taste:** Where there is no "correct" answer, diversity of preference is natural and not undesirable <a class="yt-timestamp" data-t="00:45:03">[00:45:03]</a>.
    *   However, in judgments where a correct answer exists and two people disagree, at least one must be wrong <a class="yt-timestamp" data-t="00:45:47">[00:45:47]</a>.

*   **Noise Audits:** Methodologies for conducting [[noise_and_variability_in_human_decisions | noise audits]] are detailed in "Appendix A" of the book *Noise*, with ongoing technical research on specific applications <a class="yt-timestamp" data-t="00:46:17">[00:46:17]</a>.

*   **Democratization of AI:** Simple, highly effective [[AI in decision making | AI decision aids]] (like basic algorithms that fit "on the back of an envelope") are already much better than human judgment and are not costly <a class="yt-timestamp" data-t="00:47:51">[00:47:51]</a>. The cost of advanced AI might be a factor for certain applications, but less so for basic decision tools, which often save money by reducing human intervention <a class="yt-timestamp" data-t="00:48:41">[00:48:41]</a>.

*   **AI and Confirmation Bias:** While LLMs, like ChatGPT, can present opposing viewpoints (e.g., "however" clauses), their utility in overcoming confirmation bias depends on the user's mindset <a class="yt-timestamp" data-t="00:49:12">[00:49:12]</a>. For researchers with an open mind, it can be helpful. However, for a decision-maker at the end of their process, their willingness to accept an AI's contradictory advice is the critical factor <a class="yt-timestamp" data-t="00:49:51">[00:49:51]</a>.

*   **Responsibility and Accountability:** Decision-makers are responsible for their [[decision_making | decisions]], and it is in their interest to use [[AI in decision making | AI]] that is more accurate <a class="yt-timestamp" data-t="00:51:18">[00:51:18]</a>. The legal framework needs to evolve to evaluate [[decision_making | decisions]] based on their probabilistic nature and aggregate outcomes, rather than on a case-by-case basis <a class="yt-timestamp" data-t="00:53:02">[00:53:02]</a>. Unlike humans, whose thought processes are opaque, algorithms are by design more transparent and testable, potentially leading to greater accountability <a class="yt-timestamp" data-t="00:53:14">[00:53:14]</a>.

*   **Personal vs. Professional Decisions:** The arguments for using [[AI in decision making | AI]] to improve [[decision_making | decision-making]] primarily apply to *professional judgments* where there is an obligation to stakeholders (e.g., doctors to patients, judges to justice, executives to companies) <a class="yt-timestamp" data-t="00:55:01">[00:55:01]</a>. For *personal decisions* (e.g., choosing a city, buying cheese), the loss of agency and the pleasure of making one's own choices might outweigh the benefits of outsourcing to AI <a class="yt-timestamp" data-t="00:55:04">[00:55:04]</a>.