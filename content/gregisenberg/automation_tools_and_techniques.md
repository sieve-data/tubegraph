---
title: Automation tools and techniques
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Tony, an expert in [[automations_and_ai_tools_for_business_efficiency | automations and AI tools]], highlights the significant potential of voice AIs, believing that any phone-based work could be automated within the next 1 to 3 years <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. He shares insights into the tools, workflows, and prompts used for such automations <a class="yt-timestamp" data-t="01:11:02">[01:11:02]</a>.

## Case Study: "Lowballer 9000" Voice AI

Tony developed a voice AI, affectionately named "Lowballer 9000," whose primary function is to call luxury watch dealers across the US and lowball them for Rolex Daytonas <a class="yt-timestamp" data-t="01:12:08">[01:12:08]</a>. The AI, named Alex, acts as a negotiator, specifically targeting secondhand dealers rather than official Rolex stores <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

Its core tasks include:
*   Gathering critical details about the watch, such as condition, original documentation, and packaging, which significantly impact the quoted cost <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.
*   Negotiating prices with dealers <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

### Core Tool: Vappy

The primary platform used for building this voice agent is Vappy, which stands for Voice API <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. Vappy offers flexibility, allowing users to bring their own prompts and select their preferred service providers, rather than being locked into proprietary systems <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

### Vappy Configuration and Best Practices

*   **Prompt Engineering** <a class="yt-timestamp" data-t="03:11:00">[03:11:00]</a>:
    *   The prompt for Lowballer 9000 was primarily written by Tony, drawing inspiration from Vappy's general best practices documentation <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
    *   Prompt refinement is an iterative process, heavily influenced by testing and observing how the AI responds in simulated conversations <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. For instance, an early issue where the AI would ask all questions at once was resolved by adding a rule to keep responses concise (1-2 sentences maximum) <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. This iterative "patching holes" approach helps improve the AI's conversational flow <a class="yt-timestamp" data-t="04:50:00">[04:50:00]</a>.
    *   **Key Insight:** For more human-sounding conversations and longer call durations, prompts should aim for a "sixth-grade English level" <a class="yt-timestamp" data-t="05:27:00">[05:27:00]</a>.
*   **Model Selection**:
    *   The choice of AI model (e.g., Gemini 20 Flash, DeepSeek) is context-dependent and often follows a "flavor of the month" trend <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>.
    *   Practical considerations are crucial: DeepSeek, while cost-effective initially, crashed due to high traffic during its hype cycle, causing the bot to become unresponsive <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>. It's important to pick a model that is available and reliable <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.
*   **Temperature Setting**:
    *   "Temperature" controls how creative the AI's responses are <a class="yt-timestamp" data-t="08:21:00">[08:21:00]</a>.
    *   A temperature closer to zero results in a more deterministic and predictable system <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>. However, this can lead to inappropriate responses when faced with uncommon questions <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.
*   **Voice Configuration**:
    *   Vappy allows selection of different voices, such as "Cartisia" or "New York man" (a reference to the Sopranos character) <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

### Leveraging Tool Calls for Data Analysis

A powerful feature of Vappy is its "tool calls," which enable the voice AI to interact with existing external tools <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
*   **Call Recording and Analysis**: A critical tool call records all conversations and analyzes the transcript to identify actionable outcomes <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>.
*   **Airtable Integration**: The `get best offer` tool call interacts with an Airtable spreadsheet (the "watch list") to:
    *   Record every call the AI makes <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>.
    *   Determine if an offer was received <a class="yt-timestamp" data-t="11:00:00">[11:00:00]</a>.
    *   Note how much the AI lowballed and whether the lowball was accepted <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
    *   Capture any counter-offers and final prices <a class="yt-timestamp" data-t="11:20:00">[11:20:00]</a>.
This process simplifies sifting through hundreds of calls to find relevant data for content creation or business insights <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.

### Integration with Lindy

Lindy is highlighted as an [[ai_automation_in_business_workflows | AI automation]] tool particularly effective at flexibly processing large amounts of text and organizing it into spreadsheets <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. Lindy can dynamically add columns to a spreadsheet and automatically populate them based on content (e.g., identifying "vegan friendly" restaurants from a menu scrape), removing the need for manual rule writing or reconfiguring automations <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>. This capability makes it a strong partner for Vappy in various automation scenarios <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>.

### Overcoming Technical Hurdles: Twilio and SHAKEN/STIR

A significant challenge in setting up voice AI calls is ensuring they ring through to phones rather than going straight to voicemail <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.
*   **The Problem**: The FCC's SHAKEN/STIR mechanism requires phone numbers to be registered in their database with Know Your Customer (KYC) verification <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. Unregistered numbers will often be sent directly to voicemail <a class="yt-timestamp" data-t="15:28:00">[15:28:00]</a>.
*   **The Solution**: Users must bring their own registered phone number and ensure KYC is complete before placing calls <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>. Tony experienced over 300 calls going to voicemail before implementing this solution <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.

## Broader Use Cases for Voice AI

Voice AIs offer significant potential for various business applications beyond just lowballing <a class="yt-timestamp" data-t="15:50:00">[15:50:00]</a>.

### Examples of [[ai_automation_in_business_workflows | AI Automation]] Use Cases:
*   **Sales Prospecting**: In real estate, a voice AI can call prospects to gather specific information (e.g., if a family member recently passed or if a house is going on the market soon) <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>. By asking targeted questions, it can identify high-potential leads that match specific criteria <a class="yt-timestamp" data-t="16:42:00">[16:42:00]</a>. This can be scaled to thousands of calls to generate qualified leads <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>.
*   **Data Arbitrage**: Voice AI agents are excellent for acquiring data that provides an "unfair advantage" in a market <a class="yt-timestamp" data-t="17:32:00">[17:32:00]</a>. The watch lowballing example itself demonstrates how data (e.g., knowing where to buy a watch for $19,000 and sell it for $22,000) can enable an arbitrage business at scale <a class="yt-timestamp" data-t="17:42:00">[17:42:00]</a>. If knowledge provides a competitive edge, there's likely a voice AI opportunity <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>.
*   **Automated Feedback Collection**: A voice AI can collect feedback from users (e.g., members leaving a community) by allowing them to simply "brain dump" their thoughts over the phone <a class="yt-timestamp" data-t="20:24:00">[20:24:00]</a>. This feedback can then be categorized, classified, and used to improve services <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>.

> [!example] Startup Empire's Feedback Bot
> As an example of automated feedback collection, Startup Empire (a private membership for building cash-flowing internet businesses) uses a voice AI <a class="yt-timestamp" data-t="21:04:00">[21:04:00]</a>. Members can call a number, express their likes or dislikes about the community, and the AI (likely in conjunction with Lindy) processes this feedback, summarizes it, and posts it to a Slack channel. This allows the team to receive actionable feedback directly and continuously, improving the product <a class="yt-timestamp" data-t="21:13:00">[21:13:00]</a>.
>
> This particular implementation also represents a potential business idea: offering such automated feedback services to other companies, which would likely be willing to pay for the convenience and insights <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>.