---
title: Prompt engineering for voice AI
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Prompt engineering for voice AI involves crafting specific instructions and configurations to guide an AI agent's conversational behavior and achieve desired outcomes during phone interactions. It leverages various tools and iterative refinement to create highly effective and specialized AI assistants.

## The "Lowballer 9000" Case Study

Tony, an automation expert, created a voice AI named "Lowballer 9000" to negotiate prices for Rolex Daytona watches with secondhand luxury watch dealers across the US <a class="yt-timestamp" data-t="00:08:00">[00:08:00]</a>. This AI successfully "lowballed" dealers, even for a $35,000 watch <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>, demonstrating the significant potential of voice AI <a class="yt-timestamp" data-t="00:54:00">[00:54:00]</a>. Tony believes that any phone-based work could be automated within 1 to 3 years <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>.

The AI, affectionately dubbed "Alex," was designed with a singular purpose: to find a Rolex Daytona from secondhand luxury watch dealers, not official Rolex factories <a class="yt-timestamp" data-t="01:46:00">[01:46:00]</a>, <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. Key tasks included gathering critical details like watch condition, original documentation, and packaging, as these significantly impact the quoted cost <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.

### Platform: Vappy

The core platform used for this project was Vappy (Voice API) <a class="yt-timestamp" data-t="02:47:00">[02:47:00]</a>. Vappy is a flexible tool that allows users to bring their own prompts and select different service providers for various AI components, making it adaptable for building voice agents <a class="yt-timestamp" data-t="02:54:00">[02:54:00]</a>.

### Prompt Engineering Process

The system prompt for Alex was primarily written by Tony himself, though he also leveraged Vappy's documentation for general best practices <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>.

#### Iterative Refinement

A significant part of the prompt engineering process involved iterative testing and refinement, described as "patching holes" in a sinking boat <a class="yt-timestamp" data-t="04:53:00">[04:53:00]</a>. This involved:
*   Observing human watch sellers in real-life scenarios <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.
*   Simulating these conversations with Alex via Vappy <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
*   Identifying undesirable AI responses (e.g., Alex "ramming every single question down my throat") <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a>.
*   Modifying the prompt to correct the behavior, making interactions more engaging and less "obviously AI" <a class="yt-timestamp" data-t="04:26:00">[04:26:00]</a>.

#### Key Prompt Strategies

*   **Conciseness**: Instructions like "keep responses concise. One to two sentences max" were added to prevent the AI from overwhelming the caller with too much information at once <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>. This also helps reduce errors from the Vappy platform <a class="yt-timestamp" data-t="05:05:00">[05:05:00]</a>.
*   **Language Level**: A crucial learning was that most conversations occur at a "sixth-grade English level" <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>. Adjusting the prompt to use simpler language significantly increased call durations and made the AI sound "so much more human" <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

#### Model and Voice Selection

*   **Model Choice**: The choice of AI model (e.g., Gemini 2.0 Flash) is often dependent on the "flavor of the month" <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>. Tony initially used DeepSeek, but its API became "slammed" during a hype cycle, causing the bot to crash or not respond <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>, <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. The advice is to pick a model that is currently available <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.
*   **Temperature Setting**: This setting controls the AI's creativity <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. A temperature closer to zero results in a more predictable, "deterministic" system <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>. However, a very low temperature might prevent the AI from responding appropriately to uncommon questions <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>.
*   **Voice Configuration**: Vappy allows selection of various popular voices. Tony chose "Cartisia" also known as "New York man," which has a distinctive sound reminiscent of a Soprano's character <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

### Integration with External Tools (Tool Calls)

One of Vappy's most powerful features is "tool calling," which allows the voice AI to interact with existing external tools <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.

*   **Data Collection with AirTable**: Tony used an AirTable spreadsheet as a "watch list" database to record every call placed by the AI <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>. A tool call was created to automatically process the transcript after each conversation and determine if an offer was made, the lowballed amount, and whether the offer was accepted <a class="yt-timestamp" data-t="10:52:00">[10:52:00]</a>. This system makes it easy to filter through hundreds of calls to find actionable outcomes <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.
*   **Data Processing with Lindy**: Lindy is highlighted for its ability to flexibly process large amounts of text and populate spreadsheets <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. For example, if a new column like "vegan friendly" is added to a spreadsheet, Lindy can automatically read website scrapes or menus and check the appropriate box without requiring manual configuration or new rules <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>. This capability could be used with Vappy for various data management tasks <a class="yt-timestamp" data-t="14:24:00">[14:24:00]</a>. Lindy is also used in Startup Empire to summarize and post feedback from voice AI calls to a Slack channel <a class="yt-timestamp" data-t="21:19:00">[21:19:00]</a>.

### Overcoming Technical [[Challenges and solutions in implementing voice AI]]

A significant hurdle encountered was ensuring calls actually rang through to phones rather than going straight to voicemail <a class="yt-timestamp" data-t="15:03:00">[15:03:00]</a>. This is due to an FCC mechanism called SHAKEN/STIR, which requires phone numbers to be registered in a database (Know Your Customer or KYC) <a class="yt-timestamp" data-t="15:07:00">[15:07:07]</a>. Without proper registration via services like Twilio, calls will be sent directly to voicemail <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>. Tony experienced over 300 calls going to voicemail before addressing this <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.

## Broader Implications and Use Cases

Voice AIs are capable of automating any phone-based work <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>, offering significant advantages for various businesses and initiatives. This aligns with the concept of [[ai_automation_for_phonebased_tasks | AI automation for phone-based tasks]].

*   **Sales and Lead Generation**: A prime example is real estate <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>. A voice AI can call prospects and ask specific questions (e.g., about family status or potential market entry) to identify leads with a higher probability of putting a house on the market <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a>. By calling thousands of numbers, the AI can filter and present actionable leads for human follow-up <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>. This demonstrates how AI can assist in [[voice_ai_in_business_deal_negotiation | business deal negotiation]] by automating initial contact and data gathering.

*   **Data-Driven Arbitrage Businesses**: Voice AI agents are excellent for acquiring data that provides an "unfair advantage" <a class="yt-timestamp" data-t="17:32:00">[17:32:00]</a>. The Rolex example itself is an arbitrage business where the AI collects price data to identify opportunities to buy low and sell high, potentially making thousands of dollars at scale <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a>. Businesses where "knowledge is an unfair advantage" are ripe for voice AI opportunities <a class="yt-timestamp" data-t="18:25:00">[18:25:00]</a>. This approach can create a more transparent secondary market for various goods <a class="yt-timestamp" data-t="18:47:00">[18:47:00]</a>.

*   **Customer Feedback and Service**: Voice AIs can collect feedback from users who might otherwise be unwilling to fill out forms <a class="yt-timestamp" data-t="20:27:00">[20:27:00]</a>. For example, a voice AI for "Startup Empire" allows members to "brain dump" their thoughts on the community <a class="yt-timestamp" data-t="20:44:00">[20:44:00]</a>. This unstructured voice data can then be categorized, classified, summarized (e.g., by Lindy), and delivered to relevant channels (like Slack), enabling continuous service improvement <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a>. This showcases potential for [[voicefirst_interfaces_and_advanced_voice_notes | voicefirst interfaces and advanced voice notes]].

These applications highlight the versatility of prompt engineering for voice AI in [[implementing_ai_in_app_development_processes | implementing AI in app development processes]] and [[designing_user_experience_for_ai_apps | designing user experience for AI apps]].