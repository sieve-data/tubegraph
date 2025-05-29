---
title: Improving AI conversation handling
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AIs are capable of much more than currently understood, with the potential to automate phone-based work within the next one to three years <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>. Effective AI conversation handling relies on careful design, testing, and integration of various tools.

## Case Study: The Lowballer 9000 AI

A voice AI, dubbed "Lowballer 9000" and named Alex, was created to negotiate prices for Rolex Daytonas with secondhand luxury watch dealers across the US <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a> <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. The AI's primary job was to find a Rolex Daytona, specifically targeting secondhand dealers rather than official Rolex stores <a class="yt-timestamp" data-t="00:01:44">[00:01:44]</a> <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

To facilitate negotiations, the AI needed to gather critical details about the watch, such as its condition, and whether all original documentation and packaging were available. These details can significantly impact the watch's quoted cost <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>.

## Tools and Platforms for Voice AI

The project utilized several key tools to enable the voice AI's functionality:

*   **Vapi**: This platform serves as a flexible way to build voice agents, allowing users to "bring their own prompt" and select different service providers <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Vapi does not lock users into proprietary systems <a class="yt-timestamp" data-t="00:02:57">[00:02:57]</a>.
*   **Model Selection**: The choice of AI model is crucial and often depends on current "flavor of the month" trends <a class="yt-timestamp" data-t="00:06:12">[00:06:12]</a>. Initially, DeepSeek was used due to its cost-effectiveness, but its API became overwhelmed during a "hype cycle," causing the bot to crash or fail to respond <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a> <a class="yt-timestamp" data-t="00:08:09">[00:08:09]</a>. It's recommended to pick an available and reliable model <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.
*   **Voice Configuration**: Vapi allows selection of specific voices. For the Lowballer 9000, "Cartisia" or "New York man" was used <a class="yt-timestamp" data-t="00:09:06">[00:09:06]</a>.
*   **Twilio**: This service is essential for enabling calls to actually ring phones. A significant hurdle was navigating the "Shake and Stir" FCC rule, which requires phone numbers to be registered in a database (KYC) to prevent calls from going straight to voicemail <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Hundreds of calls can go to voicemail if KYC is not completed <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>.

## [[Prompting techniques for effective use of AI models | Prompting Techniques]] for Improved Conversation

The core of effective AI conversation handling lies in iterative [[Prompting techniques for effective use of AI models | prompting techniques]]. The prompt for Alex was written by the creator, but also refined through observation and testing <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>.

Key [[Prompting techniques for effective use of AI models | prompting techniques]] include:

*   **Iterative Refinement**: The process involves observing how the AI responds in simulated conversations (e.g., watching human lowballers interact with watch sellers) and then patching "holes" in the prompt when the AI responds in an undesirable way <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Conciseness**: Initially, the AI would "ram every single question down [the user's] throat" <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. The prompt was adjusted to keep responses concise, typically one to two sentences max, to make the AI sound more engaging and less obviously artificial <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This also helps Vapi avoid errors <a class="yt-timestamp" data-t="00:05:05">[00:05:05]</a>.
*   **Simplicity of Language**: Using "sixth-grade English" in the prompt led to significantly longer call durations and a more human-like sound <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.
*   **Temperature Setting**: This setting controls the creativity of the AI's responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. A temperature closer to zero creates a more deterministic, predictable system, but it may struggle with uncommon questions <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>.

## Integration with Other Tools (Tool Calls)

Voice AIs become powerful when they can interact with existing tools <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>. This is achieved through "tool calls," which allow the AI to perform actions or retrieve information outside of its core dialogue.

*   **Call Recording and Data Extraction**: The Lowballer 9000 used a tool call to record all conversations and send the transcripts to a database (an AirTable spreadsheet referred to as a "watch list") <a class="yt-timestamp" data-t="00:10:27">[00:10:27]</a>. Another tool call, "get best offer," processed the entire transcript to determine if an offer was received, how much the item was lowballed for, whether the lowball was accepted, or if another price was given <a class="yt-timestamp" data-t="00:10:58">[00:10:58]</a>. This automated categorization made it easy to sift through over 800 calls and identify actionable leads <a class="yt-timestamp" data-t="00:11:46">[00:11:46]</a>.
*   **Lindy Integration**: Lindy is an AI tool particularly good at flexibly taking large amounts of text and structuring it into a spreadsheet <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. For example, if a spreadsheet column like "vegan friendly" is added, Lindy can automatically read content (e.g., a website scrape or menu) and check the box if relevant, without requiring manual rule writing or logging back in <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>.

## Broader Applications of Voice AI

The capabilities demonstrated by the Lowballer 9000 have wide-ranging applications:

*   **Sales**: Voice AIs can automate prospecting, such as calling real estate leads to gather specific information (e.g., if a house is likely to go on the market soon) <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. This allows businesses to identify qualified leads at scale <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
*   **Data Collection for Arbitrage**: Voice AI is excellent for acquiring data, providing an "unfair advantage" <a class="yt-timestamp" data-t="00:17:32">[00:17:32]</a>. For instance, in the watch example, collecting price data enables an arbitrage business where items can be bought low and sold higher at scale <a class="yt-timestamp" data-t="00:17:42">[00:17:42]</a>. Any business where "knowledge is an unfair advantage" likely has a voice AI opportunity <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.
*   **Customer Feedback**: Voice AIs can be used to collect feedback. For example, a feedback bot for Startup Empire allows members to call a number and "brain dump" their thoughts on the community <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This feedback is then summarized and posted to a Slack channel via Lindy, making it easy for the product team to categorize and use for improvements <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>. This concept could be offered as a service to other companies <a class="yt-timestamp" data-t="00:22:04">[00:22:04]</a>.
*   **Market Transparency**: Voice AI can contribute to creating more transparent secondary markets by efficiently gathering and disseminating price data <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>.