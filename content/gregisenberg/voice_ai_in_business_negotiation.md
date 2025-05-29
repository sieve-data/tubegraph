---
title: Voice AI in business negotiation
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AI is increasingly capable of automating phone-based work, potentially transforming various business operations within 1 to 3 years <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This technology can be leveraged for tasks like negotiation, sales, and data collection, providing a significant competitive advantage.

## Case Study: The "Lowballer 9000" Voice AI

Tony from SA Checkout developed a voice AI, named "Lowballer 9000" (or Alex), with the specific goal of lowballing luxury watch dealers in the US for Rolex Daytonas, which are watches valued around $35,000 <a class="yt-timestamp" data-t="00:00:08">[00:00:08]</a> <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>. This AI successfully secured an offer, demonstrating the potential of voice AI in business negotiation <a class="yt-timestamp" data-t="00:00:19">[00:00:19]</a> <a class="yt-timestamp" data-t="00:00:40">[00:00:40]</a>.

The AI's primary job was to find a Rolex Daytona by calling secondhand luxury watch dealers <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a> <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. It was programmed to:
*   Gather critical details about the watch, such as its condition, original documentation, and packaging, as these details can significantly impact the price <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.
*   Engage in negotiation to lowball the dealers <a class="yt-timestamp" data-t="01:13:00">[01:13:00]</a>.

## [[tools_and_models_for_voice_automation | Tools and Models for Voice Automation]]

### Vapi
The "Lowballer 9000" was built using Vapi, a platform that provides a flexible way to build voice agents <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a> <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>. Vapi allows users to bring their own prompts and select their preferred service providers for different functionalities, without locking them into proprietary systems <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>.

### Prompt Engineering
The AI's prompt was developed through an iterative process, reacting to testing and observations of how human watch sellers operate in real life <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Key prompt adjustments included:
*   **Conciseness:** Ensuring responses were concise, often one to two sentences max, to prevent the AI from "ramming every single question down one's throat" and sounding less engaging or obviously AI <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a> <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
*   **Language Level:** Changing the prompt to use "sixth-grade English" significantly increased call durations and made the AI sound more human, as most conversations occur at this language level <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a> <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

### Model Selection
The choice of an AI model depends on the specific use case <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. The "Lowballer 9000" initially used DeepSeek, which was cost-effective but later experienced crashes due to high demand and API congestion <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a> <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. The current model is Gemini 20 Flash <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. It's important to pick a model that is available and reliable <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.

### Temperature Parameter
The "temperature" setting (e.g., `temperature: 1`) controls how creative the AI's responses are <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. A temperature closer to zero results in a more deterministic and predictable system, but it may struggle to respond appropriately to uncommon questions <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.

### Voice Configuration
The AI's voice plays a role in its perceived humanity. The "Lowballer 9000" uses the "Cartisia" voice, which is described as a "New York man" (allegedly referencing a character from "The Sopranos") <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

### Tool Calls and Integrations
A powerful aspect of voice AI is its ability to interact with existing tools through "tool calls" <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
*   **Data Recording and Analysis:** The "Lowballer 9000" used a tool call to record all conversations and send the transcripts to an AirTable spreadsheet <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a> <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>. This allowed the system to automatically identify calls that resulted in actionable offers, including whether an offer was received, if the lowball was accepted, or if a final price was given <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a> <a class="yt-timestamp" data-t="11:11:00">[11:11:00]</a>. This streamlined the process of sifting through over 800 calls <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.
*   **Lindy Integration:** For flexible data processing, especially for taking large amounts of text and structuring it into spreadsheets, an AI tool like Lindy can be integrated <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. Lindy can automatically read column names (e.g., "vegan friendly") and categorize information from content like website scrapes or menus, automating data entry without manual intervention <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.
*   **Twilio for Calls:** To ensure calls actually ring phones and avoid going straight to voicemail, it's crucial to use a registered phone number (e.g., through Twilio) and complete KYC (Know Your Customer) requirements due to FCC mechanisms like "shake and stir" <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a> <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>.

## Broader [[applications_of_voice_ai_in_sales_and_feedback_collection | Applications of Voice AI in Sales and Feedback Collection]]

Voice AI extends far beyond negotiation:
*   **Sales:** In real estate, for example, a voice AI can call prospects to gather information (e.g., if a family member recently passed, or if a house is going on the market soon) to identify leads with a high likelihood of conversion <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>. This allows for calling thousands of numbers to filter for specific criteria <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>.
*   **Arbitrage Businesses:** Voice AI can gather data to create arbitrage opportunities, like identifying items (e.g., watches) that can be bought at a lower price from one source and sold at a higher price in a secondary market <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a> <a class="yt-timestamp" data-t="19:06:00">[19:06:00]</a>.
*   **Feedback Collection:** Voice AIs can collect feedback from users without requiring them to fill out forms <a class="yt-timestamp" data-t="20:24:00">[20:24:00]</a>. For instance, a bot can listen to "brain dumps" from community members, categorize the information, and then summarize it into a Slack channel, providing actionable insights for service improvement <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a> <a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>.

## [[ai_agents_in_business_automation | AI Agents in Business Automation]]

The core principle for identifying business opportunities with voice AI agents is to consider where "data is an unfair advantage" or where "knowledge is an unfair advantage" <a class="yt-timestamp" data-t="17:32:00">[17:32:00]</a> <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>. If knowing something more than a competitor can provide an edge, there is likely a voice AI opportunity to gather that information at scale <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>. This approach can lead to the creation of more transparent secondary markets <a class="yt-timestamp" data-t="18:47:00">[18:47:00]</a>.