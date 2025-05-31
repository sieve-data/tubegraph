---
title: Role of large language models in healthcare
videoId: VUBfFv-Un3c
---

From: [[redpointai]] <br/> 

Oscar Health, a $3 billion public health insurance company, has been at the forefront of innovating with technology in healthcare for the past decade <a class="yt-timestamp" data-t="00:00:20">[00:00:20]</a>. Mario Schaer, CTO and co-founder of Oscar Health, shares insights into the practical implementation of AI models for real [[exploring_use_cases_and_challenges_of_ai_in_healthcare_systems | use cases and challenges of AI in healthcare systems]] within the healthcare system <a class="yt-timestamp" data-t="00:00:47">[00:00:47]</a>. Oscar functions as both an insurer and a care provider, experimenting extensively with advanced AI models like GPT-4 <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>.

## LLMs as Language Translators in Healthcare

A key strength of Large Language Models (LLMs) is their ability to convert between informal and formal language <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Healthcare uniquely combines both: highly formalized language (e.g., ICD-10, CPT codes, utilization management guidelines) and highly human language (e.g., patient-provider conversations, electronic medical record notes) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This unique blend has historically limited algorithmic coverage in healthcare, where predictive models often stopped at the surface of formal language <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. LLMs excel at this threshold, moving back and forth between formal and informal language <a class="yt-timestamp" data-t="00:02:55">[00:02:55]</a>.

The ability of LLMs to present information at different levels of sophistication based on the end user is highly compelling <a class="yt-timestamp" data-t="00:05:32">[00:05:32]</a>. For example, they can translate complex insurance bills and claim statuses into understandable terms for patients <a class="yt-timestamp" data-t="00:05:39">[00:05:39]</a>, or transform clinical data for either doctor-to-doctor communication or patient-friendly summaries <a class="yt-timestamp" data-t="00:06:05">[00:06:05]</a>.

## AI Use Cases at Oscar Health

Oscar Health leverages [[ai_in_healthcare_and_insurance | AI in healthcare and insurance]] across three primary financial levers: growth and retention, operational efficiency (administrative), and clinical cost reduction/outcome improvement <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

### Growth and Retention
AI assists in retaining members by enabling personalized outbound campaigns, reminding them of benefits or specific preventative care actions taken, like colorectal cancer screenings <a class="yt-timestamp" data-t="00:13:42">[00:13:42]</a>. Different segments of members respond to different messaging; chronically ill members respond better to convenience, while generally healthy members respond better to empathy <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>. LLMs can extract personas and issues from customer service conversations to inform these strategies <a class="yt-timestamp" data-t="00:15:51">[00:15:51]</a>. They can also assist in filling missing demographic information, like ethnicity, by analyzing names or detecting conversation language <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.

### Administrative Use Cases
Initially, many [[transforming_clinical_processes_with_AI | transforming clinical processes with AI]] and use cases for LLMs at Oscar Health are administrative, aiming for real-time, transparent, and bidirectional processes <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. Examples include:
*   **Claims Explanation**: LLMs translate complex rule-based claim traces (e.g., 1,000 lines of logic) into understandable explanations for care guides or laypersons, detailing why a claim was paid or denied <a class="yt-timestamp" data-t="00:03:37">[00:03:37]</a>.
*   **Call Summarization**: LLMs are increasingly replacing manual note-taking by care guides during customer service calls <a class="yt-timestamp" data-t="00:17:22">[00:17:22]</a>.
*   **Lab Test Summarization**: Launched within Oscar's medical group <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Secure Messaging Medical Records Generation**: Also launched in the medical group <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   These administrative applications currently save "a few cents PMPM (per member per month)" <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

### Clinical Use Cases
While administrative applications offer immediate, tangible savings, the long-term goal is to replace caregivers and clinical intelligence with machine intelligence, significantly reducing the cost of doctor visits and potentially replacing specialists with AI <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. The biggest current clinical use case is enabling doctors to "talk to their own medical records" <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.

#### Challenges in Clinical AI
*   **Contextual Knowledge**: Human providers often possess subtle contextual knowledge (e.g., remembering previous conversations not explicitly in records) that LLMs lack, making it an "unfair playing field" when inputs and outputs are less clean <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. Improving LLM performance in clinical settings requires not just better models, but also expanding their "horizon of knowledge" by providing more context <a class="yt-timestamp" data-t="00:08:04">[00:08:04]</a>.
*   **Physical vs. Virtual Interaction**: While two-thirds of claims *could* be handled virtually, real-world patient loyalty to PCPs is low (only 28% of members stick to their attributed PCP) <a class="yt-timestamp" data-t="00:59:02">[00:59:02]</a>. This suggests that the need for in-person actions (e.g., lab tests, foot exams) causes "leakage" that prevents clinical chatbots from fully replacing physicians or the entire system <a class="yt-timestamp" data-t="00:59:42">[00:59:42]</a>.
*   **Business Models**: Health systems currently have little incentive to switch to lower-cost care delivery channels, as this could lead to reduced reimbursement <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. Insurers, while well-positioned to deploy automated virtual care, often lack the necessary member engagement <a class="yt-timestamp" data-t="01:00:15">[01:00:15]</a>.

## Regulatory and Implementation Challenges

Healthcare AI faces significant regulatory hurdles, primarily HIPAA (Health Insurance Portability and Accountability Act) <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>, which governs patient-specific information. Vendors must sign Business Associate Agreements (BAAs) to handle protected health information (PHI) <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. Oscar was the first organization to sign a BAA directly with OpenAI <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>.

New models, like Google's Gemini Ultra, are not immediately covered by existing BAA agreements, requiring a delay of three to four months before they can be used with real medical records <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. During this period, Oscar uses synthetic or anonymized test data <a class="yt-timestamp" data-t="00:22:46">[00:22:46]</a>.

Gaining trust and navigating enterprise sales processes are more critical than having the "best" product <a class="yt-timestamp" data-t="00:24:42">[00:24:42]</a>. Hospitals and insurance companies are generally slow to rapidly prototype or follow up on pilots <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. Industry collaborations, such as a consortium of health systems and insurers that wrote a document on principles for AI in healthcare, aim to democratize analytics and accelerate adoption <a class="yt-timestamp" data-t="00:26:03">[00:26:03]</a>.

## [[Limitations of AI language models | Limitations of AI language models]] and Troubleshooting LLMs

LLMs have specific limitations that impact their performance:
*   **Counting and Categorization**: GPT-4 can fail miserably at tasks requiring it to characterize and count occurrences of specific reasons from a batch of customer service calls, especially when the context window is large <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. This is a fundamental limitation, potentially due to how layers process tokens and synthesize information <a class="yt-timestamp" data-t="00:28:21">[00:28:21]</a>. This can be mitigated by splitting tasks into different steps or chaining models (e.g., Chain of Thought prompting) <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.
*   **False Positives**: LLMs can generate a high rate of false positives for concepts like "post-traumatic injury" when extracting information from medical records for utilization management <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>. This likely occurs because the model's training data contains layperson associations of the term, differing from its precise, regulated definition in healthcare <a class="yt-timestamp" data-t="00:32:52">[00:32:52]</a>. A solution involves using "self-consistency questionnaires," where the LLM generates multiple ways a concept might appear in records, which are then independently evaluated <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>.
*   **Context Window Issues**: Early attempts at claims explanation faced context window limitations (e.g., 8,000 tokens for GPT-4), as the full internal logic trace was too large <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>. The solution was to provide the traces at a higher hierarchical level, allowing the LLM to "double-click" on specific sub-procedures for more detail <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.

## [[specialized_vs_general_ai_models_in_translation | Specialized vs General AI models in translation]]

Oscar's experience suggests that when specializing a general-purpose model for a particular area (e.g., healthcare), there's a risk of losing "alignments," meaning the model may fail to follow simple instructions (e.g., formatting output in JSON) <a class="yt-timestamp" data-t="00:44:05">[00:44:05]</a>. The current recommendation is to use the biggest general-purpose model for the best reasoning and combine it with Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="00:45:09">[00:45:09]</a>. Recent research indicates that RAG and fine-tuning offer independent improvements in performance, suggesting both should be utilized <a class="yt-timestamp" data-t="00:45:31">[00:45:31]</a>.

## Structuring AI Teams

Oscar Health has adopted a successful model for structuring its AI teams <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>.
*   **AI Pod**: A dedicated team of seven people (two product managers, data scientists, engineers) provides office hours for anyone in the company working on AI <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. This centralized pod also has its own three product priorities to ensure tangible outcomes <a class="yt-timestamp" data-t="00:47:34">[00:47:34]</a>.
*   **Weekly Hacking Sessions**: A regular, informal gathering (e.g., Monday nights) where anyone can bring ideas and show off their AI projects <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>. The goal is to lower the bar for participation and encourage sharing of both successes and failures <a class="yt-timestamp" data-t="00:48:56">[00:48:56]</a>.
*   **Open Sharing**: The company encourages sharing of insights and practices both internally and externally, as evidenced by their public resources <a class="yt-timestamp" data-t="00:41:29">[00:41:29]</a>.

## Opportunities for AI Startups in Healthcare

For new [[challenges_and_opportunities_of_ai_integration_in_healthcare | AI in healthcare]] companies, obscure niches that solve very particular issues for non-technical users might be the most promising <a class="yt-timestamp" data-t="00:53:22">[00:53:22]</a>.
*   **Regulatory Filings Composition**: Automating the generation of regulatory documentation (e.g., for NCQA, state health departments, SOX compliance) could significantly reduce overhead <a class="yt-timestamp" data-t="00:53:37">[00:53:37]</a>.
*   **Fraud, Waste, and Abuse**: This industry segment is still dominated by older, expensive players, suggesting a ripe opportunity for disruption with AI <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>.
*   **Prior Authorization**: While many companies are entering this space, it's very close to the core competency of insurance companies <a class="yt-timestamp" data-t="00:55:22">[00:55:22]</a>. Startups might struggle if they cannot offer highly interactive or platform-based solutions <a class="yt-timestamp" data-t="00:55:46">[00:55:46]</a>.

## Overhyped and Underhyped AI in Healthcare

*   **Overhyped**: Clinical chatbots <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>.
*   **Underhyped**: Voice outputs <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>.

## Learning More

To learn more about Oscar Health's AI work and insights, visit their collection of papers and articles at [hi.oscar.health](https://hi.oscar.health) <a class="yt-timestamp" data-t="01:01:50">[01:01:50]</a>. Mario Schaer also posts his explorations and Oscar's work on Twitter (MarioTS) <a class="yt-timestamp" data-t="01:02:07">[01:02:07]</a>. He's interested in using LLMs for novel applications, such as generating RPGs from company documents or dynamic games like Oregon Trail <a class="yt-timestamp" data-t="01:02:40">[01:02:40]</a>.