---
title: Applications and future of AI technology
videoId: jMoAaZP_Kkw
---

From: [[aidotengineer]] <br/> 

## Introduction

The speaker, a co-founder of PyTorch, which is software that powers many AI APIs and is largely funded by Meta, discusses the future of AI, specifically focusing on personal local agents <a class="yt-timestamp" data-t="00:00:30">[00:00:30]</a>. While working on Llama, the speaker does not share any secrets about its future releases <a class="yt-timestamp" data-t="00:00:54">[00:00:54]</a>.

## The Rise of AI Agents

The speaker's interest in personal local agents stemmed from personal experience. Swyx's AI news, an aggregator, significantly saved time by summarizing AI news, which was personally effective for productivity and led to a deeper integration of AI into daily life <a class="yt-timestamp" data-t="00:01:20">[00:01:20]</a>. Additionally, work in robotics, where robots inherently act as agents, reinforced this interest <a class="yt-timestamp" data-t="00:02:09">[00:02:09]</a>. The ultimate goal is to build home robots to handle errands <a class="yt-timestamp" data-t="00:02:17">[00:02:17]</a>.

### Defining an Agent

An agent is defined as something that can act in the world and has "agency" <a class="yt-timestamp" data-t="00:03:05">[00:03:05]</a>. If a system can only gather context but cannot take action, it is not considered an agent <a class="yt-timestamp" data-t="00:03:12">[00:03:12]</a>.

### The Critical Need for Context

A highly intelligent agent without the right context is largely useless <a class="yt-timestamp" data-t="00:03:21">[00:03:21]</a>. For example, an agent with access to Gmail, WhatsApp, and a calendar might lie about a prescription renewal if it doesn't have access to iMessage where the text from CVS was received <a class="yt-timestamp" data-t="00:03:32">[00:03:32]</a>. Similarly, an agent only accessing one bank account might miss funds transferred via Venmo <a class="yt-timestamp" data-t="00:04:08">[00:04:08]</a>. Without sufficient context, a personal agent becomes irritating and unreliable, leading to a lack of trust from the user <a class="yt-timestamp" data-t="00:04:17">[00:04:17]</a>. For an agent to be truly useful, it needs to reach a certain level of reliability and predictability <a class="yt-timestamp" data-t="00:04:36">[00:04:36]</a>.

## Enabling Personal Local Agents

The ideal scenario for providing context to an AI agent is for it to see everything the user sees and hear everything the user hears, essentially having access to all "variables" of one's life <a class="yt-timestamp" data-t="00:05:17">[00:05:17]</a>.

### Challenges with Current Devices

*   **Wearable Devices (e.g., smart glasses):** Battery life limitations make continuous context provision impractical <a class="yt-timestamp" data-t="00:05:31">[00:05:31]</a>.
*   **Smartphones:** Ecosystem restrictions, particularly from companies like Apple, prevent applications from running asynchronously in the background and constantly monitoring screen activity, limiting the agent's ability to gain context <a class="yt-timestamp" data-t="00:05:53">[00:05:53]</a>.

### The Case for Dedicated Local Hardware

A feasible solution for running a personal AI agent right now is a device like a Mac Mini <a class="yt-timestamp" data-t="00:06:30">[00:06:30]</a>. It can be placed at home, connected to the internet, and run agents asynchronously without battery life concerns <a class="yt-timestamp" data-t="00:06:33">[00:06:33]</a>. It also allows logging into various services and can access Android ecosystems <a class="yt-timestamp" data-t="00:06:40">[00:06:40]</a>.

## Why Local and Private? (Privacy and Control)

The speaker strongly advocates for running personal agents locally and privately, rather than relying on cloud services provided by large tech companies <a class="yt-timestamp" data-t="00:07:11">[00:07:11]</a>.

### Trust, Predictability, and Action Space

Unlike existing digital services like cloud email, which have a simple and predictable mental model (email in, reply out), AI agents possess a powerful and unpredictable action space <a class="yt-timestamp" data-t="00:08:01">[00:08:01]</a>. For example, if an email service suddenly offered to auto-reply on your behalf, users would become uncomfortable because they don't understand the full scope of potential actions, such as sending a "nasty" reply to a boss <a class="yt-timestamp" data-t="00:08:27">[00:08:27]</a>. This unpredictability makes users uneasy when they are not in full control <a class="yt-timestamp" data-t="00:08:58">[00:08:58]</a>. Furthermore, cloud services might monetize in ways that compromise user interests, such as making an agent prioritize purchases from partners who offer kickbacks <a class="yt-timestamp" data-t="00:09:09">[00:09:09]</a>. Ultimately, users want control over something as personal and intimate as their AI agent <a class="yt-timestamp" data-t="00:09:30">[00:09:30]</a>.

### Avoiding Walled Gardens

Running a personal agent in a centralized cloud ecosystem risks locking users into "walled gardens" that restrict interoperability <a class="yt-timestamp" data-t="00:09:53">[00:09:53]</a>. While this might be acceptable for compartmentalized services like maps or email, it poses a significant concern for an agent that can take a wide variety of actions across a user's entire daily life <a class="yt-timestamp" data-t="00:10:01">[00:10:01]</a>. Therefore, the speaker believes the world should move towards local personalized agents as the norm <a class="yt-timestamp" data-t="00:10:32">[00:10:32]</a>.

### Protecting "Thought Crimes"

A highly personal AI agent acts as an extension of the user, potentially processing thoughts and queries that one would never voice aloud <a class="yt-timestamp" data-t="00:11:00">[00:11:00]</a>. Relying on cloud providers for such intimate interactions carries the risk of legal or social repercussions due to mandated logging and safety checks, even under enterprise-grade contracts <a class="yt-timestamp" data-t="00:11:16">[00:11:16]</a>. To avoid being "punished for thought crimes," a local agent ensures privacy and control over highly sensitive personal data <a class="yt-timestamp" data-t="00:11:42">[00:11:42]</a>.

## Technical Hurdles and Opportunities

While the speaker is convinced of the necessity of local and private AI agents, there are technical challenges to overcome <a class="yt-timestamp" data-t="00:12:15">[00:12:15]</a>.

### Local Inference Performance

Running local models, which are key components of these agents, is facilitated by open-source projects like vLLM and MLC LLM (referred to as SG Lang) <a class="yt-timestamp" data-t="00:12:28">[00:12:28]</a>. Both are built on PyTorch <a class="yt-timestamp" data-t="00:12:43">[00:12:43]</a>. However, local model inference remains slower and more limited compared to cloud services, even on powerful machines <a class="yt-timestamp" data-t="00:13:13">[00:13:13]</a>. While a 20-billion parameter or distilled model might run quickly locally, the latest, unquantized models are still very slow <a class="yt-timestamp" data-t="00:13:28">[00:13:28]</a>. This is expected to improve and "fix itself" over time, though users might not always run the absolute latest and greatest models <a class="yt-timestamp" data-t="00:13:45">[00:13:45]</a>.

### Research and Product Gaps

The primary challenges are not infrastructural but rather in research and product development <a class="yt-timestamp" data-t="00:14:00">[00:14:00]</a>, presenting an [[challenges_and_opportunities_in_ai_adoption | open challenge for AI engineers]]:

*   **Open Multimodal Models:** Current open multimodal models are good but not great, particularly in areas like computer vision. Even closed models struggle with computer use and tend to break <a class="yt-timestamp" data-t="00:14:20">[00:14:20]</a>. When asked to shop, they often provide boring, generic results and struggle with visually identifying specific tastes <a class="yt-timestamp" data-t="00:14:42">[00:14:42]</a>.
*   **Catastrophic Action Classifiers:** A significant gap exists in the ability of agents to identify "catastrophic actions" – irreversible and harmful actions like purchasing a Tesla instead of Tide Pods <a class="yt-timestamp" data-t="00:15:37">[00:15:37]</a>. More research is needed to enable agents to identify such actions and notify users before proceeding <a class="yt-timestamp" data-t="00:16:22">[00:16:22]</a>.
*   **Open-Source Voice Mode:** The state of open-source voice mode for personal agents is currently insufficient, yet it is crucial for a natural interaction experience <a class="yt-timestamp" data-t="00:16:52">[00:16:52]</a>.

## Optimism for the Future

Despite the challenges, the speaker is bullish on the future of personal local agents due to the rapid [[advancements_in_ai_and_future_implications | advancements in AI]] and the progress of open models.

### Open Models' Compounding Intelligence

Open models are compounding in intelligence faster than closed models because resources are being pooled across a broad community <a class="yt-timestamp" data-t="00:17:11">[00:17:11]</a>. Unlike companies like OpenAI or Anthropic, which focus on improving their own proprietary models, open models benefit from coordinated efforts globally <a class="yt-timestamp" data-t="00:17:19">[00:17:19]</a>. This phenomenon has been evident with the releases of LLaMA, Mistral, and GGUF <a class="yt-timestamp" data-t="00:17:37">[00:17:37]</a>. Historically, open source projects, once they achieve critical mass, tend to win in unprecedented ways, as seen with Linux <a class="yt-timestamp" data-t="00:18:05">[00:18:05]</a>. The speaker believes that open models will eventually become better than closed models in terms of intelligence per dollar invested <a class="yt-timestamp" data-t="00:18:22">[00:18:22]</a>.

### Current Efforts

*   Ross Taylor is working on plugging the reasoning gap between open and closed models by releasing open reasoning data <a class="yt-timestamp" data-t="00:19:14">[00:19:14]</a>.
*   PyTorch is actively working on enabling local agents and addressing the technical challenges, and is hiring AI and systems engineers <a class="yt-timestamp" data-t="00:19:27">[00:19:27]</a>.
*   LlamaCon, an event focusing on Llama-related developments, is scheduled for April 29th <a class="yt-timestamp" data-t="00:19:55">[00:19:55]</a>.