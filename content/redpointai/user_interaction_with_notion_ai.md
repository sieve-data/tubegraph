---
title: User interaction with Notion AI
videoId: og57f_tv3zY
---

From: [[redpointai]] <br/> 

Notion AI is designed to augment user workflows within the Notion platform, helping with tasks ranging from writing and editing to information retrieval. Understanding how users interact with these AI features has been a continuous learning process for the Notion AI team <a class="yt-timestamp" data-t="00:16:54">[00:16:54]</a>.

## Collaborative Human-AI Interaction
From the outset, Notion observed a core theme in user interaction with AI: humans and AI consistently work together to iterate and achieve better outcomes <a class="yt-timestamp" data-t="00:12:00">[00:12:00]</a>. Users often generate a draft with AI and then refine it, or they iterate on their own drafts to fix mistakes and improve clarity <a class="yt-timestamp" data-t="00:04:18">[00:04:18]</a>. This led to the addition of conversational follow-ups for generated content, allowing users to ask the AI to "make it shorter" or "more punchy" <a class="yt-timestamp" data-t="00:04:30">[00:04:30]</a>. This iterative approach is a key aspect of [[humanai_interaction_in_education_and_society | HumanAI interaction]].

## Identifying and Integrating New Features
Notion employs several methods to learn about user interaction and discover new use cases:

*   **Internal Dogfooding**
    The Notion team heavily uses its own product, including AI features, in a process called "dogfooding" <a class="yt-timestamp" data-t="00:08:05">[00:08:05]</a>. This internal usage, particularly during the ideation phase, provides a rich source of information for understanding useful ways to apply the AI <a class="yt-timestamp" data-t="00:17:14">[00:17:14]</a>. For example, an "annoying prototype" of the Q&A feature, which responded to every internal question, forced the team to rapidly iterate and improve the quality of outputs because they were "so face-to-face with it every day" <a class="yt-timestamp" data-t="00:09:58">[00:09:58]</a>. This constant exposure made it evident whether the feature was useful or not, adding pressure to improve the model quality <a class="yt-timestamp" data-t="00:10:52">[00:10:52]</a>.

*   **Early Testers and Ambassadors**
    Notion also works with early testers, Notion ambassadors, and partners. These external users often take initial [[features_and_enhancements_in_notion_ai | features and enhancements in Notion AI]], especially those requiring prompt engineering, and apply them to unanticipated use cases <a class="yt-timestamp" data-t="00:18:00">[00:18:00]</a>. An example of this was the discovery of translation as a popular use case for AI autofill outside the US, leading Notion to integrate translation as a built-in prompt <a class="yt-timestamp" data-t="00:18:25">[00:18:25]</a>. This method helps in [[using_ai_for_personalized_user_experiences | using AI for personalized user experiences]].

## Pre-built vs. Custom Prompts
Notion's approach to user interaction balances guiding users with providing flexibility:

*   **Guided Experience:** Notion provides pre-built prompts (e.g., "summarize this page," "fix spelling and grammar mistakes," "improve writing") <a class="yt-timestamp" data-t="00:04:46">[00:04:46]</a>. These serve as templates and are the most popular use cases, especially for Notion AI Writer and Autofill <a class="yt-timestamp" data-t="00:19:15">[00:19:15]</a>. Summarization, writing improvement, grammar correction, and translation are particularly widely used <a class="yt-timestamp" data-t="00:19:34">[00:19:34]</a>.

*   **Customization for Power Users:** Users can also access a "custom prompt" field for more specific requests <a class="yt-timestamp" data-t="00:18:37">[00:18:37]</a>. This extensibility allows Notion to discover new common [[creative_process_and_experimentation_with_ai | creative process and experimentation with AI]] use cases, which are then built into pre-baked formulas or templates over time <a class="yt-timestamp" data-t="00:19:08">[00:19:08]</a>. Power users often start with pre-built options for inspiration, then hand-write and reuse their own specific prompts to fit their unique workflows, such as a newsletter writer generating social media tags for new issues <a class="yt-timestamp" data-t="00:20:13">[00:20:13]</a>.

## User Education and Discovery
Notion recognizes the "blank canvas problem" where users may struggle to know how to interact with AI <a class="yt-timestamp" data-t="00:40:40">[00:40:40]</a>. Pre-built prompts help overcome this by showing possibilities, getting "creative juices flowing" <a class="yt-timestamp" data-t="00:21:09">[00:21:09]</a>. Notion considers suggesting different types of revisions based on what the user is working on, or after AI has generated something, to reduce the "mental work" of coming up with a prompt <a class="yt-timestamp" data-t="00:22:12">[00:22:12]</a>.

## Challenges in Understanding User Patterns
Despite extensive internal testing, Notion encounters diverse user patterns and [[challenges_in_deploying_ai_in_notion | challenges in deploying AI in Notion]]:

*   **Varied User Demographics:** Notion's internal usage might not be fully representative of all users, which include individuals, students, and organizations with diverse ways of using the product (e.g., some still use Google Docs in addition to Notion) <a class="yt-timestamp" data-t="00:17:24">[00:17:24]</a>.
*   **"Meta" Questions in Q&A:** A challenge with Notion Q&A was anticipating users asking "meta questions" about Notion itself, such as "How can I share this page with Jack?" or "How many people are in my workspace?" <a class="yt-timestamp" data-t="00:24:19">[00:24:19]</a>. These questions are not answered by content within a user's workspace <a class="yt-timestamp" data-t="00:24:24">[00:24:24]</a>.
*   **Temporal Queries:** Another challenge was handling questions involving time ranges, like "What is the marketing team working on this week?" <a class="yt-timestamp" data-t="00:24:47">[00:24:47]</a>. Such queries require the AI to understand continuous updates over time rather than just looking at static documents <a class="yt-timestamp" data-t="00:24:57">[00:24:57]</a>.

These complexities highlight the need for sophisticated evaluation methods and internal tools to understand and address the "fuzzy boundary" of what the model should be able to do <a class="yt-timestamp" data-t="00:24:01">[00:24:01]</a>.