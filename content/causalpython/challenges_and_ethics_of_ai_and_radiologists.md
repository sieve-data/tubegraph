---
title: Challenges and Ethics of AI and Radiologists
videoId: ofAtKK6O2dE
---

From: [[causalpython]] <br/> 

The discussion surrounding the integration of Artificial Intelligence (AI) in medical imaging, particularly concerning radiologists, raises significant technical, ethical, and practical challenges. A prominent quote by Jeffrey Hinton from November 24th, 2016, suggested that "in 5 years deep learning is going to do better than Radiologists" and that "people should stop training Radiologists now" <a class="yt-timestamp" data-t="01:54:00">[01:54:00]</a>. Eight years later, this prediction has not materialized, underscoring the complexities involved in fully automating medical diagnosis and decision-making <a class="yt-timestamp" data-t="02:32:00">[02:32:00]</a>.

## Why AI Hasn't Replaced Radiologists: Beyond Image Identification

While deep learning systems excel at tasks like identifying lesions or measuring specific metrics (e.g., baby's head circumference in ultrasound), the role of a radiologist extends far beyond mere image analysis <a class="yt-timestamp" data-t="02:42:00">[02:42:00]</a>. Key reasons AI hasn't replaced human radiologists include:

*   **Decision-Making and Evaluation** Radiologists are crucial for evaluating images and making complex decisions based on their observations <a class="yt-timestamp" data-t="02:53:00">[02:53:00]</a>.
*   **Associational Learning** Deep learning systems currently struggle with learning subtle associations between seemingly irrelevant elements in an image, a skill that experienced radiologists develop over years of training and practice (10 or more years of medical school) <a class="yt-timestamp" data-t="03:08:00">[03:08:00]</a>. This human expertise is very difficult to replace with an ML system <a class="yt-timestamp" data-t="03:30:00">[03:30:00]</a>.
*   **Trust and Robustness** AI systems are not yet robust or trustworthy enough to make life-and-death decisions, which are inherent in a doctor's profession <a class="yt-timestamp" data-t="03:50:00">[03:50:00]</a>. Potentially, advancements in [[causality_and_ai_challenges_and_opportunities | causal AI]] could lead to more reliable systems <a class="yt-timestamp" data-t="04:01:00">[04:01:00]</a>.

Instead of replacement, the goal for the medical imaging community is to develop better tools that empower radiologists to perform their jobs more efficiently and accurately <a class="yt-timestamp" data-t="04:58:00">[04:58:00]</a>, enhancing their existing, irreplaceable expertise <a class="yt-timestamp" data-t="05:12:00">[05:12:00]</a>.

## Ethical and Legal Landscape

Beyond technical limitations, significant ethical and legal challenges impede the full automation of medical diagnosis:

*   **Accountability** When an AI makes a wrong diagnosis, the question of blame arises: Is it the model, the company that built it, or the doctor who used it? <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a> Society has not yet progressed to a point where these legal considerations are resolved, making full AI replacement of radiologists premature <a class="yt-timestamp" data-t="04:42:00">[04:42:00]</a>.
*   **Mission-Critical Applications** Unlike applications such as chatbots (e.g., ChatGPT aiding essay writing), medical diagnosis is a "mission-critical" application where errors have severe, potentially life-threatening, consequences <a class="yt-timestamp" data-t="13:36:00">[13:36:00]</a>. The need for robust and reliable systems is paramount <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>.

## Technical Hurdles in Medical AI Development

Developing reliable [[causal_ai_in_medicine | Causal AI in medicine]] faces several technical hurdles:

### Data Quality and Bias
The foundation of any effective machine learning algorithm is high-quality, representative data <a class="yt-timestamp" data-t="06:06:00">[06:06:00]</a>. In the medical field, this means having data sets that accurately reflect the diversity of the patient population and clinical settings.
A significant challenge is data bias. For instance, early pandemic efforts to detect COVID-19 from X-rays failed when models learned to classify images based on the hospital origin (e.g., Chinese x-rays for positives, US x-rays for negatives) rather than actual disease <a class="yt-timestamp" data-t="06:28:00">[06:28:00]</a>.
Furthermore, variations within the same medical modality (e.g., ultrasounds, MRIs, PET scans) exist even across identical machines in different hospitals, based on how doctors use them <a class="yt-timestamp" data-t="07:12:00">[07:12:00]</a>. These "unobserved confounding elements" can heavily influence image quality and subsequent diagnoses <a class="yt-timestamp" data-t="07:34:00">[07:34:00]</a>.
Thinking about data collection in a [[causality_and_ai_challenges_and_opportunities | causal way]] is crucial for building better datasets <a class="yt-timestamp" data-t="07:46:00">[07:46:00]</a>. Causality is not just about the modeling part; it's about the entire system-building process, from data collection and parameter consideration to robust deployment <a class="yt-timestamp" data-t="08:00:00">[08:00:00]</a>. Gathering correct data in the medical field is exceptionally difficult but vital for success <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

### Unstated Assumptions in AI Models
All models, whether deep learning or [[causality_and_ai_challenges_and_opportunities | causal AI]], rely on assumptions <a class="yt-timestamp" data-t="15:57:00">[15:57:00]</a>. The danger lies not in making assumptions, but in forgetting or not explicitly stating them <a class="yt-timestamp" data-t="16:31:00">[16:31:00]</a>. For example, many deep learning models implicitly assume a Euclidean latent space, yet empirical evidence shows models often build highly complex Riemannian manifolds <a class="yt-timestamp" data-t="17:16:00">[17:16:00]</a>. Ignoring such fundamental assumptions can lead to unreliable models <a class="yt-timestamp" data-t="19:07:00">[19:07:00]</a>. [[causality_robustness_and_fairness_in_ai_models | Causal AI models]] explicitly state their assumptions, allowing for testing, challenge, and discussion <a class="yt-timestamp" data-t="16:42:00">[16:42:00]</a>.

## The Role of Technology Readiness Levels
Technology Readiness Levels (TRLs), originally developed by the US military and adopted by NASA, provide a framework to formalize technology development and evaluate its readiness before production <a class="yt-timestamp" data-t="10:57:00">[10:57:00]</a>. Applying TRLs to medical ML algorithms is crucial. Many systems today jump through these levels without sufficient consideration, leading to chaotic development and problems in deployment <a class="yt-timestamp" data-t="12:55:00">[12:55:00]</a>. Steadily progressing through TRLs with checks and balances ensures accountability and robustness, especially in critical fields like medicine <a class="yt-timestamp" data-t="13:10:00">[13:10:00]</a>. The essence of [[causality_robustness_and_fairness_in_ai_models | causality]] can be introduced throughout the TRLs, particularly when robustifying a system to ensure it's not relying on spurious correlations <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>.

## Causality as a Foundational Principle
The speaker argues that [[causality_and_ai_challenges_and_opportunities | causality]] is not merely a modeling tool but a way of reasoning and thinking about problems <a class="yt-timestamp" data-t="25:17:00">[25:17:00]</a>. By employing causal reasoning, identifying potential confounding variables, and controlling for them, better models can be built <a class="yt-timestamp" data-t="25:01:00">[25:05:00]</a>. While not a "panacea," causal thinking can significantly improve AI systems <a class="yt-timestamp" data-t="28:34:00">[28:34:00]</a>.
A key insight is that people, regardless of formal training in [[causality_and_ai_challenges_and_opportunities | causal AI]], possess an innate understanding of causality <a class="yt-timestamp" data-t="38:05:00">[38:05:00]</a>. This inherent human capacity to understand cause and effect, honed by basic interactions (e.g., pushing a mug and it falling), makes the adoption and application of causal concepts in product development easier to convey and appreciate <a class="yt-timestamp" data-t="38:28:00">[38:28:00]</a>. People quickly grasp the value of controlling for spurious correlations <a class="yt-timestamp" data-t="39:09:00">[39:09:00]</a>.

## AI as a Tool, Not a Replacement
Ultimately, the future of AI in medical imaging lies in its development as a tool to augment human capabilities, not replace them <a class="yt-timestamp" data-t="09:01:00">[09:01:00]</a>. This approach leverages AI for efficiency and accuracy while preserving the irreplaceable expertise, decision-making, and ethical judgment of human radiologists. This collaborative model, rather than one of displacement, aligns with the complex and high-stakes nature of medical practice.