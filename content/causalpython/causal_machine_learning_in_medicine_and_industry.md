---
title: Causal Machine Learning in Medicine and Industry
videoId: _mJclm_aJlc
---

From: [[causalpython]] <br/> 

Professor Stefan Wager, Head of the Institute for AI and Management at LMU, emphasizes the critical need for [[causal_ai_and_machine_learning | causal machine learning]] to make a distinctive and profound impact in practice, particularly in medicine and various industries <a class="yt-timestamp" data-t="01:45:18">[01:45:18]</a>. His team's papers are consistently accepted at top machine learning conferences globally <a class="yt-timestamp" data-t="00:24:02">[00:24:02]</a>.

## Driving Impact in Medicine

Wager highlights that medicine is one of the fields where [[causal_ai_in_medicine | causal AI and machine learning]] could have a significant impact on patients' lives <a class="yt-timestamp" data-t="01:51:18">[01:51:18]</a>. However, a major challenge lies in encouraging medical professionals to actually use [[causal_ai_in_medicine | causal machine learning]] tools <a class="yt-timestamp" data-t="02:05:00">[02:05:00]</a>.

To facilitate adoption, the causal community needs to:
*   **Go to them**: Instead of waiting for medical professionals to realize the benefits, the community should actively show them how to use [[causal_ai_in_medicine | causal machine learning]] in their day-to-day work to answer new or existing questions more rigorously <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.
*   **Speak their language**: It is crucial to translate complex methods and specialized language into terms that medical practitioners can understand, making them feel understood rather than just trying to make them understand <a class="yt-timestamp" data-t="03:07:00">[03:07:00]</a>, <a class="yt-timestamp" data-t="03:29:00">[03:29:00]</a>, <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.
*   **Simplify concepts**: Complex [[causal_ai_and_machine_learning | causal machine learning]] methods are difficult to explain to those without a solid technical background in statistics, mathematics, or computer science, such as medical users <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>, <a class="yt-timestamp" data-t="05:52:00">[05:52:00]</a>. A "magic wizard" that explains concepts instantly would be ideal <a class="yt-timestamp" data-t="05:18:00">[05:18:00]</a>.

### Application Example: Diabetes Prevention
In a collaboration with a large health insurance company in the Middle East, a two-stage [[causal_ai_and_machine_learning | machine learning]] model was developed to improve diabetes prevention programs <a class="yt-timestamp" data-t="10:34:00">[10:34:00]</a>.
1.  The first stage estimated the potential benefit of preventive care from electronic health records <a class="yt-timestamp" data-t="12:09:00">[12:09:00]</a>.
2.  The second stage involved an optimization model to identify patients who would benefit most, allowing the health insurance company to allocate limited resources cost-effectively <a class="yt-timestamp" data-t="12:17:00">[12:17:00]</a>. This contrasts with traditional predictive [[machine_learning_versus_causal_inference_for_decisionmaking | machine learning]], which would only target those with the highest risk, not considering the impact of intervention <a class="yt-timestamp" data-t="11:25:00">[11:25:00]</a>.

### The Importance of Uncertainty Quantification
Wager stresses that uncertainty quantification is "hugely important" for reliable decision-making in medicine <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>. Unlike in machine learning, medical papers rigorously report uncertainty intervals for estimates <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>. For treatment recommendations, medical practice will not use methods that rely solely on point estimates <a class="yt-timestamp" data-t="09:44:00">[09:44:00]</a>. Developing methods for reliable uncertainty quantification is considered the "holy grail" for bringing [[causal_ai_in_medicine | causal machine learning]] into medical practice <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

## Causal Machine Learning in Industry

Wager refutes criticisms that [[causality_and_machine_learning | causal machine learning]] is impossible to implement in practice or drive real-world outcomes, offering several examples:

*   **ABB Hitachi**: A [[causal_machine_learning_applications_in_various_industries | causal machine learning]] tool was implemented in a field experiment to reduce yield loss in semiconductor fabrication by almost 50% (49%) <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>, <a class="yt-timestamp" data-t="14:43:00">[14:43:00]</a>, <a class="yt-timestamp" data-t="16:01:00">[16:01:00]</a>.
*   **Large Media Company**: A [[causal_machine_learning_applications_in_various_industries | causal inference]] task was used to optimize the front page of a newspaper, developing decision support systems that empowered editors to make better choices, rather than replacing them <a class="yt-timestamp" data-t="13:15:00">[13:15:00]</a>.
*   **Booking.com**: This company runs [[causal_machine_learning_applications_in_various_industries | causal machine learning]] algorithms at a large scale <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>, <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.
*   **OECD (Development Aid)**: Unique data from the OECD was used to create a model for allocating development aid, a complex problem involving hundreds of stakeholders and countries <a class="yt-timestamp" data-t="24:42:00">[24:42:00]</a>. The paper aims to provide a gentle introduction on how [[causal_ai_and_its_connection_to_machine_learning | causal machine learning]] can assist in such decision-making settings <a class="yt-timestamp" data-t="25:40:00">[25:40:00]</a>. Notably, this solution used a simpler generalized propensity score with polynomial regression, outperforming more complex approaches like neural networks, due to common data sparsity in enterprises <a class="yt-timestamp" data-t="26:50:00">[26:50:00]</a>.

## Pillars for Improvement and Success

Wager outlines three key pillars for improving [[causal_ai_and_machine_learning | causal machine learning]] models and methods to ensure reliable inferences:
1.  **Move Beyond Stylized Settings**: Current research often focuses on stylized settings for rigorous method demonstration <a class="yt-timestamp" data-t="07:47:00">[07:47:00]</a>. However, real-world decision-making settings are not stylized, requiring methods that extend beyond binary treatments and outcomes, such as time series analysis, drug combinations, and complex treatments <a class="yt-timestamp" data-t="08:06:00">[08:06:00]</a>.
2.  **Uncertainty Quantification**: As discussed, this is critical for reliable decision-making in practice <a class="yt-timestamp" data-t="08:49:00">[08:49:00]</a>.
3.  **Complex Treatments**: Developing methods to analyze complex treatments is an ongoing area of research <a class="yt-timestamp" data-t="08:40:00">[08:40:00]</a>.

### The "Recipe for Success"
Wager attributes his team's consistent acceptance at top conferences to a "great team" <a class="yt-timestamp" data-t="19:52:00">[19:52:00]</a>. Key elements include:
*   **Joint Lunch**: A "very European way" to discuss ideas <a class="yt-timestamp" data-t="20:15:00">[20:15:00]</a>.
*   **Whiteboards**: Present in all offices for discussion <a class="yt-timestamp" data-t="20:29:00">[20:29:00]</a>.
*   **Good Team Spirit**: Essential for collaboration <a class="yt-timestamp" data-t="20:34:00">[20:34:00]</a>.
*   **Diversity**: Not just cultural or gender diversity, but diversity in academic backgrounds (mathematics, data science, statistics, computer science, economics) <a class="yt-timestamp" data-t="21:12:00">[21:12:00]</a>. This allows for different perspectives and problem-solving approaches, combining expertise across fields <a class="yt-timestamp" data-t="21:30:00">[21:30:00]</a>, <a class="yt-timestamp" data-t="22:35:00">[22:35:00]</a>.

## Education and Practical Application

Wager advocates for better educational resources, including summary pieces and "role model papers," to help practitioners understand [[causal_ai_and_its_connection_to_machine_learning | causal machine learning]] concepts and best practices, especially concerning the underlying assumptions and robustness checks <a class="yt-timestamp" data-t="19:02:00">[19:02:00]</a>. He suggests that the community needs to get out of its "rabbit hole" and explain complex methods in simpler terms for domain experts or managers <a class="yt-timestamp" data-t="16:54:00">[16:54:00]</a>.

His personal analogy for managers explaining the value of [[causal_ai_and_its_connection_to_machine_learning | causal machine learning]] is using two "crystal balls" – one for decision A and one for decision B – to show how different choices improve future outcomes, rather than just predicting the future <a class="yt-timestamp" data-t="18:02:00">[18:02:00]</a>.

### Lessons from Entrepreneurship
From his experience starting a company that aimed to use [[machine_learning_and_causality | machine learning]] to improve corporate communication, Wager learned:
*   **Being too early**: Customers needed too much education and trust-building in AI systems <a class="yt-timestamp" data-t="28:21:00">[28:21:00]</a>.
*   **Product complexity**: The product required too much customization, making the sales process complex <a class="yt-timestamp" data-t="28:35:00">[28:35:00]</a>.
*   **Test ideas early**: Don't be too attached to ideas, especially for academics who "love our algorithms" <a class="yt-timestamp" data-t="28:48:00">[28:48:00]</a>. This "one-day rule" suggests that if a standard [[machine_learning_and_causality | machine learning]] approach (like linear regression or random forest) doesn't work on a dataset within the first day, the task might not be solvable by [[machine_learning_and_causality | machine learning]], or the data might be problematic <a class="yt-timestamp" data-t="29:57:00">[29:57:00]</a>.

## Message to the Causal Python Community

Wager calls for more Python packages, similar to `EconML` and `DoubleML`, particularly for other parts of the [[causality_and_machine_learning | causal inference]] pipeline, such as partial identification <a class="yt-timestamp" data-t="31:06:00">[31:06:00]</a>. These libraries would help in the uptake of [[causal_ai_and_machine_learning | causal machine learning]] ideas <a class="yt-timestamp" data-t="31:43:00">[31:43:00]</a>.

For managers and entrepreneurs, Wager advises testing [[causal_ai_and_machine_learning | causal machine learning]] ideas to identify effective use cases and understand which methods work in practice and are sufficiently robust <a class="yt-timestamp" data-t="32:54:00">[32:54:00]</a>. He notes that while a simple S-learner (traditional [[machine_learning_and_causality | machine learning]]) might suffice for many applications, others may require more rigorous approaches like a Causal Forest or models from the `DoubleML` package, especially given the challenge of unobserved counterfactual values <a class="yt-timestamp" data-t="33:04:00">[33:04:00]</a>.