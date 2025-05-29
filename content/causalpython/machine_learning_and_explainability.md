---
title: Machine Learning and Explainability
videoId: gmFWhAAeBfE
---

From: [[causalpython]] <br/> 

Traditional machine learning (ML) models, while powerful for prediction, often face challenges in providing clear explanations and actionable business recommendations. This limitation leads to a "trust deficit" with stakeholders and business experts, who require more than just accurate predictions; they need to understand *why* something happened and *what* actions to take <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This article explores the challenges of explainability in traditional ML and how [[Causal AI and machine learning | causal AI]] addresses these issues.

## The Need for Explainability and Actionable Insights

Many traditional [[Machine learning and causality | machine learning]] models operate as "blackbox" systems <a class="yt-timestamp" data-t="00:03:57">[00:03:57]</a>. While they excel at making predictions, they often fail to provide the underlying reasons for those predictions <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>. This gap is significant in corporate settings where data scientists report to management responsible for major decisions <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>. Managers frequently ask:
*   "Explain me the model" <a class="yt-timestamp" data-t="00:10:12">[00:10:12]</a>
*   "What exactly caused something?" <a class="yt-timestamp" data-t="00:09:13">[00:09:13]</a>
*   "Tell me the next step" <a class="yt-timestamp" data-t="00:09:15">[00:09:15]</a>

Data scientists often struggle to answer these questions using conventional methods. Explaining models through accuracy scores, root mean square errors, or post-hoc [[Explainable AI and Feature Importance | explainability methods]] like LIME and SHAP, frequently leads to stakeholders losing interest or not trusting the models <a class="yt-timestamp" data-t="00:09:29">[00:09:29]</a>. The fundamental issue is that these methods provide "mere predictions and not business recommendations" <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>, limiting their direct utility for decision-making.

## [[Causal AI and machine learning | Causal AI]] as a Solution for Explainability

[[Causal AI and machine learning | Causal machine learning]] directly addresses the explainability gap by focusing on cause-and-effect relationships <a class="yt-timestamp" data-t="00:04:27">[00:04:27]</a>. Its benefits include:
*   **Enhanced Explainability:** [[Causal AI and machine learning | Causal models]] are inherently more explainable due to [[Explainable AI and Feature Importance | causal discovery graphs]] <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. These graphs visually represent relationships, allowing stakeholders to see how actions can lead to specific effects <a class="yt-timestamp" data-t="00:25:04">[00:25:04]</a>.
*   **Business Recommendations:** Beyond predictions, [[Causal AI and machine learning | causal models]] provide actionable business recommendations <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.
*   **"What If" and [[Counterfactual Explanations and Model Explainability | Counterfactual Scenarios]]:** The ability to run simulations and "what if" scenarios (also known as [[Counterfactual Explanations and Model Explainability | counterfactual scenarios]]) builds trust with management <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>, allowing them to test different interventions and understand potential outcomes <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.
*   **Trust Building:** By integrating expert knowledge directly into the models, [[Causal AI and machine learning | causal models]] become an "extension of their own brain" for stakeholders <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>. This fosters trust and encourages engagement, leading to continuous model improvement <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.

## The Role of Human Expertise

Human experts play a crucial role in [[Causal AI and machine learning | causal machine learning]], particularly in the construction and validation of [[Explainable AI and Feature Importance | causal discovery graphs]].

### Interviewing Experts
Gathering "tribal knowledge" from experienced professionals is essential <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Techniques like multi-criteria decision-making methods (e.g., FHP, TOPSIS, Analytic Hierarchy Process) can ensure consistency and reduce human biases during interviews <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. The goal is to collaboratively build a tribal knowledge graph that identifies cause-and-effect relationships within a domain, such as how external factors impact supplier backlogs <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. This process not only gathers information but also "saves" the knowledge of experts, preserving their legacy within the company, even if they retire <a class="yt-timestamp" data-t="00:19:26">[00:19:26]</a>.

### Iterative Model Building
Building [[Causality and Machine Learning | causal models]] often follows an iterative approach <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. Starting with a simplified model and gradually adding complexity, triangulating results with real data, and incorporating more expert knowledge over time is often the most effective strategy <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. This incremental approach builds trust with stakeholders, as they see tangible progress and can validate the model's logic at each stage <a class="yt-timestamp" data-t="00:11:58">[00:11:58]</a>. While models might not be perfect initially, they improve over time as management gains confidence and actively contributes to their refinement <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.

## Leveraging Large Language Models (LLMs) for [[Causal AI and machine learning | Causal Discovery]]

The intersection of large language models (LLMs) and [[Causal AI and machine learning | causal AI]] is an exciting development <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. A significant challenge in [[Causal AI and machine learning | causal discovery]] is the time-consuming process of interviewing experts to gather relationships, sometimes taking 40-50 hours for 25 experts <a class="yt-timestamp" data-t="00:21:40">[00:21:40]</a>. LLMs can expedite this process significantly <a class="yt-timestamp" data-t="00:21:53">[00:21:53]</a>.

Instead of starting from scratch, LLMs can be used to generate an initial [[Explainable AI and Feature Importance | causal discovery graph]] based on available information, even after just one or two prompts <a class="yt-timestamp" data-t="00:23:06">[00:23:06]</a>. Experts can then validate or critique this pre-built graph, which not only saves time but also motivates them to share their unique experiences and knowledge <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>. This iterative approach fosters greater trust and facilitates the development of more meaningful models <a class="yt-timestamp" data-t="00:24:20">[00:24:20]</a>. Techniques like retrieval-augmented generation can further reduce hallucinations in LLM outputs, making them more reliable for causal discovery <a class="yt-timestamp" data-t="00:47:31">[00:47:31]</a>.

## Evaluating [[Causal AI and machine learning | Causal Models]]

Evaluating [[Causality and Machine Learning | causal models]] remains a challenge <a class="yt-timestamp" data-t="00:24:41">[00:24:41]</a>. While data-driven evaluation metrics exist in the causal world (e.g., SHDS Hamming distance, number of indirect edges) <a class="yt-timestamp" data-t="00:25:37">[00:25:37]</a>, direct comparison to ground truth can be difficult without robust expert validation.

The role of stakeholders and business experts in evaluation is paramount <a class="yt-timestamp" data-t="00:24:48">[00:24:48]</a>. By making [[Explainable AI and Feature Importance | causal discovery visualizations]] available, they can see the effects of actions, run simulations, and understand the model's implications <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. This hands-on engagement helps them trust the model and provide crucial feedback for improvement <a class="yt-timestamp" data-t="00:25:26">[00:25:26]</a>. Even when facing unprecedented events like an "alien attack" <a class="yt-timestamp" data-t="00:49:44">[00:49:44]</a>, [[Causal AI and machine learning | causal models]], by treating such events as exogenous distributions, can still offer more useful insights than random guessing <a class="yt-timestamp" data-t="00:51:06">[00:51:06]</a>.

Key strategies for evaluating and validating [[Causality Robustness and Fairness in AI Models | causal models]] without constant expert input include:
*   **Sensitivity Analysis and Partial Identification:** These advanced identification strategies account for hidden variables and expand the range of valid causal inferences <a class="yt-timestamp" data-t="00:45:37">[00:45:37]</a>.
*   **Iterative Model Building with Data Comparison:** Continuously comparing model distributions with observational data and intervening on small subsamples <a class="yt-timestamp" data-t="00:46:21">[00:46:21]</a>.
*   **Optimal Experimentation Theory:** Utilizing theories like ABCI (Active Bayesian [[Causal AI and machine learning | Causal Inference]]) to assess actions that minimize uncertainty in an optimal way <a class="yt-timestamp" data-t="00:48:18">[00:48:18]</a>.
*   **[[Causal AI and machine learning | Causal Data Fusion]]:** Combining experimental and observational data to draw causal conclusions by leveraging structural properties <a class="yt-timestamp" data-t="00:48:47">[00:48:47]</a>.

## Industry Adoption and Future Outlook

[[Causal AI and machine learning | Causal machine learning]] is not just the future; it's already the present <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Recent global events like geopolitical issues, pandemics (e.g., Corona), and semiconductor shortages have highlighted the limitations of blackbox predictive models and underscored the urgent need for [[Causal AI and machine learning | causal approaches]] <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>.

Companies are increasingly moving from descriptive and predictive analytics to prescriptive, "actionable intelligence" <a class="yt-timestamp" data-t="00:28:19">[00:28:19]</a>. The advice for companies is to directly explore [[Machine learning versus causal inference for decisionmaking | causal AI]] rather than strictly following the traditional ladder, as predictive models often fail to move beyond the experimental phase due to explainability and trust issues <a class="yt-timestamp" data-t="00:28:45">[00:28:45]</a>. When exposed to [[Causal AI and machine learning | causal approaches]], stakeholders often find that "it just makes sense" <a class="yt-timestamp" data-t="00:29:27">[00:29:27]</a>, leading to greater adoption and real-world impact. The future of dashboarding is envisioned as combining [[Causal AI and machine learning | causal AI]] with LLMs, allowing decision-makers to ask "what if" questions and quantify effects directly <a class="yt-timestamp" data-t="00:44:33">[00:44:33]</a>.

## Resources for Learning

For data scientists interested in [[Causality and Machine Learning | causality]]:
*   **"The Book of Why" by Judea Pearl:** Recommended as a foundational read to shift mindset <a class="yt-timestamp" data-t="00:31:56">[00:31:56]</a>.
*   **"Causal Inference and Discovery in Python" by You:** Described as a revolutionary book for its practical, hands-on approach to learning by doing <a class="yt-timestamp" data-t="00:32:06">[00:32:06]</a>.
*   **Open-source Libraries:** Libraries like "DoWhy" are available for practical application <a class="yt-timestamp" data-t="00:33:04">[00:33:04]</a>.
*   **Research Papers:** Staying current with recent research, such as Microsoft's work combining LLMs and [[Causal AI and machine learning | causal AI]] methods, is beneficial <a class="yt-timestamp" data-t="00:33:25">[00:33:25]</a>.
*   **Online Communities:** LinkedIn is highlighted as an "amazing resource" for connecting with [[Causality and Machine Learning | causal ambassadors]], companies, and academics to discuss problems and find solutions <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

For those starting in [[Causal AI and machine learning | causal machine learning]], the advice is to "get your hands dirty" <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. This means experimenting with algorithms, visualizing data, and consistently validating results with domain experts <a class="yt-timestamp" data-t="00:15:26">[00:15:26]</a>. Algorithms like PC algorithm and Resist have shown promising results in [[Explainable AI and Feature Importance | causal discovery]] <a class="yt-timestamp" data-t="00:15:56">[00:15:56]</a>.