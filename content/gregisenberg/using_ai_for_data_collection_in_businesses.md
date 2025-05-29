---
title: Using AI for data collection in businesses
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Tony, an automation expert from SA Checkout, demonstrates the capabilities of voice AIs for business applications, highlighting their potential for automating phone-based work and efficiently collecting data <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a>. He believes that any work currently done over the phone could be automated within the next one to three years <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## Case Study: "Lowballer 9000" Voice AI

Tony showcases a voice AI he developed, named "Lowballer 9000" (or Alex), designed to lowball luxury watch dealers across the US for Rolex Daytonas <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a> <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The AI's primary objective is to acquire a Rolex Daytona, a watch valued at around $35,000 <a class="yt-timestamp" data-t="00:01:15">[00:01:15]</a> <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.

The AI targets secondhand luxury watch dealers, not official Rolex factory dealers <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>. Its tasks include:
*   Gathering critical details like the watch's condition <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   Confirming the presence of original documentation and packaging <a class="yt-timestamp" data-t="00:02:01">[00:02:01]</a>.
These details significantly impact the watch's quoted cost <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>.

## Key Tools and Workflow

### Vappy: The Voice API Platform
Tony uses Vappy (short for Voice API) as the platform for [[building_automated_businesses_with_ai | building automated businesses with AI]] and these voice agents <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Vappy offers flexibility by allowing users to bring their own prompts and choose various service providers without proprietary lock-ins <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

### Prompt Engineering Best Practices
The AI's prompt was primarily written by Tony, with guidance from Vappy's general best practices <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The prompt is continuously refined based on testing and observing how the AI responds to real-world conversations <a class="yt-timestamp" data-t="00:03:45">[00:03:45]</a>.
*   **Iterative Refinement**: Tony simulates conversations based on how human lowballers interact with watch sellers, then "patches holes" in the AI's responses when it behaves undesirably <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a> <a class="yt-timestamp" data-t="00:04:50">[00:04:50]</a>. For example, he modified the prompt to ensure the AI asks one question at a time, keeping responses concise (one to two sentences max) to avoid sounding robotic <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a> <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **"Sixth-Grade English" Rule**: Tony discovered that structuring the prompt to use "sixth-grade English" significantly increased call durations and made the AI sound more human <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Model Selection and Temperature
*   **Model Choice**: The choice of AI model (e.g., Gemini 20 Flash, DeepSeek) is often influenced by the "flavor of the month" <a class="yt-timestamp" data-t="00:06:01">[00:06:01]</a> <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. API stability is a critical factor, as high demand can lead to service interruptions <a class="yt-timestamp" data-t="00:08:12">[00:08:12]</a>.
*   **Temperature Setting**: "Temperature" controls the creativity of the AI's responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. A lower temperature (closer to zero) results in a more predictable, almost deterministic system, while a higher temperature allows for more creative, but potentially inappropriate, responses to unusual questions <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

### Voice Configuration
For the "Lowballer 9000," Tony selected a voice named "Cartisia, New York man," which sounds like a Soprano's character <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a> <a class="yt-timestamp" data-t="00:09:19">[00:09:19]</a>.

### Twilio and Call Delivery
A significant hurdle was ensuring calls actually rang phones instead of going straight to voicemail <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. This requires users to bring their own registered phone number and complete KYC (Know Your Customer) requirements to comply with FCC mechanisms like "shake and stir" <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Tony noted that hundreds of his initial calls went straight to voicemail due to this issue <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

## Leveraging Collected Data with Tool Calls and Lindy

A key feature for [[automating_business_processes_with_ai | automating business processes with AI]] and making voice AIs powerful is their ability to interact with existing tools via "tool calls" <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a> <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.

### Automated Call Data Management
Tony integrated his AI with an AirTable spreadsheet acting as a "watch list" database <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This database automatically records every call placed by the AI <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. After each conversation, a tool call analyzes the transcript to extract actionable information, such as:
*   Whether an offer was received <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   The lowballed amount <a class="yt-timestamp" data-t="00:11:13">[00:11:13]</a>.
*   Whether the lowball was accepted <a class="yt-timestamp" data-t="00:11:18">[00:11:18]</a>.
*   The final price offered if the lowball was not accepted <a class="yt-timestamp" data-t="00:11:20">[00:11:20]</a>.

This automation makes it easy to sift through hundreds of calls to find those that resulted in an actionable offer, saving significant manual effort <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.

### Lindy for Flexible Data Extraction
Lindy is highlighted as an excellent tool for flexibly taking large amounts of text and organizing it into a spreadsheet <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. It can automatically read column names (e.g., "vegan friendly") and populate corresponding data from given content (like a website scrape or menu), without requiring manual rule-writing or logging back in to configure automations <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. This capability enables powerful [[using_ai_and_automation_tools_for_efficient_business_solutions | efficient business solutions using AI and automation tools]] when combined with Vappy <a class="yt-timestamp" data-t="00:14:27">[00:14:27]</a>.

## Broader Applications and Business Ideas

The potential of voice AIs extends far beyond watch dealing, offering significant opportunities for [[examples_of_ai_applications_in_business | examples of AI applications in business]] and startups.

### Sales and Lead Generation
Voice AIs can automate sales prospecting <a class="yt-timestamp" data-t="00:16:16">[00:16:16]</a>. For example, in real estate, an AI could call a prospect list to ascertain if a family member recently passed or if a house is likely to enter the market soon <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>. By asking specific questions, the AI can gather data to identify houses with a higher probability of appearing on the market <a class="yt-timestamp" data-t="00:16:35">[00:16:35]</a>. This allows businesses to call thousands of numbers to identify qualified leads for human follow-up <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>. This exemplifies [[using_ai_for_data_enrichment_and_lead_generation | using AI for data enrichment and lead generation]].

### Data as an Unfair Advantage
A core framework for [[utilizing_ai_and_tools_for_business_development | utilizing AI and tools for business development]] is to view voice AI agents as a way to acquire data that provides an "unfair advantage" <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a> <a class="yt-timestamp" data-t="00:17:36">[00:17:36]</a>.
*   **Arbitrage Businesses**: The watch lowballing AI is a prime example of an arbitrage business, where data acquisition allows for buying at a lower price and selling higher, creating thousands of dollars in profit at scale <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a> <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. This can be scaled by automating the dispatch of a team to pick up items once an offer is accepted <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>.
*   **Information Edge**: If data or knowledge provides an unfair advantage over competitors, then a voice AI opportunity likely exists <a class="yt-timestamp" data-t="00:18:21">[00:18:21]</a>. This can lead to a more transparent secondary market in various industries <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.

### Automating Customer Feedback with AI Agents
Tony developed another voice AI for Startup Empire, a private membership for building cash-flowing internet businesses <a class="yt-timestamp" data-t="00:20:29">[00:20:29]</a> <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. This AI collects feedback from members via voice calls, allowing them to "brain dump" without filling out forms <a class="yt-timestamp" data-t="00:20:32">[00:20:32]</a> <a class="yt-timestamp" data-t="00:20:47">[00:20:47]</a>. The AI, combined with Lindy, categorizes, classifies, summarizes, and posts the feedback to a Slack channel, making it easy for the core team to act on <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a> <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>. This is a practical [[utilizing_ai_agents_to_automate_business_tasks | utilization of AI agents to automate business tasks]]. This specific application highlights the [[role_of_ai_in_marketing_and_business_growth | role of AI in marketing and business growth]].

This feedback system is also presented as a potential business idea: offering such a voice AI feedback collection and reporting service to other companies <a class="yt-timestamp" data-t="00:22:03">[00:22:03]</a>.