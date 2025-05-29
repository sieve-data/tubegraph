---
title: Synthetic control in causal inference
videoId: CzL0pV6LyRk
---

From: [[causalpython]] <br/> 

Synthetic control is a methodology frequently used in [[Causal Inference and Identification | causal inference]] for situations where a "treatment" or intervention is administered at a very precise time to a specific unit, user, or population [03:41]. It helps to understand the effect of that intervention on the unit [03:52].

## When to Use Synthetic Control

This method is particularly useful in scenarios where:
*   A treatment or intervention has a clear, precise time of administration (e.g., "a new feature is released on this day" [03:47], "a user interacts with an artist in a very fixed way on this point in time" [04:43]) [04:52]. This allows for a clearly defined "before treatment" and "after treatment" period [04:00].
*   It is challenging to identify or measure all relevant confounders for adjustment [04:08], or some confounders might be hidden [05:00].
*   A set of "similar looking units" (donor units) exists that were *not* impacted by the treatment and can be used to construct a synthetic control [04:16], [05:03].

## Advantages of Synthetic Control

*   **Intuitiveness:** The method is considered very intuitive, making it easy for non-experts to grasp [05:10], [05:19].
*   **Confounder Handling:** It offers a "nice approach" when it's difficult to identify appropriate confounders for adjustment [04:12]. By finding similar-looking units, a synthetic control can be constructed, which helps infer the impact of the treatment [04:16], [04:27].

## Challenges and Methodologies

### Not Out-of-the-Box Causal Identification
Despite its intuitiveness, synthetic control does not provide [[Causal Inference and Identification | causal identification]] "out of the box" [05:39], [05:41]. The method was originally developed by economists, whose viewpoint sometimes differs from the [[Causal Inference and Identification | Pearlian SCM (Structural Causal Model)]] approach [06:06], [06:11], [06:15].

### Underlying Assumptions
Traditional synthetic control methods rely on semi-parametric assumptions, specifically that linear factor models generate the time series evolution of both the treated unit and similar units [07:07], [07:10]. This implies a commitment that the underlying linear factor model remains the same before and after the treatment, apart from the treatment's impact itself [07:31], [07:35]. This can be a "stringent set of assumptions" [07:43].

### Combining with DAGs and Non-Parametric Assumptions
To address these limitations and enable [[Role of assumptions in causal inference | sensitivity analysis]], researchers have explored combining synthetic control with the framework of directed acyclic graphs (DAGs) [05:51], [05:54].

A key step was to draw a DAG representing the synthetic control model, which had not been standard practice in the literature at the time [06:38], [06:51], [06:56]. This led to questions about the underlying graphical assumptions [06:43].

By framing synthetic control within a non-parametric set of assumptions, it becomes possible to identify the counterfactual necessary for causal effect estimation [08:08], [08:21]. This involves using ideas from [[Role of reinforcement learning in causal inference | proximal causal inference]], where it's assumed that underlying latents drive the evolution of units [08:34], [08:41]. Instead of assuming specific parameterizations like linear factors, it's assumed that observed drivers are proxies for these underlying latents [08:57], [09:04].

This approach allows for:
*   Deriving general identifiability results without relying on linearity [09:19], [09:22].
*   Building sensitivity analysis around how wrong estimates might be if assumptions are slightly violated or misspecified [09:29], [09:33], [09:47]. This helps to gain confidence in causal estimates [09:52], [10:01].

This marriage of the [[Causal Inference and Identification | SCM Pearlian approach]] with econometrics ideas allows for general [[Role of assumptions in causal inference | sensitivity analysis]] and increased confidence in synthetic control estimates [09:54], [10:03].

## Building Trust in Causal Models

While deep learning practitioners may view the numerous assumptions in causal methods as a weakness [10:14], [10:20], thinking deeply about these assumptions upfront is considered a bonus [10:48]. It forces a thorough consideration of whether the data generation process for a specific problem aligns with the assumptions [10:52].

When assumptions are violated (e.g., not measuring all relevant confounders [11:11]), methods can be used to gain confidence. For instance, by leveraging domain knowledge about the most important confounders, one can set bounds on how much the effect estimate might change if other, less important confounders were missed [11:25], [11:30], [11:47], [11:58]. Even if the causal effect cannot be precisely point-identified, setting upper and lower bounds can still provide valuable insights, especially if they do not intersect zero [12:07], [12:12], [12:15]. This ability to propagate uncertainties about assumptions to uncertainties about causal effect estimates is seen as a feature, not a bug, of [[Causal Inference and Identification | causal inference]] [12:41], [12:46], [13:31].