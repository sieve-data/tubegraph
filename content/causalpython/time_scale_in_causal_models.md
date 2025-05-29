---
title: Time scale in causal models
videoId: UQ8j-DEkB98
---

From: [[causalpython]] <br/> 

Dr. Naftali Weinberger, a philosopher of science, emphasizes that [[causality_and_causal_models | causality]] is not a relic of a bygone age, but rather a concept of extreme usefulness in modern science and industry <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>. His work particularly focuses on the significance of considering [[time_series_causal_discovery | time scales]] and other spatiotemporal scales when developing and applying [[causal_reasoning_and_structural_causal_models | causal models]] <a class="yt-timestamp" data-t="02:44:00">[02:44:00]</a>, <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

## The Pervasive Influence of Time Scale

Weinberger argues that time scale, and scale more generally, is crucial for any scientific model or phenomenon studied <a class="yt-timestamp" data-t="02:52:50">[02:52:50]</a>. Just as physicists recognize different behaviors at quantum versus Newtonian scales, or biologists differentiate between cell and systems biology, causal relationships also vary depending on the time scale at which a system is considered <a class="yt-timestamp" data-t="03:06:06">[03:06:06]</a>. This systematic consideration of scale in the causal context has not been widely discussed <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>, despite being inspired by Herbert Simon's work, particularly his 1994 paper with Yumi I wasaki, "[[Abstractions and Causal Models | Causality and Model Abstraction]]" <a class="yt-timestamp" data-t="03:40:00">[03:40:00]</a>.

### The Flossing Example
A simple everyday example illustrates this point:
The statement "flossing makes my gums bleed" versus "your gums bleed because you don't floss" <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>.
*   **Short Time Scale**: If someone unused to flossing starts, their gums *will* bleed on that day <a class="yt-timestamp" data-t="04:25:00">[04:25:00]</a>.
*   **Long Time Scale**: If they floss consistently for a week, their gums will stop bleeding <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

These are not contradictions but different causal relationships valid at different time scales <a class="yt-timestamp" data-t="04:41:00">[04:41:00]</a>. Therefore, making a causal claim or building a [[causal_reasoning_and_structural_causal_models | causal model]] inherently incorporates assumptions about the time scale of the system <a class="yt-timestamp" data-t="04:56:00">[04:56:00]</a>.

## Hidden Confounders and Time Scales

Concerns about hidden confounders in [[evaluating_causal_models_in_practice | evaluating causal models in practice]] often lead to two ways of thinking: variables known but hard to measure, or variables operating on large time scales <a class="yt-timestamp" data-t="05:11:00">[05:11:00]</a>. Weinberger suggests neither option fully captures the issue, as not allowing for hidden confounders is a strong assumption <a class="yt-timestamp" data-t="06:31:00">[06:31:00]</a>.

Regarding time scales and confounders, he highlights that a causal claim is always relative to a concrete system and its background conditions <a class="yt-timestamp" data-t="07:17:00">[07:17:00]</a>. Variables that are constant over the observed time scale might be considered background context rather than confounders, influencing the system but not varying to cause problems within the model's scope <a class="yt-timestamp" data-t="08:26:00">[08:26:00]</a>. For example, capitalism as a background factor in a study of trading behavior over centuries <a class="yt-timestamp" data-t="08:34:00">[08:34:00]</a>.

### The Rainfall and Crops Example
A classic example from Simon and Werr illustrates how time scale affects the perception of variables as exogenous:
*   **Short Time Scale**: Rainfall is typically seen as an exogenous variable for crop growth, as crop growth does not influence rainfall <a class="yt-timestamp" data-t="10:49:00">[10:49:00]</a>.
*   **Long Time Scale**: Over centuries, agriculture (crop growth across wide areas) can influence climate and future rainfall, creating a feedback loop <a class="yt-timestamp" data-t="11:49:00">[11:49:00]</a>.

Both models (rainfall as exogenous at short scales; a feedback loop at long scales) are appropriate at their respective time scales <a class="yt-timestamp" data-t="13:02:00">[13:02:00]</a>. Problems arise when extrapolating across time scales without adjusting the model <a class="yt-timestamp" data-t="13:12:00">[13:12:00]</a>.

## Emergence and Causality in Complex Systems

The discussion of scales naturally leads to complex systems and phenomena like emergence <a class="yt-timestamp" data-t="15:45:00">[15:45:00]</a>. Weinberger suggests that understanding [[causality_and_causal_models | causal relationships]] as relative to a time scale helps to demystify emergence <a class="yt-timestamp" data-t="16:30:00">[16:30:00]</a>. Patterns of regularity can emerge at a higher level or different scale, even if a lower level appears chaotic <a class="yt-timestamp" data-t="16:51:00">[16:51:00]</a>.

He clarifies that when considering a system at different scales, one is essentially considering different "objects" – zooming in and zooming out changes the focus <a class="yt-timestamp" data-t="18:45:00">[18:45:00]</a>.

### The Thermostat Example
If an oven is turned on:
*   **Short-term (5 minutes)**: The room becomes hotter <a class="yt-timestamp" data-t="19:04:00">[19:04:00]</a>.
*   **Longer-term (1 hour)**: The room does *not* become hotter because the thermostat equilibrates the temperature <a class="yt-timestamp" data-t="19:06:00">[19:06:00]</a>.

There is no contradiction or metaphysical puzzle; these are different patterns of behavior at different time scales <a class="yt-timestamp" data-t="19:17:00">[19:17:10]</a>. The universe clearly exhibits different patterns of behavior at different spatiotemporal scales <a class="yt-timestamp" data-t="20:20:00">[20:20:00]</a>.

## Defining Causality: The Interventionist Approach

Weinberger views [[causality_and_causal_models | causality]] methodologically, influenced by Nancy Cartwright's "Causal Laws and Effective Strategies" <a class="yt-timestamp" data-t="21:07:00">[21:07:00]</a>. The core idea is that [[causality_and_causal_models | causal knowledge]] is needed to understand the difference between mere prediction and effective intervention <a class="yt-timestamp" data-t="21:15:00">[21:15:00]</a>. For example, knowing that giving a drug *causes* recovery, rather than just correlating with it <a class="yt-timestamp" data-t="21:27:00">[21:27:00]</a>.

[[Causal reasoning and structural causal models | Causal models]] are fundamentally built on assumptions. The "arrows missing" from a [[causal_reasoning_and_structural_causal_models | causal model]] (e.g., a Directed Acyclic Graph or DAG) represent strong assumptions about the absence of direct causal relationships or common causes <a class="yt-timestamp" data-t="34:44:00">[34:44:00]</a>. These "background assumptions" are what make [[causal_reasoning_and_structural_causal_models | causal models]] work <a class="yt-timestamp" data-t="35:05:00">[35:05:00]</a>. The benefit of explicit [[causal_reasoning_and_structural_causal_models | causal models]] is that they clarify these assumptions, making it easier to learn when the model is wrong and how to improve it <a class="yt-timestamp" data-t="38:09:00">[38:09:00]</a>, <a class="yt-timestamp" data-t="38:53:00">[38:53:00]</a>.

## Intervening and Letting Go

Weinberger's paper "Intervening and Letting Go" explores the distinction between different types of interventions in [[causality_in_dynamical_systems | dynamical systems]] and their implications for [[causal_reasoning_and_structural_causal_models | causal models]] <a class="yt-timestamp" data-t="40:39:00">[40:39:00]</a>, <a class="yt-timestamp" data-t="40:59:00">[40:59:00]</a>.

### The Ideal Gas System Example
Consider a gas in a container governed by the ideal gas law (pressure × volume ∝ temperature):
*   **Sealed Container (Fixed Volume)**: Volume and temperature are causes of pressure <a class="yt-timestamp" data-t="41:42:00">[41:42:00]</a>.
*   **Movable Piston (Constant Pressure)**: Pressure and temperature are causes of volume <a class="yt-timestamp" data-t="41:54:00">[41:54:00]</a>.

A puzzle arises when transforming between these setups <a class="yt-timestamp" data-t="42:09:00">[42:09:00]</a>. If you start with a movable piston and then "fix" the volume (e.g., by inserting a pin), it behaves like a sealed container <a class="yt-timestamp" data-t="42:25:00">[42:25:00]</a>. This intervention does not yield the result expected by the standard `do` operator for intervention in the initial movable piston model <a class="yt-timestamp" data-t="42:40:00">[42:42:40]</a>.

This highlights that [[causal_reasoning_and_structural_causal_models | causal models]] are relative to a setup <a class="yt-timestamp" data-t="41:37:00">[41:37:00]</a>. Looking at the dynamics (how the system moves towards equilibrium) reveals a feedback loop between pressure and volume <a class="yt-timestamp" data-t="44:17:00">[44:17:00]</a>. A "clamp intervention," which holds a variable fixed indefinitely, destroys the system's ability to operate its natural feedback loop to reach equilibrium <a class="yt-timestamp" data-t="46:26:00">[46:26:00]</a>, <a class="yt-timestamp" data-t="46:40:00">[46:46:40]</a>.

The paper argues that preferring one equilibrium model over another is unfounded <a class="yt-timestamp" data-t="47:00:00">[47:00:00]</a>. While one model might predict more interventions, each is true for a different equilibrium state <a class="yt-timestamp" data-t="47:07:00">[47:07:00]</a>. The "blind spot" of the [[causal_reasoning_and_structural_causal_models | structural causal model]] formalism is its lack of an operation for "letting go" (removing a constraint) <a class="yt-timestamp" data-t="47:42:00">[47:42:00]</a>.

### Types of Interventions
When considering variables measured repeatedly over time, interventions can be distinguished by their duration:
*   **Clamp intervention**: Holds a variable in place indefinitely <a class="yt-timestamp" data-t="49:58:00">[49:58:00]</a>.
*   **Shock intervention**: Influences at only one time step <a class="yt-timestamp" data-t="50:06:00">[50:06:00]</a>.
*   **Repeated shocks**: Influences at different intervals <a class="yt-timestamp" data-t="50:10:00">[50:10:00]</a>.

In real-world scenarios, interventions (causes) and their observed effects occur over varying durations <a class="yt-timestamp" data-t="51:51:00">[51:51:00]</a>. For example, chemotherapy aims to change the entire state and stability properties of a system to bring it to a new equilibrium <a class="yt-timestamp" data-t="51:14:00">[51:14:00]</a>.

## Bridging Dynamical Systems and Causal Frameworks

There is exciting work, particularly from the University of Amsterdam, on building bridges between [[causality_in_dynamical_systems | causal models]] and [[causality_in_dynamical_systems | dynamical systems]] using differential equations <a class="yt-timestamp" data-t="53:30:00">[53:30:00]</a>. This work allows for understanding the relationship between causal representations at equilibrium and away from equilibrium, which in turn helps understand [[causality_and_causal_models | causal relations]] at different time scales <a class="yt-timestamp" data-t="54:02:00">[54:02:00]</a>.

Weinberger notes that Herbert Simon, a pioneer in the development of [[causal_reasoning_and_structural_causal_models | causal models]] in the 1950s, also influenced the structural equations tradition <a class="yt-timestamp" data-t="55:27:00">[55:27:00]</a>. This continuity suggests that the framework of [[causal_reasoning_and_structural_causal_models | causal models]] can be generalized to incorporate the operations found in calculus and [[causality_in_dynamical_systems | dynamical systems]] theory <a class="yt-timestamp" data-t="54:42:00">[54:42:00]</a>.

## Big Data and Causality

The "Big Data Revolution" initially promoted the idea that collecting vast amounts of data could solve any problem through prediction, potentially rendering [[causality_and_causal_models | causality]] obsolete <a class="yt-timestamp" data-t="56:11:00">[56:11:00]</a>. Weinberger is suspicious of this view, arguing that [[causality_and_causal_models | causality]] is about making assumptions to manage the complexity of the world in a local and manageable way, not just throwing data into a machine <a class="yt-timestamp" data-t="56:56:00">[56:56:00]</a>.

While large language models show what can be achieved with massive data, [[causal_reasoning_and_structural_causal_models | causal reasoning]] addresses a different problem: how limited beings, like humans, can understand and interact with the world without knowing everything about the universe <a class="yt-timestamp" data-t="58:47:00">[58:47:00]</a>.

## Advice and Outlook

Weinberger advises those starting with [[causality_and_causal_models | causality]] to find an aspect that genuinely interests them and connects to their existing knowledge, rather than trying to grasp everything at once <a class="yt-timestamp" data-t="01:05:28">[01:05:28]</a>. Resources like "The Book of Why" by Judea Pearl or introductions to causal inference algorithms are good starting points <a class="yt-timestamp" data-t="01:06:07">[01:06:07]</a>, <a class="yt-timestamp" data-t="01:15:01">[01:15:01]</a>. He emphasizes the importance of learning from being wrong and iteratively improving models <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

<div class="callout callout-info">
**Advice for Learning Causality**
*   Find a topic that interests you and branch out from there <a class="yt-timestamp" data-t="01:05:51">[01:05:51]</a>.
*   Don't overthink where to start; delve into something that appeals to you <a class="yt-timestamp" data-t="01:07:06">[01:07:06]</a>.
*   Embrace the learning opportunity when a model is wrong <a class="yt-timestamp" data-t="01:01:02">[01:01:02]</a>.
</div>

He believes there are still many unasked questions in the [[causality_and_causal_models | causal community]], particularly concerning the conditions under which [[causal_reasoning_and_structural_causal_models | causal models]] apply <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. Understanding the limits of models and why they work (or fail) is crucial <a class="yt-timestamp" data-t="01:19:13">[01:19:13]</a>. Time scale analysis, for example, can illuminate how exogeneity is relative to time scale, providing insights into these conditions <a class="yt-timestamp" data-t="01:19:46">[01:19:46]</a>.

For collaboration between academia and industry, Weinberger supports building bridges to share different perspectives and terminology, as many industry problems might already be solved within academic niches <a class="yt-timestamp" data-t="01:10:32">[01:10:32]</a>, <a class="yt-timestamp" data-t="01:12:02">[01:12:02]</a>. He believes [[causality_and_causal_models | causality]] is not just a trend but a valuable tool, as people typically care about intervening, not just predicting, and about invariant correlations rather than mere statistical relationships <a class="yt-timestamp" data-t="01:21:38">[01:21:38]</a>, <a class="yt-timestamp" data-t="01:21:44">[01:21:44]</a>. The challenge lies in effective implementation and incentives to encourage its widespread adoption <a class="yt-timestamp" data-t="01:22:25">[01:22:25]</a>.