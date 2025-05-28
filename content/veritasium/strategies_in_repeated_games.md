---
title: strategies in repeated games
videoId: mScpHTIi-kM
---

From: [[veritasium]] <br/> 

## The Foundation: Game Theory and the Prisoner's Dilemma

Game theory studies problems that emerge in situations where individuals or groups are in conflict, ranging from international relations to everyday interactions between roommates <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Figuring out the best strategy in such scenarios can have profound implications, even leading to the emergence of cooperation <a class="yt-timestamp" data-t="00:00:22">[00:00:22]</a>.

One of the most famous problems in [[game theory and life | game theory]] is [[the_prisoners_dilemma | the prisoner's dilemma]] <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>. This concept gained prominence in 1950 when two mathematicians at the RAND Corporation invented a game that closely resembled the US-Soviet conflict <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>.

### Understanding [[the_prisoners_dilemma | The Prisoner's Dilemma]]

In a typical [[the_prisoners_dilemma | prisoner's dilemma]] scenario, two players each have two choices: cooperate or defect <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. The payoffs are structured as follows:
*   **Both Cooperate**: Each gets three coins <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   **One Cooperates, One Defects**: The defector gets five coins, the cooperator gets nothing <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   **Both Defect**: Each gets one coin <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

The goal is to maximize one's own coin count <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>. A rational analysis shows that no matter what the opponent does, defecting is always the better option for an individual <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>. Consequently, if both players are rational, they both defect, leading to a suboptimal outcome where each gets one coin, instead of three if they had both cooperated <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

This phenomenon was observed during the Cold War, where the US and Soviet Union, acting in their perceived best interest, developed massive nuclear arsenals, spending trillions of dollars, despite both being worse off than if they had cooperated to prevent further development <a class="yt-timestamp" data-t="00:03:54">[00:04:25]</a>.

## Repeated Games: A Shift in Strategy

Many real-world problems, such as impalas grooming each other, are not single instances of [[the_prisoners_dilemma | the prisoner's dilemma]], but rather repeated interactions <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a> <a class="yt-timestamp" data-t="00:05:45">[00:05:45]</a>. In a single interaction, defecting is the rational choice <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>. However, when the game is played repeatedly, a player's current actions can influence future interactions <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### Axelrod's Computer Tournaments

In 1980, political scientist Robert Axelrod conducted a computer tournament to discover the best strategy in a repeated [[the_prisoners_dilemma | prisoner's dilemma]] <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Leading game theorists submitted computer programs, or "strategies," to play against each other over 200 rounds <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a> <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>.

#### First Tournament Results: The Rise of Tit for Tat

Surprisingly, the simplest program, called **Tit for Tat**, won the tournament <a class="yt-timestamp" data-t="00:08:21">[00:08:21]</a>. Its strategy was straightforward:
1.  Start by cooperating <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
2.  Then, copy exactly what the opponent did in the last move (cooperate after cooperation, defect after defection) <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
3.  It only retaliates once; if the opponent cooperates again, so does Tit for Tat <a class="yt-timestamp" data-t="00:08:40">[00:08:40]</a>.

Axelrod identified four key qualities shared by the best-performing strategies, including Tit for Tat:

*   **Nice**: Strategies that are never the first to defect <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a> <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. All top eight strategies in the first tournament were "nice" <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
*   **Forgiving**: Strategies that retaliate but don't hold a grudge <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a> <a class="yt-timestamp" data-t="00:10:50">[00:10:50]</a>. They don't let past defections (beyond the immediate last round) influence current decisions <a class="yt-timestamp" data-t="00:10:59">[00:10:59]</a>. This was a shock to experts who expected complex, tricky strategies to win <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
*   **Retaliatory (Provokable)**: If the opponent defects, the strategy strikes back immediately, avoiding being a pushover <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a> <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
*   **Clear**: Simple and predictable, allowing other programs to understand their behavior and establish trust <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a> <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

#### Second Tournament and the Importance of Unknown Endings

Axelrod held a second tournament, with one critical change: the exact number of rounds was unknown, though the average was 200 <a class="yt-timestamp" data-t="00:12:22">[00:12:22]</a> <a class="yt-timestamp" data-t="00:13:01">[00:13:01]</a>. Knowing the end date would lead rational players to defect in the final round, triggering a chain reaction of defections backward to the first round <a class="yt-timestamp" data-t="00:12:32">[00:12:32]</a>. Uncertainty about the end encourages continued cooperation <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>.

Despite contestants having access to the first tournament's results, Tit for Tat won again <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. Nice strategies continued to perform significantly better than nasty ones <a class="yt-timestamp" data-t="00:14:21">[00:14:21]</a>.

### The Dynamic Nature of Best Strategies

Axelrod's tournaments showed that there is no single "best strategy" in the repeated [[the_prisoners_dilemma | prisoner's dilemma]]; the optimal strategy depends on the other strategies in the environment <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a> <a class="yt-timestamp" data-t="00:16:10">[00:16:10]</a>. For example, if Tit for Tat is placed in an environment of only "always defect" strategies, it performs poorly <a class="yt-timestamp" data-t="00:16:15">[00:16:15]</a>.

### Ecological Simulation: The Emergence of Cooperation

Axelrod conducted a simulation where successful strategies grew in number across generations, while unsuccessful ones diminished <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. After 1,000 generations, only nice strategies survived, with Tit for Tat again coming out on top <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. This suggests that even in a harsh environment populated by defectors, a small cluster of cooperators can emerge and spread, eventually taking over the population <a class="yt-timestamp" data-t="00:17:39">[00:18:11]</a>. This highlights how cooperation can emerge even among self-interested players, without requiring altruism <a class="yt-timestamp" data-t="00:18:14">[00:18:31]</a>. This concept has been applied to evolutionary biology to explain how cooperation might have emerged in selfish organisms <a class="yt-timestamp" data-t="00:18:38">[00:18:51]</a>.

## Strategies in Noisy Environments

Real-world interactions often involve "noise" or random errors, where an intended cooperation might be perceived as a defection <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. For example, a Soviet early warning system once confused sunlight reflecting off clouds with a ballistic missile launch <a class="yt-timestamp" data-t="00:19:50">[00:20:07]</a>.

In a noisy environment, Tit for Tat can suffer greatly because a single perceived defection can trigger a continuous chain of alternating retaliations, leading to poor outcomes <a class="yt-timestamp" data-t="00:20:47">[00:21:14]</a>. To address this, a "generous Tit for Tat" strategy is more effective: it's like Tit for Tat, but with about 10% more forgiveness, retaliating only nine out of ten times <a class="yt-timestamp" data-t="00:21:21">[00:21:41]</a>. This helps break echo effects while remaining retaliatory enough to avoid exploitation <a class="yt-timestamp" data-t="00:21:38">[00:21:41]</a>.

## Beyond Zero-Sum: The Power of Cooperation

A common misconception is that to win, one must beat the other person, as in zero-sum games like chess or poker where one's gain is another's loss <a class="yt-timestamp" data-t="00:29:27">[00:22:43]</a>. However, most of life is not zero-sum <a class="yt-timestamp" data-t="00:22:43">[00:22:46]</a>. In repeated interactions, strategies like Tit for Tat, which can never "win" (only draw or lose against an individual opponent in terms of relative score), consistently come out ahead when total interactions are tallied <a class="yt-timestamp" data-t="00:22:01">[00:22:13]</a>. This demonstrates that cooperation can pay off, even among rivals, by unlocking rewards from the "banker" (the world or overall system) <a class="yt-timestamp" data-t="00:22:46">[00:23:04]</a>.

The US and Soviet Union, for instance, learned to cooperate in disarming nuclear weapons by taking small, verifiable steps, turning a single [[the_prisoners_dilemma | prisoner's dilemma]] into a repeated game where mutual cooperation could be checked and repeated annually <a class="yt-timestamp" data-t="00:23:08">[00:23:43]</a>.

Decisions made today, especially in repeated interactions, can have far-reaching impacts, shaping not only individual futures but also the environment itself <a class="yt-timestamp" data-t="00:24:54">[00:25:11]</a>. The core takeaways from Axelrod's work — be nice, forgiving, but don't be a pushover — remain relevant for navigating complex interactions <a class="yt-timestamp" data-t="00:24:09">[00:24:13]</a>.