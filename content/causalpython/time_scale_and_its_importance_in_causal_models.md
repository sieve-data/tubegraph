---
title: Time scale and its importance in causal models
videoId: UQ8j-DEkB98
---

From: [[causalpython]] <br/> 

Dr. Naftali Reinberger, a philosopher of science, emphasizes that understanding causality requires considering the time scale at which a system is observed and modeled <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>. This perspective is crucial for developing accurate [[structural_causal_models_and_graph_theory | causal models]] and interpreting their findings.

## Causality's Enduring Scientific Legitimacy

Reinberger refutes the iconic British philosopher Bertrand Russell's early 20th-century assertion that "causality is a relic of the bygone age" <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>. He argues that causality is demonstrably legitimate and useful in various scientific disciplines, including epidemiology, sociology, and industry, where causal knowledge is essential <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. While causality's role in fundamental physics may remain a subject of debate, its practical utility in other sciences is undeniable <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

## Time and Spatio-Temporal Scale in Scientific Modeling

For any scientific claim or phenomenon study, time and spatio-temporal scale are crucial <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.
*   **Physics**: Different behaviors are observed at different scales; for example, quantum scale versus higher scales where Newtonian physics is a better approximation <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Biology**: Cell biology and systems biology involve different relationships <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.

This concept, though general to science, has not been systematically explored in the causal context <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Reinberger's work on this topic is inspired by Herbert Simon, particularly the 1994 paper "Causality and Model Abstraction" by Yumi Iiwasaki and Herbert Simon <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### The Flossing Example: Different Causal Relations at Different Scales
A simple everyday example highlights this:
*   A dentist tells a patient, "Your gums bleed because you don't floss." <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>
*   The patient might respond, "I don't floss because it makes my gums bleed." <a class="yt-timestamp" data-t="00:04:13">[00:04:13]</a>

Both statements are true depending on the time scale <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>. If someone starts flossing after not having done so, their gums will bleed that day (short-term effect) <a class="yt-timestamp" data-t="00:04:24">[00:04:24]</a>. However, if they floss daily for a week, their gums will stop bleeding (long-term effect) <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. This illustrates how a causal representation inherently builds in assumptions about the time scale of the system being considered <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>.

## Confounders and Long-Term Factors

In [[challenges_in_evaluating_causal_models | causal models]], hidden confounders are a common concern <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. Reinberger explains that assuming confounders are not present is a strong assumption <a class="yt-timestamp" data-t="00:06:31">[00:06:31]</a>. Experiments can, by design, remove their influence <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

The relationship between time scale and confounders is subtle <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. Causal claims are often relative to a concrete system and its specific context <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. Variables that remain constant over a long period might not be considered confounders, but rather background context, even if they influence the system <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. For instance, studying trading behavior in a capitalist economy over centuries would treat "capitalist country with a free market" as a constant background factor, not a confounder, because it's a precondition for the observed dynamics <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

### Rainfall and Crop Growth Example: Exogenous Variables and Feedback Loops
The example of rainfall, crops planted, and crops grown illustrates how variables can appear exogenous at one time scale but not another <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>.
*   **Short Time Scale**: Rainfall is considered an exogenous variable (it doesn't depend on crops grown) because crop growth does not influence rainfall in the short term <a class="yt-timestamp" data-t="00:11:17">[00:11:17]</a>.
*   **Long Time Scale**: Over centuries, agriculture (amount of crops grown year after year) can influence climate and future rainfall, creating a feedback loop <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

Both representations (one with rainfall as exogenous, one with a feedback loop) are appropriate at their respective time scales <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>. The problem arises from extrapolating across time scales <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. For example, a [[application_of_causal_models_in_climate_science | climate scientist]] studying long-term global warming effects cannot use a model where crop growth has no effect on rainfall <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

## Time Scale, Complex Systems, and Emergence

The discussion of time scales naturally extends to complex systems and [[philosophical_aspects_of_causality | emergence]] <a class="yt-timestamp" data-t="00:15:45">[00:15:45]</a>. Reinberger argues that many discussions about emergence are understood by acknowledging that causal relationships are relative to a time scale <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>. A system might appear chaotic at a lower spatio-temporal scale, but patterns and regularities "emerge" at a higher level of description <a class="yt-timestamp" data-t="00:16:42">[00:16:42]</a>. This is not "spooky" but rather a natural consequence of different patterns of behavior existing at different scales <a class="yt-timestamp" data-t="00:19:57">[00:19:57]</a>.

An example is a room regulated by a thermostat <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>:
*   Turning on an oven makes the room hotter in 5 minutes (short-term effect) <a class="yt-timestamp" data-t="00:19:02">[00:19:02]</a>.
*   An hour later, the room is not hotter because the thermostat equilibrates the temperature (long-term effect) <a class="yt-timestamp" data-t="00:19:06">[00:19:06]</a>.
These models are not contradictory; they describe behavior at different time scales <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.

## The Methodological Approach to Causality

Reinberger defines causality not by cataloging "causal stuff" in the universe, but methodologically <a class="yt-timestamp" data-t="00:21:04">[00:21:04]</a>. Influenced by Nancy Cartwright's "Causal Laws and Effective Strategies," he stresses that causal knowledge is needed to distinguish mere prediction from effective intervention <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. For instance, knowing that giving a drug *causes* recovery, rather than just being correlated with it, is crucial <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>. This perspective underpins the development of [[structural_causal_models_and_causal_discovery | causal discovery algorithms]] based on interventions <a class="yt-timestamp" data-t="00:21:47">[00:21:47]</a>.

He emphasizes that this methodological focus is not merely pragmatic or epistemological; the success of causal methods implies underlying features of the world that make them work <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>.

## Interventions and Time Scale: "Intervening and Letting Go"

Reinberger's paper "Intervening and Letting Go" (co-authored with Ruben Stern and Dan H. M. Hausman) explores how the nature of interventions changes with time scale <a class="yt-timestamp" data-t="00:40:59">[00:40:59]</a>.

### The Ideal Gas System Example
Consider an ideal gas in a container, governed by the ideal gas law (pressure x volume is proportional to temperature) <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>.
*   **Sealed Container (Fixed Volume)**: Volume and temperature cause pressure <a class="yt-timestamp" data-t="00:41:42">[00:41:42]</a>.
*   **Movable Piston (Constant Pressure)**: Pressure and temperature cause volume <a class="yt-timestamp" data-t="00:41:54">[00:41:54]</a>.

The puzzle arises when changing the system from a movable piston to a sealed container by "sticking a pin" to fix the volume <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>. This act, resembling an intervention, does not yield the expected results if interpreted solely by the `do` operator in typical [[structural_causal_models_and_graph_theory | causal models]] <a class="yt-timestamp" data-t="00:42:57">[00:42:57]</a>.

Denver Dash's work, focusing on the dynamics of the system, provides insight <a class="yt-timestamp" data-t="00:43:37">[00:43:37]</a>. A dynamic representation (like Iiwasaki and Simon's work) shows a feedback loop between pressure and volume as the piston expands or contracts away from equilibrium <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>.

The key insight is that when considering a system at a longer time scale, or assuming it has reached equilibrium, you are not considering its evolution over time <a class="yt-timestamp" data-t="00:46:08">[00:46:08]</a>. An intervention in this context, often called a "clamp intervention," holds a variable fixed indefinitely <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>. This type of intervention can destroy the system's ability to reach a certain equilibrium, as it prevents the feedback loop from operating <a class="yt-timestamp" data-t="00:46:40">[00:46:40]</a>.

Reinberger argues that neither equilibrium model (sealed container vs. movable piston) is inherently superior <a class="yt-timestamp" data-t="00:47:00">[00:47:00]</a>. While one might predict all interventions, each is true for a different equilibrium state <a class="yt-timestamp" data-t="00:47:07">[00:47:07]</a>. The failure of the movable piston model to predict the "pin insertion" is paralleled by the sealed container model's inability to predict what happens when the pin is *removed* (i.e., "letting go" of the constraint) <a class="yt-timestamp" data-t="00:47:14">[00:47:14]</a>. This highlights a "blind spot" in the standard [[structural_causal_models_and_graph_theory | structural causal model]] formalism <a class="yt-timestamp" data-t="00:47:45">[00:47:45]</a>.

### Implications for Practicing Scientists
When time is introduced into causal models, it changes how interventions are conceived <a class="yt-timestamp" data-t="00:49:27">[00:49:27]</a>. One can distinguish between:
*   **Clamp intervention**: Holds a variable in place indefinitely <a class="yt-timestamp" data-t="00:49:58">[00:49:58]</a>.
*   **Shock intervention**: Influences a variable at only one time step <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>.
*   Various repeated shocks at different intervals <a class="yt-timestamp" data-t="00:50:10">[00:50:10]</a>.

These distinctions are crucial because real-world interventions have different durations and persistence <a class="yt-timestamp" data-t="00:51:51">[00:51:51]</a>. For example, chemotherapy aims to change the body's entire system state and influence feedback loops to bring it to a new equilibrium <a class="yt-timestamp" data-t="00:51:14">[00:51:14]</a>.

## Bridging Dynamical Systems and Causal Models

Reinberger acknowledges the exciting work being done by the lab of Joris Mooij at the University of Amsterdam on this topic <a class="yt-timestamp" data-t="00:53:00">[00:53:00]</a>. Dynamic [[time_series_designs_and_causal_inference | causal models]] allow for understanding the relationship between causal representations at equilibrium and away from equilibrium <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>. These models incorporate calculus operations like time derivatives and integration, showing a generalization of the standard causal framework <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>. This bridge helps understand how [[structural_causal_models_and_graph_theory | causal graphs]] and their interpretations can be extended to dynamic systems, maintaining continuity with the work of pioneers like Herbert Simon <a class="yt-timestamp" data-t="00:55:21">[00:55:21]</a>.

## The Big Data Revolution and Causality

Reinberger is suspicious of the idea from the early 2010s "Big Data Revolution" that collecting enough data alone can solve any problem without causal assumptions <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>. He argues that causality is not about "throwing it into a machine or a grinder and getting a result" <a class="yt-timestamp" data-t="00:57:04">[00:57:04]</a>. Instead, it's about making assumptions to simplify the world and interact with it in a local, manageable way <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>.

While acknowledging that technological evolution can sometimes yield unexpected solutions (e.g., large language models not explicitly programmed with grammatical rules but still performing tasks), he maintains that causal reasoning offers a different, valuable approach <a class="yt-timestamp" data-t="00:57:50">[00:57:50]</a>. Causal reasoning is essential for a "limited being operating at a particular time scale" who doesn't need to know "everything happening in the universe" to predict local events <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>.

## Advice for Aspiring Causal Practitioners

For those starting in causality, Reinberger recommends:
*   **Find an Entry Point**: Identify an aspect that personally interests you and connects to your other interests <a class="yt-timestamp" data-t="01:05:28">[01:05:28]</a>. This could be a specific debate, an algorithm, or a philosophical concept <a class="yt-timestamp" data-t="01:06:16">[01:06:16]</a>.
*   **Embrace Iteration**: Building a model, even if it's wrong, is a learning opportunity to modify and improve it <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>. This [[iterative_approach_in_building_causal_models | iterative approach]] is more fruitful than avoiding explicit models due to fear of being wrong <a class="yt-timestamp" data-t="00:35:55">[00:35:55]</a>.
*   **Understand Assumptions**: Causal models are transparent about their assumptions, particularly through missing arrows (representing lack of direct causal relationship or common cause) <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>. This clarity helps understand when and why models break down <a class="yt-timestamp" data-t="00:40:01">[00:40:01]</a>. As Nancy Cartwright said, "no causes in, no causes out" – causal assumptions are necessary to derive causal knowledge <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>.

His background in Talmudic literature, a legal style of analysis, cultivated a flexibility of thought that helps him triangulate different sources and embrace the idea that models can be wrong but still provide learning <a class="yt-timestamp" data-t="01:00:22">[01:00:22]</a>. Similarly, studying Islamic Sufi texts fostered an appreciation for reconciling personal experience with broader system functions <a class="yt-timestamp" data-t="01:03:00">[01:03:00]</a>.

## Message to the Causal Community

Reinberger encourages the causal community to ask more fundamental questions beyond just algorithmic development <a class="yt-timestamp" data-t="01:08:08">[01:08:08]</a>. He calls for a deeper understanding of the "conditions of causal representation" – the types of systems to which causal models apply <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. Understanding time scale as a determinant of exogeneity, for instance, clarifies the conditions under which causal models are valid <a class="yt-timestamp" data-t="01:19:46">[01:19:46]</a>.

He argues against defensiveness when model limitations are pointed out, seeing it as an opportunity to understand where models break down and how to fix them <a class="yt-timestamp" data-t="01:20:04">[01:20:04]</a>.

## The Future of Causality

While declining to predict industry trends, Reinberger asserts that causality is a valuable tool because most problems, even seemingly predictive ones, involve the desire to intervene <a class="yt-timestamp" data-t="01:21:21">[01:21:21]</a>. People care about invariant correlations, which traditional statistics alone cannot provide <a class="yt-timestamp" data-t="01:21:44">[01:21:44]</a>. The challenge lies in implementation and incentives, ensuring that causal tools can be easily integrated into existing workflows and recognized by publishing venues <a class="yt-timestamp" data-t="01:22:25">[01:22:25]</a>. This may require "change management experts" more than additional causality specialists <a class="yt-timestamp" data-t="01:23:36">[01:23:36]</a>.

## Recommended Resources for Starting with Causality

*   **Felix Elwert (Sociologist, Wisconsin)**: Chapter in a handbook for causality (easy to find online), covering confounding, d-separation, endogenous selection bias, and time-varying treatments <a class="yt-timestamp" data-t="01:13:30">[01:13:30]</a>.
*   **Felix Elwert & Christopher Winship (Harvard)**: Paper on endogenous selection bias (conditioning on a collider) <a class="yt-timestamp" data-t="01:14:10">[01:14:10]</a>.
*   **Frederick Eberhardt (Caltech)**: A short introduction (around 10-12 pages, ~2012) to [[applications_of_generative_modeling_in_causality | causal inference algorithms]], including traditional and machine learning approaches (e.g., solving the two-variable problem where traditional algorithms fail) <a class="yt-timestamp" data-t="01:14:39">[01:14:39]</a>.
*   **Jonas Peters, Dominik Janzing, Bernhard Schölkopf**: Textbook for more detailed information on causal inference algorithms <a class="yt-timestamp" data-t="01:15:53">[01:15:53]</a>.
*   **Michael Nielsen**: Introduction to d-separation on his website, noted as the most accessible <a class="yt-timestamp" data-t="01:16:07">[01:16:07]</a>.
*   **Naftali Reinberger**: Article on Simpson's Paradox in the Stanford Encyclopedia of Philosophy, which connects causal modeling methods to earlier philosophical theories <a class="yt-timestamp" data-t="01:16:33">[01:16:33]</a>.
*   **Judea Pearl**: "The Book of Why" for an accessible landscape overview <a class="yt-timestamp" data-t="01:06:10">[01:06:10]</a>.

More about Dr. Reinberger's work can be found on his website or his Twitter account (@NaftaliReinberg), where his pinned tweet provides links to relevant papers <a class="yt-timestamp" data-t="01:17:44">[01:17:44]</a>.