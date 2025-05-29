---
title: Demystifying Causal Inference in Medical Imaging
videoId: ofAtKK6O2dE
---

From: [[causalpython]] <br/> 

Dr. Athanasios Bonos, a research scientist at Spotify's Advanced [[Causal Inference and Identification | Causal Inference]] Lab and a computer scientist specializing in medical imaging, shares his insights on the role of [[Causal inference and its applications | causality]] in advancing science and technology, particularly in the medical field. His background includes work with Apple, NASA stakeholders at SETI Institute, and a PhD from Imperial College where he focused on [[Causal inference and its applications | causality]] <a class="yt-timestamp" data-t="00:00:14">[00:00:14]</a> <a class="yt-timestamp" data-t="00:54:05">[00:54:05]</a>.

## Challenging the AI Radiologist Vision

Dr. Bonos strongly disagrees with Geoffrey Hinton's 2016 prediction that deep learning would replace radiologists within five years <a class="yt-timestamp" data-t="02:07:07">[02:07:07]</a>. Eight years later, radiologists have not been replaced by AI for multiple reasons <a class="yt-timestamp" data-t="02:31:07">[02:31:07]</a>:
*   **Beyond Lesion Identification**: A radiologist's job extends beyond identifying lesions or measuring features like a baby's head circumference <a class="yt-timestamp" data-t="02:42:07">[02:42:07]</a>. It critically involves decision-making and evaluating complex associations in images <a class="yt-timestamp" data-t="02:53:07">[02:53:07]</a>.
*   **Human Expertise**: The human brain excels at discerning subtle, seemingly irrelevant associations that are crucial for diagnosis, a skill developed through years of medical school and practice <a class="yt-timestamp" data-t="03:18:07">[03:18:07]</a>. Machine learning (ML) systems cannot yet learn these complex associations effectively <a class="yt-timestamp" data-t="03:02:07">[03:02:07]</a>.
*   **Life-and-Death Decisions**: Radiologists make life-and-death decisions for patients <a class="yt-timestamp" data-t="03:40:07">[03:40:07]</a>. ML systems are not yet robust or trustworthy enough for such critical decision-making <a class="yt-timestamp" data-t="03:47:07">[03:47:07]</a>. [[Causal AI in medicine | Causal learning]] and [[Causal Discovery versus Causal Inference | causal discovery]] could potentially advance this, but not currently <a class="yt-timestamp" data-t="04:01:07">[04:01:07]</a>.
*   **Legal and Ethical Considerations**: Questions of blame arise if an AI makes a wrong diagnosis (model, company, or doctor?) <a class="yt-timestamp" data-t="04:16:07">[04:16:07]</a>. Society has not yet progressed to a point where AI systems can replace human radiologists <a class="yt-timestamp" data-t="04:42:07">[04:42:07]</a>.

Instead of replacement, the focus should be on building better tools to enable radiologists to perform their jobs more efficiently and accurately <a class="yt-timestamp" data-t="04:52:07">[04:52:07]</a> <a class="yt-timestamp" data-t="09:01:07">[09:01:07]</a>. Human expertise and deep knowledge are irreplaceable <a class="yt-timestamp" data-t="05:12:07">[05:12:07]</a>.

## Technical Challenges in Medical AI

Overcoming the vision of AI replacing radiologists presents several interconnected technical challenges <a class="yt-timestamp" data-t="05:28:07">[05:28:07]</a>:

### Data Quality and Representation
High-quality, representative data is paramount for any ML algorithm <a class="yt-timestamp" data-t="06:00:07">[06:00:07]</a>.
*   **Bias**: A common pitfall is biased datasets. For instance, early pandemic COVID-19 detection tools based on X-rays often classified images based on their origin (e.g., China vs. US) rather than actual disease, due to confounding factors in data collection <a class="yt-timestamp" data-t="06:21:07">[06:21:07]</a>.
*   **Variations in Modalities**: Even within the same machine type, image quality can vary between hospitals due to differing usage, leading to unobserved confounding elements that affect diagnoses <a class="yt-timestamp" data-t="07:10:07">[07:10:07]</a>.
*   **Causal Thinking in Data**: Approaching data collection with a [[Causal inference and its applications | causal perspective]] can help build better datasets by considering which parameters influence the outcomes and controlling for confounding factors <a class="yt-timestamp" data-t="07:46:07">[07:46:07]</a>. [[Causal thinking]] is not just about modeling but about the entire system-building process, from data collection to robust serving <a class="yt-timestamp" data-t="08:00:07">[08:00:07]</a>.

### Modeling and Implementation
After data collection, the modeling process must adhere to rules to create robust models. Finally, the implementation of these models in production must consider whether they replace or merely assist human experts <a class="yt-timestamp" data-t="08:33:07">[08:33:07]</a>.

### Problem Identification
A crucial challenge is realizing and identifying the core problems, including the key elements and underlying assumptions, before attempting to solve them <a class="yt-timestamp" data-t="09:36:07">[09:36:07]</a>.

## Technology Readiness Levels (TRLs) in Medical AI

Dr. Bonos highlights the importance of Technology Readiness Levels (TRLs) for developing reliable medical AI systems <a class="yt-timestamp" data-t="10:17:07">[10:17:07]</a>.
*   **Origin and Purpose**: TRLs, originating from the US military in the 1950s and adopted by NASA and ISO standards, provide a framework to formalize and evaluate the readiness of any technology before production <a class="yt-timestamp" data-t="10:57:07">[10:57:07]</a>.
*   **Application to ML**: A paper involving his colleagues (Kieran, Yarin G, and others from NASA SETI Institute, Intel) mapped TRLs to the roadmap of developing AI products <a class="yt-timestamp" data-t="11:37:07">[11:37:07]</a>.
*   **Avoiding "Jumping Levels"**: In medical imaging ML, many systems tend to skip crucial TRLs, leading to issues <a class="yt-timestamp" data-t="12:42:07">[12:42:07]</a>. A steady progression through TRLs with checks and balances ensures accountability and robustness, especially in mission-critical fields like medicine and aeronautics where lives are at stake <a class="yt-timestamp" data-t="13:00:07">[13:00:07]</a>.
*   **Incorporating [[Causal inference and its applications | Causality]]**: [[Causal inference and its applications | Causality]] can be integrated throughout the TRL process, particularly in the "robustification" phase of an MVP (Minimum Viable Product). This helps ensure models don't rely on spurious correlations <a class="yt-timestamp" data-t="13:54:07">[13:54:07]</a>.

## The Role of Assumptions in Machine Learning and Causal Inference

Deep learning models, despite their flexibility, still rely on underlying assumptions <a class="yt-timestamp" data-t="15:00:07">[15:00:07]</a>.
*   **Explicit vs. Implicit Assumptions**: While no model can exist without assumptions, [[Causal inference and its applications | causal inference]] explicitly states its assumptions, allowing them to be challenged, debated, and relaxed <a class="yt-timestamp" data-t="16:34:07">[16:34:07]</a>. Problems often arise from forgotten or implicit assumptions <a class="yt-timestamp" data-t="17:07:07">[17:07:07]</a>.
*   **Example: Euclidean Latent Spaces**: A common, often forgotten, assumption is that models operate in Euclidean latent spaces. However, research (e.g., "Latent Space Audity" by Lou/Aran) shows that models might build highly dimensional Riemannian manifolds, leading to noise if standard Euclidean interpolations are used <a class="yt-timestamp" data-t="17:16:07">[17:16:07]</a>. Challenging this led to hyperbolic machine learning models <a class="yt-timestamp" data-t="18:31:07">[18:31:07]</a>.
*   **Picking Assumptions**: The key is to consciously pick which assumptions are valid and to make them explicit <a class="yt-timestamp" data-t="18:53:07">[18:53:07]</a>.

## Real-World [[Causal inference methods and applications | Causal Applications]]: Synthetic Control and Sensitivity Analysis

Dr. Bonos describes a project at Spotify with Jacob Ziller and Kieran, adapting a synthetic control estimator and integrating sensitivity analysis <a class="yt-timestamp" data-t="19:20:07">[19:20:07]</a>.
*   **Combining Frameworks**: The project combined synthetic control (common in econometrics) and sensitivity analysis with the [[Causal Inference and Identification | Pearlian reasoning framework]], challenging existing assumptions <a class="yt-timestamp" data-t="20:44:07">[20:44:07]</a>.
*   **Pragmatism in Practice**: Addressing real-world problems (like those at Spotify, medical imaging, or SETI) requires pragmatism due to real-life constraints <a class="yt-timestamp" data-t="21:21:07">[21:21:07]</a>. This environment serves as a valuable testbed for new models <a class="yt-timestamp" data-t="21:55:07">[21:55:07]</a>.
*   **Understanding Model Failure**: Sensitivity analysis is crucial for understanding when and why models might fail, leading to more robust systems <a class="yt-timestamp" data-t="22:15:07">[22:15:07]</a>.

## Defending [[Causal inference and its applications | Causal Inference]] against Criticism

When faced with criticisms that [[Causal inference and its applications | causal inference]] is too nascent or impractical due to assumptions, Dr. Bonos offers several counterarguments:
*   **Decades of Practice**: Point to the long history of [[Causal inference methods and applications | causal models]] in econometrics and epidemiology, where they have been widely used and validated <a class="yt-timestamp" data-t="23:44:07">[23:44:07]</a>. Many concepts applied in computer science, like the non-prevention monotonicity constraint for identifiability, originate from epidemiology <a class="yt-timestamp" data-t="24:00:07">[24:00:07]</a>.
*   **A Way of Reasoning**: [[Causal inference and its applications | Causal inference]] is not just a modeling tool but a fundamental way of thinking and reasoning about problems <a class="yt-timestamp" data-t="25:17:07">[25:17:07]</a>. Thinking causally, even with approximate models, leads to better outcomes by helping to identify and control for confounding variables <a class="yt-timestamp" data-t="24:47:07">[24:47:07]</a>.
*   **All Models Can Fail**: Just like [[Causal inference and its applications | causal models]], non-causal models like ChatGPT can hallucinate or fail <a class="yt-timestamp" data-t="26:12:07">[26:12:07]</a>. The key is to make assumptions explicit, test them, and understand when a tool is appropriate for a given problem <a class="yt-timestamp" data-t="27:35:07">[27:35:07]</a>.
*   **Human Inertia**: Resistance to new technologies like [[Causal inference and its applications | causality]] is natural, reflecting human inertia and discomfort with change. However, an open mind and willingness to explore lead to significant learnings, allowing us to adopt beneficial elements and discard others <a class="yt-timestamp" data-t="28:47:07">[28:47:07]</a>.

## The Allure of [[Causal Discovery versus Causal Inference | Causal Discovery]]

Dr. Bonos finds [[Causal Discovery versus Causal Inference | causal discovery]] a "better riddle" than [[Causal Inference and Identification | causal inference]] because it's more difficult and exciting <a class="yt-timestamp" data-t="43:12:07">[43:12:07]</a>.
*   **Unveiling Unknown Relationships**: While [[Causal Inference and Identification | causal inference]] assumes knowledge of the causal graph (DAG), [[Causal Discovery versus Causal Inference | causal discovery]] aims to identify these causal connections, often from observational data <a class="yt-timestamp" data-t="43:23:07">[43:23:07]</a>. This is crucial when the causal relationships are unknown or potentially misunderstood <a class="yt-timestamp" data-t="43:52:07">[43:52:07]</a>.
*   **Examples**:
    *   **Ionosphere Impurities**: At the SETI Institute, Dr. Bonos worked on predicting ionosphere impurities affecting GPS signals <a class="yt-timestamp" data-t="44:38:07">[44:38:07]</a>. While impurities around the poles are understood (due to solar wind and Earth's magnetic field), those around the equator are not fully explained <a class="yt-timestamp" data-t="45:05:07">[45:05:07]</a>. This requires discovering new physics or causal relationships <a class="yt-timestamp" data-t="45:35:07">[45:35:07]</a>.
    *   **Modeling Radiologists' Thinking**: To build AI that mimics a radiologist's diagnostic process, one must discover the causal links between elements in their minds, often inferred from observational data like patient tests <a class="yt-timestamp" data-t="45:59:07">[45:59:07]</a>. Identifying causes for missing data, for instance, is a [[Causal Discovery versus Causal Inference | causal discovery]] problem <a class="yt-timestamp" data-t="46:23:07">[46:23:07]</a>.

[[Causal Discovery versus Causal Inference | Causal discovery]] embodies "true science" – the exploration of the unknown <a class="yt-timestamp" data-t="47:07:07">[47:07:07]</a>. It pushes the boundaries of knowledge, leading to the "final frontier" of understanding <a class="yt-timestamp" data-t="47:40:07">[47:40:07]</a>. This innate human drive for exploration, seen historically in migrations, climbing peaks, and scientific inquiry (like Galileo's experiments), is perfectly encapsulated in [[Causal Discovery versus Causal Inference | causal discovery]] <a class="yt-timestamp" data-t="48:11:07">[48:11:07]</a>.

## Interdisciplinary Collaboration and the Future of Science

Working at Spotify's Advanced [[Causal Inference and Identification | Causal Inference]] Lab is rewarding due to Spotify's collaborative, open, and artistic environment <a class="yt-timestamp" data-t="34:11:07">[34:11:07]</a>. A key strength is the interdisciplinary expertise of the team <a class="yt-timestamp" data-t="34:54:07">[34:54:07]</a>:
*   **Diverse Backgrounds**: Team members come from various fields: engineering/computer science with medical focus (Bonos), software engineering/reinforcement learning (Orel), astrophysics (Michael), and quantum physics/computing (Kieran) <a class="yt-timestamp" data-t="35:08:07">[35:08:07]</a>.
*   **Melting Pot of Ideas**: This "melting pot" of different expertises and personalities fosters creativity and leads to unique solutions <a class="yt-timestamp" data-t="35:53:07">[35:53:07]</a>. This approach has proven successful in past projects, like predicting ionosphere problems at SETI with a mix of ML, solar, and ionospheric physicists <a class="yt-timestamp" data-t="36:14:07">[36:14:07]</a>.
*   **Historical Precedent**: This collaborative model echoes successful historical examples like Lockheed Martin's Skunk Works, which prioritized small, diverse teams for rapid innovation <a class="yt-timestamp" data-t="36:46:07">[36:46:07]</a>.

### Key Lessons for [[Causal inference and decision making | Causal Reasoning]] in Product Development
The most surprising lesson from applying [[Causal inference and decision making | causal reasoning]] in a product context is people's innate understanding of [[Causal inference and its applications | causality]] <a class="yt-timestamp" data-t="38:04:07">[38:04:07]</a>. Even without formal training, people grasp cause-and-effect because it's how humans learn and how the universe operates <a class="yt-timestamp" data-t="38:23:07">[38:23:07]</a>. This makes it easier to integrate [[Causal inference concepts and applications | causal concepts]] into product development <a class="yt-timestamp" data-t="38:52:07">[38:52:07]</a>.

### The Continuous Drive for Discovery
Dr. Bonos acknowledges that while society has achieved a high level of comfort and technology, there are still countless unknowns. The notion that "physics is solved" is far from the truth <a class="yt-timestamp" data-t="51:35:07">[51:35:07]</a>. The human drive to explore, invent, and push limits remains strong, whether in the arts, science, or politics <a class="yt-timestamp" data-t="52:29:07">[52:29:07]</a>. Science is not linear; it's a winding path with twists and turns, driven by the essence of exploration <a class="yt-timestamp" data-t="53:50:07">[53:50:07]</a>. Even small contributions matter, as they collectively advance knowledge and create a better world <a class="yt-timestamp" data-t="55:56:07">[55:56:07]</a>.

If Dr. Bonos had a billion dollars for [[Causal inference methods and applications | causal research]], he would invest 75% in [[Causal Discovery versus Causal Inference | causal discovery]] efforts across all fields and 25% in education about [[Causal inference concepts and applications | causality]]. This would foster critical thinking, reduce mistakes, and raise the burden of proof in society <a class="yt-timestamp" data-t="58:35:07">[58:35:07]</a>.

## Recommended Resources for Learning [[Causal inference concepts and applications | Causality]]

For those interested in [[Causal inference concepts and applications | causality]], Dr. Bonos recommends:
*   Reading textbooks (e.g., Pearl's *Book of Why*) and blog posts <a class="yt-timestamp" data-t="01:05:57">[01:05:57]</a>.
*   The most crucial advice: **learn by doing**. Pick a small project and explore what happens from both an associational and a causal perspective <a class="yt-timestamp" data-t="01:06:19">[01:06:19]</a>. This hands-on experience provides insight into why and how [[Causal inference concepts and applications | causal methods]] are applied <a class="yt-timestamp" data-t="01:06:41">[01:06:41]</a>.