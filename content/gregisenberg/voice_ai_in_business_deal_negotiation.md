---
title: Voice AI in business deal negotiation
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Tony, an automation expert from SA Checkout, shared insights into the capabilities of voice AIs, specifically detailing his experience using a voice AI dubbed "Lowballer 9000" to negotiate deals for Rolex Daytonas [00:00:08]. He believes that any work currently done over the phone could be automated within the next one to three years [00:01:00].

## The Lowballer 9000 AI

The "Lowballer 9000" AI, named Alex, was designed to find and negotiate the purchase of Rolex Daytonas from secondhand luxury watch dealers across the U.S. [00:01:10]. Its primary objective was to lowball these dealers [00:00:12].

### Key Information Gathering
Alex's role involves gathering critical details during conversations, such as:
*   The condition of the watch [00:01:57].
*   Whether all original documentation and packaging are available [00:02:01]. These details significantly impact the watch's quoted cost [00:02:09].

The AI targets secondhand dealers, not official Rolex factory dealers [00:02:26].

## Tools and Workflow

### Vappy: The Voice Agent Platform
The core platform used for this voice AI was Vappy, which essentially stands for Voice API [00:02:47]. Vappy offers a flexible way to build voice agents, allowing users to "bring their prompt, pick their providers for different services, and then literally hit go and run it" [00:03:00].

### [[prompt_engineering_for_voice_ai | Prompt Engineering]]
The AI's prompt was primarily written by Tony himself, though Vappy's documentation provided general best practices [00:03:22]. The development of the prompt was an iterative process, involving observing real-life lowballing techniques by content creators and then refining the AI's responses based on testing [00:03:42]. For example, an early issue was the AI "ramming every single question...down my throat" [00:04:17], which was addressed by telling it to "keep responses concise. One to two sentences max" [00:04:43].

A significant learning in [[prompt_engineering_for_voice_ai | prompt engineering]] for voice AIs is that most phone conversations occur at approximately a sixth-grade English level [00:05:27]. Adjusting the prompt to use simpler language led to significantly longer call durations and more human-like interactions [00:05:47].

### Model Selection
The choice of AI model (e.g., Gemini 20 Flash) is often dependent on current trends, described as "flavor of the month" [00:06:18]. Tony initially used DeepSeek due to its cost-effectiveness, but its subsequent surge in popularity led to API saturation, causing the bot to crash and fail to respond during calls [00:06:21]. It's crucial to select a model that is consistently available [00:08:15].

### Temperature Setting
"Temperature" in this context refers to how creative the AI's responses should be [00:08:24]. A temperature closer to zero results in a more predictable, deterministic system [00:08:29]. However, this can lead to the AI not knowing how to respond to uncommon questions, resulting in inappropriate answers [00:08:41].

### Voice Configuration
The specific voice used for Alex was "Cartisia," also referred to as "New York man," hinting at a character from a popular TV show [00:09:12].

### Tool Calls and Data Management
A powerful feature of Vappy is its "tool calls," which allow the voice AI to interact with existing external tools [00:10:09]. For this project, a tool call was set up to record and analyze every call in a database (an AirTable spreadsheet dubbed "watch list") [00:10:26].

The AI would automatically:
*   Record the entire transcript of a conversation [00:11:00].
*   Determine if an offer was received [00:11:07].
*   Assess if the bot successfully lowballed the dealer [00:11:13].
*   Track if the lowball offer was accepted or if a different price was given [00:11:18].

This automation significantly streamlined the process of sifting through over 800 calls to identify actionable offers for content creation [00:11:40].

### Lindy Integration
Lindy, another AI tool, is particularly adept at flexibly processing large amounts of text and organizing it into spreadsheets [00:12:47]. It can automatically infer and populate new columns in a spreadsheet based on content, eliminating the need for manual rule adjustments or re-logging into automation tools [00:13:52]. This integration makes it possible to combine Vappy's voice agent capabilities with Lindy's data processing for enhanced automation [00:14:24].

### [[challenges_and_solutions_in_implementing_voice_ai | Challenges and Solutions in Implementing Voice AI]]
A significant hurdle encountered was ensuring calls actually rang the phones of recipients instead of going straight to voicemail [00:14:57]. This was due to "Shake and Stir," an FCC mechanism requiring phone numbers to be registered in a database for Know Your Customer (KYC) verification [00:15:07]. Failing to register resulted in calls being sent directly to voicemail; Tony experienced at least 300 calls going unanswered due to this [00:15:39]. Therefore, bringing your own registered number and completing KYC is essential for call reliability [00:15:32].

## Business Opportunities with Voice AI

Tony highlights the vast potential of voice AIs beyond simple demos, particularly for startup founders and entrepreneurs looking to [[business_opportunities_with_ai | make money online]]. He argues that any work involving phone communication is ripe for automation [00:01:00].

### [[examples_of_ai_applications_in_business | Sales and Prospecting]]
A clear application is in sales, such as real estate [00:16:20]. A voice AI can call prospects, ask targeted questions (e.g., about family status or property market intentions), and collect data to identify leads with a high likelihood of selling their home [00:16:33]. This allows for scaling prospecting efforts by calling thousands of numbers and identifying qualified leads [00:16:59].

### Data-Driven Arbitrage
Voice AI agents are excellent for acquiring data, which can provide an "unfair advantage" in business [00:17:32]. The Rolex example demonstrates how collecting pricing data can enable an arbitrage business model, buying watches at a lower price and selling them higher [00:17:45]. The key is to identify businesses where "data is an unfair advantage" or "knowledge is an unfair advantage," as these present voice AI opportunities [00:18:24]. This approach can create a more transparent secondary market in various industries [00:18:49].

### [[automating_business_processes_with_ai | Automating Business Processes]]
Voice AIs can also be used for internal business processes, such as collecting feedback [00:20:20]. For instance, a voice AI can listen to users "brain dump" their feedback (positive or negative) without needing to fill out forms, categorize the information, and send summaries to relevant internal channels (e.2.g., Slack) [00:20:47]. This allows businesses to receive continuous, unfiltered feedback directly [00:21:49]. This type of service could be offered to other companies as a product [00:22:04].

> "Any work that you do that's over the phone could and may get automated in the next 1 to 3 years." <a class="yt-timestamp" data-t="01:00">[01:00]</a>