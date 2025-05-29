---
title: Lessons from failure in engineering projects
videoId: Z9ftpRhRiJE
---

From: [[lennyspodcast]] <br/> 

## The Dig V4 Rewrite: A Case Study in Failure

The Dig V4 rewrite serves as a potent example of a challenging engineering project that, despite heroic efforts, ultimately did not save the company, yet provided invaluable [[the_personal_development_of_a_founder_and_leadership_lessons | personal development]] and [[lessons_in_leadership_and_team_management | lessons in leadership and team management]].

### The Context and Problem
Around 2012, Dig, a social news aggregator, was losing market share to social networks like Twitter and Facebook, as well as Reddit <a class="yt-timestamp" data-t="01:03:08">[01:03:08]</a>. The fear was that aggregated news would be outcompeted <a class="yt-timestamp" data-t="01:03:15">[01:03:15]</a>. The existing version of the platform could not support the necessary social functionality <a class="yt-timestamp" data-t="01:03:32">[01:03:32]</a>. An SEO change further exacerbated the situation, causing traffic and monetization to decline, putting the company "on fire" <a class="yt-timestamp" data-t="01:10:13">[01:10:13]</a>.

### The Decision to Rewrite
The decision was made to undertake a complete rewrite of the platform to incorporate social features <a class="yt-timestamp" data-t="01:03:49">[01:03:49]</a>. This decision was made about two and a half years before the new version was launched <a class="yt-timestamp" data-t="01:03:41">[01:03:41]</a>.

>[!warning] Complete Rewrites
>A complete rewrite of a system "never works out for anyone" <a class="yt-timestamp" data-t="01:03:51">[01:03:51]</a>.

### The "Death March" and Disastrous Launch
The project was characterized by a "Death March" as the team pushed intensely to release the new version <a class="yt-timestamp" data-t="01:03:35">[01:03:35]</a>. This was before the widespread adoption of cloud services, so the team wiped and reimaged nearly all existing servers to transition to the new software <a class="yt-timestamp" data-t="01:04:41">[01:04:41]</a>.

Upon attempting to launch, the site continuously crashed <a class="yt-timestamp" data-t="01:04:49">[01:04:49]</a>. It took approximately a month to get the site fully functional again <a class="yt-timestamp" data-t="01:04:52">[01:04:52]</a>. For much of that month, the actual user functionality was not working properly <a class="yt-timestamp" data-t="01:08:54">[01:08:54]</a>. While a read-only version was back up in about three days, the core functionality remained broken <a class="yt-timestamp" data-t="01:08:51">[01:08:51]</a>.

### Technical Challenges and Solutions
During the month-long recovery, only about five people were still actively trying to get the site back up <a class="yt-timestamp" data-t="01:05:08">[01:05:08]</a>. Within the first two days, a caching system had to be written from scratch, which helped get the site partially online, though it still required every server to be restarted every 12 hours <a class="yt-timestamp" data-t="01:05:24">[01:05:24]</a>.

The core bug causing the 12-hour crashes was identified about three weeks later <a class="yt-timestamp" data-t="01:05:48">[01:05:48]</a>. It was an "incredibly simple issue" related to how Python initiates variables used as default parameters <a class="yt-timestamp" data-t="01:05:54">[01:05:54]</a>. The bug was introduced by someone new to Python who didn't realize the issue, and it wasn't caught during review <a class="yt-timestamp" data-t="01:06:09">[01:06:09]</a>. It didn't break anything directly but caused significant extra load on servers <a class="yt-timestamp" data-t="01:06:21">[01:06:21]</a>.

>[!info] Anti-Patterns
>The rapid development of a caching system and the debugging process were a "series of anti-patterns" <a class="yt-timestamp" data-t="01:05:32">[01:05:32]</a>.

### Outcome and Personal Impact
Despite the team's heroic efforts to get the site working again, the company "still went to zero," running out of money and eventually selling for parts <a class="yt-timestamp" data-t="01:06:35">[01:06:35]</a>. A new CEO arrived a few weeks after the difficult launch, initiating layoffs <a class="yt-timestamp" data-t="01:06:45">[01:06:45]</a>. Nine months after joining, the engineering team had shrunk from 100 people to about 30 <a class="yt-timestamp" data-t="01:06:53">[01:06:53]</a>.

This challenging experience, however, was "truly phenomenal" for personal growth <a class="yt-timestamp" data-t="01:02:45">[01:02:45]</a>. It shaped Will Larson's perspective on early career development, highlighting the value of joining a struggling company <a class="yt-timestamp" data-t="01:07:07">[01:07:07]</a>. Despite not being qualified, Will became a manager and essentially ran the entire engineering team due to others quitting or being laid off <a class="yt-timestamp" data-t="01:07:16">[01:07:16]</a>. This "kernel" experience shaped his entire career <a class="yt-timestamp" data-t="01:07:40">[01:07:40]</a>.

## General Lessons on Overcoming Challenges

### Empowering Engineers as Peers
Engineers are often treated "a little bit like children" instead of being given the responsibility to thrive as adults <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>. This includes sheltering them from "what is important" or the "real problem" <a class="yt-timestamp" data-t="00:00:13">[00:00:13]</a>, <a class="yt-timestamp" data-t="00:07:09">[00:07:09]</a>. Historically, this "coddling" happened to improve retention <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.

However, there's a shift towards treating engineers as peers, enabling them to take on senior leadership roles <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. This means leaders can give engineers "real hard problems" and hold them accountable <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. Accountability allows engineers to be placed in senior roles, offering them the growth opportunities they seek <a class="yt-timestamp" data-t="00:08:23">[00:08:23]</a>.

### Understanding and Addressing Incentives in Teams
Misaligned incentives are a core problem in many Engineering Manager (EM) and Product Manager (PM) partnerships <a class="yt-timestamp" data-t="00:41:44">[00:41:44]</a>. While it's rare for individuals to be "villains," complex incentives can lead to conflicts <a class="yt-timestamp" data-t="00:42:26">[00:42:26]</a>. For example, a PM might prioritize a sales commitment vital for their promotion, while the EM knows it's technically unfeasible <a class="yt-timestamp" data-t="00:42:05">[00:42:05]</a>.

To improve these relationships, both EMs and PMs should prioritize understanding each other's true needs before attempting to solve conflicts <a class="yt-timestamp" data-t="00:43:02">[00:43:02]</a>. Often, a compromise solution exists that can satisfy everyone's needs if there's a deep understanding of what each party truly wants, which might not be what they initially articulate <a class="yt-timestamp" data-t="00:43:27">[00:43:27]</a>.

>[!tip] Shared Accountability
>A powerful approach to addressing misaligned incentives is to ensure that EM and PM pairs generally receive the same performance rating <a class="yt-timestamp" data-t="00:44:06">[00:44:06]</a>. This encourages them to work together and evaluate problems based on the entire set of constraints, rather than just their functional constraints <a class="yt-timestamp" data-t="00:45:15">[00:45:15]</a>. This approach can extend to other functions like design managers or even business leadership in a "trifecta" model <a class="yt-timestamp" data-t="00:45:00">[00:45:00]</a>.

A common stressor for EMs is balancing the product team's need for numerous, sometimes "boring" experiments with the engineers' desire for "interesting work" like building something brand new <a class="yt-timestamp" data-t="00:47:06">[00:47:06]</a>. If a PM doesn't understand these "invisible constraints" on the EM, it can make the EM seem unreliable <a class="yt-timestamp" data-t="00:47:50">[00:47:50]</a>.

### Embracing Systems Thinking for Problem Diagnosis
Systems thinking involves conceptualizing problems in terms of "stocks" (things that accumulate, like fish in a lake or candidates in a pipeline) and "flows" (movement between stocks) <a class="yt-timestamp" data-t="00:11:43">[00:11:43]</a>. This approach helps in modeling reality to improve diagnosis <a class="yt-timestamp" data-t="00:52:52">[00:52:52]</a>.

>[!warning] Reality is Always Right
>A common mistake in systems thinking is believing "reality is wrong" when it conflicts with a model <a class="yt-timestamp" data-t="00:09:24">[00:09:24]</a>. Instead, "your model is always wrong if it's in conflict with reality" <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. The conflict highlights where your mental model is flawed, allowing for learning and improvement <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

An example of applying systems thinking is analyzing a hiring pipeline <a class="yt-timestamp" data-t="00:13:15">[00:13:15]</a>. By mapping stocks (potential candidates, sourced candidates, screened candidates, etc.) and flows (conversion rates between stages), one can identify bottlenecks. For instance, if many candidates reach the offer stage but few accept, the problem lies in the offer acceptance rate, not necessarily the sourcing <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.

This diagnostic power helps target efforts effectively, preventing teams from making "big changes with no data behind them" <a class="yt-timestamp" data-t="00:15:38">[00:15:38]</a>.

### Defining and Using Engineering Strategy
While many companies lack a written strategy, every function implicitly has one <a class="yt-timestamp" data-t="00:16:53">[00:16:53]</a>. The first step to improvement is writing it down, allowing for debugging and consistent application <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

Good strategy, though often "boring," clarifies how future decisions are made and aligns efforts with company priorities <a class="yt-timestamp" data-t="00:19:07">[00:19:07]</a>. For example, a strategy of "we only use the tools we have today" might frustrate some engineers, but it focuses energy on valued company problems rather than building new tooling <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>.

>[!example] Engineering Strategies
>*   **Self-hosted data centers**: Uber's policy of only using its own data centers (no cloud) allowed rapid expansion into new geopolitical regions, despite requiring significant internal development <a class="yt-timestamp" data-t="00:22:07">[00:22:07]</a>.
>*   **Monolithic codebase**: Stripe's "Ruby monolith" policy focused engineers on building innovative features rather than supporting multiple programming languages <a class="yt-timestamp" data-t="00:23:25">[00:23:25]</a>.

The common theme in effective strategies is [[engineering_leadership_and_management_strategies | constraint]]: intentionally limiting options to accelerate progress and focus on critical matters <a class="yt-timestamp" data-t="00:24:18">[00:24:18]</a>. Bad strategies often stem from a "willful disbelief of what an accurate diagnosis is," leading to incoherent guiding policies <a class="yt-timestamp" data-t="00:24:58">[00:24:58]</a>.

### Measuring Engineering Productivity
The challenge of measuring engineering productivity is amplified during periods of team reduction and increased pressure for efficiency <a class="yt-timestamp" data-t="00:48:45">[00:48:45]</a>.

Common approaches:
1.  **Benchmarking against funding**: This mechanical exercise provides a defensible answer to investors but doesn't offer insights for effective organizational management <a class="yt-timestamp" data-t="00:49:16">[00:49:16]</a>.
2.  **Listening to engineers**: Engineers often know if their teams are effective and why not, providing "crumbs" for leaders to investigate further <a class="yt-timestamp" data-t="00:50:31">[00:50:31]</a>.
3.  **Aligning evaluation to business/product goals**: Engineering effectiveness should be tied directly to product goals and customer value, rather than internal metrics alone <a class="yt-timestamp" data-t="00:51:27">[00:51:27]</a>.
4.  **Showcasing valuable work**: Regularly demonstrating the "meaningful meaty things" with tangible impact helps manage concerns from leadership <a class="yt-timestamp" data-t="00:52:03">[00:52:03]</a>.

While metrics like the DORA metrics (lead time, incident remediation time, failure rate, etc.) are excellent for *diagnosis*—showing where to improve—they don't directly tell you if a team is "good" or "bad" <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>.

>[!tip] Measure Something Imperfectly
>Engineers often resist measuring anything due to concerns about accuracy <a class="yt-timestamp" data-t="00:54:21">[00:54:21]</a>. However, it's better to "get comfortable measuring something that's not perfect but you can actually measure" <a class="yt-timestamp" data-t="00:54:41">[00:54:41]</a>. These imperfect metrics create opportunities to educate stakeholders on the nuances of engineering <a class="yt-timestamp" data-t="00:54:50">[00:54:50]</a>.

### Crafting Meaningful Company Values
Company values should be:
1.  **Honest**: They must accurately reflect actual decisions and behaviors, not just aspirations <a class="yt-timestamp" data-t="00:57:07">[00:57:07]</a>. Values like "users first" are only valuable if consistently applied, otherwise, they undermine confidence <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>.
2.  **Applicable**: Values should guide real-world decisions. For instance, whether to "optimize globally" for the organization or "do what's good for your team" <a class="yt-timestamp" data-t="00:57:33">[00:57:33]</a>.
3.  **Reversible**: Good values imply a clear alternative that the company *doesn't* do <a class="yt-timestamp" data-t="00:59:01">[00:59:01]</a>. For example, "we build good software" is not a useful value because no company would claim to build bad software <a class="yt-timestamp" data-t="00:59:05">[00:59:05]</a>. Values like "Integrity" are often "identity values" that describe who you *want* to be but offer no practical guidance <a class="yt-timestamp" data-t="00:59:28">[00:59:28]</a>.

Truly useful values help define who "doesn't quite fit" in the company, acting as a hiring filter <a class="yt-timestamp" data-t="01:00:40">[01:00:40]</a>. If a value applies to everyone, it's not unique or helpful <a class="yt-timestamp" data-t="01:01:01">[01:01:01]</a>. Values should describe "who you are, not who you want to be and aspire to be" <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

### Embracing the "Long Game" in Content Creation
For those aspiring to write, a key lesson is to focus on sustainability and passion. Writing "what you want to write" and where there is "energy" is crucial for long-term consistency <a class="yt-timestamp" data-t="00:30:00">[00:30:00]</a>. Conversely, writing for financial gain or on a strict schedule can be draining <a class="yt-timestamp" data-t="00:27:45">[00:27:45]</a>.

The biggest risk for writers and content creators is "quitting soon" due to burnout, rather than slow initial growth <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>. It's never "too late" to start, as consistent creation of quality content builds an audience over time <a class="yt-timestamp" data-t="00:32:56">[00:32:56]</a>. The focus should be on finding something that can be maintained for a decade, not just a year <a class="yt-timestamp" data-t="00:33:20">[00:33:20]</a>. Success in the "infinite game" of content creation comes from persistence <a class="yt-timestamp" data-t="00:33:59">[00:33:59]</a>.

>[!tip] Aligning Work and Writing
>One way to find time for writing while having an intense full-time job is to choose topics that "directly relate to what I'm working on" <a class="yt-timestamp" data-t="00:35:47">[00:35:47]</a>. This allows writing to refine thinking and improve performance at work, creating alignment rather than conflict <a class="yt-timestamp" data-t="00:36:27">[00:36:27]</a>.

For those aiming for career advancement through writing, focus on creating "two or three really good things" with extensive drafting, revision, and feedback, rather than starting a long-running blog <a class="yt-timestamp" data-t="00:37:55">[00:37:55]</a>. However, for consistent, high-volume writing, the advice is to "just publish" most of what you write, without excessive concern for perfection <a class="yt-timestamp" data-t="00:38:35">[00:38:35]</a>. This approach allows for learning and evolving as a thinker <a class="yt-timestamp" data-t="00:39:13">[00:39:13]</a>.

>[!quote] "Hard to work with"
>One piece of underappreciated writing by Will Larson, "Hard to work with," addresses talented individuals who are viewed as "combative or difficult to work with" because they hold peers to high standards <a class="yt-timestamp" data-t="01:14:34">[01:14:34]</a>. This often stems from a personal struggle of trying to enforce high standards while being perceived negatively <a class="yt-timestamp" data-t="01:14:47">[01:14:47]</a>.

### Embracing Challenges and Difficult Decisions
Often, the most interesting and impactful experiences are those that are "so bad and hard" in the moment <a class="yt-timestamp" data-t="01:07:52">[01:07:52]</a>. These situations, though not voluntarily chosen, foster strong bonds and a collective desire to overcome challenges with respected colleagues <a class="yt-timestamp" data-t="01:16:12">[01:16:12]</a>.

>[!quote] "There's no way around, just through"
>A motto from a challenging time at Uber: "There's no way around, just through" <a class="yt-timestamp" data-t="01:13:47">[01:13:47]</a>. This emphasizes gutting through difficulties to reach the other side.

For many daily decisions, leaders should ask: "will anyone remember what we decided in six months?" <a class="yt-timestamp" data-t="01:14:01">[01:14:01]</a>. Most decisions aren't that important, and stressing over them is unproductive <a class="yt-timestamp" data-t="01:14:07">[01:14:07]</a>. It's better to make a "reasonable" choice and move on to more significant matters <a class="yt-timestamp" data-t="01:14:14">[01:14:14]</a>.