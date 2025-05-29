---
title: Benefits and challenges of causal machine learning
videoId: gmFWhAAeBfE
---

From: [[causalpython]] <br/> 

The Causal Bandits podcast frequently explores the intersection of [[Causal inference and machine learning | causality and machine learning]]. In one episode, Lead Data Scientist at BMW Group, Ishan Gupta, discusses his journey into the field, highlighting the [[Integration of Causal Thinking in Machine Learning | benefits and challenges of causal machine learning]]. Gupta emphasizes that traditional machine learning often lacks explainability and actionable business recommendations, areas where causal machine learning excels <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>.

## Benefits of Causal Machine Learning

### Enhanced Explainability and Trust
One of the primary advantages of causal machine learning is its ability to provide explainable models <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>. Unlike black-box models, causal models, particularly through causal discovery graphs, allow stakeholders to understand "what exactly caused something" <a class="yt-timestamp" data-t="09:15:00">[09:15:00]</a> <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. This transparency builds significant trust with management and business experts, as they see the models as an "extension of their own brain" because their tribal knowledge is integrated <a class="yt-timestamp" data-t="10:28:00">[10:28:00]</a>.

### Actionable Business Recommendations
Causal machine learning moves beyond mere predictions to offer actionable business recommendations <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a> <a class="yt-timestamp" data-t="04:48:00">[04:48:00]</a>. It enables "what if" and counterfactual scenarios, allowing users to run simulations and play around with different outcomes, which is highly valued by management <a class="yt-timestamp" data-t="04:52:00">[04:52:00]</a> <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a> <a class="yt-timestamp" data-t="25:09:00">[25:09:00]</a>. This capability helps in making better data-backed decisions and potentially saving significant money <a class="yt-timestamp" data-t="07:07:00">[07:07:00]</a> <a class="yt-timestamp" data-t="08:33:00">[08:33:00]</a>.

### Integration of Expert Knowledge
A key strength lies in its capacity to incorporate the vast knowledge of business experts. By conducting non-biased interviews, data scientists can build tribal knowledge graphs that serve as a "ground truth" for model validation <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a> <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>. This process not only refines the models but also preserves the legacy of experts' knowledge within the company, even after they leave <a class="yt-timestamp" data-t="19:26:00">[19:26:00]</a> <a class="yt-timestamp" data-t="20:06:00">[20:06:00]</a>.

### Efficiency with Large Language Models (LLMs)
The intersection of [[Causal AI and machine learning intersection | causal AI]] and LLMs is particularly exciting for expediting causal discovery <a class="yt-timestamp" data-t="21:14:00">[21:14:00]</a> <a class="yt-timestamp" data-t="21:49:00">[21:49:00]</a>. Instead of starting from scratch, LLMs can generate initial causal relationship graphs, which experts can then validate or criticize, significantly reducing the time required for interviews <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a> <a class="yt-timestamp" data-t="22:20:00">[22:20:00]</a>. This approach not only boosts efficiency but also motivates experts by showing them the potential of their knowledge <a class="yt-timestamp" data-t="23:25:00">[23:25:00]</a>.

### Versatility Across Industries
Causal machine learning is not limited to specific industries like supply chain or automotive. Its applicability extends to sports (e.g., predicting player injuries, evaluating match performance based on sleep hours) and even medicine (e.g., predicting cancer early) <a class="yt-timestamp" data-t="26:09:00">[26:09:00]</a> <a class="yt-timestamp" data-t="58:28:00">[58:28:00]</a>. This broad applicability underlines its immense potential <a class="yt-timestamp" data-t="26:58:00">[26:58:00]</a>.

## Challenges of Causal Machine Learning

### Stakeholder Hesitation
Initially, stakeholders, including business experts and data scientists, can be apprehensive about causal AI, fearing it might replace their jobs <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a> <a class="yt-timestamp" data-t="30:27:00">[30:27:00]</a>. This "fundamental fear of causality" highlights a need for clear communication and involvement in the process to demonstrate its complementary nature <a class="yt-timestamp" data-t="29:46:00">[29:46:46]</a> <a class="yt-timestamp" data-t="30:38:00">[30:38:00]</a>.

### Complexity of Causal Discovery
[[Challenges in causal machine learning compared to traditional methods | Causal discovery]] can be challenging in real-world settings due to limitations of methods and inherent complexities <a class="yt-timestamp" data-t="12:39:00">[12:39:00]</a>. While algorithms like PC and Resist show promising results in approximating ground truth graphs, human biases and the need for expert validation remain critical <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a> <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>.

### Time-Consuming Expert Interviews
Gathering meaningful relationships and constructing comprehensive Directed Acyclic Graphs (DAGs) from expert interviews is a time-consuming process. Interviewing 25 experts, for instance, can take over 50 hours <a class="yt-timestamp" data-t="21:38:00">[21:38:00]</a> <a class="yt-timestamp" data-t="21:40:00">[21:40:00]</a>. Corporate environments often lack this much dedicated time <a class="yt-timestamp" data-t="21:42:00">[21:42:00]</a>.

### Evaluation and [[Benchmarking in causal machine learning | Benchmarking]]
Evaluating causal models remains a challenge, even with metrics like Hamming distance. While these numbers are useful for data scientists, convincing management often requires the direct involvement of business experts to validate the model's logic and practical implications through simulations <a class="yt-timestamp" data-t="24:41:00">[24:41:00]</a> <a class="yt-timestamp" data-t="25:32:00">[25:32:00]</a> <a class="yt-timestamp" data-t="30:05:00">[30:05:00]</a>.

### Data Scientist Familiarity
Many data scientists are not familiar with causal methods, as these topics were often not covered in their academic training <a class="yt-timestamp" data-t="39:59:00">[39:59:00]</a>. This lack of foundational knowledge creates a barrier to broader adoption <a class="yt-timestamp" data-t="31:25:00">[31:25:00]</a>.

### Limitations of Science
It's crucial to acknowledge that causal models, like science itself, have limitations and are not ultimate solutions <a class="yt-timestamp" data-t="53:30:00">[53:30:00]</a> <a class="yt-timestamp" data-t="54:19:00">[54:19:00]</a>. Expectations should be managed; causal models are an embodiment of the scientific method, offering strong hypotheses to be falsified, not absolute truths <a class="yt-timestamp" data-t="53:01:00">[53:01:00]</a> <a class="yt-timestamp" data-t="53:41:00">[53:41:00]</a>.

## Strategies for Adoption

### Iterative Approach
An effective strategy is to start small and simple, building trust with stakeholders and iterating on the model <a class="yt-timestamp" data-t="11:48:00">[11:48:00]</a> <a class="yt-timestamp" data-t="12:02:00">[12:02:00]</a>. This involves comparing model distributions with observational data and performing interventions on small subsamples <a class="yt-timestamp" data-t="46:18:00">[46:18:00]</a>.

### Leveraging Expert Knowledge and LLMs
Actively involving multiple business experts in the evaluation process helps validate the causal graphs and reduces human biases <a class="yt-timestamp" data-t="30:55:00">[30:55:00]</a> <a class="yt-timestamp" data-t="31:00:00">[31:00:00]</a>. Utilizing LLMs to generate preliminary causal relationships can significantly streamline this process, allowing experts to focus on refinement rather than initial construction <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>. Non-biased interviewing methods like Multi-Criteria Decision Making (MCDM), including FHP, TOPSIS, or Analytic Hierarchy Process (AHP), can ensure consistency and reduce bias when gathering expert knowledge <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>.

### Educational Resources and Community
To address the lack of familiarity among data scientists, resources like "The Book of Why" by Judea Pearl and "Causal Inference and Discovery in Python" are highly recommended <a class="yt-timestamp" data-t="31:56:00">[31:56:00]</a> <a class="yt-timestamp" data-t="32:06:00">[32:06:00]</a>. These books encourage a "learning by doing" approach. Staying connected with the [[advances in causal machine learning research | causal community]] on platforms like LinkedIn provides access to new research papers and allows for direct interaction with experts and practitioners <a class="yt-timestamp" data-t="33:57:00">[33:57:00]</a> <a class="yt-timestamp" data-t="34:18:00">[34:18:00]</a>.

### Practical Application and Networking
The advice is to "get your hands dirty" by applying causal concepts to real-world use cases, even if initially simple <a class="yt-timestamp" data-t="15:07:00">[15:07:07]</a> <a class="yt-timestamp" data-t="56:30:00">[56:30:00]</a>. Networking is crucial, not only for validation from domain experts but also for gaining diverse perspectives on problems from professionals in different fields <a class="yt-timestamp" data-t="35:00:00">[35:00:00]</a> <a class="yt-timestamp" data-t="35:51:00">[35:51:00]</a>.

## Future of Causal Machine Learning

Gupta believes that [[Causal AI and machine learning intersection | causal machine learning]] is not just the future but already the present, especially with recent global events highlighting the need for more than just black-box predictions <a class="yt-timestamp" data-t="27:10:00">[27:10:00]</a> <a class="yt-timestamp" data-t="27:51:00">[27:51:00]</a>. He envisions a future where dashboards combine causal AI with LLMs, allowing decision-makers to ask direct causal questions (e.g., "Tell me which supplier will be affected if there's a tsunami in Miami and in what way?") and receive quantifiable, actionable insights <a class="yt-timestamp" data-t="44:33:00">[44:33:00]</a> <a class="yt-timestamp" data-t="44:59:00">[44:59:00]</a>.

The goal for companies should be to move directly to "actionable intelligence" or "causal intelligence" rather than following the traditional progression from descriptive to predictive analytics, which often stalls at the experimental phase due to trust deficits and explainability issues <a class="yt-timestamp" data-t="28:37:00">[28:37:00]</a> <a class="yt-timestamp" data-t="28:45:00">[28:45:00]</a>. Causal thinking provides a better way of approaching machine learning by clarifying which questions require a causal model, thus moving the entire AI community forward <a class="yt-timestamp" data-t="55:10:00">[55:10:00]</a> <a class="yt-timestamp" data-t="55:38:00">[55:38:00]</a>. The increasing emphasis on causality in academia, with universities now incorporating it into their curricula, further paves the way for its wider [[Impact of causal machine learning beyond academia | adoption and impact]] <a class="yt-timestamp" data-t="40:10:00">[40:10:00]</a>.