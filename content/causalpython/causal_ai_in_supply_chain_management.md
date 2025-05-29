---
title: Causal AI in supply chain management
videoId: gmFWhAAeBfE
---

From: [[causalpython]] <br/> 

Ishan Gupta, Lead Data Scientist at BMW Group, discusses the application of [[causal_ai_in_business_applications | Causal AI]] and [[causal_ai_and_machine_learning_intersection | machine learning]] in supply chain management, emphasizing its ability to provide explainable models and actionable business recommendations.

## Ishan Gupta's Journey to Causal AI

Ishan Gupta's interest in data began at age 10 as a cricket player, realizing the potential of data <a class="yt-timestamp" data-t="00:34:00">[00:34:00]</a>. He pursued computer science and explored various fields, including website and Android development, before focusing on data science <a class="yt-timestamp" data-t="03:04:00">[03:04:00]</a>. His fascination with predicting outcomes, from stock investments to sports team performance, fueled his interest <a class="yt-timestamp" data-t="03:36:00">[03:36:00]</a>.

He found traditional data science lacked "explainability" and often resulted in mere predictions rather than actionable business recommendations <a class="yt-timestamp" data-t="03:52:00">[03:52:00]</a>. With an entrepreneurial background, he sought to make a tangible difference <a class="yt-timestamp" data-t="04:05:00">[04:05:00]</a>. This led him to [[causality_in_ai | causality]], which he saw as "connecting the missing puzzle" by covering explainability, addressing black-box modeling, and enabling "what-if" and counterfactual scenarios <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>.

His introduction to [[causality_in_ai | causality]] began with a simple Google search for "explainability" and how to incorporate tribal knowledge into models <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>. During his PhD research, he discovered [[causal_reasoning_in_artificial_intelligence | causal machine learning]] and read "The Book of Why" by Judea Pearl, which solidified his interest <a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>.

## PhD Work and Industry Application

Ishan's PhD program in Germany allowed him to work in industry while remaining connected to academia, focusing on practical application rather than just theoretical research <a class="yt-timestamp" data-t="06:09:00">[06:09:00]</a>. The main topic of his PhD was [[causal_ai_in_business_applications | supply chain management]] <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>. He saw many use cases for combining [[causal_ai_and_machine_learning_intersection | machine learning]] with supply chain, especially given its increasing complexity due to geopolitical issues, pandemics (like COVID-19), and semiconductor shortages <a class="yt-timestamp" data-t="07:54:00">[07:54:00]</a>. These challenges presented an opportunity for companies to use [[causal_ai_in_business_applications | causal machine learning]] to make better data-backed decisions and provide business recommendations beyond mere predictions <a class="yt-timestamp" data-t="08:17:00">[08:17:00]</a>.

## Causal Machine Learning in Supply Chain Challenges

Traditional statistical and [[causal_ai_and_machine_learning_intersection | machine learning]] solutions often fail to address key challenges in supply chain management, particularly in gaining stakeholder trust <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>. Management often asks for explanations of what *caused* an outcome and what the next steps should be <a class="yt-timestamp" data-t="09:10:00">[09:10:00]</a>. Data scientists struggle to explain models using complex metrics or post-hoc explainability methods like LIME and SHAP, leading to a loss of trust from stakeholders <a class="yt-timestamp" data-t="09:25:00">[09:25:00]</a>.

### Addressing Explainability and Trust
[[causal_ai_in_business_applications | Causal machine learning]] models are inherently more explainable due to causal discovery graphs, allowing for "what-if" simulations and future scenarios <a class="yt-timestamp" data-t="10:01:00">[10:01:00]</a>. This builds trust because stakeholders see their own knowledge reflected in the models, viewing them as an extension of their own understanding <a class="yt-timestamp" data-t="10:20:00">[10:20:00]</a>. While initial models might not be perfect, this trust encourages management to improve them <a class="yt-timestamp" data-t="10:38:00">[10:38:00]</a>.

### Iterative Approach
An iterative approach to building [[causal_reasoning_in_artificial_intelligence | causal models]] is highly effective in corporate settings <a class="yt-timestamp" data-t="11:44:00">[11:44:00]</a>. Starting small and simple builds trust with stakeholders <a class="yt-timestamp" data-t="12:00:00">[12:00:00]</a>. It's crucial to provide some added value beyond what experts already know, to demonstrate the model's utility <a class="yt-timestamp" data-t="12:11:00">[12:11:00]</a>.

### Causal Discovery Algorithms
While [[causal_reasoning_in_artificial_intelligence | causal discovery]] can be challenging and imperfect, it helps reduce human biases <a class="yt-timestamp" data-t="13:13:00">[13:13:00]</a>. Ishan's experience with these algorithms has been positive <a class="yt-timestamp" data-t="13:31:00">[13:31:00]</a>. He tested algorithms against a "ground truth" tribal knowledge graph derived from interviewing 25 experts <a class="yt-timestamp" data-t="13:35:00">[13:35:00]</a>. The "Resist" algorithm performed exceptionally well, producing causal discovery graphs closely resembling the ground truth for internal supplier performance KPIs like backlogs or wrong deliveries <a class="yt-timestamp" data-t="16:05:00">[16:05:00]</a>. The PC algorithm is also a good option <a class="yt-timestamp" data-t="15:58:00">[15:58:00]</a>. Ultimately, a business expert is needed to validate and refine the model's edges <a class="yt-timestamp" data-t="14:26:00">[14:26:00]</a>.

### Interviewing Subject Matter Experts
Interviewing experts is crucial for [[causal_ai_in_business_applications | causal machine learning]] models <a class="yt-timestamp" data-t="17:16:00">[17:16:00]</a>. Methods like Multi-Criteria Decision Making (MCDM) approaches, specifically FHP (Fuzzy Analytic Hierarchy Process), TOPSIS (Technique for Order Preference by Similarity to Ideal Solution), and Analytic Hierarchy Process (AHP), help ensure consistency and reduce human biases <a class="yt-timestamp" data-t="17:33:00">[17:33:00]</a>. Experts may initially underestimate their own knowledge, but workshops help them build a Directed Acyclic Graph (DAG) and realize the value of their insights <a class="yt-timestamp" data-t="18:16:00">[18:16:00]</a>. This process of constructing graphs is a way to preserve organizational knowledge, even when experts retire or leave, creating a lasting "monument" to their expertise <a class="yt-timestamp" data-t="19:26:00">[19:26:00]</a>.

### Intersection with Generative AI (LLMs)
Leveraging generative AI, specifically Large Language Models (LLMs), can significantly expedite the [[causal_reasoning_in_artificial_intelligence | causal discovery]] process <a class="yt-timestamp" data-t="21:46:00">[21:46:00]</a>. Instead of starting from scratch, LLMs can generate an initial causal discovery graph that experts can then validate or criticize, making the process more efficient <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>. Ishan found that LLMs produced results very close to his manually constructed ground truth graph with just a few prompts <a class="yt-timestamp" data-t="23:04:00">[23:04:00]</a>. This not only boosts efficiency but also motivates experts, as they appreciate the model's recommendations and are eager to contribute their unique experiences <a class="yt-timestamp" data-t="23:51:00">[23:51:00]</a>. This fosters trust and builds better technology <a class="yt-timestamp" data-t="24:20:00">[24:20:00]</a>.

### Evaluation of Causal Models
Evaluating [[causality_in_ai | causal models]] is still a challenge, but the role of stakeholders and business experts remains paramount <a class="yt-timestamp" data-t="24:41:00">[24:41:00]</a>. Causal discovery visualizations simplify complex relationships, allowing experts to see cause-and-effect and run simulations <a class="yt-timestamp" data-t="24:58:00">[24:58:00]</a>. While metrics like Hamming distance and the number of indirect edges exist for [[causal_reasoning_in_artificial_intelligence | causal discovery]] methods, stakeholder involvement and validation are key <a class="yt-timestamp" data-t="25:37:00">[25:37:00]</a>.

## Causal AI Beyond Supply Chain
[[causal_ai_and_its_application_in_different_sciences | Causal AI]] is not limited to supply chain or automotive industries <a class="yt-timestamp" data-t="27:00:00">[27:00:00]</a>. Ishan notes its applicability in sports, such as root cause analysis for athlete injuries or predicting match performance based on variables like sleep duration <a class="yt-timestamp" data-t="26:16:00">[26:16:00]</a>. The potential is immense and spans across various sectors <a class="yt-timestamp" data-t="26:58:00">[26:58:00]</a>.

## The Future of Causal AI

Ishan believes [[causality_in_ai | causal AI]] is not just the future but already the present, particularly highlighted by recent global events like the Eastern European conflict, pandemics, and semiconductor issues that exposed the limitations of black-box models <a class="yt-timestamp" data-t="27:09:00">[27:09:00]</a>. Many companies are now actively exploring and implementing [[causal_ai_in_business_applications | causal solutions]] <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>.

He advises companies to move directly towards "causal intelligence" (prescriptive analytics) rather than following the traditional ladder of descriptive, diagnostic, and predictive analytics <a class="yt-timestamp" data-t="28:22:00">[28:22:00]</a>. Predictive models often get stuck in the experimental phase due to explainability and trust issues <a class="yt-timestamp" data-t="28:48:00">[28:48:00]</a>. [[causal_ai_in_business_applications | Causal AI]] offers actionable intelligence that "just makes sense" to stakeholders, even if companies aren't using it widely yet, they will eventually have no choice <a class="yt-timestamp" data-t="29:21:00">[29:21:00]</a>.

## Resources for Data Scientists
For data scientists interested in [[causality_in_ai | causality]], Ishan recommends:
*   **Books**:
    *   "The Book of Why" by Judea Pearl <a class="yt-timestamp" data-t="31:56:00">[31:56:00]</a>.
    *   "Causal Inference and Discovery in Python" by Yu <a class="yt-timestamp" data-t="32:06:00">[32:06:00]</a>.
*   **Practical Application**: Get hands-on by trying out different algorithms (like PC or Resist), using open-source libraries (e.g., DoWhy), and conducting visualizations <a class="yt-timestamp" data-t="32:26:00">[32:26:00]</a>.
*   **Networking**: Connect with the [[causal_ai_and_its_role_in_experiments | Causal AI]] community on LinkedIn, follow companies like Causalens, and engage with academics and industry professionals (e.g., from Spotify or Netflix) to learn about diverse use cases <a class="yt-timestamp" data-t="33:57:00">[33:57:00]</a>.

## Motivation and Outlook

Ishan is motivated by the ability of data science to make a difference in people's lives, akin to how doctors impact health <a class="yt-timestamp" data-t="00:58:08">[00:58:08]</a>. He envisions a future where managers can ask dashboards complex [[causal_reasoning_in_artificial_intelligence | causal questions]], combining [[causal_ai_in_business_applications | Causal AI]] with LLMs, such as predicting which supplier will be affected by a tsunami and quantifying that effect <a class="yt-timestamp" data-t="00:44:33">[00:44:33]</a>. This future of dashboarding, offering actionable insights for unprecedented events, is expected "sooner than later" <a class="yt-timestamp" data-t="00:45:08">[00:45:08]</a>.

He clarifies that [[causal_ai_and_machine_learning_intersection | causal machine learning]] is not "better" than predictive machine learning; rather, the challenge lies in understanding which questions require a [[causal_reasoning_in_artificial_intelligence | causal model]] versus an associative model <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>. Recognizing this distinction will advance the entire AI community <a class="yt-timestamp" data-t="00:55:35">[00:55:35]</a>.

### Advice for Newcomers
For those feeling overwhelmed by the complexity of [[causality_in_ai | causality]], Ishan advises:
*   **Learning by Doing**: Apply theoretical knowledge by finding use cases and getting hands-on experience <a class="yt-timestamp" data-t="00:56:26">[00:56:26]</a>.
*   **Causal Framing**: Reframe conventional [[causal_ai_and_machine_learning_intersection | machine learning]] problems as [[causal_reasoning_in_artificial_intelligence | causal problems]] to see how [[causal_ai_and_its_application_in_different_sciences | Causal AI]] can be more beneficial <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>.
*   **Embrace Questions**: Questions from others, even about extreme scenarios like "alien attacks," drive further learning and engagement with the community <a class="yt-timestamp" data-t="00:57:33">[00:57:33]</a>.

## Changing Landscape in Academia
Ishan observes a significant change in academia, with universities like TUM, LMU, and MIT increasingly incorporating [[causal_reasoning_in_artificial_intelligence | causal machine learning]] into their curricula <a class="yt-timestamp" data-t="00:40:26">[00:40:26]</a>. This offers the new generation an early opportunity to delve deeper into the topic <a class="yt-timestamp" data-t="00:40:55">[00:40:55]</a>.

## Insights from Analytics Levels
Comparing descriptive, diagnostic, predictive, and prescriptive (causal) analytics, Ishan's research found that experts overwhelmingly preferred a [[causal_reasoning_in_artificial_intelligence | causal approach]] <a class="yt-timestamp" data-t="00:41:42">[00:41:42]</a>.
*   **Explainability**: Experts clearly distrusted traditional [[causal_ai_and_machine_learning_intersection | machine learning]] for explainability but highly trusted [[causal_ai_in_business_applications | causal machine learning]] <a class="yt-timestamp" data-t="00:42:28">[00:42:28]</a>.
*   **Key Capabilities**: For critical capabilities in supply chain like stress testing and time to recover, [[causal_ai_in_business_applications | Causal AI]] scored significantly higher <a class="yt-timestamp" data-t="00:42:39">[00:42:39]</a>.
*   **Overall Preference**: Across all criteria, [[causal_ai_in_business_applications | causal machine learning]] was preferred by approximately 48% of experts, significantly outweighing descriptive (24%) and predictive analytics <a class="yt-timestamp" data-t="00:43:01">[00:43:01]</a>. This suggests that large investments in predictive models might not yield proportional trust from stakeholders <a class="yt-timestamp" data-t="00:43:20">[00:43:20]</a>.

Ishan concludes that experts "absolutely loved" the [[causal_ai_in_business_applications | causal machine learning]] tool, eagerly engaging with it to run simulations and gain insights <a class="yt-timestamp" data-t="00:43:52">[00:43:52]</a>.