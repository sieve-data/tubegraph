---
title: Influence of philosophical and historical perspectives on causality
videoId: UQ8j-DEkB98
---

From: [[causalpython]] <br/> 

Dr. Naftali Weinberger, a philosopher of science, discusses the [[philosophical perspectives on causality|philosophical]] and historical underpinnings of causality, its application across various sciences, and its evolving role, particularly in the context of time scales and complex systems <a class="yt-timestamp" data-t="00:01:24">[00:01:24]</a>.

## Bertrand Russell's Stance on Causality

Over a century ago, iconic British philosopher Bertrand Russell famously stated that causality is a relic of a bygone age <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>. Dr. Weinberger firmly disagrees with this view, arguing that causation is clearly not a relic <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

Russell's perspective was influenced by the physics of his time, such as gravitational astronomy, before quantum mechanics <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. However, Dr. Weinberger asserts that to determine if causation is scientifically legitimate and relevant, one should look at fields like epidemiology, sociology, and industry, all of which undeniably require causal knowledge <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>. Its usefulness is beyond question <a class="yt-timestamp" data-t="00:02:19">[00:02:19]</a>.

Interestingly, Russell has been vindicated in one important sense: 19th-century physics textbooks often presented causation (e.g., forces causing acceleration, acceleration causing velocity), but Russell and Ernst Mach realized it wasn't necessary for the physical theory to work <a class="yt-timestamp" data-t="00:24:00">[00:24:00]</a>. Today, whether causation exists in physics remains controversial, often differing from the causal relations seen in causal graphs used in other sciences <a class="yt-timestamp" data-t="00:24:40">[00:24:40]</a>.

## Causality and Time Scale

A key area of Dr. Weinberger's work is the importance of considering causation at different [[time_scale_and_its_importance_in_causal_models|time scales]] <a class="yt-timestamp" data-t="00:02:44">[00:02:44]</a>. This concept is crucial across all sciences, as any claim or phenomenon studied depends on its spatio-temporal scale <a class="yt-timestamp" data-t="00:02:52">[00:02:52]</a>. For example:
*   **Physics**: Behavior differs at quantum scale versus higher scales where Newtonian physics approximates better <a class="yt-timestamp" data-t="00:03:07">[00:03:07]</a>.
*   **Biology**: Cell biology versus systems biology reveal different relationships <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.

This focus on time scale in a causal context is inspired by Herbert Simon, particularly his 1994 paper with Yumi Iwasaki, "Causality and Model Abstraction" <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.

### The Flossing Example

A simple everyday illustration of time scale's importance is the relationship between flossing and gums bleeding <a class="yt-timestamp" data-t="00:04:00">[00:04:00]</a>:
*   If someone hasn't flossed and starts, their gums will bleed that day <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.
*   If they floss every day for a week, their gums will stop bleeding <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.
These seemingly contradictory statements are both true, as they refer to different time scales, demonstrating how causal relationships vary with the description of the system <a class="yt-timestamp" data-t="00:04:35">[00:04:35]</a>. Every causal model implicitly builds in assumptions about the time scale being considered <a class="yt-timestamp" data-t="00:04:59">[00:04:59]</a>.

## Hidden Confounders and Time Scale

In [[challenges_of_implementing_causality_in_research_and_industry|industry]], a common concern when implementing causality is the possibility of hidden confounders <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. Dr. Weinberger argues that if a causal model does not include confounders, it strongly assumes they are not present <a class="yt-timestamp" data-t="00:06:29">[00:06:29]</a>. Experiments, at least certain types, can remove the influence of confounders by design <a class="yt-timestamp" data-t="00:06:39">[00:06:39]</a>.

The relationship between time scale and confounders is subtle <a class="yt-timestamp" data-t="00:06:48">[00:06:48]</a>. A causal claim is always relative to some concrete system <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. For example, the effect of watching violent television on behavior can vary across societies and depends on various factors <a class="yt-timestamp" data-t="00:07:51">[00:07:51]</a>.

Variables that are very constant over time might not be considered confounders because they don't vary, instead being relegated to the background context <a class="yt-timestamp" data-t="00:08:18">[00:08:18]</a>. For instance, studying trading behavior in a capitalist economy over hundreds of years, the capitalist system itself isn't a confounder, but a constant background condition influencing observations <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>. These long-term factors are important for understanding the conditions under which a model applies <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.

However, these background variables can become problematic on longer time scales <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>. Dr. Weinberger uses an example from Simon and Wicker (1960s) involving crop growth, crops planted, and rainfall <a class="yt-timestamp" data-t="00:10:33">[00:10:33]</a>. Rainfall is typically considered an exogenous variable (not dependent on other variables in the model) <a class="yt-timestamp" data-t="00:10:49">[00:10:49]</a>. But over a long enough time scale (e.g., 100-200 years), agriculture can influence climate, meaning crop growth can influence future rainfall, creating a feedback loop <a class="yt-timestamp" data-t="00:11:49">[00:11:49]</a>.

Both short-term (rainfall exogenous) and long-term (feedback loop) representations are appropriate at their respective time scales <a class="yt-timestamp" data-t="00:12:56">[00:12:56]</a>. The issue arises when extrapolating across time scales <a class="yt-timestamp" data-t="00:13:12">[00:13:12]</a>. This idea is echoed in Ray Dalio's work, which suggests that observations limited to a lifetime are short samples compared to global historical patterns, highlighting the importance of characteristic time scales for understanding historical events or making predictions <a class="yt-timestamp" data-t="00:14:12">[00:14:12]</a>.

## Emergence and Causality in Complex Systems

The discussion of scales naturally leads to complex systems and [[philosophical_aspects_of_causality#Emergence and Causality|emergent phenomena]] <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>. Dr. Weinberger's broad project examines whether causation exists in complex systems <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>. If causal relationships are relative to a time scale, then many discussions about emergence can be understood <a class="yt-timestamp" data-t="00:16:39">[00:16:39]</a>. A system might appear chaotic at a lower descriptive level, but patterns of regularity can emerge at a higher level <a class="yt-timestamp" data-t="00:16:47">[00:16:47]</a>.

Unlike philosophical discussions that often assume "levels" of description (e.g., physical vs. functional), Dr. Weinberger prefers thinking in terms of "zooming in and zooming out" on different objects (or different descriptions of the same object) at different scales <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   **Thermostat Example**: Turning on an oven makes a room hotter in 5 minutes, but an hour later, it's not hotter due to the thermostat <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>. There's no contradiction or metaphysical puzzle; these are different patterns of behavior at different time scales <a class="yt-timestamp" data-t="00:19:17">[00:19:17]</a>.
*   More complex systems with feedback loops and self-regulation exhibit complexity not seen by looking at only parts of the system <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>.

## Defining Causality from a Philosophical Perspective

Dr. Weinberger approaches causality methodologically, heavily influenced by Nancy Cartwright's "Causal Laws and Effective Strategies" <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>. The core idea is that causal knowledge is needed to understand the difference between mere prediction and cases where intervention on a system is desired <a class="yt-timestamp" data-t="00:21:14">[00:21:14]</a>. For example, knowing that giving a drug *causes* recovery, not just that drug-takers are more likely to recover <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

This is not merely a pragmatic or epistemological account; the efficacy of causal methods implies underlying features of the world <a class="yt-timestamp" data-t="00:22:29">[00:22:29]</a>. By studying causal methodology, one can learn about the nature of causation and the world <a class="yt-timestamp" data-t="00:23:02">[00:23:02]</a>.

## Causality and Cognitive Science

Dr. Weinberger has also explored connections between physical processes and mental states, though he now adopts a more pragmatic view <a class="yt-timestamp" data-t="00:27:06">[00:27:06]</a>. He prefers discussing "scales" rather than traditional "levels" (like mental and physical) to avoid Cartesian errors and offer a more precise, scientifically interesting framework <a class="yt-timestamp" data-t="00:28:20">[00:28:20]</a>.

In collaboration with Colin Allen, Dr. Weinberger examined debates in cognitive science, such as whether cognition is like a computer or a dynamical system <a class="yt-timestamp" data-t="00:29:01">[00:29:01]</a>. Research by Randy Beer's lab evolving artificial organisms to perform tasks (e.g., finding food) shows that considering systems computationally or dynamically can be complementary descriptions, not necessarily in conflict <a class="yt-timestamp" data-t="00:29:20">[00:29:20]</a>. Dynamical models, like computational ones, involve modeling assumptions (e.g., boundary conditions, initial conditions) <a class="yt-timestamp" data-t="00:33:42">[00:33:42]</a>.

## Assumptions in Causal Models

A critical point about causal models is that their assumptions are explicitly visible, corresponding to the arrows *missing* from the model <a class="yt-timestamp" data-t="00:34:43">[00:34:43]</a>. If there's no arrow between two variables and no common cause, it's a strong assumption <a class="yt-timestamp" data-t="00:34:50">[00:34:50]</a>. As Nancy Cartwright stated, "no causes in, no causes out" – causal assumptions are required to derive causal knowledge <a class="yt-timestamp" data-t="00:35:17">[00:35:17]</a>.

While many researchers fear building an incorrect causal graph, Dr. Weinberger emphasizes that making a graph explicitly allows for learning from errors <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. An explicitly wrong model is a learning opportunity to modify and improve it <a class="yt-timestamp" data-t="00:38:32">[00:38:32]</a>. Without explicit causal methods, researchers might still draw causal conclusions from non-causal analyses, leading to implicit, unexamined assumptions <a class="yt-timestamp" data-t="00:37:08">[00:37:08]</a>.

## Interventions in Dynamical Systems ("Intervening and Letting Go")

In his 2018 paper "Intervening and Letting Go," Dr. Weinberger explored how different types of interventions affect dynamical systems <a class="yt-timestamp" data-t="00:40:39">[00:40:39]</a>. Using the example of an ideal gas in a container, he demonstrates how causal models are relative to a specific setup <a class="yt-timestamp" data-t="00:41:07">[00:41:07]</a>.

He discusses a puzzle related to interventions:
*   A movable piston system (pressure and temperature cause volume) <a class="yt-timestamp" data-t="00:41:54">[00:41:54]</a>.
*   Fixing the volume by inserting a pin makes the system behave like a sealed container (volume and temperature cause pressure) <a class="yt-timestamp" data-t="00:42:25">[00:42:25]</a>.
The key insight, inspired by Denver Dash's work, is that this "intervention" (fixing volume) doesn't behave as expected by standard intervention formalisms like the "do-operator" <a class="yt-timestamp" data-t="00:42:57">[00:42:57]</a>.

This puzzle is resolved by considering the system's dynamics <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>. In a dynamic model, there's a feedback loop (e.g., between pressure and volume) that allows the system to reach equilibrium <a class="yt-timestamp" data-t="00:44:08">[00:44:08]</a>.
*   **Clamp Intervention**: Holding a variable fixed indefinitely (like inserting a pin) destroys the system's ability to operate its feedback loop and reach a certain equilibrium <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>.
*   **Letting Go**: Removing a constraint (like pulling out the pin) is a separate action that the standard formalism doesn't account for <a class="yt-timestamp" data-t="00:47:20">[00:47:20]</a>.

This highlights that causal models need to incorporate how different types of interventions (e.g., clamp, shock, repeated shocks) affect systems over various durations <a class="yt-timestamp" data-t="00:49:55">[00:49:55]</a>. The goal is often to change the entire state or stability properties of a system, influencing its feedback loops to bring it into a new equilibrium <a class="yt-timestamp" data-t="00:51:14">[00:51:14]</a>.

### Bridging Causal Frameworks and Dynamical Systems
Dr. Weinberger emphasizes the exciting work by Yori Moens's lab at the University of Amsterdam and Conrad Delft Institute, which is bridging the gap between causal inference and dynamical systems <a class="yt-timestamp" data-t="00:53:05">[00:53:05]</a>. This includes incorporating time derivatives and integration operations into causal models <a class="yt-timestamp" data-t="00:54:14">[00:54:14]</a>. This work shows a clear generalization of the standard causal framework, with a continuity tracing back to Herbert Simon's pioneering work in structural equations <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.

## Historical Parallels: Big Data Revolution

The "Big Data Revolution" of the early 2010s, with its idea that collecting enough data could solve any problem predictively <a class="yt-timestamp" data-t="00:56:11">[00:56:11]</a>, is met with suspicion by Dr. Weinberger <a class="yt-timestamp" data-t="00:56:54">[00:56:54]</a>. Causality, in contrast, is about making assumptions to manage the world's complexity in a local and manageable way <a class="yt-timestamp" data-t="00:57:08">[00:57:08]</a>. While empirical results (e.g., large language models) might challenge pre-conceived notions about needing specific structures, causal reasoning serves a different purpose <a class="yt-timestamp" data-t="00:58:17">[00:58:17]</a>. It's about a "limited being operating at a particular time scale" who doesn't need to know everything to predict localized events <a class="yt-timestamp" data-t="00:58:48">[00:58:48]</a>.

## Personal Influences on Philosophical Thinking

Dr. Weinberger believes his extensive study of the Talmud (a legal-style literature requiring triangulation of different sources) and Islamic Sufi texts has influenced his thinking <a class="yt-timestamp" data-t="00:59:59">[00:59:59]</a>. The Talmudic tradition, with its multiple, often conflicting, interpretations by different rabbis, fosters a flexibility of thought <a class="yt-timestamp" data-t="01:00:22">[01:00:22]</a>. This encourages viewing models not as final solutions, but as systematic ways to explore and learn, even when wrong <a class="yt-timestamp" data-t="01:01:06">[01:01:06]</a>. This training proved invaluable when delving into the legal literature on discrimination for his work on the [[integration_of_causality_in_economic_modeling|causal analysis of racial discrimination]] <a class="yt-timestamp" data-t="01:01:20">[01:01:20]</a>.

Sufi texts and Kabbalah, mystical traditions, emphasize human experience and reconciling imminence and transcendence – personal experience with a broader system that makes the world function <a class="yt-timestamp" data-t="01:02:54">[01:02:54]</a>. This resonates with the dilemma of how a limited individual interacts with a complex world <a class="yt-timestamp" data-t="01:03:10">[01:03:10]</a>.

## Advice for Those Starting with Causality

Dr. Weinberger recommends finding an aspect of causality that genuinely interests the individual, even if it seems random <a class="yt-timestamp" data-t="01:05:28">[01:05:28]</a>. This provides an "in" to branch out and learn <a class="yt-timestamp" data-t="01:05:48">[01:05:48]</a>. Resources include:
*   Felix Elwert's chapter in a causality handbook (good for social scientists, covers confounding, d-separation, endogenous selection bias, time-varying treatments) <a class="yt-timestamp" data-t="01:13:30">[01:13:30]</a>.
*   Elwert and Chris Winship's paper on endogenous selection bias (conditioning on a collider) <a class="yt-timestamp" data-t="01:14:07">[01:14:07]</a>.
*   Frederick Eberhardt's short introduction to causal inference algorithms (covers traditional and machine learning algorithms, including the two-variable problem) <a class="yt-timestamp" data-t="01:14:39">[01:14:39]</a>.
*   The textbook by Shoelkopf, Janzing, and Peters for more detail on machine learning methods <a class="yt-timestamp" data-t="01:15:53">[01:15:53]</a>.
*   Michael Nielsen's website for an accessible introduction to d-separation <a class="yt-timestamp" data-t="01:16:07">[01:16:07]</a>.
*   Dr. Weinberger's own Stanford Encyclopedia of Philosophy article on Simpson's Paradox, which relates causal modeling to earlier [[philosophical_aspects_of_causality#Historical Development and Key Papers|philosophical theories]] <a class="yt-timestamp" data-t="01:16:33">[01:16:33]</a>.

## The Future of Causality

Dr. Weinberger believes that while there has been immense progress in the algorithmic side of causality, many fundamental questions are still not being asked <a class="yt-timestamp" data-t="01:18:08">[01:18:08]</a>. Beyond axiomatic approaches, there's a need to explore the "conditions of causal representation" – understanding the types of systems to which causal models apply and *why* they work <a class="yt-timestamp" data-t="01:19:00">[01:19:00]</a>. He views the [[time_scale_and_its_importance_in_causal_models|time scale]] as an antidote to purely axiomatic approaches, as it clarifies how facts about exogeneity are relative to time scale, thus defining the conditions of model applicability <a class="yt-timestamp" data-t="01:19:35">[01:19:35]</a>.

He emphasizes that understanding limitations of models is not criticism but an opportunity to learn where they break down and how to fix them <a class="yt-timestamp" data-t="01:20:04">[01:20:04]</a>. Causality, he argues, is a valuable tool because most problems, even in industry, are not purely predictive; they involve interventions or invariant correlations <a class="yt-timestamp" data-t="01:21:21">[01:21:21]</a>. The challenge lies in implementation and incentives, ensuring that useful causal tools are easily adopted and recognized in practice <a class="yt-timestamp" data-t="01:22:25">[01:22:25]</a>.