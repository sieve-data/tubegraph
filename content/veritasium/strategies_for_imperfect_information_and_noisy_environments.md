---
title: strategies for imperfect information and noisy environments
videoId: mScpHTIi-kM
---

From: [[veritasium]] <br/> 

The [[game_theory_and_the_prisoners_dilemma | Prisoner's Dilemma]], a foundational problem in [[game_theory_and_the_prisoners_dilemma | game theory]], often appears in real-world scenarios where perfect information is unavailable and "noise" or errors can occur <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Understanding how strategies perform in these imperfect conditions is crucial, as the consequences can range from roommate conflicts to international relations and the destruction of the planet <a class="yt-timestamp" data-t="00:00:00">[00:00:03]</a>.

## The Challenge of Noise in Iterated Games

In the context of [[game_theory_and_the_prisoners_dilemma | game theory]], "noise" refers to random errors or misinterpretations of actions within a system <a class="yt-timestamp" data-t="00:00:00">[19:36]</a>. This means a player might intend to cooperate, but their action is perceived as a defection <a class="yt-timestamp" data-t="00:00:00">[19:42]</a>. Such errors are common in the real world <a class="yt-timestamp" data-t="00:00:00">[19:47]</a>.

A historical example illustrating the costs of signal error occurred in 1983 when the Soviet satellite-based early warning system incorrectly detected the launch of an intercontinental ballistic missile from the US <a class="yt-timestamp" data-t="00:00:00">[19:50]</a>. The system had confused sunlight reflecting off high-altitude clouds with a ballistic missile <a class="yt-timestamp" data-t="00:00:00">[00:02:00]</a>. Thankfully, the Soviet officer on duty, Stanislav Petrov, dismissed the alarm <a class="yt-timestamp" data-t="00:00:00">[20:07]</a>. This incident highlights the importance of studying the effects of noise on strategic decision-making <a class="yt-timestamp" data-t="00:00:00">[20:15]</a>.

### Impact on [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]]

While [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] (cooperate first, then copy the opponent's last move) performed exceptionally well in tournaments without noise, its performance suffers significantly in noisy environments <a class="yt-timestamp" data-t="00:00:00">[20:47]</a>.

Consider two [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] players interacting in a noisy environment:
1.  They both start by cooperating <a class="yt-timestamp" data-t="00:00:00">[20:50]</a>.
2.  If one player's cooperation is misperceived as a defection, the other [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] player retaliates <a class="yt-timestamp" data-t="00:00:00">[20:53]</a>.
3.  This can trigger a chain of alternating retaliations, an "echo effect" <a class="yt-timestamp" data-t="00:00:00">[20:58]</a>.
4.  If another cooperation is misperceived as a defection, the game can devolve into constant mutual defection <a class="yt-timestamp" data-t="00:00:00">[21:02]</a>.

In such scenarios, both players would receive only about a third of the points they would earn in a perfect environment <a class="yt-timestamp" data-t="00:00:00">[21:08]</a>. This demonstrates how [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] can go from performing very well to very poorly when noise is introduced <a class="yt-timestamp" data-t="00:00:00">[21:14]</a>.

## Generous [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]]: A Solution

To address the challenges posed by noise, a modified strategy called "generous [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]]" emerges as more effective <a class="yt-timestamp" data-t="00:00:00">[21:26]</a>. This strategy incorporates an element of forgiveness:
*   It plays [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] but includes approximately 10% more forgiveness <a class="yt-timestamp" data-t="00:00:00">[21:28]</a>.
*   Instead of retaliating after every defection, it only retaliates about nine out of ten times <a class="yt-timestamp" data-t="00:00:00">[21:31]</a>.

This increased forgiveness helps break out of the negative "echo effects" caused by misinterpretations, while still being retaliatory enough to prevent exploitation <a class="yt-timestamp" data-t="00:00:00">[21:38]</a>. When Axelrod ran tournaments with noise, this more generous approach performed quite well <a class="yt-timestamp" data-t="00:00:00">[21:44]</a>.

### The Four Qualities of Successful Strategies

Robert Axelrod's tournaments, which involved leading [[game_theory_and_the_prisoners_dilemma | game theorists]] submitting computer programs to play the [[game_theory_and_the_prisoners_dilemma | Prisoner's Dilemma]] over 200 rounds <a class="yt-timestamp" data-t="00:00:00">[06:20]</a>, revealed four key qualities of the most successful strategies, which remain relevant even in noisy environments:

1.  **Nice:** Strategies that are never the first to defect <a class="yt-timestamp" data-t="00:00:00">[10:15]</a>.
2.  **Forgiving:** Strategies that retaliate but do not hold a grudge, not letting past defections (beyond the immediate last round) influence current decisions <a class="yt-timestamp" data-t="00:00:00">[10:46]</a>.
3.  **Retaliatory:** Strategies that strike back immediately if an opponent defects, avoiding being a "pushover" <a class="yt-timestamp" data-t="00:00:00">[14:38]</a>.
4.  **Clear:** Strategies that are predictable and easy for other programs to understand, fostering trust and cooperation rather than prompting defection <a class="yt-timestamp" data-t="00:00:00">[14:58]</a>. Strategies that are too opaque or random often lead to mutual defection because opponents cannot anticipate their moves <a class="yt-timestamp" data-t="00:00:00">[15:01]</a>.

These principles, particularly clarity and forgiveness, are vital for navigating environments with imperfect information, allowing for the establishment of trust and the avoidance of escalating conflicts triggered by misunderstanding or error <a class="yt-timestamp" data-t="00:00:00">[15:09]</a>.

## Real-World Implications and Adaptability

The insights from these studies have been applied to diverse fields, including evolutionary biology and international conflicts <a class="yt-timestamp" data-t="00:00:00">[21:27]</a>. The US and Soviet Union, for instance, learned to reduce their nuclear arsenals by disarming slowly and checking each other's cooperation over time, transforming a single [[game_theory_and_the_prisoners_dilemma | Prisoner's Dilemma]] into an iterated one where mutual cooperation could emerge <a class="yt-timestamp" data-t="00:00:00">[23:08]</a>.

While [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] or generous [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] may not always emerge as the single best strategy across all possible environments (as the optimal strategy depends on the other strategies present <a class="yt-timestamp" data-t="00:00:00">[16:06]</a>), Axelrod's core takeaways — to be nice, forgiving, but not a pushover — remain fundamental <a class="yt-timestamp" data-t="00:00:00">[24:09]</a>. These findings emphasize that cooperation can emerge even among self-interested rivals, as long as the conditions allow for repeated interactions and the strategies employed can adapt to imperfect information <a class="yt-timestamp" data-t="00:00:00">[18:14]</a>.

For individuals seeking to develop their [[mathematical_probability_strategies | problem-solving skills]] and ability to make decisions in uncertain situations, understanding these principles, including the use of [[mathematical_probability_strategies | computer simulations]] to test strategies, can be highly beneficial <a class="yt-timestamp" data-t="00:00:00">[25:27]</a>.