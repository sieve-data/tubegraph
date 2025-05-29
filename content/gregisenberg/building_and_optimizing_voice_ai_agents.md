---
title: Building and optimizing voice AI agents
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Tony, an automation expert with SA Checkout, shares insights into [[tools_and_models_for_voice_automation | building and optimizing voice AI agents]] based on his experience creating a voice AI that successfully lowballed luxury watch dealers for Rolex Daytonas across the US <a class="yt-timestamp" data-t="00:00:00">[00:00:00]</a>. This $35,000 watch pursuit demonstrated the surprising effectiveness of [[voice_ai_in_business_negotiation | voice AI in business negotiation]] <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

## Why Voice AI Matters
There's a belief that people are "drastically underestimating" the capabilities of [[tools_and_models_for_voice_automation | voice AIs]] <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>. Any work conducted over the phone could potentially be automated within the next one to three years <a class="yt-timestamp" data-t="00:01:00">[00:01:00]</a>.

## The "Lowballer 9000" AI: Alex
Tony's voice AI, named "Alex" and affectionately dubbed "Lowballer 9000," was designed for a singular purpose: to find and negotiate the purchase of Rolex Daytonas from secondhand luxury watch dealers <a class="yt-timestamp" data-t="00:01:28">[00:01:28]</a>. This AI was tasked with gathering critical details, such as the watch's condition and the availability of original documentation and packaging, as these factors significantly impact the quoted price <a class="yt-timestamp" data-t="00:01:56">[00:01:56]</a>. The targets were not official Rolex dealers but rather individuals who buy and sell secondhand Rolexes <a class="yt-timestamp" data-t="00:02:26">[00:02:26]</a>.

### Core Tool: Vappy
The platform used for this project is Vappy, which essentially stands for "Voice API" <a class="yt-timestamp" data-t="00:02:49">[00:02:49]</a>. Vappy offers a flexible way to [[building_apps_with_ai_tools | build voice agents]] without locking users into proprietary systems, allowing them to bring their own prompts and choose their service providers <a class="yt-timestamp" data-t="00:02:54">[00:02:54]</a>.

## Optimizing Voice AI Agents
### Prompt Engineering
The prompt for Alex was primarily written by Tony himself, drawing on best practices and iterative testing <a class="yt-timestamp" data-t="00:03:22">[00:03:22]</a>. The process involved:
*   **Observation**: Studying how human lowballers interact with watch sellers in real-life scenarios <a class="yt-timestamp" data-t="00:03:53">[00:03:53]</a>.
*   **Simulation & Refinement**: Simulating these conversations with Alex and then refining the prompt based on undesirable AI responses. For example, initially, Alex would "ram every single question...down my throat," leading to an unengaging and obviously AI-driven interaction <a class="yt-timestamp" data-t="00:04:10">[00:04:10]</a>.
*   **Conciseness**: A key adjustment was to instruct the AI to keep responses concise, "one to two sentences max," preventing it from overwhelming the interlocutor <a class="yt-timestamp" data-t="00:04:43">[00:04:43]</a>.
*   **Language Level**: A significant improvement in call duration and human-like interaction was observed by instructing the prompt to use language at a "sixth-grade English level," as most conversations occur at this level <a class="yt-timestamp" data-t="00:05:30">[00:05:30]</a>.

### Model Selection
The choice of model is often dependent on the "flavor of the month" <a class="yt-timestamp" data-t="00:06:18">[00:06:18]</a>. Tony initially used DeepSeek, which was cost-effective but later experienced crashes and unresponsiveness due to high demand following its hype cycle <a class="yt-timestamp" data-t="00:06:21">[00:06:21]</a>. Currently, Gemini 20 Flash is in use <a class="yt-timestamp" data-t="00:06:04">[00:06:04]</a>. The key takeaway is to select a model that is available and responsive <a class="yt-timestamp" data-t="00:08:15">[00:08:15]</a>.

### Temperature Setting
"Temperature" controls the creativity of the AI's responses <a class="yt-timestamp" data-t="00:08:24">[00:08:24]</a>. A temperature closer to zero results in a more predictable, deterministic system <a class="yt-timestamp" data-t="00:08:29">[00:08:29]</a>. However, a very low temperature can cause the AI to fail to respond appropriately to uncommon questions <a class="yt-timestamp" data-t="00:08:41">[00:08:41]</a>.

### Voice Configuration
The AI's voice was configured using "Cartisia," described as a "New York man" voice, possibly referencing a popular fictional character <a class="yt-timestamp" data-t="00:09:12">[00:09:12]</a>.

### Tool Calls and Integrations
A powerful feature of Vappy is its ability to interact with existing tools through "tool calls" <a class="yt-timestamp" data-t="00:10:09">[00:10:09]</a>.
*   **Database Integration (Airtable)**: Tony integrated Vappy with an Airtable database to record and categorize over 800 calls <a class="yt-timestamp" data-t="00:10:31">[00:10:31]</a>. This allowed the system to automatically identify calls that resulted in actionable offers, saving time from sifting through raw transcripts <a class="yt-timestamp" data-t="00:10:40">[00:10:40]</a>. The tool call was designed to assess if an offer was received, if it was lowballed, whether the lowball was accepted, and if a counter-price was given <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>.
*   **Lindy Integration**: Lindy is beneficial for flexibly processing large amounts of text and populating spreadsheets <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>. It can automatically read column names (e.g., "vegan friendly") and extract relevant information from text (like a website scrape or menu) to populate those columns without requiring manual configuration or rule writing <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. This integration enables sophisticated data collection and organization.

### Call Logistics: Twilio and KYC
A significant hurdle in deploying the voice AI was ensuring calls actually rang through to phones rather than going straight to voicemail <a class="yt-timestamp" data-t="00:14:57">[00:14:57]</a>. This issue is often due to "Shake and Stir," an FCC mechanism that requires phone numbers to be registered in a database for KYC (Know Your Customer) purposes <a class="yt-timestamp" data-t="00:15:07">[00:15:07]</a>. Unregistered numbers will have their calls sent directly to voicemail <a class="yt-timestamp" data-t="00:15:27">[00:15:27]</a>, as Tony experienced with 300 initial calls <a class="yt-timestamp" data-t="00:15:39">[00:15:39]</a>. It's crucial to bring your own number and complete KYC before placing calls <a class="yt-timestamp" data-t="00:15:32">[00:15:32]</a>.

## [[building_successful_ai_apps | Building Successful AI Apps]]: Use Cases and Business Opportunities
Voice AI opens up numerous possibilities for startups and individuals seeking to leverage automation for business <a class="yt-timestamp" data-t="00:16:04">[00:16:04]</a>:

*   **Sales Automation**: Automating initial prospecting calls, such as in real estate, to identify leads based on specific criteria (e.g., family changes, property market status) <a class="yt-timestamp" data-t="00:16:20">[00:16:20]</a>. An AI can quickly qualify thousands of numbers to identify high-potential prospects <a class="yt-timestamp" data-t="00:16:59">[00:16:59]</a>.
*   **[[applications_of_voice_ai_in_sales_and_feedback_collection | Feedback Collection]]**: [[creating_ai_employees_and_agents | Voice AIs]] can serve as feedback bots, allowing users to "brain dump" their thoughts on a service or product <a class="yt-timestamp" data-t="00:20:24">[00:20:24]</a>. This information can then be automatically categorized, classified, and used to improve services <a class="yt-timestamp" data-t="00:20:58">[00:20:58]</a>.
    *   *Example*: Startup Empire, a private membership for [[building_successful_ai_apps | building cash-flowing internet businesses]], uses a [[applications_of_voice_ai_in_sales_and_feedback_collection | voice AI]] to collect feedback from members <a class="yt-timestamp" data-t="00:21:05">[00:21:05]</a>. This feedback is summarized and posted directly to a Slack channel, making it easily accessible for product improvement <a class="yt-timestamp" data-t="00:21:39">[00:21:39]</a>.
*   **Data Arbitrage**: Voice AIs are excellent for gathering data, which can provide an "unfair advantage" in various markets <a class="yt-timestamp" data-t="00:17:34">[00:17:34]</a>.
    *   **Transparent Secondary Markets**: By collecting pricing data, voice AIs can help create more transparent secondary markets <a class="yt-timestamp" data-t="00:18:47">[00:18:47]</a>. This enables arbitrage opportunities, such as buying a watch for $19,000 and reselling it for $22,000 <a class="yt-timestamp" data-t="00:19:10">[00:19:10]</a>.
    *   **Scalability**: The process can be scaled and further automated, allowing for dispatching teams to pick up items once an offer is accepted <a class="yt-timestamp" data-t="00:19:23">[00:19:23]</a>.
*   **Knowledge as Advantage**: If knowledge or data is an unfair advantage in a particular business, then there is likely a [[creating_ai_employees_and_agents | voice AI opportunity]] <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>.

Ultimately, voice AI enables the creation of [[creating_ai_employees_and_agents | AI employees and agents]] capable of executing tasks that traditionally require human interaction over the phone, leading to efficient data collection and new business models.