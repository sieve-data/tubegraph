---
title: Effective strategies for using Windsurf in coding
videoId: ukhe1013Jpk
---

From: [[colemedin]] <br/> 

[[introduction_to_windsurf_as_an_ai_ide | Windsurf]] is considered by some to be the premier [[ai_ides_and_platforms|AI IDE]], distinguishing itself by combining the collaborative ease of a co-pilot with the advanced capabilities of an agent for long-running and complex coding tasks <a class="yt-timestamp" data-t="00:00:02">[00:00:02]</a>. It's designed to keep developers in a "Flow State," fostering a cohesive experience where the AI agent is deeply integrated into the coding process <a class="yt-timestamp" data-t="00:02:03">[00:02:03]</a>. This means a synced timeline between the developer and the AI, allowing awareness of all changes made by both parties <a class="yt-timestamp" data-t="00:04:06">[00:04:06]</a>.

While Windsurf offers significant time savings and enhances code quality <a class="yt-timestamp" data-t="00:01:07">[00:01:07]</a>, it's not a perfect platform and still requires substantial coding knowledge to produce production-ready code <a class="yt-timestamp" data-t="00:01:04">[00:01:04]</a>.

## General Application Building Workflow

A recommended workflow for building applications with [[ai_coding_assistants_and_how_to_use_them_effectively|AI coding assistants]] involves a multi-tool approach:
*   **Initial Front-End Development**: Begin by building the initial front-end with tools like AutoDev or Bolt.new, as they excel in this area <a class="yt-timestamp" data-t="00:04:42">[00:04:42]</a>. Continue using them until the project encounters a snag <a class="yt-timestamp" data-t="00:04:51">[00:04:51]</a>.
*   **Transition to Windsurf**: Export the project and import it into Windsurf to add finishing touches and handle backend elements <a class="yt-timestamp" data-t="00:04:55">[00:04:55]</a>. Windsurf is particularly strong with Python coding and database management <a class="yt-timestamp" data-t="00:05:01">[00:05:01]</a>.

## [[troubleshooting_and_optimizing_workflows_with_windsurf | Troubleshooting and Optimizing Workflows with Windsurf]]

### Managing Long Conversations
Large Language Models (LLMs) can become confused and "hallucinate" in lengthy conversations <a class="yt-timestamp" data-t="00:08:31">[00:08:31]</a>.
*   **Start a New Conversation**: When Windsurf (or the underlying LLM like Claude 3.5 Sonnet) starts to hallucinate, it's best to start a brand new conversation <a class="yt-timestamp" data-t="00:08:52">[00:08:52]</a>. While this means losing some context, re-explaining the issue briefly will save significant time by eliminating hallucinations <a class="yt-timestamp" data-t="00:09:02">[00:09:02]</a>.

### Prioritizing Requests
Avoid overwhelming the AI with too many requests at once <a class="yt-timestamp" data-t="00:09:23">[00:09:23]</a>.
*   **One Request at a Time**: It's much more effective to give Windsurf one request at a time <a class="yt-timestamp" data-t="00:09:42">[00:09:42]</a>. Implement each change, ensure it's correct, and then move on to the next <a class="yt-timestamp" data-t="00:09:59">[00:09:59]</a>. This patience leads to better results and ultimately saves time <a class="yt-timestamp" data-t="00:10:07">[00:10:07]</a>.

### Leveraging Accept/Reject Features
Windsurf implements changes in the code *before* you formally accept them, allowing for testing <a class="yt-timestamp" data-t="00:10:28">[00:10:28]</a>.
*   **Test Before Accepting**: You can test the changes in your application before accepting or rejecting them <a class="yt-timestamp" data-t="00:10:37">[00:10:37]</a>. If a change doesn't work or isn't desired, you can easily reject it within Windsurf, which handles the revert <a class="yt-timestamp" data-t="00:10:54">[00:10:54]</a>.
*   **Selective Acceptance/Rejection**: Utilize the ability to accept or reject specific changes across different files <a class="yt-timestamp" data-t="00:11:14">[00:11:14]</a>. If the AI gets some things right but others wrong, you can reject only the problematic parts before accepting the rest <a class="yt-timestamp" data-t="00:11:28">[00:11:28]</a>. This ensures the AI knows what was rejected for future corrections <a class="yt-timestamp" data-t="00:11:59">[00:11:59]</a>.

### External AI Assistance
*   **Using 01.ai**: When Windsurf struggles with a specific problem, especially if Claude 3.5 Sonnet is confused, consider using 01.ai <a class="yt-timestamp" data-t="00:14:26">[00:14:26]</a>. Paste your code, describe the issue and error, get the fix from 01.ai, apply it manually, and then continue in Windsurf. The "Flow State" ensures Windsurf recognizes your manual changes <a class="yt-timestamp" data-t="00:15:04">[00:15:04]</a>.

## [[recommended_techniques_for_prompt_engineering | Recommended Techniques for Prompt Engineering]]

### Specificity in Prompts
*   **Call Out Files/Functions**: Use the "@" symbol to call out specific files or functions, guiding the AI to exactly what you're referring to <a class="yt-timestamp" data-t="00:12:10">[00:12:10]</a>. This prevents the AI from hallucinating or editing the wrong files <a class="yt-timestamp" data-t="00:12:54">[00:12:54]</a>.
*   **Define Tech Stack**: At the start of application creation, define your tech stack, programming languages, and technologies explicitly <a class="yt-timestamp" data-t="00:13:31">[00:13:31]</a>. Provide specific details about the API endpoint, database type, and schema <a class="yt-timestamp" data-t="00:13:54">[00:13:54]</a>. This ensures the AI acts as a true co-pilot rather than "doing its own thing" <a class="yt-timestamp" data-t="00:14:13">[00:14:13]</a>.

## Leveraging Windsurf's Built-in Features

### Directed Code Changes
*   **Refactor Button**: For focused changes, click on the specific function or class you want to modify, and use the "Refactor" button <a class="yt-timestamp" data-t="00:15:30">[00:15:30]</a>. You can use predefined options or type custom instructions, which will only apply to the selected function, ensuring a very focused context <a class="yt-timestamp" data-t="00:15:41">[00:15:41]</a>.

### Code Understanding
*   **Explain Button**: To understand a specific function, whether it's AI-generated or imported from another project, select the function and click "Explain" <a class="yt-timestamp" data-t="00:16:00">[00:16:00]</a>. This provides a clear explanation of that particular code segment <a class="yt-timestamp" data-t="00:16:11">[00:16:11]</a>.

## Documentation and Testing

### Code Documentation
*   **Documenting Code**: Windsurf excels at generating code documentation, saving significant time <a class="yt-timestamp" data-t="00:16:24">[00:16:24]</a>. You can prompt it to document specific functions, files, or even the entire project <a class="yt-timestamp" data-t="00:16:48">[00:16:48]</a>.
*   **Prevent Unwanted Code Updates**: When asking for documentation, explicitly tell Windsurf *not* to update the code in any other way <a class="yt-timestamp" data-t="00:17:00">[00:17:00]</a>. This ensures it focuses solely on adding comments and docstrings without altering existing logic <a class="yt-timestamp" data-t="00:17:40">[00:17:40]</a>.

### Test Generation
*   **Writing Tests**: Windsurf is highly beneficial for writing tests, a critical but often annoying part of development <a class="yt-timestamp" data-t="00:17:53">[00:17:53]</a>. It helps set up boilerplate code for libraries like Jest, React Testing Library, or Pytest, saving hours of configuration <a class="yt-timestamp" data-t="00:18:16">[00:18:16]</a>. While AI-generated tests may not work perfectly initially, they provide a strong foundation for tweaking <a class="yt-timestamp" data-t="00:18:14">[00:18:14]</a>.

## The Future of [[ai_ides_and_platforms|AI IDEs]]
The potential for [[ai_ides_and_platforms|AI IDEs]] like Windsurf is immense. The future likely holds fully agentic IDEs running locally with full access to a computer's resources, capable of researching library documentation, and deploying built applications autonomously <a class="yt-timestamp" data-t="00:18:53">[00:18:53]</a>.