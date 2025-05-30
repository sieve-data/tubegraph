---
title: Cost optimization vs exploration in AI
videoId: fi4-kSuaw40
---

From: [[redpointai]] <br/> 

Intercom, a company deeply rooted in customer support, provides a unique perspective on navigating the rapidly evolving landscape of AI, balancing initial [[Exploration and Experimentation in AI | exploration]] with eventual [[Cost optimization and economic considerations for AI model deployment | cost optimization]]. Dez Trainer, co-founder and Chief Strategy Officer of Intercom, shared insights into their journey, highlighting the strategic decisions made since the launch of ChatGPT <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

## Intercom's Immediate AI Shift

Upon ChatGPT's release, Intercom recognized customer support as a "kill zone" for AI due to large language models' inherent conversational, fact-finding, and summarization capabilities <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>. The company swiftly decided to "rip up the entire AI/ML roadmap" to go "all in" on this new technology, shipping their first AI product before Christmas and launching "Finn" in March <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a><a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>.

Their initial strategy involved launching "zero downside" AI features into their inbox, such as conversation summarization, message translation, and text expansion/collapse <a class="yt-timestamp" data-t="00:03:39">[00:03:39]</a><a class="yt-timestamp" data-t="00:03:52">[00:03:52]</a>. These features were designed so that if users didn't find them useful, they simply wouldn't click the button <a class="yt-timestamp" data-t="00:04:40">[00:04:40]</a>.

### Early Cost Realizations

This initial [[Exploration and Experimentation in AI | exploration]] quickly brought [[Cost optimization and economic considerations for AI model deployment | cost considerations]] to the forefront <a class="yt-timestamp" data-t="00:04:53">[00:04:53]</a>. With Intercom handling 500 million conversations monthly, automatically summarizing all of them would have been prohibitively expensive, potentially bankrupting the company <a class="yt-timestamp" data-t="00:04:56">[00:04:56]</a><a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>. This immediately made them realize that certain features, while desirable, were not yet affordable by default <a class="yt-timestamp" data-t="00:10:44">[00:10:44]</a>.

## Current Stance: Deep Exploration Over Cost Optimization

Despite these early cost insights, Intercom remains in a "deep [[Exploration and Experimentation in AI | exploration]] mode" <a class="yt-timestamp" data-t="00:11:03">[00:11:03]</a>. The primary reason is the abundance of opportunities to embed AI across their product, from reporting and human agent augmentation to messaging <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.

While acknowledging that some calls could be moved from more expensive models like GPT-4 to cheaper ones like GPT-3.5 or even open-source models like Llama, this isn't their immediate focus <a class="yt-timestamp" data-t="00:11:12">[00:11:12]</a>. Their strategy prioritizes building the "best possible product" first, assuming that technology will generally become cheaper and faster over time <a class="yt-timestamp" data-t="00:13:53">[00:13:53]</a><a class="yt-timestamp" data-t="00:14:43">[00:14:43]</a>.

### Latency as a Forcing Function

For Intercom, latency is a more pressing concern than raw cost. The current feel of AI interactions can be like "modem internet days," and improving speed is a top priority <a class="yt-timestamp" data-t="00:12:27">[00:12:27]</a><a class="yt-timestamp" data-t="00:13:20">[00:13:20]</a>. The expectation is that AI, especially with on-device models from companies like Apple and Google, will become instantaneous <a class="yt-timestamp" data-t="00:12:44">[00:12:44]</a><a class="yt-timestamp" data-t="00:12:55">[00:12:55]</a>.

## When to Shift to Cost Optimization

Intercom anticipates a shift towards [[Cost optimization and economic considerations for AI model deployment | cost optimization]] and refining existing solutions once the underlying AI models begin to "plateau," meaning incremental improvements become less significant (e.g., GPT-7 is only marginally better than GPT-6) <a class="yt-timestamp" data-t="00:15:12">[00:15:12]</a>. This is when it will make sense to optimize what they have rather than constantly reimagining the solution <a class="yt-timestamp" data-t="00:15:22">[00:15:22]</a>.

## Challenges and Future of AI Adoption

### The "Portfolio of Bets" Approach

Developing with AI involves a unique challenge: the uncertainty of whether a feature is even possible <a class="yt-timestamp" data-t="00:23:05">[00:23:05]</a>. Unlike traditional software, where uncertainty is largely in the design phase, AI projects can involve a "second wave" of uncertainty where the technical feasibility is unknown even after design <a class="yt-timestamp" data-t="00:23:01">[00:23:01]</a>. Therefore, AI development needs to be treated as a "portfolio of bets," with some having high probability (e.g., text expansion) and others being lower probability but high-impact (e.g., generating complex graphics) <a class="yt-timestamp" data-t="00:23:39">[00:23:39]</a><a class="yt-timestamp" data-t="00:23:51">[00:23:51]</a>.

### Phased Rollout and Customer Adoption

Intercom's approach to rolling out AI features to customers emphasizes a "crawl, walk, run" strategy, allowing clients to "dip their toe in" rather than a "trust fall" <a class="yt-timestamp" data-t="00:27:09">[00:27:09]</a>. They enable [[Experimenting and testing AI use cases | piloting]] features for specific user segments (e.g., free users, weekend support) to demonstrate value and build trust <a class="yt-timestamp" data-t="00:27:21">[00:27:21]</a>. This often leads to customers rapidly expanding AI usage once they see the benefits, sometimes even realizing their free users are getting better support than paid ones due to instant answers <a class="yt-timestamp" data-t="00:28:09">[00:28:09]</a><a class="yt-timestamp" data-t="00:28:11">[00:28:11]</a>.

The widespread adoption of AI by major consumer platforms like Apple and Google is expected to normalize the concept of "talking to software," making customers more accepting of AI-enriched applications <a class="yt-timestamp" data-t="00:30:29">[00:30:29]</a><a class="yt-timestamp" data-t="00:30:35">[00:30:35]</a>.

### Finetuning vs. RAG

Currently, Intercom's AI products, like Finn, primarily use Retrieval-Augmented Generation (RAG) rather than extensive [[Finetuning approaches and considerations in AI | finetuning]] per customer <a class="yt-timestamp" data-t="00:31:32">[00:31:32]</a>. While they do [[Finetuning approaches and considerations in AI | finetune]] for tone of voice, this is achieved through prompting <a class="yt-timestamp" data-t="00:31:37">[00:31:37]</a>. Finn naturally picks up the tone of voice by reading customer documentation and support conversations <a class="yt-timestamp" data-t="00:32:50">[00:32:50]</a>.

### Automation Levels and Future Capabilities

The percentage of requests handled by AI will vary significantly by industry vertical <a class="yt-timestamp" data-t="00:33:25">[00:33:25]</a>. Simple e-commerce queries might see 100% automation, while more complex products like Google Docs might only reach 80-90% due to diverse query types <a class="yt-timestamp" data-t="00:33:52">[00:33:52]</a><a class="yt-timestamp" data-t="00:34:06">[00:34:06]</a>.

A significant [[Future development areas for AI and efficiency optimizations | future development area]] for AI in customer support is enabling AI to take actions (e.g., issuing refunds, canceling orders) rather than just providing text answers <a class="yt-timestamp" data-t="00:35:08">[00:35:08]</a><a class="yt-timestamp" data-t="00:35:23">[00:35:23]</a>. This requires substantial software development, including authentication, monitoring, and data logging <a class="yt-timestamp" data-t="00:38:05">[00:38:05]</a>. Some customers will embrace full automation, while others may prefer a human oversight model, where AI proposes actions for a manager's approval <a class="yt-timestamp" data-t="00:35:58">[00:35:58]</a><a class="yt-timestamp" data-t="00:36:23">[00:36:23]</a>.

## Strategic Lessons for Companies

### For Startups

Startups entering the AI space should identify areas where the incumbent technology stack is largely irrelevant <a class="yt-timestamp" data-t="00:41:34">[00:41:34]</a>. This means finding product areas where, if rebuilt today, the entire system—features, UI, and underlying architecture—would be "entirely differently" designed because of AI capabilities <a class="yt-timestamp" data-t="00:41:46">[00:41:46]</a><a class="yt-timestamp" data-t="00:42:01">[00:42:01]</a>. An example of an entire product category being replaced is advertising optimization <a class="yt-timestamp" data-t="00:39:34">[00:39:34]</a>.

### For Incumbents

Larger companies should adopt a structured approach to integrate AI <a class="yt-timestamp" data-t="00:43:54">[00:43:54]</a>:

1.  **Find Asymmetric Upside**: Start with simple AI features that offer quick wins and help the organization learn about costs and latency <a class="yt-timestamp" data-t="00:42:19">[00:42:19]</a>.
2.  **Workflow Analysis**: Break down the entire product into individual workflows <a class="yt-timestamp" data-t="00:42:38">[00:42:38]</a>.
3.  **Automate or Delete**: If AI can reliably and accurately perform an entire workflow, let AI do it and remove the old process <a class="yt-timestamp" data-t="00:43:04">[00:43:04]</a>.
4.  **Augment or Simplify**: If AI cannot fully remove a workflow, but can augment it or reduce it to a simple decision, implement that <a class="yt-timestamp" data-t="00:43:32">[00:43:32]</a>.
5.  **Sprinkle AI**: For other areas, "sprinkle" AI elements to ensure the offering looks comprehensive <a class="yt-timestamp" data-t="00:43:51">[00:43:51]</a>.
6.  **Sell the Value**: Crucially, learn how to communicate and sell the value of these AI enhancements to customers <a class="yt-timestamp" data-t="00:44:12">[00:44:12]</a>.

## Overhyped vs. Underhyped AI Areas

Dez Trainer identified the following:

*   **Overhyped**: AI productivity tools focused on generating content like emails or sales pitches <a class="yt-timestamp" data-t="00:44:35">[00:44:35]</a>. He believes people will learn to detect AI-generated content, and the focus on "good writing" will return <a class="yt-timestamp" data-t="00:44:42">[00:44:42]</a>.
*   **Underhyped**: The transformative impact of AI on creativity <a class="yt-timestamp" data-t="00:44:56">[00:44:56]</a>. Referencing Instagram's filters democratizing photography, he highlights tools like Kaiber, Refusion (for sound), and Synthesia (for video) as ushering in new forms of creativity that are yet to be fully understood <a class="yt-timestamp" data-t="00:45:01">[00:45:01]</a><a class="yt-timestamp" data-t="00:45:22">[00:45:22]</a><a class="yt-timestamp" data-t="00:45:27">[00:45:27]</a>.

## Impressive and Disappointing Incumbents

Beyond Microsoft and Google, Adobe, Figma, and Miro were cited as impressive incumbents for quickly integrating useful AI features <a class="yt-timestamp" data-t="00:46:11">[00:46:11]</a><a class="yt-timestamp" data-t="00:46:21">[00:46:21]</a>. On the other hand, Apple and Amazon were noted for their surprisingly slow adoption of advanced AI capabilities in products like Siri and Alexa, which currently feel primitive compared to tools like ChatGPT <a class="yt-timestamp" data-t="00:46:48">[00:46:48]</a><a class="yt-timestamp" data-t="00:46:50">[00:46:50]</a><a class="yt-timestamp" data-t="00:47:30">[00:47:30]</a>. Dez hopes for a "leveling out" in 2024 as these major players inevitably integrate more sophisticated AI <a class="yt-timestamp" data-t="00:47:44">[00:47:44]</a>.