---
title: Automation tools for phonebased work
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Phone-based work is increasingly susceptible to automation, with predictions suggesting that any work currently done over the phone could be automated within the next one to three years <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This automation offers significant opportunities for efficiency and new business models, particularly in data collection and arbitrage.

## Case Study: The Lowballer 9000 Voice AI

Tony, an automation expert from SA Checkout, created a voice AI named "Lowballer 9000" (also known as Alex) <a class="yt-timestamp" data-t="01:28:00">[01:28:00]</a>. This AI was designed to lowball luxury watch dealers across the U.S. for a Rolex Daytona, a watch valued at around $35,000 <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The experiment successfully yielded an actual offer <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.

The AI's primary job was to find a Rolex Daytona by calling secondhand luxury watch dealers, not official Rolex factory dealers <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. Alex needed to gather critical details during conversations, such as:
*   The watch's condition <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>
*   Availability of original documentation and packaging <a class="yt-timestamp" data-t="02:01:00">[02:01:00]</a>

These details are crucial as they can significantly impact the quoted cost of the watch <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.

## Core Tool: Vapi (Voice API)

The platform used for building the Lowballer 9000 was Vapi (Vapi.u), which stands for Voice API <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. Vapi offers a flexible way to build voice agents, allowing users to bring their own prompts and select their preferred service providers without proprietary lock-ins <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

### Prompt Engineering and Best Practices

Developing an effective prompt for a voice AI involves an iterative process:
*   **Initial Draft**: The prompt for Alex was largely self-written, incorporating general best practices from Vapi's documentation <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.
*   **Iterative Refinement**: A significant part of prompt development involves reacting to test calls. By simulating conversations and observing the AI's responses, "holes" in the prompt can be patched <a class="yt-timestamp" data-t="03:45:00">[03:45:00]</a>. For instance, an initial issue was Alex "ramming every single question down my throat" at the start of a call, which made it sound unnatural <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a>. This was addressed by instructing the AI to "keep responses concise. One to two sentences max" <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
*   **Readability Level**: A general learning is that most human conversations happen at a "sixth-grade English level" <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>. Changing the prompt to use this simpler language significantly increased call durations and made the AI sound more human <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

### Model and Voice Selection

*   **Model Choice**: The choice of AI model (e.g., Gemini 20 Flash) is dependent on the desired "flavor of the month" <a class="yt-timestamp" data-t="06:01:00">[06:01:00]</a>. Early use of DeepSeek saved money, but its subsequent hype cycle led to API slamming, causing the bot to crash or not respond <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>. It's crucial to pick a model that is available and reliable <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.
*   **Temperature Setting**: This parameter controls how creative the AI's responses are <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. A temperature closer to zero results in a more deterministic and predictable system, but it may struggle with uncommon questions. A higher temperature allows for more creative responses to varied inputs <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.
*   **Voice Configuration**: Vapi allows users to select specific voices. For Lowballer 9000, "Cartisia" or "New York man" was chosen, humorously implying a "Soprano's voice" <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.

### Advanced Features: Tool Calls and Integrations

The true power of voice AIs lies in their ability to interact with existing tools through "tool calls" <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.

*   **Call Logging and Analysis**: To manage over 800 calls, a tool call was created to record conversations and analyze transcripts in a database (like Airtable) <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a>. This tool automatically determined if an offer was received, the lowball amount, whether it was accepted, and if a final price was given <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>. This process significantly streamlined the identification of actionable calls for content creation <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.
*   **Integration with Lindy**: Lindy excels at flexibly taking large amounts of text and organizing it into spreadsheets <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. For example, if a spreadsheet column like "vegan friendly" is added during research, Lindy can automatically read the column name, process content (like a website scrape or menu), and check the box without requiring manual rule writing or logging back into an automation <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>. This integration between Vapi and Lindy allows for seamless data processing and categorization.

### Technical Requirement: Twilio and KYC

A significant hurdle in implementing voice AI for outbound calls is ensuring calls actually ring through <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.
*   **Twilio**: This service is essential for managing phone numbers and calls <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.
*   **Shake and Stir (FCC Rule)**: The FCC's "Shake and Stir" mechanism requires phone numbers to be registered in their database for KYC (Know Your Customer) purposes <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. Failing to register a number means calls will likely go straight to voicemail. It's crucial to bring your own registered number and complete KYC before placing calls; otherwise, hundreds of calls may be wasted <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>.

## Use Cases for Voice AI Automation

[[AI tools and productivity enhancement | Voice AI agents]] are excellent for gathering data, providing an unfair advantage, and identifying arbitrage opportunities <a class="yt-timestamp" data-t="17:32:00">[17:32:00]</a>.

Potential use cases include:

*   **Sales Prospecting**: Automating calls for real estate agents to ask qualifying questions about potential property listings. An AI can call thousands of numbers, identify individuals who meet specific criteria (e.g., house likely to go on market), and then hand off these qualified leads for human follow-up <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>.
*   **Arbitrage Businesses**: Similar to the Rolex Daytona example, [[AI tools for validating and developing startup ideas | voice AIs]] can be used to gather data that reveals price discrepancies in markets, enabling arbitrage. For instance, buying a watch for $19,000 and selling it for $22,000, then scaling this process <a class="yt-timestamp" data-t="19:06:00">[19:06:00]</a>. The framework for identifying such opportunities is to ask: "What businesses exist where gaining data provides an unfair advantage or knowledge over competitors?" <a class="yt-timestamp" data-t="17:55:00">[17:55:00]</a>.
*   **Customer Feedback Collection**: Voice AIs can collect feedback from users who prefer to "brain dump" verbally rather than filling out forms <a class="yt-timestamp" data-t="20:32:00">[20:32:00]</a>. For example, a "feedback bot" used within Startup Empire allows members to call a number, share their thoughts, and have the AI categorize and summarize the feedback, which is then posted to a Slack channel <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>. This allows product teams to receive categorized feedback directly and efficiently, improving service <a class="yt-timestamp" data-t="21:00:00">[21:00:00]</a>. This type of service could also be offered to other companies <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>.

If data or knowledge provides an unfair advantage, there is likely a voice AI opportunity to exploit <a class="yt-timestamp" data-t="18:21:00">[18:21:00]</a>.