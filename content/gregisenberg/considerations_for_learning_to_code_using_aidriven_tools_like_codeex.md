---
title: Considerations for learning to code using AIdriven tools like Codeex
videoId: B0IvHPnwPx0
---

From: [[gregisenberg]] <br/> 

OpenAI's Codeex is an AI engineer in the browser designed to help users, including non-technical individuals, generate and manage code [00:00:00]. It allows users to type in a task, which the AI then codes and pushes to GitHub [00:01:40].

## Why Use Codeex for Learning?

While Codeex might initially seem overwhelming to non-technical users compared to prototyping tools like Bolt [00:11:00], it offers a unique approach to learning and building:

*   **Abstraction from Code**: Codeex allows users to build without directly looking at or thinking about the code [00:12:16]. The user provides a task, and Codeex handles the underlying coding [00:12:31].
*   **Iterative Development**: Unlike text-to-app builders that might create an "overbuilt" but under-functional application [00:13:06], Codeex supports iteratively adding features. This means each new addition technically includes tests and checks, reducing time spent debugging [00:13:49].
*   **Automated Processes**: Tasks are delegated to an AI agent [00:14:51], and future automation could even handle processes like merging pull requests without direct user intervention [00:15:01].
*   **Accessibility**: Codeex is accessible on mobile devices through chat, making it possible to "ship all the time" [00:12:48].
*   **Introduction to Development Concepts**: Using Codeex can serve as a "lightweight way to learn how to code" [00:32:14], introducing users to computer science and development terminology in a more engaging manner [00:32:23]. It can "drip feeds" coding knowledge by integrating with essential development tools like GitHub [00:33:36].

## Getting Started with Codeex

For non-technical users exploring Codeex, the initial setup involves connecting to GitHub [00:02:57]:

### Understanding GitHub
[[introduction_to_openais_codeex_and_its_use_for_nontechnical_users | GitHub]] is a platform for storing and managing code [00:03:03]. It organizes code into "repositories" (repos), which are essentially projects [00:03:16]. Changes made to the code are recorded as "commits" [00:03:29].

### Setting up a Repository
To start a new project (e.g., a personal site or marketing site), you must create a new repository on GitHub [00:04:01]. You can name it, choose between public or private, and add a "readme" file to explain the project [00:04:14].

### Initial Site Creation
A website can be created with Codeex from scratch, or an existing site built on a no-code tool like Card can be converted [00:04:41]. This involves viewing the page source code from the no-code builder, copying it, and using a coding agent (like Codeex) to put it onto a GitHub repo [00:05:05].

### Deployment
Once the code is on GitHub, it can be deployed to make the website live [00:05:32]. Options include GitHub Pages or Vercel [00:05:37].

## Core Workflow

The typical workflow in Codeex for modifying a website:

1.  **Add a Task**: Input a command or request, such as "add another tab next to investments tools that is called food. I like in the dock. put tacos" [00:06:02].
2.  **Generate Code**: Click "Code" to initiate the AI's coding process [00:06:17]. Codeex uses the terminal to find files and understand the existing codebase [00:06:43].
3.  **Review Changes**: Codeex shows the files it intends to change and summarizes its plan (e.g., creating new documents, updating the main site) [00:07:23]. It also indicates how many lines of code were added or removed [00:08:12].
4.  **Create a Pull Request (PR)**: To apply changes, create a new Pull Request [00:09:15]. A PR involves creating a "branch" (a copy of the main code) where changes are made. If there are no conflicts, the changes can be "merged" back into the main branch [00:09:27].
5.  **Merge and Deploy**: If checks pass and there are no conflicts, the PR can be merged [00:10:11]. The changes will then deploy and become visible on the live site [00:10:29].

Codeex also includes an internal testing feature, but it may be more technical than needed for basic workflows [00:08:42].

## Limitations and Challenges

Despite its benefits, Codeex and similar [[current_limitations_and_future_potential_of_ai_coding_tools | AI coding tools]] present challenges for non-technical users:

*   **Overwhelm**: The initial setup and terminology (GitHub, repositories, commits, branches, pull requests) can be daunting [00:11:00], making the process feel "10 times more overwhelming" than simpler prototyping tools [00:32:01].
*   **Complexity**: Codeex struggles with complex tasks like user interfaces ("make the UI look like this") [00:21:00], file uploads (images) [00:20:58], databases, or authentication [00:24:12].
*   **Technical Environment Setup**: For more advanced projects involving frameworks like Next.js or Python, users may need to run terminal commands (e.g., `pmpm install`) within Codeex's environment, which can be confusing for those without a technical background [00:28:28].
*   **Early Stage**: As an early preview tool [00:15:20], Codeex may have limitations, such as tasks breaking after 30 minutes [00:15:16].

## Best Practices for Learning and Use

For non-technical users looking to learn and effectively use Codeex:

*   **Start Simple**: Begin with a personal site or create a new, non-critical site [00:18:38]. Basic tasks include making a website with a name as the header, adding an about section, or social links [00:19:38].
*   **Iterate Gradually**: Add features line by line or piece by piece, rather than attempting a large, complex project like a "Spotify clone" all at once [00:19:02], [00:31:39].
*   **Leverage GitHub's Version Control**: If a change breaks the site, GitHub allows you to revert to a previous working version, minimizing risk for personal projects [00:20:08].
*   **Use External AI for Support**: When encountering difficulties or needing to understand Git concepts, ask general purpose AI tools like ChatGPT for help. This can involve copying large blocks of code for analysis [00:22:09], [00:20:48].
*   **Explore Open-Source Projects**: GitHub hosts many open-source repositories that can be forked (copied) and modified using Codeex, providing real-world examples and learning opportunities [00:25:33].
*   **Manage Expectations**: Understand that Codeex "drip feeds" coding exposure rather than instantly making you a developer [00:33:36]. It's a tool to get "curious enough to go past those barriers" of traditional coding [00:31:22].

Using Codeex allows non-technical users to experience the entire development loop—from writing a task to seeing changes live on a site—without needing to write a single line of code themselves [00:17:03].