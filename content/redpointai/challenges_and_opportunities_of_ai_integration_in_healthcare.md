---
title: Challenges and opportunities of AI integration in healthcare
videoId: VUBfFv-Un3c
---

From: [[redpointai]] <br/> 

AI integration in healthcare presents a unique set of [[challenges_and_opportunities_in_ai_development | challenges and opportunities]], primarily due to the industry's complex regulatory environment and the nature of medical information. Oscar Health, a $3 billion public health insurance company, operates at the forefront of this intersection, leveraging AI for both administrative efficiency and clinical improvements <a class="yt-timestamp" data-t="00:00:17">[00:00:17]</a>.

## AI's Transformative Potential in Healthcare

Large Language Models (LLMs) are particularly well-suited for healthcare due to their ability to translate between informal and formal language <a class="yt-timestamp" data-t="01:59:37">[01:59:37]</a>. Healthcare uniquely possesses both:
*   **Highly Formalized Language**: Such as ICD10 codes, CPT codes, and utilization management guidelines <a class="yt-timestamp" data-t="02:04:02">[02:04:02]</a>.
*   **Abundant Human Language**: Including conversations between providers and patients, and electronic medical record notes <a class="yt-timestamp" data-t="02:15:20">[02:15:20]</a>.

This capability marks a significant shift from previous algorithmic applications in healthcare, which often "ended at that surface" where formal and informal languages met <a class="yt-timestamp" data-t="02:46:58">[02:46:58]</a>. The aim is to create a healthcare system where costs are transparent, alternatives are clear, and administrative issues like claims denials are minimized <a class="yt-timestamp" data-t="04:04:33">[04:04:33]</a>.

## Oscar Health's AI Applications and Strategy

Oscar Health is both an insurer and a care provider, with its own medical group and care teams <a class="yt-timestamp" data-t="00:31:07">[00:31:07]</a>. Their AI strategy focuses on three key financial levers <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>:

1.  **Growth and Retention**: AI is used for personalized outbound campaigns to remind members of Oscar's benefits and encourage re-enrollment <a class="yt-timestamp" data-t="13:37:00">[13:37:00]</a>. This includes tailoring messages based on member personas, such as using "empathy" for chronically ill members and "convenience" for generally healthy ones <a class="yt-timestamp" data-t="14:48:00">[14:48:00]</a>. LLMs can extract persona characteristics from customer service conversations <a class="yt-timestamp" data-t="15:51:00">[15:51:00]</a>.
2.  **Operational Efficiency (Administrative)**: Oscar has focused heavily on [[transforming_clinical_processes_with_ai | administrative AI use cases]] in the short term, aiming for rapid deployment and savings <a class="yt-timestamp" data-t="05:20:00">[05:20:00]</a>.
    *   **Call Summarization**: Increasingly phasing out manual note-taking by care guides in favor of LLM-generated summaries <a class="yt-timestamp" data-t="17:20:00">[17:20:00]</a>.
    *   **Lab Test Summarization**: Launched within Oscar's medical group <a class="yt-timestamp" data-t="17:41:00">[17:41:43]</a>.
    *   **Secure Messaging Medical Records Generation**: Also launched in the medical group <a class="yt-timestamp" data-t="17:46:00">[17:46:00]</a>.
    *   **Claims Explainers**: Translating complex internal claims logic into understandable language for care guides, eventually aiming for direct member communication <a class="yt-timestamp" data-t="17:52:00">[17:52:00]</a>.
3.  **Medical Cost Reduction and Outcomes Improvement (Clinical)**: This area is seen as having the greatest long-term impact on healthcare costs <a class="yt-timestamp" data-t="12:26:00">[12:26:00]</a>. A primary use case is enabling doctors and customer service agents to "talk to the medical records" <a class="yt-timestamp" data-t="18:52:00">[18:52:00]</a>.

## [[Challenges in AI Adoption and Deployment | Challenges in AI Adoption and Deployment]] in Healthcare

Integrating AI into healthcare is fraught with specific obstacles:

### Regulatory and Compliance Hurdles
*   **HIPAA and BAAs**: Strict patient privacy regulations like HIPAA require Business Associate Agreements (BAAs) with AI vendors <a class="yt-timestamp" data-t="20:56:00">[20:56:00]</a>. Oscar was among the first to sign a BAA directly with OpenAI <a class="yt-timestamp" data-t="21:18:00">[21:18:00]</a>.
*   **New Model Adoption Delays**: When new AI models are released (e.g., Google's Gemini Ultra), they are not immediately covered under existing HIPAA agreements. This necessitates using synthetic or anonymized test data for initial evaluations, with a typical delay of 3-4 months before real medical data can be used <a class="yt-timestamp" data-t="22:30:00">[22:30:00]</a>.
*   **Security Reviews and Certifications**: Hospitals and insurance companies require extensive security and policy reviews, often involving long checklists or certifications like "High Trust" <a class="yt-timestamp" data-t="23:58:00">[23:58:00]</a>.

### LLM Limitations and Data Cleanliness
*   **Contextual Knowledge Gaps**: LLMs struggle with subtle contextual knowledge that humans possess (e.g., a doctor remembering a previous conversation not in formal records), making it an "unfair playing field" when inputs are less clean <a class="yt-timestamp" data-t="07:11:00">[07:11:00]</a>.
*   **Complex Logical Tasks**: LLMs can fail at tasks requiring simultaneous processing and counting, such as categorizing and then tallying reasons for customer service calls <a class="yt-timestamp" data-t="27:48:00">[27:48:00]</a>. This points to a "fundamental limitation of LLMs" related to their internal "layers" or processing capacity <a class="yt-timestamp" data-t="28:20:00">[28:20:00]</a>.
*   **False Positives**: LLMs can generate high false positive rates for medically specific questions (e.g., "post-traumatic injury") because their training data includes broader, layperson understandings of concepts, not just precise medical definitions <a class="yt-timestamp" data-t="31:49:00">[31:49:00]</a>.

### Healthcare System Inertia
*   **Slow Prototyping**: Health systems and insurance companies are "not good at rapidly prototyping things" <a class="yt-timestamp" data-t="25:01:00">[25:01:00]</a>.
*   **Enterprise Sales Focus**: In health tech, "the best products in healthcare unfortunately do not win; it really still is the best enterprise sales processes that win" <a class="yt-timestamp" data-t="25:29:00">[25:29:00]</a>. This means founders often need to prioritize client trust and engagement over product refinement <a class="yt-timestamp" data-t="25:42:00">[25:42:00]</a>.

### Physical vs. Virtual Care and Business Models
*   **"Leakage" from Virtual Care**: While about two-thirds of claims could theoretically be handled virtually, physical interactions (e.g., lab tests, foot exams for diabetics) remain necessary <a class="yt-timestamp" data-t="57:52:00">[57:52:00]</a>. This need for in-person care can "sidetrack" patients away from digital doctor interactions, limiting the full replacement of physicians by AI <a class="yt-timestamp" data-t="59:29:00">[59:29:00]</a>.
*   **Misaligned Incentives**: Large health systems often lack financial incentive to transition to lower-cost care channels, as this could lead to reduced reimbursement from insurers and the government <a class="yt-timestamp" data-t="59:50:00">[59:50:00]</a>.

### Safety and Inference
*   **Safety Layer**: A significant challenge is ensuring AI outputs are safe and not "insulting" or inaccurate, often requiring a human-in-the-loop for dangerous use cases <a class="yt-timestamp" data-t="50:44:00">[50:44:00]</a>.
*   **Faster Inference Times**: The desire for faster inference times and the ability to run multiple AI outputs in parallel for verification (e.g., generating a thousand code listings and picking the best) is a key need for improved AI applications <a class="yt-timestamp" data-t="51:27:00">[51:27:00]</a>.

## [[Challenges and opportunities in AI model development and infrastructure | Opportunities in AI Model Development and Infrastructure]]

Despite challenges, AI offers significant opportunities:

### Underhyped Areas
*   **Voice Outputs**: The potential for voice outputs in healthcare AI is seen as underhyped, offering quick progress as long as it's not used for clinical advice <a class="yt-timestamp" data-t="01:00:52">[01:00:52]</a>.
*   **Regulatory Filings Composition**: Automating the generation of regulatory documentation for entities like the NCQA or State Health Departments could significantly reduce overhead <a class="yt-timestamp" data-t="53:31:00">[53:31:00]</a>.
*   **Fraud, Waste, and Abuse Detection**: This area is ripe for disruption, as it is currently dominated by "very old school players" making substantial profits <a class="yt-timestamp" data-t="56:16:00">[56:16:00]</a>.

### AI Doctor (Long-term Vision)
The concept of an "AI doctor" is seen as inevitable, given that medical knowledge is highly "regimented," "algorithmic," and based on "existing knowledge" and "inference based on concrete data points" <a class="yt-timestamp" data-t="56:59:00">[56:59:00]</a>.

### Development Strategies
*   **Chain of Thought**: Chaining LLMs to each other, effectively expanding their "layer space," helps solve complex tasks by breaking them into multiple steps <a class="yt-timestamp" data-t="29:52:00">[29:52:00]</a>.
*   **Self-Consistency Questionnaires**: Prompting an LLM to generate its own ways of interpreting data (e.g., 30 different ways a post-traumatic injury might appear in medical records) and then evaluating these methods independently can significantly improve accuracy <a class="yt-timestamp" data-t="33:38:00">[33:38:00]</a>.
*   **Hierarchical Prompting**: For complex systems like claims processing, providing LLMs with traces at a high level of hierarchy and allowing them to "double click" into specific functions for more detail is effective <a class="yt-timestamp" data-t="38:20:00">[38:20:00]</a>.
*   **General Purpose vs. Specialized Models**: While specialized healthcare-specific models exist (e.g., Google's Med-PaLM), general-purpose models like GPT-4 often maintain better "alignment" and follow instructions more reliably, especially for formatting requirements like JSON <a class="yt-timestamp" data-t="43:40:00">[43:40:00]</a>. The current best approach is to use the biggest general model for reasoning and potentially combine it with Retrieval Augmented Generation (RAG) and fine-tuning, as both methods offer independent performance improvements <a class="yt-timestamp" data-t="45:09:00">[45:09:00]</a>.

## [[Enterprise AI adoption challenges and solutions | Enterprise AI Adoption and Team Structure]]

Oscar Health employs a hybrid model for AI development, fostering both centralization and decentralization:
*   **Centralized "Pod"**: A 7-person team (2 product managers, data scientists, engineers) holds weekly office hours to assist other teams with AI queries and maintains three core projects <a class="yt-timestamp" data-t="47:10:00">[47:10:00]</a>. They also track all AI projects across the company <a class="yt-timestamp" data-t="50:05:00">[50:05:00]</a>.
*   **Weekly Hacking Sessions**: These informal sessions encourage sharing of ideas, successes, and failures, lowering the barrier for experimentation across the company <a class="yt-timestamp" data-t="47:54:00">[47:54:00]</a>.

This structure facilitates learning and rapid iteration, as much of the effective prompting and systems design knowledge is gained through hands-on experimentation rather than formal literature <a class="yt-timestamp" data-t="40:48:00">[40:48:00]</a>.

## Overhyped vs. Underhyped AI in Healthcare

*   **Overhyped**: Clinical chatbots, generally <a class="yt-timestamp" data-t="01:00:46">[01:00:46]</a>.
*   **Underhyped**: Voice outputs <a class="yt-timestamp" data-t="01:00:52">[01:00:52]</a>.

To learn more about Oscar's AI work, visit hi.oscar.com or follow Mario Scher on Twitter (@MarioTS) <a class="yt-timestamp" data-t="01:01:49">[01:01:49]</a>.