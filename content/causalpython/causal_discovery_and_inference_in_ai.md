---
title: Causal discovery and inference in AI
videoId: ofAtKK6O2dE
---

From: [[causalpython]] <br/> 

Science is not a linear pursuit; it is driven by exploration and is "all over the place" <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The notion of [[Causal reasoning in AI | causality]], as applied in organizations like Spotify and in academic research, extends beyond just the modeling phase <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. It is integral to the entire system-building process, from data collection to robust implementation <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

## Causal Discovery vs. Causal Inference

While both are crucial, [[Causal discovery and learning | causal discovery]] is considered a "better riddle" than [[Causal reasoning in artificial intelligence | causal inference]] because it is "plain and simple more difficult" and more exciting <a class="yt-timestamp" data-t="00:50:07">[00:50:07]</a>, <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.

*   **[[Causal reasoning in artificial intelligence | Causal Inference]]** <a class="yt-timestamp" data-t="00:43:23">[00:43:23]</a>: Makes assumptions, such as knowing the Directed Acyclic Graph (DAG) and that X causes Y <a class="yt-timestamp" data-t="00:43:24">[00:43:24]</a>. The primary challenge is that this knowledge may not span the entirety of the cosmos, or may be mistaken <a class="yt-timestamp" data-t="00:43:38">[00:43:38]</a>.
*   **[[Causal discovery and learning | Causal Discovery]]** <a class="yt-timestamp" data-t="00:44:11">[00:44:11]</a>: Aims to identify these causal graphs (DAGs), leveraging expert knowledge but primarily focusing on figuring out underlying causal relationships <a class="yt-timestamp" data-t="00:44:11">[00:44:11]</a>. This is a very challenging and interesting task <a class="yt-timestamp" data-t="00:44:22">[00:44:22]</a>.

### Examples Requiring Causal Discovery

1.  **Ionospheric Impurities**: Research at the SETI Institute involves understanding impurities in the ionosphere that disrupt GNSS (e.g., GPS) bands <a class="yt-timestamp" data-t="00:44:38">[00:44:38]</a>. While the physics around the poles is well understood, the causes of impurities around the equator are not fully certain <a class="yt-timestamp" data-t="00:45:19">[00:45:19]</a>. This requires discovering new physics or causal relationships <a class="yt-timestamp" data-t="00:45:37">[00:45:37]</a>.
2.  **Medical Field and Radiologist Decision-Making**: To model a radiologist's thinking, one needs to discover the causal links between elements in their minds <a class="yt-timestamp" data-t="00:46:02">[00:46:02]</a>. For example, identifying the cause of missing observational data, which might not be missing at random, is a truly interesting and challenging task <a class="yt-timestamp" data-t="00:46:23">[00:46:23]</a>.

[[Causal discovery and learning | Causal discovery]] is seen as "true science" or exploration, as it involves finding out something unknown <a class="yt-timestamp" data-t="00:47:07">[00:47:07]</a>, <a class="yt-timestamp" data-t="00:47:15">[00:47:15]</a>. It leads to the "final frontier" of what humans know <a class="yt-timestamp" data-t="00:47:43">[00:47:43]</a>.

## Challenges and Limitations of AI Models

The widespread belief that AI, specifically deep learning, will completely replace human roles like radiologists, as suggested by Jeffrey Hinton in 2016 <a class="yt-timestamp" data-t="00:01:57">[00:01:57]</a>, is respectfully disagreed with <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Eight years later, radiologists have not been replaced by AI for multiple reasons <a class="yt-timestamp" data-t="00:02:32">[00:02:32]</a>.

### Why AI Hasn't Replaced Radiologists
*   **Beyond Lesion Identification**: A radiologist's job involves more than just identifying lesions or making measurements; it heavily includes decision-making and evaluating what they see <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>.
*   **Associational Learning vs. Causal Understanding**: Deep learning systems struggle to learn associations between seemingly irrelevant things that are, in fact, connected <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. Human experience, gained from years of medical training, excels at this <a class="yt-timestamp" data-t="00:03:18">[00:03:18]</a>.
*   **Life-and-Death Decision Making**: ML systems are not yet robust enough to make life-and-death decisions for patients in a trustworthy manner <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>.
*   **Legal and Ethical Considerations**: Questions of blame for wrong diagnoses (model, company, or doctor) highlight the need for legal and ethical frameworks that are not yet established for AI systems in critical fields <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>.

Instead of replacement, the goal is to provide better tools to enable radiologists to perform their jobs more efficiently, not to replace their irreplaceable human expertise <a class="yt-timestamp" data-t="00:05:07">[00:05:07]</a>.

### Technical Challenges to Hinton's Vision
Success in AI for medical imaging relies on overcoming several interconnected and crucial challenges:
1.  **Data Quality**: Having good, representative data is key <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. Biased datasets, like those early in the pandemic where COVID-positive X-rays were from China and negatives from Stanford, lead to models classifying location rather than disease <a class="yt-timestamp" data-t="00:06:37">[00:06:37]</a>. Variations even within the same machine across different hospitals can introduce unobserved confounding elements <a class="yt-timestamp" data-t="00:07:18">[00:07:18]</a>. Thinking in a [[causal_reasoning_in_ai | causal way]] helps build better datasets <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>.
2.  **Modeling**: The actual modeling process must abide by certain rules to produce robust models <a class="yt-timestamp" data-t="00:08:36">[00:08:36]</a>.
3.  **Implementation**: How AI systems are implemented in production is vital. They should be tools to assist, not replace, human professionals <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>.

The fundamental challenge is realizing "where is a problem" and identifying its key elements <a class="yt-timestamp" data-t="00:09:38">[00:09:38]</a>. This encompasses data, modeling, and many other components <a class="yt-timestamp" data-t="00:09:49">[00:09:49]</a>.

### The Importance of Explicit Assumptions
Deep learning models, despite their non-parametric nature, are still based on assumptions <a class="yt-timestamp" data-t="00:15:00">[00:15:00]</a>. The problem is not having assumptions, but forgetting them or making invalid ones <a class="yt-timestamp" data-t="00:16:31">[00:16:31]</a>. [[Causal reasoning in artificial intelligence | Causal inference]] explicitly states its assumptions, allowing them to be tested, challenged, and discussed <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

For example, the common assumption that models operate in Euclidean latent spaces is often false; models may build highly dimensional Riemannian manifolds <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. Challenging this led to hyperbolic machine learning models <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. It is crucial to pick assumptions that are valid, make them explicit, and not forget about them <a class="yt-timestamp" data-t="00:18:56">[00:18:56]</a>.

## Application in Practice and Technology Readiness Levels

[[Causal AI and its role in experiments | Causal AI]] and thinking are applied in practical, real-world settings, such as medical imaging, Spotify, and the SETI Institute <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>.

### Technology Readiness Levels (TRLs)
TRLs, originating from the US military and NASA, provide a framework for developing and evaluating technology readiness <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. This framework has been incorporated into ISO standards <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. Papers, some co-authored by the speaker's colleagues from Spotify and NASA SETI Institute, discuss how TRLs apply to ML algorithms <a class="yt-timestamp" data-t="00:11:48">[00:11:48]</a>.

In medical imaging, these levels are universal and task-agnostic <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. Skipping crucial TRLs can lead to problems <a class="yt-timestamp" data-t="00:12:52">[00:12:52]</a>. Steadily progressing through TRLs with checks and balances ensures accountability and robustness, especially in mission-critical fields like medicine and aeronautics where decisions are life-and-death <a class="yt-timestamp" data-t="00:13:10">[00:13:10]</a>. The essence of [[causality in AI | causality]] can be introduced throughout the TRLs, particularly in robustifying a system's Minimum Viable Product (MVP) <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

### Spotify Project Example
A project at Spotify adapted synthetic control estimators, common in econometrics, and combined them with Pearl's causal reasoning framework, including sensitivity analysis <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. This project challenged existing assumptions and formalized methods, leading to robust results by understanding when models might fail <a class="yt-timestamp" data-t="00:22:02">[00:22:02]</a>.

## Addressing Criticisms of Causal Inference

Critics often argue that [[Causal reasoning in artificial intelligence | causal inference]] is in its early stages or useless due to its reliance on assumptions <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>.

However, [[causal_reasoning_in_ai | causal inference]] has decades of literature and practical application in fields like econometrics and epidemiology <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. Many concepts applied in computer science today originate from these fields <a class="yt-timestamp" data-t="00:23:55">[00:23:55]</a>.

While models can fail (e.g., ChatGPT hallucinations <a class="yt-timestamp" data-t="00:26:16">[00:26:16]</a>), this is true for any field, and it doesn't invalidate the approach <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>. The key is making assumptions explicit, testable, and understanding when a tool is appropriate <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. [[Causality in AI | Causality]] is not a panacea, but it can help in many circumstances <a class="yt-timestamp" data-t="00:28:37">[00:28:37]</a>.

### Why [[Causality in AI | Causal Thinking]] Works
Thinking in a [[causal_reasoning_in_ai | causal manner]] is essential for solving problems, even if a model isn't 100% causal <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>. By understanding what could affect results and controlling for variables, one can build better models <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. [[Causal reasoning in AI | Causal inference]] is more than just a modeling tool; it's a way of reasoning and thinking about things <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>.

## Interdisciplinary Thinking and Exploration

Interdisciplinary research, borrowing from different fields and combining them, leads to interesting discoveries <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>. An example is the Minkowski SpaceTime paper, which challenged the assumption of Euclidean space in models, revealing that [[causality_in_ai | causality]] does not emerge in a flat Euclidean space but requires a Lorentzian group space <a class="yt-timestamp" data-t="00:32:51">[00:32:51]</a>. This highlights the value of challenging assumptions and exploring new approaches <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>.

The Advanced Causal Inference Lab at Spotify embodies this interdisciplinary approach, with team members from diverse backgrounds like electrical engineering, computer science, reinforcement learning, astrophysics, and quantum physics <a class="yt-timestamp" data-t="00:35:01">[00:35:01]</a>. This "melting pot" fosters creativity and leads to unique results <a class="yt-timestamp" data-t="00:35:53">[00:35:53]</a>. Examples include predicting ionospheric problems due to solar weather by combining machine learning, solar physics, and ionospheric physics expertise <a class="yt-timestamp" data-t="00:36:13">[00:36:13]</a>.

## The Innate Understanding of Causality

A surprising lesson from applying [[Causal reasoning in AI | causal reasoning]] in a product context is that people, regardless of their academic background, have an innate understanding of [[causality in AI | causality]] <a class="yt-timestamp" data-t="00:38:00">[00:38:00]</a>. This understanding is built into human nature, as we learn from cause-and-effect relationships from a young age <a class="yt-timestamp" data-t="00:38:23">[00:38:23]</a>. This makes building products based on causal concepts easier, as people appreciate its power <a class="yt-timestamp" data-t="00:38:52">[00:38:52]</a>.

## Investment in Causal Research

If given $1 billion for [[advancements in causal modeling and AI | causal research]], the investment would be largely dedicated to [[Causal discovery algorithms and realworld applications | causal discovery]] and education:
*   **75% to [[Causal discovery algorithms and realworld applications | Causal Discovery]]**: Applying it in every imaginable field of science and technology <a class="yt-timestamp" data-t="00:59:41">[00:59:41]</a>.
*   **25% to Education**: Helping people realize what [[causality in AI | causality]] is, encouraging skepticism about what they see, and promoting more logical thinking to decrease mistakes <a class="yt-timestamp" data-t="00:59:51">[00:59:51]</a>.

## Conclusion

The essence of exploration drives scientific and technological advancement <a class="yt-timestamp" data-t="00:55:18">[00:55:18]</a>. This is encapsulated in [[Causal discovery and learning | causal discovery]], which represents the innate human drive to understand the "why" behind phenomena <a class="yt-timestamp" data-t="00:49:15">[00:49:15]</a>. While the world may seem to "work fairly okay" and some believe physics is solved, there are still countless unknowns <a class="yt-timestamp" data-t="00:51:54">[00:51:54]</a>. Continual pushing of limits, even in seemingly mundane areas, can lead to unique solutions and significant contributions <a class="yt-timestamp" data-t="00:55:31">[00:55:31]</a>. Interdisciplinary collaboration and an open mind to explore new ideas are key to future [[advancements in causal modeling and AI | advancements in causal modeling and AI]] <a class="yt-timestamp" data-t="00:29:42">[00:29:42]</a>, <a class="yt-timestamp" data-t="00:30:16">[00:30:16]</a>.