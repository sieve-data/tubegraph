---
title: AI in healthcare and insurance
videoId: VUBfFv-Un3c
---

From: [[redpointai]] <br/> 

Oscar Health, a $3 billion public health insurance company, has been at the forefront of innovating with technology in healthcare for the past decade <a class="yt-timestamp" data-t="00:00:23">[00:00:23]</a>. As both an insurer and a provider of care, Oscar Health is actively experimenting with models like GPT-4 across various healthcare use cases <a class="yt-timestamp" data-t="00:00:31">[00:00:31]</a>. Mario Scher, the CTO and co-founder of Oscar Health, offers insights into implementing these models for real use cases and the broader future of [[AI in healthcare and human interaction | AI in healthcare]] <a class="yt-timestamp" data-t="00:00:44">[00:00:44]</a>.

## Core Applications of AI in Healthcare

Large Language Models (LLMs) excel at translating between informal and formal language, which is highly relevant in healthcare <a class="yt-timestamp" data-t="00:01:40">[00:01:40]</a>. Healthcare involves highly formalized language (e.g., ICD-10, CPT codes, utilization management guidelines) alongside a wealth of human language (e.g., patient-provider conversations, electronic medical record notes) <a class="yt-timestamp" data-t="00:02:02">[00:02:02]</a>. While healthcare has seen less algorithmic coverage compared to other industries in the past 15 years, LLMs are now incredibly adept at bridging this gap <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Administrative Use Cases
Initially, many applications are found on the administrative side <a class="yt-timestamp" data-t="00:03:11">[00:03:11]</a>. For instance, LLMs can translate complex claim processing traces, which are full of formal rules, into understandable informal language for laypersons <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>. The goal for the next five years is to make administrative processes real-time, bidirectional, and more transparent, allowing patients to understand costs and alternatives instantly <a class="yt-timestamp" data-t="00:03:55">[00:03:55]</a>.

### Clinical Use Cases
The long-term vision includes using [[Transforming clinical processes with AI | AI]] to replace caregivers and machine intelligence with clinical intelligence, ultimately reducing the cost of doctor visits by factors of 10 or 100, and potentially replacing specialists <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. However, this runs into issues of hallucinations, safety, and biases in training data <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. Oscar Health's current focus is primarily on administrative use cases, with one clinical project underway, but with lower short-term expectations for breakthroughs <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.

## Oscar Health's AI Strategy and Use Cases

Oscar Health leverages [[Exploring use cases and challenges of AI in healthcare systems | AI]] across three main financial levers: growth and retention, operational efficiency (administrative), and medical cost reduction/outcome improvement (clinical) <a class="yt-timestamp" data-t="00:10:24">[00:10:24]</a>.

*   **Growth and Retention**:
    *   **Personalized Outreach**: AI is used to send personalized outbound campaigns to members, reminding them of positive experiences or preventative care actions taken (e.g., colon cancer screenings) <a class="yt-timestamp" data-t="00:13:39">[00:13:39]</a>.
    *   **Persona-Based Messaging**: Messaging is tailored based on member personas; chronically ill members respond better to empathy, while generally healthy members prefer convenience <a class="yt-timestamp" data-t="00:14:41">[00:14:41]</a>.
    *   **Demographic Inference**: LLMs can help fill missing demographic information (e.g., ethnicity from names or conversation language) to better match members with appropriate care or communication <a class="yt-timestamp" data-t="00:16:07">[00:16:07]</a>.

*   **Administrative Efficiency**:
    *   **Call Summarization**: LLMs are increasingly replacing manual note-taking by care guides during customer service calls <a class="yt-timestamp" data-t="00:17:26">[00:17:26]</a>.
    *   **Lab Test Summarization**: Used within Oscar's medical group <a class="yt-timestamp" data-t="00:17:41">[00:17:41]</a>.
    *   **Secure Messaging Medical Records Generation**: Also within the medical group <a class="yt-timestamp" data-t="00:17:46">[00:17:46]</a>.
    *   **Claims Explainers**: Providing internal care guides with clear explanations for claim statuses <a class="yt-timestamp" data-t="00:17:52">[00:17:52]</a>. These administrative automations yield savings measured in cents per member per month (PMPM) <a class="yt-timestamp" data-t="00:18:01">[00:18:01]</a>.

*   **Clinical Applications**:
    *   **Medical Record Interaction**: A key current use case is enabling doctors, customer service agents, or other Oscar personnel to "talk to" medical records <a class="yt-timestamp" data-t="00:18:51">[00:18:51]</a>.

## Challenges of AI Implementation in Healthcare

### Regulatory Hurdles
Healthcare is a highly regulated industry. HIPAA (Health Insurance Portability and Accountability Act) is the biggest constraint, requiring strict protection of patient-specific information <a class="yt-timestamp" data-t="00:20:56">[00:20:56]</a>. This means AI vendors must sign Business Associate Agreements (BAAs) <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. Oscar Health was reportedly the first organization to sign a BAA directly with OpenAI <a class="yt-timestamp" data-t="00:21:18">[00:21:18]</a>. New LLM models from providers like Google (e.g., Gemini Ultra) do not automatically fall under existing HIPAA agreements, requiring a waiting period (typically 3-4 months) before real medical data can be used <a class="yt-timestamp" data-t="00:22:30">[00:22:30]</a>. In the interim, synthetic or anonymized test data is used <a class="yt-timestamp" data-t="00:22:51">[00:22:51]</a>.

For companies looking to sell AI solutions to healthcare, strict security and policy reviews are standard <a class="yt-timestamp" data-t="00:23:58">[00:23:58]</a>. Certifications like "High Trust" can ease the process, but ultimately, building trust with hospitals is paramount <a class="yt-timestamp" data-t="00:24:23">[00:24:23]</a>.

### Data Cleanliness and Context
A significant challenge in clinical use cases is the lack of clean, complete inputs and outputs compared to administrative tasks <a class="yt-timestamp" data-t="00:06:43">[00:06:43]</a>. Human-written summaries often contain subtle contextual knowledge (e.g., a provider remembering a previous unrecorded conversation with a patient) that LLMs cannot access <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>. To improve LLM performance in these "wide open" clinical scenarios, it's crucial to improve the "horizon of knowledge" by feeding the LLM more context <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.

### LLM Limitations and Prompting Strategies
*   **Counting/Categorization**: LLMs like GPT-4 struggle with tasks that require both processing input tokens and simultaneously counting or categorizing them within the same prompt, especially with large datasets <a class="yt-timestamp" data-t="00:27:48">[00:27:48]</a>. This limitation, often called "running out of layers," can be addressed by breaking down tasks into multiple steps or using a "Chain of Thought" approach, effectively chaining LLMs together to expand the processing capacity <a class="yt-timestamp" data-t="00:29:52">[00:29:52]</a>.
*   **False Positives for Specific Concepts**: In medical record extraction, LLMs can generate high false positives for specific concepts like "post-traumatic injury" <a class="yt-timestamp" data-t="00:31:49">[00:31:49]</a>. This happens because the LLM's general training data includes broader, layperson associations of the term that differ from its strict medical definition within utilization management <a class="yt-timestamp" data-t="00:32:40">[00:32:40]</a>. A solution involves using "self-consistency questionnaires" where the LLM first generates multiple ways a concept might appear in records, then evaluates them independently before synthesizing a final answer <a class="yt-timestamp" data-t="00:33:41">[00:33:41]</a>.
*   **Context Window Issues**: Early in AI development, LLMs had limited context windows, preventing large claim traces (e.g., 1,000 lines of logic) from fitting in a single prompt <a class="yt-timestamp" data-t="00:37:09">[00:37:09]</a>. Even with larger windows, LLMs struggled with the complexity of long decision trees <a class="yt-timestamp" data-t="00:37:32">[00:37:32]</a>. The solution was to provide hierarchical prompts, giving a high-level trace and allowing the LLM to "double-click" on specific functions for more detail <a class="yt-timestamp" data-t="00:38:25">[00:38:25]</a>.

### Trust and Enterprise Sales
Health systems and insurance companies are generally slow at rapid prototyping and follow-up <a class="yt-timestamp" data-t="00:25:01">[00:25:01]</a>. In health tech, the "best products" do not always win; rather, the "best enterprise sales processes" often prevail <a class="yt-timestamp" data-t="00:25:29">[00:25:29]</a>. Founders are advised to spend more time engaging with potential clients to build trust rather than solely focusing on model tweaking <a class="yt-timestamp" data-t="00:25:39">[00:25:39]</a>.

## Future of AI in Healthcare

### General Purpose vs. Specialized Models
Oscar Health has consistently found that specializing a general-purpose model in a particular area often leads to a loss of "alignment," meaning the model struggles to follow instructions (e.g., outputting JSON) <a class="yt-timestamp" data-t="00:43:40">[00:43:40]</a>. The preference is to use the largest general-purpose models for better reasoning capabilities, potentially combined with techniques like Retrieval-Augmented Generation (RAG) and fine-tuning <a class="yt-timestamp" data-t="00:45:09">[00:45:09]</a>. Recent research suggests RAG and fine-tuning provide independent improvements in performance, making it beneficial to use both <a class="yt-timestamp" data-t="00:45:16">[00:45:16]</a>.

### AI Doctor/Clinical Chatbots
While there's no inherent reason why AI shouldn't eventually take on the role of a "doctor" given the algorithmic nature of medical knowledge <a class="yt-timestamp" data-t="00:56:59">[00:56:59]</a>, several practical issues remain:
1.  **Safety**: Direct LLM interaction with end-users in clinical settings is currently very difficult due to safety concerns <a class="yt-timestamp" data-t="00:57:44">[00:57:44]</a>. A human-in-the-loop is currently required for sensitive use cases <a class="yt-timestamp" data-t="00:50:58">[00:50:58]</a>.
2.  **Physical Interaction**: A significant portion of medical care (e.g., foot exams for diabetics, lab tests) requires in-person interaction, leading to "leakage" from virtual care systems <a class="yt-timestamp" data-t="00:57:52">[00:57:52]</a>.
3.  **Business Model**: Health systems currently have little incentive to switch to lower-cost virtual care channels, as this could reduce reimbursement <a class="yt-timestamp" data-t="00:59:50">[00:59:50]</a>. Insurers are better positioned to deploy automated virtual primary care but lack member engagement <a class="yt-timestamp" data-t="01:00:15">[01:00:15]</a>.

#### Overhyped/Underhyped in Healthcare AI
*   **Overhyped**: Clinical chatbots generally <a class="yt-timestamp" data-t="01:00:49">[01:00:49]</a>.
*   **Underhyped**: Voice outputs, especially for non-clinical applications <a class="yt-timestamp" data-t="01:00:56">[01:00:56]</a>.

### Commercial Opportunities
*   **Niche Regulatory Filings**: Generating regulatory documentation and reports using LLMs could be a significant opportunity <a class="yt-timestamp" data-t="00:53:30">[00:53:30]</a>.
*   **Fraud, Waste, and Abuse (FWA)**: This industry is still dominated by older players, presenting an opportunity for AI-driven disruption <a class="yt-timestamp" data-t="01:00:52">[01:00:52]</a>.
*   **Prior Authorization**: While many companies are focusing on [[Transforming clinical processes with AI | AI]] for prior authorization, it's a "neuralgic" function very close to an insurer's core competency <a class="yt-timestamp" data-t="00:55:00">[00:55:00]</a>.

## Structuring AI Teams at Oscar Health

Oscar Health has adopted a decentralized yet supported approach to AI development <a class="yt-timestamp" data-t="00:46:20">[00:46:20]</a>:
*   **Hackathons**: Quarterly hackathons serve as a catalyst for experimentation and sharing, with the first AI-focused hackathon seeing the highest participation <a class="yt-timestamp" data-t="00:46:37">[00:46:37]</a>.
*   **AI Pod**: A dedicated seven-person "AI Pod" consisting of product managers, data scientists, and engineers <a class="yt-timestamp" data-t="00:47:10">[00:47:10]</a>. This pod has:
    *   Weekly office hours for any employee to get help with prompts or AI-related questions <a class="yt-timestamp" data-t="00:47:22">[00:47:22]</a>.
    *   Three core projects that the pod itself needs to complete <a class="yt-timestamp" data-t="00:47:34">[00:47:34]</a>.
    *   Weekly "hacking sessions" to encourage open sharing of ideas and prototypes, whether successful or not <a class="yt-timestamp" data-t="00:47:54">[00:47:54]</a>.
*   **Transparency**: Oscar Health actively publishes its research and insights on its `ai.hioscar.com` website to foster open learning and sharing within the industry <a class="yt-timestamp" data-t="01:01:50">[01:01:50]</a>.

## Desired Tooling and Vision

Key tooling needs include:
*   **Safety Layer**: A mechanism to verify if LLM outputs are insulting or inappropriate before reaching end-users <a class="yt-timestamp" data-t="00:50:44">[00:50:44]</a>. Currently, this relies on a human-in-the-loop <a class="yt-timestamp" data-t="00:50:58">[00:50:58]</a>.
*   **Faster Inference Times**: Enabling rapid parallel generation of multiple outputs, allowing selection of the best one <a class="yt-timestamp" data-t="00:51:27">[00:51:27]</a>.

Mario Scher envisions [[AI and education technology | AI]] democratizing analytics within organizations, enabling more people to interact with models like GPT-4 <a class="yt-timestamp" data-t="00:26:39">[00:26:39]</a>. Beyond healthcare, he is interested in using LLMs for creative applications, such as generating regulatory reports, creating internal company RPGs (role-playing games) based on company documents, or developing dynamic game mechanics that balance economies <a class="yt-timestamp" data-t="01:02:19">[01:02:19]</a>.