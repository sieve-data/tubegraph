---
title: game theory and the prisoners dilemma
videoId: mScpHTIi-kM
---

From: [[veritasium]] <br/> 

Game theory is a field that studies strategic decision-making in situations where the outcome for each participant depends on the choices of all participants <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. Problems in game theory arise in diverse scenarios, from international conflicts to everyday interactions like roommates doing dishes <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>. Understanding the best strategy in such situations can have profound implications, affecting outcomes ranging from personal flourishing to global peace <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a>. Within the mechanics of these games, insights into unexpected phenomena, such as cooperation, can be found <a class="yt-timestamp" data-t="00:00:26">[00:00:26]</a>.

## Origins in the Cold War

The most famous problem in game theory, the Prisoner's Dilemma, emerged during the Cold War era <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. On September 3, 1949, an American weather monitoring plane detected radioactive material in air samples collected over Japan, indicating a recent nuclear explosion <a class="yt-timestamp" data-t="00:00:41">[00:00:41]</a>. Further tests confirmed the presence of Cerium-141 and Yttrium-91, isotopes with short half-lives, confirming a recent nuclear detonation <a class="yt-timestamp" data-t="00:00:53">[00:00:53]</a>. Since the US had not conducted any tests that year, the conclusion was that the Soviet Union had developed a nuclear bomb <a class="yt-timestamp" data-t="00:01:17">[00:01:17]</a>. This development greatly exacerbated the problem of Western Europe and the United States, increasing the perceived imminence of war <a class="yt-timestamp" data-t="00:01:35">[00:01:35]</a>.

Some US officials, like Navy Secretary Matthews, even proposed a preemptive nuclear strike against the Soviets while the US still held an advantage, calling it "aggressors for peace" <a class="yt-timestamp" data-t="00:01:47">[00:01:47]</a>. John von Neumann, a founder of game theory, advocated for immediate action, stating, "If you say why not bomb them tomorrow, I say, why not bomb them today?" <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>.

In 1950, the RAND Corporation, a US-based think tank, studied this question using game theory <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. That same year, two mathematicians at RAND invented a new game that closely mirrored the US-Soviet conflict: the Prisoner's Dilemma <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

## Understanding the Prisoner's Dilemma

The Prisoner's Dilemma involves two players, each facing two choices: cooperate or defect <a class="yt-timestamp" data-t="00:02:43">[00:02:43]</a>. The outcomes are as follows <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>:
*   **Both Cooperate**: Each player receives three coins <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>.
*   **One Cooperates, One Defects**: The defector receives five coins, and the cooperator gets nothing <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.
*   **Both Defect**: Each player receives one coin <a class="yt-timestamp" data-t="00:02:59">[00:02:59]</a>.

The goal is to maximize one's own coins <a class="yt-timestamp" data-t="00:03:02">[00:03:02]</a>.

### The Paradox of Rationality

When analyzing the game, a rational player determines their best move regardless of the opponent's choice <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>:
*   **If the opponent cooperates**: Defecting yields five coins (vs. three for cooperating), making defection the better choice <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **If the opponent defects**: Defecting yields one coin (vs. zero for cooperating), making defection the better choice <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

Therefore, no matter what the opponent does, the best option is always to defect <a class="yt-timestamp" data-t="00:03:34">[00:03:34]</a>. If both players are rational, they will both defect, leading to a suboptimal outcome where each gets only one coin, even though they could have both received three by cooperating <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>.

This dilemma was evident in the US-Soviet nuclear arms race <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Both countries developed tens of thousands of nuclear weapons, enough to destroy each other many times over, at a cost of around $10 trillion <a class="yt-timestamp" data-t="00:04:15">[00:04:15]</a>. Despite neither being able to use them, they both acted in their own perceived best interest, resulting in a worse situation for everyone <a class="yt-timestamp" data-t="00:04:25">[00:04:25]</a>.

## The Repeated Prisoner's Dilemma

The Prisoner's Dilemma appears in many real-world scenarios, such as impalas grooming each other to remove ticks <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a>. Grooming requires time and resources, making it costly to help another impala <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. If they interact only once, the rational choice for each impala is to defect <a class="yt-timestamp" data-t="00:05:36">[00:05:36]</a>.

However, many real-world problems are not single interactions but repeated encounters, like impalas seeing each other daily <a class="yt-timestamp" data-t="00:05:50">[00:05:50]</a>. This changes the problem, as past actions can influence future interactions <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>.

### Axelrod's Tournaments

In 1980, political scientist Robert Axelrod conducted a computer tournament to discover the best strategy for the repeated Prisoner's Dilemma <a class="yt-timestamp" data-t="00:06:22">[00:06:22]</a>. He invited leading game theorists to submit computer programs, or strategies, to play against each other over 200 rounds <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. The goal was to win as many points as possible <a class="yt-timestamp" data-t="00:06:56">[00:06:56]</a>.

Among the 15 strategies submitted (including a random one), the winning strategy was surprisingly simple: [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] <a class="yt-timestamp" data-t="00:08:25">[00:08:25]</a>.

### [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] Strategy

[[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] starts by cooperating and then simply copies the opponent's previous move <a class="yt-timestamp" data-t="00:08:32">[00:08:32]</a>. It cooperates if the opponent cooperated and defects if the opponent defected, but only once; if the opponent returns to cooperating, so does [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] <a class="yt-timestamp" data-t="00:08:43">[00:08:43]</a>. For example, when playing against Friedman, which cooperated first and then defected permanently after any opponent defection, both [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] and Friedman cooperated throughout, achieving perfect scores <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. However, against Joss, which copied the last move but also defected 10% of the time, [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] and Joss engaged in alternating defections, an "echo effect," leading to poor scores for both <a class="yt-timestamp" data-t="00:09:03">[00:09:03]</a>. Despite this, [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] won the tournament by cooperating effectively with other strategies <a class="yt-timestamp" data-t="00:09:41">[00:09:41]</a>.

### Qualities of Successful Strategies

Axelrod identified four key qualities shared by the best-performing strategies, including [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] <a class="yt-timestamp" data-t="00:10:10">[00:10:10]</a>:

1.  **Nice**: Strategies that are never the first to defect <a class="yt-timestamp" data-t="00:10:17">[00:10:17]</a>. [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] is nice because it only defects in retaliation <a class="yt-timestamp" data-t="00:10:22">[00:10:22]</a>. In the first tournament, all top eight strategies were nice, and even the worst-performing nice strategy outscored the best nasty one <a class="yt-timestamp" data-t="00:10:42">[00:10:42]</a>.
2.  **Forgiving**: Strategies that retaliate but do not hold a grudge <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>. [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] is forgiving as it responds to defection but doesn't let past defections (before the last round) influence its current decision <a class="yt-timestamp" data-t="00:11:01">[00:11:01]</a>. In contrast, Friedman was maximally unforgiving <a class="yt-timestamp" data-t="00:11:08">[00:11:08]</a>.
3.  **Retaliatory (Provokable)**: If an opponent defects, the strategy immediately strikes back <a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>. This prevents being a pushover; for example, an "always cooperate" strategy is easily exploited <a class="yt-timestamp" data-t="00:14:50">[00:14:50]</a>. [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] is difficult to take advantage of <a class="yt-timestamp" data-t="00:14:54">[00:14:54]</a>.
4.  **Clear**: Simple and predictable programs that allow opponents to figure them out and establish patterns of trust <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Opaque or random strategies make it hard to cooperate <a class="yt-timestamp" data-t="00:15:13">[00:15:13]</a>.

These principles—being nice, forgiving, provokable, and clear—resemble the "eye for an eye" morality found in many cultures <a class="yt-timestamp" data-t="00:15:44">[00:15:44]</a>.

### The Second Tournament and Unknown Endings

Axelrod held a second tournament, with contestants having access to the first results and analysis <a class="yt-timestamp" data-t="00:12:29">[00:12:29]</a>. A crucial change was made: the number of rounds was not fixed at 200, but rather averaged 200, with a random number generator preventing players from knowing the exact end <a class="yt-timestamp" data-t="00:13:07">[00:13:07]</a>. If the end is known, rational players would defect in the last round, and by backward induction, this defection would propagate to the first round <a class="yt-timestamp" data-t="00:12:57">[00:12:57]</a>. An uncertain ending encourages continued cooperation <a class="yt-timestamp" data-t="00:13:17">[00:13:17]</a>.

Some contestants submitted nice and forgiving strategies, while others submitted nasty strategies, hoping to exploit the forgiving ones <a class="yt-timestamp" data-t="00:13:52">[00:13:52]</a>. For instance, Tester would defect first to probe its opponent and then either apologize and play [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] or defect every other move if the opponent didn't retaliate <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>. Despite the new entries, [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] again proved most effective <a class="yt-timestamp" data-t="00:14:16">[00:14:16]</a>. Nice strategies continued to perform significantly better overall <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

Interestingly, a more forgiving strategy like "[[tit_for_tat_strategy_in_iterative_games | Tit for Two Tats]]" (which defects only after its opponent defects twice in a row) would have won the first tournament but placed only 24th in the second <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. This highlights that there is no single best strategy in the repeated Prisoner's Dilemma; the optimal strategy depends on the environment and the other strategies present <a class="yt-timestamp" data-t="00:16:13">[00:16:13]</a>.

## Evolution of Cooperation

Axelrod conducted a simulation where successful strategies multiplied and unsuccessful ones dwindled, mimicking ecological or evolutionary processes <a class="yt-timestamp" data-t="00:16:41">[00:16:41]</a>. Nasty strategies, like Harrington, initially thrived by preying on others but quickly declined as their exploitable targets went extinct <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>. After a thousand generations, only nice strategies survived, with [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] being the most common, representing 14.5% of the total population <a class="yt-timestamp" data-t="00:17:21">[00:17:21]</a>.

This simulation suggests that even in a world populated by self-interested individuals, cooperation can emerge and spread <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. A small cluster of cooperative players, like [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] players, can accumulate benefits from cooperating with each other, leading to their growth and eventual dominance in the population <a class="yt-timestamp" data-t="00:18:02">[00:18:02]</a>. This provides a possible explanation for the emergence of cooperation in nature, from impalas grooming each other to fish cleaning sharks <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>. Such strategies can be encoded in DNA, allowing them to spread if they perform better than others <a class="yt-timestamp" data-t="00:19:18">[00:19:18]</a>.

## The Impact of Noise and Errors

Axelrod's original tournaments did not fully account for "noise" or random errors in communication <a class="yt-timestamp" data-t="00:19:40">[00:19:40]</a>. For example, a cooperative act might be misinterpreted as a defection <a class="yt-timestamp" data-t="00:19:44">[00:19:44]</a>. This is relevant to real-world scenarios, such as the 1983 incident where a Soviet early warning system mistook sunlight reflecting off clouds for a US ballistic missile launch <a class="yt-timestamp" data-t="00:20:03">[00:20:03]</a>. Fortunately, Soviet officer Stanislav Petrov dismissed the false alarm <a class="yt-timestamp" data-t="00:20:12">[00:20:12]</a>.

In a noisy environment, [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] playing against itself can lead to a chain of alternating retaliations if a cooperation is misinterpreted as a defection <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. This can cause both players to eventually default to constant mutual defection, significantly reducing their scores <a class="yt-timestamp" data-t="00:21:11">[00:21:11]</a>.

To solve this, a strategy needs a way to break out of echo effects <a class="yt-timestamp" data-t="00:21:25">[00:21:25]</a>. One solution is to play [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] with approximately 10% more forgiveness, retaliating only about nine out of ten times <a class="yt-timestamp" data-t="00:21:38">[00:21:38]</a>. This "generous [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]]" strategy allows for breaking retaliatory cycles while remaining sufficiently retaliatory to avoid exploitation <a class="yt-timestamp" data-t="00:21:41">[00:21:41]</a>.

### Winning Without Beating the Opponent

It's important to note that [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] can never achieve a higher score than the player it's playing with; it can only lose or draw <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>. Yet, when all interactions are tallied, it consistently comes out ahead of other strategies <a class="yt-timestamp" data-t="00:22:13">[00:22:13]</a>. Conversely, a strategy like "always defect" can never lose a game (only draw or win), but it performs extremely poorly overall <a class="yt-timestamp" data-t="00:22:23">[00:22:23]</a>.

This highlights a common misconception: winning does not always mean beating the other person <a class="yt-timestamp" data-t="00:22:31">[00:22:31]</a>. While games like chess or poker are zero-sum (one's gain is another's loss), most of life is not <a class="yt-timestamp" data-t="00:22:43">[00:22:43]</a>. Rewards can come from the environment (the "banker"), not solely from the opponent <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>. The goal is to find "win-win" situations and cooperate to unlock shared rewards <a class="yt-timestamp" data-t="00:23:00">[00:23:00]</a>.

## Real-World Applications and Continued Research

The insights from Axelrod's tournaments have been applied to various fields, including evolutionary biology and international conflicts <a class="yt-timestamp" data-t="00:19:30">[00:19:30]</a>. The US and Soviet Union, after decades of non-cooperation in nuclear arms development, began reducing their nuclear stockpiles from the late 1980s onwards <a class="yt-timestamp" data-t="00:23:17">[00:23:17]</a>. They applied the principles of the repeated Prisoner's Dilemma by disarming slowly, checking each other's cooperation annually, and repeating the process <a class="yt-timestamp" data-t="00:23:43">[00:23:43]</a>.

Over 40 years since Axelrod's tournaments, researchers continue to study optimal strategies in diverse environments, varying payoff structures, strategies, and errors <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>. While [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] or generous [[tit_for_tat_strategy_in_iterative_games | Tit for Tat]] don't always win, Axelrod's core takeaways remain: be nice, forgiving, but don't be a pushover <a class="yt-timestamp" data-t="00:24:13">[00:24:13]</a>.

Game theory highlights that life involves choices that shape not only one's own future but also the future of those one interacts with <a class="yt-timestamp" data-t="00:25:00">[00:25:00]</a>. In the short term, the environment may dictate which players succeed, but in the long run, the players themselves shape the environment <a class="yt-timestamp" data-t="00:25:11">[00:25:11]</a>. Making wise choices in the "game of life" can have far-reaching impacts <a class="yt-timestamp" data-t="00:25:19">[00:25:19]</a>.