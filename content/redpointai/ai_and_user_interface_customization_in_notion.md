---
title: AI and user interface customization in Notion
videoId: og57f_tv3zY
---

From: [[redpointai]] <br/> 

Notion is actively integrating AI into its product, with a focus on enhancing user experience and productivity. Linus Lee, who helps lead Notion's AI efforts, shared insights into the company's approach to AI development and how users interact with these new features <a class="yt-timestamp" data-t="00:00:07">[00:00:07]</a>.

## Notion AI Product Offerings
Notion's journey into AI began around a year ago with a hackathon, where co-founders Ivan Zhao and Simon Last explored the capabilities of GPT-3 <a class="yt-timestamp" data-t="03:02:00">[03:02:00]</a>. This led to the development of several key AI features:

*   **Notion AI Writer** The first major AI feature, launched in beta in November and publicly in February <a class="yt-timestamp" data-t="03:38:00">[03:38:00]</a>. It functions as an AI assistant within documents, allowing users to:
    *   Summarize pages in various formats <a class="yt-timestamp" data-t="03:48:00">[03:48:00]</a>.
    *   Extract key ideas, action items, or topics <a class="yt-timestamp" data-t="03:51:00">[03:51:00]</a>.
    *   Fix spelling and grammar mistakes <a class="yt-timestamp" data-t="03:56:00">[03:56:00]</a>.
    *   Improve writing style and voice <a class="yt-timestamp" data-t="04:00:00">[04:00:00]</a>.
    *   Draft initial ideas or marketing copy <a class="yt-timestamp" data-t="04:07:00">[04:07:00]</a>.
    *   Users can conversationally follow up on generated content to refine it, making it shorter or more "Punchy" <a class="yt-timestamp" data-t="04:30:00">[04:30:00]</a>.

*   **AI Autofill** Released in May, this feature integrates AI into Notion databases, which are often used for project management <a class="yt-timestamp" data-t="04:44:00">[04:44:00]</a>. It can automatically populate entire columns or properties, such as:
    *   Identifying key topics from meeting notes <a class="yt-timestamp" data-t="05:04:00">[05:04:00]</a>.
    *   Extracting core customer needs or company roles from interview transcripts <a class="yt-timestamp" data-t="05:07:00">[05:07:00]</a>.

*   **Notion Q&A** The most recent addition, Notion Q&A, moves beyond page-level assistance. It understands the entire workspace, allowing users to ask questions and receive answers from across multiple pages <a class="yt-timestamp" data-t="05:32:00">[05:32:00]</a>. This feature aims to solve the problem of finding information in complex, growing organizational workspaces <a class="yt-timestamp" data-t="06:04:00">[06:04:00]</a>. It utilizes Retrieval Augmented Generation (RAG) <a class="yt-timestamp" data-t="06:36:00">[06:36:00]</a>.

## Development Philosophy and User Interaction
Notion's AI development blends user problem-solving with exploring new technological capabilities <a class="yt-timestamp" data-t="07:06:00">[07:06:00]</a>. The team, comprising about a dozen engineers and several designers, operates in an "expand out and then contract" cycle, prototyping quickly and "dogfooding" extensively by using Notion to build Notion <a class="yt-timestamp" data-t="07:27:00">[07:27:00]</a>.

### User Education and Customization
Notion leverages internal testing and early user feedback to understand how people interact with AI features. They found that users often take initial features, especially those requiring prompt engineering, and apply them to unanticipated use cases <a class="yt-timestamp" data-t="00:18:07">[00:18:07]</a>.

A key learning is the pattern of **pre-built, optimized prompts** alongside **custom prompt fields** <a class="yt-timestamp" data-t="00:18:45">[00:18:45]</a>.
*   **Pre-built prompts**: Most users opt for these, with popular use cases including summarization, improving writing, fixing grammar, and translation <a class="yt-timestamp" data-t="00:19:32">[00:19:32]</a>.
*   **Custom prompts**: These allow power users to extend the AI's functionality and inspire new pre-built features <a class="yt-timestamp" data-t="00:19:05">[00:19:05]</a>. For example, translation became a built-in prompt after users frequently employed custom prompts for it <a class="yt-timestamp" data-t="00:18:41">[00:18:41]</a>.

Notion aims to help users overcome the "blank canvas problem" <a class="yt-timestamp" data-t="00:40:00">[00:40:00]</a> by providing structured starting points and suggestions for next steps based on AI output <a class="yt-timestamp" data-t="00:22:00">[00:22:00]</a>. The goal is to reduce the "mental work" of coming up with what to say to the AI <a class="yt-timestamp" data-t="00:22:26">[00:22:26]</a>.

### Interface Design for AI
Linus Lee emphasizes the importance of iterating on interfaces to suit AI use cases. For every AI feature, users can drop down to a "lowest level" of direct AI prompting <a class="yt-timestamp" data-t="00:40:11">[00:40:11]</a>. The challenge is defining the "right building blocks" or "blocks for AI" <a class="yt-timestamp" data-t="00:40:51">[00:40:51]</a>.

*   For writing, free-form custom prompts work well <a class="yt-timestamp" data-t="00:41:10">[00:41:10]</a>.
*   For "generative interfaces" where models output UI elements instead of text, a component library or UI language would be needed to ensure coherence <a class="yt-timestamp" data-t="00:41:50">[00:41:50]</a>.

Notion is exploring how much control AI should have over the UI. While hardcoded interfaces powered by AI are easier, giving AI more control over what appears on screen could lead to more interesting outcomes, despite being a harder machine learning problem <a class="yt-timestamp" data-t="00:47:38">[00:47:38]</a>.

## Challenges in AI Development
One of the hardest challenges has been **evaluation** of language models, especially for features like Q&A where correctness is paramount <a class="yt-timestamp" data-t="00:23:14">[00:23:14]</a>. Unlike creative writing where "wiggle room" exists, Q&A demands specific answers. The team also grapples with anticipating and addressing "meta questions" about Notion itself or queries involving dynamic, time-sensitive information that isn't explicitly documented <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>.

Notion has built most of its evaluation tools in-house due to the complex, structured nature of Notion documents and the need for faster iteration <a class="yt-timestamp" data-t="00:26:21">[00:26:21]</a>.

## Model Strategy and Partnerships
Notion partners closely with [[Advancements in AI for Creative Tools | Anthropic]] and [[Advancements in AI for Creative Tools | OpenAI]] for their large language models (LLMs), recognizing the difficulty of competing at the infrastructure level <a class="yt-timestamp" data-t="00:31:08">[00:31:08]</a>. Notion's role is to understand specific tasks, collect or generate synthetic data, and build evaluations, especially considering their commitment **not to train on customer data** <a class="yt-timestamp" data-t="00:31:40">[00:31:40]</a>.

They iterate on the full stack of their AI pipeline, from embeddings and ranking (for retrieval) to the answering component of the model <a class="yt-timestamp" data-t="00:29:30">[00:29:30]</a>.

## Future Outlook
Linus Lee believes that while LLMs will become a skill in every engineer's toolkit, a centralized AI team remains beneficial for quality control, monitoring, and managing data sets and training workflows <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

He notes that "context length" in models might be overhyped for most useful tasks, while "alternatives to Transformers" are underhyped <a class="yt-timestamp" data-t="00:42:22">[00:42:22]</a>. He suggests that the focus should be on building general approaches that understand the domain of the product rather than highly specific models for each task, betting on the increasing generality and capability of models <a class="yt-timestamp" data-t="00:46:14">[00:46:14]</a>.

For more information, visit Notion AI at [notion.ai](http://notion.ai) <a class="yt-timestamp" data-t="00:50:06">[00:50:06]</a>.