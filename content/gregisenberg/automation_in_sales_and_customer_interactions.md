---
title: Automation in Sales and Customer Interactions
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

[[Automation and AI in customer support | Voice AIs]] are demonstrating capabilities that many people underestimate, with the potential to [[Automating business processes with AI | automate]] most phone-based work within the next one to three years <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. This extends to various aspects of sales and customer interactions, from outbound sales calls to gathering customer feedback.

## Case Study: The "Lowballer 9000" Voice AI

Tony, an [[Automating Business Processes with AI Agents | automation]] expert, created a voice AI named "Lowballer 9000" (or Alex) to negotiate prices for a Rolex Daytona, a $35,000 watch, with luxury secondhand watch dealers across the US <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>.

The AI's primary objectives were to:
*   Identify sellers of Rolex Daytona watches <a class="yt-timestamp" data-t="00:01:46">[00:01:46]</a>.
*   Gather critical details about the watch, such as its condition, and whether it included original documentation and packaging, as these factors significantly impact the quoted price <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.
*   Attempt to lowball dealers <a class="yt-timestamp" data-t="00:00:12">[00:00:12]</a>.

### Tools and Workflows

The voice AI was built using **Vappy**, a flexible platform for creating voice agents <a class="yt-timestamp" data-t="00:02:47">[00:02:47]</a>. Vappy allows users to bring their own prompts and choose their service providers <a class="yt-timestamp" data-t="00:03:00">[00:03:00]</a>.

Key aspects of the setup included:

*   **Prompt Engineering**
    *   The prompt was initially self-written and refined through iterative testing and observation of human lowballers <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.
    *   **Conciseness**: Responses were kept to one or two sentences maximum to prevent the AI from overwhelming the caller with too much information at once <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
    *   **Language Level**: Adopting a "sixth-grade English level" for conversations significantly increased call durations and made the AI sound more human <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Model Selection**
    *   The choice of AI model (e.g., Gemini 20 Flash, DeepSeek) is often dynamic, influenced by factors like cost and API availability <a class="yt-timestamp" data-t="00:06:07">[00:06:07]</a>. API stability is crucial, as a model's increased popularity can lead to service disruptions <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>.
*   **Temperature Setting**
    *   The "temperature" setting controls the AI's creativity <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. A temperature closer to zero results in more predictable, deterministic responses, while a higher temperature allows for more creative, yet potentially inappropriate, answers when faced with unexpected questions <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.
*   **Voice Configuration**
    *   A specific voice, like "Cartisia" (referred to as "New York man" or "Sopranos voice"), was chosen for its distinct character <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Tool Calls**
    *   The most powerful feature of Vappy is its ability to integrate with existing tools <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
    *   **Call Data Management**: A tool call was set up to record all conversations into a database (e.g., Airtable). After each call, the transcript was analyzed to determine if an offer was received, if the lowball offer was accepted, or if a final price was provided <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This allowed for efficient sifting through hundreds of calls to find actionable outcomes <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
    *   **Data Extraction**: Integration with tools like Lindy can flexibly extract large amounts of text data and organize it into spreadsheets, even adapting to new columns automatically <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.
*   **Phone Number Registration (Twilio)**
    *   A significant hurdle was ensuring calls actually rang through instead of going straight to voicemail <a class="yt-timestamp" data-t="00:15:03">[00:15:03]</a>. This required registering the phone number in a database to comply with FCC mechanisms like Stir/Shaken, which perform "Know Your Customer" (KYC) checks on numbers to prevent spam calls <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>.

## Broader Use Cases for Voice AIs in Business

Beyond the watch-dealing example, [[Automating Business Processes with AI Agents | voice AI agents]] offer significant opportunities for businesses, particularly in sales and data acquisition:

*   **Sales Prospecting**: Voice AIs can call prospect lists, ask qualifying questions, and identify leads that meet specific criteria (e.g., in real estate, determining if a house is likely to go on the market) <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. This allows for large-scale data collection to identify high-potential targets for human follow-up <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
*   **[[Automation in app creation | Data-Driven Arbitrage Businesses]]**: Voice AIs excel at gathering specific data, which can provide an "unfair advantage" in markets where information asymmetry exists <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. For example, identifying undervalued items by calling sellers and then reselling them on secondary markets for a profit <a class="yt-timestamp" data-t="00:19:09">[00:19:09]</a>. This process can be further [[role_of_ai_in_automating_manual_processes | automated]] to dispatch teams for pickups once an offer is accepted <a class="yt-timestamp" data-t="00:19:25">[00:19:25]</a>.
*   **Customer Feedback Collection**: Voice AIs can be used to collect qualitative feedback from customers, allowing them to "brain dump" their thoughts freely <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This feedback can then be automatically categorized, classified, summarized, and posted to internal communication channels (e.g., Slack) to improve services, replacing traditional, often tedious, feedback forms <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>. This provides businesses with direct, organized customer insights without manual effort <a class="yt-timestamp" data-t="00:21:49">[00:21:49]</a>. This is an example of [[ai_agents_and_customer_service | AI agents and customer service]].

The potential for [[Automated business creation using AI | automation]] using voice AIs lies in leveraging data to create an unfair advantage. Any business where "knowledge is an unfair advantage" and knowing more than a competitor is key, likely has a voice AI opportunity <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.