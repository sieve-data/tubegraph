---
title: Interventions and causal models
videoId: UQ8j-DEkB98
---

From: [[causalpython]] <br/> 

In the realm of [[Causality and Causal Models | causality]], interventions are paramount for understanding and predicting how systems behave. Causal knowledge is essential to distinguish between mere prediction and scenarios where an intervention can actively change a system [02:15:18]. For example, knowing that giving people a drug makes them more likely to recover is a causal claim, unlike just observing that people who take a drug are more likely to recover [02:29:17].

## The Nature of Causality and Interventions

From a philosophical perspective, the understanding of [[Causality and Causal Models | causality]] is intrinsically linked to methodology, particularly the ability to intervene on a system [02:46:46]. The effectiveness of causal methods, such as those using the "do-operator," is presumed to stem from inherent features of the world, allowing for insights into the nature of causation itself [02:29:29].

While some 20th-century philosophers, like Bertrand Russell, argued that [[Causality and Causal Models | causality]] was a "relic of the bygone age" and not relevant to fundamental physics, the reality is that causal knowledge is widely needed and used across various sciences, including epidemiology, sociology, and industry [01:10:07]. The scientific legitimacy of [[Causality and Causal Models | causation]] should not be questioned based solely on its role (or perceived lack thereof) in fundamental physics [01:40:02].

## Time Scale and Causal Relationships

A crucial aspect of [[Abstractions and Causal Models | causal models]] is their relativity to time and spatial scales [03:02:54]. The relationship between variables can appear different depending on the observation timescale.

### Everyday Examples
*   **Flossing and Bleeding Gums**: If you don't floss and start, your gums might bleed that day. However, if you floss daily for a week, they will stop bleeding. Both statements are true at different time scales [04:08:10].
*   **Crops and Rainfall**: Over a short period, rainfall influences crop growth, and is considered an "exogenous variable" (not influenced by other variables in the model) [11:14:17]. However, over 100 to 200 years, agriculture can influence climate, creating a feedback loop where crop amounts can affect future rainfall [11:58:01]. These different causal representations are appropriate for their respective time scales [12:56:04].

This implies that when making a causal claim or building a [[Causal reasoning and structural causal models | causal model]], assumptions about the system's time scale are implicitly built in [04:51:00]. Extrapolating a model across inappropriate time scales can lead to incorrect conclusions [13:12:05].

### Confounders and Background Context
Long-term factors are not necessarily confounders if they remain constant over the observed period [09:06:08]. For instance, the capitalist economy in a study of trading behavior might be a constant background condition influencing observations, but not a confounder that needs to be measured and controlled if it doesn't vary [08:31:00]. In such cases, these factors become preconditions for the model's application rather than variables within it [09:11:00].

Conversely, assuming the absence of hidden confounders is a strong assumption in causal modeling [06:31:00]. Experiments, when possible, can help remove the influence of confounders by design [06:39:00].

## Interventions in Dynamic Systems

The concept of intervention needs to be nuanced when considering systems over time.

### "Intervening and Letting Go"
A paper titled "Intervening and Letting Go" explored how interventions behave in dynamic systems, particularly thermodynamic ones like an ideal gas in a container [04:57:00].
*   **Ideal Gas System**: In a system with a movable piston, pressure and temperature cause volume. If you fix the volume by inserting a pin, the system behaves like a sealed container where volume and temperature cause pressure [04:54:00].
*   **The Puzzle**: The standard "do-operator" for interventions doesn't fully capture this shift. Sticking a pin in looks like an intervention, but the resulting causal relationships don't align with expectations based on the operator alone [04:57:00]. This is because the intervention (clamping volume) destroys the system's ability to reach its previous equilibrium, effectively changing the system's inherent feedback loops [04:40:00].

### Types of Interventions
*   **Clamp Intervention**: Holds a variable fixed indefinitely [49:58]. This type of intervention can alter the system's ability to reach its natural equilibrium [04:46:00].
*   **Shock Intervention**: Influences a variable only at one time step [05:06:00].
*   **Letting Go**: This refers to removing a constraint or intervention, allowing the system to revert to its natural dynamics [04:20:00]. The current structural causal model formalism has a "blind spot" for this operation, as it primarily focuses on imposing new constraints [04:42:00].

In real-world applications, interventions are often complex, lasting for different durations and amounts of time [04:43:00]. Understanding these different intervention types and their temporal aspects is crucial for [[Challenges and methodologies in causal inference | causal inference]], especially when the outcome of interest is a stable state or a change in system stability, such as administering chemotherapy to change a patient's bodily state and immune system's ability to eradicate cancer [04:50:00].

## Bridging Dynamic Systems and Causal Frameworks

Recent work, particularly from Joris Mooij's lab at the University of Amsterdam, aims to bridge the gap between dynamic models (often described by differential equations) and the Judea Pearl framework of [[Causal reasoning and structural causal models | structural causal models]] [05:32:00]. Dynamic causal models, inspired by the work of Herbert Simon and Yumi Iwasaki, help understand the relationship between causal representations at equilibrium and those away from equilibrium [05:27:00]. This integration shows that standard calculus operations (like time derivatives and integration) can appear in causal models, suggesting a generalization of the standard causal framework to certain types of dynamic systems [05:54:00].

## Practical Implications for Causal Modeling

### Embracing Being Wrong
Many practitioners fear making mistakes when building causal graphs (DAGs) [03:53:00]. However, explicitly building a model, even if it turns out to be wrong, provides a valuable learning opportunity to understand where the model breaks down and how to improve it [03:30:00]. Without explicit models, assumptions often remain hidden in the "statistical subconscious," preventing learning [03:39:00].

### Importance of Causal Assumptions
If the goal is to make causal claims, model the effects of interventions, or interpret invariant probabilistic relationships, then causal assumptions and models are necessary [03:41:00]. [[The integration of expert knowledge in causal models | Causal models]] make these assumptions systematic and explicit, clearly spelling out what is needed to reach a desired conclusion [03:11:00].

This stands in contrast to the "Big Data Revolution" idea that merely collecting enough data can solve any problem [05:11:00]. [[Causality and Causal Models | Causality]] is not about blindly throwing data into a machine but about making assumptions to manage the complexity of the world in a localized way [05:17:00].

## Future Directions and Outlook

The field of [[Causality and Causal Models | causality]] is still in its early stages of development, with significant work remaining, particularly in understanding the conditions under which [[Causal reasoning and structural causal models | causal models]] apply [01:19:56]. Researchers are exploring how facts about exogeneity (variables not caused by others in the system) relate to time scale, which informs the applicability of [[Causal reasoning and structural causal models | causal models]] [01:46:00].

The interaction between academic and industrial causal researchers is crucial to foster progress. By building bridges between different perspectives and "schools of thought" (e.g., potential outcomes vs. graphical models, epidemiology vs. econometrics vs. computer science), the field can move forward, preventing valuable solutions from remaining in isolated niches [01:10:28].

Ultimately, [[Causality and Causal Models | causality]] is not just a passing trend but a valuable tool, especially in industry, where problems often involve interventions rather than purely predictive tasks [02:11:00]. The challenge lies not only in developing tools but also in enabling their practical implementation by understanding and overcoming the incentives and systemic barriers that prevent their widespread adoption [02:22:00].

### Recommended Resources:
*   **Felix Elwert**: Handbook for [[Causality and Causal Models | Causality]] (chapter covers confounding, d-separation, endogenous selection bias, time-varying treatments). [01:13:30]
*   **Felix Elwert & Chris Winship**: Paper on endogenous selection bias (conditioning on a collider). [01:14:10]
*   **Frederick Eberhardt**: Short introduction to [[Tools and frameworks for causal analysis | causal inference algorithms]] (c. 2012), covering traditional and machine learning algorithms. [01:14:39]
*   **Jonas Peters, Dominik Janzing, & Bernhard Schölkopf**: Textbook on [[Tools and frameworks for causal analysis | causal inference]]. [01:15:53]
*   **Michael Nielsen**: Website introduction to d-separation. [01:16:07]
*   **Naftali Weinberger**: Stanford Encyclopedia of Philosophy article on Simpson's Paradox, relating causal modeling to earlier philosophical theories. [01:16:33]