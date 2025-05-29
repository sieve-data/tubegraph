---
title: Technological and ethical considerations of AI in healthcare
videoId: ofAtKK6O2dE
---

From: [[causalpython]] <br/> 

Science is not a linear process; it is an exploration driven by the notion of [[Causality in AI | causality]] <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. The application of AI, particularly in medical imaging, brings forth significant technological and ethical challenges that require careful consideration <a class="yt-timestamp" data-t="00:01:02">[00:01:02]</a>.

## AI vs. Radiologists: A Disagreement
In 2016, Jeffrey Hinton famously stated that deep learning would outperform radiologists in five years, suggesting that people should "stop training Radiologists now" <a class="yt-timestamp" data-t="00:01:54">[00:01:54]</a>. However, Dr. Athanasios Bonos and many in the medical imaging community respectfully disagree with this prediction <a class="yt-timestamp" data-t="00:02:20">[00:02:20]</a>. Eight years later, radiologists have not been replaced by AI for multiple reasons <a class="yt-timestamp" data-t="00:02:31">[00:02:31]</a>.

### The Role of Radiologists
A radiologist's job extends beyond simply identifying lesions or making measurements, such as the circumference of a baby's head in an ultrasound <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. It significantly involves:
*   **Decision-making and evaluation**: Radiologists evaluate what they see in images <a class="yt-timestamp" data-t="00:02:53">[00:02:53]</a>.
*   **Associative reasoning**: The human brain excels at identifying associations between seemingly irrelevant elements that are, in fact, connected <a class="yt-timestamp" data-t="00:03:08">[00:03:08]</a>. This experience, gained through 10 or more years of medical school training, is exceptionally difficult to replace with an ML system <a class="yt-timestamp" data-t="00:03:20">[00:03:20]</a>.
*   **Life-and-death decisions**: Medical professionals make critical decisions for patients <a class="yt-timestamp" data-t="00:03:40">[00:03:40]</a>. ML systems are not yet robust enough to be fully trusted with such decisions <a class="yt-timestamp" data-t="00:03:50">[00:03:50]</a>, though [[Causal AI in Medicine | causal AI in medicine]] could potentially help in the future <a class="yt-timestamp" data-t="00:04:01">[00:04:01]</a>.

### Legal and Ethical Considerations
Beyond technical points, the legal and ethical aspects of AI in medicine are crucial <a class="yt-timestamp" data-t="00:04:19">[00:04:19]</a>. If an AI makes a wrong diagnosis that affects a person's life, questions arise about accountability: Is the model, the company, or the doctor to blame? <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a> Society has not yet progressed to a point where AI systems can fully replace radiologists <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. The aim should be to develop better tools that enable radiologists to perform their jobs more efficiently and accurately, rather than replacing their irreplaceable human expertise <a class="yt-timestamp" data-t="00:04:52">[00:04:52]</a>.

## Key Technical Challenges for AI in Healthcare
Achieving the vision of AI deeply integrated into healthcare, as Hinton suggested, presents numerous interconnected challenges <a class="yt-timestamp" data-t="00:05:51">[00:05:51]</a>.

### Data Quality and Representativeness
The foundation of any successful ML algorithm is good quality data <a class="yt-timestamp" data-t="00:06:06">[00:06:06]</a>. In the medical field, data sets must be highly representative to avoid bias <a class="yt-timestamp" data-t="00:06:17">[00:06:17]</a>.
*   **COVID-19 X-ray example**: Early pandemic papers on AI tools for COVID detection were often flawed because "positives" came from X-rays in China, while "negatives" came from Stanford in the US, creating a biased classifier that distinguished location rather than disease <a class="yt-timestamp" data-t="00:06:28">[00:06:28]</a>.
*   **Variations in imaging**: More complex modalities like ultrasounds, MRIs, and PET-CTs show variations even within the same machine model across different hospitals, influenced by how doctors use them <a class="yt-timestamp" data-t="00:07:08">[00:07:08]</a>. This can introduce unobserved confounding elements that affect the output image and diagnosis <a class="yt-timestamp" data-t="00:07:34">[00:07:34]</a>.

Thinking about data collection causally can help build better datasets <a class="yt-timestamp" data-t="00:07:46">[00:07:46]</a>. [[Causality in AI | Causality]] should be integrated throughout the entire system-building process, from data collection and parameter consideration to data modeling and robust deployment for the end-user <a class="yt-timestamp" data-t="00:08:06">[00:08:06]</a>.

### Implementation and Robustness
The actual implementation of AI models needs to be considered carefully <a class="yt-timestamp" data-t="00:08:50">[00:08:50]</a>. They should serve as tools to make radiologists' lives easier, allowing them to see more patients and diagnose them more accurately and quickly, rather than replacing them <a class="yt-timestamp" data-t="00:09:00">[00:09:00]</a>.

## Technology Readiness Levels (TRLs) in AI
The concept of Technology Readiness Levels (TRLs), originating from the US military in the 1950s and adopted by NASA and ISO standards, provides a framework for developing and evaluating technology readiness <a class="yt-timestamp" data-t="00:10:57">[00:10:57]</a>. This framework helps ensure accountability and robustness, especially for mission-critical applications like aeronautics and medicine, where decisions are life-and-death <a class="yt-timestamp" data-t="00:13:25">[00:13:25]</a>.

A paper co-authored by Dr. Bonos argues that TRLs are universal and task/application agnostic, and blindly skipping stages can lead to significant problems <a class="yt-timestamp" data-t="00:12:42">[00:12:42]</a>. In the context of AI and machine learning, [[Causality in AI | causality]] can be introduced throughout the TRLs, particularly to ensure the robustness of an MVP (Minimum Viable Product) <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. This involves ensuring the model isn't relying on spurious correlations <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

## The Role of Assumptions in AI Models
All models, including deep learning models, are based on assumptions <a class="yt-timestamp" data-t="00:15:06">[00:15:06]</a>. While deep learning has moved towards non-parametric large models that relax some assumptions (e.g., neural networks being more flexible than linear regression), it's crucial not to forget the underlying assumptions that remain <a class="yt-timestamp" data-t="00:15:15">[00:15:15]</a>. For models to be robust and generalize, these assumptions must be remembered <a class="yt-timestamp" data-t="00:15:47">[00:15:47]</a>.

### Explicit vs. Forgotten Assumptions
Not all assumptions are "created equal" <a class="yt-timestamp" data-t="00:16:03">[00:16:03]</a>. The problem often lies in forgetting assumptions, rather than making them explicitly <a class="yt-timestamp" data-t="00:16:32">[00:16:32]</a>. A key benefit of [[Causality in AI | causal inference]] and causal discovery is making assumptions explicit, allowing them to be tested, challenged, and discussed <a class="yt-timestamp" data-t="00:16:40">[00:16:40]</a>.

*   **Euclidean Latent Spaces Example**: A common forgotten assumption is that models have Euclidean latent spaces <a class="yt-timestamp" data-t="00:17:16">[00:17:16]</a>. Research shows that models, like Variational Autoencoders (VAEs), might build highly high-dimensional Riemannian manifolds instead <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>. Challenging this led to hyperbolic machine learning models <a class="yt-timestamp" data-t="00:18:31">[00:18:31]</a>. For [[Causality in AI | causality]] to emerge in a latent space, it needs to be a Lorentzian group space, not a flat Euclidean space <a class="yt-timestamp" data-t="00:32:58">[00:32:58]</a>.

## Causality in Practice: The Spotify Project
A project at Spotify, involving Jacob Ziff and Kieran, adapted a synthetic control estimator from econometrics and combined it with identification strategies from the Judea Pearl tradition, adding sensitivity analysis <a class="yt-timestamp" data-t="00:19:20">[00:19:20]</a>. This pragmatic approach to real-world problems highlights the need to live with existing constraints <a class="yt-timestamp" data-t="00:21:21">[00:21:21]</a>. The sensitivity analysis specifically aimed to understand when assumptions and models would fail and why, leading to more robust systems <a class="yt-timestamp" data-t="00:22:20">[00:22:20]</a>.

## Addressing Criticisms of Causal Inference
Critics sometimes argue that [[Causality in AI | causal inference]] is in its early stages or that its assumptions make it useless in practice <a class="yt-timestamp" data-t="00:22:54">[00:22:54]</a>.

### Historical Context and Practical Value
*   **Decades of Use**: [[Causality in AI | Causal models]] have been used for decades in econometrics and epidemiology <a class="yt-timestamp" data-t="00:23:46">[00:23:46]</a>. Many concepts applied in computer science, such as the monotonicity constraint (no prevention) for identifiability, originate from epidemiology <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>.
*   **A Way of Reasoning**: [[Causality in AI | Causal inference]] is not merely a modeling tool but a way of reasoning and thinking about problems <a class="yt-timestamp" data-t="00:25:17">[00:25:17]</a>. Even if a model isn't 100% causal, employing causal reasoning techniques to understand what affects outcomes and to control for confounding variables leads to better models <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>.

### Model Failures and Assumptions
It is unrealistic to expect any model to always work <a class="yt-timestamp" data-t="00:26:12">[00:26:12]</a>. Even models like ChatGPT, which make no causal assumptions, can hallucinate and provide incorrect answers <a class="yt-timestamp" data-t="00:26:18">[00:26:18]</a>. The key is making assumptions explicit, testable, and understanding when a tool is appropriate for a given problem <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. [[Causality in AI | Causal modeling]] is not a panacea, but it is highly beneficial in many circumstances <a class="yt-timestamp" data-t="00:28:34">[00:28:34]</a>.

## The Nature of Science and Exploration
Science and technology are rarely linear paths; they involve twists, turns, and constant exploration <a class="yt-timestamp" data-t="00:30:50">[00:30:50]</a>.

### Interdisciplinary Research and Challenging Assumptions
A significant discovery is the power of interdisciplinary research, borrowing and combining ideas from different fields <a class="yt-timestamp" data-t="00:32:09">[00:32:09]</a>. This approach fosters creativity and leads to unique results <a class="yt-timestamp" data-t="00:36:04">[00:36:04]</a>. Examples include:
*   **Spotify's Advanced Causal Inference Lab**: Composed of individuals from diverse backgrounds including engineering, computer science, medical imaging, reinforcement learning, astrophysics, and quantum physics <a class="yt-timestamp" data-t="00:35:05">[00:35:05]</a>.
*   **SETI Institute Project**: A project involving machine learning experts, solar physicists, and an ionospheric physicist to predict ionosphere problems due to solar weather <a class="yt-timestamp" data-t="00:36:14">[00:36:14]</a>.
*   **Minkowski Spacetime Paper**: This paper challenged the assumption of Euclidean space in models, demonstrating that [[Causality in AI | causality]] requires a Lorentzian group space <a class="yt-timestamp" data-t="00:32:46">[00:32:46]</a>. This "crackpot science" that challenges everything is where magic happens <a class="yt-timestamp" data-t="00:33:53">[00:33:53]</a>.

### Causal Discovery vs. Causal Inference
*   **Causal Discovery as a "Better Riddle"**: Causal discovery is more difficult and exciting than causal inference because it aims to figure out how things are causally connected without prior assumptions about the causal graph (DAG) <a class="yt-timestamp" data-t="00:43:12">[00:43:12]</a>.
*   **Unknown Causal Relationships**: In many fields, like the ionosphere's behavior around the equator (affecting GNSS/GPS), the underlying causal physics is not 100% understood, requiring the discovery of new causal relationships <a class="yt-timestamp" data-t="00:45:19">[00:45:19]</a>. Similarly, modeling how radiologists think involves discovering the causal links between elements in their minds based on observational data <a class="yt-timestamp" data-t="00:45:59">[00:45:59]</a>.
*   **True Science**: Causal discovery is seen as "true science" and "exploration," trying to find out something unknown, while causal inference is considered "applied science" or "technology" <a class="yt-timestamp" data-t="00:47:03">[00:47:03]</a>. This leads to the "final frontier" of knowledge <a class="yt-timestamp" data-t="00:47:40">[00:47:40]</a>, echoing the exploration drive seen throughout human history and popularized in shows like Star Trek <a class="yt-timestamp" data-t="00:47:49">[00:47:49]</a>.

### Human Nature and the Drive for Discovery
Despite living in a technologically advanced world where knowledge seems readily available (e.g., Wikipedia), many fundamental unknowns persist <a class="yt-timestamp" data-t="00:50:27">[00:50:27]</a>. Forgetting that we live in a world where we don't know many things can stifle the innate human drive to explore and understand the "why" <a class="yt-timestamp" data-t="00:51:02">[00:51:02]</a>. This drive is inherent in human nature, pushing individuals to push limits in arts, science, technology, and politics <a class="yt-timestamp" data-t="00:52:45">[00:52:45]</a>. Even small contributions matter in this collective effort <a class="yt-timestamp" data-t="00:55:56">[00:55:56]</a>.

## Investing in Causal Research
If given $1 billion for [[Causality in AI | causal research]], the investment would be primarily in:
1.  **Causal Discovery (75%)**: To help the world greatly by applying it across every imaginable field of science and technology <a class="yt-timestamp" data-t="00:58:40">[00:58:40]</a>.
2.  **Education (25%)**: To help people realize what [[Causality in AI | causality]] is, appreciate its embedded nature in human beings, be skeptical about what they see, and apply logical reasoning. This would decrease mistakes and encourage more accurate and logical thinking in society <a class="yt-timestamp" data-t="00:58:46">[00:58:46]</a>.

A major unsolved problem in [[Causality in AI | causality]] is finding a way to create accurate and meaningful bounds from purely observational data, which is currently considered impossible without substantial assumptions <a class="yt-timestamp" data-t="00:57:51">[00:57:51]</a>.

## Learning More About Causality
For those interested in learning more about [[Causality in AI | causality]], recommendations include:
*   Books: Jacob's book, Judea Pearl's "Book of Why," and other textbooks <a class="yt-timestamp" data-t="00:55:57">[00:55:57]</a>.
*   Online Resources: Medium articles and blog posts <a class="yt-timestamp" data-t="00:57:07">[00:57:07]</a>.
*   **Experiential Learning**: The most recommended method is to "learn by doing" by picking a small project and experimenting with both associational and causal perspectives <a class="yt-timestamp" data-t="00:57:19">[00:57:19]</a>. This hands-on experience provides insight into why certain approaches are necessary <a class="yt-timestamp" data-t="00:57:41">[00:57:41]</a>.