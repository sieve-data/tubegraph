---
title: Implementing AI in healthcare systems
videoId: VUBfFv-Un3c
---

From: [[redpointai]] <br/> 

Oscar Health, a $3 billion public health insurance company, has been at the forefront of innovating with technology in healthcare for the past decade, including the application of AI and large language models (LLMs) [00:00:18]. The company serves as both an insurer and a care provider, experimenting with advanced models like GPT-4 in numerous healthcare contexts [00:00:31]. Oscar Health was notably among the first organizations to secure regulatory approval from OpenAI to use its models in healthcare [00:00:38].

## The Transformative Potential of AI in Healthcare

AI, particularly LLMs, excels at translating between informal and formal language, which is highly relevant in healthcare due to its unique blend of structured codes (e.g., ICD-10, CPT codes) and human-centric conversations between providers and patients [00:01:40]. Historically, healthcare has seen relatively less algorithmic coverage compared to other industries [00:02:26]. LLMs bridge this gap by seamlessly moving between formal, regulated medical language and everyday human communication [00:02:55].

### Administrative Use Cases
Initially, many AI applications in healthcare, especially for insurers like Oscar, are focused on the [[Administrative and clinical use cases of AI in health insurance | administrative side]] [00:03:09]. These applications aim to make complex processes like claims payment more transparent and efficient [00:03:15]:

*   **Claims Processing**: LLMs can translate detailed rule-based claim traces (e.g., which rules were applied, which failed) into understandable explanations for non-experts [00:03:30]. This facilitates real-time, bidirectional transparency in the claims process [00:03:51].
*   **Cost Transparency**: The goal is to create a healthcare system where patients immediately know the cost of a service or potential alternatives before receiving care [00:04:06].
*   **Operational Efficiency**: Automating administrative tasks can lead to significant cost savings; even small improvements on the 15% administrative overhead of insurance companies can notably impact margins [00:11:52].

### Clinical Use Cases
The long-term vision for AI in healthcare involves reducing the cost of doctor visits and potentially replacing specialists with AI [00:04:30]. However, this area faces significant [[Challenges in virtual healthcare and AI doctors | challenges]] related to hallucinations, safety, bias, and the need to improve the "horizon of knowledge" for LLMs [00:04:49]. For instance, Oscar Health sequences its AI projects with a current focus on three administrative use cases and one clinical use case, with higher immediate expectations for administrative breakthroughs [00:05:06].

## Financial Drivers for AI Adoption in Insurance

Oscar Health's financial outcomes are driven by three main levers [00:10:24]:

1.  **Growth and Retention**: AI helps retain members by personalizing outbound campaigns during the annual re-enrollment period [00:13:01]. For example, reminding members about preventative screenings like colorectal cancer screenings has been effective, especially with specific demographics like Asian-Americans [00:14:05]. Messaging can be tailored based on member personas; chronically ill members respond better to convenience messaging, while generally healthy members respond better to empathy [00:14:40]. LLMs can extract personas and issues from customer service conversations to inform these personalized messages [00:15:51]. They can also infer demographic information (e.g., ethnicity, language spoken) from names or conversation context to improve matching members with appropriate doctors [00:16:33]. This represents a form of [[Proactive AI interventions | proactive AI intervention]].
2.  **Operational Efficiency**: Automating internal processes to reduce administrative overhead [00:11:46].
3.  **Medical Cost Reduction and Outcome Improvement**: Addressing the 85% of costs that constitute medical expenses has the most significant potential for improving margins [00:12:26].

## Implementation and Regulatory Challenges in Healthcare AI

Implementing AI in healthcare is complex due to strict regulations, most notably HIPAA (Health Insurance Portability and Accountability Act) [00:19:05]. HIPAA mandates that patient-specific information cannot be shared without proper agreements, specifically Business Associate Agreements (BAAs) [00:20:58]. Oscar Health was among the first organizations to sign a BAA directly with OpenAI [00:21:17].

Key considerations and challenges include:

*   **BAA Compliance**: AI model providers (like Google, OpenAI) typically roll out BAA coverage for their latest models a few months after general release [00:22:30]. This requires healthcare organizations to use anonymized or synthetic test data for initial model evaluation until BAA compliance is secured [00:22:46].
*   **Data Cleanliness and Context**: [[Challenges in virtual healthcare and AI doctors | Clinical use cases]] often involve less clean inputs and outputs compared to administrative ones [00:06:43]. Human providers leverage subtle contextual knowledge (e.g., prior conversations, local conditions like weather or public transport) that LLMs cannot access unless explicitly provided [00:07:11]. This means improving LLM performance in clinical settings requires not just model improvement but also enhancing the LLM's "horizon of knowledge" [00:08:02].
*   [[Enterprise adoption of AI agents | Enterprise Adoption]]**: Healthcare systems and insurance companies are generally slow at rapidly prototyping and following up on new technologies [00:24:55]. Success often depends more on effective enterprise sales processes and building trust with institutions than solely on product quality [00:25:29]. A consortium of health systems and insurers, including Oscar, developed principles for AI in healthcare that emphasize AI's potential to [[Cost efficiency and accessibility in AI technologies | democratize analytics]] and encourage wider adoption [00:26:03]. [[Challenges and strategies in AI deployment | This points to a need for a collaborative approach to foster broader AI adoption]].

## Real-World AI Applications at Oscar Health

Oscar Health has several working AI applications [00:09:53]:

*   **Customer Service Call Summarization**: Increasingly phasing out manual note-taking by care guides, letting LLMs automatically summarize calls [00:17:20].
*   **Lab Test Summarization**: Launched within the Oscar Medical Group [00:17:41].
*   **Secure Messaging and Medical Record Generation**: Used within the Oscar Medical Group for generating medical records from secure messages [00:17:46].
*   **Claims Explainers**: Providing internal care guides with AI-generated explanations of claim denials to better communicate with members [00:17:52].
*   **"Talking to the Medical Records"**: Allowing doctors and other internal staff to query and understand medical records using natural language [00:18:52]. This is an example of [[The role of AI in enhancing patientprovider communication | AI enhancing provider-internal communication]].

These administrative use cases currently save Oscar "a few cents PMPM" (per member per month), accumulating to meaningful savings when scaled [00:17:58].

## Navigating LLM Limitations and Building Robust Systems

Oscar Health has encountered specific [[Compound AI systems and their development | LLM limitations]], particularly with tasks requiring aggregation or deep contextual understanding within formal systems [00:27:28]:

*   **Counting and Aggregation**: LLMs struggle with accurately counting or categorizing multiple items within a single context window, such as summarizing and tallying reasons from numerous customer service calls [00:27:51]. This often requires breaking down tasks into multiple steps or "chain of thought" prompting [00:29:51].
*   **Context Window Limitations**: Early models had smaller context windows (e.g., 8,000 tokens), making it impossible to feed entire, verbose internal traces (like 1,000 lines of logic for a single claim) [00:37:09]. Even with larger context windows, providing the right level of abstraction is crucial [00:37:25].
*   **Ambiguous Medical Concepts**: LLMs can misinterpret medical concepts (e.g., "post-traumatic injury") when the definition in general training data differs from a specific, formalized clinical context (e.g., utilization management criteria) [00:31:01]. A strategy to mitigate this involves having the LLM create a "self-consistency questionnaire" by prompting it to list various ways a concept might appear in medical records, then using these generated examples to refine the evaluation [00:33:41]. This essentially involves breaking down complex questions into sub-prompts and processing them independently [00:34:36].
*   **Claims Assistant Product**: This product aims to translate complex internal claim logic into intuitive explanations for end-users [00:35:40]. The challenge lies in providing the LLM with the right hierarchical level of information from the claim system's trace, focusing on key decision points rather than every sub-procedure call [00:38:20]. This strategy involves an iterative process where the LLM can "double-click" on specific functions for more detail [00:38:46].

Oscar's approach to prompting strategies often relies more on iterative experimentation and system design (how to chain models together) rather than solely on academic literature [00:39:48].

## General vs. Specialized AI Models

Oscar Health currently prefers general-purpose models like GPT-4 over specialized healthcare models (e.g., Google's Med-PaLM) for many use cases [00:43:06]. The primary reason is that specialized models tend to "lose alignments," meaning they are less consistent at following instructions, especially for formalized outputs like JSON [00:44:10]. The belief is that a larger general-purpose model provides better reasoning capabilities, and that until symbolic processing (planning) can be decoupled from content generation, bigger general models remain superior [00:44:41]. Combining retrieval-augmented generation (RAG) with fine-tuning offers independent performance improvements [00:45:11].

## Structuring AI Teams at Oscar Health

Oscar Health has a dedicated "AI Pod" consisting of product managers, data scientists, and engineers [00:47:10]. This centralized team facilitates knowledge sharing, offers office hours for consultation on prompts and strategies, and has its own set of three priority projects to ensure practical application [00:47:22]. They also host weekly "hacking sessions" where any employee can showcase AI experiments, fostering a culture of experimentation and lowering the barrier to entry for AI exploration [00:47:54]. [[Implementing AI at the district level | This model encourages decentralized innovation while providing centralized support and knowledge sharing]].

## The Future of Healthcare AI

### Overhyped vs. Underhyped

*   **Overhyped**: Clinical chatbots, generally [01:00:49].
*   **Underhyped**: Voice outputs [01:00:52].

### Challenges for AI Doctors and Virtual Healthcare
The concept of an "AI doctor" or fully automated virtual healthcare faces several significant hurdles [00:56:59]:

1.  **Safety and Direct Patient Interaction**: Direct LLM-to-patient interaction is still very difficult due to safety concerns and regulatory requirements [00:57:42].
2.  **Physical vs. Virtual Interactions**: While approximately two-thirds of claims *could* be handled virtually, this doesn't equate to two-thirds of *people* [00:58:16]. Many chronic conditions require in-person examinations or lab tests (e.g., diabetic foot exams), creating "leakage" where patients must transition from virtual to physical care, disrupting continuity [00:58:26]. Patient loyalty to specific PCPs is also surprisingly low, further complicating consistent virtual care [00:59:02]. These are key [[Challenges in virtual healthcare and AI doctors | challenges in virtual healthcare]].
3.  **Business Models and Incentives**: Current healthcare business models often disincentivize health systems from adopting lower-cost virtual care channels, as it can lead to reduced reimbursement rates and capacity [00:59:50]. Insurers are better positioned to deploy automated virtual primary care but often lack member engagement to do so effectively [01:00:15]. These [[Challenges in virtual healthcare and AI doctors | business model challenges]] need to be addressed to realize the full potential of AI.

### Promising Areas for AI in Healthcare
Beyond existing applications, opportunities exist in:

*   **Obscure Niches**: Targeting very specific, non-technical issues within healthcare, such as regulatory filings composition [00:53:22]. This could involve LLMs watching data flows and automatically generating regulatory reports for health regulators, NCQA, or state health departments [00:54:11].
*   **Fraud, Waste, and Abuse (FWA)**: This is an industry dominated by older players, and AI could offer more cost-effective solutions [01:01:16].

### Less Promising Areas for AI in Healthcare
*   **Prior Authorization (PA) Companies**: While seemingly ripe for AI, this area is considered very close to the core competency of insurance companies [00:55:00]. External companies trying to take over PA risk a "low ceiling" on their potential, as insurers may prefer to develop these capabilities internally [00:55:54].

### Future AI Explorations
Mario Schaer is interested in exploring AI applications in gaming, such as creating RPGs based on company internal documents for new employee onboarding or developing games that dynamically generate new mechanics and maintain economic balance as they are played [01:02:19].