---
title: AI automation for phonebased tasks
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AIs are capable of automating phone-based tasks, with predictions suggesting that any work currently done over the phone could be automated within the next one to three years <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This automation can provide an unfair advantage by collecting data and creating arbitrage opportunities <a class="yt-timestamp" data-t="01:37:38">[01:37:38]</a>.

## Case Study: Lowballer 9000

Tony, an automation expert from SA Checkout, demonstrated "Lowballer 9000," a voice AI designed to negotiate prices for luxury watches <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. This AI successfully lowballed luxury watch dealers across the U.S. for Rolex Daytonas, watches valued around $35,000 <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>.

The AI, named Alex, was tasked with:
*   Searching for Rolex Daytonas <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.
*   Identifying that it was speaking with secondhand luxury watch dealers <a class="yt-timestamp" data-t="01:49:00">[01:49:00]</a>.
*   Gathering critical details about the watch, such as its condition and whether original documentation and packaging were included, as these details significantly impact the quoted cost <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

## Tools and Workflow

The primary platform used for building the voice agent was Vapi (Voice API) <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. Vapi offers flexibility, allowing users to bring their own prompts and choose various service providers <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### Prompt Engineering
The AI's prompt was developed through an iterative process of testing and refinement <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. Key prompt strategies included:
*   Observing and simulating real-life lowballing conversations by content creators <a class="yt-timestamp" data-t="03:55:00">[03:55:00]</a>.
*   Patching "holes" in the AI's responses, such as preventing it from asking too many questions at once <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.
*   Keeping responses concise, typically one to two sentences max <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
*   Instructing the AI to use language at a "sixth-grade English level" to increase call durations and make conversations sound more human <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.

### AI Model Selection
Model choice is often dependent on current trends, described as "flavor of the month" <a class="yt-timestamp" data-t="06:18:00">[06:18:00]</a>. The project initially used DeepSeek, which caused issues when its API became overloaded due to hype, leading to the bot not responding to calls <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. The general recommendation is to pick a model that is available and reliable <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.

### Temperature Setting
"Temperature" controls how creative the AI's responses are <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. A temperature closer to zero results in a more predictable, deterministic system, but it may struggle with uncommon questions <a class="yt-timestamp" data-t="08:35:00">[08:35:00]</a>.

### Voice Configuration
Specific voices can be selected; for Lowballer 9000, "Cartisia" (dubbed "New York man") was used, which has an Italian/New Jersey accent, reminiscent of a fictional character <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

### Tool Calling and Integrations
The true power of voice AIs lies in their ability to interact with existing tools <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.
*   **Data Recording and Analysis:** Lowballer 9000 used a tool call to record all conversations and process transcripts, automatically identifying actionable offers received from dealers <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>. This data was then organized into an AirTable spreadsheet, making it easy to sift through hundreds of calls and find valuable information for content creation <a class="yt-timestamp" data-t="11:28:00">[11:28:00]</a>.
*   **Lindy for Flexible Data Categorization:** [[Lindy | Lindy]] excels at taking large amounts of text and flexibly populating spreadsheets, even when new columns (e.g., "vegan friendly") are added mid-research, automatically reading the column name and categorizing content without manual rule updates <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. This capability allows for more dynamic [[automating_workflows_using_ai | automating workflows using AI]] and [[automating_business_processes_with_ai | Automating business processes with AI]].

### Call Delivery with Twilio
A significant hurdle in call automation is ensuring calls actually ring the phones rather than going straight to voicemail <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>. This requires complying with FCC mechanisms like "Shake and Stir," which necessitates registering phone numbers in a database for KYC (Know Your Customer) <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. Without proper registration, hundreds of calls may fail to connect <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.

## AI Use Cases and Business Opportunities

Voice AIs offer numerous opportunities for businesses and startups:

*   **Sales Prospecting:** Automating outreach to prospect lists, such as in real estate, to gather specific information (e.g., if a house is likely to go on the market soon) <a class="yt-timestamp" data-t="16:20:00">[01:16:20]</a>. This allows for rapid qualification of leads at scale <a class="yt-timestamp" data-t="16:59:00">[01:16:59]</a>.
*   **Data Collection for Arbitrage:** Voice AI is a powerful tool to collect data, providing an "unfair advantage" in markets where information is key <a class="yt-timestamp" data-t="17:34:00">[01:17:34]</a>. This can lead to arbitrage opportunities, as demonstrated by the watch lowballing, where thousands of dollars in profit can be made by efficiently acquiring data on buying and selling prices <a class="yt-timestamp" data-t="17:49:00">[01:17:49]</a>. Businesses where "knowledge is an unfair advantage" are prime candidates for [[utilizing_ai_agents_to_automate_business_tasks | utilizing AI agents to automate business tasks]] <a class="yt-timestamp" data-t="18:25:00">[01:18:25]</a>.
*   **Automated Feedback Collection:** An [[ai_workflow_automation | AI workflow automation]] can collect feedback from customers via voice, allowing for "brain dumps" that are then categorized and summarized (e.g., in a Slack channel) <a class="yt-timestamp" data-t="20:27:00">[02:20:27]</a>. This [[adding_ai_intelligence_to_manual_processes | adding AI intelligence to manual processes]] improves service delivery by providing instant, organized insights without manual form completion <a class="yt-timestamp" data-t="20:58:00">[02:20:58]</a>. This can be productized as a service for other companies <a class="yt-timestamp" data-t="22:05:00">[02:22:05]</a>.

Ultimately, if knowing more than a competitor provides an advantage, there is likely an opportunity for voice AI <a class="yt-timestamp" data-t="18:28:00">[01:18:28]</a>.