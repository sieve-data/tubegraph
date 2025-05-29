---
title: Automation in luxury watch market
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Tony, an "automation man" from SA Checkout, demonstrated how a voice AI can be used to navigate and potentially disrupt the [[luxury_and_status_goods_in_the_ai_era | luxury watch market]] by lowballing dealers <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This practical application highlights the underestimated capabilities of voice AIs and suggests that any phone-based work could be [[automating_business_tasks_with_ai | automated]] within the next 1 to 3 years <a class="yt-timestamp" data-t="01:05">[00:01:05]</a>.

## Lowballer 9000: An AI for Luxury Watches

Tony developed a voice AI, affectionately named "Lowballer 9000" (or Alex), whose primary objective is to find a Rolex Daytona <a class="yt-timestamp" data-t="01:31">[00:01:31]</a>. The AI targets secondhand luxury watch dealers, not official Rolex factory dealers, seeking to acquire watches like the Rolex Daytona, which can be valued around $35,000 <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>, at a lower price <a class="yt-timestamp" data-t="02:26">[00:02:26]</a>.

Alex's key tasks include:
*   Gathering critical details about the watch's condition <a class="yt-timestamp" data-t="01:56">[00:01:56]</a>.
*   Confirming the availability of original documentation and packaging, as these factors significantly impact the watch's quoted cost <a class="yt-timestamp" data-t="02:01">[00:02:01]</a>.

## Tools and Workflow for Voice AI Automation

### Vappy: The Core Platform
The platform used for this voice AI project is Vappy, which essentially functions as a flexible Voice API <a class="yt-timestamp" data-t="02:49">[00:02:49]</a>. Vappy allows users to bring their own prompts and select different service providers for various AI functionalities, offering a non-proprietary environment for building voice agents <a class="yt-timestamp" data-t="03:02">[00:03:02]</a>.

### Prompt Engineering and Refinement
The AI's prompt was largely self-written and iteratively refined based on testing and real-world observations <a class="yt-timestamp" data-t="03:26">[00:03:26]</a>. Tony's process involved:
*   Observing how real people lowball watch sellers <a class="yt-timestamp" data-t="03:55">[00:03:55]</a>.
*   Simulating those conversations with Alex and Vappy <a class="yt-timestamp" data-t="04:02">[00:04:02]</a>.
*   Patching "holes" in the prompt when Alex responded in undesirable ways, such as asking too many questions at once <a class="yt-timestamp" data-t="04:57">[00:04:57]</a>.
*   Adding instructions like "keep responses concise. One to two sentences max" to make interactions more natural and less "obviously AI" <a class="yt-timestamp" data-t="04:43">[00:04:43]</a>.
*   A crucial learning was to instruct the AI to use "sixth-grade English" as most conversations happen at this level, which led to longer call durations and more human-like interactions <a class="yt-timestamp" data-t="05:33">[00:05:33]</a>.

### AI Model Selection
The choice of AI model for the voice agent is described as "flavor of the month" dependent <a class="yt-timestamp" data-t="06:18">[00:06:18]</a>. While the demonstration showed Gemini 20 Flash <a class="yt-timestamp" data-t="06:04">[00:06:04]</a>, Tony initially used DeepSeek <a class="yt-timestamp" data-t="06:23">[00:06:23]</a>. However, DeepSeek's API became "slammed" during a hype cycle, causing the bot to crash or not respond to calls <a class="yt-timestamp" data-t="08:12">[00:08:12]</a>. The advice is to pick a model that is currently available and stable <a class="yt-timestamp" data-t="08:17">[00:08:17]</a>.

The "temperature" setting in the model configuration controls the AI's creativity <a class="yt-timestamp" data-t="08:24">[00:08:24]</a>. A temperature closer to zero makes the system more deterministic, but it might struggle with uncommon questions <a class="yt-timestamp" data-t="08:35">[00:08:35]</a>.

### Voice Configuration
The AI's voice was configured using "Cartisia" or "New York man," which has a Sopranos-like quality <a class="yt-timestamp" data-t="09:19">[00:09:19]</a>.

### Tool Calls and Data Management
A powerful aspect of Vappy is its ability to interact with existing tools through "tool calls" <a class="yt-timestamp" data-t="10:12">[00:10:12]</a>.
*   **Call Recording and Analysis**: A key tool call was set up to record all calls and analyze transcripts upon conversation completion <a class="yt-timestamp" data-t="10:27">[00:10:27]</a>. This enabled the system to automatically determine if an offer was received, how much the item was lowballed for, and if the lowball was accepted or a counter-offer given <a class="yt-timestamp" data-t="11:00">[00:11:00]</a>.
*   **AirTable Integration**: The data from these calls was stored in an AirTable spreadsheet, allowing for easy sifting through hundreds of calls to find actionable offers <a class="yt-timestamp" data-t="10:34">[00:10:34]</a>.

### Lindy Integration for Flexible Data Extraction
Lindy is highlighted for its ability to flexibly process large amounts of text and populate spreadsheets <a class="yt-timestamp" data-t="12:50">[00:12:50]</a>. It can automatically understand column names (e.g., "vegan friendly") and extract relevant information from unstructured text (like a restaurant menu) to populate the spreadsheet without requiring manual rule-writing or logging back into an automation platform <a class="yt-timestamp" data-t="13:54">[00:13:54]</a>. This capability could be married with Vappy to enhance data collection workflows.

### Twilio and Phone Number Registration
A significant hurdle in implementing such voice AI was ensuring calls actually rang through to phones <a class="yt-timestamp" data-t="14:59">[00:14:59]</a>. This requires using a service like Twilio <a class="yt-timestamp" data-t="14:53">[00:14:53]</a> and complying with "Shake and Stir" regulations, an FCC mechanism that requires phone number registration (KYC) <a class="yt-timestamp" data-t="15:07">[00:15:07]</a>. Failure to do so results in calls going straight to voicemail <a class="yt-timestamp" data-t="15:28">[00:15:28]</a>.

## Business Opportunities with Voice AI

The demonstration of the luxury watch lowballer bot illustrates broader [[opportunities_in_automated_workflow_platforms | opportunities in automated workflow platforms]] and [[building_automated_businesses_with_ai | building automated businesses with AI]].

### Arbitrage Businesses
Voice AIs can gather data to create an "unfair advantage" and facilitate arbitrage businesses <a class="yt-timestamp" data-t="17:38">[00:17:38]</a>. In the luxury watch example, collecting data on low prices allows for buying watches (e.g., for $19,000) and reselling them on the secondary market for a profit (e.g., $22,000), a process that can be scaled and further automated <a class="yt-timestamp" data-t="19:10">[00:19:10]</a>. The core idea is to identify businesses where data or knowledge provides a competitive edge <a class="yt-timestamp" data-t="18:25">[00:18:25]</a>.

### Sales Prospecting
Voice AIs can automate sales prospecting calls <a class="yt-timestamp" data-t="16:20">[00:16:20]</a>. For instance, in real estate, an AI could call prospects to ask specific questions, classify responses, and identify properties likely to enter the market soon <a class="yt-timestamp" data-t="16:25">[00:16:25]</a>. This allows for targeting only those who meet specific criteria for follow-up <a class="yt-timestamp" data-t="17:01">[00:17:01]</a>.

### Customer Feedback Collection
Another practical application is building a voice AI to collect customer feedback <a class="yt-timestamp" data-t="20:24">[00:20:24]</a>. For example, a feedback bot for Startup Empire, a private membership for [[building_automated_businesses_with_ai | building cash-flowing internet businesses]] <a class="yt-timestamp" data-t="21:07">[00:21:07]</a>, allows members to call a number and "brain dump" their feedback <a class="yt-timestamp" data-t="20:48">[00:20:48]</a>. The AI then categorizes and classifies this information, which is summarized and posted to a Slack channel, providing actionable insights for improving the service <a class="yt-timestamp" data-t="20:58">[00:20:58]</a>. This represents a potentially lucrative business idea that can be offered to other companies <a class="yt-timestamp" data-t="22:05">[00:22:05]</a>.

This demonstrates the broad utility of [[ai_automation_tools_for_workflows | AI automation tools for workflows]] and offers concrete examples of [[how_to_automate_business_processes_with_ai | how to automate business processes with AI]] to generate value from [[manual_processes_and_opportunities_for_automation | manual processes and opportunities for automation]]. The core principle is leveraging voice AI to gather valuable data and gain a competitive edge.