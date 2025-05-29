---
title: The future of AI integrating generative AI and causal AI
videoId: pKhUuwxBdX4
---

From: [[causalpython]] <br/> 

The field of AI is rapidly evolving, with significant advancements in both [[Generative AI and causal reasoning | generative AI]] and [[Causality in AI | causal AI]]. While these two areas offer distinct strengths, their combination holds substantial, yet largely unexploited, potential for the future of intelligent systems and decision-making <a class="yt-timestamp" data-t="19:34:00">[19:34:00]</a>.

## The Contrarian Bet on Causal AI

In 2017, [[Causality in AI | causal AI]] was a niche topic <a class="yt-timestamp" data-t="00:07:07">[00:07:07]</a>. At a time when deep learning was gaining immense excitement following events like AlphaGo beating the world champion at Go <a class="yt-timestamp" data-t="01:30:00">[01:30:00]</a>, many AI researchers pivoted their focus towards deep learning, believing it would solve everything <a class="yt-timestamp" data-t="01:38:00">[01:38:00]</a>.

However, a contrarian view held that while deep learning excels in situations with fixed rules, such as board games <a class="yt-timestamp" data-t="01:58:00">[01:58:00]</a>, its reliance on learning historical patterns can lead to trouble in the real world <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>. Experience in the hedge fund world demonstrated that financial markets rarely repeat past patterns, making correlation-based approaches insufficient <a class="yt-timestamp" data-t="02:12:00">[02:12:00]</a>. This realization highlighted the need for a deeper understanding of cause and effect, leading to the development of [[Causal AI and machine learning intersection | causal AI]] <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.

### Limitations of Deep Learning in the Real World

During PhD research in computer vision, deep learning models showed incredible performance in lab settings where backgrounds and conditions were consistent. More data consistently improved deep learning performance <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. Yet, when these models were deployed in the real world, they catastrophically failed <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>.

In contrast, model-based approaches, which focused on understanding the underlying structure (e.g., how human body parts move, 3D facial shapes), retained their performance in the real world despite slightly worse lab results <a class="yt-timestamp" data-t="05:19:00">[05:19:00]</a>. This demonstrated that without understanding cause-and-effect mechanisms, models struggle to generalize <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

This issue persists in the enterprise today, where 85-90% of projects never make it out of the lab <a class="yt-timestamp" data-t="05:59:00">[05:59:00]</a>. The fundamental reasons are:
1.  Failure to deliver in the real world <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.
2.  Lack of trust from human users who do not understand the underlying causal model <a class="yt-timestamp" data-t="06:24:00">[06:24:00]</a>.

[[Causality in AI | Causality in AI]] helps address these two critical challenges, enabling AI to move from the lab to real-world applications <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

## Real-World Application of Causal AI: Manufacturing Process Modeling

A concrete example of [[Causal AI and its application in different sciences | causal AI]]'s success comes from a client modeling a physical manufacturing system with inherent cause-and-effect relationships (e.g., connected cogs or chains) <a class="yt-timestamp" data-t="07:23:00">[07:23:00]</a>.

Initially, the client attempted to solve this with deep learning, which performed well in the lab but failed catastrophically upon deployment in the real world <a class="yt-timestamp" data-t="08:18:00">[08:18:00]</a>. Even after engaging six deep learning companies, performance improvement was limited, and senior leadership couldn't understand or trust how the system worked <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>. They considered abandoning AI altogether <a class="yt-timestamp" data-t="09:16:00">[09:16:00]</a>.

Upon trying [[Causality in AI | causal AI]], automated [[Causal AI and machine learning intersection | causal discovery]] was performed on their data, essentially creating a "digital twin" of the machine <a class="yt-timestamp" data-t="09:35:00">[09:35:00]</a>. This proposed causal diagram was then given to domain experts who could validate and refine it, identifying specific links that were either incorrectly detected or missed by the algorithm due to a lack of historical faults <a class="yt-timestamp" data-t="09:51:00">[09:51:00]</a>. This highlights the iterative nature of the [[Causal AI and machine learning intersection | causal discovery]] process, where humans are involved from the very beginning, a fundamental difference from the "throw data at it" approach of deep learning and [[Generative AI and causal reasoning | generative AI]] <a class="yt-timestamp" data-t="10:29:00">[10:29:00]</a>.

## The Synergy: Generative AI and Causal AI

The future of AI lies in combining the strengths of both [[Generative AI and causal reasoning | generative AI]] and [[Causality in AI | causal AI]]. While each is powerful individually, their integration offers a synergistic effect where "1 + 1 equals 3" <a class="yt-timestamp" data-t="19:43:00">[19:43:00]</a>. There is significant, unexploited potential in combining these two technologies <a class="yt-timestamp" data-t="19:51:00">[19:51:00]</a>.

### Missing Building Blocks for AGI

While [[Generative AI and causal reasoning | generative AI]] and [[Causality in AI | causal AI]] are great building blocks, additional components are likely needed to achieve Artificial General Intelligence (AGI) <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>. The exact nature of these missing elements remains an "unknown unknown," requiring further hard work and research to identify and develop new theories <a class="yt-timestamp" data-t="20:30:00">[20:30:00]</a>.

### The Need for Harmonization in Causal AI Tooling

A significant current gap in the [[advancements in causal modeling and AI | causal AI]] field is the lack of harmonization across various open-source packages <a class="yt-timestamp" data-t="21:26:00">[21:26:00]</a>. Unlike established fields with unified interfaces like Scikit-learn for machine learning, [[Causality in AI | causal AI]] currently lacks a standardized way for different [[Causal AI and machine learning intersection | causal discovery]], modeling, and decision intelligence engines to work together <a class="yt-timestamp" data-t="21:29:00">[21:29:00]</a>. Addressing this by open-sourcing interfaces and promoting community adoption is crucial for widespread [[Causality in AI | causal AI]] adoption <a class="yt-timestamp" data-t="22:01:00">[22:01:00]</a>.