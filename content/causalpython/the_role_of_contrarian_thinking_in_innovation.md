---
title: The Role of Contrarian Thinking in Innovation
videoId: pKhUuwxBdX4
---

From: [[causalpython]] <br/> 

Calen started in 2017, when causal AI was a very niche topic, making the early experience of building the community feel "very lonely" to its founders [00:00:07]. Despite this, they believed it would one day become significant and focused on laying strong foundations to support future growth [00:00:31]. This approach stemmed from a "contrarian bet" [00:00:57].

## Origins in the Hedge Fund World

The decision to pursue causal AI was heavily influenced by the co-founders' backgrounds in hedge funds. The speaker, a computer scientist, and co-founder Max, a physicist, both worked in the hedge fund world before starting Calen [00:01:07].

At the time, following AlphaGo's victory over the Go world champion, there was widespread excitement about deep learning, with many pivoting their AI research towards it, believing it would solve everything [00:01:24]. However, the co-founders held a "very contrarian view" [00:01:52]. They recognized that while deep learning excelled in certain situations, like board games with fixed rules, it could lead to trouble in the real world by solely [[Causality in marketing and decisionmaking | learning historical patterns]] [00:01:55]. Their experience in finance demonstrated that "the past almost never repeats in financial markets," and relying on correlations alone was problematic [00:02:12].

A key lesson from the hedge fund world was that "the way to win big is to take a contrarian view" [00:02:25]. While doing what everyone else does yields small returns, significant gains come from doing something "completely different" [00:02:30]. The speaker emphasizes that being contrarian isn't enough; one must be "contrarian and right" [00:02:43]. Fortunately, causal AI proved to be a contrarian bet that was "right and is becoming more right by the day" [00:02:49].

## Key Lessons from Contrarian Bets

Two primary lessons were learned from the hedge fund environment that informed the move into causal AI:
*   **Nature of Patterns** The understanding that in the real world, patterns can change rapidly, and historical data isn't necessarily predictive of the future [00:03:09].
*   **Taking Calculated Risks** The importance of taking a bet on a different approach [00:03:27].

## Career Path Towards Causality

The speaker's personal career trajectory further reinforced the need for a contrarian approach. During their PhD in computer vision, focusing on biometrics, they found that deep learning performed "incredibly well in the lab" where backgrounds and conditions were controlled [00:03:51]. However, "soon as we took out the Deep learning in the real world, it all broke down catastrophically" [00:04:26].

In contrast, a model-based approach, which involved understanding the underlying structure (e.g., human body features for recognition), performed slightly worse in the lab but "retained its performance" in the real world, demonstrating much better generalization [00:04:52]. This experience highlighted a core motivation for causality: without understanding the "cause and effect mechanisms," models might excel in controlled lab settings but fail in real-world applications [00:05:40]. A significant challenge in enterprise AI is that 85-90% of projects never make it out of the lab, often due to catastrophic failure or a lack of trust from human users who don't understand the underlying causal model [00:05:59].

Causality addresses two fundamental needs for taking AI from the lab to the real world: ensuring the system works effectively in diverse environments and building human trust through transparency and explainability [00:06:36].

### Real-World Application Example

A recent client example illustrates this point:
1.  **The Problem** A client sought to model a physical manufacturing system with inherent cause-and-effect mechanisms [00:07:23].
2.  **Deep Learning Failure** They initially used deep learning, which worked well in the lab but failed catastrophically in the real world [00:08:18]. Even after working with six deep learning companies, performance improved, but senior leadership didn't understand how the system worked or its real-world connectivity, leading them to abandon AI [00:08:52].
3.  **Causal AI Success** A data scientist discovered causal AI, and upon implementing automated [[Causality in marketing and decisionmaking | causal discovery]], a "digital twin" of the machine was created [00:09:23]. This causal diagram was then presented to domain experts, who could validate and refine it, identifying specific physical connections or disconnections [00:09:48]. This iterative process, where humans are involved from the very beginning, is fundamentally different from deep learning approaches where data is simply thrown at a model [00:10:29].