---
title: Causal AI and Personalization in ECommerce
videoId: xkx1tXLAP-o
---

From: [[causalpython]] <br/> 

Traditional recommender systems in machine learning often function as predictive or associative devices, aiming to identify the most suitable items based on correlations [01:34:00]. However, integrating [[causal_ai_and_machine_learning | causal inference]] into these systems shifts the focus from mere prediction to understanding and influencing user behavior [01:46:00]. This approach seeks to determine the *incremental impact* of a recommendation, specifically what action a customer would take *differently* if a particular recommendation were (or were not) presented [03:32:00].

## Benefits of Causal AI in Recommendations

[[causal_ai_applications_in_business_and_technology | Causal AI applications in business and technology]] aim to move beyond simply predicting what is most likely to happen, to understanding what would happen under different scenarios (counterfactual outcomes) [03:55:00]. This is crucial for:

*   **Driving Incremental Behavior Change**: Rather than recommending something a user would have found anyway, causal recommenders aim to incentivize actions the user wouldn't otherwise take [03:44:00]. This means focusing on innovative or trending options that truly change behavior, rather than just popular or frequently chosen ones [04:19:00].
*   **Optimizing Promotions and Discounts**: While offering discounts can expand the customer base and increase volumes, giving them to every customer is not financially viable [07:14:00]. [[causal_ai_applications_in_business_and_technology | Causal AI]] helps determine when a discount will genuinely change a customer's booking behavior versus when they would have booked anyway, thus preventing unnecessary costs [07:27:00]. This involves understanding the *counterfactual problem*: what would happen *with* and *without* the treatment (discount) [08:02:00].
    *   **Budget Constraints**: Promotions typically have a "trigger cost" – the cost is incurred only if the customer acts on the offer [09:21:00]. Within a fixed budget, the goal is to maximize incremental volumes (new customers/reservations) while controlling incremental costs and maintaining a specific return on investment (ROI) threshold [11:20:00]. This often leads to a "knapsack problem" of optimally allocating resources [12:36:00].
*   **Addressing Human Psychology**: Human behavior is often inconsistent and not purely rational [08:49:00]. For example, recommending a longer stay in Paris (which is statistically more common) might present an expensive price, scaring away customers. Recommending a single night, though less common, might present a cheaper price and encourage further exploration, leading to a booking [02:50:00]. [[causal_ai_and_machine_learning | Causal thinking]] helps uncover these counterintuitive patterns through experimentation, "hacking the mind of the people" [31:12:00].

> "You need to focus on something that actually going to change the outcome between A and B because I think like we're doing a lot of ab tests we try run hundreds or even thousand of ab tests in parallel sometimes and trying any change that we do on the website starting from copyrighting and ux to back fixes and obviously any machine learning models or something like that." <a class="yt-timestamp" data-t="05:50:49">[05:50:49]</a>

## [[challenges_in_integrating_causal_ai_in_business_settings | Challenges and Opportunities]]

Integrating [[causal_ai_and_machine_learning | causal inference]] with optimization and recommendation systems presents several [[causality_and_ai_challenges_and_opportunities | challenges]]:

*   **Noisy Data and Overfitting**: Real-world data is noisy and prone to overfitting and seasonality, making it harder to apply theoretical causal models [14:28:00].
*   **Dynamic Environments**: The business environment is constantly evolving. Problems change, new constraints emerge, and solutions need to be robust and adaptable rather than strictly optimal for a single point in time [14:54:00]. Continuous monitoring against a control group (holdout) is essential [16:34:00].
*   **Offline vs. Online Mismatch**: Models that perform well in offline evaluations (e.g., good uplift models, nice Q-curves) might fail in production due to fundamental biases or gaps in data collection or metric definitions [17:41:00].
*   **Cost of Online Testing**: Experimenting with [[causal_ai_applications_in_business_and_technology | causal AI]] online, especially with discounts, can be costly if implemented incorrectly, leading to sub-optimal results [17:59:00].
*   **Human Inconsistency**: Human psychology is not always consistent. An experiment that yields significant results on one platform or demographic might show inverse results on another [32:10:00]. This means external validity cannot be taken for granted [34:24:00].
*   **Conceptual Difficulty of Counterfactuals**: Thinking in terms of counterfactuals (what *would* have happened) is not intuitive, even for experienced professionals. Unlike predictive models, there are no "true labels" for counterfactual outcomes, making model evaluation, explainability, and monitoring more challenging [37:05:00].
*   **Terminology Gaps**: Different fields (e.g., economics, healthcare, computer science) often use different terminology for the same [[causal_ai_and_machine_learning | causal inference]] concepts, leading to communication and knowledge transfer gaps [01:03:33:00]. For example, "heterogeneous treatment effect" and "uplift modeling" refer to similar ideas [01:04:47:00].

## Strategies for Success

To overcome these [[causality_and_ai_challenges_and_opportunities | challenges]], effective strategies include:

*   **Continuous Experimentation (A/B Testing)**: Running hundreds or thousands of A/B tests in parallel for virtually any website change, including back fixes and machine learning solutions, is crucial for validating impact on key metrics [01:47:00], [05:53:00].
*   **Aligning Metrics and Data**: Ensuring that online and offline metrics and data collection processes are consistently defined and aligned is a fundamental, albeit "boring," step [01:40:00]. Establishing a simple baseline and comparing its offline and online measurements helps quantify any existing gaps [01:19:11:00].
*   **Robust Solutions via Portfolio Approach**: Instead of relying on a single optimal treatment, developing several diverse strategies (a portfolio) ensures that if one method fails, others can still be relied upon [02:00:58:00].
*   **Prioritizing Simple Models**: While complex models with many features might achieve good offline benchmarks, they are harder to deploy, maintain, and are more susceptible to overfitting and data drift in dynamic online environments [02:29:43:00]. Often, simpler models can have a significant business impact [02:00:30:00].
*   **Understanding Business Needs**: Technical teams must connect their work to actual product needs and expected business impact [02:48:50:00]. This involves understanding how a model's accuracy translates into tangible value for customers and the company [02:59:00]. Having product managers closely assigned to technical teams helps bridge this gap [02:15:11:00].
*   **Humble and Collaborative Culture**: Acknowledge that the world is complex and human behavior inconsistent [03:30:00]. A culture where teams openly share knowledge, learn from each other's successes, and collaborate on solutions is vital for continuous improvement [02:29:31:00].
*   **Iterative Development**: Start with simple solutions, learn from their deployment, and gradually introduce more complexity [04:47:00]. For promotions, this could mean starting with a simple "give or not give" decision, then adding levers like promotion type, discount level, timing, or specific items [04:56:00].

> "First of all understand the problem that you're trying to solve and only then pick up the tools that you need to solve" <a class="yt-timestamp" data-t="00:52:01">[00:52:01]</a>

## Key Concepts and Tools

*   **Uplift Modeling / Heterogeneous Treatment Effect**: This is a core [[causal_ai_and_machine_learning | causal AI]] approach in personalization, aiming to find the conditional average treatment effect (CATE) of a treatment [04:49:00]. It identifies which segments are most likely to benefit from a specific intervention (e.g., a discount) [04:22:00].
*   **Counterfactuals**: The "what if" scenarios that compare outcomes under different treatments for the same individual or group [03:35:00].
*   **A/B Testing**: The primary method for online evaluation of causal effects, comparing a treatment group to a control group [01:47:00].
*   **Knapsack Problem**: An optimization problem where one needs to select items to maximize value within a given capacity constraint, analogous to allocating limited promotional budgets [12:36:00].
*   **Q-curves**: Used in [[causal_ai_and_machine_learning | causal measurement]] to understand optimal threshold points for interventions [04:56:00].

Ultimately, the goal of [[causal_ai_and_its_connection_to_machine_learning | causal AI and its connection to machine learning]] in e-commerce personalization is to not just predict what a customer *might* want, but to understand what *will change their behavior* in a desired, measurable, and incrementally valuable way [02:20:00].