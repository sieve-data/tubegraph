---
title: Negotiation strategies using AI
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AIs are capable of automating work done over the phone, potentially revolutionizing various industries within the next 1 to 3 years <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This article explores how AI can be leveraged for negotiation and data acquisition, using the example of "Lowballer 9000," a voice AI designed to negotiate the purchase of luxury watches.

## The Lowballer 9000 Project

Tony, an automation expert, created a voice AI named "Alex," or "Lowballer 9000," to lowball luxury watch dealers in the US for Rolex Daytonas, which are valued at $35,000 <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a> <a class="yt-timestamp" data-t="01:16:00">[01:16:00]</a>. The AI successfully secured actual offers <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a>.

### AI's Objectives
Alex's primary job is to find a Rolex Daytona by calling secondhand luxury watch dealers, not official Rolex factories <a class="yt-timestamp" data-t="02:20:00">[02:20:00]</a> <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>. It needs to gather critical details to impact the watch's quoted cost, such as:
*   The condition of the watch <a class="yt-timestamp" data-t="01:57:00">[01:57:00]</a>
*   Possession of original documentation and packaging <a class="yt-timestamp" data-t="02:04:00">[02:04:00]</a>

## Building the Voice AI

### Choosing a Platform: Vapi
The project utilized Vapi (Voice API), a flexible platform for building voice agents that does not lock users into proprietary systems <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a> <a class="yt-timestamp" data-t="02:57:00">[02:57:00]</a>. Users can bring their own prompts and select providers for different services <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

### Prompt Engineering and Refinement
The AI's prompt was primarily written by hand, but also informed by Vapi's best practices documentation <a class="yt-timestamp" data-t="03:26:00">[03:26:00]</a> <a class="yt-timestamp" data-t="03:32:00">[03:32:00]</a>. The process involved:
1.  **Observation**: Watching real-life lowballing conversations with watch sellers <a class="yt-timestamp" data-t="03:53:00">[03:53:00]</a>.
2.  **Simulation**: Simulating these conversations with Alex via Vapi <a class="yt-timestamp" data-t="04:02:00">[04:02:00]</a>.
3.  **Iteration**: Adjusting the prompt based on undesirable AI responses, akin to "patching holes" in a sinking boat <a class="yt-timestamp" data-t="04:10:00">[04:10:00]</a> <a class="yt-timestamp" data-t="04:54:00">[04:54:00]</a>.
    *   **Conciseness**: Ensuring responses were concise (1-2 sentences maximum) to prevent the AI from "ramming every single question down [the user's] throat" and sounding less engaging <a class="yt-timestamp" data-t="04:17:00">[04:17:00]</a> <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
    *   **Simplicity**: Using "sixth-grade English" in the prompt led to significantly longer call durations and more human-sounding interactions <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a> <a class="yt-timestamp" data-t="05:47:00">[05:47:00]</a>.

### Model Selection and Voice Configuration
*   **Model**: The choice of AI model (e.g., Gemini 2.0 Flash) is often dependent on current trends. DeepSeek was initially used but faced performance issues due to high demand, leading to calls not being responded to <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a> <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a> <a class="yt-timestamp" data-t="08:09:00">[08:09:00]</a>. It's crucial to pick a model that is available and reliable <a class="yt-timestamp" data-t="08:15:00">[08:15:00]</a>.
*   **Temperature**: This setting controls the creativity of the AI's responses <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>. A temperature closer to zero yields more predictable, deterministic responses, but the AI might struggle with uncommon questions <a class="yt-timestamp" data-t="08:29:00">[08:29:00]</a>.
*   **Voice**: The specific voice used for Alex was "Cartesia," described as a "New York man" voice, reminiscent of a popular fictional character <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a> <a class="yt-timestamp" data-t="09:19:00">[09:19:00]</a>.

### [[utilizing_ai_tools_for_efficient_content_strategy | Tool Calls]] for Data Management
One of Vapi's most powerful features is its ability to interact with existing tools through "tool calls" <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a> <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.
*   **Call Recording and Analysis**: A tool call was set up to record all calls and, after each conversation, analyze the transcript to determine if an offer was received, the lowball amount, and if the lowball was accepted or a counter-offer was given <a class="yt-timestamp" data-t="10:24:00">[10:24:00]</a> <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>.
*   **Database Integration**: This data was fed into an AirTable spreadsheet (watch list) to efficiently sift through over 800 calls and identify actionable outcomes, making it easy to find calls that resulted in content for videos <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a> <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a> <a class="yt-timestamp" data-t="11:50:00">[11:50:00]</a>.

### Integration with Lindy
Lindy excels at flexibly processing large amounts of text and organizing it into spreadsheets <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a> <a class="yt-timestamp" data-t="12:59:00">[12:59:00]</a>. For example, if adding a new column like "vegan friendly" to a restaurant spreadsheet, Lindy can automatically read the column name, analyze website scrapes or menus, and check the appropriate boxes without manual rule writing or logging back in <a class="yt-timestamp" data-t="13:32:00">[13:32:00]</a> <a class="yt-timestamp" data-t="14:14:00">[14:14:00]</a>.

## Technical Hurdle: Call Delivery
A significant challenge was ensuring calls actually rang phones instead of going straight to voicemail <a class="yt-timestamp" data-t="14:57:00">[14:57:00]</a>. This is due to an FCC mechanism called "Shake and Stir," which requires phone numbers to be registered in a database for KYC (Know Your Customer) purposes <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. Without proper registration and KYC, calls may not be honored <a class="yt-timestamp" data-t="15:20:00">[15:20:00]</a>. Hundreds of calls went to voicemail before this issue was addressed <a class="yt-timestamp" data-t="15:39:00">[15:39:00]</a>.

## Broader Use Cases for Voice AI
Voice AI has potential beyond just negotiating luxury watch prices. It can automate any phone-based work and provide an unfair advantage through data collection.

### Sales and Prospecting
*   **Real Estate**: Voice AI can call prospect lists to gather information, such as whether a family member recently passed or if a house is about to go on the market <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>. By asking specific questions, the AI can identify leads with a higher probability of putting their house on the market, then pass these qualified leads to human agents for follow-up <a class="yt-timestamp" data-t="16:33:00">[16:33:00]</a> <a class="yt-timestamp" data-t="17:01:00">[17:01:00]</a>. This is an example of [[utilizing_ai_for_automation_and_scalability | automation and scalability]].

### Data for [[using_ai_for_business_efficiency_and_expansion | Arbitrage Opportunities]]
A core framework for using voice AI is to acquire data that creates an unfair advantage <a class="yt-timestamp" data-t="17:34:00">[17:34:00]</a>.
*   **Secondary Markets**: Just as the watch project demonstrated, voice AI can identify arbitrage opportunities by finding items at low prices and selling them for a profit in a secondary market <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a> <a class="yt-timestamp" data-t="19:08:00">[19:08:00]</a>. If data or knowledge provides a competitive edge, there is likely a voice AI opportunity <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>.
*   **Market Transparency**: Voice AI can contribute to creating more transparent secondary markets <a class="yt-timestamp" data-t="18:47:00">[18:47:00]</a>.

### [[improving_customer_interactions_with_ai | Improving Customer Interactions]]: The Feedback Bot
Tony also developed a voice AI feedback bot for Startup Empire, a private membership for building cash-flowing internet businesses <a class="yt-timestamp" data-t="20:24:00">[20:24:00]</a> <a class="yt-timestamp" data-t="21:04:00">[21:04:00]</a>.
*   **Overcoming Feedback Form Fatigue**: The bot addresses the common dislike of filling out lengthy feedback forms <a class="yt-timestamp" data-t="20:32:00">[20:32:00]</a>.
*   **Brain Dump Mechanism**: Users can call a number and "brain dump" their feedback, whether positive or negative, into the AI <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a> <a class="yt-timestamp" data-t="21:28:00">[21:28:00]</a>.
*   **Automated Summarization**: The AI (via Lindy) takes the audio feedback, categorizes and classifies it, and posts summarized feedback directly to a Slack channel for the product team <a class="yt-timestamp" data-t="20:58:00">[20:58:00]</a> <a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>. This provides immediate, organized insights without the need for manual retrieval <a class="yt-timestamp" data-t="21:49:00">[21:49:00]</a>. This automated feedback collection presents a viable business idea for other companies <a class="yt-timestamp" data-t="22:03:00">[22:03:00]</a>.