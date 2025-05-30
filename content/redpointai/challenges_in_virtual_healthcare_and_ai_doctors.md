---
title: Challenges in virtual healthcare and AI doctors
videoId: VUBfFv-Un3c
---

From: [[redpointai]] <br/> 

The application of Artificial Intelligence (AI) in healthcare, particularly in virtual care settings and the development of AI doctors, presents unique challenges despite its immense potential for efficiency and cost reduction <a class="yt-timestamp" data-t="00:04:37">[00:04:37]</a>. While AI can significantly impact healthcare by transforming informal language into formal data (and vice-versa) <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>, its full integration into clinical practice faces several hurdles.

## Limitations of AI in Clinical Use Cases

Large Language Models (LLMs) are incredibly adept at translating between formal and informal language, which is crucial in healthcare given the mix of highly formalized codes (ICD-10, CPT) and human conversations (patient-provider dialogue, medical record notes) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. However, [[implementing_ai_in_healthcare_systems | implementing AI in healthcare systems]] for clinical applications currently faces several limitations:

*   **Subtle Contextual Knowledge**
    *   Human-written medical summaries often contain subtle contextual knowledge that LLMs cannot possess <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>. This includes a provider remembering previous conversations with a patient that aren't explicitly documented <a class="yt-timestamp" data-t="00:07:28">[00:07:28]</a>.
    *   Geographical or environmental factors, such as local transportation options or daily weather, are critical contextual pieces known to human care agents but not readily available to LLMs unless specifically provided <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
    *   To improve LLM performance in these "wide-open" clinical scenarios, it's essential to enhance the LLM's "horizon of knowledge" by feeding it more comprehensive and relevant data <a class="yt-timestamp" data-t="00:07:53">[00:07:53]</a>.

*   **Unclean Inputs and Outputs**
    *   Unlike administrative tasks with clean, structured inputs and outputs (e.g., claims processing) <a class="yt-timestamp" data-t="00:06:14">[00:06:14]</a>, clinical use cases often involve less standardized data <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. This "unfair playing field" makes it challenging for LLMs to perform accurately <a class="yt-timestamp" data-t="00:07:41">[00:07:41]</a>.

*   **False Positives in Medical Extraction**
    *   LLMs can struggle with specific medical concepts that have different meanings in layperson's terms versus formal medical definitions <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>. For example, the term "post-traumatic injury" is a common source of false positives for LLMs when deciding on care authorization because the model's training data includes a broader, more common understanding of the term, not the specific, regulated definition used in utilization management <a class="yt-timestamp" data-t="00:32:00">[00:32:00]</a>. This issue can be mitigated by having the LLM generate its own self-consistency questionnaires and breaking down complex questions into sub-prompts <a class="yt-timestamp" data-t="00:33:38">[00:33:38]</a>.

## Specific Challenges for AI Doctors

While the idea of an AI doctor is promising given the algorithmic nature of medical knowledge <a class="yt-timestamp" data-t="00:57:05">[00:57:05]</a>, several practical issues remain:

*   **Safety and Direct Patient Interaction**
    *   One of the primary [[challenges_and_strategies_in_ai_deployment | challenges and strategies in AI deployment]] for clinical AI is safety <a class="yt-timestamp" data-t="00:57:42">[00:57:42]</a>. It is currently very difficult to allow an LLM to talk directly to an end-user due to the risk of hallucinations or biases <a class="yt-timestamp" data-t="00:04:49">[00:04:49]</a>, <a class="yt-timestamp" data-t="00:57:44">[00:57:44]</a>. Current solutions involve a "human in the loop," where a doctor or care guide reviews AI-generated summaries and explanations before they reach the patient <a class="yt-timestamp" data-t="00:50:57">[00:50:57]</a>.

*   **Necessity of Physical Interaction**
    *   Despite many medical claims being suitable for virtual settings (an estimated two-thirds) <a class="yt-timestamp" data-t="00:58:18">[00:58:18]</a>, certain procedures or examinations require in-person interaction (e.g., a foot exam for a diabetic patient) <a class="yt-timestamp" data-t="00:58:31">[00:58:31]</a>.
    *   This requirement for physical interaction leads to "leakage" from virtual care <a class="yt-timestamp" data-t="00:59:31">[00:59:31]</a>. As long as lab tests and hands-on physical assessments cannot be conducted virtually, AI cannot entirely replace human physicians or fundamentally transform the healthcare system <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a>.

*   **Business Model Incentives**
    *   A significant systemic challenge is the lack of incentive for large health systems to shift towards lower-cost virtual care channels <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a>. Such a shift could lead to pressure from insurance companies and the government to reduce reimbursement costs, potentially impacting capacity <a class="yt-timestamp" data-t="01:00:06">[01:00:06]</a>.
    *   While insurers are well-positioned to deploy automated virtual primary care, they often lack sufficient member engagement to do so effectively <a class="yt-timestamp" data-t="01:00:17">[01:00:17]</a>.

## Current State of AI in Clinical Contexts

Currently, clinical chatbots are considered "overhyped" compared to their actual capabilities and immediate applicability <a class="yt-timestamp" data-t="01:00:46">[01:00:46]</a>. However, advancements in voice outputs are seen as "underhyped" and offer significant potential for progress, especially in non-clinical contexts <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>.

Despite these [[challenges_and_advancements_in_ai_technology | challenges and advancements in AI technology]], the goal remains to harness AI for its transformative potential in healthcare, recognizing that administrative use cases currently yield faster, more tangible results than complex clinical applications <a class="yt-timestamp" data-t="00:05:08">[00:05:08]</a>.