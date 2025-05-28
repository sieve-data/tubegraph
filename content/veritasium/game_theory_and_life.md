---
title: game theory and life
videoId: mScpHTIi-kM
---

From: [[veritasium]] <br/> 

Game theory provides a framework for understanding situations where individuals make choices that affect each other, with widespread applications from international conflict to daily interactions <a class="yt-timestamp" data-t="00:00:03">[00:00:03]</a>. Figuring out optimal [[strategies in repeated games | strategies]] in these scenarios can determine outcomes ranging from war and peace to flourishing and destruction <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. Within the mechanics of these games, the very source of unexpected phenomena like [[evolutionary_biology_and_cooperation | cooperation]] can be found <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>.

## The Cold War Context and the Birth of a Problem

On September 3, 1949, an American weather monitoring plane detected radioactive material in air samples over Japan <a class="yt-timestamp" data-t="00:00:34">[00:00:34]</a>. Subsequent testing by the Navy confirmed the presence of Cerium-141 and Yttrium-91, isotopes with short half-lives, indicating a recent nuclear explosion <a class="yt-timestamp" data-t="00:00:52">[00:00:52]</a>. Since the U.S. had conducted no tests that year, the conclusion was that the Soviet Union had developed a nuclear bomb <a class="yt-timestamp" data-t="00:01:09">[00:01:09]</a>.

This news posed a serious threat to Western Europe and the United States, raising fears of imminent war <a class="yt-timestamp" data-t="00:01:30">[00:01:30]</a>. Some advised a pre-emptive nuclear strike against the Soviets <a class="yt-timestamp" data-t="00:01:37">[00:01:37]</a>. John von Neumann, a founder of game theory, advocated for immediate action, stating, "If you say why not bomb them tomorrow, I say, why not bomb them today?" <a class="yt-timestamp" data-t="00:01:51">[00:01:51]</a>.

In 1950, the RAND Corporation, a U.S. think tank, turned to game theory to study the nuclear weapons problem <a class="yt-timestamp" data-t="00:02:11">[00:02:11]</a>. That same year, two mathematicians at RAND invented a game that mirrored the U.S.-Soviet conflict, now known as the **Prisoner's Dilemma** <a class="yt-timestamp" data-t="00:02:21">[00:02:21]</a>.

### Understanding the Prisoner's Dilemma

The Prisoner's Dilemma involves two players, each with two choices: cooperate or defect <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   If both cooperate, they each receive three coins <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>.
*   If one cooperates and the other defects, the defector gets five coins, and the cooperator gets nothing <a class="yt-timestamp" data-t="00:02:50">[00:02:50]</a>.
*   If both defect, they each receive one coin <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.

The goal is to maximize one's own coins <a class="yt-timestamp" data-t="00:03:01">[00:03:01]</a>.
If an opponent cooperates, defecting yields five coins instead of three <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. If an opponent defects, defecting yields one coin instead of zero <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. Thus, regardless of the opponent's choice, defecting is always the "rational" individual choice <a class="yt-timestamp" data-t="00:03:31">[00:03:31]</a>.

However, if both players act rationally, they both defect and end up with one coin each, a suboptimal outcome compared to the three coins they could have received through mutual cooperation <a class="yt-timestamp" data-t="00:03:44">[00:03:44]</a>.

This outcome mirrored the U.S. and Soviet Union's development of vast nuclear arsenals, spending around $10 trillion, when both would have been better off cooperating to limit this technology <a class="yt-timestamp" data-t="00:03:54">[00:03:54]</a>. Their self-interested actions led to a worse situation for everyone <a class="yt-timestamp" data-t="00:04:22">[00:04:22]</a>.

## The Emergence of Cooperation in Repeated Games

The Prisoner's Dilemma appears in numerous real-world situations <a class="yt-timestamp" data-t="00:04:39">[00:04:39]</a>. For example, impalas grooming each other to remove ticks, where grooming costs resources <a class="yt-timestamp" data-t="00:04:44">[00:04:44]</a>. If they only interact once, the rational choice is to defect and not groom, as the other impala won't help in return <a class="yt-timestamp" data-t="00:05:34">[00:05:34]</a>.

However, many real-life problems involve repeated interactions, like impalas seeing each other daily <a class="yt-timestamp" data-t="00:05:43">[00:05:43]</a>. This changes the dynamic, as past defections can influence future interactions <a class="yt-timestamp" data-t="00:06:02">[00:06:02]</a>.

### Axelrod's Tournaments on [[strategies in repeated games | Strategies in Repeated Games]]

In 1980, political scientist Robert Axelrod conducted a computer tournament to discover the best strategy for the repeated Prisoner's Dilemma <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. He invited game theorists to submit computer programs (strategies) that would play against each other over 200 rounds <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. The games were repeated five times to ensure robustness <a class="yt-timestamp" data-t="00:06:58">[00:06:58]</a>. Crucially, the exact number of rounds was not known with certainty, preventing a "backwards induction" problem that would lead to universal defection <a class="yt-timestamp" data-t="00:13:00">[00:13:00]</a>.

Out of 15 submitted strategies (including a random one) <a class="yt-timestamp" data-t="00:07:16">[00:07:16]</a>, the simplest program, **Tit for Tat**, emerged as the winner <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

#### The Winning Strategy: Tit for Tat

Tit for Tat's rules are simple:
1.  Start by cooperating <a class="yt-timestamp" data-t="00:08:28">[00:08:28]</a>.
2.  Then, copy the opponent's last move <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.

When Tit for Tat played against another cooperative strategy like Friedman (which defects only after one opponent defection), both cooperated throughout and achieved perfect scores <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. However, against strategies like Joss (which randomly defects 10% of the time) <a class="yt-timestamp" data-t="00:07:50">[00:07:50]</a>, Tit for Tat would retaliate, leading to cycles of mutual defection <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>. Despite these poor individual matches, Tit for Tat won the tournament by cooperating effectively with enough other strategies <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.

#### Qualities of Successful Strategies

Axelrod identified four key qualities shared by the best-performing strategies, including Tit for Tat <a class="yt-timestamp" data-t="00:10:08">[00:10:08]</a>:

1.  **Nice**: Not being the first to defect <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. All top eight strategies were "nice," and the worst-performing nice strategy still outscored the best "nasty" (first-to-defect) strategy <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>.
2.  **Forgiving**: Retaliating but not holding a grudge, not letting past defections (before the last round) influence current decisions <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>. Friedman, for example, was maximally unforgiving, defecting for the rest of the game after a single opponent defection, which proved suboptimal in the long run <a class="yt-timestamp" data-t="00:11:05">[00:11:05]</a>. This finding—that it pays to be nice and forgiving—shocked experts who had tried complex, tricky strategies <a class="yt-timestamp" data-t="00:11:23">[00:11:23]</a>.
3.  **Retaliatory**: Striking back immediately if the opponent defects, not being a pushover <a class="yt-timestamp" data-t="00:14:38">[00:14:38]</a>. Strategies like "Always Cooperate" are easily exploited <a class="yt-timestamp" data-t="00:14:47">[00:14:47]</a>.
4.  **Clear**: Being easy to understand and predictable in behavior <a class="yt-timestamp" data-t="00:14:59">[00:14:59]</a>. Opaque or random-like programs made it hard to establish trust, leading opponents to default to defection <a class="yt-timestamp" data-t="00:15:01">[00:15:01]</a>.

These four principles—being nice, forgiving, provokable, and clear—remarkably resemble the "eye for an eye" morality found in many cultures <a class="yt-timestamp" data-t="00:15:31">[00:15:31]</a>.

### The Impact of Noise and Generosity

Axelrod conducted a second tournament, where contestants had the results and analysis from the first <a class="yt-timestamp" data-t="00:13:21">[00:13:21]</a>. Some submitted nice, forgiving strategies, while others submitted nasty ones, hoping to exploit the forgiving nature of others <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>. Still, "nasty" didn't pay; Tit for Tat won again <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

However, a critical factor for real-world application is the presence of **noise** or random error <a class="yt-timestamp" data-t="00:19:36">[00:19:36]</a>. For instance, a cooperation might be perceived as a defection <a class="yt-timestamp" data-t="00:19:42">[00:19:42]</a>. An example is the 1983 Soviet false alarm of a U.S. missile launch due to sunlight reflecting off clouds <a class="yt-timestamp" data-t="00:19:50">[00:19:50]</a>.

In a noisy environment, Tit for Tat playing against itself can lead to a cycle of alternating retaliations if an error occurs <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. This significantly reduces their scores <a class="yt-timestamp" data-t="00:21:08">[00:21:08]</a>. To break these "echo effects," strategies need a way to re-establish cooperation <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. One solution is **Generous Tit for Tat**, which retaliates only about nine out of ten times, introducing forgiveness to break cycles while remaining retaliatory <a class="yt-timestamp" data-t="00:21:27">[00:21:27]</a>.

## Life as a Non-Zero-Sum Game

A key insight from these tournaments is that there is no single "best" strategy in the repeated Prisoner's Dilemma, as performance depends on the other strategies in the environment <a class="yt-timestamp" data-t="00:16:06">[00:16:06]</a>.

Axelrod's ecological simulation, where successful strategies increased in number and unsuccessful ones declined, showed that even in a "nasty" world dominated by defection, small clusters of cooperative players (like Tit for Tat) could emerge and spread, eventually taking over the population <a class="yt-timestamp" data-t="00:17:35">[00:17:35]</a>. This suggests that cooperation can emerge even among self-interested individuals, without requiring altruism <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

This concept could explain how [[evolutionary_biology_and_cooperation | cooperation]] arose and flourished in life, from impalas grooming to fish cleaning sharks <a class="yt-timestamp" data-t="00:18:38">[00:18:38]</a>. The strategies don't require conscious thought but can be encoded in DNA, allowing successful cooperative strategies to take over a population <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>.

> [00:22:27] This highlights a common misconception because for many people when they think about winning, they think they need to beat the other person. In games like chess or poker, this is true since one person's gain is necessarily another person's loss, so these games are zero sum. But most of life is not zero sum. To win, you don't need to get your reward from the other player. Instead, you can get it from the banker. Only in real life, the banker is the world. It is literally everything around you. It is just up to us to find those win-win situations, and then work together to unlock those rewards. Cooperation pays even among rivals.

From 1950 to 1986, the U.S. and Soviet Union struggled to cooperate on nuclear disarmament <a class="yt-timestamp" data-t="00:23:08">[00:23:08]</a>. However, from the late 1980s onward, they began reducing their nuclear stockpiles <a class="yt-timestamp" data-t="00:23:15">[00:23:15]</a>. They learned to disarm slowly, checking each other for mutual cooperation and repeating the process yearly, effectively turning a single Prisoner's Dilemma into a repeated game <a class="yt-timestamp" data-t="00:23:24">[00:23:24]</a>.

Axelrod's main takeaways still hold true: to navigate the "game of life" effectively, be nice, forgiving, but don't be a pushover <a class="yt-timestamp" data-t="00:24:09">[00:24:09]</a>. While the environment shapes the player in the short term, in the long run, players shape the environment <a class="yt-timestamp" data-t="00:25:02">[00:25:02]</a>.

## Enhance Your Problem-Solving Skills

Figuring out the best strategy requires critical thinking and innovative solutions <a class="yt-timestamp" data-t="00:25:30">[00:25:30]</a>. For those looking to build [[probability_theory_in_problem_solving | problem-solving skills]], resources like Brilliant offer courses in areas such as math, data science, programming, and technology <a class="yt-timestamp" data-t="00:25:40">[00:25:40]</a>. Their "Intro to Probability" course, for example, teaches how to construct and analyze models of real-world situations and build computer simulations to test strategies, much like Axelrod's tournaments <a class="yt-timestamp" data-t="00:26:06">[00:26:06]</a>.