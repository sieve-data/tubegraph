---
title: The integration of expert knowledge in causal models
videoId: Hc3rIGmX59k
---

From: [[causalpython]] <br/> 

The role of assumptions is fundamental in [[causality_and_causal_models | causal models]] and [[causal_reasoning_and_structural_causal_models | causal inference]] generally [01:55]. Assumptions are not binary (true or false) but exist on a spectrum, like a slider that can be adjusted [00:02:02]. Understanding these assumptions, their "cost," and how to integrate expert knowledge can significantly improve the reliability and applicability of [[causal_reasoning_and_structural_causal_models | causal models]].

## The Cost of Assumptions

Assumptions are necessary for [[causal_reasoning_and_structural_causal_models | causal inference]] [02:14]. However, there is an often-ignored "cost" associated with these assumptions [02:29].

For example:
*   **Randomization**, the best assumption for establishing causality, comes at a high financial cost, such as millions or billions for pharmaceutical clinical trials [02:35]. This high cost, however, provides a high degree of certainty about the causal effect [02:48].
*   **Observational studies** often rely on assumptions like "no unmeasured confounding," which come "for free" in terms of direct monetary cost, but carry a higher risk of being wrong [02:57].

The heavier the assumption, the greater the risk [03:20]. Spending money can help reduce this risk [03:11]. For instance, at Harvard's public health school, significant funds are invested in discussing assumptions for observational studies, which are empirically unverifiable [04:17]. This discussion, involving paid professors and public engagement, helps reduce the risk of making wrong assumptions [04:42]. This concept aligns with the "no free lunch" idea in statistics and machine learning [05:00].

## Assumptions as a Range: Partial Identification

Traditionally, [[causality_and_causal_models | causal effect analysis]] often assumes a set of binary conditions (A, B, C) that, if true, yield a single "point identification" for a causal effect [05:38]. However, assumptions exist as a range, not a binary choice [05:09].

The concept of **partial identification** (or [[causal_model_evaluation_and_selection | causal bounds]]) offers a more flexible approach [05:59]. Instead of a single number, it provides a lower and upper bound on the true causal effect [06:16]. As more assumptions are added, these bounds become tighter and tighter, eventually collapsing to point identification [06:20]. This non-binary perspective allows for more nuanced discussion and justification of causal results, particularly when strong assumptions are hard to defend [08:49].

Partial identification has been explored since 1989 by researchers like Robins and Pearl, with significant contributions from economists like Charles Manski [07:42]. A "third generation" of partial identification research is emerging, driven by the need for more flexibility and weaker assumptions [08:28].

<div class="transclusion internal-embed is-loaded"><a class="internal-link" href="/_wiki/causal_model_evaluation_and_selection#Sensitivity%20Analysis%20vs.%20Partial%20Identification">[[causal_model_evaluation_and_selection#Sensitivity Analysis vs. Partial Identification | Sensitivity Analysis vs. Partial Identification]]</a></div>

## Integrating Expert Knowledge

Integrating expert knowledge is crucial for reducing the search space in [[causal_model_evaluation_and_selection | causal model evaluation and selection]], whether in [[causal_reasoning_and_structural_causal_models | causal discovery]], optimal experimentation, or structural Bayesian models [05:56]. Expert knowledge can be used to:

1.  **Refine Causal Graphs (DAGs)**: Experts can provide insights into relationships between variables, helping to define the [[causal_reasoning_and_structural_causal_models | causal graph]] [10:35]. While the causal graph might be subjective, it's the only inherently subjective part of partial identification [10:35].
2.  **Constrain the Problem Space**: In partial identification, expert knowledge acts like "slicing" a multi-dimensional "polytope" that represents the causal problem space [04:51]. Each assumption, derived from expert knowledge or data, removes parts of this space, tightening the bounds on the causal effect [04:51]. This process moves closer to "point identification" (a single point in the polytope) [05:07].
3.  **Guide Optimal Experimentation**: In fields like Material Science, expert knowledge (e.g., physics formulas) can guide where to collect new data points or conduct experiments, avoiding physically nonsensical areas in the parameter space [05:47]. This helps optimize the allocation of resources for data collection [05:31]. This is similar to geostatistical methods like kriging used in mining to intelligently explore a three-dimensional space [05:50]. [[interventions_and_causal_models | Bayesian optimization]] can also use uncertainty in predictions to decide where the next data point should be acquired, making experimentation more efficient than random or brute-force approaches [05:09].
4.  **Characterize Assumptions in Specific Methods**: For methods like synthetic control, which is widely used in marketing and time series analysis, expert knowledge can help characterize the untestable assumptions involved [03:05]. For instance, a project at Spotify involved characterizing synthetic control using [[causal_reasoning_and_structural_causal_models | DAGs]] to better understand its assumptions and enable sensitivity analysis [03:39].

### The Cost and Risks of Expert Knowledge

While invaluable, acquiring and integrating expert knowledge also has a cost [05:53]:
*   **Financial Cost**: Good experts can be expensive [05:56].
*   **Risk of Error**: Expert knowledge can be wrong, especially if the expert is not sufficiently skilled or if the context is misunderstood [05:07]. Bayesian approaches can partially mitigate this by allowing new, true data to eventually overrule incorrect expert knowledge, but this still requires data collection, which comes at a cost [05:22].

<a class="yt-timestamp" data-t="05:21:00">[05:21:00]</a>

> [!INFO] Quote on Expert Knowledge
> "We are already confidently moving away from Big Data and building models that just are supposed to explain and predict everything to a world where we like we have these expert they know these things better than a machine better than J GPT which hallucinates and we're going to bring those into those models." <a class="yt-timestamp" data-t="05:27:21">[05:27:21]</a>

## Embracing a Causal Future

The community has become more receptive to causality because traditional machine learning models often fail when the world changes systematically (e.g., during a pandemic) [02:52]. This highlights the need for models that incorporate causal thinking beyond mere correlation [02:52]. Math provides the formal language to characterize causality [02:51].

For those starting in [[causality_and_causal_models | causality]] or machine learning, it's advisable to focus on quality over quantity in learning [01:07:25]. Understanding established concepts like the instrumental variable model thoroughly can provide a strong foundation [01:07:36]. The core of causality is not inherently difficult; the challenge has often been in how it's taught [01:08:08]. The future is inherently [[causality_and_causal_models | causal]], and being explicit about cause and effect is crucial [01:16:04].

<a class="yt-timestamp" data-t="01:12:05">[01:12:05]</a>

> [!TIP] Message to the Causal Python Community
> "Think about the cost of your [[causality_and_causal_models | causal assumptions]]. Number one the step first is to question your assumptions and then think about what's the price what's the dollar tag on this and because they don't come for free some are cheaper some are more expensive and do just really consider when experimentation is a good choice. I think that's that is the most realistic perspective of [[causality_and_causal_models | causal inference]] you're going to get because we want to avoid a world where we just walking around with purely observational data sets. I'm okay with people doing observational studies to inform trials but I find it really hard to just do an observational study and never even think about how you would run an experiment for that to actually verify the results." <a class="yt-timestamp" data-t="01:12:09">[01:12:09]</a>

The advice for practitioners is to always question assumptions and consider their associated costs [01:12:15]. Focusing on justifiable assumptions, even if they require more investment in experimentation, leads to more robust and reliable causal conclusions [01:12:57].