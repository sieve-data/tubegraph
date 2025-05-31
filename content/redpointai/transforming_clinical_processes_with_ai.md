---
title: Transforming clinical processes with AI
videoId: VUBfFv-Un3c
---

From: [[redpointai]] <br/> 

Large Language Models (LLMs) are poised to have a significant impact on healthcare, particularly by bridging the gap between informal and formal language <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Healthcare involves highly formalized data like ICD10 and CPT codes, as well as informal human interactions such as patient-provider conversations and electronic medical record notes <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. LLMs excel at transforming data between these structured and unstructured formats <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

Historically, the healthcare industry has seen relatively limited algorithmic adoption compared to other sectors <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. However, LLMs can facilitate greater transparency and bidirectionality in healthcare interactions, leading to a system where patients can quickly understand costs or explore alternative treatments <a class="yt-timestamp" data-t="00:04:04">[00:04:04]</a>.

## Clinical Use Cases at Oscar Health

Oscar Health, a health insurance company that also provides care to patients, is actively experimenting with LLMs like GPT-4 in various aspects of healthcare <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. While most initial applications are administrative, one key clinical focus is leveraging AI to reduce medical costs and improve patient outcomes <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

Specific clinical applications include:
*   **Medical Record Generation** Oscar Health uses LLMs to summarize conversations between providers and members in virtual primary care settings, generating medical records from these summaries <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a> <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   **Lab Test Summarization** LLMs are used to summarize lab test results within the Oscar Medical Group <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Interacting with Medical Records** The biggest clinical use case is allowing doctors, customer service agents, and other Oscar personnel to "talk to" their own medical records, enabling easier information retrieval and analysis <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.

## Challenges in Clinical AI Adoption

Despite the potential, implementing AI in clinical settings faces several challenges:

*   **Contextual Knowledge Gaps** Human-written summaries often contain subtle contextual knowledge that LLMs cannot access, such as a provider's memory of a previous conversation with a patient not recorded in the medical records <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. LLMs struggle when inputs and outputs are "less clean," requiring improvements in the breadth of knowledge fed into the model <a class="yt-timestamp" data-t="00:07:38">[00:07:38]</a> <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>.
*   **Regulatory Hurdles** [[Enterprise adoption and use cases for AI | Healthcare]] is a highly regulated industry. Adherence to regulations like HIPAA, which prevents sharing patient-specific information without proper agreements (Business Associate Agreements or BAAs), is crucial <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a> <a class="yt-timestamp" data-t="00:21:07">[00:21:07]</a>. New models from providers like Google or OpenAI require time to become HIPAA-compliant <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>.
*   **Safety and Hallucinations** AI models can hallucinate or perpetuate biases present in their training data, posing significant safety concerns when applied to clinical decision-making <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Currently, any clinical use case with potential danger involves a human in the loop for verification <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.
*   **Physical Interaction Limitations** A significant portion of healthcare still requires physical interaction. Research at Oscar suggested that while two-thirds of claims could theoretically be handled virtually, this doesn't translate to two-thirds of *people* <a class="yt-timestamp" data-t="00:58:21">[00:58:21]</a>. Many chronic conditions, for example, require in-person exams (e.g., foot exams for diabetics), leading to "leakage" from virtual care if in-person needs are not seamlessly integrated <a class="yt-timestamp" data-t="00:58:28">[00:58:28]</a> <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a>.
*   **Business Model Incentives** Health systems often lack incentive to switch to lower-cost care delivery channels, as this could lead to reduced reimbursement costs and capacity reduction <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. Insurers, while in a good position to deploy automated virtual primary care, often lack the member engagement to do so effectively <a class="yt-timestamp" data-t="01:00:17">[01:00:17]</a>.

## Overhyped and Underhyped Areas

*   **Overhyped**: Clinical chatbots are currently considered overhyped due to the safety and interaction challenges <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>.
*   **Underhyped**: Voice outputs are seen as underhyped, with potential for significant progress, especially in non-clinical contexts <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>.

## Future Outlook

The long-term goal is to replace caregivers and clinical intelligence with machine intelligence, potentially reducing the cost of doctor visits significantly and replacing specialists with AI <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. This vision will require overcoming current limitations related to hallucinations, safety, and biases in training data <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>.

For developing healthcare AI solutions, particularly in the clinical space, a founder might consider very obscure niches. For example, using generative AI to compose regulatory filings and clinical reports, which are often lengthy and require natural language generation, presents a compelling opportunity <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a> <a class="yt-timestamp" data-t="00:54:28">[00:54:28]</a>. This approach leverages AI's strength in text generation for highly specialized and regulated documentation.

Regarding the debate on general purpose versus healthcare-specific models, experience at Oscar suggests that specialized models often lose "alignment" and struggle to follow instructions (e.g., generating JSON output) <a class="yt-timestamp" data-t="00:44:10">[00:44:10]</a> <a class="yt-timestamp" data-t="00:44:20">[00:44:20]</a>. Therefore, for now, using the largest general-purpose model for better reasoning, combined with techniques like Retrieval Augmented Generation (RAG) and fine-tuning, tends to yield better results <a class="yt-timestamp" data-t="00:45:09">[00:45:09]</a> <a class="yt-timestamp" data-t="00:45:37">[00:45:37]</a>.

Ultimately, the future of [[AI in healthcare and insurance | healthcare AI]] will depend on evolving AI capabilities, addressing regulatory and safety concerns, and aligning business models to support innovative care delivery. The development of AI within healthcare organizations benefits from knowledge sharing and a culture that encourages experimentation, even with failures <a class="yt-timestamp" data-t="00:48:57">[00:48:57]</a>.