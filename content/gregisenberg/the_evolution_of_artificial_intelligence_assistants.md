---
title: The evolution of artificial intelligence assistants
videoId: 7j_NE6Pjv-E
---

From: [[gregisenberg]] <br/> 

The field of artificial intelligence (AI), particularly with the advent of large language models (LLMs), has seen rapid evolution in how AI assistants are developed and integrated with external capabilities <a class="yt-timestamp" data-t="00:00:16">[00:00:16]</a>. This progression can be understood through three main stages, each addressing the limitations of the last.

## Stage 1: Large Language Models (LLMs) by Themselves

Initially, LLMs were limited in their capabilities <a class="yt-timestamp" data-t="00:02:42">[00:02:42]</a>. By themselves, LLMs cannot perform "meaningful" actions like sending an email or executing specific tasks on a user's behalf <a class="yt-timestamp" data-t="00:03:14">[00:03:14]</a>. Their primary function is to predict the next word in a sequence, making them suitable for tasks like answering questions or generating text <a class="yt-timestamp" data-t="00:03:25">[00:03:25]</a>. For example, given the phrase "My Big Fat Greek," an LLM would predict "Wedding" <a class="yt-timestamp" data-t="00:03:30">[00:03:30]</a>.

## Stage 2: LLMs Combined with Tools

The next significant step in the [[the_evolving_scope_of_ai_in_product_design_and_development | evolution of AI]] assistants involved developers finding ways to combine LLMs with external tools, such as APIs <a class="yt-timestamp" data-t="00:04:48">[00:04:48]</a>. This integration allowed LLMs to perform more complex actions.

*   **Examples of Tool Integration**
    *   **Internet Search:** Chatbots like Perplexity can search the internet by accessing an external service, although the LLM itself does not possess this capability natively <a class="yt-timestamp" data-t="00:03:58">[00:03:58]</a>. Services like Brave search and OpenAI APIs are also used <a class="yt-timestamp" data-t="00:04:28">[00:04:28]</a>.
    *   **Automation:** LLMs can be connected to automation services like Zapier or End8 to trigger actions, such as creating a spreadsheet entry every time an email is received <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. This broadened the [[ai_agents_and_automation | scope of AI agents and automation]] <a class="yt-timestamp" data-t="00:04:57">[00:04:57]</a>.

*   **Challenges of Tool Integration**
    Despite the increased functionality, combining multiple tools with LLMs presents significant challenges <a class="yt-timestamp" data-t="00:05:09">[00:05:09]</a>. Each tool often requires a different setup, akin to speaking a different language, making the process cumbersome and frustrating <a class="yt-timestamp" data-t="00:08:02">[00:08:02]</a>.
    *   **Complexity:** Building an assistant that handles multiple tasks (e.g., searching, reading emails, summarizing) involves gluing together many different tools, which can become a nightmare for engineers <a class="yt-timestamp" data-t="00:05:11">[00:05:11]</a>.
    *   **Maintenance:** Updates to external service APIs can break existing integrations, requiring constant manual adjustments <a class="yt-timestamp" data-t="00:10:18">[00:10:18]</a>.
    *   **Reliability:** LLMs, despite their capabilities, can still "hallucinate" or produce incorrect outputs, especially when interacting with external services <a class="yt-timestamp" data-t="00:06:26">[00:06:26]</a>. This stage highlights [[challenges_and_opportunities_for_ai_integration | challenges for AI integration]] <a class="yt-timestamp" data-t="00:06:11">[00:06:11]</a>.

## Stage 3: The mCP Protocol

The limitations of directly connecting LLMs to various tools led to the development of the mCP (Machine Comprehensible Protocol). mCP acts as a crucial intermediary layer between the LLM and the diverse tools and services it needs to interact with <a class="yt-timestamp" data-t="00:08:38">[00:08:38]</a>.

### What is mCP?
mCP is a standard that unifies the communication between LLMs and external services <a class="yt-timestamp" data-t="00:12:51">[00:12:51]</a>. It translates the different "languages" of various tools into a single, unified language that the LLM can easily understand and utilize <a class="yt-timestamp" data-t="00:08:45">[00:08:45]</a>. This simplifies the process of integrating and stacking multiple tools, aiming to overcome the complexities faced in Stage 2 <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>.

### The mCP Ecosystem
The mCP ecosystem comprises:
*   **mCP Client:** The LLM-facing side, such as platforms like Tempo, Windswept, or Cursor <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>.
*   **mCP Protocol:** The two-way communication standard between the client and server <a class="yt-timestamp" data-t="00:11:32">[00:11:32]</a>.
*   **mCP Server:** Constructed by the service provider (e.g., a database company). This server translates the service's capabilities into the mCP protocol, allowing the mCP client (and thus the LLM) to access it <a class="yt-timestamp" data-t="00:11:34">[00:11:34]</a>.

Anthropic is credited with architecting this system, shifting the responsibility of creating the mCP server to the external service providers themselves <a class="yt-timestamp" data-t="00:11:51">[00:11:51]</a>. This encourages service providers to build their integrations in a standardized way <a class="yt-timestamp" data-t="00:12:34">[00:12:34]</a>.

### Benefits of mCP
*   **Seamless Integration:** Makes it much simpler for LLMs to connect to and access diverse outside resources like databases or other tools <a class="yt-timestamp" data-t="00:09:01">[00:09:01]</a>.
*   **Reduced Manual Work:** Significantly decreases the manual planning and edge case handling previously required <a class="yt-timestamp" data-t="00:09:36">[00:09:36]</a>.
*   **Enhanced Capabilities:** Allows LLMs to become capable of "important stuff," moving beyond just predicting text <a class="yt-timestamp" data-t="00:13:41">[00:13:41]</a>. This improves [[improving_ai_conversation_handling | AI conversation handling]] and the effectiveness of [[use_cases_and_applications_of_ai_agents | AI agents]] <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.

### Current Challenges
While promising, mCP is still in its early stages. Setting up mCP servers can be annoying and involves a lot of local file management <a class="yt-timestamp" data-t="00:13:59">[00:13:59]</a>. These "kinks" need to be resolved, and the standard may evolve or even be challenged by competing protocols <a class="yt-timestamp" data-t="00:14:08">[00:14:08]</a>.

## Startup Opportunities and Future Outlook

The [[the_evolving_scope_of_ai_in_product_design_and_development | evolution of AI]] communication standards like mCP creates new opportunities, similar to how past protocols like HTTPS and SMTP led to major businesses <a class="yt-timestamp" data-t="00:16:01">[00:16:01]</a>.

*   **For Technical Individuals**
    *   **mCP App Store:** A significant opportunity exists to create a platform where users can browse, install, and deploy mCP servers from various repositories, providing a URL for easy integration with mCP clients <a class="yt-timestamp" data-t="00:16:38">[00:16:38]</a>. This relates to [[building_apps_using_ai_tools | building apps using AI tools]] <a class="yt-timestamp" data-t="00:17:10">[00:17:10]</a>.

*   **For Non-Technical Individuals**
    *   **Stay Informed:** It's crucial for non-technical entrepreneurs and business owners to stay updated on platforms adopting mCP capabilities and the finalization of the standard <a class="yt-timestamp" data-t="00:17:31">[00:17:31]</a>.
    *   **Observe and Learn:** The current phase is one of observation and learning. Once the standard is solidified and widely adopted, integrating AI capabilities will become much easier and more seamless, allowing for rapid development of [[developing_startup_ideas_with_ai_assistance | startup ideas]] <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

The goal of mCP is to make LLMs more capable and to provide a structured way for them to interact with the vast ecosystem of digital services, ultimately moving towards a future with more advanced and integrated AI assistants <a class="yt-timestamp" data-t="00:14:24">[00:14:24]</a>.