---
title: Participating in AI hackathons and building communitydriven projects
videoId: 56D91EcaUnM
---

From: [[colemedin]] <br/> 

## Introduction to the AI Hackathon
A hackathon competition, also known as a coding competition, has been launched by Automator for its [[Community-Driven AI agents | Live Agent Studio]] platform <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Announced on December 25th, it offers a [[Prize breakdown for AI Hackathon | $5,000 prize pool]] <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. The sole requirement for participation is to build an AI agent for the [[Community-Driven AI agents | Live Agent Studio]] <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

The competition is sponsored by [[Opensource AI coding assistants and community building | Voiceflow]] and [[Opensource AI coding assistants and community building | n8n]], both widely used no-code/low-code tools for building AI agents <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. Automator's platform also contributes to the prize pool <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. It offers an exciting opportunity to join a community, develop agents, win prizes, and showcase AI mastery <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

## The Live Agent Studio: A [[Community-Driven AI agents | Community-Driven]] Platform
The [[Community-Driven AI agents | Live Agent Studio]] is a platform developed as part of Automator, designed to be a [[Community-Driven AI agents | community-driven]] hub for AI agents <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. All agents on the platform are open source, allowing users to try them out, view their source code, download them, and learn how to implement them through extensive documentation <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The goal is to establish a central hub for [[Opensource AI coding assistants and community building | open-source]] agents, fostering learning and growth in AI together <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

## [[AI Hackathon competition details | Hackathon Details]]

### Purpose and Prizes
The total [[Prize breakdown for AI Hackathon | prize pool]] is $5,000 <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. The best overall agent will receive $1,500 <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. [[Participating in AI agent hackathons | Registration is free]] <a class="yt-timestamp" data-t="00:11:27">[00:11:27]</a>.

### [[Timeline and registration process for AI Hackathon | Timeline and Registration]]
*   **Registration:** Open until January 8th <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **Competition & Submissions:** January 8th through January 22nd <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Winner Announcement:** A live stream on February 1st <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### [[Judging criteria for AI Hackathon | Judging]] and [[Community engagement in open source projects | Community Engagement]]
The Automator team will conduct an initial round of [[Judging criteria for AI Hackathon | judging]] <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. Following this, selected agents will be uploaded to the [[Community-Driven AI agents | Live Agent Studio]] for [[Community engagement in open source projects | community voting]] to determine the winners <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. Measures will be in place to ensure fair voting <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

## Building Your AI Agent for the Hackathon

### Supported Platforms and Tools
Participants can use various platforms to build their agents:
*   [[Opensource AI coding assistants and community building | n8n]] <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   Any Python framework, including custom code with OpenAI API or Anthropic <a class="yt-timestamp" data-t="02:00:34">[02:00:34]</a>.
*   [[Opensource AI coding assistants and community building | Voiceflow]] <a class="yt-timestamp" data-t="02:01:08">[02:01:08]</a>.
*   Any language supported within a Docker container (e.g., Go, Rust), provided the API request and conversation memory are handled internally <a class="yt-timestamp" data-t="02:01:20">[02:01:20]</a>.

### Making Your Agent Compatible
To ensure compatibility with the [[Community-Driven AI agents | Live Agent Studio]], agents must adhere to a standardized method for accepting input, outputting information, and managing conversation history <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. This is because the platform hosts all agents on a single front-end <a class="yt-timestamp" data-t="01:48:13">[01:48:13]</a>.

Key compatibility aspects include:
*   **API Endpoint:** Turning the agent into an API endpoint using a webhook trigger <a class="yt-timestamp" data-t="01:49:41">[01:49:41]</a>.
*   **Input Parameters:** Handling specific input parameters like query, user ID, request ID, and session ID (for conversation tracking) <a class="yt-timestamp" data-t="01:49:49">[01:49:49]</a>.
*   **Conversation History:** Utilizing a PostgreSQL database (like Superbase) for chat memory, which the AI agent node in n8n can automatically set up <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a>.
*   **Real-time Reporting:** Inserting messages into the database to report the agent's actions in real-time <a class="yt-timestamp" data-t="01:55:18">[01:55:18]</a>.
*   **Output Parameters:** Producing a final JSON output indicating workflow success or failure <a class="yt-timestamp" data-t="01:57:01">[01:57:01]</a>.

### Resources for Developers
*   **Developer Guide:** An extensive developer guide provides detailed instructions on how to build agents compatible with the studio <a class="yt-timestamp" data-t="01:47:40">[01:47:40]</a>.
*   **Sample Agents:** [[Testing and deploying AIassisted code projects | Sample n8n]] and Python agents are available as templates, demonstrating how to implement an AI agent for the [[Community-Driven AI agents | Live Agent Studio]] <a class="yt-timestamp" data-t="01:48:41">[01:48:41]</a>. These can be downloaded from the [[Opensource AI coding assistants and community building | Automator Agents]] open-source repository <a class="yt-timestamp" data-t="01:48:49">[01:48:49]</a>.
*   **Video Tutorials:** Videos are provided to walk users through the documentation <a class="yt-timestamp" data-t="01:50:01">[01:50:01]</a>.
*   **Docker File:** A Docker file is included in the sample Python agent to show how to containerize an agent <a class="yt-timestamp" data-t="02:02:01">[02:02:01]</a>.

> [!info] Tip:
> It's helpful to use AI assistants like Claude to generate code snippets, such as regular expressions for parsing URLs, especially if you're not deeply familiar with coding <a class="yt-timestamp" data-t="01:58:15">[01:58:15]</a>.

> [!note] Example Agent:
> The GitHub assistant agent, a prototype built during the session using n8n and Gemini 2.0 Flash, is available to try on the [[Community-Driven AI agents | Live Agent Studio]] <a class="yt-timestamp" data-t="01:19:07">[01:19:07]</a>. This agent can analyze the file structure of a public GitHub repository and answer questions about specific files <a class="yt-timestamp" data-t="01:16:57">[01:16:57]</a>. Its prototype capabilities include extracting organization and repository names from URLs, making HTTP requests to GitHub APIs, and formatting responses for clear understanding by the LLM <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>.```markdown
# [[participating_in_ai_agent_hackathons | Participating in AI Agent Hackathons]] and [[communitydriven_ai_agents | Community-Driven AI Agents]]

## Introduction to the AI Hackathon
A hackathon competition, also known as a coding competition, has been launched by Automator for its [[Community-Driven AI agents | Live Agent Studio]] platform <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Announced on December 25th, it offers a [[Prize breakdown for AI Hackathon | $5,000 prize pool]] <a class="yt-timestamp" data-t="00:10:15">[00:10:15]</a>. The sole requirement for participation is to build an AI agent for the [[Community-Driven AI agents | Live Agent Studio]] <a class="yt-timestamp" data-t="00:10:20">[00:10:20]</a>.

The competition is sponsored by [[Opensource AI coding assistants and community building | Voiceflow]] and [[Opensource AI coding assistants and community building | n8n]], both widely used no-code/low-code tools for building AI agents <a class="yt-timestamp" data-t="00:10:43">[00:10:43]</a>. Automator's platform also contributes to the prize pool <a class="yt-timestamp" data-t="00:10:51">[00:10:51]</a>. It offers an exciting opportunity to join a community, develop agents, win prizes, and showcase AI mastery <a class="yt-timestamp" data-t="00:10:55">[00:10:55]</a>.

## The Live Agent Studio: A [[Community-Driven AI agents | Community-Driven]] Platform
The [[Community-Driven AI agents | Live Agent Studio]] is a platform developed as part of Automator, designed to be a [[Community-Driven AI agents | community-driven]] hub for AI agents <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. All agents on the platform are open source, allowing users to try them out, view their source code, download them, and learn how to implement them through extensive documentation <a class="yt-timestamp" data-t="00:09:21">[00:09:21]</a>. The goal is to establish a central hub for [[Opensource AI coding assistants and community building | open-source]] agents, fostering learning and growth in AI together <a class="yt-timestamp" data-t="00:12:39">[00:12:39]</a>.

## [[AI Hackathon competition details | Hackathon Details]]

### Purpose and Prizes
The total [[Prize breakdown for AI Hackathon | prize pool]] is $5,000 <a class="yt-timestamp" data-t="00:11:06">[00:11:06]</a>. The best overall agent will receive $1,500 <a class="yt-timestamp" data-t="00:11:11">[00:11:11]</a>. [[participating_in_ai_agent_hackathons | Registration is free]] <a class="yt-timestamp" data-t="01:11:27">[01:11:27]</a>.

### [[Timeline and registration process for AI Hackathon | Timeline and Registration]]
*   **Registration:** Open until January 8th <a class="yt-timestamp" data-t="00:12:05">[00:12:05]</a>.
*   **Competition & Submissions:** January 8th through January 22nd <a class="yt-timestamp" data-t="00:12:09">[00:12:09]</a>.
*   **Winner Announcement:** A live stream on February 1st <a class="yt-timestamp" data-t="00:12:47">[00:12:47]</a>.

### [[Judging criteria for AI Hackathon | Judging]] and [[Community engagement in open source projects | Community Engagement]]
The Automator team will conduct an initial round of [[Judging criteria for AI Hackathon | judging]] <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>. Following this, selected agents will be uploaded to the [[Community-Driven AI agents | Live Agent Studio]] for [[Community engagement in open source projects | community voting]] to determine the winners <a class="yt-timestamp" data-t="00:12:19">[00:12:19]</a>. Measures will be in place to ensure fair voting <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>.

## Building Your AI Agent for the Hackathon

### Supported Platforms and Tools
Participants can use various platforms to build their agents:
*   [[Opensource AI coding assistants and community building | n8n]] <a class="yt-timestamp" data-t="00:11:47">[00:11:47]</a>.
*   Any Python framework, including custom code with OpenAI API or Anthropic <a class="yt-timestamp" data-t="02:00:34">[02:00:34]</a>.
*   [[Opensource AI coding assistants and community building | Voiceflow]] <a class="yt-timestamp" data-t="02:01:08">[02:01:08]</a>.
*   Any language supported within a Docker container (e.g., Go, Rust), provided the API request and conversation memory are handled internally <a class="yt-timestamp" data-t="02:01:20">[02:01:20]</a>.

### Making Your Agent Compatible
To ensure compatibility with the [[Community-Driven AI agents | Live Agent Studio]], agents must adhere to a standardized method for accepting input, outputting information, and managing conversation history <a class="yt-timestamp" data-t="01:48:00">[01:48:00]</a>. This is because the platform hosts all agents on a single front-end <a class="yt-timestamp" data-t="01:48:13">[01:48:13]</a>.

Key compatibility aspects include:
*   **API Endpoint:** Turning the agent into an API endpoint using a webhook trigger <a class="yt-timestamp" data-t="01:49:41">[01:49:41]</a>.
*   **Input Parameters:** Handling specific input parameters like query, user ID, request ID, and session ID (for conversation tracking) <a class="yt-timestamp" data-t="01:49:49">[01:49:49]</a>.
*   **Conversation History:** Utilizing a PostgreSQL database (like Superbase) for chat memory, which the AI agent node in n8n can automatically set up <a class="yt-timestamp" data-t="01:53:50">[01:53:50]</a>.
*   **Real-time Reporting:** Inserting messages into the database to report the agent's actions in real-time <a class="yt-timestamp" data-t="01:55:18">[01:55:18]</a>.
*   **Output Parameters:** Producing a final JSON output indicating workflow success or failure <a class="yt-timestamp" data-t="01:57:01">[01:57:01]</a>.

### Resources for Developers
*   **Developer Guide:** An extensive developer guide provides detailed instructions on how to build agents compatible with the studio <a class="yt-timestamp" data-t="01:47:40">[01:47:40]</a>.
*   **Sample Agents:** [[Testing and deploying AIassisted code projects | Sample n8n]] and Python agents are available as templates, demonstrating how to implement an AI agent for the [[Community-Driven AI agents | Live Agent Studio]] <a class="yt-timestamp" data-t="01:48:41">[01:48:41]</a>. These can be downloaded from the [[Opensource AI coding assistants and community building | Automator Agents]] open-source repository <a class="yt-timestamp" data-t="01:48:49">[01:48:49]</a>.
*   **Video Tutorials:** Videos are provided to walk users through the documentation <a class="yt-timestamp" data-t="01:50:01">[01:50:01]</a>.
*   **Docker File:** A Docker file is included in the sample Python agent to show how to containerize an agent <a class="yt-timestamp" data-t="02:02:01">[02:02:01]</a>.

> [!info] Tip:
> It's helpful to use AI assistants like Claude to generate code snippets, such as regular expressions for parsing URLs, especially if you're not deeply familiar with coding <a class="yt-timestamp" data-t="01:58:15">[01:58:15]</a>.

> [!note] Example Agent:
> The GitHub assistant agent, a prototype built during the session using n8n and Gemini 2.0 Flash, is available to try on the [[Community-Driven AI agents | Live Agent Studio]] <a class="yt-timestamp" data-t="01:19:07">[01:19:07]</a>. This agent can analyze the file structure of a public GitHub repository and answer questions about specific files <a class="yt-timestamp" data-t="01:16:57">[01:16:57]</a>. Its prototype capabilities include extracting organization and repository names from URLs, making HTTP requests to GitHub APIs, and formatting responses for clear understanding by the LLM <a class="yt-timestamp" data-t="00:58:51">[00:58:51]</a>.
```