---
title: Applications of AI in Datadriven Business Models
videoId: MAFHmyURRXo
---

From: [[gregisenberg]] <br/> 

Voice AI, specifically voice agents, are capable of automating tasks typically done over the phone, with potential for widespread adoption within 1 to 3 years <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>. This technology can be leveraged to create [[automating_business_processes_with_ai | automated business processes]] and [[impact_of_ai_on_business_efficiency | improve business efficiency]] by gathering specific data for strategic advantages <a class="yt-timestamp" data-t="01:32:32">[01:32:32]</a>.

## Case Study: "Lowballer 9000" Voice AI

Tony, an automation expert, developed a voice AI named "Lowballer 9000" (also known as Alex) to negotiate prices for Rolex Daytonas with secondhand luxury watch dealers across the U.S. <a class="yt-timestamp" data-t="00:00:10">[00:00:10]</a>. This AI aimed to acquire a $35,000 watch at a low price <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>.

### Purpose and Functionality
The primary job of "Lowballer 9000" was to seek out a Rolex Daytona from luxury watch dealers <a class="yt-timestamp" data-t="01:44:00">[01:44:00]</a>. It was programmed to:
*   Gather critical details like the watch's condition, original documentation, and packaging <a class="yt-timestamp" data-t="01:56:00">[01:56:00]</a>.
*   Understand that these details dramatically impact the quoted cost <a class="yt-timestamp" data-t="02:09:00">[02:09:00]</a>.
*   Target secondhand dealers rather than official Rolex stores <a class="yt-timestamp" data-t="02:26:00">[02:26:00]</a>.

### Tools Used
*   **Vapi (Voice API)**: The core platform used to build flexible voice agents. It allows users to bring their own prompts and select different service providers <a class="yt-timestamp" data-t="02:49:00">[02:49:00]</a>.
*   **AI Models**:
    *   **DeepSeek**: Initially used for its cost-effectiveness, but experienced outages due to high demand, causing the bot to crash or not respond <a class="yt-timestamp" data-t="06:21:00">[06:21:00]</a>.
    *   **Gemini 20 Flash**: Used as an alternative model <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>.
*   **Voice Configuration**: The "Cartisia" voice, also referred to as "New York man" or "Soprano's voice," was chosen to give the AI a specific persona <a class="yt-timestamp" data-t="09:06:00">[09:06:00]</a>.
*   **Airtable**: Used as a database to record and track every call placed by the AI. This allowed for easy sifting of over 800 calls to identify actionable offers <a class="yt-timestamp" data-t="10:31:00">[10:31:00]</a>.
*   **Lindy**: A tool for flexibly taking large amounts of text and organizing it into spreadsheets <a class="yt-timestamp" data-t="12:47:00">[12:47:00]</a>. It can automatically categorize information based on column names (e.g., "vegan friendly" for restaurants) <a class="yt-timestamp" data-t="13:52:00">[13:52:00]</a>.
*   **Twilio**: Used for placing calls. A crucial aspect is adhering to "Shake and Stir" FCC regulations, which require registering phone numbers in a database to avoid calls going straight to voicemail <a class="yt-timestamp" data-t="14:53:00">[14:53:00]</a>.

### Prompt Engineering Strategies
The prompt for the AI was developed through iterative testing and observation of real-life lowballing conversations <a class="yt-timestamp" data-t="03:42:00">[03:42:00]</a>. Key strategies for [[business_applications_of_ai_prompting | business applications of AI prompting]] included:
*   **Conciseness**: Instructing the AI to keep responses concise, typically one to two sentences max, to avoid overwhelming the recipient and making the AI's nature obvious <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
*   **Simplicity**: Using "sixth-grade English" in the prompt led to longer call durations and more human-sounding interactions, as most phone conversations occur at this level <a class="yt-timestamp" data-t="05:30:00">[05:30:00]</a>.
*   **Temperature Setting**: A temperature of "one" was used to allow for more creative responses, preventing the AI from failing to respond to uncommon questions, which can happen with lower (closer to zero) temperature settings <a class="yt-timestamp" data-t="08:24:00">[08:24:00]</a>.

### Integrating with External Systems (Tool Calls)
A powerful feature of Vapi is its "tool calls," which allow the voice AI to interact with existing tools <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>. For example, a tool call was created to process the entire transcript of a conversation once it was finished <a class="yt-timestamp" data-t="10:58:00">[10:58:00]</a>. This tool would then determine:
*   If an offer was received <a class="yt-timestamp" data-t="11:07:00">[11:07:00]</a>.
*   If the bot lowballed the dealer and by how much <a class="yt-timestamp" data-t="11:13:00">[11:13:00]</a>.
*   If the lowball offer was accepted or if a counter-price was given <a class="yt-timestamp" data-t="11:18:00">[11:18:00]</a>.
This integration allowed for automated tracking of actionable calls, saving significant time in sifting through data <a class="yt-timestamp" data-t="11:46:00">[11:46:00]</a>.

## Broader Applications and Business Ideas
The successful deployment of voice AI in the watch lowballing scenario highlights its potential for broader [[use_cases_for_ai_agents_in_business_operations | use cases for AI agents in business operations]] and [[using_ai_tools_for_business_growth | business growth]].

### Sales Automation
Voice AI can significantly impact sales by [[automating_business_processes_with_ai | automating business processes]] like prospecting. For instance, in real estate, an AI can call potential leads to determine if a property might soon enter the market by asking specific questions <a class="yt-timestamp" data-t="16:20:00">[16:20:00]</a>. This allows for high-volume outreach (e.g., calling 30,000 numbers) to identify qualified leads for human follow-up <a class="yt-timestamp" data-t="16:59:00">[16:59:00]</a>.

### Data-driven Arbitrage
Voice AI agents are excellent for acquiring data, which can provide an "unfair advantage" in business <a class="yt-timestamp" data-t="17:32:00">[17:32:00]</a>. If knowing more than competitors is a key advantage, then there's likely a voice AI opportunity <a class="yt-timestamp" data-t="18:28:00">[18:28:00]</a>. The watch lowballing example itself demonstrates how AI can [[using_ai_to_analyze_trends_and_generate_business_concepts | analyze trends and generate business concepts]] by creating an arbitrage business model: buying a watch at a low price identified by the AI and selling it at a higher secondary market price <a class="yt-timestamp" data-t="17:45:00">[17:45:00]</a>. This can be scaled further by automating team dispatches to pick up items when offers are accepted <a class="yt-timestamp" data-t="19:25:00">[19:25:00]</a>.

### Automated Customer Feedback
Voice AI can also be used to collect customer feedback <a class="yt-timestamp" data-t="20:27:00">[20:27:00]</a>. Instead of filling out forms, users can simply call a number and brain dump their thoughts. The AI can listen, categorize, and classify this information, and even post summaries to platforms like Slack, providing valuable insights to improve services <a class="yt-timestamp" data-t="20:48:00">[20:48:00]</a>. This demonstrates how AI can streamline internal operations and enhance customer service, which could be offered as a service to other companies <a class="yt-timestamp" data-t="22:04:00">[22:04:00]</a>.

## Key Takeaways for AI Implementation
*   **Automation Potential**: Voice AI can automate any work done over the phone <a class="yt-timestamp" data-t="01:00:00">[01:00:00]</a>.
*   **Strategic Data Collection**: AI is a powerful tool for gathering data that creates an arbitrage opportunity or an unfair advantage <a class="yt-timestamp" data-t="17:32:00">[17:32:00]</a>.
*   **Prompt Refinement**: Prompts should be concise and use simple language for optimal AI performance <a class="yt-timestamp" data-t="04:43:00">[04:43:00]</a>.
*   **Model Selection**: The choice of AI model can depend on current trends and availability; be mindful of potential API slowness during hype cycles <a class="yt-timestamp" data-t="06:12:00">[06:12:00]</a>.
*   **Tool Integration**: Connecting voice AI with external tools (like databases and text processors) dramatically increases its utility and automation capabilities <a class="yt-timestamp" data-t="10:09:00">[10:09:00]</a>.
*   **Regulatory Compliance**: Ensure compliance with telecommunication regulations (e.g., FCC's Shake and Stir) when placing calls to avoid issues like calls going straight to voicemail <a class="yt-timestamp" data-t="15:07:00">[15:07:00]</a>.