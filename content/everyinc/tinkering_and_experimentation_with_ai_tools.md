---
title: Tinkering and experimentation with AI tools
videoId: WVKgeSDVBow
---

From: [[everyinc]] <br/> 
The spirit of [[experimentation_with_aigenerated_content | tinkering]] and [[experimentation_with_aigenerated_content | experimentation]] is crucial when working in the current wave of AI development <a class="yt-timestamp" data-t="01:35:10">[01:35:10]</a>. The availability of [[experiments_and_tools_in_ai_research | tools]] makes it possible to constantly build and ship new things <a class="yt-timestamp" data-t="01:43:56">[01:43:56]</a>.

## How the AI Role Began <a class="yt-timestamp" data-t="01:52:45">[01:52:45]</a>

Matt, who works at Union Square Ventures (USV), a top Venture Capital firm, became the "AI guy" by following his curiosity <a class="yt-timestamp" data-t="02:00:52">[02:00:52]</a>. For about six years, he worked on the talent side, but his passion lay elsewhere <a class="yt-timestamp" data-t="02:05:43">[02:05:43]</a>. He would append his weekly talent emails with "here's this weird thing I made over the weekend that you might want to play with" <a class="yt-timestamp" data-t="02:46:17">[02:46:17]</a>.

Initially, these projects included making "fake movie trailers" using [[creating_cinematic_experiences_with_ai_tools | Runway ML]] <a class="yt-timestamp" data-t="02:55:00">[02:55:00]</a>. He would outline a rom-com idea, ask ChatGPT to write a 30-second script with timestamps, and then feed each timestamped prompt into Runway ML to generate video <a class="yt-timestamp" data-t="03:04:47">[03:04:47]</a>. After paternity leave, USV partners recognized his natural inclination to [[experimentation_with_aigenerated_content | tinker]] and offered him a full-time role dedicated to [[developing_apps_and_prototypes_using_ai | making prototypes with AI]] <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a><a class="yt-timestamp" data-t="04:05:07">[04:05:07]</a>.

## Early Discoveries and the Creative Potential of AI <a class="yt-timestamp" data-t="04:57:04">[04:57:04]</a>

The initial spark came from [[experiments_and_tools_in_ai_research | tools]] like DALL-E or ChatGPT <a class="yt-timestamp" data-t="05:08:47">[05:08:47]</a>. A distinct memory involves writing a musical about Jeff Koons with ChatGPT over two years ago, where the AI would generate the story and refine it based on feedback <a class="yt-timestamp" data-t="05:31:00">[05:31:00]</a><a class="yt-timestamp" data-t="05:48:46">[05:48:46]</a>. Another pivotal moment was seeing his illustrator wife use DALL-E to design a cross-stitch pattern she could then execute in real life <a class="yt-timestamp" data-t="06:08:00">[06:08:00]</a>. This demonstrated that AI could be a [[enhancing_creativity_and_idea_development_with_ai | tool to help bring out human creativity]] <a class="yt-timestamp" data-t="06:17:00">[06:17:00]</a>.

## The Tinkerer's Mindset <a class="yt-timestamp" data-t="06:21:49">[06:21:49]</a>

Matt attributes his [[experimentation_with_aigenerated_content | tinkering]] nature to his father, who always had broken machinery or ham radios he was building <a class="yt-timestamp" data-t="06:32:00">[06:32:00]</a>. As a "generalist" without many "hard skills" like playing piano, AI [[experiments_and_tools_in_ai_research | tools]] allowed him to learn alongside the creative process <a class="yt-timestamp" data-t="06:57:00">[06:57:00]</a>. The feedback loops are incredibly fast; for example, a custom GPT could guide him on how to connect two APIs to read a live spreadsheet, something he wouldn't know as a software engineer <a class="yt-timestamp" data-t="07:57:00">[07:57:00]</a>.

This approach contrasts with traditional learning methods, such as programming courses that start with basic building blocks like variables and functions before allowing students to build something tangible <a class="yt-timestamp" data-t="08:41:00">[08:41:00]</a>. With AI, one can make something that looks like the desired final product within 30 minutes, then delve into how it works <a class="yt-timestamp" data-t="09:11:00">[09:11:00]</a>. This is akin to building a clock radio and then taking it apart to understand its mechanics, fostering skill development <a class="yt-timestamp" data-t="09:56:00">[09:56:00]</a>. The only limiting factors become time and patience <a class="yt-timestamp" data-t="10:27:00">[10:27:00]</a>.

## Practical AI Applications at USV <a class="yt-timestamp" data-t="10:32:15">[10:32:15]</a>

### The Librarian (Chatbot) <a class="yt-timestamp" data-t="10:37:00">[10:37:00]</a>

Initially, the idea was to build a monolithic "super app" with a name, face, and personality <a class="yt-timestamp" data-t="10:51:00">[10:51:00]</a>. However, the approach shifted to building individual agents (GPTs) that perform specific tasks using existing [[experiments_and_tools_in_ai_research | tools]] <a class="yt-timestamp" data-t="11:15:00">[11:15:00]</a>.

The core of "The Librarian" is a chatbot built on USV's 20-year history of writing, comprising about 15,000 articles <a class="yt-timestamp" data-t="12:01:00">[12:01:00]</a>. The motivation came from a partner who often found himself re-writing blog posts because he had already covered the topic <a class="yt-timestamp" data-t="12:27:00">[12:27:00]</a>. The goal was to create a bot that allowed conversational interaction with their extensive writing <a class="yt-timestamp" data-t="12:41:00">[12:41:00]</a>.

Naming the bot was a [[challenges_in_building_ai_tools | challenge]]; names like "Conversations" and "At the Edge" didn't resonate, but "The Librarian" clicked due to its powerful metaphor <a class="yt-timestamp" data-t="12:56:00">[12:56:00]</a>. While initially a standalone app built with No-code MBA, maintaining a custom UI became a pain <a class="yt-timestamp" data-t="13:47:00">[13:47:00]</a>. It was then broken down into separate, specialized GPTs <a class="yt-timestamp" data-t="14:09:00">[14:09:00]</a>.

**Demo of The Librarian**:
The process involves pasting a company's "about page" (e.g., Consensus) into the GPT and asking it to pull out relevant USV blog posts <a class="yt-timestamp" data-t="14:35:00">[14:35:00]</a>. The GPT, having access to USV's knowledge base, identifies major themes from their writings relevant to the company, such as "AI unlocking knowledge," "democratizing science," and "trust in AI systems" <a class="yt-timestamp" data-t="15:47:00">[15:47:00]</a>.

One [[challenges_in_building_ai_tools | challenge]] encountered was the AI's tendency to "lie" by providing fake URLs for cited articles <a class="yt-timestamp" data-t="17:47:00">[17:47:00]</a>. A trick to spot fake URLs in ChatGPT is when the cursor appears as a text-highlighting cursor instead of a mouse hand <a class="yt-timestamp" data-t="17:58:00">[17:58:00]</a>. By prompting the AI to try again, it generates real links <a class="yt-timestamp" data-t="18:34:00">[18:34:00]</a>. This highlights that AI should be seen as an "enhancer," not a producer of the final product <a class="yt-timestamp" data-t="19:22:00">[19:22:00]</a>.

The purpose of this tool is to quickly demonstrate USV's long-term alignment with potential investment companies, proving they aren't just "chasing the hot thing" <a class="yt-timestamp" data-t="17:17:00">[17:17:00]</a>. While the AI can draft emails incorporating these articles, partners would typically refine them <a class="yt-timestamp" data-t="20:47:00">[20:47:00]</a>.

### Portfolio Tracker GPT <a class="yt-timestamp" data-t="21:16:00">[21:16:00]</a>

This separate GPT categorizes USV's investments by company, investment date, and ownership percentage <a class="yt-timestamp" data-t="21:17:00">[21:17:00]</a>. It can generate charts plotting investments in specific areas (e.g., education, search, AI) over time <a class="yt-timestamp" data-t="21:38:00">[21:38:00]</a>. Users can correct missing data or refine the charts based on their internal knowledge <a class="yt-timestamp" data-t="21:55:00">[21:55:00]</a>. These [[experiments_and_tools_in_ai_research | tools]] significantly speed up knowledge gathering that would traditionally take a long time <a class="yt-timestamp" data-t="22:34:00">[22:34:00]</a>.

The goal is to eventually make "The Librarian" publicly available on the USV website, allowing external parties to query USV's thesis and writings <a class="yt-timestamp" data-t="22:51:00">[22:51:00]</a>. It could allow founders to dump their pitch decks and receive relevant USV articles, helping them align with USV's thinking before meetings <a class="yt-timestamp" data-t="23:54:00">[23:54:00]</a>.

### AI for Internal Decision-Making and Playbooks <a class="yt-timestamp" data-t="24:12:00">[24:12:00]</a>

USV focuses on [[exploring_human_and_ai_collaboration | enhancing, not replacing]] human interaction <a class="yt-timestamp" data-t="26:28:00">[26:28:00]</a>. They are not interested in building digital clones of partners to replicate their investment "taste" or decision-making process, as partners are highly accessible <a class="yt-timestamp" data-t="25:06:00">[25:06:00]</a>.

However, AI is used to capture and organize the "wealth of knowledge" shared in weekly portfolio meetings <a class="yt-timestamp" data-t="28:01:00">[28:01:00]</a>. The aim is to build "playbooks" for tricky, repetitive situations that often arise but are rarely written down, such as a CEO stepping down <a class="yt-timestamp" data-t="31:05:00">[31:05:05]</a><a class="yt-timestamp" data-t="31:08:00">[31:08:00]</a>. AI transcribers can note when such conversations occur and record them as playbooks <a class="yt-timestamp" data-t="31:16:00">[31:16:00]</a>. This reveals how much businesses repeat themselves, as AI is adept at pattern matching <a class="yt-timestamp" data-t="29:03:00">[29:03:00]</a>.

### AI for Meeting Summaries and Podcasts <a class="yt-timestamp" data-t="34:33:00">[34:33:00]</a>

USV transcribes its special topical meetings (AI, crypto, climate) and ports these transcripts into a GPT, allowing questions to be asked about the meetings <a class="yt-timestamp" data-t="34:47:00">[34:47:00]</a>. While purpose-built tools exist, having these functions within a unified conversational interface (like ChatGPT or Claude on a phone) offers greater ease of access <a class="yt-timestamp" data-t="35:16:00">[35:16:00]</a>.

One preferred [[experiments_and_tools_in_ai_research | tool]] for meeting notes is NotebookLM due to its insightful question prompts, better citation capabilities, and the ability to turn meeting notes into podcasts <a class="yt-timestamp" data-t="36:17:00">[36:17:00]</a>.

**Meeting Podcasts**:
Key meetings are turned into 10-15 minute podcasts, allowing team members to listen on the go (subway, city bike) while doing other tasks like responding to emails <a class="yt-timestamp" data-t="37:17:00">[37:17:17]</a>. An example is a podcast created from a meeting with Chad Hurwitz, who directed the generative AI film about Brian Eno <a class="yt-timestamp" data-t="37:28:00">[37:28:00]</a>.

This concept extends to internal product incubations, where all meeting recordings and important Discord messages are automatically processed to create a podcast summary of what happened <a class="yt-timestamp" data-t="38:44:00">[38:44:00]</a>. This is particularly useful for leaders who cannot attend every meeting but want to stay informed <a class="yt-timestamp" data-t="39:02:00">[39:02:00]</a>.

The availability of AI for storytelling significantly reduces the "cost of storytelling" <a class="yt-timestamp" data-t="42:29:00">[42:29:00]</a>. This means high-quality stories can be told about subjects previously deemed too expensive or mundane, such as company meetings or daily life <a class="yt-timestamp" data-t="42:44:00">[42:44:00]</a>. AI can pick out interesting moments and leave out the rest <a class="yt-timestamp" data-t="43:05:00">[43:05:00]</a>.

**Process for generating "Overheard at USV" tweets**:
This process has evolved from fully automated to semi-automated <a class="yt-timestamp" data-t="44:21:00">[44:21:00]</a>. Using ChatGPT, a prompt requests five "Overheards" from specific AI meeting dates, explicitly excluding company-specific mentions to prevent sharing confidential pitches <a class="yt-timestamp" data-t="44:54:00">[44:54:00]</a>.

Initial AI-generated summaries often lack concrete details or explicit positions, making them less valuable <a class="yt-timestamp" data-t="47:10:00">[47:10:00]</a>. For example, a point about "uncorrelated bets" might pose a question without revealing USV's perspective or the nuances of the internal debate <a class="yt-timestamp" data-t="47:20:00">[47:20:00]</a>. Re-prompting the AI to be more concrete about the different positions taken in the meeting significantly improves the output <a class="yt-timestamp" data-t="50:51:00">[50:51:00]</a>. The ideal approach is to use AI [[exploring_human_and_ai_collaboration | in partnership with humans]] to create better, more valuable content, rather than relying on purely AI-generated media <a class="yt-timestamp" data-t="55:57:00">[55:57:00]</a>.

## The Dream Machine <a class="yt-timestamp" data-t="01:03:04">[01:03:04]</a>

"The Dream Machine" is a locally running visual diffusion model hooked up to a television in the USV office <a class="yt-timestamp" data-t="01:03:21">[01:03:21]</a>. It is connected to the Whisper API, listening to conversations and generating real-time moving images based on what is being discussed <a class="yt-timestamp" data-t="01:03:38">[01:03:38]</a>. Developed by an artist known as "Human," this machine is a constant source of fascination for both visitors and staff <a class="yt-timestamp" data-t="01:03:50">[01:03:50]</a><a class="yt-timestamp" data-t="01:04:06">[01:04:06]</a>.

Though it can get "backlogged" and slow to respond, resetting its memory allows it to immediately reflect the current conversation, transforming spoken words into visual scenes, like whales appearing when Moby Dick is mentioned <a class="yt-timestamp" data-t="01:05:09">[01:05:09]</a>. This [[experiments_and_tools_in_ai_research | tool]] highlights how AI can [[creating_cinematic_experiences_with_ai_tools | create artistic experiences]] that reflect internal states and conversations in a visceral, dramatic way, similar to how setting reflects a character's emotions in fiction <a class="yt-timestamp" data-t="01:05:57">[01:05:57]</a>. It is considered one of the first truly native AI art forms that could not exist prior to AI <a class="yt-timestamp" data-t="01:07:02">[01:07:02]</a>.

Ultimately, the core lesson from all these [[developing_apps_and_prototypes_using_ai | prototypes]] and [[experimentation_with_aigenerated_content | experiments]] is to "bring your ideas to life" and "just make stuff" because the [[experiments_and_tools_in_ai_research | tools]] are readily available <a class="yt-timestamp" data-t="01:07:41">[01:07:41]</a>.