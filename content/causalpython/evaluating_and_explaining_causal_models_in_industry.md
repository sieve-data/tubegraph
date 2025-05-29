---
title: Evaluating and explaining causal models in industry
videoId: gmFWhAAeBfE
---

From: [[causalpython]] <br/> 

Ishan Gupta, a lead data scientist at BMW Group, discusses the application of causality and machine learning in industrial settings, particularly focusing on how causal models can be effectively evaluated and explained to stakeholders. He highlights the shift from mere prediction to actionable business recommendations, emphasizing the importance of trust and domain expertise in the adoption of causal AI <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.

## Transition to Causal Machine Learning

Ishan Gupta's journey into data science began with a fascination for predicting things like stock investments and sports team performance <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>. He initially explored various fields within computer science, from website development to Android development, before finding his passion in data science <a class="yt-timestamp" data-t="03:15:00">[03:15:00]</a>.

He eventually identified a "missing thing" in traditional data science: the lack of explainability and actionable business recommendations beyond just predictions <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>. This led him to discover causality, which he found connected the missing puzzle pieces by offering explainability, addressing black-box modeling issues, and enabling "what if" or counterfactual scenarios <a class="yt-timestamp" data-t="04:22:00">[04:22:00]</a>. His introduction to causality came through researching explainability and how to incorporate tribal knowledge into models, eventually leading him to Judea Pearl's book, *The Book of Why* <a class="yt-timestamp" data-t="05:00:00">[05:00:00]</a>.

His PhD program in Germany allowed him to work in industry while staying connected to academics, providing an opportunity to apply research papers practically and see immediate results in business decisions, such as saving money or influencing outcomes <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>.

## Causal Machine Learning in Supply Chain Management

Ishan Gupta's main PhD focus was on supply chain management, a field he finds particularly interesting due to its complexity and the opportunity to apply machine learning <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>. He notes that the supply chain is more complex than ever, influenced by geopolitical issues, pandemics like Corona, and semiconductor shortages affecting the automotive industry <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. These urgent problems also present opportunities for companies to gain a competitive edge <a class="yt-timestamp" data-t="08:11:00">[08:11:00]</a>.

[[causality_and_its_role_in_industrial_and_manufacturing_processes | Causal machine learning]] can help business owners make better data-backed decisions, moving beyond mere predictions to provide business recommendations <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

### Addressing Challenges with Causal Models

Traditional statistical and machine learning solutions often fall short in answering critical questions from management, such as "What exactly caused something?" and "Tell me the next step?" <a class="yt-timestamp" data-t="09:02:00">[09:02:00]</a>. Data scientists often struggle to explain models using metrics like accuracy scores or post-hoc explainability methods (e.g., LIME and SHAP), which stakeholders often do not trust <a class="yt-timestamp" data-t="09:20:00">[09:20:00]</a>.

Causal machine learning addresses these gaps by:
*   **Explainability**: Causal models are inherently more explainable due to causal discovery graphs <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>.
*   **Simulations**: The ability to run "what if" and counterfactual simulations provides trust to management, allowing them to explore historical and future scenarios <a class="yt-timestamp" data-t="10:07:00">[10:07:00]</a>.
*   **Trust and Ownership**: Stakeholders trust causal models more because their domain knowledge can be integrated into the models, seeing them as an extension of their own understanding <a class="yt-timestamp" data-t="10:22:00">[10:22:00]</a>. This engagement encourages them to make the models better over time <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>.

## The Iterative Approach to Causal Modeling

An iterative approach to building causal models is a highly effective strategy in corporate settings <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>. It is crucial to start small and simple to build trust with stakeholders <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>. While starting simple, models should also provide something "extra" beyond what stakeholders already know, preventing them from dismissing the model as obvious <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>. This approach allows for gradual improvement, triangulating model results with real data and integrating more expert knowledge over time <a class="yt-timestamp" data-t="11:19:00">[11:19:00]</a>.

## Causal Discovery and Expert Knowledge

[[challenges_in_implementing_causal_analysis_in_practice | Causal discovery]] can be challenging in real-world settings due to inherent limitations <a class="yt-timestamp" data-t="13:39:00">[13:39:00]</a>. However, causal discovery algorithms can help reduce human biases <a class="yt-timestamp" data-t="13:25:00">[13:25:00]</a>.

Ishan Gupta's experience includes:
*   **Methodology**: Interviewing experts to create a "tribal knowledge graph" representing how external factors (e.g., news) affect supply chain elements like supplier backlogs or wrong deliveries <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>. This serves as a "ground truth" <a class="yt-timestamp" data-t="14:01:00">[14:01:00]</a>.
*   **Algorithm Testing**: Running causal discovery algorithms on data and comparing the generated graphs to the tribal knowledge graph <a class="yt-timestamp" data-t="14:02:00">[14:02:00]</a>. Results were "really satisfying" and close to the ground truth <a class="yt-timestamp" data-t="14:15:00">[14:15:00]</a>.
*   **Algorithms**: The PC algorithm is generally a good option <a class="yt-timestamp" data-t="15:56:00">[15:56:00]</a>. For his specific use case, the "Resist" algorithm performed exceptionally well in comparing tribal knowledge graphs <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>. The choice of algorithm depends on the specific task and data suitability <a class="yt-timestamp" data-t="16:50:00">[16:50:00]</a>.
*   **Expert Validation**: A business expert is always needed to validate the causal graph, correct edges, and potentially even trigger new insights for the expert themselves <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>.

### Interviewing Subject Matter Experts

Interviewing experts is a necessary and highly beneficial process for causal machine learning models <a class="yt-timestamp" data-t="17:16:00">[17:16:00]</a>. To ensure consistency and reduce human biases, methods like multi-criteria decision-making (e.g., FHP, TOPSIS, Analytic Hierarchy Process) can be used <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>.

Key lessons for interviewing experts:
*   Conduct interviews in a non-biased way <a class="yt-timestamp" data-t="17:30:00">[17:30:00]</a>.
*   Focus on finding cause-and-effect relationships (e.g., how external events affect supplier backlogs) <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>.
*   Collaboratively build the tribal knowledge graph <a class="yt-timestamp" data-t="18:09:00">[18:09:00]</a>.
*   Experts often don't initially realize the extent of their knowledge; motivating them to share more details is crucial <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a>.
*   Always validate the resulting graph and ensure it's a Directed Acyclic Graph (DAG) for causal machine learning <a class="yt-timestamp" data-t="18:46:00">[18:46:00]</a>.
*   Interviewing multiple experts helps mitigate human bias <a class="yt-timestamp" data-t="30:55:00">[30:55:00]</a>.

A significant benefit of this process is that the knowledge of experienced individuals, even if they retire or leave the company, is preserved within the graphical structure of the causal model <a class="yt-timestamp" data-t="19:26:00">[19:26:00]</a>. This creates a lasting impact and a win-win situation for both experts and companies <a class="yt-timestamp" data-t="20:06:00">[20:06:00]</a>.

## Leveraging Large Language Models (LLMs) for Causal Discovery

The intersection of generative AI (like LLMs) and causal AI is "exciting" <a class="yt-timestamp" data-t="21:11:00">[21:11:00]</a>. A major challenge in traditional causal discovery is the time commitment required to interview experts (e.g., 50+ hours for 25 experts) <a class="yt-timestamp" data-t="21:42:00">[21:42:00]</a>.

LLMs can significantly expedite this process by:
*   **Expediting Discovery**: Instead of starting from scratch with experts, LLMs can be used to generate initial causal relationships and build a preliminary causal discovery graph <a class="yt-timestamp" data-t="21:50:00">[21:50:00]</a>.
*   **Expert Validation**: Experts can then validate or critique this initial graph, which is often more engaging than starting from zero <a class="yt-timestamp" data-t="22:11:00">[22:11:00]</a>.
*   **Efficiency**: Ishan Gupta's research showed that LLMs could generate causal graphs very close to the "ground truth" after just one or two prompts, significantly reducing the time spent on initial discovery <a class="yt-timestamp" data-t="22:50:00">[22:50:00]</a>.

This approach not only boosts efficiency but also motivates experts by providing a starting point they can refine and add their unique knowledge to <a class="yt-timestamp" data-t="23:25:00">[23:25:00]</a>. It builds trust by showing that the models can already appreciate their domain expertise <a class="yt-timestamp" data-t="24:18:00">[24:18:00]</a>.

## [[Challenges in Evaluating Causal Models]]

[[challenges_in_evaluating_causal_models | Evaluation of causal models]] remains a challenge in the causal world <a class="yt-timestamp" data-t="24:41:00">[24:41:00]</a>. However, the role of stakeholders and business experts becomes even more critical <a class="yt-timestamp" data-t="24:48:00">[24:48:00]</a>.

Key aspects of evaluating causal models:
*   **Simulations**: Causal discovery visualizations, such as DAGs, simplify things for experts, allowing them to see cause-and-effect relationships and run simulations (e.g., counterfactual capabilities) <a class="yt-timestamp" data-t="25:01:00">[25:01:00]</a>.
*   **Iterative Improvement**: Even if a model is not perfect initially, it improves as experts interact with it and "play around" with its capabilities <a class="yt-timestamp" data-t="25:24:00">[25:24:00]</a>.
*   **Metrics vs. Expert Input**: While technical evaluation metrics for causal discovery methods exist (e.g., Structural Hamming Distance, number of indirect edges), they should not be solely relied upon <a class="yt-timestamp" data-t="25:32:00">[25:32:00]</a>. The role of stakeholders and business experts in validation remains paramount <a class="yt-timestamp" data-t="25:46:00">[25:46:00]</a>.
*   **Overcoming Fear**: Many people are initially "scared" of causal AI, fearing it might replace their jobs <a class="yt-timestamp" data-t="30:27:00">[30:27:00]</a>. However, once they experience it, they perceive it as an "extension of 100% their own knowledge," which fosters acceptance and collaboration <a class="yt-timestamp" data-t="30:35:00">[30:35:00]</a>. Involving them more in the evaluation process is key <a class="yt-timestamp" data-t="30:38:00">[30:38:00]</a>.

When experts are unavailable, data evaluation metrics become the primary means, but an iterative approach involving comparing model distributions with observational data and performing small-scale interventions can help validate models over time <a class="yt-timestamp" data-t="46:16:00">[46:16:00]</a>. Expert knowledge from documents can also be retrieved using LLMs with retrieval-augmented generation to reduce hallucinations <a class="yt-timestamp" data-t="47:06:00">[47:06:00]</a>.

For "black swan" events like an "alien attack" (a hypothetical extreme scenario), a causal model might still be useful by treating the event as a new, exogenous variable that interferes with existing processes <a class="yt-timestamp" data-t="50:01:00">[50:01:00]</a>. While challenging, especially if direct impacts are involved, propagating the distribution through the structural causal model can still yield relevant outcomes <a class="yt-timestamp" data-t="51:10:00">[51:10:00]</a>.

## [[Application of Causal Methods in Industry]]

Causality is not restricted to any particular industry <a class="yt-timestamp" data-t="26:09:00">[26:09:00]</a>.
*   **Sports Industry**: Causal models can be applied to understand what causes a sports person's injury through root cause analysis <a class="yt-timestamp" data-t="26:16:00">[26:16:00]</a>. They can also predict the effect of variables, such as a player's sleep duration, on match performance (e.g., expected goals) or injury risk <a class="yt-timestamp" data-t="26:26:00">[26:26:00]</a>.
*   **General Industry**: The ability to identify root causes and run "what if" scenarios (e.g., "If there's a tsunami in Miami, which supplier will be affected and how?") is the future of decision-making dashboards <a class="yt-timestamp" data-t="44:56:00">[44:56:00]</a>.

## The Future of Causality in Industry

Ishan Gupta believes that causality is already the present, particularly highlighted by recent global events like geopolitical conflicts, pandemics, and semiconductor shortages <a class="yt-timestamp" data-t="27:09:00">[27:09:00]</a>. These events have made companies realize the need for something more beyond black-box models <a class="yt-timestamp" data-t="27:28:00">[27:28:00]</a>. The trend of companies adopting and implementing causal methods has significantly accelerated in the past year <a class="yt-timestamp" data-t="27:49:00">[27:49:00]</a>.

### Advice for Companies Applying Causal Methodology

For companies interested in [[causal_tools_and_methodologies_in_business_applications | applying causal methodology]], it's common to progress from descriptive to diagnostic, then predictive, and finally prescriptive analytics <a class="yt-timestamp" data-t="28:12:00">[28:12:00]</a>. Ishan Gupta associates causal AI with the prescriptive part, which focuses on "what the business wants" <a class="yt-timestamp" data-t="28:22:00">[28:28:00]</a>.

His advice is to:
*   **Move Directly to Actionable Intelligence**: Instead of following the traditional linear path, companies should consider moving directly to [[causal_analysis_and_decision_making | causal intelligence]] for actionable insights <a class="yt-timestamp" data-t="28:34:00">[28:34:00]</a>.
*   **Overcome Trust Deficit**: Predictive models often don't move beyond the experimental phase due to explainability and trust deficits <a class="yt-timestamp" data-t="28:51:00">[28:51:00]</a>. Causal AI helps bridge this trust deficit <a class="yt-timestamp" data-t="29:32:00">[29:32:00]</a>.
*   **Start with Research and Experimentation**: While not straightforward, companies should invest in research and "try it out" <a class="yt-timestamp" data-t="29:09:00">[29:09:00]</a>. Stakeholders often intuitively find that causal models "just make sense" <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>. Companies may eventually have no choice but to adopt causal methods due to emerging issues <a class="yt-timestamp" data-t="29:34:00">[29:34:00]</a>.

### [[Machine learning versus causal models in business | Machine learning versus causal models in business]]

Predictive machine learning is powerful and amazing, but the challenge lies in distinguishing which questions can be answered with predictive/associative machine learning and which require a causal model <a class="yt-timestamp" data-t="55:04:00">[55:04:00]</a>. Recognizing and addressing this distinction will accelerate the entire AI community <a class="yt-timestamp" data-t="55:35:00">[55:35:00]</a>.

## Resources for Data Scientists

For data scientists interested in causality, overcoming the initial mental barrier that "something like this exists" is key, as it involves concepts and calculations often not taught in conventional education <a class="yt-timestamp" data-t="31:38:00">[31:38:00]</a>.

Recommended resources:
*   **Books**:
    *   *The Book of Why* by Judea Pearl, which helps change one's mindset <a class="yt-timestamp" data-t="31:56:00">[31:56:00]</a>.
    *   *Causal Inference and Discovery in Python* by Y, described as a "revolutionary book" for its hands-on approach and connection to NLP and LLMs, making causality less foreign <a class="yt-timestamp" data-t="32:06:00">[32:06:00]</a>.
*   **Community**:
    *   Open-source libraries like DoWhy <a class="yt-timestamp" data-t="33:04:00">[33:04:00]</a>.
    *   LinkedIn is an "amazing" and "underrated" resource for staying updated on research papers and connecting with causal ambassadors and companies like Causalens <a class="yt-timestamp" data-t="33:57:00">[33:57:00]</a>. Engaging in comment sections and asking questions fosters learning <a class="yt-timestamp" data-t="34:25:00">[34:25:00]</a>.
*   **Academia**: There's a noticeable shift in academia, with universities like TUM, LMU, and MIT incorporating causal machine learning into their curricula and research, indicating a growing recognition of its importance <a class="yt-timestamp" data-t="40:10:00">[40:10:00]</a>.

## Personal Journey and Advice

Ishan Gupta emphasizes "learning by doing" and getting hands-on experience, rather than just theoretical study <a class="yt-timestamp" data-t="56:30:00">[56:30:00]</a>. He suggests taking a conventional machine learning use case and reframing it as a causal problem to explore the benefits of causal AI <a class="yt-timestamp" data-t="57:05:00">[57:05:00]</a>.

Key advice for those starting out:
*   **Get Your Hands Dirty**: Try out different algorithms, visualizations, and datasets <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.
*   **Clean Data**: Follow conventional data science practices, including working with clean data <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>.
*   **Domain Expertise**: Always have a domain expert validate the results <a class="yt-timestamp" data-t="15:33:00">[15:33:00]</a>.
*   **Networking**: Networking is crucial for success, especially in the causal world where experts are needed to validate models <a class="yt-timestamp" data-t="35:00:00">[35:00:00]</a>. Diverse networking (e.g., with lawyers or medical professionals) can provide unique perspectives <a class="yt-timestamp" data-t="35:41:00">[35:41:00]</a>.

His motivation stems from the ability of data science to "create a difference in people's lives," whether it's by making companies more profitable, helping sports teams win championships, or even predicting health conditions like cancer early on <a class="yt-timestamp" data-t="58:08:00">[58:08:00]</a>. He sees data scientists as "fancy doctors" who can predict things earlier and quicker than conventional methods <a class="yt-timestamp" data-t="58:42:00">[58:42:00]</a>.

Transitioning between industries, such as from sports to automotive, can be challenging due to a lack of domain knowledge <a class="yt-timestamp" data-t="59:25:00">[59:25:00]</a>. However, having supportive people and role models, combined with continuous learning and networking, helps navigate such transitions <a class="yt-timestamp" data-t="59:59:00">[59:59:00]</a>.

A good leader, according to Ishan Gupta, leads from the front while trusting their team and giving them the freedom to innovate <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>. They should prioritize "best ideas" over hierarchy and be open to both giving and receiving criticism <a class="yt-timestamp" data-t="01:01:41">[01:01:41]</a>.