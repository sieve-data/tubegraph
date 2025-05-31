---
title: Exploring use cases and challenges of AI in healthcare systems
videoId: VUBfFv-Un3c
---

From: [[redpointai]] <br/> 

The "Unsupervised Learning" podcast, hosted by Jacob Efron, featured Mario Scher, CTO and co-founder of Oscar Health, a $3 billion public health insurance company. Oscar Health is recognized for its innovation in technology and healthcare over the past decade <a class="yt-timestamp" data-t="00:00:24">[00:00:24]</a>. Scher provided insights into implementing AI models for real-world use cases and broader perspectives on the future of [[ai_in_healthcare_and_insurance | AI in healthcare]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>. Oscar Health operates as both an insurer and a care provider, actively experimenting with GPT-4 in various healthcare contexts <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. They were among the first to gain regulatory approval from OpenAI to work in healthcare <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## AI's Impact in Healthcare

Mario Scher believes that Large Language Models (LLMs) excel at transforming informal language into formal language and vice-versa <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Healthcare, with its mix of highly formalized codes (e.g., ICD-10, CPT, utilization management guidelines) and human language (e.g., patient-provider conversations, medical record notes), is an industry where LLMs can have a significant impact <a class="yt-timestamp" data-t="00:02:00">[00:02:00]</a>.

Historically, healthcare has seen relatively less algorithmic coverage compared to other industries, lacking an equivalent of PageRank <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Existing predictive models, such as logistic regressions, often halted at the interface between formal and informal language <a class="yt-timestamp" data-t="00:02:46">[00:02:46]</a>. LLMs, however, are adept at bridging this gap <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

In the next five years, AI is expected to revolutionize the administrative side of healthcare, making processes like claims payment, authorizations, and cost transparency real-time and bidirectional <a class="yt-timestamp" data-t="00:03:09">[00:03:09]</a>. This could lead to patients knowing costs upfront and understanding care alternatives <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>. Beyond this, the long-term goal is to replace caregivers and clinical intelligence with machine intelligence, potentially reducing the cost of doctor visits significantly <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. This clinical application, however, faces challenges related to hallucinations, safety, and bias <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>.

## Oscar Health's AI Applications

Oscar Health prioritizes [[enterprise_adoption_and_use_cases_for_ai | AI adoption]] based on three financial levers:
1.  **Growth and Retention**: Enhancing member acquisition and retention <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
2.  **Operational Efficiency**: Streamlining administrative processes <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
3.  **Medical Cost Reduction and Outcomes Improvement**: Directly impacting the majority of healthcare costs <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

### Retention Campaigns
Oscar leverages AI to run outbound campaigns to retain members during the six-week annual enrollment period <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. These campaigns personalize messages to remind members of positive experiences with Oscar in the preceding 12 months <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>.

AI helps tailor messaging based on member personas:
*   Reminding specific demographics (e.g., Asian-Americans) about preventative care like colorectal cancer screenings proved effective <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>.
*   Chronically ill members respond better to messages emphasizing convenience, while generally healthy members resonate more with empathetic messages <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.

LLMs, like GPT-4, have been effective "out of the box" for extracting information from customer service conversations to identify patient issues and persona characteristics <a class="yt-timestamp" data-t="00:15:48">[00:15:48]</a>. They can also assist in tasks like inferring ethnicity from names or detecting conversation languages to fill in missing member data <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

### Administrative Use Cases
Oscar is phasing out manual note-taking for customer service calls, relying entirely on LLMs for call summarization <a class="yt-timestamp" data-t="00:17:28">[00:17:28]</a>. Other launched administrative applications include:
*   Lab test summarization in the Oscar Medical Group <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   Secure messaging medical records generation <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   Claims explainers for internal care guides <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>.

These administrative improvements aim to save "cents PMPM" (per member per month), which can accumulate into significant savings for an insurance company <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

### Clinical Use Cases
One of the earliest and biggest clinical use cases involves enabling doctors and other Oscar personnel to "talk to the medical records" <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.

## [[Challenges in AI Adoption and Deployment | Challenges in AI Adoption and Deployment]] in Healthcare

Integrating AI into healthcare presents several unique [[Challenges and opportunities of AI integration in healthcare | challenges]].

### Regulatory Hurdles
Healthcare is a highly regulated industry, with HIPAA (Health Insurance Portability and Accountability Act) being a major constraint <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. HIPAA restricts the sharing of patient-specific information <a class="yt-timestamp" data-t="00:21:01">[00:21:01]</a>. AI vendors, like OpenAI, must sign Business Associate Agreements (BAAs) to handle protected health information <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. Oscar Health was the first organization to sign a BAA directly with OpenAI <a class="yt-timestamp" data-t="00:21:17">[00:21:17]</a>.

New AI models from providers like Google's Gemini Ultra are not immediately covered under existing HIPAA agreements, requiring a waiting period (typically 3-4 months) before real medical data can be used <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. During this period, synthetic or anonymized test data is used <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.

### Data Cleanliness and Contextual Knowledge
In administrative use cases, inputs and outputs are typically very clean and structured (e.g., claims data in EDI format) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>. However, in clinical use cases, this is often not the case <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. When summarizing conversations between providers and members, human-written summaries often contain subtle contextual knowledge that LLMs cannot access, such as a provider remembering a previous, unrecorded conversation with a patient <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. This "horizon of knowledge" needs to be expanded for LLMs to improve performance in open-ended clinical scenarios <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.

### Trust and Prototyping
Hospitals and insurance companies often require extensive security and policy reviews, making rapid prototyping difficult <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. Building trust with these organizations is paramount and cannot be outsourced solely to certifications like "High Trust" <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>. The focus for founders should be on fostering relationships and collaborative testing rather than solely on product tweaking <a class="yt-timestamp" data-t="00:25:23">[00:25:23]</a>.

### LLM Limitations
Even advanced LLMs like GPT-4 exhibit fundamental limitations:
*   **Compositional Tasks**: GPT-4 struggles with tasks that require multiple steps of processing and aggregation within a single prompt, such as categorizing and then counting different types of customer service calls <a class="yt-timestamp" data-t="00:27:35">[00:27:35]</a>. This is believed to be due to how Transformers process information across layers <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>.
*   **False Positives**: LLMs can yield high false positives on seemingly simple binary questions, like whether a member has a "post-traumatic injury," because the term has a specific, formal definition in a clinical context that differs from its common understanding in the training data <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>.

### Business Model Disincentives
For large health systems, there's often little incentive to switch to lower-cost care delivery channels (like virtual care) because it can lead to pressure from insurers and government to reduce reimbursement costs <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a>. This "conundrum of healthcare" creates a barrier to broader adoption of cost-saving AI solutions <a class="yt-timestamp" data-t="01:00:24">[01:00:24]</a>.

## Strategies for AI Implementation

### Prompting Strategies
To overcome LLM limitations, strategies like "chain of thought" prompting are used, effectively chaining LLMs together to expand their "layer space" and manage complex tasks <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>. For tasks like medical record extraction, a "self-consistency questionnaire" approach can be employed <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>. This involves prompting the LLM to generate multiple ways a concept might appear in medical records, then independently evaluating each, and integrating the findings <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a>.

For complex claim explanations, Oscar provides LLMs with hierarchical traces of their internal rule base, allowing the model to "double-click" on specific functions for more detail rather than processing the entire thousand-line logic at once <a class="yt-timestamp" data-t="00:38:18">[00:38:18]</a>. This helps manage context window limitations and improves accuracy <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>.

### Model Choice
Oscar has consistently found that general-purpose models like GPT-4, despite not being specialized for healthcare, outperform specialized models (like Google's Med-PaLM) <a class="yt-timestamp" data-t="00:44:00">[00:44:00]</a>. Specialized models tend to "lose alignment," struggling with basic instructions like generating output in JSON format <a class="yt-timestamp" data-t="00:44:11">[00:44:11]</a>. Until symbolic processing (planning) can be decoupled from content generation in LLMs, the biggest general-purpose model is preferred for better reasoning <a class="yt-timestamp" data-t="00:45:09">[00:45:09]</a>.

### RAG and Fine-tuning
A recent paper suggests that combining Retrieval Augmented Generation (RAG) and fine-tuning yields independent improvements in performance, indicating that both strategies are beneficial for LLM applications <a class="yt-timestamp" data-t="00:45:15">[00:45:15]</a>.

## Structuring AI Teams

Oscar Health's approach to structuring AI teams originated from a hackathon <a class="yt-timestamp" data-t="00:46:26">[00:46:26]</a>. They established a dedicated "Pod" of seven people (product managers, data scientists, engineers) <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. This Pod provides:
*   **Office Hours**: Weekly sessions where anyone in the company can bring their AI prompts and ideas for feedback <a class="yt-timestamp" data-t="00:47:22">[00:47:22]</a>.
*   **Dedicated Projects**: The Pod has its own set of three priority projects to ensure practical application and completion, avoiding endless research <a class="yt-timestamp" data-t="00:47:34">[00:47:34]</a>.
*   **Weekly Hacking Sessions**: Open sessions where anyone can share their AI projects, fostering a culture of experimentation and knowledge sharing <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.

This mixed model, with centralized support and decentralized implementation, encourages experimentation and lowers the bar for participation across the company <a class="yt-timestamp" data-t="00:50:10">[00:50:10]</a>.

## Overhyped and Underhyped Healthcare AI

*   **Overhyped**: Clinical chatbots generally <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>.
*   **Underhyped**: Voice outputs <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>.

## Future Opportunities in Healthcare AI

If starting a new healthcare AI company, Mario Scher suggests focusing on a very obscure niche where technical solutions can solve specific issues for non-technical users <a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a>. An example is the **composition of regulatory filings** <a class="yt-timestamp" data-t="00:53:37">[00:53:37]</a>. LLMs could watch data flow and automatically generate regulatory reports, including clinical reports for organizations like NCQA or state health departments, which are often in natural language format <a class="yt-timestamp" data-t="00:54:11">[00:54:11]</a>.

Regarding **prior authorization companies**, while seemingly interesting, Scher advises caution as this is a core competency for insurance companies, and external solutions might face limitations if not deeply integrated and interactive <a class="yt-timestamp" data-t="00:55:59">[00:55:59]</a>.

A more promising area for disruption is **fraud, waste, and abuse** within the industry, which is currently dominated by older, expensive players <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>.

## The "AI Doctor" Future

Mario Scher sees no reason why an "AI doctor" future shouldn't materialize <a class="yt-timestamp" data-t="00:56:59">[00:56:59]</a>. The medical profession is highly computerized and algorithmic, relying on existing knowledge and inference from concrete data points, making it well-suited for LLM applications <a class="yt-timestamp" data-t="00:57:12">[00:57:12]</a>.

However, several practical issues remain:
*   **Safety**: Currently, it is very difficult for LLMs to directly interact with end-users in a clinical context due to safety concerns <a class="yt-timestamp" data-t="00:57:42">[00:57:42]</a>. Outputs must be vetted by a human-in-the-loop <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.
*   **Physical Interaction**: While two-thirds of claims *could* be handled virtually, many patients (e.g., diabetics) still require in-person care for specific procedures like foot exams <a class="yt-timestamp" data-t="00:58:16">[00:58:16]</a>. This need for physical interaction creates "leakage" that prevents clinical chatbots from fully replacing physicians or transforming the system on a larger scale <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a>.
*   **Business Model**: Large health systems often lack financial incentives to adopt lower-cost virtual care channels, as it could lead to reduced reimbursement rates <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a>. Insurers are better positioned to deploy automated virtual primary care but struggle with member engagement <a class="yt-timestamp" data-t="01:00:15">[01:00:15]</a>.

## Learn More

To learn more about Mario Scher and Oscar Health's AI work, visit [hi.oscar.com](https://hi.oscar.com) for articles, insights, and papers <a class="yt-timestamp" data-t="01:01:50">[01:01:50]</a>. Mario also shares his explorations and Oscar's projects on Twitter ([@MarioTS](https://twitter.com/MarioTS)) <a class="yt-timestamp" data-t="01:02:07">[01:02:07]</a>.