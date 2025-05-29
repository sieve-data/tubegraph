---
title: Building voice AI agents with Vappy
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

[[Voice AI applications in startups | Voice AI]] is rapidly advancing, with capabilities that could automate phone-based work within 1 to 3 years <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. Vappy is a platform that allows users to build flexible voice agents without being locked into proprietary systems <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

## Case Study: Lowballer 9000
Tony, an automation expert, developed a voice AI named "Lowballer 9000" (also called Alex) <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. Its purpose was to call luxury secondhand watch dealers across the US and lowball them for Rolex Daytonas, a watch valued at around $35,000 <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>.

The AI's primary job was to:
*   Look for a Rolex Daytona <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>.
*   Gather critical details about the watch, such as its condition and whether it had original documentation and packaging, which can significantly impact the price <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.
*   Target secondhand dealers, not official Rolex factory dealers <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

## Vappy: The Platform for Voice Agents
Vappy, short for Voice API, provides a flexible environment for [[building apps using ai_tools | building voice agents]] <a class="yt-timestamp" data-t="02:52:00">[02:52:00]</a>. Users can bring their own prompts, select their preferred service providers, and run the agent <a class="yt-timestamp" data-t="03:00:00">[03:00:00]</a>.

### Prompt Engineering
The process of creating effective prompts for Vappy involves iterative refinement based on testing <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Tony's approach involved:
*   **Observation**: Watching how human watch sellers lowball in real life <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.
*   **Simulation & Refinement**: Simulating those conversations with the AI and adjusting the prompt when the AI responded inappropriately <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>. For example, to prevent the AI from asking too many questions at once, the prompt was set to keep responses concise (one to two sentences maximum) <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
*   **Language Level**: A key learning was that most conversations occur at a "sixth-grade English level" <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>. Adjusting the prompt to use simple language led to longer call durations and more human-like interactions <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

### Model Selection
The choice of AI model (e.g., Gemini 20 Flash) depends on the specific needs, but the "model game" is often dictated by current trends <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. Tony initially used DeepSeek, but its API became overloaded during a hype cycle, causing the bot to crash or not respond to calls <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>. It's important to pick a model that is available and reliable <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.

*   **Temperature Setting**: This setting controls the creativity of the AI's responses <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. A temperature closer to zero results in a more deterministic system, but it may struggle with uncommon questions <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.

### Voice Configuration
Vappy allows users to select a specific voice for their AI agent <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>. For the Lowballer 9000, the "Cartisia" voice was chosen, which is described as a "New York man" or "Sopranos-like" voice <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

## Tool Calls and Integrations
The most powerful aspect of Vappy is its ability to interact with existing tools through "tool calls" <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.

*   **Call Recording and Data Logging**: Tony integrated Vappy with an AirTable spreadsheet (his "watch list") to record and categorize calls <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>. After each conversation, a tool call would process the transcript to determine if an offer was received, how much the item was lowballed for, and if the lowball was accepted or a counter-offer was given <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>. This system efficiently filtered actionable calls from over 800 total calls <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.
*   **Lindy Integration**: Lindy is an AI tool adept at flexibly taking large amounts of text and organizing it into spreadsheets <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>. It can automatically categorize information based on column names (e.g., "vegan friendly") without needing manual rule creation or re-logging <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>. This capability could be combined with Vappy for advanced data processing.
*   **Twilio for Phone Calls**: To ensure calls actually ring phones and don't go straight to voicemail, it's crucial to use Twilio and register the phone number in a database to comply with FCC mechanisms like STIR/SHAKEN <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>. Tony noted that 300 of his initial calls went to voicemail due to not adhering to KYC (Know Your Customer) requirements <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.

## Use Cases and Business Opportunities
Voice AI agents offer significant potential for various applications and can be used to gain an unfair advantage through data collection <a class="yt-timestamp" data-t="17:36:00">[17:36:00]</a>.

*   **Sales and Lead Qualification**: Automating calls to prospect lists to gather key information (e.g., in real estate, identifying homes likely to go on the market) <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>. This allows businesses to qualify thousands of leads and pursue those meeting specific criteria <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>.
*   **Arbitrage Businesses**: By collecting data on pricing discrepancies, voice AIs can facilitate arbitrage opportunities <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a>. For example, buying a watch low from one person and selling it higher on a secondary market <a class="yt-timestamp" data-t="19:09:00">[19:09:00]</a>. This process can be scaled and further automated <a class="yt-timestamp" data-t="19:21:00">[19:21:00]</a>.
*   **Customer Feedback Collection**: Voice AIs can be used to collect feedback from customers, allowing them to "brain dump" without filling out forms <a class="yt-timestamp" data-t="20:24:00">[20:24:00]</a>. The collected information can then be categorized, classified, and summarized (e.g., posting to Slack channels via Lindy) to improve services <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>. This provides a constant feed of actionable insights directly to relevant teams <a class="yt-timestamp" data-t="21:49:00">[21:49:00]</a>. Such a service could be offered to other companies <a class="yt-timestamp" data-t="22:05:00">[22:05:00]</a>.
*   **General Principle**: If data or knowledge provides an unfair advantage over competitors, there's likely a [[voice_ai_in_business_negotiations | voice AI opportunity]] <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>. This allows for the creation of more transparent secondary markets <a class="yt-timestamp" data-t="18:49:00">[18:49:00]</a>.