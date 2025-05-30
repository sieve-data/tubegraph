---
title: Use and evaluation of large language models LLMs
videoId: jGlSC4t7XvU
---

From: [[redpointai]] <br/> 

## Grammarly's Evolution with LLMs

Grammarly, a personalized [[building_and_utilizing_large_language_models | AI productivity tooling]] assistant app for writing, has been building AI solutions for 15 years, launching in 2009 <a class="yt-timestamp" data-t="04:13:00">[04:13:00]</a>. The company has ridden multiple technology waves, starting primarily with rules-based [[understanding_language_models | Natural Language Processing]] (NLP) <a class="yt-timestamp" data-t="04:23:00">[04:23:00]</a>, moving to [[building_and_utilizing_large_language_models | deep learning models]] <a class="yt-timestamp" data-t="04:27:00">[04:27:00]</a>, and now extensively utilizing [[building_and_utilizing_large_language_models | LLMs]] and [[building_and_utilizing_large_language_models | GenAI]] <a class="yt-timestamp" data-t="04:28:00">[04:28:00]</a>. The approach is to identify user problems and then apply the best available technology to solve them effectively <a class="yt-timestamp" data-t="04:32:00">[04:32:00]</a>.

The emergence of ChatGPT was a "watershed moment" for Grammarly, surprising them with its speed, scale, and pace of quality improvement <a class="yt-timestamp" data-t="15:55:00">[15:55:00]</a>. While earlier NLP-based systems had greater precision compared to initial [[building_and_utilizing_large_language_models | LLM]] outputs that frequently hallucinated, the quality improvements in LLMs over the last couple of years have been phenomenal, with these models now essentially as good as rule-based systems for grammar <a class="yt-timestamp" data-t="17:35:00">[17:35:00]</a>. Grammarly views [[building_and_utilizing_large_language_models | LLMs]] as a "huge enabler" for its mission, allowing them to provide better, deeper, and more meaningful solutions to long-standing user problems <a class="yt-timestamp" data-t="16:32:00">[16:32:00]</a>.

## Expanding Communication Capabilities with LLMs

Grammarly envisions the communication lifecycle in four stages:
1.  **Ideation and Conceptualization:** Thinking about what to say <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>.
2.  **Composition:** Writing down the message <a class="yt-timestamp" data-t="05:01:00">[05:01:00]</a>.
3.  **Revision and Polishing:** Making the text better <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
4.  **Comprehension:** The recipient understanding the message <a class="yt-timestamp" data-t="05:08:00">[05:08:00]</a>.

Historically, Grammarly focused on the revision phase, helping with correctness, style guides, tone, and brevity <a class="yt-timestamp" data-t="05:23:00">[05:23:00]</a>. [[building_and_utilizing_large_language_models | LLMs]] enable Grammarly to "turbocharge" the value provided to users in two main ways:
*   **Strategic Suggestions:** Tying communication to business outcomes by offering suggestions aligned with desired goals (e.g., adding free food details to an event email to drum up enthusiasm, or clarifying a call to action in a board email) <a class="yt-timestamp" data-t="06:00:00">[06:00:00]</a>. Basic mechanics like correctness and tone can be auto-applied <a class="yt-timestamp" data-t="07:08:00">[07:08:00]</a>.
*   **Full Communication Lifecycle Support:** Moving beyond just revision to assist with ideation, composition, and comprehension (e.g., summarizing long email threads and identifying action items) <a class="yt-timestamp" data-t="07:22:00">[07:22:00]</a>.

Looking ahead, future [[building_and_utilizing_large_language_models | LLMs]] are expected to be more capable of [[the_rise_of_multimodal_models_and_their_implications | multi-step reasoning]] <a class="yt-timestamp" data-t="21:25:00">[21:25:00]</a>, which will enable [[lang_chain_as_a_framework_for_ai_development | agentic workflows]] <a class="yt-timestamp" data-t="21:28:00">[21:28:00]</a>. This means Grammarly could orchestrate complex, multi-step communication flows by pulling in context from various sources and even proposing the best steps to achieve a communication goal, reducing "drudgery" and enabling "flow state" <a class="yt-timestamp" data-t="21:33:00">[21:33:00]</a>.

## Challenges and Evaluation Strategies

A significant challenge in deploying [[building_and_utilizing_large_language_models | LLMs]] is ensuring quality and safety, especially given the "high stakes nature of human communication" <a class="yt-timestamp" data-t="08:38:00">[08:38:00]</a>. False positives, sensitive text issues, or safety concerns can have real consequences <a class="yt-timestamp" data-t="08:45:00">[08:45:00]</a>. Therefore, Grammarly does extensive work to [[building_and_utilizing_large_language_models | fine-tune]] models for specific use cases and conducts rigorous [[challenges_and_strategies_in_ai_model_evaluation | quality evals]] and [[challenges_and_strategies_in_ai_model_evaluation | safety evals]] before shipping models to users <a class="yt-timestamp" data-t="08:56:00">[08:56:00]</a>.

### Evaluation Methods
Grammarly employs a multi-dimensional process for evaluating [[building_and_utilizing_large_language_models | LLMs]]:
*   **External Benchmarks:** Looking at general-purpose benchmarks closest to their use cases for objective external measurements <a class="yt-timestamp" data-t="28:59:00">[28:59:00]</a>.
*   **Safety Evals:** Running internal safety evaluations based on extensive user feedback and understanding of guardrails around sensitive content <a class="yt-timestamp" data-t="29:11:00">[29:11:00]</a>. This provides a "powerful" [[challenges_and_strategies_in_ai_model_evaluation | eval]] data set from real-world scenarios <a class="yt-timestamp" data-t="29:30:00">[29:30:00]</a>.
*   **Side-by-Side Comparisons:** Linguistic experts rate [[building_and_utilizing_large_language_models | LLM]] output against human-curated output to determine preferences <a class="yt-timestamp" data-t="29:36:00">[29:36:00]</a>.
*   **User Feedback and Engagement:** Tracking how users accept or reject suggestions and engage with features provides continuous quality input <a class="yt-timestamp" data-t="10:02:00">[10:02:00]</a>. Experiments are run with small user percentages to gauge real-world performance <a class="yt-timestamp" data-t="10:21:00">[10:21:00]</a>. This feedback loop is crucial, as features that pass internal evaluations might not resonate with users in practice <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>.
    *   *Example:* The tone detector feature, while popular, revealed unexpected edge cases where tone suggestions were inappropriate, such as for police reports of serious crimes <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.

## Tailoring and Optimizing LLMs

Grammarly uses a combination of [[open_source_vs_closed_source_large_language_models | closed source]] and [[open_source_vs_closed_source_large_language_models | open source]] models in production, often [[building_and_utilizing_large_language_models | fine-tuned]] on their vast user data <a class="yt-timestamp" data-t="24:08:00">[24:08:00]</a>. The company processes 75 billion user events daily, providing a unique advantage in fine-tuning and personalizing models for different use cases <a class="yt-timestamp" data-t="26:01:00">[26:01:00]</a>.

The goal is not to use the smallest possible model, but the most [[building_and_utilizing_large_language_models | efficient model]] without compromising quality or fidelity <a class="yt-timestamp" data-t="24:44:00">[24:44:00]</a>. Cost and latency are key considerations; low latency enhances user experience and "flow state" <a class="yt-timestamp" data-t="25:11:00">[25:11:00]</a>.

Grammarly tailors its product in several ways:
*   **Personalization:** Allowing individual users to define and refine their unique voice <a class="yt-timestamp" data-t="26:37:00">[26:37:00]</a>.
*   **Organizational Customization:** Ingesting organization-specific knowledge like style guides, brand tones, and corporate values to ensure consistent and compliant communication across the organization and with customers <a class="yt-timestamp" data-t="26:54:00">[26:54:00]</a>. This helps automate the application of rules that might otherwise be found in large, manual documents <a class="yt-timestamp" data-t="27:51:00">[27:51:00]</a>.

The models are [[building_and_utilizing_large_language_models | fine-tuned]] on use cases, and organizational-specific knowledge is ingested separately to apply rules and guidelines in the flow of communication <a class="yt-timestamp" data-t="27:37:00">[27:37:00]</a>.

## LLMs in Enterprise and Education

### Enterprise Adoption
The [[impact_of_large_language_models_on_business_operations | Enterprise AI Market]] is seen as a "transformation journey" rather than a one-time deployment <a class="yt-timestamp" data-t="36:17:00">[36:17:00]</a>. Enterprises need to select trusted partners for this multi-year transformation <a class="yt-timestamp" data-t="36:52:00">[36:52:00]</a>. While there's much excitement and investment, measurable productivity gains from AI are still "elusive" outside of a few core use cases like software engineering and code generation <a class="yt-timestamp" data-t="37:23:00">[37:23:00]</a>. Grammarly emphasizes demonstrating measurable value; for instance, the average Grammarly user in an organization saves 19 days per year <a class="yt-timestamp" data-t="38:03:00">[38:03:00]</a>.

### Education Sector
The education sector faces the challenge of responsibly incorporating powerful new [[building_and_utilizing_large_language_models | AI tools]] into classrooms and pedagogical methods <a class="yt-timestamp" data-t="39:51:00">[39:51:00]</a>. The initial impulse to ban AI has largely dissipated, replaced by an eagerness to engage and equip graduates with essential AI skills for the workforce <a class="yt-timestamp" data-t="40:53:00">[40:53:00]</a>.

Grammarly supports responsible AI use in education through features like:
*   **Citing AI Use:** Allows students to cite how they used AI in their work, differentiating between using AI for full content generation (e.g., writing an essay) versus using it as a co-pilot for feedback and refinement <a class="yt-timestamp" data-t="41:18:00">[41:18:00]</a>. This promotes deeper engagement and learning <a class="yt-timestamp" data-t="42:01:00">[42:01:00]</a>.
*   **Authorship Detection:** A feature that identifies the provenance of every piece of content in a document, distinguishing between manually written, cut-and-pasted, or AI-generated sections <a class="yt-timestamp" data-t="42:27:00">[42:27:00]</a>. This provides transparency and tools for educators to build guardrails around AI use <a class="yt-timestamp" data-t="43:04:00">[43:04:00]</a>.

Ultimately, AI in education should serve as a "tool to give us superpowers" and "augment" human capabilities, not displace them <a class="yt-timestamp" data-t="44:24:00">[44:24:00]</a>. AI also acts as a "great leveler" and "democratizer of skills," providing educational support to those who may not otherwise have access <a class="yt-timestamp" data-t="44:48:00">[44:48:00]</a>.

## Future Outlook

Grammarly currently utilizes about "half a dozen or so" [[building_and_utilizing_large_language_models | LLMs]] in production, a combination of [[open_source_vs_closed_source_large_language_models | closed source]] and [[open_source_vs_closed_source_large_language_models | open source]] models, mostly [[building_and_utilizing_large_language_models | fine-tuned]] <a class="yt-timestamp" data-t="24:08:00">[24:08:00]</a>. While current models are "idiosyncratic" and require significant work to adapt for specific use cases <a class="yt-timestamp" data-t="23:17:00">[23:17:00]</a>, the increasing efficiency gains mean that a lot of inference could move [[the_role_of_specialized_models_in_speech_recognition | on device]] in the near future <a class="yt-timestamp" data-t="19:34:00">[19:34:00]</a>. This shift to [[the_role_of_specialized_models_in_speech_recognition | on-device]] processing offers benefits in security, privacy, latency, and user experience <a class="yt-timestamp" data-t="20:01:00">[20:01:00]</a>.

The general consensus is that [[building_and_utilizing_large_language_models | AI]] is "overhyped in the short term and underhyped in the long term" <a class="yt-timestamp" data-t="14:50:00">[14:50:00]</a>. While transformative, simply "sticking AI into everything" without clear goals is not an effective way to solve user problems <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>. For the broader [[impact_of_large_language_models_on_business_operations | Enterprise]] market, AI is expected to profoundly transform work <a class="yt-timestamp" data-t="36:03:00">[36:03:00]</a>.

One underhyped aspect of AI is its potential to "upskill and uplevel people around the world," serving as a powerful "democratizer of skills" and a "force multiplier" in the workforce <a class="yt-timestamp" data-t="46:52:00">[46:52:00]</a>. This is particularly impactful for those who may lack access to traditional educational resources or professional development opportunities <a class="yt-timestamp" data-t="47:05:00">[47:05:00]</a>.