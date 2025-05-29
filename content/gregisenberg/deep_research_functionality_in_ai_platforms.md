---
title: Deep research functionality in AI platforms
videoId: QVNjP6siwEU
---

From: [[gregisenberg]] <br/> 

Deep research functionality in AI platforms like OpenAI's ChatGPT and Perplexity allows for in-depth analysis of user queries, similar to a junior analyst performing extensive research [00:00:24]. This goes beyond quick answers, providing detailed insights into specific questions [00:00:31].

## Comparing OpenAI ChatGPT Deep Research vs. Perplexity Deep Research

An experiment was conducted to compare the deep research capabilities of OpenAI's ChatGPT Pro Plan ($200/month) and Perplexity's Deep Research ($20/month) [00:00:44]. The goal was to see which platform could generate better startup ideas, including tactics for building and growing a business to a target of $1 million in year one, $3 million in year two, and $5 million in year three [00:01:00].

The same prompt was given to both AIs:
"I want to create a startup. I want it to be an AI agent that focuses on a high-value niche. I want it to be defensible, not just a flash in the pan. I want you to create a zero-to-one playbook of how you'd launch it to get customers. Give me five ideas with five playbooks on how to grow it. I'm looking for $1 million year one, $3 million year two, $5 million year three." [00:01:20]

Additional clarifying questions were posed to ChatGPT Deep Research to refine the request, including:
*   No specific industry preference, looking for ideas with the highest likelihood of success [00:02:39].
*   Open to B2B or B2C targets [00:02:58].
*   No preference for AI application types (automation, data analysis), again focusing on the highest probability of success [00:03:06].
*   A preference for an MVP (Minimal Viable Product) cost of $5,000 or less, with the builder not being highly technical [00:03:30].
*   An interest in potentially raising VC money if the business could scale beyond $100 million ARR [00:04:05].
*   A lean towards viral self-serve growth for go-to-market, but open to other suggestions [00:04:25].

### Perplexity Deep Research Analysis

Perplexity Deep Research proved to be faster than ChatGPT, completing its analysis while ChatGPT was still processing [00:09:00]. It also leverages a greater number of sources, sometimes going through 29 or even 34 sources for its research [00:07:48]. One interesting finding was that Perplexity did not ask follow-up qualification questions like ChatGPT did initially [00:08:14].

#### Example Idea: Legal Contract Lifecycle AI Agent

Perplexity suggested an "AI Legal Contract Lifecycle Agent" [00:09:51].
*   **Problem Space:** Corporate legal teams spend 23% of their time manually reviewing boilerplate contracts and struggle with version control errors, costing enterprises $2.4 billion annually [00:10:00]. Existing solutions require extensive customization and fail to adapt to company-specific negotiation patterns [00:10:16].
*   **Defensible Solution:** An [[building_niche_ai_apps | AI agent]] that:
    *   Integrates with email, SharePoint, and DocuSign via API [00:10:30].
    *   Learns organizational risk thresholds through historical contract analysis [00:10:34].
    *   Auto-redlines third-party paper using firm-specific fallback positions [00:10:40].
    *   Maintains version lineage with blockchain-style audit trails (though this might be complex for an MVP) [00:10:46].
*   **Defensibility:** It develops institutional memory through continuous exposure to negotiation outcomes, embeds into legal department workflows (averaging 14.3 logins per week per user), and would require retraining equivalent to six to nine months of human experience to replace [00:11:29].
*   **Growth Playbook:**
    *   **Phase 1: Niche Validation (90 days):** Build a Chrome extension to record legal contract review sessions (with permission) to train the initial model. Offer free redline audits for 100 AmLaw 200 firms, targeting mid-market companies ($50-500 million revenue) [00:12:20].
    *   **Monetization:** $2,500/month subscription locked to specific document types [00:13:08].
    *   **Phase 2: Workflow Embedding (Months 4-9):** Integrate with legal ops platforms like Lexion and Entra. Launch a Clause Library Builder using clients' historical favored language. Implement usage-based pricing at $0.25 per review clause [00:13:25].
    *   **Phase 3: Enterprise Scaling (Months 10-12):** Add SOC 2 Type 2 compliance. Develop custom connectors for ServiceNow and Salesforce CPQ. Upsell to an $8,000/month Enterprise tier with custom playbooks [00:13:55].
*   **Financial Roadmap:**
    *   **Year 1:** 40 clients at $2,500/month = $1.2 million ARR [00:14:16].
    *   **Year 2:** 150 clients at $5,000/month plus $250k usage pay = $3.1 million ARR [00:14:24].
    *   **Year 3:** Platform fees from 300+ embedded instances = $5.4 million ARR [00:14:31].
*   **Follow-up Research:** When prompted to make the idea "non-obvious" and provide a step-by-step MVP plan under $5,000, Perplexity produced an executive summary of the legal AI startup space, competitive analysis, an "Opportunity Matrix," and a detailed MVP implementation plan with a $4,800 budget [00:31:48]. It provided a Chrome extension prototype using Manifest V3 and TensorFlow.js (zero development cost), legal team interviews, and phase two core feature builds with costs [00:32:53]. The go-to-market sequencing included offering free clause vulnerability audits and usage-based pricing [00:33:52].

> [!NOTE] Key takeaway for Perplexity: It is fast and provides valuable data points and structured breakdowns. While its initial output might be less verbose than ChatGPT, it can provide deep, specific details with further prompting, especially regarding implementation plans and cost estimates [00:37:32].

### ChatGPT Deep Research Analysis

ChatGPT Deep Research produced a much longer, more in-depth "business brief" [00:16:11].

#### Example Idea: AI Sales Outreach Assistant

ChatGPT suggested an "AI Sales Outreach Assistant" [00:15:55].
*   **Solution:** An [[utilizing_ai_for_scaling_and_automation | AI-powered sales outreach assistant]] that acts as a virtual Sales Development Representative (SDR), automating prospect research and personalized cold email/LinkedIn messages [00:16:27].
*   **Target Market:** B2B companies, from startups to mid-size firms, needing more pipeline without hiring extra SDRs [00:16:38]. The [[leveraging_ai_tools_for_product_design_and_market_analysis | AI agent]] enriches lead data and crafts tailored outreach at scale [00:16:45].
*   **Defensibility (Data Network Effect):** It learns from every interaction, identifying which messaging yields replies and building a unique dataset of what works in each industry [00:16:53]. This allows for superior personalization and lead scoring over time, which is hard for competitors to replicate [00:17:25]. Integration into CRMs and email systems further deepens the moat by embedding the AI into the sales team's workflow [00:17:34]. Demand for such tools is high, with 66% of sales reps saying AI helps them better understand customers and personalize outreach [00:17:42].
*   **Zero-to-One Playbook (MVP for $5,000 or less):**
    *   **Focus:** Narrow to a high-value use case, e.g., automating follow-up emails to warm leads with a templated but AI-personalized approach [00:18:05].
    *   **MVP:** A web app or Chrome extension where a salesperson inputs prospects or connects their CRM, and the AI generates and sends personalized emails [00:18:43].
    *   **Cheap Build:**
        *   Utilize existing AI APIs like OpenAI's GPT-4 for text generation, avoiding expensive model training [00:18:59].
        *   No-frills UI using low-code tools or templates [00:19:18].
        *   Single-channel focus (start with email) [00:19:30].
        *   Manual fallback: If AI is unsure, it flags for human review to ensure quality and gather data for improvement [00:19:38].
    *   **Cost:** Main cost is developer time and API calls, estimated to be less than $5,000 [00:19:51].
*   **Customer Acquisition and Growth:**
    *   **Product-Led Viral Adoption:** Offer a self-serve free tier (e.g., 50 AI-generated emails per month) for individual sales reps or small startups [00:20:34].
    *   **Viral Loop:** Prompt users to share success internally (e.g., "This meeting was set by AI") when the assistant books a meeting or gets a reply [00:21:04].
    *   **Referral Incentives:** As more reps use it, the AI performs better with shared data, creating a network effect [00:21:20].
    *   **Content Marketing:** Publish case studies and short demos (e.g., "How X startup tripled using AI") [00:21:27]. Links to relevant success stories like Jenny AI are provided [00:21:38].
    *   **CRM Marketplaces:** Presence on platforms like HubSpot for distribution [00:21:57].
    *   **Financial Goal:** Reach a few hundred paying teams in year one (e.g., 200 companies at $5,000/year = $1 million ARR) [00:22:07]. Growth to $3 million in year two comes from "land and expand" – converting free users and expanding usage among paid teams [00:22:21].
*   **Monetization and Pricing:**
    *   Per-seat or usage-based tiers (e.g., $100-$150/month per sales rep or by volume) [00:23:21].
    *   Typical structure: Basic plan ($49/month, solo rep, limited emails), Team plan ($199/month, five reps, more emails, CRM integration), Enterprise plan [00:23:36].
    *   Ideas for revenue optimization: premium upsells, annual deals, premium features, performance-based options [00:24:49].
*   **VC Readiness:** The idea is presented as having the potential to scale to $100 million ARR and may require VC funding to reach that level [00:25:13].

> [!NOTE] Key takeaway for ChatGPT: It provides incredibly detailed, structured reports that read like a full business plan. It’s excellent for getting a comprehensive overview and specific tactical advice in a single output, though it takes longer to process [00:37:44].

## Conclusion

Both Perplexity Deep Research and ChatGPT Deep Research offer powerful capabilities for [[efficient_market_research_using_ai_agents | efficient market research using AI agents]] and [[framework_for_developing_ai_saas_ideas | developing AI SaaS ideas]].

*   **Perplexity Deep Research** is notably faster and more concise, often presenting information in useful tables. It may require more specific follow-up prompts to achieve the same level of depth as ChatGPT, but some users might prefer this manual approach [00:27:27]. It can also be used for free for a limited number of deep research queries [00:27:02].
*   **ChatGPT Deep Research** provides extremely detailed and comprehensive reports, resembling a full business document. While it takes longer to generate responses, the output is rich in detail and often requires less immediate follow-up [00:26:04].

Both tools are considered "insanely good" and offer an "unfair advantage" for individuals looking to build startups or refine product ideas [00:31:31]. The choice between them often comes down to preferred workflow—whether one prefers faster, more concise outputs requiring additional prompting or longer, more exhaustive single outputs [00:37:58].