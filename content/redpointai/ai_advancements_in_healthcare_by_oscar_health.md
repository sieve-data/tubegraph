---
title: AI advancements in healthcare by Oscar Health
videoId: VUBfFv-Un3c
---

From: [[redpointai]] <br/> 

Oscar Health, a $3 billion public [[implementing_ai_in_healthcare_systems | health insurance]] company, has been at the forefront of innovating in healthcare technology for the past decade <a class="yt-timestamp" data-t="00:00:18">[00:00:18]</a>. As both an insurer and a care provider, Oscar Health is actively experimenting with models like GPT-4 in various healthcare contexts <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. They were among the first to gain regulatory approval from OpenAI to work in healthcare <a class="yt-timestamp" data-t="00:00:38">[00:00:38]</a>.

## The Future of AI in Healthcare

Mario Schaer, CTO and co-founder of Oscar Health, believes that large language models (LLMs) are exceptionally good at translating between informal and formal language <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Healthcare, uniquely, possesses an abundance of both: highly formalized language (e.g., ICD-10 codes, CPT codes, utilization management guidelines) and highly human, informal language (e.g., conversations between providers and patients, electronic medical record notes) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. This capability of LLMs can bridge the gap that traditional algorithmic approaches have historically struggled with in healthcare <a class="yt-timestamp" data-t="00:02:25">[00:02:25]</a>.

Schaer anticipates that the next five years of healthcare will see administrative processes become real-time, bidirectional, and more transparent, driven by LLM capabilities <a class="yt-timestamp" data-t="00:03:51">[00:03:51]</a>. This would allow patients to know costs upfront, understand alternatives, and avoid issues like denied claims or authorization delays <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>. Longer term, the goal is to replace caregiver and clinical intelligence with machine intelligence, significantly reducing costs and replacing specialists with AI <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>.

## Oscar Health's AI Implementation

Oscar Health sequences its AI implementation, prioritizing [[administrative_and_clinical_use_cases_of_ai_in_health_insurance | administrative use cases]] before clinical ones <a class="yt-timestamp" data-t="00:05:06">[00:05:06]</a>. Currently, three out of their top four use cases are administrative, with one clinical <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

Oscar Health's financial outcomes are driven by three main levers <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>:
1.  **Growth and Retention:** Improving member acquisition and retention <a class="yt-timestamp" data-t="00:10:36">[00:10:36]</a>.
2.  **Operational Efficiency:** Streamlining administrative processes <a class="yt-timestamp" data-t="00:10:46">[00:10:46]</a>.
3.  **Clinical Cost Reduction and Outcome Improvement:** Directly impacting medical costs and patient health <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

### Key Use Cases and Applications

*   **Retention Campaigns:** Oscar Health utilizes LLMs to personalize outbound campaigns during the annual six-week re-enrollment period <a class="yt-timestamp" data-t="00:13:08">[00:13:08]</a>. This involves reminding members of beneficial services like colorectal cancer screenings, with messaging tailored to specific demographics (e.g., Asian-Americans) <a class="yt-timestamp" data-t="00:14:07">[00:14:07]</a>. They also differentiate messaging for chronically ill members (emphasizing convenience) versus generally healthy members (emphasizing empathy) <a class="yt-timestamp" data-t="00:14:51">[00:14:51]</a>.
*   **Ethnicity Information Capture:** LLMs help fill in missing ethnicity data for members by analyzing names or detected languages in conversations, enhancing personalization <a class="yt-timestamp" data-t="00:16:33">[00:16:33]</a>.
*   **Call Summarization:** LLMs are increasingly taking over manual note-taking for customer service calls, phasing out human intervention <a class="yt-timestamp" data-t="00:17:20">[00:17:20]</a>.
*   **Lab Test Summarization:** Implemented in the Oscar Medical Group <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
*   **Secure Messaging Medical Records Generation:** Also launched in the Oscar Medical Group <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
*   **Claims Explainers:** Providing internal care guides with clearer explanations of complex claim payment logic, translating formal rule traces into informal language <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. The goal is to explain why a claim was denied, or even why a specific amount was paid <a class="yt-timestamp" data-t="00:35:40">[00:35:40]</a>.
*   **Medical Record Interaction:** Enabling doctors, customer service agents, and other internal staff to "talk to" medical records <a class="yt-timestamp" data-t="00:18:52">[00:18:52]</a>.

## [[challenges_and_advancements_in_ai_technology | Challenges and Learnings in AI Deployment]]

### Regulatory Hurdles
Oscar Health, as a highly regulated insurance company, was fortunate to have a strong compliance foundation <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a>. A major constraint is HIPAA, which requires business associate agreements (BAAs) with AI providers like OpenAI <a class="yt-timestamp" data-t="00:20:55">[00:20:55]</a>. Oscar was reportedly the first organization to sign a BAA directly with OpenAI <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. New models from providers (e.g., Google's Gemini Ultra) are typically not immediately under existing HIPAA agreements, necessitating a wait of three to four months before real medical data can be used <a class="yt-timestamp" data-t="00:23:04">[00:23:04]</a>. During this period, Oscar uses synthetic or anonymized test data <a class="yt-timestamp" data-t="00:22:50">[00:22:50]</a>. For healthcare companies building their own models, security and policy reviews, often involving long checklists from hospitals, are necessary, with certifications like "High Trust" easing the process <a class="yt-timestamp" data-t="00:23:57">[00:23:57]</a>.

### LLM Limitations and Solutions
*   **Counting and Multi-step Reasoning:** LLMs struggle with tasks requiring multiple, distinct reasoning steps, such as categorizing and then counting different types of customer service calls based on a self-generated taxonomy <a class="yt-timestamp" data-t="00:27:30">[00:27:30]</a>. This is attributed to limitations in their "layers" or computational depth for complex, sequential tasks <a class="yt-timestamp" data-t="00:28:25">[00:28:25]</a>.
    *   **Solution:** Employing "Chain of Thought" prompting, which effectively chains multiple LLMs or prompts together to break down a complex task into smaller, manageable steps, overcoming the "token pollution" issue where too much information in a single pass confuses the model <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.
*   **Contextual Knowledge:** LLMs lack the subtle contextual knowledge that human providers possess (e.g., remembering a previous conversation not captured in formal records, or understanding local geographical nuances like public transport options) <a class="yt-timestamp" data-t="00:07:17">[00:07:17]</a>.
    *   **Solution:** The focus must be on improving the "horizon of knowledge" or the breadth of input provided to the LLM <a class="yt-timestamp" data-t="00:08:07">[00:08:07]</a>.
*   **False Positives in Medical Extraction:** A notable challenge was accurately identifying "post-traumatic injury" from medical records for utilization management, with LLMs producing a high rate of false positives <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>. This is because the LLM's training data contains diverse, layperson associations with the term, which do not align with its strict medical definition within utilization management guidelines <a class="yt-timestamp" data-t="00:33:01">[00:33:01]</a>.
    *   **Solution:** Implementing a "self-consistency questionnaire" where the LLM is prompted to generate 30 different ways a concept (e.g., post-traumatic injury) might appear in medical records. These generated examples are then used in the prompt to guide the LLM's evaluation in a multi-step process, improving accuracy <a class="yt-timestamp" data-t="00:33:43">[00:33:43]</a>.

### Prompting Strategies
Oscar's approach to prompting is largely empirical, with 90% of strategies developed through trial and error <a class="yt-timestamp" data-t="00:39:48">[00:39:48]</a>. Emphasis is placed on "systems design" – how LLM calls are chained together in a logical sequence – rather than just individual prompts <a class="yt-timestamp" data-t="00:40:30">[00:40:30]</a>.

## LLM Selection Strategy
Oscar Health prefers general-purpose models like GPT-4 over [[advancements_and_implications_of_ai_models_like_o1 | healthcare-specific models]] (e.g., Google's Med-PaLM) <a class="yt-timestamp" data-t="00:43:06">[00:43:06]</a>. The reason is that specialized models tend to "lose alignment," meaning they struggle to follow simple instructions, such as outputting information in JSON format <a class="yt-timestamp" data-t="00:44:03">[00:44:03]</a>. This loss of instruction-following ability outweighs the benefits of specialized training data <a class="yt-timestamp" data-t="00:44:20">[00:44:20]</a>. Until symbolic processing (planning/reasoning) can be decoupled from content generation in LLMs, bigger general models are preferred, often combined with Retrieval Augmented Generation (RAG) and fine-tuning <a class="yt-timestamp" data-t="00:44:41">[00:44:41]</a>.

## AI Team Structure
Oscar Health has developed a successful model for its AI team structure <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>:
*   **Hackathon Origins:** The current structure evolved from a highly popular AI hackathon, highlighting the need for sharing and discussion around prompting strategies <a class="yt-timestamp" data-t="00:46:23">[00:46:23]</a>.
*   **Centralized "Pod" Team:** A seven-person team (two product managers, data scientists, engineers) acts as a central resource <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>.
    *   **Office Hours:** They hold weekly office hours for any employee to get feedback on their AI prompts or ideas <a class="yt-timestamp" data-t="00:47:22">[00:47:22]</a>.
    *   **Dedicated Projects:** The Pod also has its own three core projects to complete, ensuring tangible output <a class="yt-timestamp" data-t="00:47:34">[00:47:34]</a>.
    *   **Weekly Hacking Sessions:** Monday night sessions are open to anyone in the company to share AI ideas, successful projects, or even failures, fostering an environment where trying and discussing are encouraged <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.
*   **Decentralized AI Projects:** Various teams across the company work on their own AI initiatives, and the Pod helps track and share these <a class="yt-timestamp" data-t="00:50:05">[00:50:05]</a>. This hybrid approach balances centralized guidance with decentralized experimentation.

## Future Opportunities and Over/Underhyped Areas in Healthcare AI

### Overhyped
*   **Clinical Chatbots (generally):** Currently, they are overhyped due to safety concerns (hallucinations, biases), the need for physical interaction in many medical scenarios, and adverse business models in the healthcare system <a class="yt-timestamp" data-t="00:49:00">[00:49:00]</a>, <a class="yt-timestamp" data-t="00:56:56">[00:56:56]</a>, <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>.

### Underhyped
*   **Voice Outputs:** This area has significant potential for rapid advancement, particularly for non-clinical applications <a class="yt-timestamp" data-t="01:00:55">[01:00:55]</a>.

### Commercial Opportunities
*   **Regulatory Filings Composition:** Automating the generation of complex regulatory documentation (e.g., for state regulators, NCQA, or even internal SOX compliance) using LLMs that can watch data flows <a class="yt-timestamp" data-t="00:53:35">[00:53:35]</a>.
*   **Fraud, Waste, and Abuse:** This industry segment is still dominated by older, expensive players and is ripe for AI disruption to reduce overpayment <a class="yt-timestamp" data-t="00:56:16">[00:56:16]</a>.
*   **Prior Authorization:** While many companies are entering this space, it's considered very close to the core competency of insurance companies. External solutions might struggle to achieve significant impact unless they offer highly interactive and platform-like integration, as insurers prefer to manage clinical management themselves <a class="yt-timestamp" data-t="00:55:20">[00:55:20]</a>.

### [[challenges_in_virtual_healthcare_and_ai_doctors | Challenges to AI Doctors / Virtual Healthcare]]
Even though approximately two-thirds of claims could theoretically be handled virtually (not two-thirds of people), significant barriers remain:
1.  **Safety:** Direct LLM-to-patient interaction is difficult due to the risk of hallucinations and biases <a class="yt-timestamp" data-t="00:57:42">[00:57:42]</a>.
2.  **Physical Interaction:** The inability to perform virtual lab tests or hands-on exams creates "leakage," where patients need to seek in-person care, disrupting continuous virtual engagement <a class="yt-timestamp" data-t="00:59:36">[00:59:36]</a>. This also impacts patient loyalty to specific primary care physicians <a class="yt-timestamp" data-t="00:59:09">[00:59:09]</a>.
3.  **Business Models:** Large health systems lack incentive to transition to lower-cost virtual care channels, as it can lead to reduced reimbursement and capacity <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a>. Insurers are better positioned to deploy virtual primary care but often lack member engagement to do so effectively <a class="yt-timestamp" data-t="01:00:15">[01:00:15]</a>.

## Learning More

To learn more about Oscar Health's AI work and insights, visit hi.oscar.com <a class="yt-timestamp" data-t="01:01:50">[01:01:50]</a>. Mario Schaer also posts his explorations and Oscar's AI initiatives on Twitter @MarioTS <a class="yt-timestamp" data-t="01:02:07">[01:02:07]</a>. He is also exploring [[ai_applications_and_market_potential_across_various_industries | AI applications in gaming]], including generating RPGs from company documents and creating games that dynamically add mechanics using LLMs <a class="yt-timestamp" data-t="01:02:19">[01:02:19]</a>, <a class="yt-timestamp" data-t="01:03:13">[01:03:13]</a>.