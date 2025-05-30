---
title: Administrative and clinical use cases of AI in health insurance
videoId: VUBfFv-Un3c
---

From: [[redpointai]] <br/> 

Oscar Health, a $3 billion public health insurance company, has been at the forefront of innovating in health technology for the past decade, actively experimenting with large language models (LLMs) like GPT-4 in various healthcare applications <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Mario Schaer, CTO and co-founder of Oscar Health, shared insights into the practical implementation of these models for real-world use cases, as well as a broader outlook on the future of healthcare and AI <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## AI's Impact in Healthcare

LLMs are particularly effective at transitioning between informal and formal language <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Healthcare, with its highly formalized codes (e.g., ICD-10, CPT, utilization management guidelines) and abundant human language (patient-provider conversations, electronic medical record notes), is uniquely positioned to benefit from this capability <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. While healthcare has seen less algorithmic coverage compared to other industries, LLMs can now bridge this gap, enabling greater transparency and efficiency <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Administrative Use Cases

Initially, many AI use cases in healthcare will focus on administrative tasks <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. The goal is to make processes like claims, authorizations, and cost transparency real-time and bidirectional <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

<br>
> [!example] Examples
> *   **Claims Explanation**: LLMs can translate complex claim rule traces into understandable language for laypersons, explaining why a claim was paid or denied <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.
> *   **Call Summarization**: LLMs can summarize customer service calls, potentially phasing out manual note-taking by care guides <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
> *   **Lab Test Summarization**: Launched in Oscar's medical group <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
> *   **Secure Messaging Medical Records Generation**: Implemented in Oscar's Medical Group <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
> *   **Improving Growth and Retention**: Running outbound campaigns to remind members of Oscar's benefits and personalized care (e.g., reminding Asian-Americans about colorectal cancer screenings) <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>. Messaging can be tailored based on member personas, such as focusing on empathy for chronically ill members and convenience for generally healthy ones <a class="yt-timestamp" data-t="00:14:52">[00:14:52]</a>.
> *   **Ethnicity Information Extraction**: LLMs can infer ethnicity from names or conversation language, which aids in matching members to appropriate doctors and conversations <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
<br>

Oscar's top four use cases include three administrative ones and one clinical <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>. The administrative applications are expected to yield tangible results more quickly <a class="yt-timestamp" data-t="00:05:22">[00:05:22]</a>, with savings estimated in "cents PMPM" (per member per month) <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

A challenge in administrative tasks like claims processing is the need for the LLM to process information at a specific level of hierarchy, requiring careful prompting to avoid context window issues and to focus on relevant details <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.

### Clinical Use Cases

The long-term goal is to replace caregivers and clinical intelligence with machine intelligence, ultimately reducing the cost of doctor visits and potentially replacing specialists with AI <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

<br>
> [!example] Examples
> *   **Medical Record Generation**: LLMs can summarize conversations between Oscar providers and members in [[challenges_in_virtual_healthcare_and_ai_doctors | virtual care settings]] to generate medical records <a class="yt-timestamp" data-t="00:06:50">[00:06:50]</a>.
> *   **"Talking to the Medical Records"**: Enabling doctors, customer service agents, or anyone within Oscar to query medical records using natural language <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.
<br>

<br>
> [!warning] Challenges in Clinical AI
> *   **Contextual Knowledge Gaps**: LLMs often lack subtle contextual knowledge that human providers possess (e.g., remembering a previous conversation not in the medical record), leading to less accurate summaries <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. Improving LLM performance in clinical settings requires not just better models but also expanding their "horizon of knowledge" through comprehensive input data <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
> *   **False Positives**: For complex concepts like "post-traumatic injury" in utilization management, LLMs can generate a high rate of false positives because their training data includes broader, layperson associations of the term, differing from its precise medical definition <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>. Strategies like self-consistency questionnaires, providing short examples, and pre-processing steps where the LLM generates its own knowledge about how the condition might appear in records can improve accuracy <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>.
> *   **Safety**: Ensuring patient safety is paramount, making it difficult for LLMs to directly interact with end-users in clinical contexts due to the risk of hallucinations or insulting outputs <a class="yt-timestamp" data-t="00:50:50">[00:50:50]</a>. Current solutions often involve a human in the loop <a class="yt-timestamp" data-t="00:51:00">[00:51:00]</a>.
> *   **Physical Interaction**: A significant portion of healthcare (around one-third of claims data) still requires in-person interaction, leading to "leakage" from [[challenges_in_virtual_healthcare_and_ai_doctors | virtual care]] to in-person visits and reducing patient loyalty to a single primary care provider <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a>.
> *   **Business Model Incentives**: Large health systems currently have little financial incentive to switch to lower-cost [[cost_efficiency_and_accessibility_in_ai_technologies | channels of care delivery]] like automated virtual primary care, as it could lead to reduced reimbursement from insurers and the government <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a>.
<br>

## Regulation and Implementation

[[regulation_and_policy_implications_of_ai | Implementing AI in healthcare systems]] is subject to strict regulations, primarily HIPAA, which mandates business associate agreements (BAAs) to ensure patient data privacy <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. Oscar Health was notably the first organization to sign a BAA directly with OpenAI <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.

New LLM models from providers like Google (Gemini Ultra) or OpenAI typically require a waiting period (e.g., 3-4 months) before they are officially covered under existing HIPAA agreements <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. During this period, testing is done with synthetic or anonymized data <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>.

For companies looking to sell AI solutions to hospitals, formal requirements include security and policy reviews, often involving long checklists, and certifications like HiTrust <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>. However, gaining trust from hospitals is more critical than merely passing certifications <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>. The healthcare industry is generally slow at rapid prototyping and emphasizes enterprise sales processes over product perfection <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>.

Mario Schaer participated in a consortium of health systems and insurance companies that drafted principles for AI in healthcare, advocating for the democratization of analytics through AI <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.

## Structuring AI Teams

Oscar Health has a "Pod" structure for its AI team, comprising seven people, including product managers, data scientists, and engineers <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. This team holds weekly office hours and hacking sessions where anyone in the company can bring their AI ideas and discuss prompting strategies <a class="yt-timestamp" data-t="00:47:22">[00:47:22]</a>. The Pod also has its own three priorities to ensure project completion and avoid endless research <a class="yt-timestamp" data-t="00:47:34">[00:47:34]</a>. This structure balances centralized guidance with decentralized experimentation, fostering an environment where trying new things is encouraged <a class="yt-timestamp" data-t="00:50:10">[00:50:10]</a>.

## Overhyped, Underhyped, and Future Opportunities

*   **Overhyped**: Clinical chatbots, generally speaking <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>.
*   **Underhyped**: Voice outputs <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>.

Mario Schaer is most excited about OpenAI for its continued model development and Hugging Face for centralizing models <a class="yt-timestamp" data-t="01:01:13">[01:01:13]</a>.

Regarding commercial opportunities, he suggests focusing on very obscure niches in healthcare, such as [[regulation_and_policy_implications_of_ai | regulatory filings composition]] <a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a>. This includes generating regulatory documentation for health regulators, SEC compliance (Sox), NCQA clinical reports, and state health department reports <a class="yt-timestamp" data-t="00:54:02">[00:54:02]</a>. He views [[proactive_ai_interventions | prior authorization]] companies as risky, as it's a core competency of insurance companies <a class="yt-timestamp" data-t="00:55:59">[00:55:59]</a>. Another promising area is fraud, waste, and abuse detection, an industry currently dominated by outdated players <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>.

<br>
> [!info] Learn More
> To learn more about Oscar Health's AI work and insights, visit [Hi.Oscar.Health](https://hi.oscar.health) <a class="yt-timestamp" data-t="01:01:50">[01:01:50]</a>. Mario Schaer also shares his explorations on Twitter: @MarioTS <a class="yt-timestamp" data-t="01:02:07">[01:02:07]</a>.
>
> Mario also shared some fun, non-healthcare related AI ideas, including building an RPG game based on a company's internal documents and an Oregon Trail-like game where an LLM dynamically writes game mechanics as it's played <a class="yt-timestamp" data-t="01:02:32">[01:02:32]</a>.
<br>