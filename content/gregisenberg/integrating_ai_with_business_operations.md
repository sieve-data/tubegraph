---
title: Integrating AI with business operations
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Tony, an automation expert from SA Checkout, demonstrates how voice AI can be integrated into business operations, emphasizing its potential for automation and data collection. He predicts that phone-based work could be largely automated within the next 1 to 3 years <a class="yt-timestamp" data-t="01:02:00">[01:02:00]</a>. This represents a significant shift towards [[automating_business_workflows_with_ai | automating business workflows with AI]] and highlights [[the_role_of_ai_in_modern_business_operations | the role of AI in modern business operations]].

## Case Study: "Lowballer 9000" Voice AI

Tony illustrates the power of voice AI through his creation, "Lowballer 9000," an AI he affectionately calls Alex <a class="yt-timestamp" data-t="01:31:00">[01:31:00]</a>.

### Purpose and Functionality
The AI's primary job was to call luxury watch dealers across the US and lowball them for a Rolex Daytona, a watch valued at $35,000 <a class="yt-timestamp" data-t="00:10:00">[00:10:00]</a>. The AI specifically targeted secondhand dealers, not official Rolex outlets <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

Its core tasks included:
*   **Gathering Critical Details:** Inquiring about the watch's condition, original documentation, and packaging, as these details significantly impact the quoted cost <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.
*   **Negotiating:** Attempting to secure the lowest possible price.

### Tools and Development

The "Lowballer 9000" was built using Vappy, a flexible voice API platform that allows users to "bring your prompt, pick your providers for your different services, and then literally hit go and run it" <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>.

#### Vappy Configuration
*   **Prompting:** Tony wrote the prompt himself, iteratively refining it based on testing and observation of real-life lowballing conversations <a class="yt-timestamp" data-t="03:22:00">[03:22:00]</a>. Key prompt refinements included:
    *   Keeping responses concise (one to two sentences max) to improve engagement and sound less like an AI <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
    *   Instructing the AI to use language at a "sixth-grade English level" to increase call durations and sound more human <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
*   **Model Selection:** The choice of AI model (e.g., Gemini 20 Flash, DeepSeek) is dynamic and dependent on current availability and performance. Tony initially used DeepSeek but faced issues due to its popularity leading to API overload <a class="yt-timestamp" data-t="06:07:00">[06:07:00]</a>.
*   **Temperature Setting:** This parameter controls the AI's creativity. A temperature closer to zero results in more deterministic, predictable responses, while a higher setting allows for more varied, though potentially inappropriate, answers to uncommon questions <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.
*   **Voice Configuration:** Tony selected the "Cartisia" voice, which Vappy refers to as "New York man," hinting at a popular fictional character <a class="yt-timestamp" data-t="09:12:00">[09:12:00]</a>.

#### Enhancing Functionality with Tool Calls
A crucial aspect of powerful voice AI is its ability to interact with existing tools via "tool calls" <a class="yt-timestamp" data-t="10:18:00">[10:18:00]</a>.
*   **Data Recording and Analysis:** Tony created a tool call to record and analyze every conversation. This allowed the AI to automatically process transcripts and identify calls that resulted in actionable offers, saving immense manual effort in sifting through over 800 calls <a class="yt-timestamp" data-t="10:40:00">[10:40:00]</a>. This exemplifies [[ai_integration_and_data_handling_in_business | AI integration and data handling in business]].
*   **AirTable Integration:** The "get best offer" tool was configured to communicate with an AirTable spreadsheet, allowing the AI to access the best offers gathered and use them in negotiations <a class="yt-timestamp" data-t="12:05:00">[12:05:00]</a>.

#### Integrating with Other AI Services: Lindy
Lindy, another AI service, is highlighted for its ability to flexibly process large amounts of text and populate spreadsheets <a class="yt-timestamp" data-t="12:50:00">[12:50:00]</a>. It can automatically read column names (e.g., "vegan friendly") and extract relevant information from unstructured text (e.g., a website scrape or menu) to populate those columns, eliminating the need for manual rule writing <a class="yt-timestamp" data-t="13:54:00">[13:54:00]</a>. The synergy between Lindy and Vappy allows for automated data extraction and categorization from voice AI conversations, further enhancing [[automating_business_workflows_with_ai | business workflows]].

#### Technical Considerations: Twilio and FCC Compliance
A significant hurdle in implementing voice AI for outbound calls is ensuring calls ring through. Tony emphasized the importance of Twilio and adhering to the FCC's "Shake and Stir" mechanism <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>. This rule requires phone numbers to be registered (KYC) to prevent calls from going straight to voicemail. Ignoring this can result in many wasted calls, as Tony experienced with 300 calls going to voicemail <a class="yt-timestamp" data-t="15:32:00">[15:32:00]</a>.

## Broader Use Cases and Business Opportunities
Beyond the watch lowballing demo, voice AI presents numerous opportunities for startups and businesses looking to make money online, contributing to [[developing_aiassisted_business_strategies | developing AI-assisted business strategies]].

*   **Sales Automation:** Voice AIs can automate outbound sales calls for tasks like qualifying leads (e.g., in real estate, asking questions to assess property sale likelihood) <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>. This can involve calling thousands of numbers to identify prospects who meet specific criteria, demonstrating [[benefits_of_ai_in_business_efficiency | benefits of AI in business efficiency]].
*   **Data Collection for Arbitrage:** Voice AI is an excellent tool for gathering data to gain an "unfair advantage" <a class="yt-timestamp" data-t="17:32:00">[17:32:00]</a>. This allows for the creation of arbitrage businesses, where knowledge or data leads to profit opportunities. The Rolex example demonstrates this by enabling users to identify watches that can be bought low and sold for a higher price on the secondary market <a class="yt-timestamp" data-t="19:08:00">[19:08:00]</a>.
*   **Automated Feedback Collection:** As implemented within "Startup Empire," a voice AI can collect feedback from users who prefer to "brain dump" rather than fill out forms <a class="yt-timestamp" data-t="20:24:00">[20:24:00]</a>. This raw feedback can then be categorized and summarized (potentially using Lindy) and pushed to internal communication channels (e.g., Slack) for immediate review and service improvement <a class="yt-timestamp" data-t="21:39:00">[21:39:00]</a>. This showcases a clear example of [[integrating_ai_in_existing_app_ideas | integrating AI in existing app ideas]].

Overall, the potential for [[integrating_ai_services_and_apis_in_app_development | integrating AI services and APIs in app development]] and business operations is vast, particularly in areas where data collection and automated communication can create efficiency or arbitrage opportunities.