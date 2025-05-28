---
title: tit for tat strategy in iterative games
videoId: mScpHTIi-kM
---

From: [[veritasium]] <br/> 

The [[game theory and the prisoners dilemma | Prisoner's Dilemma]] is considered the most famous problem in [[game theory and the prisoners dilemma | game theory]] <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. Problems of this type are ubiquitous, appearing in scenarios ranging from international conflicts to everyday interactions like roommates doing dishes <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>. Understanding the best strategy can have significant implications for outcomes such as war, peace, and cooperation <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

## The Prisoner's Dilemma

The [[game theory and the prisoners dilemma | Prisoner's Dilemma]] was invented in 1950 by two mathematicians at the RAND Corporation, a U.S.-based think tank, while studying questions related to the Cold War, specifically the US-Soviet conflict <a class="yt-timestamp" data-t="02:11:00">[02:11:00]</a>.

### Game Mechanics

In a typical scenario, two players are presented with two choices: "cooperate" or "defect" <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. The payoffs are structured as follows <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>:
*   **Both Cooperate**: Each player receives a moderate reward (e.g., three coins) <a class="yt-timestamp" data-t="02:46:00">[02:46:00]</a>.
*   **One Cooperates, One Defects**: The defector receives a high reward (e.g., five coins), while the cooperator receives nothing <a class="yt-timestamp" data-t="02:50:00">[02:50:00]</a>.
*   **Both Defect**: Each player receives a low reward (e.g., one coin) <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

The goal is to maximize one's own reward <a class="yt-timestamp" data-t="03:01:00">[03:01:00]</a>. Rationally, no matter what the opponent does, defecting always yields a better individual outcome <a class="yt-timestamp" data-t="03:31:00">[03:31:00]</a>. If both players act rationally, they both defect, resulting in a suboptimal outcome where each receives only one coin, when they could have received three by cooperating <a class="yt-timestamp" data-t="03:44:00">[03:44:00]</a>.

### Real-World Applications
The [[game theory and the prisoners dilemma | Prisoner's Dilemma]] applies to many real-world situations <a class="yt-timestamp" data-t="04:39:00">[04:39:00]</a>:
*   **Cold War Nuclear Arms Race**: The US and Soviet Union, acting in their perceived best interests, developed vast nuclear arsenals, leading to mutual assured destruction and enormous costs, despite both being better off if they had cooperated to limit development <a class="yt-timestamp" data-t="03:54:00">[03:54:00]</a>.
*   **Animal Behavior**: Impalas, for instance, need to groom each other to remove ticks. Grooming costs resources, but not grooming means they cannot reach all ticks. This poses a choice: cooperate (groom) or defect (don't groom) <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>.

## The Iterated Prisoner's Dilemma

Most real-world problems are not single instances of the [[game theory and the prisoners dilemma | Prisoner's Dilemma]], but rather repeated interactions <a class="yt-timestamp" data-t="05:45:00">[05:45:00]</a>. This changes the dynamics, as past actions can influence future ones <a class="yt-timestamp" data-t="06:02:00">[06:02:00]</a>.

### Axelrod's Tournaments
In 1980, political scientist Robert Axelrod organized a computer tournament to identify the best strategy for the repeated [[game theory and the prisoners dilemma | Prisoner's Dilemma]] <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>. Leading [[game theory and the prisoners dilemma | game theorists]] submitted computer programs (strategies) that would play against each other over 200 rounds <a class="yt-timestamp" data-t="06:26:00">[06:26:00]</a>. Payoffs were based on points, with the goal of maximizing total points <a class="yt-timestamp" data-t="06:49:00">[06:49:00]</a>.

Some notable strategies submitted included:
*   **Friedman**: Starts by cooperating, but if the opponent defects once, it defects for the rest of the game <a class="yt-timestamp" data-t="07:32:00">[07:32:00]</a>.
*   **Joss**: Starts by cooperating, copies the opponent's last move, but defects 10% of the time <a class="yt-timestamp" data-t="07:42:00">[07:42:00]</a>.
*   **Graaskamp**: Similar to Joss, but defects deterministically in the 50th round to probe the opponent's strategy <a class="yt-timestamp" data-t="07:55:00">[07:55:00]</a>.
*   **Random**: Cooperates or defects randomly 50% of the time <a class="yt-timestamp" data-t="07:19:00">[07:19:00]</a>.

### The Winner: Tit for Tat

The simplest program, "Tit for Tat," emerged as the winner <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.
*   **Description**: Tit for Tat starts by cooperating and then, in every subsequent round, copies exactly what its opponent did in the previous move <a class="yt-timestamp" data-t="08:31:00">[08:31:00]</a>. It cooperates if the opponent cooperated and defects if the opponent defected, but only once; if the opponent returns to cooperating, so does Tit for Tat <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>.
*   **Performance**:
    *   Against Friedman: Both cooperated throughout, achieving perfect scores <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>.
    *   Against Joss: Joss's probabilistic defection led to a series of back-and-forth defections, an "echo effect," resulting in poor scores for both <a class="yt-timestamp" data-t="08:54:00">[08:54:00]</a>. Despite this, Tit for Tat won overall due to its cooperation with other strategies <a class="yt-timestamp" data-t="09:36:00">[09:36:00]</a>.

### Qualities of Successful Strategies
Axelrod identified four key qualities shared by the best-performing strategies, including Tit for Tat <a class="yt-timestamp" data-t="10:08:00">[10:08:00]</a>:

1.  **Nice**: Strategies that are never the first to defect <a class="yt-timestamp" data-t="10:15:00">[10:15:00]</a>. All top eight strategies in the first tournament were "nice," and even the worst nice strategy outscored the best "nasty" (first-to-defect) strategy <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>.
2.  **Forgiving**: Strategies that retaliate but do not hold a grudge <a class="yt-timestamp" data-t="10:46:00">[10:46:00]</a>. Tit for Tat retaliates immediately but does not let past defections (before the last round) influence current decisions <a class="yt-timestamp" data-t="10:54:00">[10:54:00]</a>. "Friedman," being maximally unforgiving, performed poorly in the long run <a class="yt-timestamp" data-t="11:05:00">[11:05:00]</a>.
    *   A more forgiving variant, "Tit for Two Tats," only defects after its opponent defects twice in a row <a class="yt-timestamp" data-t="11:49:00">[11:49:00]</a>. Axelrod's analysis showed this strategy would have won the first tournament if submitted <a class="yt-timestamp" data-t="11:54:00">[11:54:00]</a>.
3.  **Retaliatory**: Strategies that strike back immediately if the opponent defects, avoiding being a "pushover" <a class="yt-timestamp" data-t="14:38:00">[14:38:00]</a>. While "Always Cooperate" is easily exploited, Tit for Tat is difficult to take advantage of <a class="yt-timestamp" data-t="14:47:00">[14:47:00]</a>.
4.  **Clear**: Strategies that are easy to understand and predictable <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>. Opaque or overly complicated strategies made it difficult for others to establish trust, leading to more defections <a class="yt-timestamp" data-t="15:01:00">[15:01:00]</a>.

These four principles — being nice, forgiving, provokable (retaliatory), and clear — resonate with moral philosophies, often summarized as "an eye for an eye" <a class="yt-timestamp" data-t="15:31:00">[15:31:00]</a>.

### The Second Tournament and Imperfect Information
Axelrod conducted a second tournament, sharing the results and analysis of the first with new contestants <a class="yt-timestamp" data-t="12:15:00">[12:15:00]</a>. One crucial change was how the number of rounds was determined: instead of a fixed 200 rounds, the average was 200, but the exact end was uncertain due to a random number generator <a class="yt-timestamp" data-t="13:04:00">[13:04:00]</a>. This prevents "backward induction," where knowing the end leads to defection in all preceding rounds <a class="yt-timestamp" data-t="12:28:00">[12:28:00]</a>.

Despite some entrants submitting "nasty" strategies to exploit expected "niceness" from others, Tit for Tat won again <a class="yt-timestamp" data-t="14:13:00">[14:13:00]</a>. Nice strategies continued to dominate the top ranks <a class="yt-timestamp" data-t="14:21:00">[14:21:00]</a>.

### Environmental Influence and Evolution of Cooperation
No single strategy is universally best in the repeated [[game theory and the prisoners dilemma | Prisoner's Dilemma]]; the optimal strategy depends on the interacting strategies within the environment <a class="yt-timestamp" data-t="16:03:00">[16:03:00]</a>. For example, Tit for Tat performs poorly if paired only with "Always Defect" strategies <a class="yt-timestamp" data-t="16:15:00">[16:15:00]</a>.

Axelrod's simulations, where successful strategies "grow" and unsuccessful ones "shrink" over generations (an ecological simulation, not evolutionary as there are no mutations), showed that only nice strategies survive in the long run <a class="yt-timestamp" data-t="16:35:00">[16:35:00]</a>. Tit for Tat consistently came out on top <a class="yt-timestamp" data-t="17:18:00">[17:18:00]</a>. This suggests that even in a harsh environment populated by self-interested players, a small cluster of cooperating players (like Tit for Tat) can emerge and spread, eventually taking over the population <a class="yt-timestamp" data-t="17:39:00">[17:39:00]</a>. Cooperation can emerge without altruism, driven by self-interest <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>.

This concept may explain how cooperation arose in nature, from selfish organisms to those exhibiting mutualistic behaviors like impalas grooming each other or fish cleaning sharks <a class="yt-timestamp" data-t="18:38:00">[18:38:00]</a>. The strategy can be encoded in DNA; if it performs better, it can spread through a population <a class="yt-timestamp" data-t="19:11:00">[19:11:00]</a>.

### Strategies for Imperfect Information and Noisy Environments
Axelrod's original tournaments did not account for "noise" or random errors in the system <a class="yt-timestamp" data-t="19:36:00">[19:36:00]</a>. For example, one player tries to cooperate, but it's perceived as a defection <a class="yt-timestamp" data-t="19:42:00">[19:42:00]</a>. Such errors happen frequently in the real world, as seen in the 1983 incident where a Soviet early warning system confused sunlight with a ballistic missile launch <a class="yt-timestamp" data-t="19:50:00">[19:50:00]</a>.

In a noisy environment, Tit for Tat can suffer greatly. If a cooperation is mistakenly perceived as a defection, it triggers a chain of alternating retaliations, leading to constant mutual defection for the rest of the game <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>. To solve this, strategies need a way to break out of these echo effects <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>.

A solution is to play Tit for Tat with about 10% more forgiveness, retaliating only about nine out of every ten times a defection occurs <a class="yt-timestamp" data-t="21:25:00">[21:25:00]</a>. This "generous Tit for Tat" helps break echoes while remaining retaliatory enough to avoid exploitation <a class="yt-timestamp" data-t="21:38:00">[21:38:00]</a>.

## Conclusion: Cooperation Pays

One of the most striking findings is that Tit for Tat, by design, can never score higher than its opponent (it can only lose or draw a single game), yet it consistently wins overall in tournaments <a class="yt-timestamp" data-t="21:57:00">[21:57:00]</a>. Conversely, "Always Defect" can only draw or win a single game, but performs extremely poorly overall <a class="yt-timestamp" data-t="22:17:00">[22:17:00]</a>.

This highlights that life is not a "zero-sum game" where one person's gain is another's loss, like chess or poker <a class="yt-timestamp" data-t="22:37:00">[22:37:00]</a>. In most of life, rewards come from the "banker" (the world), not directly from the opponent <a class="yt-timestamp" data-t="22:46:00">[22:46:00]</a>. The key is to find "win-win situations" and cooperate to unlock collective rewards <a class="yt-timestamp" data-t="22:57:00">[22:57:00]</a>.

The US and Soviet Union, for instance, learned to cooperate on nuclear disarmament by disarming slowly and checking each other's compliance, rather than attempting a single, all-at-once agreement <a class="yt-timestamp" data-t="23:08:00">[23:08:00]</a>. This iterative approach allowed for mutual cooperation.

Since Axelrod's tournaments, research has continued to explore optimal [[strategies for imperfect information and noisy environments | strategies for imperfect information and noisy environments]] in various conditions, including payoff structures and mutations <a class="yt-timestamp" data-t="23:47:00">[23:47:00]</a>. While Tit for Tat or generous Tit for Tat may not always win, Axelrod's core lessons remain: be nice, forgiving, but not a pushover <a class="yt-timestamp" data-t="24:09:00">[24:09:00]</a>.

Ultimately, in the short term, the environment shapes the player, but in the long run, players shape the environment <a class="yt-timestamp" data-t="25:02:00">[25:02:00]</a>. The choices made in iterative games can have far-reaching impacts <a class="yt-timestamp" data-t="25:17:00">[25:17:00]</a>.

### See Also
*   [[game theory and the prisoners dilemma | Game Theory and the Prisoner's Dilemma]]
*   [[strategies for imperfect information and noisy environments | Strategies for Imperfect Information and Noisy Environments]]
*   [[Mathematical probability strategies | Mathematical Probability Strategies]]